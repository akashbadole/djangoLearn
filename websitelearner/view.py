from django.shortcuts import render
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
