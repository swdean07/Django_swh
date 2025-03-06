from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return render(request, "main.html")
    # return HttpResponse("안녕하세요. 장고 웹 프레임워크~~ Hello World")

def lunch_list(request):
    return render(request, "lunch_list.html")
    # return HttpResponse("lunch_list : 점심 메뉴입니다.")

def introduce(request):
    return HttpResponse("hello. this is swh.")

def sports(request):
    return render(request, "spo.html")

def music(request):
    return render(request, "muse.html")

def animal(request):
    return render(request, "ani.html")

def weather(request):
    return render(request, "wea.html")