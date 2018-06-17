# Standard Libary
import logging
import uuid

# Third-Party
from django_fsm import FSMIntegerField
from django_fsm import transition
from django_fsm_log.decorators import fsm_log_by
from dry_rest_permissions.generics import allow_staff_or_superuser
from dry_rest_permissions.generics import authenticated_users
from model_utils import Choices
from model_utils.models import TimeStampedModel

# Django
from django.apps import apps as api_apps
from django.db import models

config = api_apps.get_app_config('api')

log = logging.getLogger(__name__)


class Contest(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    STATUS = Choices(
        (-10, 'excluded', 'Excluded',),
        (0, 'new', 'New',),
        (10, 'included', 'Included',),
    )

    status = FSMIntegerField(
        help_text="""DO NOT CHANGE MANUALLY unless correcting a mistake.  Use the buttons to change state.""",
        choices=STATUS,
        default=STATUS.new,
    )

    # Private
    champion = models.ForeignKey(
        'Group',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    # FKs
    session = models.ForeignKey(
        'Session',
        related_name='contests',
        on_delete=models.CASCADE,
    )

    award = models.ForeignKey(
        'Award',
        related_name='contests',
        on_delete=models.CASCADE,
    )

    # Internals
    class Meta:
        unique_together = (
            ('session', 'award',)
        )

    class JSONAPIMeta:
        resource_name = "contest"

    def __str__(self):
        return "{0}".format(
            self.award.name,
        )

    # Contest Permissions
    @staticmethod
    @allow_staff_or_superuser
    def has_read_permission(request):
        return True

    @allow_staff_or_superuser
    def has_object_read_permission(self, request):
        return True

    @staticmethod
    @allow_staff_or_superuser
    @authenticated_users
    def has_write_permission(request):
        return True
        # return any([
        #     request.user.person.officers.filter(office__is_convention_manager=True),
        #     request.user.person.officers.filter(office__is_session_manager=True),
        # ])

    @allow_staff_or_superuser
    @authenticated_users
    def has_object_write_permission(self, request):
        return True
        # return all([
        #     self.session.convention.assignments.filter(
        #         person__user=request.user,
        #         category__lte=10,
        #         kind=10,
        #         status=10,
        #     ),
        #     self.session.status == self.session.STATUS.new,
        # ])

    # Methods
    def calculate(self, *args, **kwargs):
        if self.award.level == self.award.LEVEL.qualifier:
            champion = None
        contestants = self.contestants.filter(
            status__gt=0,
        ).order_by(
            '-entry__competitor__tot_points',
            '-entry__competitor__sng_points',
            '-entry__competitor__mus_points',
            '-entry__competitor__per_points',
        )
        if contestants:
            champion = contestants.first().entry.group
        else:
            champion = None
        self.champion = champion
        return

    # Transitions
    @fsm_log_by
    @transition(field=status, source=[STATUS.new, STATUS.excluded], target=STATUS.included)
    def include(self, *args, **kwargs):
        return

    @fsm_log_by
    @transition(field=status, source=[STATUS.new, STATUS.included], target=STATUS.excluded)
    def exclude(self, *args, **kwargs):
        return
