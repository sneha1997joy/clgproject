from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login

from clgapp.models import CourseModel, StudentModels, TeacherModel

# Create your views here.
def home(request):
    return render(request,'home.html')

def signuppage(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'signup.html',context)

def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        address=request.POST['address']
        age=request.POST['age']
        select=request.POST['select']
        course=CourseModel.objects.get(id=select)
       # course=request.POST['course']
        img=request.FILES.get('file')
        

        if password==cpassword: 
            if User.objects.filter(username=username).exists(): 
                messages.info(request, 'This username already exists!!!!!!')
                #print("Username already Taken..")
                return redirect('signuppage')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email,
                    )
                user.save()
                Teachers=TeacherModel( First_Name=first_name,
                                      Last_Name=last_name, 
                                      User_Name=username,
                                      Email=email,
                                      Address=address,
                                      Age=age,
                                      Course_Name=course,
                                      image=img)
                Teachers.save()
                messages.info(request, 'SuccessFully completed.......')
                print("Successed...")


        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signuppage')
        return redirect('loginpage')
    else:
        return render('signup.html')

def loginpage(request):
    return render(request,'login.html')

def userlogin(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username= username,password= password)

        if user is not None:
                    if user.is_staff:
                         login(request,user)
                         return redirect('admin_home')
                    else:
                         auth.login(request,user)
                         messages.info(request,f'welcome {username}' )
                         return redirect('user_home')
        else:
             messages.info(request, 'Invalid Usename or Password . Try Agin.')
             return redirect('loginpage')
    else:
        #messages.info(request, 'Oops Something Wrong.')
        return redirect('loginpage')
    
def admin_home(request):
     return render(request,'admin.html')

def addcoursepage(request):
     return render(request,'addcourse.html')
def addcourse(request):
     if request.method =='POST':
          coursename=request.POST['coursename']
          coursefees=request.POST['coursefees']
          data = CourseModel(Course_Name=coursename,Course_Fees=coursefees)
          data.save()
        # messages.info(request, 'New User Added')
          return redirect('showcourse')    
                         
def showcourse(request):
     crs=CourseModel.objects.all()
     return render(request,'course.html',{'crs':crs})

def user_home(request):
     tchr=TeacherModel.objects.all()
     return render(request,'user.html',{'tchr':tchr})

def editpage(request,id=id):
    tchr=TeacherModel.objects.get(id=id)
    return render(request,'alter.html',{'tchr':tchr})

def editteacher(request,id=id):
     if  request.method == 'POST':
          tchr=TeacherModel.objects.get(id=id)
          tchr.First_Name=request.POST.get('f_name')
          tchr.Last_Name=request.POST.get('l_name')
          tchr.Age=request.POST.get('age')
          tchr.Course_Name=CourseModel.objects.get(id=id)
          tchr.Address=request.POST.get('address')
          tchr.Email=request.POST.get('email')
          if 'image' in request.FILES:
            tchr.image=request.FILES.get('file')

          tchr.save()  
          return redirect('user_home')
     return render(request,'alter.html')

def deletepage(request,id):
    crs=CourseModel.objects.get(id=id)
    return render(request,'delete.html',{'crs':crs})

def deletecourse(request,id):
    if request.method=='POST':
      crs=CourseModel.objects.get(id=id)
      crs.delete()
      return redirect('showcourse')
    return render(request,'delete.html')

def addstudentpage(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'addstudent.html',context)
     
def addstudent(request):
    if request.method == 'POST':
        studentname=request.POST['studentname']
        pnumber=request.POST['phone']
        select=request.POST['select']
        coursename=CourseModel.objects.get(id=select)
        gender=request.POST['gender']
        address=request.POST['address']
        data = StudentModels(Course_Name=coursename,Student_Name=studentname,Phone_Number=pnumber,Gender=gender,Address=address)
        data.save()
        # messages.info(request, 'New User Added')
        return redirect('showstudent')

def showstudent(request):
     std=StudentModels.objects.all()
     return render(request,'student.html',{'std':std})

def deletestudent(request,id):
    if request.method=='POST':
        std=StudentModels.objects.get(id=id)
        std.delete()
        return redirect('showstudent')
    return render(request,'deletes.html')

def deletepages(request,id):
   std=StudentModels.objects.get(id=id)
   return render(request,'deletes.html',{'std':std})

def showteacher(request):
     tchr=TeacherModel.objects.all()
     return render(request,'teacher.html',{'tchr':tchr})


def deletepaget(request,id):

    tchr=TeacherModel.objects.get(id=id)
    return render(request,'deletet.html',{'tchr':tchr})
        
def deleteteacher(request,id):
    if request.method=='POST':
        tchr=TeacherModel.objects.get(id=id)
        tchr.delete()
        return redirect('showteacher')
    return render(request,'deletet.html')

def adminlogout(request):
    return redirect('loginpage')

