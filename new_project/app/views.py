from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from django.template import loader
from django.http import HttpResponse
from .models import Board, Comment
from .forms import BoardForm, CommentForm

# Create your views here.
# board=[
#  {'id':1, 'title':'title1', 'content':'content1'},
#  {'id':2, 'title':'title2', 'content':'content2'},
#  {'id':3, 'title':'title3', 'content':'content3'},
# ]

class IndexView(ListView):
    template_name = 'app/index.html'
    # context_object_name = 'board'

    # def get_queryset(self):
    #     return Board.objects.all()



# def index(request):
#     board=Board.objects.all()
#     context={
#         'board' : board
#     }
#     return render(request,'app/index.html', context )


class BoardView(DetailView):
    template_name = 'app/board.html'
    context_object_name = 'board'
    model = Board
    #
    # def get_queryset(self):
    #     return Board.objects.filter(id=self.kwargs.get('pk'))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board'] = Board.objects.filter(id=self.kwargs.get('pk')).first()
        context['form'] = CommentForm
        return context

# def boardDetail( request, boardId ) :
#     retBoard=Board.objects.filter(id=boardId).first()
#     context={
#         'board': retBoard,
#     }
#     return render(request, 'app/board.html', context)

def newBoard(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/app')
    else:
    #
        form = BoardForm()
    context={
        'form' : form
    }
    return render(request, 'app/new.html', context)

def deleteBoard(request,pk):
    delBoard= Board.objects.filter(id=pk).first()
    delBoard.delete()
    return redirect('/app')

def newComment(request,pk):
    if request.method == 'POST':
        board=Board.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)   # False 처리를 통해 저장을 시도 안함,참조식으로 바뀜
            comment.board= board
            comment.save()
        return redirect('/app/board/' + str(pk))
    else:
        return redirect('/app')









# request는 client로부터 server로 데이터를 넘기게 하는 작업, 이거에 대한 응답이 response
# return HttpResponse(template.render(context, request))랑 동일

#MVT(model-view-template)형식, 왼쪽으로 서버랑 가깝고 오른쪽으로 가까울수록 클라이언트랑 가까움, 왼쪽->db 존재,오른쪽->page 존재
#model이 필요한 정보를 가져와 views 에 넘겨 가공을 한뒤 template 에 전달
