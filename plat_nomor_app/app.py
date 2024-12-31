from flask import Flask, render_template, request

app = Flask(__name__)

# Daftar kode plat nomor kendaraan dan daerah
kode_plat = {
    "A": "Banten", "AA": "Kediri", "AB": "Yogyakarta", "AD": "Surakarta", "AE": "Madiun", "AG": "Kediri",
    "B": "Jakarta", "BA": "Sumatera Barat", "BB": "Sumatera Utara (Tapanuli)", "BD": "Sumatera Utara (Sibolga)",
    "BE": "Lampung", "BG": "Sumatera Selatan", "BH": "Jambi", "BK": "Sumatera Utara (Medan)", "BL": "Aceh",
    "BM": "Riau", "BN": "Bangka Belitung", "BP": "Kepulauan Riau", "CC": "Bali", "CD": "Kalimantan Selatan",
    "CE": "Kalimantan Timur", "CG": "Kalimantan Tengah", "CH": "Kalimantan Barat", "CK": "Kalimantan Utara",
    "D": "Bandung", "DA": "Kalimantan Selatan (Banjarmasin)", "DB": "Sulawesi Utara (Manado)", "DC": "Sulawesi Barat",
    "DD": "Sulawesi Selatan (Makassar)", "DE": "Maluku", "DG": "Maluku Utara", "DH": "Nusa Tenggara Timur (Kupang)",
    "DK": "Bali", "DL": "Sulawesi Utara (Gorontalo)", "DM": "Sulawesi Tengah", "DN": "Sulawesi Tenggara",
    "DP": "Sulawesi Selatan (Parepare)", "DR": "Nusa Tenggara Barat (Mataram)", "DS": "Papua Barat", "DT": "Papua",
    "E": "Cirebon", "EA": "Nusa Tenggara Timur", "EB": "Nusa Tenggara Timur (Ende)", "ED": "Nusa Tenggara Timur (Maumere)",
    "F": "Bogor", "G": "Pekalongan", "H": "Semarang", "K": "Pati", "KB": "Kalimantan Barat (Pontianak)",
    "KH": "Kalimantan Tengah (Palangkaraya)", "KT": "Kalimantan Timur (Samarinda)", "L": "Surabaya", "M": "Madura",
    "N": "Malang", "P": "Jember", "PA": "Kalimantan Barat (Singkawang)", "PB": "Kalimantan Barat (Sintang)",
    "R": "Banyuwangi", "S": "Bojonegoro", "T": "Ngawi", "W": "Sidoarjo", "Z": "Kediri"
}

# Fungsi untuk mengklasifikasikan plat nomor
def klasifikasi_plat_nomor(plat_nomor):
    plat_nomor = plat_nomor.strip().upper()  # Hapus spasi dan ubah ke huruf kapital

    # Cek apakah panjang plat nomor tepat 1 atau 2 karakter
    if len(plat_nomor) < 1 or len(plat_nomor) > 2:
        return "Kode plat tidak dikenal"
    
    # Cek apakah kode ada dalam daftar
    if plat_nomor in kode_plat:
        return kode_plat[plat_nomor]
    
    return "Kode plat tidak dikenal"

@app.route("/", methods=["GET", "POST"])
def index():
    daerah = ""
    if request.method == "POST":
        plat_nomor_input = request.form["plat_nomor"]
        daerah = klasifikasi_plat_nomor(plat_nomor_input)
    return render_template("index.html", daerah=daerah)

if __name__ == "__main__":
    app.run(debug=True)
