# Third-Party
from django_filters import rest_framework as filters

# Local
from .models import (
    Catalog,
    Contestant,
    Convention,
    Group,
    Judge,
    Performer,
    Person,
    Session,
    Submission,
    Venue,
)


class CatalogFilter(filters.FilterSet):
    class Meta:
        model = Catalog
        fields = {
            'title': [
                'icontains',
            ],
        }


class ConventionFilter(filters.FilterSet):
    class Meta:
        model = Convention
        fields = {
            'status': [
                'exact',
            ],
            'year': [
                'exact',
            ],
        }


class GroupFilter(filters.FilterSet):
    class Meta:
        model = Group
        fields = {
            'nomen': [
                'icontains',
            ],
            'kind': [
                'exact',
            ],
            'status': [
                'exact',
            ],
        }


class JudgeFilter(filters.FilterSet):
    class Meta:
        model = Judge
        fields = {
            'nomen': [
                'icontains',
            ],
            'category': [
                'exact',
            ],
        }


class ContestantFilter(filters.FilterSet):
    class Meta:
        model = Contestant
        fields = {
            'nomen': [
                'icontains',
            ],
        }


class PerformerFilter(filters.FilterSet):
    class Meta:
        model = Performer
        fields = {
            'nomen': [
                'icontains',
            ],
            'group': [
                'exact',
            ],
        }


class PersonFilter(filters.FilterSet):
    class Meta:
        model = Person
        fields = {
            'nomen': [
                'icontains',
            ],
            'status': [
                'exact',
            ],
        }


class SessionFilter(filters.FilterSet):
    class Meta:
        model = Session
        fields = {
            'status': [
                'exact',
            ],
            'convention': [
                'exact',
            ],
        }


class SubmissionFilter(filters.FilterSet):
    class Meta:
        model = Submission
        fields = {
            'status': [
                'exact',
            ],
        }


class VenueFilter(filters.FilterSet):
    class Meta:
        model = Venue
        fields = {
            'nomen': [
                'icontains',
            ],
        }
