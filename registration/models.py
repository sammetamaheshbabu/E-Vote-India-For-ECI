import datetime
from django.db import models
from django.utils.crypto import get_random_string


class NewVoteRegistrationData(models.Model):
    # Section A: Personal Information
    state = models.CharField(max_length=100, default="")
    district = models.CharField(max_length=100, default="")
    assembly_constituency = models.CharField(max_length=100, default="")

    # Section B: Personal Details
    first_name = models.CharField(max_length=100, default="")
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, default="")
    photo = models.ImageField(
        upload_to="DataBase/DP_photos/", max_length=255, default=""
    )

    # Section C: Relative Information
    relative_type = models.CharField(
        max_length=20,
        choices=[
            ("father", "Father"),
            ("mother", "Mother"),
            ("husband", "Husband"),
            ("wife", "Wife"),
            ("legal_guardian", "Legal Guardian"),
        ],
    )
    relative_name = models.CharField(max_length=100, default="")
    relative_surname = models.CharField(max_length=100, default="")

    # Section D: Contact Details
    mobile_ownership = models.CharField(
        max_length=20,
        choices=[
            ("self", "Self"),
            ("relative", "Relative Mentioned Above"),
        ],
    )
    mobile_number = models.CharField(max_length=15, default="", blank=True, null=True)
    email_ownership = models.CharField(
        max_length=20,
        choices=[
            ("self", "Self"),
            ("relative", "Relative Mentioned Above"),
        ],
    )
    email_id = models.EmailField(default="", blank=True, null=True)

    # Section E: Aadhaar Details
    aadhaar_availability = models.CharField(
        max_length=3,
        choices=[
            ("yes", "Yes"),
            ("no", "No"),
        ],
    )
    aadhaar_number = models.CharField(max_length=12, blank=True, null=True)

    # Section F: Gender
    gender = models.CharField(
        max_length=20,
        choices=[
            ("male", "Male"),
            ("female", "Female"),
            ("transgender", "Transgender"),
        ],
    )

    # Section G: Date of Birth Details
    dob = models.DateField()
    proof_of_age = models.CharField(
        max_length=20,
        choices=[
            ("birth_certificate", "Birth Certificate"),
            ("other_document", "Any Other Document"),
        ],
    )
    dob_document_type = models.CharField(max_length=50, blank=True, null=True)
    dob_document = models.FileField(upload_to="DataBase/dob_documents/")

    # Section H: Present Address Details
    house_no = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    village_town = models.CharField(max_length=100)
    post_office = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    mandal = models.CharField(max_length=100)
    district_address = models.CharField(max_length=100)
    state_address = models.CharField(max_length=100)
    proof_type = models.CharField(
        max_length=20,
        choices=[
            ("document", "Document for proof of residence"),
            ("other-document", "Any other document for proof of residence"),
        ],
    )
    address_document_type = models.CharField(max_length=100, blank=True, null=True)
    address_proof_document = models.FileField(
        upload_to="DataBase/address_proof_documents/"
    )

    # Section I: Disability Information (Optional)
    disabilityCategory = models.CharField(max_length=20, blank=True, null=True)
    otherDisability = models.CharField(max_length=100, blank=True, null=True)
    disabilityPercentage = models.PositiveSmallIntegerField(blank=True, null=True)
    disabilityDocuments = models.FileField(
        upload_to="DataBase/disability_documents/", blank=True, null=True
    )

    # Section J: Family Member Details
    familyMemberName = models.CharField(max_length=100)
    relationship = models.CharField(max_length=20)
    familyepicNumber = models.CharField(max_length=10, blank=True, null=True)

    # Section K: Declaration of Indian Citizenship
    place_of_birth = models.CharField(max_length=100)
    state_of_birth = models.CharField(max_length=100)
    district_of_birth = models.CharField(max_length=100)
    resident_since = models.CharField(max_length=50, blank=True, null=True)
    application_date = models.DateField(auto_now_add=True)

    # Section L: Captcha
    captcha_text = models.CharField(max_length=10)

    application_reference_number = models.CharField(
        max_length=20, unique=True, blank=True
    )
    epic_number = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.application_reference_number:
            self.application_reference_number = get_random_string(length=4)
        if not self.epic_number:
            district_code = self.district[:3].upper()
            mandal_post_office_code = str(self.mandal[:3]) + str(self.post_office[2:])
            person_number = str(NewVoteRegistrationData.objects.count() + 1).zfill(3)
            self.epic_number = district_code + mandal_post_office_code + person_number
        super().save(*args, **kwargs)

    def __str__(self):
        return self.relative_name
