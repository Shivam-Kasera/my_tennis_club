from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q
# Create your views here.


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "mymembers": mymembers
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember": mymember
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template("testing.html")
    fruits = ["Apple", "Mango", "Banana", "Graps"]
    # cars = [
    #     {"brand": "Toyota", "model": "Camry", "year": 2020},
    #     {"brand": "Honda", "model": "Civic", "year": 2019},
    #     {"brand": "Ford", "model": "Mustang", "year": 2021},
    #     {"brand": "Tesla", "model": "Model S", "year": 2022},
    #     {"brand": "Chevrolet", "model": "Corvette", "year": 2018}
    # ]
    # emptyObj = []
    allMembers = Member.objects.all()
    firstName = Member.objects.values_list("firstName")
    specificRow = Member.objects.filter(firstName = "Emil")
    filterWithAND = Member.objects.filter(lastName = "Refsnes", id=2)
    filterWithOR = Member.objects.filter(firstName='Emil').values() | Member.objects.filter(firstName='Tobias').values()
    filterWithQExpression = Member.objects.filter(Q(firstName="Emil") | Q(firstName="Tobias")).values()
    filterWithFieldLookups = Member.objects.filter(firstName__startswith="L").values()
    context = {
        "fruits": fruits,
        # "cars": cars,
        # "members": members,
        # "emptyObj": emptyObj
        "mymembers": allMembers,
        "firstName": firstName,
        "specificRow": specificRow,
        "filterWithAND": filterWithAND,
        "filterWithOR": filterWithOR,
        "filterWithQExpression": filterWithQExpression,
        "filterWithFieldLookups": filterWithFieldLookups
    }
    return HttpResponse(template.render(context, request))
