from django.shortcuts import render, redirect
from django.http import HttpResponse
from fees.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def home(request):
    return render(request,'home.html')
def main_menu(request):
    if not request.user.is_authenticated:
        return redirect('../adm-login')
    s= StudentDetail.objects.all()
    return render(request, 'main_menu.html', locals())
def adm_login(request):
   return render(request,'admin_login.html')
def admin_login(request):
    error= ""
    u=request.GET['username']
    p=request.GET['pwd']
    user=authenticate(username=u, password=p)
    if user !=None :
        login(request,user)
        return redirect('../main-menu')
    else:
       return redirect('../adm-login')
def admin_logout(request):
    logout(request)
    return redirect('../adm-login')
def insert_student_details(request):
    if not request.user.is_authenticated:
        return redirect('../adm-login')
    return render(request,'insert_student_details.html')
s= StudentDetail()
def ins_student_details(request):
    s= StudentDetail()
    s.name=request.GET['a1']
    s.guardianName=request.GET['a2']
    s.studentId=request.GET['a3']
    s.amount=request.GET['a4']
    s.admissionDate=request.GET['a5']
    s.std=request.GET['a6']
    s.save()
    return redirect('../main-menu')
def insert_fees_record(request):
    if not request.user.is_authenticated:
        return redirect('../adm-login')
    return render(request,'insert_fees_record.html')
def ins_fees_record(request):
    s.jan=request.GET['a7']
    s.feb=request.GET['a8']
    s.mar=request.GET['a9']
    s.april=request.GET['a10']
    s.may=request.GET['a11']
    s.june=request.GET['a12']
    s.july=request.GET['a13']
    s.aug=request.GET['a14']
    s.sept=request.GET['a15']
    s.oct=request.GET['a16']
    s.nov=request.GET['a17']
    s.dec=request.GET['a18']
    s.save()
    return redirect('../feesrecord')
def dele(request,id):
    d= StudentDetail.objects.get(id=id)
    d.delete()
    return redirect('../main-menu')
def edit(request,id):
    if not request.user.is_authenticated:
        return redirect('../adm-login')
    e=StudentDetail.objects.get(id=id)
    return render(request,'edit.html',{'e':e})
def edcode(request,id):
    e=StudentDetail.objects.get(id=id)
    e.name=request.GET['a1']
    e.guardianName=request.GET['a2']
    e.studentId=request.GET['a3']
    e.amount=request.GET['a4']
    e.std=request.GET['a6']
    e.save()
    return redirect('../main-menu')
def edit_admission_date(request,id):
    if not request.user.is_authenticated:
        return redirect('../adm-login')
    e=StudentDetail.objects.get(id=id)
    return render(request,'edit_admission_date.html',{'e':e})
def edcode_admission_date(request,id):
    e=StudentDetail.objects.get(id=id)
    e.admissionDate=request.GET['a5']
    e.save()
    return redirect('../main-menu')
def edit_fees_record(request,id):
    if not request.user.is_authenticated:
        return redirect('../adm-login')
    e=StudentDetail.objects.get(id=id)
    return render(request,'edit_fees_record.html',{'e':e})
def edcode_fees_record(request,id):
    e=StudentDetail.objects.get(id=id)
    e.jan=request.GET['a7']
    e.feb=request.GET['a8']
    e.mar=request.GET['a9']
    e.april=request.GET['a10']
    e.may=request.GET['a11']
    e.june=request.GET['a12']
    e.july=request.GET['a13']
    e.aug=request.GET['a14']
    e.sept=request.GET['a15']
    e.oct=request.GET['a16']
    e.nov=request.GET['a17']
    e.dec=request.GET['a18']
    e.save()
    return redirect('../feesrecord')
def feesrecord(request):
    if not request.user.is_authenticated:
        return redirect('../adm-login')
    s= StudentDetail.objects.all()
    return render(request, 'feesrecord.html', locals())
def credits(request):
    if not request.user.is_authenticated:
        return redirect('../adm-login')
    return render(request, 'credits.html')
