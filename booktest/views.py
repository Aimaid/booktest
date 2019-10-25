# from django.template import RequestContext,loader
# from django.http import *
#
# def index(request):
#     temp=loader.get_template('booktest/index.html')
#     return HttpResponse(temp.render())


from django.shortcuts import render
from .models import *


def index(request):  # 进行简化操作
    booklist = BookInfo.objects.all()
    context = {"booklist": booklist}
    return render(request, "booktest/index.html", context)

def show(request,id):
    book=BookInfo.objects.get(pk=id)
    herolist=book.heroinfo_set.all()
    context={"list": herolist}
    return render(request,"booktest/show.html",context)