import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("waiting for our database")
        db_con= None
        while not db_con:
            try:
                db_con= connections['default']
            except OperationalError:
                self.stdout.write("database Unavailable")
                time.sleep(1)

        self.stdout.write('database available')
