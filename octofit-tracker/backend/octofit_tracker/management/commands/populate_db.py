from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

from octofit_tracker import models as octofit_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        octofit_models.User.objects.all().delete()
        octofit_models.Team.objects.all().delete()
        octofit_models.Activity.objects.all().delete()
        octofit_models.Leaderboard.objects.all().delete()
        octofit_models.Workout.objects.all().delete()

        # Create teams
        marvel = octofit_models.Team.objects.create(name='Marvel')
        dc = octofit_models.Team.objects.create(name='DC')

        # Create users
        users = [
            octofit_models.User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            octofit_models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            octofit_models.User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            octofit_models.User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        for user in users:
            octofit_models.Activity.objects.create(user=user, type='Running', duration=30)
            octofit_models.Activity.objects.create(user=user, type='Cycling', duration=45)

        # Create workouts
        for user in users:
            octofit_models.Workout.objects.create(user=user, description='Full body workout', duration=60)

        # Create leaderboard
        for team in [marvel, dc]:
            octofit_models.Leaderboard.objects.create(team=team, points=100)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
