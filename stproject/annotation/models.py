from django.db import models
from django.core.exceptions import ValidationError

class Matches(models.Model):
    match_id = models.AutoField(primary_key=True)
    team_a_name = models.CharField(max_length=100)
    team_a_color = models.CharField(max_length=100, default='#000000')
    team_b_name = models.CharField(max_length=100)
    team_b_color = models.CharField(max_length=100, default='#000000')
    video_link = models.URLField(unique=True)
    team_a_players = models.JSONField(null=True, blank=True)
    team_b_players = models.JSONField(null=True, blank=True)
    game_type= models.CharField(max_length=100,null=True, blank=True)
    # team_a_first_five = models.JSONField(null=True, blank=True)
    # team_b_first_five = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.match_id)

    # def clean(self):
    #     # Validate that team_a_first_five is a subset of team_a_players
    #     if self.team_a_first_five and self.team_a_players:
    #         team_a_players_set = set(self.team_a_players)
    #         team_a_first_five_set = set(self.team_a_first_five)

    #         if not team_a_first_five_set.issubset(team_a_players_set):
    #             raise ValidationError('team_a_first_five must be a subset of team_a_players.')

    #     # Validate that team_b_first_five is a subset of team_b_players
    #     if self.team_b_first_five and self.team_b_players:
    #         team_b_players_set = set(self.team_b_players)
    #         team_b_first_five_set = set(self.team_b_first_five)

    #         if not team_b_first_five_set.issubset(team_b_players_set):
    #             raise ValidationError('team_b_first_five must be a subset of team_b_players.')

    # def save(self, *args, **kwargs):
    #     self.clean()  # Perform the validation before saving
    #     super().save(*args, **kwargs)




# from django.db import models
# # from django.contrib.postgres.fields import ArrayField

# class Matches(models.Model):
#     match_id = models.AutoField(primary_key=True)
#     team_a_name = models.CharField(max_length=100)
#     team_a_color = models.CharField(max_length=100,default='#000000')
#     team_b_name = models.CharField(max_length=100)
#     team_b_color = models.CharField(max_length=100,default='#000000')
#     video_link = models.URLField()
#     team_a_players = models.JSONField(null=True, blank=True)
#     team_b_players = models.JSONField(null=True, blank=True)

#     def __str__(self):
#         return str(self.match_id)

 