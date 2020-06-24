from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from shortner.models import Urls
from shortner.forms import URLForm
import hashlib


def home(request):
	form = URLForm()
	return render(request, 'shortner/index.html', {"form": form})


def shrink(request):
	form = URLForm(request.POST)
	if form.is_valid():
		data = form.cleaned_data
		url = data["targetURL"]
		hash = data["hash"]

		encryption = hashlib.md5(url.encode('utf-8') + hash.encode('utf-8'))
		shrinkedURL = encryption.hexdigest()
		try:
			check = Urls.objects.get(shrinkedURL=shrinkedURL)
		except Urls.DoesNotExist:
			entry = Urls(shrinkedURL=shrinkedURL, targetURL=url)
			entry.save()

		return render(request, 'shortner/index.html',{
				'shrinkedURL':shrinkedURL, "form": form
			})


def retrieve(request,inputURL):
	target = get_object_or_404(Urls, shrinkedURL=inputURL)
	targetURL = target.targetURL
	if(targetURL[:4] != 'http'):
		targetURL = 'http://'+targetURL
	return redirect(targetURL)