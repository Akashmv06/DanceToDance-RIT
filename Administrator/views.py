from django.shortcuts import redirect, render
from MasterEntry.models import NewsType
from .models import News
from django.http import HttpResponse


def NewstypeSelect():
    NewsTypeRecords=NewsType.objects.all()
    return NewsTypeRecords

def CreateNews(request):
    #return render(request,"Administrator/NewsManagement.html")
    NewsTypeRecords=NewstypeSelect()
    if request.method == 'POST':
        p=News()
        p.news_title= request.POST.get("ntitle")
        p.news_content= request.POST.get("ncontent")
        NewsTypeObj=NewsType.objects.get(id=request.POST.get("ntype"))
        p.news_newstype=NewsTypeObj
        p.news_poster=request.FILES.get("nposter")
        p.save()
        return render(request,"Administrator/NewsManagement.html")
    else:
        return render(request,"Administrator/NewsManagement.html",{'NewsTypeRecords':NewsTypeRecords})

