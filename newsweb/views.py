from django.shortcuts import render

# Create your views here.

def home(request):
	import requests
	import json

	news_api_request = requests.get('http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=62de380cdfdc480683ffb6d2624e5ce7')

	api = json.loads(news_api_request.content)
	return render(request,'home.html',{'api':api})
