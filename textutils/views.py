# I have made this file -> Hemant
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
     #get the text 
     djtext=request.POST.get('text','default')
     removepunc=request.POST.get('removepunc','off') 
     charcount=request.POST.get('charcount','off')
     uppercase=request.POST.get('uppercase','off')
     spaceremove=request.POST.get('spaceremove','off')
     newlineremove=request.POST.get('newlineremove','off')
     
     #Analyzing the text
     if removepunc=="on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed=""
            for char in djtext:
                if char not in punctuations:
                    analyzed=analyzed+char
     
            params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
            djtext=analyzed
           
     if charcount=="on":
         analyzed=int(len(djtext))
         params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
         djtext=analyzed
         return render(request,'analyze.html',params)
         
     if uppercase=="on":
         analyzed=djtext.upper()
         params={'purpose':'Changed To UPPER CASE','analyzed_text':analyzed}
         djtext=analyzed
         
     if spaceremove=="on":
         analyzed = ""
         for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
         params={'purpose':'spaceremove','analyzed_text':analyzed}
         djtext=analyzed
         
     if newlineremove=="on":
          analyzed = ""
          for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
          params={'purpose':'New line Removed','analyzed_text':analyzed}
          djtext=analyzed
          
     if(removepunc != "on" and newlineremove!="on" and spaceremove!="on" and uppercase!="on"):
         return HttpResponse("<h1>please select any operation and try again</h1>")
           
     return render(request,'analyze.html',params)
        
     
