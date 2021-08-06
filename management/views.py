from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from .models import *

def post_list(request):
	introduce = Introduce1.objects.all()[0]
	banner = Introduce2.objects.all()[0]
	#print(banner)
	return render(request, 'management/post_list.html', {'introduce':introduce1, 'banner':introduce2})

def contact(request):
	return render(request, 'management/contact.html', {})

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
		title = request.POST['title']
		contents = request.POST['contents']
		company = request.POST['company']
		phone_number = request.POST['phone_number']
		email = request.POST['email']
		file = request.FILES['file']
		post_request = Request(title=title, contents=contents, company=company, phone_number=phone_number, email=email, video_contents=file)
		post_request.save()
		return HttpResponseRedirect('/')
	else:
		return render(request, 'contact.html')