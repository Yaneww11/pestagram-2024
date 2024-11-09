from django.shortcuts import render

def home_page(request):
    context = {'username' : 'Yane'}
    return render(request, 'common/home-page.html', context)
