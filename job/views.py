from django.shortcuts import render
from .models import Job
from .forms import form1
# Create your views here.
def job(request):
	form= form1()
	if request.method == 'POST':
		form = form1(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			father_name = form.cleaned_data['father_name']
			cnic = form.cleaned_data['cnic']
			email = form.cleaned_data['email']
			phone_no = form.cleaned_data['phone_no']
			experience = form.cleaned_data['experience']
			address = form.cleaned_data['address']
			current_city = form.cleaned_data['current_city']
			obj = Job.objects.create(name=name, father_name=father_name, cnic=cnic, email=email, phone_no=phone_no, experience=experience, address=address, current_city=current_city)
			obj.save()
			messages = "Thanks"
			return render(request, 'job.html', {'messages': messages})
	return render(request, 'job.html',{'form':form})

def check(request):
	if request.method == 'POST':
		security = request.POST.get('security')
		if security == "Enter":
			context = Job.objects.all()
			return render(request, 'check.html', {'context':context})
		else:
			print(security)

	return render(request, 'check.html')