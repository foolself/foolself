# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article, UploadFile
from .forms import UploadFileForm
from django.http import StreamingHttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import os

def index(request):
	file_list = UploadFile.objects.all()
	return render(request, "index.html", {"file_list" : file_list})

def handle_uploaded_file(f, path):
	t = path.split("/")
	file_name = t[-1]
	extensions = file_name.split(".")[1]
	t.remove(t[-1])
	t.remove(t[0])
	path = "/".join(t)
	try:
		if not os.path.exists(path):
			os.makedirs(path)
		file_name = path + "/" + file_name +"." + extensions
		destination = open(file_name, 'wb+')
		for chunk in f.chunks():
			destination.write(chunk)
			destination.close()
	except Exception, e:
		print e
	return file_name

def uploads(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			upload_file = UploadFile.objects.create(name = request.FILES['file'].name, file = request.FILES['file'])
			path = upload_file.file.url
			handle_uploaded_file(request.FILES['file'], path)
			upload_file.save()
			return redirect("blog.views.index")
	else:
		form = UploadFileForm()
	return render(request, 'index.html', {'form': form})

def download(request, f):
	t = f.split("/")
	file_name = t[-1]
	t.remove(t[-1])
	t.remove(t[0])
	file_path = "/".join(t)
	def file_iterator(file_name, file_path, chunk_size=512):
		path = file_path +"/" + file_name
		with open(path) as f:
			while True:
				c = f.read(chunk_size)
				if c:
					yield c
				else:
					break
	try:
		response = StreamingHttpResponse(file_iterator(file_name, file_path))
		response['Content-Type'] = 'application/octet-stream'
		response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name)
	except:
		return HttpResponse("Sorry but Not Found the File")
	return response