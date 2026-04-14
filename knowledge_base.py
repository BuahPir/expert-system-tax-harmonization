# ============================================================
# BASIS PENGETAHUAN — Sistem Pakar PPh Orang Pribadi
# Sumber: UU No. 7 Tahun 2021 tentang Harmonisasi Peraturan
#         Perpajakan (UU HPP)
# ============================================================

# ----------------------------------------------------------
# DAFTAR FAKTA (F01 – F29)
# ----------------------------------------------------------
FACTS = {
    "F01": "Pengguna adalah orang pribadi (bukan badan usaha)",
    "F02": "Pengguna bertempat tinggal di Indonesia",
    "F03": "Pengguna berada di Indonesia lebih dari 183 hari dalam 12 bulan",
    "F04": "Pengguna berniat bertempat tinggal di Indonesia",
    "F05": "Pengguna adalah Warga Negara Asing (WNA)",
    "F06": "WNA memiliki keahlian tertentu sesuai peraturan perundang-undangan",
    "F07": "WNA telah menjadi subjek pajak dalam negeri kurang dari 4 tahun pajak",
    "F08": "Pengguna menerima/memperoleh penghasilan dari Indonesia",
    "F09": "Pengguna menerima/memperoleh penghasilan dari luar Indonesia",
    "F10": "Pengguna tidak bertempat tinggal di Indonesia",
    "F11": "Pengguna berada di Indonesia kurang dari 183 hari dalam 12 bulan",
    "F12": "Pengguna adalah ahli waris dari warisan yang belum terbagi",
    "F13": "Warisan belum terbagi dan masih menghasilkan penghasilan",
    "F14": "Pengguna memiliki penghasilan dari pekerjaan/jasa/gaji/upah",
    "F15": "Pengguna memiliki penghasilan dari usaha/kegiatan bebas",
    "F16": "Pengguna memiliki penghasilan dari modal (bunga, dividen, royalti, sewa)",
    "F17": "Pengguna menerima warisan",
    "F18": "Pengguna menerima hibah dari keluarga sedarah garis lurus satu derajat",
    "F19": "Pengguna menerima bantuan/sumbangan/zakat dari lembaga resmi pemerintah",
    "F20": "Pengguna memiliki peredaran bruto ≤ Rp500.000.000 dalam satu tahun pajak",
    "F21": "Pengguna menerima dividen dari dalam negeri dan diinvestasikan kembali di NKRI",
    "F22": "Pengguna berstatus lajang (tidak kawin, tanpa tanggungan)",
    "F23": "Pengguna berstatus kawin",
    "F24": "Pengguna memiliki tanggungan keluarga (maksimal 3 orang)",
    "F25": "Pengguna menerima penghasilan dalam bentuk natura/kenikmatan dari pemberi kerja",
    "F26": "Pengguna menerima penghasilan berupa bunga deposito/tabungan",
    "F27": "Pengguna menerima penghasilan dari transaksi saham di bursa efek",
    "F28": "Pengguna menerima penghasilan dari pengalihan tanah dan/atau bangunan",
    "F29": "Pengguna memiliki penghasilan kena pajak dalam setahun",
}

