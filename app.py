from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import os
from knowledge_base import (
    FACTS, QUESTIONS, CONCLUSIONS,
    get_next_question, run_inference, get_judul_deskripsi
)

app = Flask(__name__)
app.secret_key = os.urandom(24)


# ─────────────────────────────────────────────────────────
# [1] HALAMAN UTAMA
# ─────────────────────────────────────────────────────────
@app.route("/")
def index():
    session.clear()
    return render_template("index.html")


# ─────────────────────────────────────────────────────────
# [2] INPUT DATA — form data umum wajib pajak
# ─────────────────────────────────────────────────────────
@app.route("/input-data", methods=["GET", "POST"])
def input_data():
    if request.method == "POST":
        session["profil_umum"] = {
            "nama":  request.form.get("nama", "").strip() or "Wajib Pajak",
            "tahun": request.form.get("tahun", "2024").strip(),
        }
        return redirect(url_for("input_profil"))
    return render_template("input_data.html")


# ─────────────────────────────────────────────────────────
# [3] INPUT PROFIL AWAL — pre-fill fakta dasar dari form
# ─────────────────────────────────────────────────────────
@app.route("/input-profil", methods=["GET", "POST"])
def input_profil():
    if "profil_umum" not in session:
        return redirect(url_for("input_data"))

    if request.method == "POST":
        answered = {}
        history  = []

        # F01 — selalu orang pribadi
        answered["F01"] = "ya"
        history.append({"fid":"F01","fakta":FACTS["F01"],"pertanyaan":QUESTIONS["F01"],"jawaban":"ya"})

        # F05 — WNA/WNI
        kewarganegaraan = request.form.get("kewarganegaraan", "wni")
        answered["F05"] = "ya" if kewarganegaraan == "wna" else "tidak"
        history.append({"fid":"F05","fakta":FACTS["F05"],"pertanyaan":QUESTIONS["F05"],"jawaban":answered["F05"]})

        # F02 — domisili di Indonesia
        domisili = request.form.get("domisili", "ya")
        answered["F02"] = domisili
        history.append({"fid":"F02","fakta":FACTS["F02"],"pertanyaan":QUESTIONS["F02"],"jawaban":domisili})

        # F22/F23 — status kawin
        status_kawin = request.form.get("status_kawin", "lajang")
        if status_kawin == "lajang":
            answered["F22"] = "ya"
            answered["F23"] = "tidak"
        else:
            answered["F22"] = "tidak"
            answered["F23"] = "ya"
        history.append({"fid":"F22","fakta":FACTS["F22"],"pertanyaan":QUESTIONS["F22"],"jawaban":answered["F22"]})
        history.append({"fid":"F23","fakta":FACTS["F23"],"pertanyaan":QUESTIONS["F23"],"jawaban":answered["F23"]})

        session["answered"] = answered
        session["history"]  = history
        return redirect(url_for("mulai_konsultasi"))

    return render_template("input_profil.html", profil=session.get("profil_umum", {}))


# ─────────────────────────────────────────────────────────
# [4] MULAI KONSULTASI — halaman penghubung
# ─────────────────────────────────────────────────────────
@app.route("/mulai-konsultasi")
def mulai_konsultasi():
    if "answered" not in session:
        return redirect(url_for("input_data"))
    return render_template("mulai_konsultasi.html", profil=session.get("profil_umum", {}))


# ─────────────────────────────────────────────────────────
# [5] KONSULTASI — loop forward chaining
#     Menampilkan Pernyataan Fakta → cek Perlu Data Tambahan?
#     Ya  → tampilkan fakta berikutnya
#     Tidak → redirect ke Penarikan Kesimpulan
# ─────────────────────────────────────────────────────────
@app.route("/konsultasi", methods=["GET"])
def konsultasi():
    if "answered" not in session:
        return redirect(url_for("input_data"))

    answered = session["answered"]
    profil_fids = {"F01", "F02", "F05", "F22", "F23"}

    # Forward Chaining: perlu data tambahan?
    next_fid = get_next_question(answered)
    if next_fid is None:
        return redirect(url_for("hasil"))   # Tidak → Penarikan Kesimpulan

    # Ya → tampilkan pernyataan fakta berikutnya
    total_dinamis = len([f for f in QUESTIONS if f not in profil_fids])
    sudah = len([f for f in answered if f not in profil_fids])
    persen = min(int((sudah / max(total_dinamis, 1)) * 100), 99)

    return render_template(
        "konsultasi.html",
        fid=next_fid,
        pernyataan=FACTS[next_fid],
        pertanyaan=QUESTIONS[next_fid],
        nomor=sudah + 1,
        total=total_dinamis,
        persen=persen,
        history=session.get("history", []),
        profil=session.get("profil_umum", {}),
    )


