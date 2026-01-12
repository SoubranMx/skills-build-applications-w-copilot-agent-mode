from djongo import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'octofit_tracker_user'
    
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    
    class Meta:
        db_table = 'octofit_tracker_team'
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    user_email = models.EmailField()
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()
    
    class Meta:
        db_table = 'octofit_tracker_activity'
    
    def __str__(self):
        return f"{self.user_email} - {self.activity}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    
    class Meta:
        db_table = 'octofit_tracker_leaderboard'
    
    def __str__(self):
        return f"{self.team}: {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    suggested_for = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'octofit_tracker_workout'
    
    def __str__(self):
        return self.name
