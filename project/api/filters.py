# Third-Party
from django_filters import CharFilter
from django_filters import NumberFilter
from django_filters import UUIDFilter
from django_filters.rest_framework import FilterSet
from django_filters.rest_framework import OrderingFilter

# Django
from django.contrib import admin

# Local
from .models import Award
from .models import Chart
from .models import Competitor
from .models import Contestant
from .models import Convention
from .models import Entry
from .models import Grantor
from .models import Group
from .models import Member
from .models import Office
from .models import Officer
from .models import Panelist
from .models import Person
from .models import Round
from .models import Score
from .models import Session
from .models import Venue


class BHSListFilter(admin.SimpleListFilter):
    title = 'BHS'
    parameter_name = 'is_bhs'

    def lookups(self, request, model_admin):
        return (
            ('BHS', 'Yes'),
            ('NotBHS', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'BHS':
            return queryset.filter(
                bhs_pk__isnull=False,
            )
        if self.value() == 'NotBHS':
            return queryset.filter(
                bhs_pk__isnull=True,
            )


class AccountListFilter(admin.SimpleListFilter):
    title = 'account'
    parameter_name = 'account'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Yes':
            return queryset.filter(
                account_id__isnull=False,
            )
        if self.value() == 'No':
            return queryset.filter(
                account_id__isnull=True,
            )


class OfficeListFilter(admin.SimpleListFilter):
    title = 'Office'
    parameter_name = 'office'

    def lookups(self, request, model_admin):
        # offices = Office.objects.order_by(
        #     'short_name',
        # ).values_list('short_name', 'short_name').distinct()
        # return tuple(offices)
        return (
            ('SCJC', 'SCJC'),
            ('DRCJ', 'DRCJ'),
            ('JUDGE', 'JUDGE'),
            ('JUDGE CA', '- Contest Administrator'),
            ('JUDGE MUS', '- Music'),
            ('JUDGE PER', '- Performance'),
            ('JUDGE SNG', '- Singing'),
            ('C', 'CHORUS'),
            ('Q', 'QUARTET'),
        )

    def queryset(self, request, queryset):
        office = request.GET.get('office')
        if office:
            return queryset.filter(
                office__short_name__startswith=office
            )
        return queryset


class DistrictListFilter(admin.SimpleListFilter):
    title = 'district'
    parameter_name = 'district'

    def lookups(self, request, model_admin):
        districts = Group.objects.filter(
            kind__in=[
                Group.KIND.district,
                Group.KIND.noncomp,
                Group.KIND.affiliate
            ]
        ).order_by(
            'tree_sort',
        ).values_list('id', 'code')
        return districts

    def queryset(self, request, queryset):
        district = request.GET.get('district')
        if district:
            return queryset.filter(district=district)
        return queryset


class DivisionListFilter(admin.SimpleListFilter):
    title = 'division'
    parameter_name = 'division'

    def lookups(self, request, model_admin):
        divisions = Group.objects.filter(
            kind=Group.KIND.division,
        ).order_by(
            'tree_sort',
        ).values_list('id', 'name')
        return divisions

    def queryset(self, request, queryset):
        division = request.GET.get('division')
        if division:
            return queryset.filter(division=division)
        return queryset


class GroupListFilter(admin.SimpleListFilter):
    title = ('group')
    parameter_name = 'group'

    def lookups(self, request, model_admin):
        orgs = Group.objects.filter(
            kind__lte=Group.KIND.division,
        ).values_list('id', 'code')
        return orgs

    def queryset(self, request, queryset):
        group = request.GET.get('group')
        if group:
            return queryset.filter(group=group)
        return queryset


class ParentGroupListFilter(admin.SimpleListFilter):
    title = ('parent')
    parameter_name = 'org'

    def lookups(self, request, model_admin):
        orgs = Group.objects.filter(
            kind__lte=Group.KIND.division,
        ).values_list('id', 'code')
        return orgs

    def queryset(self, request, queryset):
        org = request.GET.get('org')
        if org:
            return queryset.filter(parent=org)
        return queryset


class ConventionGroupListFilter(admin.SimpleListFilter):
    title = ('district')
    parameter_name = 'district'

    def lookups(self, request, model_admin):
        districts = Group.objects.filter(
            kind__lte=Group.KIND.district,
        ).order_by(
            'tree_sort',
        ).values_list('id', 'code')
        return districts

    def queryset(self, request, queryset):
        district = request.GET.get('district')
        if district:
            return queryset.filter(group=district)
        return queryset


class SessionGroupListFilter(admin.SimpleListFilter):
    title = ('district')
    parameter_name = 'district'

    def lookups(self, request, model_admin):
        districts = Group.objects.filter(
            kind=Group.KIND.district,
        ).order_by(
            'tree_sort',
        ).values_list('id', 'code')
        return districts

    def queryset(self, request, queryset):
        district = request.GET.get('district')
        if district:
            return queryset.filter(convention__group=district)
        return queryset


class AwardFilter(FilterSet):
    class Meta:
        model = Award
        fields = {
            'nomen': [
                'icontains',
            ],
            'kind': [
                'exact',
            ],
            'gender': [
                'exact',
            ],
            'season': [
                'exact',
            ],
            'status': [
                'exact',
            ],
            'group': [
                'exact',
            ],
            'group__parent': [
                'exact',
            ],
            'group__name': [
                'exact',
            ],
            'group__kind': [
                'exact',
            ],
            'group__officers__office__short_name': [
                'exact',
            ],
            'group__officers__person__user': [
                'exact',
            ],
            'group__officers__office__is_award_manager': [
                'exact',
            ],
            'group__officers__status': [
                'exact',
                'gt',
            ],
            'group__grantors__convention': [
                'exact',
            ],
        }


class ChartFilter(FilterSet):
    class Meta:
        model = Chart
        fields = {
            'nomen': [
                'icontains',
            ],
            'status': [
                'exact',
                'gte',
            ],
        }


class ContestantFilter(FilterSet):
    class Meta:
        model = Contestant
        fields = {
            'nomen': [
                'icontains',
            ],
        }


class ConventionFilter(FilterSet):
    class Meta:
        model = Convention
        fields = {
            'status': [
                'exact',
                'lt',
            ],
            'year': [
                'exact',
            ],
            'assignments__person__user': [
                'exact',
            ],
            'group__officers__person__user': [
                'exact',
            ],
            'assignments__kind': [
                'exact',
            ],
            'assignments__category': [
                'exact',
            ],
        }


class CompetitorFilter(FilterSet):
    class Meta:
        model = Competitor
        fields = {
            'nomen': [
                'icontains',
            ],
            'is_archived': [
                'exact',
            ],
        }


class EntryFilter(FilterSet):
    class Meta:
        model = Entry
        fields = {
            'nomen': [
                'icontains',
            ],
            'is_archived': [
                'exact',
            ],
        }


class GrantorFilter(FilterSet):
    class Meta:
        model = Grantor
        fields = {
            'status': [
                'exact',
            ],
            'group': [
                'exact',
            ],
            'convention': [
                'exact',
            ],
        }


class GroupFilter(FilterSet):
    class Meta:
        model = Group
        fields = {
            'id': [
                'exact',
            ],
            'kind': [
                'exact',
                'lt',
                'in',
                'lte',
            ],
            'gender': [
                'exact',
            ],
            'parent': [
                'exact',
            ],
            'members__person__user': [
                'exact',
            ],
            'nomen': [
                'icontains',
            ],
            'status': [
                'exact',
                'gt',
            ],
        }


class PanelistFilter(FilterSet):
    class Meta:
        model = Panelist
        fields = {
            'nomen': [
                'icontains',
            ],
        }


class MemberFilter(FilterSet):
    class Meta:
        model = Member
        fields = {
            'group': [
                'exact',
            ],
            'person__user': [
                'exact',
            ],
            'status': [
                'gte',
                'exact',
            ]
        }


class OfficeFilter(FilterSet):
    class Meta:
        model = Office
        fields = {
            'kind': [
                'exact',
            ],
        }


class OfficerFilter(FilterSet):
    ordering = OrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('office__name', 'officeName'),
        ),

        # labels do not need to retain order
        field_labels={
            'office__name': 'Office',
        }
    )

    class Meta:
        model = Officer
        fields = {
            'nomen': [
                'icontains',
            ],
            'office__short_name': [
                'exact',
            ],
            'office__kind': [
                'exact',
            ],
        }


