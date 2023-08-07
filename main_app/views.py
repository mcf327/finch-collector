from django.shortcuts import render


finches = [
  {'name': 'George', 'breed': 'Eurasian bullfinch', 'description': 'not very bright', 'age': 3},
  {'name': 'Dobbs', 'breed': 'American goldfinch', 'description': 'pretty but loud', 'age': 2},
]
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })