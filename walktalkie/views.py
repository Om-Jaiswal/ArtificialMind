from django.shortcuts import render

# Create your views here.
def walktalkie(request):
    context = {
        "lang_list": ["A"]
    }
    return render(request, 'walktalkie/walktalkie.html', context)