from django.shortcuts import render

# Create your views here.
def mutetranslator(request):
    context = {
        "lang_list" : ['A'], 
        "translation" : ['A', 'B', 'C', 'D']
    }
    return render(request, 'mutetranslate/mutetranslate.html', context)