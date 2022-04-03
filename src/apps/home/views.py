from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
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
import threading



def driver(site):
    try:
        # print('driver',site)
        driver = webdriver.Remote("http://192.168.0.111:4444/wd/hub", DesiredCapabilities.CHROME)  #Driver ip Was pre set by the compose.yml
        driver.implicitly_wait(1)
        driver.set_page_load_timeout(5)
        driver.get('http://'+site)  # we are taking request.POST['siteinput']. hold out Site var and adding http:// to it
        # mybase= driver.get_screenshot_as_base64()  #local var to hold our image in Base64
        driver.quit() #kill driver
        print('driver done')
    except:
        print('driver failed')
        driver.quit() #kill driver

def mybot(request):
    print('starting')
    try:
        driver = webdriver.Remote("http://192.168.0.111:4444/wd/hub", DesiredCapabilities.CHROME)  #Driver ip Was pre set by the compose.yml
        driver.implicitly_wait(10) #lazy timeout
        driver.set_page_load_timeout(10) #no res timeout
        driver.get('http://'+request.POST['siteinput'])  # we are taking request.POST['siteinput']. hold out Site var and adding http:// to it
        mybase= driver.get_screenshot_as_base64()  #local var to hold our image in Base64
        driver.quit() #kill driver

        return HttpResponse('<div class="text-center">נשלח בהצלחה! <img class="mx-auto" src="data:image/jpeg;base64,'+mybase+'"> </div>')  #build image with base64 and return it.
    except:
        try:
            driver.quit() #kill driver

        except:
            print('no driver') 

        return HttpResponse('<div class="text-center">משהו השתבש!</div>')  #the driver didnt get the target.

def myposttest(request):
    print('starting post test')

    if request.method =='POST':
        # print(request)
        return HttpResponse('<div class="text-center">נשלח בהצלחה POST! <p>'+request.POST['mydata']+'</p></div>')
    
    if request.method =='GET':
        # print(request.GET)
        return HttpResponse('<div class="text-center">נשלח בהצלחה GET! <p>'+request.GET['mydata']+'</p></div>')



    return HttpResponse('<div class="text-center">משהו השתבש!</div>')  #Not post

import os
import psutil

def Dropletuse(request):

    
    # Getting loadover15 minutes
    load1, load5, load15 = psutil.getloadavg()
    
    cpu_usage = (load15/os.cpu_count()) * 100
    
    # print("The CPU usage is : ", cpu_usage)

    obj_dict = {
               'cpu': round(cpu_usage,1),
               'ram': round(psutil.virtual_memory()[2],1)
            }
    return render(request, 'chucky/serverstat.html', context=obj_dict)

def canibals(request):

    if request.method =='POST':
        # print(request.POST['mydata'])
        for i in range(int(request.POST['mydata'])):
            # print(i)
            x = threading.Thread(target=driver, args=('192.168.0.110:8001',))
            x.start()

        return HttpResponse('<div class="text-center">נשלח בהצלחה GET! <p>ניתן לצפות בפעולה בלוגים של השרת או בסילניום גריד</p></div>')

    
    return HttpResponse('<div class="text-center">משהו השתבש!</div>')  #Not post


def error_404_view(request, exception):
    print('404')
    return HttpResponse('<div class="text-center">משהו השתבש! <p>הדגמת איסוף שגיאה 404 על כל השרת</p></div>')  #Not post
    







