students = ["Cem Çiçek", "Ramazan Demir", "Yılmaz Tan", "Selim Dağ"]

def menu():
    sec = input("Lütfen yapmak istediğiniz işlemi seçiniz: \n"
                "1 - Öğrenci Ekle\n"
                "2 - Öğrenci Sil\n"
                "3 - Öğrencileri Listele\n"
                "4 - Öğrenci Numarası Bul\n"
                "5 - Çoklu Öğrenci Ekle\n")

    if sec == "1":
        print("-----------------------------------------------------------")
        addStudent()
    if sec == "2":
        print("-----------------------------------------------------------")
        removeStudent()
    if sec == "3":
        print("-----------------------------------------------------------")
        studentsList()
    if sec == "4":
        print("-----------------------------------------------------------")
        studentNum()
    if sec == "5":
        print("-----------------------------------------------------------")
        addMultipleStudent()

def addStudent():
    print("---Öğrenci Ekleme---")
    name = input("Eklemek istediğiniz öğrencinin İsmini giriniz: ")
    surname = input("Eklemek istediğiniz öğrencinin Soyadını giriniz: ")
    students.append(name + " " + surname)
    print(students)

def removeStudent():
    print("---Öğrenci Silme---")
    name = input("Silmek istediğiniz öğrencinin İsmini giriniz: ")
    surname = input("Silmek istediğiniz öğrencinin Soyadını giriniz: ")
    students.remove(name + " " + surname)
    print(students)

def studentsList():
    print("--Öğrenci Liste--")
    print(students)

def studentNum():
    print(students)
    name = input("Numarasını öğrenmek istediğiniz öğrencinin İsmini giriniz: ")
    surname = input("Numarsını öğrenmek istediğiniz öğrencinin Soyadını giriniz: ")
    num = students.index(name + " " + surname)
    print("{} Ad ve Soyadlı öğrencinin numarası: {} ".format(name + " " + surname,num))

def addMultipleStudent():
    print("--Çoklu Ekle--")
    number = int(input("Kaç öğrenci ekleyeceksiniz: "))
    i = 0
    while i < number:
        name = input("Eklemek istediğiniz öğrencinin İsmini giriniz: ")
        surname = input("Eklemek istediğiniz öğrencinin Soyadını giriniz: ")
        students.append(name + " " + surname)
        i += 1
    print(students)

menu()