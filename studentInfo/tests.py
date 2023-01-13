from django.test import TestCase
from .models import User


class ModelTest(TestCase):
    
    def create_user(self, national_code, student_id):
        return User.objects.create(national_code=national_code,
                                   student_id=student_id)
    
    def test_user_creation(self):
        valid_national_code = '1111111111'
        valid_student_id = '9811126101'
        new_user = self.create_user(valid_national_code, valid_student_id)
        self.assertTrue(isinstance(new_user, User))
        self.assertEqual(new_user.__str__(), valid_national_code)
        
    def test_invalidNationalCodeLength(self):
        invalid_national_code = '11111111111'
        valid_student_id = '9811126101'
        self.assertRaises(Exception, 
                          self.create_user, 
                          invalid_national_code,
                          valid_student_id)
    
    def test_invalidStudentIdLength(self):
        vaild_national_code = '1111111111'
        invalid_student_id = '9811126101'
        self.assertRaises(Exception,
                          self.create_user,
                          vaild_national_code,
                          invalid_student_id)        