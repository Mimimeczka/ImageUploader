#imageuploader app
##installation 
1. pip install -r requirements.txt
2. python3 manage.py runserver
3. admin login: justyna 
4. admin password: 1234

##rest api
1. GET imageuploader/users/<int:user_id>/ - to get all links to all images of user
2. POST imageuploader/users/<int:user_id>/images/ - to add image to user
3. GET imageuploader/users/<int:user_id>/images/<int:image_id>/ - to get all links to one image
4. GET imageuploader/users/<int:user_id>/images/<int:image_id>/<str:type>/ - to get one image in a particular size (small, medium, original)
