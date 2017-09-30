from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request):
    # test_str = '<html><head><title>To-Do lists</title></head></html>'
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html', {
        'new_item_text':request.POST.get('item_text', ''),
    })
