from django.http import HttpResponse
from django.conf import settings
from kelaskita.models import PageHit
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
	return render(request, 'kelaskita/index.html')

@csrf_exempt
def checkCount(request):
	print(request.POST.get('sessionBrowserId'))
	counts = 1
	try:
		uData = PageHit.objects.using('basic').get(pagehit_session_id=request.POST.get('sessionBrowserId'))
		counts = uData.pagehit_count + 1
		uData.pagehit_count = counts
		uData.save(using='basic')
	except:
		uData = PageHit(pagehit_session_id=request.POST.get('sessionBrowserId'),pagehit_count=1)
		uData.save(using='basic')
	data = {}
	data['response'] = 'success'
	data['counts'] = counts
	return HttpResponse(
        json.dumps(data),
        content_type="application/json"
    )