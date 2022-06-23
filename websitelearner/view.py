from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    # data={
    #     'title':'Data transfer - home page title',
    #     'data': 'Learning django',
    #     'clist': ['php', 'java', 'python'],
    #     'numbers':[30,20,16,45,65,26,60,19,90,57,71,37,82],
    #     'student_details':[
    #         {'name':'Jai', 'phone':353433544343},
    #         {'name':'Rai', 'phone':4653543},

    #     ]
    # }
    # return render(request, 'index.html', data)
    return render(request, 'index.html')

# about us integrating

def aboutus(request):
    return render(request, 'about.html')

def blog(request, courseid):
    return HttpResponse(courseid)

def homepage(request):
    return HttpResponse("hi, I love django lang")

def contact(request):
    return render(request, 'contact.html')

def feature(request):
    return render(request, 'feature.html')
    
def project(request):
    return render(request, 'project.html')
    
def quote(request):
    return render(request, 'quote.html')
    

def service(request):
    return render(request, 'service.html')
    
def team(request):
    return render(request, 'team.html')
    
def testimonial(request):
    return render(request, 'testimonial.html')

def fourzerofour(request):
    return render(request, '404.html')

def userform(request):
    finalans=0
    data={}
    try:
        if request.method == 'POST':
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            print(n1+n2)
            finalans=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }

            url='/thank-you/?output={}'.format(finalans)

            return redirect(url)
    except:
        pass
    return render(request, 'userform.html',  data)
    
def thankyou(request):
    if request.method=='GET':
        output=request.GET.get('output')

    return render(request, 'thank-you.html',{'output':output} )