# ----------------------------------------------------------
# PERTANYAAN PER FAKTA (ditampilkan ke pengguna)
# ----------------------------------------------------------
QUESTIONS = {
    "F01": "Apakah Anda adalah orang pribadi (bukan badan usaha/perusahaan)?",
    "F02": "Apakah Anda bertempat tinggal di Indonesia?",
    "F03": "Apakah Anda berada di Indonesia lebih dari 183 hari dalam 12 bulan terakhir?",
    "F04": "Apakah Anda berniat/berencana untuk bertempat tinggal di Indonesia?",
    "F05": "Apakah Anda adalah Warga Negara Asing (WNA)?",
    "F06": "Apakah Anda memiliki keahlian tertentu yang diakui sesuai peraturan perundang-undangan?",
    "F07": "Apakah Anda baru menjadi subjek pajak dalam negeri kurang dari 4 tahun pajak?",
    "F08": "Apakah Anda menerima atau memperoleh penghasilan yang bersumber dari Indonesia?",
    "F09": "Apakah Anda menerima atau memperoleh penghasilan dari luar Indonesia?",
    "F10": "Apakah Anda tidak bertempat tinggal di Indonesia?",
    "F11": "Apakah Anda berada di Indonesia kurang dari 183 hari dalam 12 bulan?",
    "F12": "Apakah Anda merupakan ahli waris dari suatu warisan yang belum dibagikan (belum terbagi)?",
    "F13": "Apakah warisan yang belum terbagi tersebut masih menghasilkan penghasilan (misalnya dari sewa, usaha, dll)?",
    "F14": "Apakah Anda memiliki penghasilan dari pekerjaan, jasa, gaji, atau upah?",
    "F15": "Apakah Anda memiliki penghasilan dari usaha sendiri atau kegiatan bebas (freelance, wiraswasta)?",
    "F16": "Apakah Anda memiliki penghasilan dari modal seperti bunga, dividen, royalti, atau sewa?",
    "F17": "Apakah Anda menerima warisan dari pewaris?",
    "F18": "Apakah Anda menerima hibah dari anggota keluarga sedarah dalam garis keturunan lurus satu derajat (orang tua atau anak kandung)?",
    "F19": "Apakah Anda menerima bantuan, sumbangan, atau zakat dari lembaga resmi yang diakui pemerintah?",
    "F20": "Apakah total peredaran bruto usaha Anda tidak melebihi Rp500.000.000 dalam satu tahun pajak?",
    "F21": "Apakah Anda menerima dividen dari dalam negeri dan dividen tersebut diinvestasikan kembali di wilayah NKRI?",
    "F22": "Apakah status perkawinan Anda saat ini lajang (belum/tidak kawin) dan tidak memiliki tanggungan?",
    "F23": "Apakah Anda berstatus kawin?",
    "F24": "Apakah Anda memiliki tanggungan keluarga (anak/anggota keluarga yang sepenuhnya menjadi tanggungan, maks 3 orang)?",
    "F25": "Apakah Anda menerima penghasilan dalam bentuk natura atau kenikmatan dari pemberi kerja (misalnya fasilitas perumahan, kendaraan, makan siang kantor)?",
    "F26": "Apakah Anda menerima penghasilan berupa bunga deposito atau bunga tabungan dari bank?",
    "F27": "Apakah Anda menerima penghasilan dari transaksi saham atau sekuritas di bursa efek?",
    "F28": "Apakah Anda menerima penghasilan dari pengalihan (jual/hibah) tanah dan/atau bangunan?",
    "F29": "Setelah dikurangi PTKP, apakah Anda masih memiliki Penghasilan Kena Pajak (PKP) yang positif?",
}

