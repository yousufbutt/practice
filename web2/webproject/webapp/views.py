
from django.shortcuts import render
from django.http import Http404
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from django.template import loader
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
	
	return render(request, 'webapp/index.html', {})

def input(request):
	return render(request, 'webapp/input.html', {})


def upload_file(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = DocumentForm()
	return render(request, 'core/model_form_upload.html', {
		'form': form
	})



	"""print ("JLANLJNJLND")
	if request.method == 'POST' and request.FILES['myfile']:
		print ("SUCCESS")
		file = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(file.name, myfile)
		uploaded_file_url= fs.url(filename)
		return render(request, 'webapp/index.html', {
				'uploaded_file_url' : uploaded_file_url
			})
	print ("FAILURE")
	return render(request, 'webapp/index.html')"""