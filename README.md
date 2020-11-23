# Very Very Simple Blog
a very very very simple blog with python Django 2.2

## Usage
1.  clone project
2.  go to project root folder
3.  install requirements with <br/>
	``` pip install -r requirements.txt ```
4. do migrations <br/>
	``` python manage.py makemigrations ``` <br/>
	``` python manage.py migrate ```
5. run server <br/>
	``` python manage.py runserver ```

## Notes
- we use sqlite3 as default database in project but can change it very easy in project setting.
- for add new post or category you can use django admin panel. remember you most first add a category then add a new post.
