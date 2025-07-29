import random
import sys
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.views.generic import View
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, DjangoUnicodeDecodeError
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse
from e_admin.models import Product , feedback,donation,room_booking,rooms,Order
import razorpay



def Home(request):  

    return render(request, "Home.html")


def Donation(request):
        user_name = request.user
        user_n = User.objects.filter(username = user_name)
        #print(user_n.values())
        
        donation_data = donation.objects.all()

        
        data={
             'user_obj' : user_n ,
             'donation' : donation_data
        }
        
        if request.method=='POST':
            username = request.POST.get('uname')
            date = request.POST.get('today')
            amountc = int(request.POST.get('amountc'))
            reason = request.POST.get('reason')
            if amountc < 50:
                response_content = '''
                    <div style="text-align: center; margin-top: 20px; font-size: 24px;">
                        Amount must be more than 50 Rs.
                    </div>
                    <div id="redirect-message" style="text-align: center; margin-top: 10px; font-size: 18px;">
                        Redirecting in <span id="countdown">3</span> seconds...
                    </div>
                    <script>
                        // JavaScript countdown logic
                        var countdownElement = document.getElementById('countdown');
                        var seconds = 3;

                        function countdown() {
                            countdownElement.textContent = seconds;
                            seconds--;

                            if (seconds >= 0) {
                                setTimeout(countdown, 1000);  // Update countdown every second (1000 milliseconds)
                            } else {
                                window.location.href = '/Donation';  // Redirect to donation page after countdown
                            }
                        }

                        // Start the countdown when the page loads
                        countdown();
                    </script>
                '''
                return HttpResponse(response_content)

                #return HttpResponse('<div style="text-align: center; margin-top: 50px; font-size: 20px;">Amount must be more than 50 Rs.</div>')
            
            print(amountc)
            client = razorpay.Client(auth=("rzp_test_8WbzVlHnGFIQf0","hDtGutmr7gsqeZGuv1a9zO8E"))
            print(client)
            payment = client.order.create({'amount': int(float(amountc) * 100) , 'currency':'INR' ,  'payment_capture': '1'})
            # print(payment)
            # print(payment.amount)
            # print(type(payment.amount))
            en = donation(username=username,date=date,amountc=amountc,reason=reason)
            
            # donation1 = donation.Objects.last()
            # donation1.razor_pay_order_id = payment["id"]
            # donation1.payment_signature = "online"
            # donation1.Paymentstatus = "sucess"
            
            # donation1.save()

            en.save()
            user_data = User.objects.all()
            for a in user_data:
                b = a.email
                c = a.username
                # print(b)
            print(b)
            print(c)

            donation_d = donation.objects.all()
            for d in donation_d:
                e = d.amountc

            print(e)
            
            subject = "Successfull Donation Message"
            message1 = "Thank you , "+str(c)+" for your donation of "+str(e) +"Rupees."
            from_email = 'templemanagementsystem66@gmail.com'
            # recipient_list = b
            send_mail(subject,message1,from_email,[b],)
            # send_mail.send()
            return render(request, "Donation.html", {'user_obj' : user_n , 'donation' : donation_data , 'payment' : payment , 'flag' : '1'})

        return render(request, "Donation.html",data)

def confirm_donation(request):
    cusername = request.user.username
    user_n = User.objects.filter(username=cusername)

def donation_email(request):
    
    return redirect('donation_email')
    
def Festival_Gallery(request):
    return render(request, "Festival_Gallery.html")


def Information(request):
    return render(request, "Information.html")


def News_And_Event(request):
    return render(request, "News_And_Event.html")


def Photo_Gallery(request):
    return render(request, "Photo_Gallery.html")


def Profile(request):
    user_name = request.user
    user_n = User.objects.filter(username = user_name)
    print(user_name)
    dict = {'user_obj' : user_n}
    return render(request, "Profile.html" , dict)


from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import room_booking, rooms  # Import your models

