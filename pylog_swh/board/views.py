from django.shortcuts import render

from board.models import Board


# Create your views here.
def board_list(request):
    board = Board.objects.all()
    context = {
        'board': board,
    }
    return render(request, "board_list.html",context)
