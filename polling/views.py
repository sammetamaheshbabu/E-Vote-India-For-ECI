from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Party, NewVoteRegistrationData, Vote
from .forms import PollingForm


def polling_page(request):
    if request.method == "POST":
        epic_number = request.POST.get("epic_number")
        aadhaar_number = request.POST.get("aadhaar_number")
        mobile_number = request.POST.get("mobile_number")
        email_id = request.POST.get("email_id")
        party_name = request.POST.get("party_name")

        if epic_number and aadhaar_number and mobile_number and email_id and party_name:
            try:
                registered_voter = NewVoteRegistrationData.objects.get(
                    epic_number=epic_number,
                    aadhaar_number=aadhaar_number,
                    mobile_number=mobile_number,
                    email_id=email_id,
                )

                captured_image_data = request.POST.get("captured_image")

                if captured_image_data:
                    try:
                        party_voted = Party.objects.get(name=party_name)
                        vote = Vote.objects.create(
                            voter=registered_voter,
                            party_voted=party_voted,
                            captured_image=captured_image_data,
                        )
                        party_voted.vote_count += 1
                        party_voted.save()
                        return redirect("results")
                    except Party.DoesNotExist:
                        error_message = "Invalid party selected: " + party_name
                else:
                    error_message = "Please capture your image."
            except NewVoteRegistrationData.DoesNotExist:
                error_message = "Invalid credentials. Please enter valid details."
            except IntegrityError:
                error_message = "You have already voted successfully."
        else:
            error_message = "Please fill in all required fields."

        return render(request, "polling.html", {"error_message": error_message})

    else:
        return render(request, "polling.html")
