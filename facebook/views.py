from django.shortcuts import render, redirect
from facebook.models import Article, Comment
# Create your views here.
#render은 페이지를 띄어줘라 redirect는 페이지를 이동해라

def newsfeed(request):
    #데이터베이스 모든 뉴스피드를 긁어오기

    articles = Article.objects.all()
    # 모든 글이 articles에 저장
    return render(request,'newsfeed.html',{'articles' : articles})



def new_feed(request):
    #1) 입력한 내용을 받아오기
    if request.method == 'POST':
        #2) 받아왔으면 그 글을 등록해라
        feed = Article.objects.create(
            author = request.POST['author'],
            title =request.POST['title'],
            text =request.POST['content'],
            password =request.POST['password'],
    )
        return redirect(f'/feed/{feed.pk}/')
    return render(request, 'new_feed.html')

def edit_feed(request, pk):
    # 수정할 글의 정보를 불러오기
    feed = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST['pw_e'] == feed.password:
            redirect(f'/feed/{feed.pk}/')
            return redirect('fail/')
        else:
            return redirect('/fail/')
        #2) 받은 정보로 수정해주세요
        feed.title = request.POST['title']
        feed.author = request.POST['author']
        feed.text = request.POST['content']
        feed.save()
        return redirect(f'/feed/{feed.pk}/')
        #f응 글자 feed.pk에 있는 실제 값으로 바꾸어줘라
        #save는 수정된 정보를 저장하게 되줌
        #'/feed/ + feed.pk'랑 같당!~!~!
    return render(request, 'edit_feed.html', {'feed': feed})

def remove_feed(request, pk):
    feed = Article.objects.get(pk=pk)
    if request.method == 'POST':
       #비밀번호를 확인하기(앞이 입력 정보 뒤가 DB정보)
       if request.POST['pw_r'] == feed.password:
           #그 글을 삭제해주세요
            feed.delete()
            return redirect('/')
       else :
           return redirect('/fail/')
    return render(request, 'remove_feed.html')
def detail_feed(request, pk):

    article = Article.objects.get(pk = pk)

    #하나의 글이 feed에 저장
    #article.objects가 데이터베이스 접근
    if request.method == 'POST':
        #코멘트 등록하기
        Comment.objects.create(
            article=article,
            author=request.POST['nickname'],
            text = request.POST['reply'],
            password = request.POST['pwd']
        )
    return render(request, 'detail_feed.html',{'feed' : article})

def fail(request):
    return render(request, 'fail.html')

