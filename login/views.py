from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
from CRUD.models import Expense
# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            ObjectUser = User(username=email)
            if ObjectUser.is_staff == True:
                ObjectExpense = Expense.objects.all()
                return render(request, 'index.html' , {'expenses': ObjectExpense})
            ObjectExpense = Expense.objects.all().filter(created_by=email)
            print(email)
            return render(request, 'index.html', {'expenses':ObjectExpense})
        else:
            return render(request, 'login.html')
        print(email, password)

    elif request.user.is_authenticated:
        email = request.user.username
        Userinstance = User(username=email)
        print(Userinstance.is_superuser)
        print(email)
        ObjectExpense = Expense.objects.all().filter(created_by=email) if email != 'admin' else Expense.objects.all()
        return render(request, 'index.html', {'expenses':ObjectExpense, 'name': email})
    return render(request, 'login.html')


def logout_func(request):
    logout(request)
    return redirect('Login')

def search(request):
    naem = request.user.username
    if request.GET['filterdate'] and request.GET['search']:
        date = request.GET['filterdate']
        text = request.GET['search']
        instanceExpence = Expense.objects.all().filter(dateOfExpense=date , name=text)
        return render(request, 'search.html', {'expenses': instanceExpence, 'name': naem})

    elif request.GET['filterdate']:
        date = request.GET['filterdate']
        instanceExpence = Expense.objects.all().filter(dateOfExpense=date)
        return render(request, 'search.html', {'expenses': instanceExpence, 'name': naem})
    elif request.GET['search']:
        text = request.GET['search']
        instanceExpence = Expense.objects.all().filter(name=text)
        return render(request, 'search.html', {'expenses': instanceExpence, 'name': naem})