from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    # params = {"name": "jinal", "place": "jupiter"}
    return render(request, 'index.html')
    # return HttpResponse("index page")


def analyze(request):
    # GET THE TEXT

    global params
    djtext = request.POST.get('text', 'default')

    # not using get bcoz url has length limit..
    # Using post so that data can be sent in the message body
    # django by default provides csrf token for sending request from your website

    # CHECKBOX VALUE

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":

        punctuations = '''!()-{}[];:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed  # overriding djtext
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        # for char in djtext:
        #     analyzed = analyzed + char.upper()

        analyzed = djtext.upper()

        params = {'purpose': 'changed to upper case', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, "analyze.html", params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'remove new lines', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, "analyze.html", params)

    # if spaceremover == "on":
    #     analyzed = ""
    #     for char in djtext:
    #         if char != " ":
    #             analyzed = analyzed + char
    #
    #     params = {'purpose': 'remove spaces in text', 'analyzed_text': analyzed}
    #
    #     return render(request, "analyze.html", params)

    if extraspaceremover == "on":
        analyzed = ""
        for ind, char in enumerate(djtext):
            if not (djtext[ind] == " " and djtext[ind + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'remove spaces in text', 'analyzed_text': analyzed}

    # elif charcount == "on":
    #     analyzed = ""
    #     count = 0
    #     for char in djtext:
    #         count += 1
    #         analyzed = f"character in the text is {count}"
    #
    #     params = {'purpose': 'count character in text', 'analyzed_text': analyzed}
    #     return render(request, "analyze.html", params)
    if removepunc == "off" and fullcaps == "off" and newlineremover == "off" and extraspaceremover == "off":
        return HttpResponse("Please select any of the option..")

    return render(request, "analyze.html", params)


# hello jinal ratgod