# ----------------------------------------------------------
# KESIMPULAN (K01 – K12)
# ----------------------------------------------------------
CONCLUSIONS = {
    "K01": {
        "judul": "Subjek Pajak Dalam Negeri",
        "deskripsi": "Anda tergolong sebagai Subjek Pajak Orang Pribadi Dalam Negeri. Anda wajib melaporkan seluruh penghasilan, baik yang diperoleh dari dalam maupun luar Indonesia, dalam Surat Pemberitahuan (SPT) Tahunan.",
        "dasar_hukum": "Pasal 2 ayat (1) UU PPh jo. UU HPP No. 7/2021",
        "tipe": "subjek",
        "warna": "blue",
    },
    "K02": {
        "judul": "Subjek Pajak Luar Negeri",
        "deskripsi": "Anda tergolong sebagai Subjek Pajak Orang Pribadi Luar Negeri. Pengenaan PPh hanya berlaku atas penghasilan yang bersumber dari Indonesia.",
        "dasar_hukum": "Pasal 2 ayat (4) UU PPh jo. UU HPP No. 7/2021",
        "tipe": "subjek",
        "warna": "orange",
    },
    "K03": {
        "judul": "WNA dengan Fasilitas Pengecualian (4 Tahun Pertama)",
        "deskripsi": "Anda adalah WNA dengan keahlian tertentu yang baru menjadi subjek pajak dalam negeri. Selama 4 tahun pajak pertama, PPh hanya dikenakan atas penghasilan yang diterima atau diperoleh dari Indonesia.",
        "dasar_hukum": "Pasal 4 ayat (1a) UU HPP No. 7/2021",
        "tipe": "subjek",
        "warna": "purple",
    },
    "K04": {
        "judul": "Warisan Belum Terbagi sebagai Subjek Pajak Pengganti",
        "deskripsi": "Warisan yang belum terbagi ditetapkan sebagai subjek pajak pengganti. Kewajiban perpajakan atas penghasilan yang dihasilkan warisan tersebut menjadi tanggung jawab salah seorang ahli waris, pelaksana wasiat, atau yang mengurus harta peninggalan.",
        "dasar_hukum": "Pasal 32 ayat (1) huruf e UU HPP No. 7/2021",
        "tipe": "subjek",
        "warna": "teal",
    },
    "K05": {
        "judul": "Penghasilan Merupakan Objek PPh",
        "deskripsi": "Penghasilan yang Anda terima merupakan Objek Pajak PPh. Anda wajib melaporkan dan membayar pajak atas penghasilan tersebut sesuai ketentuan yang berlaku.",
        "dasar_hukum": "Pasal 4 ayat (1) UU HPP No. 7/2021",
        "tipe": "objek",
        "warna": "red",
    },
    "K06": {
        "judul": "Penghasilan Bukan Objek PPh",
        "deskripsi": "Penghasilan yang Anda terima dikecualikan dari pengenaan PPh. Anda tidak perlu membayar pajak atas penghasilan tersebut.",
        "dasar_hukum": "Pasal 4 ayat (3) UU HPP No. 7/2021",
        "tipe": "objek",
        "warna": "green",
    },
    "K07": {
        "judul": "Penghasilan Dikenai PPh Final",
        "deskripsi": "Penghasilan yang Anda terima dikenai PPh yang bersifat final. Pajak disetor langsung dan tidak digabungkan ke dalam perhitungan Penghasilan Kena Pajak (PKP) tahunan.",
        "dasar_hukum": "Pasal 4 ayat (2) UU HPP No. 7/2021",
        "tipe": "objek",
        "warna": "orange",
    },
    "K08": {
        "judul": "Tidak Dikenai PPh — UMKM",
        "deskripsi": "Karena peredaran bruto usaha Anda tidak melebihi Rp500.000.000 dalam satu tahun pajak, bagian peredaran bruto tersebut tidak dikenai Pajak Penghasilan.",
        "dasar_hukum": "Pasal 7 ayat (2a) UU HPP No. 7/2021",
        "tipe": "ptkp",
        "warna": "green",
    },
    "K09": {
        "judul": "PTKP TK/0 = Rp54.000.000",
        "deskripsi": "Penghasilan Tidak Kena Pajak (PTKP) Anda sebesar Rp54.000.000 per tahun (status Tidak Kawin / TK/0 tanpa tanggungan).",
        "dasar_hukum": "Pasal 7 ayat (1) huruf a UU HPP No. 7/2021",
        "tipe": "ptkp",
        "warna": "teal",
    },
    "K10": {
        "judul": "PTKP K/0 s.d. K/3 (Status Kawin)",
        "deskripsi": "Penghasilan Tidak Kena Pajak (PTKP) Anda dihitung berdasarkan status kawin dan jumlah tanggungan: Rp54.000.000 (diri sendiri) + Rp4.500.000 (kawin) + Rp4.500.000 × jumlah tanggungan (maks 3 orang).",
        "dasar_hukum": "Pasal 7 ayat (1) huruf a, b, d UU HPP No. 7/2021",
        "tipe": "ptkp",
        "warna": "teal",
    },
    "K11": {
        "judul": "PPh Terutang dengan Tarif Progresif 5%–35%",
        "deskripsi": "Anda memiliki Penghasilan Kena Pajak (PKP) yang terutang PPh dengan tarif progresif sesuai lapisan Pasal 17 UU HPP: 5% (s.d. Rp60 juta), 15% (Rp60–250 juta), 25% (Rp250–500 juta), 30% (Rp500 juta–Rp5 miliar), 35% (di atas Rp5 miliar).",
        "dasar_hukum": "Pasal 17 ayat (1) huruf a UU HPP No. 7/2021",
        "tipe": "pph",
        "warna": "red",
    },
    "K12": {
        "judul": "Tidak Terutang PPh",
        "deskripsi": "Penghasilan Anda setelah dikurangi PTKP menghasilkan PKP ≤ 0, sehingga Anda tidak terutang Pajak Penghasilan untuk tahun pajak ini.",
        "dasar_hukum": "Pasal 7 & 17 UU HPP No. 7/2021",
        "tipe": "pph",
        "warna": "green",
    },
}

