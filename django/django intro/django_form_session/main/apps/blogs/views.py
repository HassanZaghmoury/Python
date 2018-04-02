from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, "blogs/index.html")



def create(request):
    if request.method == "POST":
        print "*"*80
	print request.POST
    print request.POST['name']
    print request.POST['desc']
    request.session['name'] = request.POST['name']
    request.session['desc'] = request.POST['desc']
    
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] = request.session['counter'] + 1
    print request.session['counter']
    print "*"*80
    return redirect("/")

def delete(request):
    del request.session["counter"]
    return redirect("/")