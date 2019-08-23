from django.shortcuts import render


def shop(request):
	return render(request, 'shop/home.html', {'title':'Homepage'})

def about(request):
	return render(request, 'shop/about.html', {'title':'About'})

def pricing(request):
	return render(request, 'shop/pricing.html', {'title':'Pricing'})

def contact(request):
	return render(request, 'shop/contact.html', {'title':'contact'})


