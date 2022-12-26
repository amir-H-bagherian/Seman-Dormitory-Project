from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, national_code, student_id, email, **extra_fields):
        """
        Create and save a User with the given national_code, student_id and email.
        """
        if not student_id or not email or not national_code:
            raise ValueError('All input fields must be set!')
        
        email = self.normalize_email(email)
        user = self.model(national_code=national_code, student_id=student_id, email=email, **extra_fields)
        user.save()
        return user

    def create_superuser(self, national_code, student_id, email, **extra_fields):
        """
        Create and save a SuperUser with the given national_code, student_id and email.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(national_code, student_id, email, **extra_fields)