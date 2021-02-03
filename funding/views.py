from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.decorators.http import require_POST

from .models import Funding

import json

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


'''
펀딩하기 버튼을 눌러 해당 펀딩 게시글의 funding_count를 1 증가시키는 함수
@param : request
@return : json
'''
@require_POST
def funding_counter(request):
    funding_id = request.POST['funding_id']

    funding = get_object_or_404(Funding, pk=funding_id)

    try:
        funding.funding_counter() # 해당 펀딩 글의 펀딩 카운트 1 증가
        message = 'Success'
    except:
        message = 'Fail'

    context = {
        "message": message,
        "funding_count": funding.funding_count,
    }

    return HttpResponse(json.dumps(context), content_type="application/json")