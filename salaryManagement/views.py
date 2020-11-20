from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from payroll.models import Contact

def home(request):
	return render(request,'main/home.html')
	
def about(request):
	# return HttpResponse('hr')
	return render(request,'main/about.html')
	
def contact(request):
	# name=request.post['name']
	if(request.method=='POST'):
		name=request.POST['name']
		email=request.POST['email']
		content=request.POST['content']
		contact=Contact(name=name,email=email,content=content)
		contact.save()
		messages.success(request,"Your query is sent successfully !!!")
		# return redirect('home')
		
	return render (request,"main/contact.html")
