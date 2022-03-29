# Server/Postgresql Pen Test Framework





## Advantages
1. מוכן לשימוש מיידי כולל הגשת דף
2. מבנה פשוט ובסיסי. הגשת פונקציות בפייטון django
3. שליטה באבטחת השרת. מכולות מופרדות לכל רכיב.
4. בנייה ב2 פקודות אוטומטית. מותאם לכל מערכת הפעלה.
5. מסוגל לרוץ במצב מקומי או במצב הגשה חיצונית לאינטרנט.
6. רשיון פתוח על כלל הסיפריות MIT.
7. HTMX מוכן לגשר בדיקות GET POST ..
8. Tailwind css
9. Django , nginx , postgresql , Docker , selenium




## פקודות בנייה גלובלי  ##
docker-compose build
<br>
docker-compose up

# 3-7 דקות. חד פעמי





## פקודות MAKE  **יש לאכלס לפי שם המכולות מקובץ ה YML  **אופציה. לא חובה!

To use this project, run this commands:

1. `make up` to build the project and starting containers.
2. `make build` to build the project.
3. `make start` to start containers if project has been up already.
4. `make stop` to stop containers.
5. `make shell-web` to shell access web container.
6. `make shell-db` to shell access db container.
7. `make shell-nginx` to shell access nginx container.
8. `make logs-web` to log access web container.
9. `make logs-db` to log access db container.
10. `make logs-nginx` to log access nginx container.
11. `make collectstatic` to put static files in static directory.
12. `make log-web` to log access web container.
13. `make log-db` to log access db container.
14. `make log-nginx` to log access nginx container.
15. `make restart` to restart containers.

## License
[MIT](https://github.com/ruddra/docker-django/blob/master/LICENSE).

## Contribute
# מתבסס בחלקים על https://github.com/ruddra/docker-django/blob/master/compose/django/Dockerfile)

Feel free to fork and create PR.





##  IO אפליקציות Github  ##

