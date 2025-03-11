from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField("게시판 제목", max_length=100)
    content = models.TextField("게시판 제목")

    def __str__(self):
        return self.title

class Reply(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField("댓글 내용")

    def __str__(self):
        return f"{self.board.title}의 댓글 ID:{self.id}"