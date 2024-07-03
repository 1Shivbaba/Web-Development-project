from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render   
from services.models import Service
from about.models import About
from careers.models import Careers
from django.core.paginator import Paginator
from contact_inquiry.models import Contact_Inquiry
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def homepage(request):
#     send_mail(
#     "This is the test mail",
#     "Namaste Shivam!.",
#     "research.shubham219@gmail.com",
#     ["sojha1633@gmail.com"],
#     fail_silently=False,
# )

    serviceData = Service.objects.all().order_by('-service_title')[:4]
    # for a in serviceData:
    #      print(a.service_icon) 
    # # # print(services)
    data = {'title':'Welcome to Techtics',
            'serviceData':serviceData,
            }
    return render(request,'index.html', data)
   

def about(request):  
    about_data =  About.objects.all()   
    data = {'title':'About-us',
            'About_data':about_data,
            }
    return render(request,'about.html', data)


def services(request): 
    serviceData = Service.objects.all()
    P = Paginator(serviceData,4)
    page_number = request.GET.get('page')
    serviceFinalPage = P.get_page(page_number)
    totalpages = serviceFinalPage.paginator.num_pages

    # if request.method =='GET':
    #      st = request.GET.get("servicename")
    #      if st!=None:
    #         serviceData = Service.objects.filter(service_title__icontains=st)  # __icontains : for like a/as word search 

    data = {'title':'Our-Services',
            'serviceData':serviceFinalPage ,
            "lastpage":totalpages,
            "pagelist":[ n+1 for n in range(totalpages)]
            }
    return render(request,'service.html', data)

def career(request):
    data = { }
    try:
        ename = request.POST['emname']
        email = request.POST.get('emmail')
        number = request.POST['mobile']
        emql = request.POST.get('emquali')
        efile = request.POST.get('emfile')
        emsg = request.POST.get('emessage')

        data = {'title':'Join our team-Career',
                'ename':ename,
                'email':email,
                'number':number,
                'emql':emql,
                'efile':efile,
                'emsg':emsg,
                }
        # return redirect('/about/')
    except Exception:
        pass 
    return render(request,'career.html', data)

def thank(request,thankyou):
    data = { }
    try:
        
        ename = request.POST['emname']
        email = request.POST.get('emmail')
        number = request.POST['mobile']
        emql = request.POST.get('emquali')
        empost = request.POST.get('position')
        efile = request.POST.get('emfile')
        emsg = request.POST.get('emessage')
        emaddress = request.POST.get('city')

        info = Careers(candidate_name=ename, candidate_mail=email, candidate_phone=number, candidate_quali=emql, candidate_post=empost, condidate_address=emaddress,condidate_message=emsg ,condidate_cv=efile)
        info.save()

        data = {'title':'Thanks-candidate',
                'ename':ename,
                'email':email,
                'number':number,
                'emql':emql,
                'efile':efile,
                'empost':empost,
                'emsg':emsg,
                'emaddress':emaddress,
                'error':True
                
                }
        # Email sending start: 
        subject = "Thanks to visit-Techtics technologies "
        from_email = settings.EMAIL_HOST_USER
        html_message = render_to_string('welcome.html',{'ename':ename})
        to_email = email
        Email = EmailMultiAlternatives(subject,html_message,from_email,[to_email])
        Email.attach_alternative(html_message, "html/text")
        Email.content_subtype= 'html'
# Send a Attech file  
                # with open("D://resume.pdf" 'rb') as f:
                #      Email.attach( "D://resume.pdf" , f.read(), 'application/pdf')
        Email.send()
        
    except Exception:
        pass 
    return render(request,'thankyou.html', data)

def contact(request): 
   data = { } 
   try:
       if request.method == 'POST':           
                
            name = request.POST['name']
            mail = request.POST.get('email')
            phone = request.POST.get('phone')
            sub = request.POST['subject']
            mes = request.POST.get('message')
            data = Contact_Inquiry(contact_name=name,contact_mail=mail, contact_phone=phone, contact_subject=sub, contact_message=mes)
            data.save()            
        
            data = {'title':'Contact-us',
                    'name':name,
                    'mail':mail,
                    'phone':phone,
                    'sub':sub,
                    'mes':mes, 
                    'error':True  
            }
            if request.POST.get('name')=="":
                            return render(request,'contact.html',data)
            if request.POST.get('email')=="":
                    return render(request,'contact.html',data)
            
            # return redirect('/contact/thanks', {'name':name})
       

   except:
    pass
   
   return render(request,'contact.html',data)

def mthanks(request,thanks): 
    data={ }
    try:
        if request.method =="POST":
                name = request.POST.get('name')
                mail = request.POST.get('email')
                phone = request.POST.get('phone')
                sub = request.POST['subject']
                mes = request.POST.get('message')

 #  Data Save in database 
                con = Contact_Inquiry(contact_name=name,contact_mail=mail, contact_phone=phone, contact_subject=sub, contact_message=mes)
                con.save()

                data  = {'title':'Thank-you-visitor',
                'name':name,
                }
# Email sending start: 
                subject = "Thanks to visit-Techtics technologies "
                from_email = settings.EMAIL_HOST_USER
                html_message = render_to_string('welcome.html',{'name':name})
                to_email = mail
                Email = EmailMultiAlternatives(subject,html_message,from_email,[to_email])
                Email.attach_alternative(html_message, "html/text")
                Email.content_subtype= 'html'
# Send a Attech file  
                # with open("D://resume.pdf" 'rb') as f:
                #      Email.attach( "D://resume.pdf" , f.read(), 'application/pdf')
                Email.send()
    except Exception:
        pass

    return render(request, 'thankyou.html', data )
    
 





def portfolio(request):      
    data = {'title':'Our-portfolio',
            }
    return render(request,'portfolio.html', data)

def pricing(request):      
    data = {'title':'Prices',
            }
    return render(request,'pricing.html', data)


def skills(request):      
    data = {'title':'Skills',
            }
    return render(request,'skill.html', data)

def Ourteam(request):      
    data = {'title':'Our-Team',
            }
    return render(request,'team.html', data)

def reviews(request):      
    data = {'title':'Reviews',
            }
    return render(request,'review.html', data)

def clients(request):      
    data = {'title':'Our-clients',
            }
    return render(request,'client.html', data)

def Singlepage(request):      
    data = {'title':'Single',
            }
    return render(request,'single.html', data)