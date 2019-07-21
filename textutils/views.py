from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')

    # return HttpResponse("Home")




def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')


    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    purpose="You"

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
               analyzed = analyzed + char
        purpose=purpose+"removed punctuations  "

        params = {'purpose':purpose, 'analyzed_text': analyzed}
        djtext = analyzed


    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        purpose=purpose+'Changed to Uppercase   '

        params = {'purpose':purpose , 'analyzed_text': analyzed}
        djtext = analyzed


    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        purpose=purpose+"extraspaces  "

        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed


    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        purpose=purpose+"removed newline  "
        print("pre", analyzed)
        params = {'purpose': purpose, 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze2.html', params)
