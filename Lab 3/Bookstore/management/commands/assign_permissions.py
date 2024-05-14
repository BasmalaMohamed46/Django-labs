
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Assign delete permission for Book model'

    def handle(self, *args, **options):
        delete_book_permission = Permission.objects.get(codename='delete_book')
        user = User.objects.get(username='basmalazain2@22')
        user.user_permissions.add(delete_book_permission)


        self.stdout.write(self.style.SUCCESS('Permissions assigned successfully'))
