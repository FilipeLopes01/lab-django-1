from django.shortcuts import render

def temporada2021(request):
	return render(request, 'website/temporada2021.html')

def piloto1(request):
	return render(request, 'website/piloto1.html')

def piloto2(request):
	return render(request, 'website/piloto2.html')

