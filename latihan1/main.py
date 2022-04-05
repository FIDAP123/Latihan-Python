""" 
belajar python 02b : 
1.  print("") tanda "" berisikan tulisan untuk ditampilkan di terminal
    untuk menampilkan python di terminal
2.  # untuk komen line dan """" """" untuk komen multi line
3.  settings vscode dengan membuat folder .vscode
    dan membuat file settings.json 
4.  untuk shortcut key https://desainerhub.com/2021/04/10-shortcut-visual-studio-code
"""
print()
print("-----|Print|-----")
print()

print("hello world")#ini cara menampilkan python di terminal
print("halo guys")
print("bang bang give alok bg")
print("hello")

"""
Belajar Python 03 :
1.  Mengubah bahasa Interpreter python menjadi bytecode
    dengan mengetik di terminal seperti ini python -m py_compile
    dan menjalankannya dengan mengetik di terminal
    seperti ini python __pycache__/main.cpython-39.pyc
    itu menggunakan bahasa command prompt
2.  untuk shortcut key https://desainerhub.com/2021/04/10-shortcut-visual-studio-code
"""

"""
Belajar Python 04 :
1.  mengenal variable, jika a = 100 maka a adalah variable, 100 adalah value, = adalah asigment
    boleh ditulis juga b = a tapi variable tidak boleh diawali dengan angka melainkan huruf    
2.  untuk shortcut key https://desainerhub.com/2021/04/10-shortcut-visual-studio-code
"""
print()
print("-----|Variable|-----")
print()

a = 10 #a adalah variable, 10 adalah value, = adalah asigment 
b = a # a tidak boleh berada di depan karena disini menjadi value dari b
print(a) #maka akan ditampilkan 10 karena a = 10
print(b) #maka akan ditampilkan 10 krn b = a dan a = 10
print("b = a maka b =",b) #tanda" di dalam print() menandakan kata yg mau ditampilkan langsung atau tidak ada efek apapun
Kilo_Meter10 = 10 #variable hanya bisa dipakaikan underscore(_) dan penggunaan angka di vareable harus berada di belakang


"""
Belajar python 05 :
1.  mengenal jenis^2 variable & tipe data
2.  untuk shortcut key https://desainerhub.com/2021/04/10-shortcut-visual-studio-code
"""
#1. tipe data integer : angka tanpa koma
print()
print("-----|Type Data|-----")
print()

data_int = 1
print("data :", data_int) #,sebagai penanda ganti command
print("-bertipe : ", type(data_int))

#2  tipe data float : angka dengan koma
data_float = 1.5
print("data :", data_float)
print("-bertipe : ", type(data_float))

#3  tipe data string : kumpulan karakter
data_str = "bang give alok bang"
print("data :", data_str)
print("-bertipe : ", type(data_str))

#4  tipe data boolean : biner true/false
data_bool = False
print("data :", data_bool)
print("-bertipe : ", type(data_bool))

#-Tipe Data Khusus
#5  tipe data complex : bilangan kompleks
data_complex = complex(5,2)
print("data :", data_complex)
print("-bertipe : ", type(data_complex))

#-Tipe Data Dari Bahasa C
#6  tipe data Bahasa C : C double, C char, C long, dll
print("=====C_DOUBLE=====")
from ctypes import c_double, sizeof  # maksudnya mengambil data dari bahasa C

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("-bertipe : ", type(data_c_double))

"""
Belajar python 06 :
1. Casting tipe data atau merunbah tipe data (ad tipe data tertentu yg error atau tdk bs dicasting atau ganti)
2. untuk shortcut key https://desainerhub.com/2021/04/10-shortcut-visual-studio-code
"""
print()
print("-----|Casting Variable Type Data|-----")
print()

data_int = 9;
print("data =", data_int ,"type,=",type(data_int))

print("=====Data Integer=====")

data_bool = bool(data_int)
data_float = float(data_int)
data_str = str(data_int)
data_complex= complex(data_int)

print("data=",data_bool, "type=",type(data_bool))
print("data=",data_float, "type=",type(data_float))
print("data=",data_str, "type=",type(data_str))
print("data=",data_complex, "type=",type(data_complex))

