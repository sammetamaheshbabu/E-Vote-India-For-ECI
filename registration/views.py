from django.contrib import messages
from django.db import IntegrityError, transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from .forms import NewVoteRegistrationForm
from .models import NewVoteRegistrationData
import logging

logger = logging.getLogger(__name__)


def registration(request):
    if request.method == "POST":
        form = NewVoteRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():  # Wrap with transaction for consistency
                    form.save()
                    messages.success(
                        request,
                        "Registration Successful! Your Application Reference Number is: "
                        + str(form.instance.application_reference_number),
                    )
                    return redirect("home")
            except IntegrityError as e:
                messages.error(request, f"Database error: {e}")
            except ValidationError as e:  # Catch specific validation errors
                messages.error(request, f"Validation error: {e}")
            except Exception as e:  # Catch other exceptions
                messages.error(request, f"An error occurred: {e}")
                logger.error(f"Registration error: {e}")  # Log the error
        else:
            messages.error(request, f"Form validation errors: {form.errors}")
    else:
        form = NewVoteRegistrationForm()

    context = {"form": form}  # Add context as needed
    return render(request, "registration.html", context)
