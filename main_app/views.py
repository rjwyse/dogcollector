from django.shortcuts import render

dogs = [
  {'name': 'Shoresy', 'breed': 'German Shepard/Lab', 'description': 'Energetic and Friendly', 'age': 3},
  {'name': 'Sully', 'breed': 'Australian Shepard Mix', 'description': 'Puppy Energy', 'age': 1},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')
def about(request):
  return render(request, 'about.html')
def dogs_index(request):
  return render(request, 'dogs/index.html', {
    'dogs': dogs
  })
