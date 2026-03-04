data={
"abhi":{'status' : True,'python':100,'mysql':99,'softskills':45}
"akhi":{'status' : False,'python':None,'mysql'=None,'softskills':None}
"anish":{'status' : True,'python':20,'mysql'=30,'softskills'=10}
"aravindh":{'status' : True,'python':50,'mysql'=79,'softskills'=55}
}
user = input("enter the student name")

if user in data:
    if data[user]['status']:
        sum =   data[user]['python']+data[user]['mysql']+data[user]['softskills']
        avg = sum/3
     if avg > 80:
    print("A grade")
    elif avg > 60:
        print("B grade")
    elif avg > 40:
            print("c grade")
    elif  avg < 40:
                print("failed")
else:
    print(f"{user},did't write exam")
    







