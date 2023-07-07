from django.shortcuts import render
import pickle

# Create your views here.
def home(request):
    return render(request, 'home.html')

def user(request):
    review = request.GET['review']
    rating = predict_rating(review)
    sentiment = predict_sentiment(review)
    return render(request, 'response.html', {'sentiment': sentiment, 'score': rating})


def predict_rating(text):
    with open('rating_predictor', 'rb') as f:
        model = pickle.load(f)
    return model.predict([text])[0]


def predict_sentiment(text):
    with open('binary_classifier', 'rb') as f:
        model = pickle.load(f)
    return  'negative' if model.predict([text])[0] else 'positive'