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