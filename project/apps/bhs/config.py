
# Django
from django.apps import AppConfig


class BhsConfig(AppConfig):
    name = 'apps.bhs'
    verbose_name = 'BHS'

    def ready(self):
        import algoliasearch_django as algoliasearch
        import api.signals
        from .indexes import ChartIndex
        from .indexes import PersonIndex
        from .indexes import GroupIndex
        Chart = self.get_model('chart')
        Person = self.get_model('person')
        Group = self.get_model('group')
        # algoliasearch.register(Chart, ChartIndex)
        # algoliasearch.register(Person, PersonIndex)
        # algoliasearch.register(Group, GroupIndex)
        return