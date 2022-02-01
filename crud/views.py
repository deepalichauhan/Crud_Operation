
# from curses import get_message
from curses import KEY_MESSAGE
from django.shortcuts import render, redirect
from .models import Member
from django.contrib import messages
from tkinter import *
from tkinter import messagebox
import time

# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/index.html', context)

def create(request):
    member = Member(firstname=request.POST['firstname'], 
    lastname=request.POST['lastname'], address= request.POST['address'])
    member.save()
    return redirect('/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)


def update(request, id):
    member = Member.objects.get(id=id)
    # Context = {'members': members}
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.address = request.POST['address']
    member.save()
    return redirect('/crud/')



def delete(request, id):
    res = messagebox.askokcancel('Confirmation', 'Do you want to delete the record?.....')
    if res == True:
        member = Member.objects.get(id=id)
        member.delete()
        return redirect('/crud/')
    elif res == False:
        return redirect('/crud/')
    else:
        messagebox.showerror('error', 'something went wrong!')


     
    