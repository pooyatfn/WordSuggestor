from django.urls import path

from . import views

app_name = 'ngram'
urlpatterns = [
    path('suggest/', views.suggest_word_api, name='suggest-word'),
    path('add/', views.add_ngram_api, name='add-ngram'),
]
