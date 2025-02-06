meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "Tertawa Terbahak bahak",
  
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("artinya:",meme_dict[word])
else:
    print("MAAF, KATA TERSEBUT BELUM TERSEDIA")
