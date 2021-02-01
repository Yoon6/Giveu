from django.shortcuts import render, get_object_or_404, redirect
from .models import Funding

# Create your views here.

'''
펀딩 글이 올라오는 게시판 list 함수
@param : request
@return : list 페이지, funding 목록 model
'''
def funding_list(request):
    funding_list = Funding.objects.all()
    return render(request, "funding_list.html", {"funding_list":funding_list})


'''
펀딩 글을 작성하는 create 함수
@param : request
@return :
    GET : create 페이지
    POST : 작성한 펀딩 글로 redirect
'''
def funding_create(request):
    if request.method == 'POST':
        funding = Funding()
        funding.title = request.POST['title']
        funding.description = request.POST['description']
        funding.photo = request.FILES['photo']
        funding.save()
        return redirect('funding_detail', funding.id)
    return render(request, "funding_create.html")


'''
특정 펀딩 페이지 detail 함수
@param : request, funding_id
@return : detail 페이지, 해당 펀딩의 model
'''
def funding_detail(request, funding_id):
    funding = get_object_or_404(Funding, pk=funding_id)
    return render(request, "funding_detail.html", {"funding":funding})


'''
펀딩 글이 수정하는 update 함수
@param : request
@return :
    GET : update 페이지
    POST : 작성한 펀딩 글로 redirect
'''
def funding_update(request, funding_id):
    funding = get_object_or_404(Funding, pk=funding_id)

    if request.method == 'POST':
        funding.title = request.POST['title']
        funding.description = request.POST['description']
        funding.photo = request.FILES['photo']
        funding.save()
        return redirect('funding_detail', funding.id)

    return render(request, "funding_update.html", {"funding":funding})


'''
특정 펀딩 글을 삭제하는 delete 함수
@param : request
@return : 펀딩 글 목록 list 페이지로 redirect
'''
def funding_delete(request, funding_id):
    funding = get_object_or_404(Funding, pk=funding_id)
    funding.delete()
    return redirect('funding_list')