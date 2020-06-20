from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   #return HttpResponse("Home")

   return render(request,'index.html')
def index2(request):
    return render(request,'index2.html')
def analyze(request):
    text1=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charactercounter=request.POST.get('charactercounter','off')
    if removepunc=="on":
    #analyzed=text1
      punctuations='''!()-[]{};:'"\,<>./?@#$%^&*~'''
      analyzed=""
      for char in text1:
        if char not in punctuations:
            analyzed=analyzed+char
      params={'purpose':'Removed Punctuations','analyzed_text': analyzed}
      text1=analyzed
      #return render(request,'analyze.html',params)
    if fullcaps=='on':
        analyzed=""
        for char in text1:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to uppercase','analyzed_text':analyzed}
        text1=analyzed
        #return render(request,'analyze.html',params)
    if newlineremover=='on':
        analyzed = ""
        for char in text1:
            if char!='\n' and char!='\r':
              analyzed = analyzed + char
        params = {'purpose': 'newlineremover', 'analyzed_text': analyzed}
        text1 = analyzed
        #return render(request, 'analyze.html', params)
    if extraspaceremover=='on':
        analyzed = ""
        for char in text1:
            if char!=' ':
                analyzed=analyzed+char
        params = {'purpose': 'extraspaceextraspaceremover', 'analyzed_text': analyzed}
        text1 = analyzed
        #return render(request,'analyze.html',params)
    if charactercounter=='on':
        cnt=0
        for char in text1:
            cnt+=1
        params={'purpose': 'charactercounter', 'analyzed_text':'no of characters are:'+str(cnt)}
        #return render(request,'analyze.html',params)
    if removepunc!='on'and newlineremover!='on' and extraspaceremover!='on' and charactercounter!='on' and fullcaps!='on':
        return HttpResponse("please select any operation and try again!")

    return render(request, 'analyze.html', params)