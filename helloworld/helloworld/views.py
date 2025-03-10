from django.http import HttpResponse
from django.shortcuts import render

from burgers.models import Burger
from coffee.models import Coffee


def main(request):
    return render(request, "main.html")
    # return HttpResponse("안녕하세요. 장고 웹 프레임워크~~ Hello World")

def lunch_list(request):
    return render(request, "lunch_list.html")
    # return HttpResponse("lunch_list : 점심 메뉴입니다.")

def introduce(request):
    return HttpResponse("hello. this is swh.")

def sports(request):
    # return HttpResponse("제가 좋아하는 스포츠는 축구")
    return render(request, "spo.html")

def music(request):
    # return HttpResponse("본인이 선호하는 음악 장르는 무엇인가요?")
    return render(request, "muse.html")

def animal(request):
    # return HttpResponse("개, 고양이, 판다")
    return render(request, "ani.html")

def weather(request):
    # return HttpResponse("오늘의 날씨는 흐림입니다.")
    return render(request, "wea.html")

def burger_list(request):
    burgers = Burger.objects.all()
    print("햄버거 전체 목록: ", burgers)
    context = {
        "burgers": burgers
    }
    return render(request, "burger_list.html", context)

def burger_search(request):
    # print(request.GET)
    keyword = request.GET.get("keyword")
    print(keyword)

    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    else:
        burgers = Burger.objects.none()

    context = {
        "burgers": burgers
    }
    print("조회된 내용: ", burgers)
    return render(request, "burger_search.html", context)

def cafe_list(request):
    coffees = Coffee.objects.all()
    print("커피 전체 리스트 목록: ", coffees)
    context = {
        "coffees": coffees
    }
    return render(request, "cafe_list.html", context)

def cafe_search(request):
    keyword = request.GET.get("keyword")
    print(keyword)

    if keyword is not None:
        coffees = Coffee.objects.filter(name__contains=keyword)
    else:
        coffees = Coffee.objects.none()

    context = {
        "coffees": coffees
    }
    print("조회된 내용: ", coffees)
    return render(request, "cafe_search.html", context)