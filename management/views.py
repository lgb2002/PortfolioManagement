from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.utils import timezone
from .models import *

def post_list(request):
	introduce1 = Introduce1.objects.all()[0]
	introduce2 = Introduce2.objects.all()[0]
	#print(banner)
	return render(request, 'management/post_list.html', {'introduce1':introduce1, 'introduce2':introduce2})

def contact(request):
	return render(request, 'management/contact.html', {})

def send(request):
	if request.method == "GET":
		devid = request.GET["devid"]
		time = request.GET["time"]
		data = {
            "result": "success"
        }
		return JsonResponse(data)
	else:
		return render(request, 'management/data.html')

def data(request):
	return render(request, 'management/data.html')

def test(request):
	return render(request, 'management/test.html', {})

def test2(request):
	return render(request, 'management/test2.html', {})

def admin(request):
	return render(request, 'management/admin.html', {})

def portfolio(request):
	coworkers = Coworker.objects.all().order_by('id')

	portfolios = Portfolio.objects.all().order_by('id')
	return render(request, 'management/portfolio.html', {'posts':portfolios, 'coworkers':coworkers})

def post_contact(request):
	if request.method == "POST":
		#title = request.POST['title']
		budget = request.POST['budget']
		contents = request.POST['contents']
		company = request.POST['company']
		phone_number = request.POST['phone_number']
		email = request.POST['email']
		#file = request.FILES['file']
		#post_request = Request(title=title, contents=contents, company=company, phone_number=phone_number, email=email, video_contents=file)
		post_request = Request(budget=budget, contents=contents, company=company, phone_number=phone_number, email=email)
		post_request.save()
		return HttpResponseRedirect('/')
	else:
		return render(request, 'contact.html')