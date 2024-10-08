# Rule.py
corn_diseases = {
    "Bulai": "P001",
    "Blight": "P002",
    "Leaf Rust": "P003",
    "Burn": "P004",
    "Stem Borer": "P005",
    "Cob Borer": "P006",
}

symptoms = {
    "P001": ["G1", "G2", "G3", "G4", "G5"],
    "P002": ["G5", "G6", "G7", "G8", "G9", "G10"],
    "P003": ["G10", "G11", "G12", "G13", "G14"],
    "P004": ["G15", "G16", "G17", "G18", "G19"],
    "P005": ["G20", "G21", "G22", "G23", "G24", "G25", "G26", "G27"],
    "P006": ["G28", "G29", "G30", "G31"],
}

symptoms_name = {
    "G1" : "Daun berwarna klorosis",
    "G2" : "Mengalami keterbelakangan pertumbuhan",
    "G3" : "Warna putihnya seperti tepung pada permukaan atas dan bawah daun yang bersifat klorosis",
    "G4" : "Daun melengkung dan dipelintir",
    "G5" : "Gangguan pembentukan tongkol",
    "G6" : "Daun yang terkena terlihat layu",
    "G7" : "Beberapa tambalan kecil bersatu untuk membentuk titik yang lebih besar",
    "G8" : "Bercak coklat muda memanjang berbentuk gulungan atau perahu",
    "G9" : "Bintik-bintik coklat berbentuk seperti elips",
    "G10" : "Daun terlihat kering",
    "G11" : "Bintik-bintik kecil berwarna coklat atau kuning di permukaan daun",
    "G12" : "Bintik-bintik merah di pelepah",
    "G13" : "Ada benang berbentuk tidak beraturan yang berwarna putih dan kemudian coklat",
    "G14" : "Keluar bubuk seperti tepung coklat kekuningan",
    "G15" : "Pembengkakan tongkol",
    "G16" : "Ada jamur putih hingga hitam pada bijinya",
    "G17" : "Biji bengkak",
    "G18" : "Kelenjar terbentuk dalam biji",
    "G19" : "Kelobot terbuka dan muncul banyak jamur putih hingga hitam",
    "G20" : "Ada lubang kecil di daun",
    "G21" : "celah di batang",
    "G22" : "bunga jantan atau dasar tongkol",
    "G23" : "batang dan jumbai (bunga jantan) yang mudah patah",
    "G24" : "tumpukan jumbai yang rusak",
    "G25" : "Bunga jantan tidak terbentuk",
    "G26" : "ada tepung/kotoran di sekitar kerekan",
    "G27" : "daun agak kuning",
    "G28" : "Lubang melintang pada daun pada tahap vegetatif",
    "G29" : "potongan rambut tongkol jagung / dikurangi / kering",
    "G30" : "Ujung tongkol memiliki kerekan",
    "G31" : "Seringkali ada larva",

}