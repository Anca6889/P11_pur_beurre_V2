""" DELETE ALL RATES AND COMMENTS DON'T USE IN PRODUCTION !!! DEV ONLY """

from django.core.management.base import BaseCommand
from app.models import Rating


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ONLY FOR DEVELOPMENT'"""

        rating_obj = Rating.objects.all()
        rating_obj.delete()
