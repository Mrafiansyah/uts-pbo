user_id = 0
loop = "n"
user =  [
            {   
                "id":"1234",
                "no_rekening":"1234567890",
                "username":"test",
                "pin":"4321",
                "saldo":0
            },
            {   
                "id":"4321",
                "no_rekening":"0987654321",
                "username":"test2",
                "pin":"1234",
                "saldo":0
            }
        ]
status_login = False
pakai_atm = "y"
 
def cek_login(p):
    for us in user:
        if us['pin'] == p:
            return us
    return False       
     
def cek_user(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return int(i)
    return -1
 
def cek_rekening(no):
    for i in range(len(user)):
        if str(user[i]['no_rekening']) == str(no):
            return int(i)
    return -1
 
def tranfer_uang(uang,no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] - int(uang)
            user[index2]['saldo'] =user[index2]['saldo'] + int(uang)
            print("Anda berhasil mentransfer uang Rp."+str(uang)+" ke Rekening "+no_rekening)
            print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
        else:
            print("Ops saldo anda tidak cukup")
             
def simpan_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] + int(uang) 
            print("penambahan saldo sebesar "+str(uang))
            print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
        else:
            print("Ops saldo anda tidak cukup")

def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] - int(uang) 
            print("Anda berhasil menarik uang Rp."+str(uang))
            print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
        else:
            print("Ops saldo anda tidak cukup")
 
 
while pakai_atm == "y":
    while status_login == False:
        print("aplikasi pencatatan uang digital")
        print("Silahkan masukan pin anda")
        pin = input("Masukan PIN : ")
     
        cl = cek_login(pin)
        if cl != False:
            print("selamat data "+cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("Ops PIN anda salah")
            print("")
            print("")
     
    while loop == "y" and status_login == True:
        u = user[cek_user(user_id)]
        print("aplikasi pencatatan uang digital")
        print("1.Cek Saldo")
        print("2.Tambah saldo")
        print("3.Ambil Uang")
        print("4.Logout")
        print("5.Keluar ATM")
        a = int(input("Silahkan pilih menu : "))
        if a == 1:
            print("")
            print("Saldo umum anda saat ini adalah: ",u['saldo'])
            print("Saldo tabungan anda saat ini adalah: ",u['saldo'])
            print("")
            loop = "n"
        elif a == 2:
            print("1. umum")
            print("2. tabungan")
            print("**********")
            a = int(input("Pilih penyimpanan : "))
            nominal = input ("Nominal uang yang akan ditambahkan : ")
            simpan_uang(nominal)
            print("")
            loop ="n"
                 
        elif a == 3:
            print("1. umum")
            print("2. tabungan")
            print("**********")
            a = int(input("Pilih penyimpanan : "))
            nominal = input("Nominal Yang Akan Di Tarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"
        elif a == 4:
            status_login = False
             
        elif a == 5:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("pilihan tidak tersedia")
        if status_login == True:
             
            input("kembali Ke menu (Enter) ")
            print("")
            loop = "y"