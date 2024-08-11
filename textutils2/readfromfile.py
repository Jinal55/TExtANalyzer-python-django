from django.http import HttpResponse

with open(r"C:\Users\jinal\OneDrive\Desktop\pythondjangotut\textutils2\textutils2\1.txt", "r") as f:
    s1 = f.read()


def filereading(request):
    return HttpResponse(s1)
