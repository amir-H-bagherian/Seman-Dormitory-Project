from django.shortcuts import render, redirect
from .models import User
import openpyxl
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


def read_from_excel():
    
    users = {}
    dataframe = openpyxl.load_workbook("Book1.xlsx")
    sheet = dataframe.active
    
    for i in range(2, sheet.max_row + 1):
        lst = []
        for j in range(1, sheet.max_column + 1):
            cell_obj = sheet.cell(row=i, column=j)
            lst.append(cell_obj.value)
        users.update({lst[0]: lst[1]})
        
    return users


def login_user(request):
    
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        national_code = request.POST.get('national_code')
        email = request.POST.get('email')
        #users = read_from_excel()
        
        # If student has registered before and wants to regsiter again for whatever reason
        # Delete the student's record and rebuild a record for the student.
        # We do this since we do not have and do not want to have acounts for our users.
        try:
            user = User.objects.get(national_code=national_code)
            user.delete()
        except:
            pass
        
        if True: #national_id in users.keys() and users[national_id] == student_id:
            
            new_user = User(national_code=national_code, student_id=student_id, email=email)
            new_user.save()
            login(request, new_user)

            return redirect('homepage') # go to the next page
        else:
            messages.error(request, "Invalid Input!")
            # return redirect('front/') # go to student does not exist in file page
    
    return render(request, 'index.html')


@login_required(login_url='index')
def home_page(request):
    return render(request, 'HomePage.html')


def farzanegan_page(request):
    return render(request, 'farzanegan.html')

def farhikhtegan_page(request):
    return render(request, 'farhikhtegan.html')

def kosar_page(request):
    return render(request, 'kosar.html')

@login_required(login_url='index')
def pre_exam_page(request):
    return render(request, 'pre-exam.html')