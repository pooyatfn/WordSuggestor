import csv
import os
import re
from collections import defaultdict

from django.conf import settings
from django.db import models


def read_phrases_from_csv(file_name):
    csv_path = os.path.join(settings.BASE_DIR, 'ngram', 'datasets', file_name)

    with open(csv_path, encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            yield row[0]


class NGramManager(models.Manager):
    def __init__(self, n=2):
        super().__init__()
        self.n = n
        self.ngram_model = defaultdict(lambda: defaultdict(int))

    def normalize_text(self, text):
        text = re.sub(r'[0-9]', '', text)
        text = re.sub(r'[:,\"\'~.<>{}،;()«»]', '', text)
        text = re.sub(r'ي', 'ی', text)
        return text

    def generate_n_gram_model(self):
        datasets_dir = os.path.join(settings.BASE_DIR, 'ngram', 'datasets')

        for file_name in os.listdir(datasets_dir):
            dataset_name = os.path.splitext(file_name)[0]
            phrases = read_phrases_from_csv(file_name)
            for phrase in phrases:
                self.add_ngram(phrase, dataset_name)

    def save_ngram_model(self):
        for (dataset_name, context), word_freq in self.ngram_model.items():
            context_str = ' '.join(context)
            for word, frequency in word_freq.items():
                NGram.objects.create(dataset_name=dataset_name, context=context_str, word=word, frequency=frequency)

    def add_ngram(self, text, dataset_name):
        normalized_phrase = self.normalize_text(text)
        words = normalized_phrase.split()
        for i in range(len(words) - self.n + 1):
            context = tuple(words[i:i + self.n - 1])
            word = words[i + self.n - 1]
            self.ngram_model[(dataset_name, context)][word] += 1
        return True

    def load_n_gram_model(self):
        ngrams = NGram.objects.all()
        for ngram in ngrams:
            context = tuple(ngram.context.split())
            self.ngram_model[(ngram.dataset_name, context)][ngram.word] = ngram.frequency

    def suggest_word(self, text, dataset_name, k=5):
        self.load_n_gram_model()
        words = text.split()
        if len(words) < 1:
            return ""
        context = tuple(words[-(self.n - 1):])
        suggestions = self.ngram_model.get((dataset_name, context), {})
        if not suggestions:
            return ""
        top_n_values = [t[0] for t in sorted(suggestions.items(), key=lambda item: item[1], reverse=True)[:k]]
        return top_n_values


class NGram(models.Model):
    dataset_name = models.CharField(max_length=100)
    context = models.TextField()
    word = models.CharField(max_length=100)
    frequency = models.IntegerField()

    objects = NGramManager()

    def __str__(self):
        return f"{self.dataset_name}: {self.context} -> {self.word} ({self.frequency})"