# ─────────────────────────────────────────────────────────
# [6] INPUT JAWABAN → Forward Chaining → cek perlu tambahan
# ─────────────────────────────────────────────────────────
@app.route("/jawab", methods=["POST"])
def jawab():
    fid = request.form.get("fid")
    jwb = request.form.get("jawab")

    if not fid or jwb not in ("ya", "tidak"):
        return redirect(url_for("konsultasi"))

    answered = session.get("answered", {})
    history  = session.get("history",  [])

    answered[fid] = jwb
    history.append({"fid":fid,"fakta":FACTS[fid],"pertanyaan":QUESTIONS[fid],"jawaban":jwb})

    session["answered"] = answered
    session["history"]  = history

    # Forward Chaining — perlu data tambahan?
    next_fid = get_next_question(answered)
    if next_fid is None:
        return redirect(url_for("hasil"))   # Tidak → Penarikan Kesimpulan

    return redirect(url_for("konsultasi"))  # Ya → loop


# ─────────────────────────────────────────────────────────
# [7] KEMBALI
# ─────────────────────────────────────────────────────────
@app.route("/kembali", methods=["POST"])
def kembali():
    profil_fids = {"F01", "F02", "F05", "F22", "F23"}
    history  = session.get("history", [])
    answered = session.get("answered", {})

    dinamis = [h for h in history if h["fid"] not in profil_fids]
    if dinamis:
        target = dinamis[-1]
        history.remove(target)
        answered.pop(target["fid"], None)
        session["history"]  = history
        session["answered"] = answered

    return redirect(url_for("konsultasi"))


# ─────────────────────────────────────────────────────────
# [8] PENARIKAN KESIMPULAN / SELESAI
# ─────────────────────────────────────────────────────────
@app.route("/hasil")
def hasil():
    answered = session.get("answered", {})
    if not answered:
        return redirect(url_for("index"))

    # run_inference sekarang mereturn list of dict: [{"kode": "K05", "pemicu": ["F14", "F25"]}, ...]
    inference_results = run_inference(answered)
    
    kesimpulan_list = []
    for item in inference_results:
        kode = item["kode"]
        pemicu = item.get("pemicu", [])
        
        if kode in CONCLUSIONS:
            # Copy data default dari CONCLUSIONS (untuk warna, dasar_hukum, tipe, dll)
            kes_data = CONCLUSIONS[kode].copy()
            
            # Dapatkan judul dan deskripsi dinamis berdasarkan pemicu
            judul_dinamis, deskripsi_dinamis = get_judul_deskripsi(kode, pemicu)
            
            # Update data dengan nilai dinamis
            kes_data["kode"] = kode
            kes_data["judul"] = judul_dinamis
            kes_data["deskripsi"] = deskripsi_dinamis
            
            kesimpulan_list.append(kes_data)

    grouped = {}
    tipe_label = {
        "subjek": "Status Subjek Pajak",
        "objek":  "Klasifikasi Objek Pajak",
        "ptkp":   "Penghasilan Tidak Kena Pajak (PTKP)",
        "pph":    "Kewajiban PPh Terutang",
    }
    for item in kesimpulan_list:
        grouped.setdefault(item.get("tipe"), []).append(item)

    return render_template(
        "hasil.html",
        grouped=grouped,
        tipe_label=tipe_label,
        history=session.get("history", []),
        profil=session.get("profil_umum", {}),
        total_jawaban=len(session.get("history", [])),
        total_kesimpulan=len(kesimpulan_list),
    )


# ─────────────────────────────────────────────────────────
# [9] RESET
# ─────────────────────────────────────────────────────────
@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))

@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("input_data"))


# ─────────────────────────────────────────────────────────
# [10] API
# ─────────────────────────────────────────────────────────
@app.route("/api/infer", methods=["POST"])
def api_infer():
    data = request.get_json()
    if not data or "answered" not in data:
        return jsonify({"error": "Field 'answered' diperlukan"}), 400
    ids    = run_inference(data["answered"])
    result = [{"kode":k,**CONCLUSIONS[k]} for k in ids if k in CONCLUSIONS]
    return jsonify({"kesimpulan": result, "total": len(result)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)