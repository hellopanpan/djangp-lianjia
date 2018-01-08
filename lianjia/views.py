from django.shortcuts import render
from lianjia.models import Area ,Login,Lianjia
# Create your views here.
from django.http import HttpResponse
from django.core import serializers
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import types

def showlist(request):
	result = Lianjia.objects.all()
	json_data = serializers.serialize("json", result)
	return HttpResponse(json_data, content_type="application/json")

def login(request):
	try:
		user = request.POST["user"]
		password = request.POST["password"]
		login = Login.objects.filter(name= user).filter(password=password)
		leng = len(login)
		if leng> 0 :
			return HttpResponse("success")
		else:
			return HttpResponse("no the user")
	except:
		return HttpResponse("try to login again")
def register(request):
	try:
		user = request.POST["user"]
		password = request.POST["password"]
		ifname = Login.objects.filter(name = user)
		if len(ifname)> 0 :
			return HttpResponse("exist")
		else:
			register = Login(name=user,password=password)
			register.save()
			return HttpResponse("success")
	except:
		return HttpResponse("error")

def index(request):
	area = Area.objects.all()
	return render(request, 'index.html')

def page1(request):
	return render(request,"login.html")

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a)+int(b)
	area = Area(name=str(a),age=c)
	area.save()
	return HttpResponse(str(c))

def template(request,a,b):
	Area.objects.filter(name="1").delete()
	info_dict = area = Area.objects.all()
	c = int(a) +int(b);
	return render(request, 'index.html', {'info_dict': info_dict,"c":c})