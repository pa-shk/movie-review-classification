from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def user(request):
    review = request.GET['review']
    print(review)
    rating = 10
    sentiment = 'positive'
    return render(request, 'response.html', {'sentiment': sentiment, 'score': rating})