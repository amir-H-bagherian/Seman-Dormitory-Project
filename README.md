# Seman-Dormitory-Project
This project is developed to help **semnan university** allocate its dormitory beds to its students. Each year the students whose names are in the list can take a personality and lifestyle exam. This will let them share a room with other students who has the same personal type and life style.
This project is aimed to reduce tension between students based on this ideology that similar people with similar interests would get along well.
This project also considered the following features:
+ friends could request to share a room without taking any personal test
+ people with disabilities are able to request for ground floor rooms
+ people who has taken [MBTI test](https://www.16personalities.com/fa/) previously are able to enter their personal type directly without taking our personal-type test


## utilized technologies and frameworks
+ HTML5
+ CSS
+ JS
+ Bootstrap
+ Django

## How to use
##### Simply clone project and use `pip install -r requirements.txt` to install necessary packages for this project on your system. Then issue makemigrations and migrate commands and runserver

## Project Apps
This project consists of 2 apps, **studentInfo** and **mbti_test**

### studentInfo
> This app handles logging the user in if their credentials match the credentials stored in _Book1.xlsx_ file which contains students credentials who are allowed to request a bed in university dormitory. This app renders all of our webpages.
> It also process user lifestyle information and store the result in DB.

### mbti_test
> This app is designed to process the mbti test of our website. It receives user personal type data from the frontend, process them ans stores the user personal type in the DB.
 
 ## User model
 > Users in our project have the following attributes:
 + student_id
 + national_code (primaryKey)
 + cigarette_status
 + bed_time
 + tidyness_status
 + personal_type
 + email
 + shared_room_id
 + is_superuser
 + is_staff
 + is_active

## Developers
+ Mohammad Hossein Abdollahi Fard
+ Saman Moshiri
+ Aboulfazl Amouzgari
+ Amir Hossein Bagherian
+ Sepehr Vahedi

## More
consider to give us a star if you like
