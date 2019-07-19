# Third-Party
from django_fsm_log.admin import StateLogInline
from fsm_admin.mixins import FSMTransitionMixin

# Django
from django.contrib import admin

# Local
from .filters import AwardQualifierLevelFilter
from .inlines import AssignmentInline
from .models import Assignment
from .models import Award
from .models import Convention

from apps.smanager.inlines import SessionInline
from .filters import DistrictListFilter

admin.site.site_header = 'Barberscore Admin Backend'


@admin.register(Assignment)
class AssignmentAdmin(FSMTransitionMixin, admin.ModelAdmin):
    fsm_field = [
        'status',
    ]
    save_on_top = True
    fields = [
        'status',
        'kind',
        'convention',
        'person_id',
        'user',
        'category',
    ]

    list_display = [
        'person_id',
        'convention',
        'kind',
        'category',
        'status',
    ]

    list_filter = (
        'status',
        'kind',
        'category',
    )

    list_select_related = [
        'convention',
    ]

    search_fields = [
        'id',
    ]

    autocomplete_fields = [
        'convention',
    ]

    readonly_fields = [
    ]
    inlines = [
        StateLogInline,
    ]
    raw_id_fields = [
        'user',
    ]


@admin.register(Award)
class AwardAdmin(FSMTransitionMixin, admin.ModelAdmin):
    fsm_field = [
        'status',
    ]
    save_on_top = True
    fields = [
        'id',
        'name',
        'status',
        'group_id',
        'kind',
        'gender',
        'district',
        'division',
        'age',
        'level',
        'season',
        'is_single',
        'is_novice',
        ('threshold', 'minimum', 'advance', 'spots',),
        'description',
        'notes',
    ]

    list_display = [
        'name',
        # 'size',
        # 'scope',
        'group_id',
        'division',
        'kind',
        'age',
        'gender',
        'level',
        # 'size',
        # 'scope',
        # 'season',
        # 'rounds',
        # 'threshold',
        # 'advance',
        # 'minimum',
        'status',
    ]

    # list_editable = [
    #     'threshold',
    #     'advance',
    #     'minimum',
    # ]
    list_filter = [
        'status',
        'kind',
        'level',
        # AwardQualifierLevelFilter,
        DistrictListFilter,
        'district',
        'division',
        'age',
        'gender',
        'season',
        'is_single',
        'is_novice',
    ]

    readonly_fields = [
        'id',
    ]

    search_fields = [
        'name',
    ]

    ordering = (
        'tree_sort',
    )


@admin.register(Convention)
class ConventionAdmin(FSMTransitionMixin, admin.ModelAdmin):
    fields = (
        'id',
        # 'legacy_selection',
        # 'legacy_complete',
        'status',
        'name',
        ('group_id', 'divisions', ),
        ('year', 'season', ),
        ('panel', 'kinds', ),
        ('open_date', 'close_date', ),
        ('start_date', 'end_date', ),
        'owners',
        'venue_name',
        'location',
        'timezone',
        'image',
        'description',
        'district',
    )

    list_display = (
        '__str__',
        'year',
        'season',
        'district',
        'name',
        # 'location',
        # 'timezone',
        # 'start_date',
        # 'end_date',
        # 'status',
    )

    list_editable = [
        'name',
        # 'location',
        # 'start_date',
        # 'end_date',
    ]

    list_filter = (
        'status',
        'season',
        'district',
        'year',
    )

    fsm_field = [
        'status',
    ]

    search_fields = [
        'name',
    ]

    inlines = [
        AssignmentInline,
        SessionInline,
    ]

    readonly_fields = (
        'id',
    )

    autocomplete_fields = [
        # 'group',
        'owners',
    ]

    ordering = (
        '-year',
        'season',
        # 'group__tree_sort',
    )
    list_select_related = [
        # 'group',
    ]

    save_on_top = True
