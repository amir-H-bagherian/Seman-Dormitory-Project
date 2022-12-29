from django.shortcuts import render
from django.http import HttpResponse
from studentInfo.models import User
from django.contrib import messages
# Create your views here.

def mbti_test(request):
    values = []
    e = 0  # Extravert
    i = 0  # Introvert

    s = 0  # Sensing
    n = 0  # iNtuition

    t = 0  # Thinking
    f = 0  # Feeling

    j = 0  # Judging
    p = 0  # Percieving
    character = ''
    if request.method=='POST':
        for i in range(60):
            values.append(request.POST.get('question_{}'.format(i+1)))

    for i in range(len(values)):
        if values[i] == 'e':
            e = + 1
        elif character == 'i':
            i = + 1
        elif character == 's':
            s = + 1
        elif character == 'n':
            n = + 1
        elif character == 't':
            t = + 1
        elif character == 'f':
            f = + 1
        elif character == 'j':
            j = + 1
        elif character == 'p':
            p = + 1
    personality_type=''
    if e >= i:
        personality_type += 'e'
    else:
        personality_type += 'i'
    if s >= n:
        personality_type += 's'
    else:
        personality_type += 'n'
    if t >= f:
        personality_type += 't'
    else:
        personality_type += 'f'
    if j >= p:
        personality_type += 'j'
    else:
        personality_type += 'p'


    user=User.objects.order_by('-last_login').first()
    user.personal_type=personality_type
    user.save()
    messages.info(request,"تیپ شخصیتی شما {}".format(personality_type))

    return render(request, 'exam.html')
