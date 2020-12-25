from os import system, name

line = "--------------"

#main func
def clear():
    #untuk windows 
    if name == 'nt':
        _ = system("cls")
    else:
        _ = system("clear")
    
#fungsi tampilkan data
def show_data():
    print(line+"[DATA BUKU]"+line)
    print("____ ____________________")
    print(" No |     Judul Buku     ")
    print("____|____________________")
    f = open("databuku.txt")
    isi = f.readlines()
    isi.sort()
    if len(isi)==0:
        print("\nBelum ada data buku yang masuk")
    else:
        i = 1;
        for x in isi:
            pecah = x.split(",")
            print(" "+str(i)+". ",end="")
            print("| "+pecah[0]+""+ pecah[1],end="")
            i += 1
    back_to_menu()

#fungsi masukkan data
def insert_data():
    buku_baru = input("Masukkan Judul Buku: ")
    tanggal_baca = ("")
    f = open("databuku.txt", "a")
    f.writelines([buku_baru+","+tanggal_baca+"\n"])
    f.close()
    sukses = True
    if sukses:
        print("Buku '", buku_baru, "' Berhasil ditambahkan")
        tanya = input("Mau isi lagi? (y/t)  : ")
        if (tanya.lower() == "y"):
            insert_data()
        else:
            stop = True
        back_to_menu()

#fungsi Cari data
def search_data():
    search = input("Masukkan Judul Buku yang ingin dicari :")
    f = open("databuku.txt")
    isi = f.readlines()
    idx = 0
    for x in isi:
        xp = x.split(",")
        if xp[0] == search:
            idx = 1
            print("buku", search, "di temukan")
    if idx == 0:
        print("tidak ditemukan")
    back_to_menu()

#fungsi edit data
def edit_data():
    ubah_nama = input("Masukan judul buku yang ingin diupdate   : ")
    judul_baru = input("Masukan judul buku baru                  : ")
    tanggal_baru = ("")

    f = open("databuku.txt")
    isi = f.readlines()
	#print(isi)
    idx = 0
    for x in isi:
        xp = x.split(",")
        if xp[0] == ubah_nama:
            xp[0] = judul_baru
            xp[1] = tanggal_baru+"\n"
            xg = ",".join(xp)
            isi[idx] = xg
        idx += 1
    f.close()
	
    f = open("databuku.txt","w")
    isi = f.writelines(isi)
    f.close()
    sukses = True
    if sukses:
        print("Buku '", ubah_nama, "' Berhasil diupdate menjadi '", judul_baru, "'")
        back_to_menu()

#fungsi hapus data
def delete_data():
    hapus_nama = input("Masukan judul buku yang ingin dihapus: ")

    f = open("databuku.txt")
    isi = f.readlines()
	#print(isi)
    idx = 0
    for x in isi:
        xp = x.split(",")
        if xp[0] == hapus_nama:
            xp[0] = ""
            xp[1] = ""
            xg = "".join(xp)
            isi[idx] = xg
        idx += 1

    f.close()
    f = open("databuku.txt","w")
    isi = f.writelines(isi)
    f.close()
    sukses = True
    if sukses:
        print("Buku '", hapus_nama, "' Telah di hapus")
        back_to_menu()

def delete_all():
    confirm = str(input("Apakah kamu yakin akan menghapus semua data buku? (y/t) : "))

    if (confirm.lower() == 'y'):
        # make a mass delete 
        f = open("databuku.txt","w")
        toDel = f.truncate(0)
        f.close()
        print("Data berhasil dihapus")
    else:
        back_to_menu()

#tampilan menu
menus =["[1] Masukkan Data Buku","[2] Tampilkan Data Buku","[3] Cari Buku","[4] Update Data Buku","[5] Hapus Buku","[6] Hapus Semua Data Buku","[7] Exit"]

def show_menu():
    clear()
    print(line+line+line)
    print("        PROGRAM DATA BUKU SEDERHANA           ")
    print(line+line+line)
    print("\n")
    print("======== MENU ========")
    for i in menus:
        print(i)

    selected_menu = input("Pilih menu> ")
    print("\n")

    if (selected_menu == "1"):
        insert_data()
    elif (selected_menu == "2"):
        show_data()
    elif (selected_menu == "3"):
        search_data()
    elif (selected_menu == "4"):
        edit_data()
    elif (selected_menu == "5"):
        delete_data()
    elif (selected_menu == "6"):
        delete_all()
    elif (selected_menu == "7"):
        exit()
    else:
        print("Masukkan pilihan sesuai nomor menu")
        back_to_menu()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

if __name__ == "__main__":
    while(True):
        show_menu()
