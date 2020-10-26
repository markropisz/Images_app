# PhotoUpload

## Server preparation
```console
python manage.py migrate
```
```console
python manage.py runserver
```

## Opening the project
Open http://127.0.0.1:8000/ URL in your browser, where you can upload images

You can see all the uploaded models in JSON form on http://127.0.0.1:8000/list/ and view the photos in "TreePicturesApp/static/uploads" directory in the project root directory

You can view individual models on http://127.0.0.1:8000/<int:pk>/ URL
