from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')
    
def result(request):
    text=request.POST['text']
    total_len=len(text)
    return render(request, 'result.html', {
        'total_len': total_len,}
        'type_text': text,
        'blank': blank,)
    