from django import forms
from .models import NewVoteRegistrationData


class NewVoteRegistrationForm(forms.ModelForm):
    class Meta:
        model = NewVoteRegistrationData
        fields = "__all__"  # Include all fields from the model

    def clean(self):  # sourcery skip: inline-immediately-returned-variable
        cleaned_data = super().clean()

        # Add any custom cleaning logic here if needed

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)  # Don't commit yet

        # Save section-wise data
        instance.application_date = self.cleaned_data.get("application_date")
        instance.captcha_text = self.cleaned_data.get("captcha_text")
        instance.state = self.cleaned_data.get("state")
        instance.district = self.cleaned_data.get("district")
        instance.assembly_constituency = self.cleaned_data.get("assembly_constituency")
        instance.first_name = self.cleaned_data.get("first_name")
        instance.middle_name = self.cleaned_data.get("middle_name")
        instance.surname = self.cleaned_data.get("surname")
        instance.photo = self.cleaned_data.get("photo")
        instance.relative_type = self.cleaned_data.get("relative_type")
        instance.relative_name = self.cleaned_data.get("relative_name")
        instance.relative_surname = self.cleaned_data.get("relative_surname")
        instance.mobile_ownership = self.cleaned_data.get("mobile_ownership")
        instance.mobile_number = self.cleaned_data.get("mobile_number")
        instance.email_ownership = self.cleaned_data.get("email_ownership")
        instance.email_id = self.cleaned_data.get("email_id")
        instance.aadhaar_availability = self.cleaned_data.get("aadhaar_availability")
        instance.aadhaar_number = self.cleaned_data.get("aadhaar_number")
        instance.gender = self.cleaned_data.get("gender")
        instance.dob = self.cleaned_data.get("dob")
        instance.proof_of_age = self.cleaned_data.get("proof_of_age")
        instance.other_document_type = self.cleaned_data.get("other_document_type")
        instance.dob_document = self.cleaned_data.get("dob_document")
        instance.house_no = self.cleaned_data.get("house_no")
        instance.street = self.cleaned_data.get("street")
        instance.village_town = self.cleaned_data.get("village_town")
        instance.post_office = self.cleaned_data.get("post_office")
        instance.pin_code = self.cleaned_data.get("pin_code")
        instance.mandal = self.cleaned_data.get("mandal")
        instance.district_address = self.cleaned_data.get("district_address")
        instance.state_address = self.cleaned_data.get("state_address")
        instance.proof_type = self.cleaned_data.get("proof_type")
        instance.other_document_type = self.cleaned_data.get("other_document_type")
        instance.address_proof_document = self.cleaned_data.get(
            "address_proof_document"
        )
        instance.disabilityCategory = self.cleaned_data.get("disabilityCategory")
        instance.otherDisability = self.cleaned_data.get("otherDisability")
        instance.disabilityPercentage = self.cleaned_data.get("disabilityPercentage")
        instance.disabilityDocuments = self.cleaned_data.get("disabilityDocuments")
        instance.familyMemberName = self.cleaned_data.get("familyMemberName")
        instance.relationship = self.cleaned_data.get("relationship")
        instance.epicNumber = self.cleaned_data.get("epicNumber")
        instance.place_of_birth = self.cleaned_data.get("place_of_birth")
        instance.state_of_birth = self.cleaned_data.get("state_of_birth")
        instance.district_of_birth = self.cleaned_data.get("district_of_birth")
        instance.resident_since = self.cleaned_data.get("resident_since")

        if commit:
            instance.save()
        return instance
