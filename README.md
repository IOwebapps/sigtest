# Server/Postgresql Pen Test Framework


![NvqzHCiqHH](https://user-images.githubusercontent.com/102602422/161429515-bd868ad7-81df-4d2c-82be-20671d5d7f56.png)

Update 1.0.3:
1. ניקיון PIP
2. תיקון UI | Mobile
3. הוספת תפריט נגישות
4. הוספת תפריט ערכות נושא + הדגמת localstorage
5. ניקיון CSS 83kb קובץ בודד
6. הוספת פונקציות וטפסים.
7. איסוף 404 על כל השרת במצב מאובטח על פונקציית פייטון.
8. Threading. מכולה קניבלית(תוקפת את עצמה)
9. הוספת בקר שליטה עבור עדכון מצב שרת. מופעל/כבוי. HTMX , Localstorage
10. אנחנו עדיין בגישת דף בודד. המערכת מעדכנת רק את האלמנט הדרוש. html | css | htmx | django
11. LOADER גלובלי על כל בקשות HTMX

![firefox_o38ZKhF94C](https://user-images.githubusercontent.com/102602422/161429517-2fc9a5b1-e20d-4d14-91fb-81f655eff7d5.png)


** המערכת דורשת docker מותקן על המחשב המארח. 
** כל עוד הדף פתוח והעדכון האוטומטי מופעל המערכת ממשיכה לשלוח בקשות. יש לסגור את העדכון האוטומטי או לצאת מהאתר בסיום הפעולה המתבקשת.

** inspect network מציג לכם את הבקשות מהדף
** inspect app local storage מציג את הנתונים המקומיים כגון עדכון אוטומטי וערכת נושא
** docker-compose up מציג log של פייטון מהשרת


** פונקציות הבדיקה להדגמה בלבד. מכולה קניבלית מכוונת אוטומטית אל המכולת WEB של עצמה.

** הUI נבנה בעזרת https://tailwindcss.com/ & https://daisyui.com/ בקוד פתוח.

** האתר משתמש בHTMX בקוד פתוח https://htmx.org/

** רוב קוד הSVG נאסף מHEROICONS https://heroicons.com/ בקוד פתוח

** הרשאה פומבית לכל משתמש לבצע כל שינוי לפי צריכיו כולל הסרה או שינוי FOOTER או כל רכיב אחר במערכת. שאר הרכיבים יש לפעול לפי MIT

** המערכת יכולה לשמש בקלות לכל פעולה או הגשה בפועל. יש לשנות את פרטי ה.env


![chrome_EjeoK4yvSW](https://user-images.githubusercontent.com/102602422/160629357-194136d9-6973-41d2-89b7-1901d8a40ecc.png)
<br>
<br>



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
<br>
<br>

![chrome_v5yt6UdCDd](https://user-images.githubusercontent.com/102602422/160629371-54c06158-bbb0-433b-a4cf-b74be605d8b9.png)

<br>
<br>




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

