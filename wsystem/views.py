from django.shortcuts import render, redirect
from django.utils import timezone
# Create your views here.
from django.http import HttpResponse
from django.urls import reverse
import datetime
from .models import CustomerTable, OrdersTable


def index(request):
    return render(request, 'wsystem/index.html')



def signin(request):
    inputUsername = request.POST['inputUsername']
    inputPassword = request.POST['inputPassword']
    try:
        user = CustomerTable.objects.get(username=inputUsername)
    except:
        return render(request, 'wsystem/errUserOrPass.html')
    if(user.password == inputPassword):
        request.session['userid'] = user.id
        return redirect(reverse('wsystem:orderlist'))
    return render(request, 'wsystem/errUserOrPass.html')

def orderList(request):
        userid = request.session['userid']
        print(userid)
        user = CustomerTable.objects.get(id=userid)
        orderlist = OrdersTable.objects.filter(username_id=userid)
        context = {'ListName': '订单列表', 'list': orderlist, 'user': user}
        return render(request, 'wsystem/OrderList.html', context)
#

def addOrder(request):
    userid = request.session['userid']
    user = CustomerTable.objects.get(id=userid)
    context = {'user': user}
    return render(request, 'wsystem/addOrder.html', context)

def addOrderList(request):
    userid = request.session['userid']
    isD = OrdersTable.objects.filter(username_id=userid, time__day=timezone.now().day)
    print(isD)
    if (len(isD) > 0):
        return render(request, 'wsystem/errWater .html')
    user = CustomerTable.objects.get(id=userid)
    nor = OrdersTable()
    nor.username = user
    nor.time = timezone.now()
    nor.money = request.POST['money']
    nor.wmodels = request.POST['wmodels']
    nor.nums = request.POST['nums']
    nor.paymodels = request.POST['paymodels']
    nor.save()
    return redirect(reverse('wsystem:orderlist'))