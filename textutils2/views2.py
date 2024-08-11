# I have created this file-jinal

from django.http import HttpResponse


def index(request):
    nav = '''<h1>home</h1>
    <li><a href="removepunc">remove punctuation</a></li>
    <li><a href="capitalizefirst">capitalize first</a></li>
    <li><a href="newlineremove">new line remover</a></li>
    <li><a href="spaceremove">space remover</a></li>
    <li><a href="charcount">character count</a></li>
    '''
    return HttpResponse(nav)


def about(request):
    return HttpResponse("about page")


def removepunc(request):
    return HttpResponse('''remove punc page <br><button><a href="/">home</a></button>''')


def capfirst(request):
    return HttpResponse('''capitalize first <br><button><a href="/">home</a></button>''')


def newlineremove(request):
    return HttpResponse('''new line remover <br><button><a href="/">home</a></button>''')


def spaceremove(request):
    return HttpResponse('''space remover <br><button><a href="/">home</a></button>''')


def charcount(request):
    return HttpResponse('''char count <br><button><a href="/">home</a></button>''')
