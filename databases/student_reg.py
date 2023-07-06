from database import Student

try:
    jina = input("Enter Name\n")
    nambariyasimu = input("Enter Phone Number\n")
    miaka = input("Enter Age\n")
    jinsia = input("Enter Gender\n")
    nambari = input("Enter Student Code\n")

    Student.create(name=jina, phone=nambariyasimu, age=miaka, gender=jinsia, studentcode=nambari)
    print("Student Created Successfully")

except:
    print("Failed To Create Student")
