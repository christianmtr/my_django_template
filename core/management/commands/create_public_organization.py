from django.core.management import BaseCommand

from core.api.serializers import OrganizationSerializer
from core.models import Organization, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        organization = Organization(name='{{ projec_name }} Public', domain_url='{{ project_name }}.com',
                                    schema_name='{{ project_name }}', ruc='20123123123')
        organization.save()
