d = {"Arjun" : 85, "Rahul" :90, "Anitha" : 78}
name = input("Enter the student name: ").strip()
try:
    print(d[name])
except Exception:
    print("student not found! ")
