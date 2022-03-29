from django import get_version
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

#Class Base Demo. Serve home.html
class HomeServe(TemplateView):
    template_name = 'home.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] ="סייבר"
        if settings.DEBUG==True:
            context['secstate']="השרת במצב לא מאובטח!!"
        else:
            context['secstate']="השרת מאובטח"
        return context

#Function Based (will get page name from the htmx request)
def pathme(request):
    mainelement=request.GET.get('query_set')
    return render(request, 'chucky/'+mainelement+'.html')


### 3rd party
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from PIL import Image
# import docker

def mybot(request):
    print('starting')
    try:
        driver = webdriver.Remote("http://192.168.0.111:4444/wd/hub", DesiredCapabilities.CHROME)  #Driver ip Was pre set by the compose.yml
        driver.get('http://'+request.POST['siteinput'])  # we are taking request.POST['siteinput']. hold out Site var and adding http:// to it
        mybase= driver.get_screenshot_as_base64()  #local var to hold our image in Base64
        driver.quit() #kill driver

        return HttpResponse('<div class="text-center">נשלח בהצלחה! <img class="mx-auto" src="data:image/jpeg;base64,'+mybase+'"> </div>')  #build image with base64 and return it.
    except:
        return HttpResponse('<div class="text-center">משהו השתבש!</div>')  #the driver didnt get the target.



def myposttest(request):
    print('starting post test')

    if request.method =='POST':
        return HttpResponse('<div class="text-center">נשלח בהצלחה POST! <p>'+request.POST['mydata']+'</p></div>')
    
    if request.method =='GET':
        print(request.GET)
        return HttpResponse('<div class="text-center">נשלח בהצלחה GET! <p>'+request.GET['mydata']+'</p></div>')



    return HttpResponse('<div class="text-center">משהו השתבש!</div>')  #Not post
    

# def formgetter(request):
#     mainelement=request.GET.get('query_set')

#     print('my main element ',mainelement)

#     if request.method =='POST':
#         print(request.POST)
#         mylist=request.POST.getlist('course')
#         filterit= myobjects.objects.all()
#         filterit =filterit.filter(course_code__in=mylist)
#         print(filterit)
#     obj_dict = {
#     'mainelement': mainelement,
#     'waldo': mylist,
#     'myfilt':filterit
#     }
#     return render(request, 'chucky/getpart.html', context=obj_dict)

# def error_404_view(request, exception):
#     data = {"name": "שגיאה 404"}
#     return render(request,'404.html', data)
    







