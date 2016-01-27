import logging
log = logging.getLogger(__name__)

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from easy_pdf.views import PDFTemplateView

from django.contrib.auth.decorators import login_required

from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
    get_user_model,
)

from django.contrib import messages

from django.db.models import (
    Prefetch,
)

from django.forms import (
    inlineformset_factory,
)


from apps.api.models import (
    Contest,
    Session,
    Round,
    Performance,
    Convention,
    Judge,
    Song,
    Score,
    Performer,
    Contestant,
)

from .forms import (
    make_performer_form,
    LoginForm,
    ContestForm,
    ScoreFormSet,
    # JudgeFormSet,
    SongForm,
)

User = get_user_model()


def home(request):
    if request.user.is_authenticated():
        return redirect('website:dashboard')
    else:
        return render(
            request,
            'home.html',
        )


def login(request):
    if request.method == 'POST':
        form = LoginForm(
            request.POST,
        )
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                if user.is_active:
                    auth_login(
                        request,
                        user,
                    )
                    messages.success(
                        request,
                        """You are logged in!"""
                    )
                    return redirect('website:home')
                else:
                    messages.error(
                        request,
                        """Your account has been closed.  Please contact Randy Meyer to reopen."""
                    )
                    return redirect('website:home')
            else:
                try:
                    user = User.objects.get(email=form.cleaned_data['email'])
                    messages.error(
                        request,
                        """That is not the correct password.  Please try again."""
                    )
                except User.DoesNotExist:
                    messages.error(
                        request,
                        """We don't recognize that email; perhaps you used a different one when you registered?"""
                    )
        else:
            for key in form.errors.keys():
                for error in form.errors[key]:
                    messages.error(
                        request,
                        error,
                    )
    else:
        form = LoginForm()
    return render(
        request,
        'registration/login.html',
        {'form': form},
    )


@login_required
def logout(request):
    auth_logout(request)
    messages.warning(
        request,
        """You are logged out""",
    )
    return redirect('website:home')


@login_required
def dashboard(request):
    conventions = Convention.objects.filter(
        year__gte=2015,
    )
    return render(
        request,
        'api/dashboard.html', {
            'conventions': conventions,
        },
    )


@login_required
def convention_detail(request, slug):
    convention = get_object_or_404(
        Convention,
        slug=slug,
    )
    sessions = convention.sessions.all()
    contests = Contest.objects.filter(
        session__convention=convention,
    )
    performers = Performer.objects.filter(
        session__convention=convention,
    )
    return render(
        request,
        'api/convention.html', {
            'convention': convention,
            'sessions': sessions,
            'contests': contests,
            'performers': performers,
        },
    )


@login_required
def round_oss(request, slug):
    round = get_object_or_404(
        Round,
        slug=slug,
        # status=Round.STATUS.final,
    )
    performances = round.performances.select_related(
        'performer__group',
    ).prefetch_related(
        'songs',
        'songs__tune',
    ).filter(
        status=Performance.STATUS.final,
    ).order_by(
        'place',
    )
    return render(
        request,
        'api/round_oss.html',
        {'round': round, 'performances': performances},
    )


@login_required
def contest_oss(request, slug):
    contest = get_object_or_404(
        Contest,
        slug=slug,
    )
    # TODO More hackery to be refactored
    judges = contest.session.judges.filter(
        kind=10,
    )
    contestants = Contestant.objects.filter(
        contest=contest,
    ).select_related(
    ).prefetch_related(
        'performer',
        'performer__performances',
        'performer__group',
        'performer__performances__songs',
    ).order_by('place')
    champion = contestants.first().performer.group
    return render(
        request,
        'api/contest_oss.html', {
            'contest': contest,
            'judges': judges,
            'contestants': contestants,
            'champion': champion,
        },
    )


class HelloPDFView(PDFTemplateView):
    template_name = "pdf/oss.html"
    model = Contest

    def get_context_data(self, **kwargs):
            context = super(HelloPDFView, self).get_context_data(**kwargs)
            contest = get_object_or_404(
                Contest,
                slug=self.kwargs['slug'],
                # status=Contest.STATUS.final,
            )
            performers = contest.performers.select_related(
                'group',
            ).prefetch_related(
                Prefetch(
                    'performances',
                    queryset=Performance.objects.order_by('round__kind'),
                ),
                Prefetch(
                    'performances__round',
                ),
                Prefetch(
                    'performances__songs',
                    queryset=Song.objects.order_by('order'),
                ),
                Prefetch('performances__songs__tune'),
            ).order_by(
                'place',
                # 'performances__round__kind',
            )
            judges = contest.judges.official
            contestants = contest.contestants.all()
            context["contest"] = contest
            context["performers"] = performers
            context["judges"] = judges
            context["contestants"] = contestants
            return context