@login_required
def Room_Booking(request):
    user_name = request.user
    user_n = User.objects.filter(username=user_name)
    print(user_n.values())
        
    roombooking_data = room_booking.objects.all()
    ava_rooms = rooms.objects.all()

    if ava_rooms.exists():
        availableRooms = ava_rooms[0].available_rooms
        print(availableRooms)
        print(type(availableRooms))
        total_rooms_ava = availableRooms
    else:
        total_rooms_ava = 0  # Set default value if no rooms 

    data = {
        'user_obj': user_n,
        'roombooking': roombooking_data,
        'Aroom': ava_rooms
    }
        
    if request.method == 'POST':
        username = request.POST.get('uname')
        place = request.POST.get('place')
        purpose = request.POST.get('purpose')
        booking_date = request.POST.get('today')  
        check_in_time = request.POST.get('checkIn')
        check_out_time = request.POST.get('checkOut')
        male = int(request.POST.get('maleGuests'))
        female = int(request.POST.get('femaleGuests'))
        children = int(request.POST.get('childrenGuests'))
        total_rooms = int(request.POST.get('rooms'))
        total_amount = int(request.POST.get('cost'))

        total_guests = male + female + children         
        total_rooms_ava = availableRooms - total_rooms
        
        if total_rooms_ava <= 0:
                response_content = '''
                    <div style="text-align: center; margin-top: 20px; font-size: 24px;">
                        Room is not available.
                    </div>
                    <div id="redirect-message" style="text-align: center; margin-top: 10px; font-size: 18px;">
                        Redirecting in <span id="countdown">3</span> seconds...
                    </div>
                    <script>
                        // JavaScript countdown logic
                        var countdownElement = document.getElementById('countdown');
                        var seconds = 3;

                        function countdown() {
                            countdownElement.textContent = seconds;
                            seconds--;

                            if (seconds >= 0) {
                                setTimeout(countdown, 1000);  // Update countdown every second (1000 milliseconds)
                            } else {
                                window.location.href = '/Room_Booking';  // Redirect to donation page after countdown
                            }
                        }

                        // Start the countdown when the page loads
                        countdown();
                    </script>
                '''
                return HttpResponse(response_content)
            
        if total_guests <= 0:
                response_content = '''
                    <div style="text-align: center; margin-top: 20px; font-size: 24px;">
                        Total Guest must more than 0.
                    </div>
                    <div id="redirect-message" style="text-align: center; margin-top: 10px; font-size: 18px;">
                        Redirecting in <span id="countdown">3</span> seconds...
                    </div>
                    <script>
                        // JavaScript countdown logic
                        var countdownElement = document.getElementById('countdown');
                        var seconds = 3;

                        function countdown() {
                            countdownElement.textContent = seconds;
                            seconds--;

                            if (seconds >= 0) {
                                setTimeout(countdown, 1000);  // Update countdown every second (1000 milliseconds)
                            } else {
                                window.location.href = '/Room_Booking';  // Redirect to donation page after countdown
                            }
                        }

                        // Start the countdown when the page loads
                        countdown();
                    </script>
                '''
                return HttpResponse(response_content)   
        

        if ava_rooms.exists():
            ava_room_instance = ava_rooms[0]
            ava_room_instance.available_rooms = total_rooms_ava
            ava_room_instance.save()
        else:
            # Create a new rooms instance if none exists
            ava_room_instance = rooms(total_rooms=10, available_rooms=total_rooms_ava)
            ava_room_instance.save()

        en = room_booking(username=username, place=place, purpose=purpose,
                          booking_date=booking_date, check_in_time=check_in_time,
                          check_out_time=check_out_time, total_rooms=total_rooms,
                          total_amount=total_amount, male=male, female=female,
                          children=children, total_guests=total_guests)
        
        print(total_amount)
        client = razorpay.Client(auth=("rzp_test_8WbzVlHnGFIQf0","hDtGutmr7gsqeZGuv1a9zO8E"))
        print(client)
        payment = client.order.create({'amount': int(float(total_amount) * 100) , 'currency':'INR' ,  'payment_capture': '1'})
        
        en.save()
        user_data = User.objects.all()
        for a in user_data:
            b1 = a.email
        room_data = room_booking.objects.all()
        for a in room_data:
            b = a.username
            c = a.male
            d = a.female
            e = a.total_rooms
            f = a.total_amount
            g = a.check_in_time
            h = a.check_out_time
        
        subject = "Successfull Room Booking Message"
        message = "Thank you , "+str(b)+" for your room booking of "+str(f)+" Rupees.              Booking Information : Male : "+str(c)+",Female : "+str(d)+",Total Rooms : "+str(e)+"and your Check in Time is : "+str(g)+" Your Check Out time is : "+str(h)+"."
        from_email = 'templemanagementsystem66@gmail.com'
        # recipient_list = b
        send_mail(subject,message,from_email,[b1])

        return render(request, "Room_Booking.html", {'user_obj': user_n, 'roombooking': roombooking_data,'Aroom': ava_rooms, 'payment' : payment , 'flag' : '1'})

    return render(request, "Room_Booking.html", data)



