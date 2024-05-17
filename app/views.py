from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'home.html')


def checkout(request):
    return render()


def profile():
    pass


def catalog(request):
    return render(request,'catalog.html')


def service():
    pass


def login():
    pass


def logout():
    pass