data_bool = False;
print("data =", data_bool ,"type,=",type(data_bool))

print("=====Data Boolean=====")

data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
data_complex = complex(data_bool)

print("data=",data_int, "type=",type(data_int))
print("data=",data_float, "type=",type(data_float))
print("data=",data_str, "type=",type(data_str))
print("data=", data_complex, "type=", type(data_complex))


data_str = "";
print("data =", data_str ,"type,=",type(data_str))

print("=====Data String=====")

data_bool = bool(data_str)

print("data=",data_bool, "type=",type(data_bool))
print("data=",data_int, "type=",type(data_int))
print("data=",data_float, "type=",type(data_float))
print("data=",data_complex, "type=",type(data_complex))

data_complex = complex(0);
print("data =", data_complex ,"type,=",type(data_complex))

print("=====Data Complex=====")

data_str = str(data_complex) #data complex hanya bisa dicasting atai diganti di data string saja karena data complex adalah bilangan imajiner sedangkan data string bisa diisi semua karakter
# data_int = int(data_complex)
# data_bool = bool(data_complex)
# data_float = float(data_complex)


print("data=",data_str, "type=",type(data_str)) #data complex hanya bisa dicasting atau diganti di data string saja karena data complex adalah bilangan imajiner sedangkan data string bisa diisi semua karakter
# print("data=",data_int, "type=",type(data_int))
# print("data=",data_bool, "type=",type(data_bool))
# print("data=",data_float, "type=",type(data_float))

"""
Belajar Python 07 :
1. cara menginput data dari user
2. untuk shortcut key https://desainerhub.com/2021/04/10-shortcut-visual-studio-code
"""
print()
print("-----|Input Data Dari User|-----")
print()

data = input ("masukkan data :") #setelah input harus masukkan string atau ("")
print("data=",data,",type =",type(data)) #,untuk ganti command
#jika data tidak ditambahkan int,float atau complex maka tipe data akan berubah menjadi string

angka = int(float(input("masukkan angka"))) #jika data tidak ditambahkan int,float 
print("data=", angka, "tipe data =",type(angka))

angka_susah = complex(int(float(input("masukkan angka"))))
print("angka =",angka_susah, type(angka_susah))#complex beda dengan bilangan integer atau float makanya akan susah merubah datanya krn beda bilangan

bilangan_complex = complex(input('isi bilangan complex contoh 1+2j='))
print('bilangan =', bilangan_complex,type(bilangan_complex))

"""
Belajar Python 08 :
1. Operasi Aritmatika
2. untuk shortcut key https://desainerhub.com/2021/04/10-shortcut-visual-studio-code
"""
print()
print("-----|Operasi Aritmatika|-----")
print()

a=3
b=5
print("a= ",a)
print("b= ",b)

#Operasi Penambahan (+)
hasil = a + b
print(a,"+",b,"= ", hasil)

#Operasi Pengurangan (-)
hasil = a - b
print(a,"-",b,"= ", hasil)

#Operasi Perkalian (*)
hasil = a * b
print(a,"x",b,"= ", hasil)

#Operasi Pembagian (/)
hasil = a / b
print(a,"/",b,"= ", hasil)

#Operasi Modulus (%)
hasil = a % b
print(a,"%",b,"= ", hasil)

#Operasi eksponen/ pangkat (^ atau **)
hasil = a ** b
print(a,"**",b,"= ", hasil)

#Operasi Floor Division atau pembulatan ke angka integer sehabis dibagi (//)
hasil = a // b
print(a,"//",b,"= ", hasil)

#Prioritas Operasi atau Urutan Operasi
# 1. ()
# 2. eksponen **
# 3. perkalian dan lain-lain * / % //
# 4. Pertambahan dan Pengurangan + -

print()
x = 5
n = 8
xx = 4
print("x = ",x)
print("n = ",n)
print("xx = ",xx)

hasil = x * n / xx ** x // n - xx + x % n 
print(x ,"*" ,n ,"/" ,xx ,"**" ,x ,"//" ,n ,"-" ,xx ,"+" ,x ,"%", n ,"= " ,hasil)

haha = x % n
print(haha)