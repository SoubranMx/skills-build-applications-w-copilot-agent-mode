from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

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
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert test data
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # Ensure unique index on email
        db.users.create_index([("email", 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
