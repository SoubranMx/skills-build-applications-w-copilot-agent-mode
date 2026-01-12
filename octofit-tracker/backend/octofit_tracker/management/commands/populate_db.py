from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Sample data for superheroes and teams
USERS = [
    {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
    {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
    {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
]
TEAMS = [
    {"name": "Marvel", "description": "Marvel superheroes team"},
    {"name": "DC", "description": "DC superheroes team"},
]
ACTIVITIES = [
    {"user_email": "superman@dc.com", "activity": "Flying", "duration": 60},
    {"user_email": "ironman@marvel.com", "activity": "Suit Up", "duration": 45},
]
LEADERBOARD = [
    {"team": "Marvel", "points": 150},
    {"team": "DC", "points": 120},
]
WORKOUTS = [
    {"name": "Strength Training", "suggested_for": "DC"},
    {"name": "Cardio Blast", "suggested_for": "Marvel"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Insert test data using Django ORM
        for user_data in USERS:
            User.objects.create(**user_data)
        
        for team_data in TEAMS:
            Team.objects.create(**team_data)
        
        for activity_data in ACTIVITIES:
            Activity.objects.create(**activity_data)
        
        for leaderboard_data in LEADERBOARD:
            Leaderboard.objects.create(**leaderboard_data)
        
        for workout_data in WORKOUTS:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