@login_required
def performer_csa(request, slug):
    performer = get_object_or_404(
        Performer,
        slug=slug,
    )
    judges = performer.session.rounds.first().judges.exclude(
        category=Judge.CATEGORY.admin,
    )
    return render(
        request,
        'api/performer_csa.html',
        {'performer': performer, 'judges': judges},
    )


@login_required
def session_oss(request, slug):
    session = get_object_or_404(
        Session,
        slug=slug,
    )
    judges = session.judges.filter(
        kind=Judge.KIND.official,
    ).exclude(
        category=Judge.CATEGORY.admin,
    )
    # performances = Performance.objects.filter(
    #     round__session=session,
    # ).order_by('-total_points')
    # songs = Song.objects.filter(
    #     performance__round__session=session,
    # ).order_by('-performance__total_points', 'order',)
    performers = Performer.objects.filter(
        session=session,
    ).prefetch_related(
        'performances',
        'performances__songs',
    ).order_by('-total_points')
    contests = Contest.objects.filter(
        session=session,
    ).prefetch_related('contestants')
    return render(
        request,
        'api/session_oss.html', {
            'session': session,
            'judges': judges,
            # 'performances': performances,
            # 'songs': songs,
            'performers': performers,
            'contests': contests,
        },
    )


@login_required
def session_sa(request, slug):
    session = get_object_or_404(
        Session,
        slug=slug,
    )
    judges = session.rounds.first().judges.exclude(
        category=Judge.CATEGORY.admin,
    )
    performances = session.rounds.first().performances.order_by('-total_points')
    return render(
        request,
        'api/session_sa.html', {
            'session': session,
            'judges': judges,
            'performances': performances,
        },
    )


@login_required
def contest(request, slug):
    contest = get_object_or_404(
        Contest,
        slug=slug,
    )
    rounds = contest.rounds.all()
    return render(
        request,
        'manage/contest.html',
        {'contest': contest, 'rounds': rounds},
    )


@login_required
def contest_build(request, slug):
    contest = get_object_or_404(
        Contest,
        slug=slug,
    )
    if request.method == 'POST':
        form = ContestForm(
            request.POST,
            instance=contest,
        )
        if form.is_valid():
            form.save()
            return redirect('website:contest_imsession', contest.slug)
        else:
            for key in form.errors.keys():
                for error in form.errors[key]:
                    messages.error(
                        request,
                        error,
                    )
    else:
        form = ContestForm(
            instance=contest,
        )
    return render(
        request,
        'manage/contest_build.html',
        {'form': form},
    )


@login_required
def contest_imsession(request, slug):
    contest = get_object_or_404(
        Contest,
        slug=slug,
    )
    if request.method == 'POST':
        # formset = JudgeFormSet(
        #     request.POST,
        #     instance=contest,
        # )
        if formset.is_valid():
            formset.save()
            return redirect('website:contest_fill', contest.slug)
        else:
            for form in formset:
                for key in form.errors.keys():
                    for error in form.errors[key]:
                        messages.error(
                            request,
                            error,
                        )
    else:
        # formset = JudgeFormSet(
        #     instance=contest,
        # )
        pass
    return render(
        request,
        'manage/contest_imsession.html',
        {'formset': formset},
    )


@login_required
def contest_fill(request, slug):
    contest = get_object_or_404(
        Contest,
        slug=slug,
    )
    PerformerForm = make_performer_form(contest)
    PerformerFormSet = inlineformset_factory(
        Contest,
        Performer,
        form=PerformerForm,
        extra=50,
        can_delete=False,
    )
    if request.method == 'POST':
        formset = PerformerFormSet(
            request.POST,
            instance=contest,
        )
        if formset.is_valid():
            formset.save()
            messages.success(
                request,
                """Performer(s) added.""",
            )
            return redirect('website:contest_fill', contest.slug)
        else:
            for form in formset:
                for key in form.errors.keys():
                    for error in form.errors[key]:
                        messages.error(
                            request,
                            error,
                        )
    else:
        formset = PerformerFormSet(
            instance=contest,
        )
    return render(
        request,
        'manage/contest_fill.html',
        {'formset': formset},
    )


