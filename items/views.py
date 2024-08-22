from django.shortcuts import render
from django.http import HttpResponse
def mobile(request,pid):
    mobiles=[{'id':1,"name":"xiomi note 9 pro","config":["8gb","256gb"],"price":10000,"camNum":3},
             {'id':2,"name":"samsung m34 pro","config":["8gb","256gb"],"price":150000,"camNum":2},
             {'id':3,"name":"vivo Y 22 pro plus","config":["6gb","256gb"],"price":17000,"camNum":2},
             {'id':4,"name":"oppo  note 9 pro","config":["8gb","256gb"],"price":122000,"camNum":4}]
    result=None
    for i in mobiles:
        if i.get('id')==pid:
            result=i
            break
    if result is not None:
        return HttpResponse (f'<p>Mobile name:{result.get("name")}<br>price:{result.get("price")} in indian rupee<br>Configuration:RAM:{result.get('config')}</p>')
    else:
        return HttpResponse ("OOOPPPSS!!! please enter valid number between 1-4")

def laptop(request,pid):
    laptops=[
    {'id':1,'name':"HP",'config':['16gb','1TB'],'cost':70000},
    {'id':2,'name':'Lenovo','config':['8gb','512gb'],'cost':10000},
    {'id':3,'name':'Dell','config':['32gb','1TB'],'cost':100000},
    {'id':4,'name':'MacBook','config':['0gb','512gb'],'cost':50}]
    result=None
    for item in laptops:
        if item.get('id')==pid:
            result=item
            break
    if result is not None:
        return HttpResponse(f"<p>Laptop Name: {result.get('name')}<br>Cost: {result.get('cost')} <br>Configuration: {result.get('config')}</p>")
    else:
        return HttpResponse("OOOPPPSS!!! please enter valid number between 1-4 ")
    

def airpod(request,pid):
    airpods=[
    {'id':1,'name':"Airpods Pro gen1",'cost':26000},
    {'id':2,'name':'TWS','cost':10000},
    {'id':3,'name':'Noise','cost':100},
    {'id':4,'name':'onePlus','cost':10}]
    result=None
    for item in airpods:
        if item.get('id')==pid:
            result=item
            break
    if result is not None:
        return HttpResponse(f"<p>Brand Name: {result.get('name')}<br>Cost: {result.get('cost')}</p>")
    else:
        return HttpResponse("Sorry Dude NO result matched")