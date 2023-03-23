from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .models import Expense
# Create your views here.
def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        descrption = request.POST['description']
        date = request.POST['date']
        amount = request.POST['expense']
        objectexpense = Expense()
        objectexpense.name = name
        objectexpense.category = category
        objectexpense.description = descrption
        objectexpense.dateOfExpense = date
        objectexpense.amount = amount
        objectexpense.created_by = request.user.username
        objectexpense.save()
        # print(name, category, descrption, date, amount)
        return redirect(request.META.get('HTTP_REFERER'))
def update(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        category = request.POST['category']
        descrption = request.POST['description']
        date = request.POST['date']
        amount = request.POST['expense']
        objectexpense = Expense(pk=id)
        objectexpense.name = name
        objectexpense.category = category
        objectexpense.description = descrption
        objectexpense.dateOfExpense = date
        objectexpense.amount = amount
        objectexpense.save()
        return redirect(request.META.get('HTTP_REFERER'))
def delete(request):
    if request.method == 'GET':
        id = request.GET['idvalue']
        instance = Expense(pk=id)
        instance.delete()
    return redirect(request.META.get('HTTP_REFERER'))

