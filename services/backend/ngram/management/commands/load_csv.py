from django.core.management.base import BaseCommand

from ngram.models import NGramManager


class Command(BaseCommand):
    help = 'Load CSV data and generate n-gram model'

    def handle(self, *args, **kwargs):
        ngram_manager = NGramManager()
        ngram_manager.generate_n_gram_model()
        ngram_manager.save_ngram_model()
        ngram_manager.load_n_gram_model()
        self.stdout.write(self.style.SUCCESS('N-gram model generated and loaded'))
