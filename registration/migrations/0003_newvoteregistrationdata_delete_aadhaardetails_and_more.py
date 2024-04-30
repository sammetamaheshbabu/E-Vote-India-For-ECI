# Generated by Django 5.0.3 on 2024-04-01 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_aadhaardetails_aadhaar_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewVoteRegistrationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relative_type', models.CharField(choices=[('father', 'Father'), ('mother', 'Mother'), ('husband', 'Husband'), ('wife', 'Wife'), ('legal_guardian', 'Legal Guardian')], max_length=20)),
                ('relative_name', models.CharField(max_length=100)),
                ('relative_surname', models.CharField(max_length=100)),
                ('mobile_ownership', models.CharField(choices=[('self', 'Self'), ('relative', 'Relative Mentioned Above')], max_length=20)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email_ownership', models.CharField(choices=[('self', 'Self'), ('relative', 'Relative Mentioned Above')], max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('aadhaar_availability', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('aadhaar_number', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')], max_length=20)),
                ('dob', models.DateField()),
                ('proof_of_age', models.CharField(choices=[('birth_certificate', 'Birth Certificate'), ('other_document', 'Any Other Document')], max_length=20)),
                ('dob_document', models.FileField(upload_to='dob_documents/')),
                ('house_no', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('village_town', models.CharField(max_length=100)),
                ('post_office', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=10)),
                ('mandal', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('proof_type', models.CharField(choices=[('document', 'Document for proof of residence'), ('other-document', 'Any other document for proof of residence')], max_length=20)),
                ('other_document_type', models.CharField(blank=True, max_length=100, null=True)),
                ('address_proof_document', models.FileField(upload_to='address_proof_documents/')),
                ('disabilityCategory', models.CharField(blank=True, max_length=20, null=True)),
                ('otherDisability', models.CharField(blank=True, max_length=100, null=True)),
                ('disabilityPercentage', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('disabilityDocuments', models.FileField(blank=True, null=True, upload_to='disability_documents/')),
                ('familyMemberName', models.CharField(max_length=100)),
                ('relationship', models.CharField(max_length=20)),
                ('epicNumber', models.CharField(blank=True, max_length=10, null=True)),
                ('place_of_birth', models.CharField(max_length=100)),
                ('state_of_birth', models.CharField(max_length=100)),
                ('district_of_birth', models.CharField(max_length=100)),
                ('resident_since', models.DateField()),
                ('application_date', models.DateField(auto_now_add=True)),
                ('captcha_text', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='AadhaarDetails',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='ApplicationReference',
        ),
        migrations.DeleteModel(
            name='Captcha',
        ),
        migrations.DeleteModel(
            name='ContactDetails',
        ),
        migrations.DeleteModel(
            name='DateOfBirth',
        ),
        migrations.DeleteModel(
            name='Declaration',
        ),
        migrations.DeleteModel(
            name='Disability',
        ),
        migrations.DeleteModel(
            name='ElectoralInfo',
        ),
        migrations.DeleteModel(
            name='EPICNumber',
        ),
        migrations.DeleteModel(
            name='FamilyMember',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='PersonalDetails',
        ),
        migrations.DeleteModel(
            name='Relative',
        ),
    ]