# ----------------------------------------------------------
# MESIN INFERENSI — RULES (IF-THEN)
# Format: {"kondisi": [list fakta], "not_kondisi": [fakta yg harus FALSE], "kesimpulan": "Kxx"}
# ----------------------------------------------------------
RULES = [
    # ── Subjek Pajak ──────────────────────────────────────
    {"kondisi": ["F01", "F02"],                         "not_kondisi": [], "kesimpulan": "K01"},
    {"kondisi": ["F01", "F03"],                         "not_kondisi": [], "kesimpulan": "K01"},
    {"kondisi": ["F01", "F04"],                         "not_kondisi": [], "kesimpulan": "K01"},
    {"kondisi": ["F01", "F10", "F11"],                  "not_kondisi": [], "kesimpulan": "K02"},
    {"kondisi": ["F12", "F13"],                         "not_kondisi": [], "kesimpulan": "K04"},
    {"kondisi": ["F05", "F06", "F07"],                  "not_kondisi": [], "kesimpulan": "K03"},

    # ── Objek Pajak (dikenai PPh) ─────────────────────────
    # F14: gaji/upah/jasa — selalu K05, tidak ada konflik
    {"kondisi": ["F01", "F14"],                         "not_kondisi": [], "kesimpulan": "K05"},
    # F15: usaha bebas — K05 hanya jika bruto > 500jt (bukan UMKM)
    {"kondisi": ["F01", "F15"],                         "not_kondisi": ["F20"], "kesimpulan": "K05"},
    # F16: modal (bunga, dividen, royalti, sewa)
    #   → K05 hanya jika TIDAK semua berupa PPh Final (F26/F27/F28)
    #   → K05 hanya jika TIDAK seluruhnya dikecualikan (F21)
    {"kondisi": ["F01", "F16"],                         "not_kondisi": ["F26", "F27", "F28", "F21"], "kesimpulan": "K05"},
    # F25: natura/kenikmatan — K05
    {"kondisi": ["F01", "F25"],                         "not_kondisi": [], "kesimpulan": "K05"},

    # ── Objek Pajak Dikecualikan ──────────────────────────
    # F17: terima warisan → bukan objek pajak
    {"kondisi": ["F01", "F17"],                         "not_kondisi": [], "kesimpulan": "K06"},
    # F18: hibah keluarga sedarah → bukan objek pajak
    {"kondisi": ["F01", "F18"],                         "not_kondisi": [], "kesimpulan": "K06"},
    # F19: bantuan/sumbangan/zakat resmi → bukan objek pajak
    {"kondisi": ["F01", "F19"],                         "not_kondisi": [], "kesimpulan": "K06"},
    # F21: dividen reinvestasi → dikecualikan (bukan K05)
    {"kondisi": ["F01", "F21"],                         "not_kondisi": [], "kesimpulan": "K06"},

    # ── PPh Final ─────────────────────────────────────────
    {"kondisi": ["F01", "F26"],                         "not_kondisi": [], "kesimpulan": "K07"},
    {"kondisi": ["F01", "F27"],                         "not_kondisi": [], "kesimpulan": "K07"},
    {"kondisi": ["F01", "F28"],                         "not_kondisi": [], "kesimpulan": "K07"},

    # ── UMKM ─────────────────────────────────────────────
    {"kondisi": ["F01", "F15", "F20"],                  "not_kondisi": [], "kesimpulan": "K08"},

    # ── PTKP ─────────────────────────────────────────────
    {"kondisi": ["F01", "F22"],                         "not_kondisi": [], "kesimpulan": "K09"},
    {"kondisi": ["F01", "F23"],                         "not_kondisi": [], "kesimpulan": "K10"},
    {"kondisi": ["F01", "F23", "F24"],                  "not_kondisi": [], "kesimpulan": "K10"},

    # ── PPh Terutang / Tidak Terutang ─────────────────────
    {"kondisi": ["F29"],                                "not_kondisi": [], "kesimpulan": "K11"},
]

