from django.db import models
from registration.models import NewVoteRegistrationData


class Party(models.Model):
    name = models.CharField(max_length=100, unique=True)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Vote(models.Model):
    voter = models.ForeignKey(NewVoteRegistrationData, on_delete=models.CASCADE)
    party_voted = models.ForeignKey(Party, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)
    captured_image = models.ImageField(upload_to="DataBase/vote_images/")

    class Meta:
        # Ensure uniqueness of EPIC number
        unique_together = ["voter", "party_voted"]

    def __str__(self):
        return f"{self.voter.epic_number} voted for {self.party_voted.name}"