class PersonFilter(FilterSet):
    class Meta:
        model = Person
        fields = {
            'nomen': [
                'icontains',
            ],
            'status': [
                'exact',
            ],
            'user': [
                'exact',
            ],
            'officers__office__kind': [
                'exact',
            ],
            'officers__office__is_judge_manager': [
                'exact',
            ],
        }


class RoundFilter(FilterSet):
    class Meta:
        model = Round
        fields = {
            'session__convention__status': [
                'exact',
            ],
            'session__convention__assignments__person__user': [
                'exact',
            ],
            'session__convention__year': [
                'exact',
            ],
            'status': [
                'exact',
                'lt',
            ],
        }


class ScoreFilter(FilterSet):
    class Meta:
        model = Score
        fields = {
            'song__appearance': [
                'exact',
            ],
        }


class SessionFilter(FilterSet):
    convention__assignments__person__user = UUIDFilter(
        field_name='convention__assignments__person__user',
        lookup_expr='exact',
        distinct=True,
    )

    convention__assignments__kind = NumberFilter(
        field_name='convention__assignments__kind',
        lookup_expr='exact',
        distinct=True,
    )

    convention__assignments__category = NumberFilter(
        field_name='convention__assignments__category',
        lookup_expr='exact',
        distinct=True,
    )

    status__lt = NumberFilter(
        field_name='status',
        lookup_expr='lt',
        distinct=True,
    )

    status = NumberFilter(
        field_name='status',
        lookup_expr='exact',
        distinct=True,
    )

    nomen__icontains = CharFilter(
        field_name='status',
        lookup_expr='icontains',
        distinct=True,
    )

    class Meta:
        model = Session
        fields = [
            'status',
            'status__lt',
            'is_archived',
            'kind',
            'gender',
            'convention',
            'is_invitational',
            'convention__status',
            'nomen__icontains',
            'convention__assignments__person__user',
            'convention__assignments__kind',
            'convention__assignments__category',
        ]


class VenueFilter(FilterSet):
    class Meta:
        model = Venue
        fields = {
            'nomen': [
                'icontains',
            ],
        }