# Rule K12 ditangani secara khusus di engine (PKP <= 0)
RULE_K12 = {"kondisi_negatif": "F29", "kesimpulan": "K12"}


# ----------------------------------------------------------
# ALUR PERTANYAAN DINAMIS
# Urutan pertanyaan ditentukan berdasarkan jawaban sebelumnya
# ----------------------------------------------------------
def get_next_question(answered: dict) -> str | None:
    """
    Menentukan pertanyaan berikutnya berdasarkan fakta yang sudah dijawab.
    Mengembalikan kode fakta (mis. 'F02') atau None jika konsultasi selesai.
    """
    # F01 selalu pertama
    if "F01" not in answered:
        return "F01"

    # Jika bukan orang pribadi, selesai
    if answered.get("F01") == "tidak":
        return None

    # Pertanyaan dasar kewarganegaraan & domisili
    for fid in ["F05", "F02"]:
        if fid not in answered:
            return fid

    is_wna = answered.get("F05") == "ya"
    tinggal_di_id = answered.get("F02") == "ya"

    if is_wna:
        for fid in ["F06", "F07"]:
            if fid not in answered:
                return fid

    if not tinggal_di_id:
        for fid in ["F03", "F04", "F10", "F11"]:
            if fid not in answered:
                return fid
    else:
        for fid in ["F03", "F04"]:
            if fid not in answered:
                return fid

    # Warisan
    for fid in ["F12"]:
        if fid not in answered:
            return fid
    if answered.get("F12") == "ya" and "F13" not in answered:
        return "F13"

    # Jenis penghasilan
    for fid in ["F14", "F15", "F16", "F25"]:
        if fid not in answered:
            return fid

    if answered.get("F15") == "ya" and "F20" not in answered:
        return "F20"

    # Penghasilan dikecualikan
    for fid in ["F17", "F18", "F19", "F21"]:
        if fid not in answered:
            return fid

    # PPh Final
    for fid in ["F26", "F27", "F28"]:
        if fid not in answered:
            return fid

    # Status kawin & tanggungan
    for fid in ["F22", "F23"]:
        if fid not in answered:
            return fid

    if answered.get("F23") == "ya" and "F24" not in answered:
        return "F24"

    # PKP
    if "F29" not in answered:
        return "F29"

    return None  # Semua sudah dijawab


def run_inference(answered: dict) -> list:
    """
    Menjalankan forward chaining berdasarkan fakta yang sudah dikonfirmasi.
    Mengembalikan list kode kesimpulan yang terpenuhi.
    """
    # Buat set fakta yang bernilai TRUE
    true_facts = {fid for fid, val in answered.items() if val == "ya"}
    results = []
    seen = set()

    for rule in RULES:
        cond_ok  = all(f in true_facts for f in rule["kondisi"])
        not_ok   = all(f not in true_facts for f in rule["not_kondisi"])
        k = rule["kesimpulan"]
        if cond_ok and not_ok and k not in seen:
            results.append(k)
            seen.add(k)

    # K12: PKP <= 0
    if "F29" in answered and answered["F29"] == "tidak" and "K12" not in seen:
        results.append("K12")
        seen.add("K12")

    return results