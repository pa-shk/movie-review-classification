from django.shortcuts import render
import pickle

with open('rating_predictor', 'rb') as f:
    RATING_PREDICTOR = pickle.load(f)

with open('binary_classifier', 'rb') as f:
    BINARY_CLASSIFIER = pickle.load(f)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def user(request):
    review = request.GET['review']
    rating = RATING_PREDICTOR.predict([review])[0]
    sentiment_code = BINARY_CLASSIFIER.predict([review])[0]
    sentiment =  'postive' if sentiment_code == 0 else 'negative'
    return render(request, 'response.html', {'sentiment': sentiment, 'score': rating})