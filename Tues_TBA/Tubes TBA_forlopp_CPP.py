sentences = input("for loop C++ : ") #inputan for loop c++ contoh for ( int i = 5 ; i > 10 ; i ++ ) { c = b + c ; }
sentences = sentences.split() #mengubah inputan menjadi list

variabel = ["a", "b", "c", "d", "e", "f", "g", "h","i"] #Variabel yang valid
angka = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"] #Angka yang valid
increment = ["++", "--"] #increment yang valid
conditions = [">=", "<=", "<", ">"] #Condition yang valid
operations = ["+", "-", "*", "/"] #Operation yang valid

checks = [
    "for", "(", "int", variabel, "=", angka, ";", variabel, conditions, angka, ";", variabel, increment, ")", #Token yang diharapkan untuk perulangan for dan kondisinya
    "{", variabel, "=", variabel, operations, variabel, ";","}", #Token yang diharapkan untuk isi Loop
]

state = 0 #Menginisialisi State
Final = True #Penentu Pharse

for sentence in sentences: #Mengiterasi list pada sentences
    if type(checks[state]) is list: #Memastikan apakah data tersebut list ato tidak
        if sentence not in checks[state]: #kondisi jika sentence index saat ini yang di iterasi pada index saat ini tidak ada pada check
            print("Error at state :",state) #Mengprint Error dan state saat ini
            Final = False #Final di set False
            break
    else:
        if sentence != checks[state]: #Jika sentence tidak ada di checks
            print("Error at state",state) #Error pada state
            Final = False #Final di set ke False
            break
    state += 1 #crement state

if Final and state == 22: #kondisi jika Final True dan state = 22
    Final = True #Final di set ke True
elif Final and state != 22: #Kondisi jika final True dan state tidak 22
    print("Error at state",state) #Print Error dan state

if Final: #kondisi jika finat True
    print("Pharsed well") #print Pharsed well