def Schedule(request):
    return render(request, "Schedule.html")


def scienceAndReligions1(request):
    return render(request, "scienceAndReligions1.html")


def scienceAndReligions2(request):
    return render(request, "scienceAndReligions2.html")


def scienceAndReligions3(request):
    return render(request, "scienceAndReligions3.html")


def scienceAndReligions4(request):
    return render(request, "scienceAndReligions4.html")




def SignUp(request):
    if request.method == "POST":
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        username=request.POST.get('uname')
        email=request.POST.get('emailid')
        password1=request.POST.get('password')
        password2=request.POST.get('password2')
        
        if len(password1) < 6:
            response_content = '''
                    <div style="text-align: center; margin-top: 20px; font-size: 24px;">
                        Password must be at least 6 characters long..
                    </div>
                    <div id="redirect-message" style="text-align: center; margin-top: 10px; font-size: 18px;">
                        Redirecting in <span id="countdown">3</span> seconds...
                    </div>
                    <script>
                        // JavaScript countdown logic
                        var countdownElement = document.getElementById('countdown');
                        var seconds = 3;

                        function countdown() {
                            countdownElement.textContent = seconds;
                            seconds--;

                            if (seconds >= 0) {
                                setTimeout(countdown, 1000);  // Update countdown every second (1000 milliseconds)
                            } else {
                                window.location.href = '/SignUp';  // Redirect to donation page after countdown
                            }
                        }

                        // Start the countdown when the page loads
                        countdown();
                    </script>
                '''
            return HttpResponse(response_content)

        if password1 != password2:
            response_content = '''
                    <div style="text-align: center; margin-top: 20px; font-size: 24px;">
                        Password must be Same.
                    </div>
                    <div id="redirect-message" style="text-align: center; margin-top: 10px; font-size: 18px;">
                        Redirecting in <span id="countdown">3</span> seconds...
                    </div>
                    <script>
                        // JavaScript countdown logic
                        var countdownElement = document.getElementById('countdown');
                        var seconds = 3;

                        function countdown() {
                            countdownElement.textContent = seconds;
                            seconds--;

                            if (seconds >= 0) {
                                setTimeout(countdown, 1000);  // Update countdown every second (1000 milliseconds)
                            } else {
                                window.location.href = '/SignUp';  // Redirect to donation page after countdown
                            }
                        }

                        // Start the countdown when the page loads
                        countdown();
                    </script>
                '''
            return HttpResponse(response_content)
        
        try:
            if User.objects.get(username=username):
                response_content = '''
                    <div style="text-align: center; margin-top: 20px; font-size: 24px;">
                        This username is already taken.
                    </div>
                    <div id="redirect-message" style="text-align: center; margin-top: 10px; font-size: 18px;">
                        Redirecting in <span id="countdown">3</span> seconds...
                    </div>
                    <script>
                        // JavaScript countdown logic
                        var countdownElement = document.getElementById('countdown');
                        var seconds = 3;

                        function countdown() {
                            countdownElement.textContent = seconds;
                            seconds--;

                            if (seconds >= 0) {
                                setTimeout(countdown, 1000);  // Update countdown every second (1000 milliseconds)
                            } else {
                                window.location.href = '/SignUp';  // Redirect to donation page after countdown
                            }
                        }

                        // Start the countdown when the page loads
                        countdown();
                    </script>
                '''
            return HttpResponse(response_content)
                
        except Exception as identifier:
            pass    

        user = User.objects.create(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
        user.password=make_password(user.password)
        user.save()
        user.is_active=False
        user.save()
        # To sending the emails to users
        email_subject="Activate Your Account by submitting the OTP." 
        otp=generate_otp()
        request.session['verification_data'] = {'otp': otp, 'username': username}
        message = render_to_string('activate.html',{
            'user':user,
            'otp':otp,

        })
        print(otp)
        # message=f'Your OTP for login activation is: {otp}'
        email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email],)
        email_message.send()
        messages.success(request,"Activate your account by clicking the link in your Gmail.")
        
        return redirect('Verification_otp') 
    
    return render(request,"SignUp.html")

