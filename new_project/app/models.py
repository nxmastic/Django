from django.db import models

# Create your models here.
class Board(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=5000)
#db를 관리하는곳, db에 대해 정의함

class Comment(models.Model):
    board = models.ForeignKey('app.Board', on_delete=models.CASCADE, related_name='comments')  #ForeignKey를 통해 Board 와 연결시킴 , related_name은 무엇을 참조할지 설정함
    content = models.TextField()

