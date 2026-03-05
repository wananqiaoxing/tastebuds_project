from django.shortcuts import render

def main(request):
    # Currently passing empty context dictionaries {} until the backend team builds the models
    context = {
        'recipes': [],       # Placeholder for recipe data
        'restaurants': []    # Placeholder for restaurant data
    }
    return render(request, 'main/index.html', context)