@login_required
def contest_start(request, slug):
    contest = get_object_or_404(
        Contest,
        slug=slug,
    )
    # round = contest.rounds.get(
    #     kind=contest.rounds,
    # )
    # performances = round.performances.order_by('position')
    # if request.method == 'POST':
    #     form = ContestForm(request.POST, instance=contest)
    #     form.start(contest)
    #     messages.success(
    #         request,
    #         """The contest has been started!""".format(contest),
    #     )
    #     return redirect('website:round_score', round.slug)
    # else:
    #     form = ContestForm(instance=contest)
    return render(
        request,
        'manage/contest_start.html', {
            'contest': contest,
        },
    )


@login_required
def round_draw(request, slug):
    round = get_object_or_404(
        Round,
        slug=slug,
    )
    # performers = contest.performers.order_by('name')
    # if request.method == 'POST':
    #     form = ContestForm(request.POST, instance=contest)
    #     form.draw(contest)
    #     messages.warning(
    #         request,
    #         """{0} has been drawn!""".format(contest),
    #     )
    #     return redirect('website:contest_start', contest.slug)
    # else:
    #     form = ContestForm(instance=contest)
    return render(
        request,
        'manage/round_draw.html',
        {'round': round},
    )


@login_required
def round_start(request, slug):
    round = get_object_or_404(
        Round,
        slug=slug,
    )
    # performances = round.performances.order_by('position')
    # if request.method == 'POST':
    #     form = ContestForm(request.POST, instance=contest)
    #     form.start(contest)
    #     messages.success(
    #         request,
    #         """The contest has been started!""".format(contest),
    #     )
    #     return redirect('website:round_score', round.slug)
    # else:
    #     form = ContestForm(instance=contest)
    return render(
        request,
        'manage/round_start.html', {
            'round': round,
        },
    )


@login_required
def performance_score(request, slug):
    round = get_object_or_404(
        Round,
        slug=slug,
    )
    performance = round.performances.get(
        status=Performance.STATUS.started,
    )
    performer = performance.performer
    song1 = performance.songs.get(order=1)
    song2 = performance.songs.get(order=2)
    if request.method == 'POST':
        songform1 = SongForm(
            request.POST,
            instance=song1,
            prefix='sf1',
        )
        songform2 = SongForm(
            request.POST,
            instance=song2,
            prefix='sf2',
        )
        formset1 = ScoreFormSet(
            request.POST,
            instance=song1,
            prefix='song1',
        )
        formset2 = ScoreFormSet(
            request.POST,
            instance=song2,
            prefix='song2',
        )
        if all([
            songform1.is_valid(),
            songform2.is_valid(),
            formset1.is_valid(),
            formset2.is_valid(),
        ]):
            songform1.save(),
            songform2.save(),
            formset1.save(),
            formset2.save(),
            # TODO plus change state, run valiations and denormalize.
            performance.end_performance()
            try:
                next_performance = Performance.objects.get(
                    round=round,
                    position=performance.position + 1,
                )
            except Performance.DoesNotExist:
                round.end_round()
                return redirect('website:home')
            next_performance.status = Performance.STATUS.started
            next_performance.save()
            return redirect('website:contest_score', contest.slug)
        else:
            for key in songform1.errors.keys():
                for error in songform1.errors[key]:
                    messages.error(
                        request,
                        error,
                    )
            for key in songform2.errors.keys():
                for error in songform2.errors[key]:
                    messages.error(
                        request,
                        error,
                    )
            for form in formset1:
                for key in form.errors.keys():
                    for error in form.errors[key]:
                        messages.error(
                            request,
                            error,
                        )
            for form in formset2:
                for key in form.errors.keys():
                    for error in form.errors[key]:
                        messages.error(
                            request,
                            error,
                        )
            formsets = [
                formset1,
                formset2,
            ]
    else:
        songform1 = SongForm(
            instance=song1,
            prefix='sf1',
        )
        songform2 = SongForm(
            instance=song2,
            prefix='sf2',
        )
        formset1 = ScoreFormSet(
            instance=song1,
            prefix='song1',
        )
        formset2 = ScoreFormSet(
            instance=song2,
            prefix='song2',
        )
        formsets = [
            formset1,
            formset2,
        ]

    return render(
        request,
        'manage/score.html', {
            'songform1': songform1,
            'songform2': songform2,
            'formsets': formsets,
            'contest': contest,
            'round': round,
            'performance': performance,
            'performer': performer,
        },
    )


@login_required
def round_end(request, slug):
    round = Round.objects.get(slug=slug)
    return render(
        request,
        'manage/round_end.html',
        {'round': round},
    )


@login_required
def contest_end(request, slug):
    contest = Contest.objects.get(slug=slug)
    return render(
        request,
        'manage/conetst_end.html',
        {'contest': contest},
    )


