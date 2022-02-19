heroku ps:scale web=1
git push heroku deploy_heroku
heroku config:add TZ="Asia/Kolkata"
# heroku config:set DISABLE_COLLECTSTATIC=1
web: python manage.py crontab add
web: python manage.py crontab show
# web: gunicorn projproducts.wsgi --log-file -
# python3 manage.py runserver
web: python3 manage.py runserver 0.0.0.0:$PORT
