from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib.auth.models import AnonymousUser, User, auth
from django.contrib import messages
from django.db.models import F,Sum
from django.core.files.storage import FileSystemStorage

from django.db.models.query import QuerySet
from .models import transction, withdraw, writer,Bids,pay,comp,withdraw

# Create your views here
def Homepage(request):
    return render(request, 'Homepage.html')
def Home(request):
    all_bids = Bids.objects.all()
    return render(request, "home.html", {'all': all_bids})
   
def Home2(request):
    all_bids = Bids.objects.all()
    return render(request, "home2.html", {'all': all_bids})
    

def register(request,i_number="1"):
     if request.method == "POST":
            name1= request.POST['name1']
            name2= request.POST['name2']
            
            username= request.POST['username']
            phone= request.POST['phone']
            
            email= request.POST['email']
            pass1= request.POST['pass1']
            pass2= request.POST['pass2']
            

            if pass1 == pass2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email used')
                    return render(request , 'register.html' ,{'name1' : name1,'name2' : name2,'email':email,'phone':phone,'password1':pass1,'password2':pass2,'username':username})

                elif writer.objects.filter(phone=phone).exists():
                    messages.info(request, 'Phone number used')
                    return render(request , 'register.html' ,{'name1' : name1,'name2' : name2,'email':email,'phone':phone,'password1':pass1,'password2':pass2,'username':username})
                
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'Phone number used')
                    return render(request , 'register.html' ,{'name1' : name1,'name2' : name2,'email':email,'phone':phone,'password1':pass1,'password2':pass2,'username':username})

          
                    


                else:

                        if writer.objects.filter(number=i_number).exists():
                            inviter= writer.objects.get(number=i_number)

                            inviter_name= inviter.first_name

                            number= writer.objects.last()
                            number= number.number

                            number = int(number)+1500*1582-1000/1509*85231
                            # if writer.objects.filter(number).exists():
                            # number=number*100+52697-1235*102354


                            user = User.objects.create_user(username=username,first_name=name1,password=pass1,email=email)
                            user.save()
                            add = writer(user=user,phone=phone,first_name=name1,username=username,second_name=name2,email=email,number=number, inviter_name= inviter_name, inviter_number= i_number )
                            add.save()
                            messages.info(request, 'Account registered,proceed to login')
                            return redirect('login.html')


                        else:
                            messages.warning(request, 'invalid')
                            return redirect('register')





            else:
              messages.info(request, 'Password mismatch')
            return render(request , 'register.html' ,{'name1' : name1,'email':email,'phone':phone,'password1':pass1,'password2':pass2,'username':username})

     else:
            return render(request, "register.html")
def login(request):
    if request.method =="POST":
        username= request.POST['username']
        pass1= request.POST['pass1']

        if User.objects.filter(username=username).exists():

            user = auth.authenticate(username= username, password=pass1)
            if user is not None:
                auth.login(request , user)
                return redirect('Profile2.html')
            
                
            else:
                
                messages.info(request , 'Wrong Password')
         
         
                return render(request , 'login.html',{'username': username,'password':pass1})

        else:
             
            messages.info(request , 'Invalid Username')
            return render(request , 'login.html',{'username': username,'password':pass1})
    
    else:
        return render(request, "login.html")
def Dashboard(request):
    all_writers=writer.objects.all()
    return render(request, "Dashboard.html",{'all':all_writers})
def Bid(request):
     if request.method=="POST":
        posts=request.POST["posts"]
        Categ=request.POST["Categ"]
        Amount=request.POST["Amount"]
        period=request.POST["period"]


       

       
        

        new2_save = Bids(post=posts,cat=Categ,price=Amount,per=period)
        new2_save.save()
        messages.info(request , 'Bid Added   successfully.')
        return render(request, "Bid.html")
     else:
        return render(request, 'Bid.html')
def privacy(request):
    return render(request, 'privacy.html')
def Payment(request):
    if request.method=="POST":
        username=request.POST["username"]
        code1=request.POST["code1"]
        mpesa_code=request.POST["mpesa_code"]
       


       

       
        

        new3_save = pay(username=username,code1=code1,mpesa_code=mpesa_code)
        new3_save.save()
        messages.info(request , 'Account Activated   successfully.')
        return render(request, "completedbids.html")
    else:
        return render(request, 'Payment.html')
def completedbids(request):
 if request.method =="POST" and request.FILES["documents"]:
        username= request.POST['username']
        mpesa_code= request.POST['mpesa_code']
        documents =request.FILES['documents']
        
        code =request.POST['code']

       
               
        new4_save = comp(username=username,mpesa_code=mpesa_code,code=code,documents=documents)
        new4_save.save()
        messages.info(request , 'Bid  successfully submited.')
        return render(request, "Payment.html")
def Profile2(request):
    all_writers = writer.objects.all()
    return render(request, 'Profile2.html',{'all':all_writers})
def withd (request):
    if request.user.is_authenticated:
        if request.method=="POST":
            withdraww=int(request.POST['withdraww'])
            phone=request.user.writer.phone
            balance=request.user.writer.total_balance


            if withdraww > balance:
                messages.info(request,'insufficient balance')

                return redirect('withd') 
            else:
                if withdraww == 0:
                    messages.info(request,'You cant withdraw 0')

                    return redirect('withd') 

                elif withdraww < 150:
                    messages.info(request,'Minimum Amount You Can withdraw')

                    return redirect('withd') 
                else:
                    transct = transction(type='withdraw',amount=withdraww,phone=phone)
                    transct.save()
                    wit =str(withdraww)
                    num =str(phone)



                    new =withdraw(amount=withdraww,phone=phone,balance=balance)

                    new.save()

                    bal=balance-withdraww
                    writer.objects.filter(phone=phone).update(total_balance=bal)
                    messages.info(request, 'Succesifully Withdrawn KES' + wit + 'To Phone number'+num)
                    messages.info(request ,"transaction will be processed after a few minutes")
                    return redirect('withd.html')

                  
    return render(request, 'withd.html' )

                
          
               
