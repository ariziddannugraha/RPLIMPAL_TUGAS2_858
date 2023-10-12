kupon = 0

def cekNomor(nomor):
    if nomor[0:2] == '62' or nomor[0:2] == '08':
        return True
    else:
        return False

def cekPulsa(havePulsa, needPulsa):
    if havePulsa > needPulsa:
        return True
    else:
        return False

def TFPulsa(punyaPulsa):
    admin = 1850
    MIN = 5000
    MAX = 1000000
    print("Silakan masukan nomor tujuan Transfer Pulsa:\n(contoh 08xxxxx atau 628xxxxx)")
    nomor = str(input(">> "))
    if cekNomor(nomor):
        print("Silakan masukan nomor jumlah pulsa yang akan\nditransfer: (min 5000, max 1jt & tanpa . (titik)\n atau , (koma)")
        nomPulsa = int(input(">>"))
        if MIN <= nomPulsa <= MAX:
            print(f"Hati2 penipuan. Anda akan Transfer\nPulsa {nomPulsa} ke nomor{nomor}?\n(Biaya 1850 & 1 Poin undian TP\niPhone14)\n1. Ya\n0. Kembali ke menu")
            confirm = int(input(">> "))
            if confirm == 1:
                if cekPulsa(punyaPulsa, nomPulsa+admin):
                    punyaPulsa -= nomPulsa+admin
                    global kupon
                    kupon = kupon + 1
                    print("Terima kasih permintaan Anda sedang diproses.")
                else:
                    print("Maaf, pulsa Anda tidak mencukupi untuk melakukan transfer pulsa.")
                    main()
    elif confirm == 0:
        main()
    else:
        print("Maaf, input Anda salah. Silahkan coba lagi.")
        main()
                
def mintaPulsa():
    MIN = 5000
    MAX = 1000000

    print("Silahkan masukkan nomor tujuan Minta Pulsa:\n(contoh: 08xxxx atau 628xxxx)")
    nomor = str(input(">> "))
    
    if cekNomor(nomor):
        print("Silahkan masukkan jumlah pulsa yang akan\ndiminta : (min 5000, max 1jt & tanpa. (titik) atau , (koma))")
        jumlahPulsa = int(input(">> "))
        if MIN <= jumlahPulsa <= MAX:
            print(f"Anda akan meminta pulsa: {jumlahPulsa} ke nomor {nomor}? (biaya 100)\n1. Ya\n2. Back\n0. Home")
            validateTransfer = int(input(">> "))
            if validateTransfer == 1:
                print("Terima kasih permintaan Anda sedang diproses\nSampaikan pd JIWA YANG BERSEDIH! Lagu viral dr Ghea Indrawari di LangitMusik Midium RP4400/3hr. Mau?\n1. Ya\n2. Tidak")
                validateIklan = int(input(">> "))
                if validateIklan == 1:
                    print("Terima kasih permintaan Anda sedang di proses")
                    global kupon
                    kupon = kupon + 1
                    main()
                elif validateIklan == 2:
                    print("Terima kasih.")
            elif validateTransfer == 2:
                mintaPulsa()
            else:
                main()
        else:
            print("Maaf nominal yang Anda masukan tidak sesuai.\nmin 5000, max 1jt & tanpa . (titik) atau , (koma)")
            main()
    else:
        print("Nomor yang anda masukkan tidak valid\n(contoh: 08xxxx atau 628xxxx)")
        main()

def autoTP(punyaPulsa, noList):
    print("Silahkan masukkan nomor tujuan yang anda Auto Transfer Pulsa: ")
    nomor = input(">> ")

    if (cekNomor(nomor)):
        print("Masukkan jumlah pulsa minimal 5000: ")
        pulsa = int(input(">> "))
        tanggalTransfer = input("Masukkan tanggal transfer (dd-yy-mm): ")

        print("Hati2 Penipuan.Anda akan Tranfer Pulsa jumlah pulsa ke nomor tujuan setiap tanggal tertentu(biaya 1850 & 1 poin undian TP iPhone14)\n1. Ya\n2. Tidak")
        validateTransfer = int(input(">> "))
        if validateTransfer == 1:
            print("Terima kasih permintaan Anda sedang diproses.")

            if cekPulsa(punyaPulsa, pulsa):
                noList.append(nomor)
                global kupon 
                kupon = kupon + 1            
            else:
                print("SMS: Pulsa anda tidak mencukupi")

            print("Sampaikan pd JIWA BERSEDIH! Lagu viral dr Ghea Indrawari di LangitMusik Midium Rp4400/3hr. Mau?\n1. Ya\n2. Tidak")
            validateIklan = int(input(">> "))
            if validateIklan == 1:
                kupon = kupon + 1   
                print("Terima kasih permintaan Anda sedang diproses.")
            else:
                print("Terima kasih.")
        else:
            print("Terima kasih.")

    else:
        print("nomor yang kamu masukan invalid silahkan menggunakan format: 08xxxx atau 628xxxx")
        main()        
def delTP(noList):
    print("Silahkan masukkan nomor tujuan yg akan\ndihapus dari list Auto Transfer Pulsa:")
    hapusDariList = input(">> ")
    noList.remove(hapusDariList)
    print(f"Anda akan menghapus nomor '{hapusDariList}' dari daftar Auto TP anda?\n1. Ya\n0. Home")
    confirm = int(input(">> "))
    if confirm == 1:
        print(f"nomor '{hapusDariList}' telah di hapus")
    elif confirm == 0:
        main()
    else:
        main()
    

def listTP(noList):
    print("Terima kasih permintaan Anda sedang di proses")
    if(not noList):
        print("SMS: Anda tidak terdaftar pada layanan Auto TP")
    else:
        print("SMS: ")
        x = 1
        for i in noList:
            print(x, ". ", i, "\n")
            x += 1

def cekKupon(kupon):
    print(f"Jumlah kupon Anda adalah: {kupon} kupon")

def main():
    print("\nMau Samsung Fold 4 dr Aldi Taher?\nHub di *500*352#")
    print("1. Transfer Pulsa")
    print("2. Minta Pulsa")
    print("3. Auto TP")
    print("4. Delete Auto TP")
    print("5. List Auto TP")
    print("6. Cek Kupon Undian TP")
    print("0. Batal")
    pilihan = int(input("pilih menu >> "))

    if (pilihan == 1):
        TFPulsa(punyaPulsa)
    elif ( pilihan == 2):
        mintaPulsa()
    elif ( pilihan == 3):
        autoTP(punyaPulsa, noList)
    elif ( pilihan == 4):
        delTP(noList)
    elif ( pilihan == 5):
        listTP(noList)
    elif ( pilihan == 6):
        cekKupon(kupon)
    elif ( pilihan == 0):
        exit()
    else:
        print("Angka yang anda masukan salah!")
        main()

if __name__ == "__main__":
    noList = ['082123456789']
    punyaPulsa = 50000
    main()