# Pizza_drf
Assignment - Pizza App made using Django that showcase the Pizza details using Django Rest Framework API Interface.
Database- MongoDB.
Endpoints-
1)http://127.0.0.1:8000/ for listing all Pizza
 Status - 200.
 
2)http://127.0.0.1:8000/Pizza/<str:id> for viewing a single Pizza 
 Status - 200.
 
3)http://127.0.0.1:8000/Create  for creating a new Pizza 
 Status -200 if created as per the rules.(The user should not be able to create a pizza of any other type which isn't present in the database.)
 else Status - 400 Bad request.
 
4)http://127.0.0.1:8000/Update/<str:id> for updating a particular Pizza 
 Status -200 if edited as per the rules.
 else Status - 400 Bad request.
 
5)http://127.0.0.1:8000/Delete/<str:id> for deleting a particular pizza
 Status - 200.


To run the project-python manage.py runserver (type this command in command prompt).