def Verification_otp(request):
    if request.method == 'POST':
        entered_otp=request.POST.get('otp')
        entered_otp = int(entered_otp)

        verification_data = request.session.get('verification_data')
        if verification_data is None:
            messages.error(request, "Session data not found. Please retry the verification process.")
            return redirect('SignUp.html')
        
        stored_otp = verification_data.get('otp')
        username = verification_data.get('username')
        user= get_user_model().objects.get(username=username)

        print(stored_otp)

        if entered_otp ==stored_otp:
            user.is_active = True
            user.save()

            # Clear OTP from session
            del request.session['verification_data']

            print("success")
            messages.success(request, "Your account has been activated successfully!")
            return redirect('SignIn') 
        else:
            # OTP verification failed
            print("unsuccess")
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect('SignUp')

    return render(request,'otp.html')


def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        print("Received username:", username)
        print("Received password:", password)
        
        users=User.objects.all()
        print(users) 

        user = authenticate(request, username=username, password=password)
        print(user)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('/')
        else:
            messages.warning(request, "Invalid username or password. Please try again.")
            return redirect('SignUp')
    
    return render(request, "SignIn.html")



def handleLogout(request):
    logout(request)
    return redirect("/")


def Store(request):
    user_name = request.user
    user_n = User.objects.filter(username = user_name)
    print(user_n.values())
        
    product_data = Product.objects.all()
    
    data={
         'user_obj' : user_n ,
         'product_data' : product_data
    }
    
    if request.method == "POST":
        username=request.POST.get('uname')
        date=request.POST.get('today')
        items=request.POST.get('item')
        quantity=int(request.POST.get('qun'))
        price=request.POST.get('aprice')
        total_amount=request.POST.get('tprice')
        address=request.POST.get('address')
        area=request.POST.get('area')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        
        address = address + ", "+area+", "+ city 
        Order_data = Order.objects.all()
        
        product = Product.objects.get(title=items)
    
        if int(product.stock) < int(quantity):
            response_content = '''
                    <div style="text-align: center; margin-top: 20px; font-size: 24px;">
                        Product is out of Stock..
                    </div>
                    <div id="redirect-message" style="text-align: center; margin-top: 10px; font-size: 18px;">
                        Redirecting in <span id="countdown">3</span> seconds...
                    </div>
                    <script>
                        // JavaScript countdown logic
                        var countdownElement = document.getElementById('countdown');
                        var seconds = 3;

                        function countdown() {
                            countdownElement.textContent = seconds;
                            seconds--;

                            if (seconds >= 0) {
                                setTimeout(countdown, 1000);  // Update countdown every second (1000 milliseconds)
                            } else {
                                window.location.href = '/Store';  // Redirect to donation page after countdown
                            }
                        }

                        // Start the countdown when the page loads
                        countdown();
                    </script>
                '''
            return HttpResponse(response_content)
        
        product.stock -= quantity
        product.save()
        
        client = razorpay.Client(auth=("rzp_test_8WbzVlHnGFIQf0","hDtGutmr7gsqeZGuv1a9zO8E"))
        print(client)
        payment = client.order.create({'amount': int(float(total_amount) * 100) , 'currency':'INR' ,  'payment_capture': '1'})
        en = Order(username=username,date=date,items=items,price=price,quantity=quantity,total_amount=total_amount,address=address,state=state,pincode=pincode)
        en.save()
        return render(request, "Room_Booking.html", {'user_obj': user_n, 'product_data' : product_data, 'payment' : payment , 'flag' : '1'})    
    
    return render(request, "Store.html",data)


def Feedback(request):
        user_name = request.user
        user_n = User.objects.filter(username = user_name)
        print(user_n.values())
        
        feedback_data = feedback.objects.all()
    
        data={
             'user_obj' : user_n ,
             'feedback' : feedback_data
        }
        
        if request.method=='POST':
            name = request.POST.get('uname')
            date = request.POST.get('today')
            state = request.POST.get('state')
            text = request.POST.get('feedback')
            
            en = feedback(username=name,date=date,state=state,feedback=text)
            en.save()


        return render(request, "Feedback.html",data)

    

def generate_otp():
    return random.randint(100000, 999999)




