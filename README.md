# Django Pagination Assessment Test

## Follow to run the Project in your local machine

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

2. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

3. Apply the migrations:

    ```sh
    (venv)$ python manage.py makemigrations
    (venv)$ python manage.py migrate
    ```

4. Seed the database:

    ```sh
    (venv)$ python manage.py seed_db
    ```

5. Run the server:

    ```sh
    (venv)$ python manage.py runserver
    ```

    Navigate to [http://127.0.0.1:8000/employees/](http://127.0.0.1:8000/employees/)

    Navigate to [http://127.0.0.1:8000/employees/](http://127.0.0.1:8000/admin/) \
    username : Test\
    password : Test@1234\
    Now you can update CustomPaginate columns ie\
        around:\ 
        bondaries :\
    to see different outputs 


