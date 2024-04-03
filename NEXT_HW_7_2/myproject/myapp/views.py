from django.shortcuts import render

# Create your views here.

def text(request):
    return render(request, 'text.html')

def count(request):
    
    
    text = request.POST['text']
    len1 = len(text)
    new = len( text.replace (" ",""))
    noblank = len(text.split(" "))
    
    
    return render(request, 'count.html',
    {'text': text, 'len1': len1, 'new' : new, 'noblank': noblank})