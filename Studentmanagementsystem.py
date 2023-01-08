#Creating Student Management System(Project for Computer Science, Class XII)
import pickle #(As we are using Binary Files)
import os #(As we are using rename and remove functions)

def acceptstudent():
    '''A function to receive student data from user and store it in a binary file'''
    f1=open("studentrecord.dat","ab")
    while True:
        print("\nEnter the details of the student")
        sroll=int(input("Enter the student's roll number: "))
        sname=input("Enter the student name: ")
        sphysics=int(input("Enter physics marks: "))
        schem=int(input("Enter chemistry marks: "))
        smaths=int(input("Enter maths marks: "))
        scomp=int(input("Enter computer marks: "))
        d1={"sroll":sroll,"sname":sname,"sphysics":sphysics,"schem":schem,"smaths":smaths,"scomp":scomp}
        pickle.dump(d1,f1)
        ch=int(input("Want to store more students record? If yes press 1, if no press 0"))
        if ch==0:
            break
    f1.close()

def viewall():
    '''A function use to display all the data of students stored till now in tabular form'''
    f1=open("studentrecord.dat","rb")
    print("\n\nRollno\t\tName\t\tPhysics\t\tChemistry\t\tMaths\t\tComputer")
    try:
        while True:
            d1=pickle.load(f1)
            print(d1["sroll"],"\t\t",d1["sname"],"\t\t",d1["sphysics"],"\t\t",d1["schem"],"\t\t",d1["smaths"],"\t\t",d1["scomp"])
    except EOFError:
        f1.close()

def viewone():
    '''A function used to search and display information of a student's data on the basis of his/her roll number'''
    f1=open("studentrecord.dat","rb")
    rollno=int(input("Enter the student roll no:"))
    found=False
    try:
        while True:
             d1=pickle.load(f1)
            if d1["sroll"]==rollno:
                 found=True
                print("\n\nThe student roll number is: ",d1["sroll"])
                print("The student name is: ",d1["sname"])
                print("The student's physics marks is: ",d1["sphysics"])
                print("The student's chemistry marks is:  ",d1["schem"])
                print("The student's maths marks is: ",d1["smaths"])
                print("The student's computer marks is: ",d1["scomp"])
    except EOFError:
          f1.close()
    if found==False:
         print("The student with the roll number ",rollno," do not exists in our record. Please try again")

def updatestudent:
    '''Code to update the information of the students whose data is stored in file'''
    f1=open("studentrecord.dat","rb+")
    rollno=int(input("Enter the employee id whose record you want to update : "))
    found=False
    try:
        while True:
            pos=f1.tell()
            d1=pickle.load(f1)
            if d1["sroll"]=rollno:
                found=True
                print("\n\nThe student roll number is:", d1["sroll"])
                print("The student name is:", d1["sroll"])
                print("The student's physics marks is:", d1["sphysics"])
                print("The student's chemistry marks is:", d1["schem"])
                print("The student's maths marks is:", d1["smaths"])
                print("The student's computer marks is:", d1["scomp"])
                print("\n")
                cphysics=int(input("Enter new physics marks or press 1 to retain old marks"))
                if cphysics!=0:
                    d1["sphysics"]=cphysics
                cchem=int(input("Enter new chemistry marks or press 2 to retain old marks"))
                if cphysics!=2:
                    d1["schem"]=cchem
                cmaths=int(input("Enter new maths marks or press 3 to retain old marks"))
                if cmaths!=3:
                    d1["smaths"]=cmaths
                ccomp=int(input("Enter new computer marks or press 4 to retain old marks"))
                if ccomp!=4:
                    d1["scomp"]=ccomp
                f1.seek(pos)
                pickle.dump(d1,f1)
                print("!!!!!Record Updated Successfully!!!!!")
    except EOFError:
        f1.close()
    if found==False:
        print("The student with roll number", rollno, "does not exist in our records. Please try again")

def deletestudent:
     '''Code to delete the information of the students whose data is stored in file'''
    f1=open("studentrecord.dat","rb")
    f2=open("temp.dat","wb")
    rollno=int(input("Enter the student's roll number whose record you want to delete: "))
    found=False
    try:
        while True:
            d1=pickle.load(f1)
            if d1["sroll"]=rollno:
                found=True
                print("\n\nThe student roll number is:", d1["sroll"])
                print("The student name is:", d1["sroll"])
                print("The student's physics marks is:", d1["sphysics"])
                print("The student's chemistry marks is:", d1["schem"])
                print("The student's maths marks is:", d1["smaths"])
                print("The student's computer marks is:", d1["scomp"])
                print("\n")
                cho=input("Are you sure you want to delete this record(Y/N)")
                if cho=="Y" or cho=='y':
                    print("!!!!!Record deleted successfully!!!!!")
                else:
                    pickle.dump(d1,f2)
            else:
                    pickle.dump(d1,f2)
    except EOFError:
        f1.close()
        f2.close()
        os.remove("studentrecord.dat")
        os.rename("temp.dat", "studentrecord.dat")
    if found==False:
        print("The student with roll number", rollno, "do not exist in our record. Please try again")

#mains(Execution of the project starts HERE)
print("Welcome to Student Management System")
while True:
    print("\nEnter  1 to add information of student(s)")
    print("Enter 2 to view all the students in tabular form")
    print("Enter 3 to view one student on the basis of his roll number")
    print("Enter 4 to update the student on the basis of his roll number")
    print("Enter 5 to delete the student on the basis of his roll number")
    print("Enter 0 to exit the application")
    choice=int(input("Enter your choice here: ")
    if choice==1:
        acceptstudent()
    elif choice==2:
        viewall()
    elif choice==3:
        viewone()
    elif choice==4:
        updatestudent()
    elif choice==5:
        deletestudent()
    elif choice==0:
        break
    else:
        print("Sorry you have entered a wrong choice. Please try again")
        
        
        

                

