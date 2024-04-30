from django.shortcuts import render
from polling.models import Party


def party_results(request):
    # Fetch the total votes for each party
    A_votes = Party.objects.get(name="A").vote_count
    B_votes = Party.objects.get(name="B").vote_count
    C_votes = Party.objects.get(name="C").vote_count
    D_votes = Party.objects.get(name="D").vote_count
    E_votes = Party.objects.get(name="E").vote_count
    F_votes = Party.objects.get(name="F").vote_count
    G_votes = Party.objects.get(name="G").vote_count
    nota_votes = Party.objects.get(name="nota").vote_count

    # Pass the total votes to the template
    return render(
        request,
        "results.html",
        {
            "A_votes": A_votes,
            "B_votes": B_votes,
            "C_votes": C_votes,
            "D_votes": D_votes,
            "E_votes": E_votes,
            "F_votes": F_votes,
            "G_votes": G_votes,
            "nota_votes": nota_votes,
        },
    )
