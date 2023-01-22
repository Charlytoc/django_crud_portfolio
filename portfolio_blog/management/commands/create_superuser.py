from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create Charly superuser'

    def handle(self, *args, **options):
        print('TODO OK')
        user = User.objects.create_user('Charlytoc', 'charlyjchaconc@gmail.com', 'Charly.8386147')
        user.is_superuser = True
        user.is_staff = True
        user.save()
        self.stdout.write(self.style.SUCCESS('Successfully created superuser'))



