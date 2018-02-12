from django.shortcuts import render
from restaurants.models import Restaurant

def list(request):
	context = {
		"restaurants": Restaurant.objects.all()
	}
	return render (request, 'list.html', context)

def detail(request, restaurant_id):
	context = {
		"restaurant": Restaurant.objects.get(id = restaurant_id)
	}
	return render (request, 'detail.html', context)
	# {
	# "jobs":[
	# { "career": "nuclear medicine tech",
	# "description":"make the pt hot!",
	# "working_time":"6hr/7days"}, 

	# { "career": "nuclear medicine",
	# "description":"make the pt hot!",
	# "working_time":"6hr/7days"},

	# { "career": "nuclear medicine",
	# "description":"make the pt hot!",
	# "working_time":"6hr/7days"}
	# ],
	# }

	# return render(request, "detail.html", context) 
