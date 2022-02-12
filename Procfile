heroku ps:scale web=1
git push heroku deploy_heroku
# heroku config:set DISABLE_COLLECTSTATIC=1
web: gunicorn projproducts.wsgi --log-file -
# python3 manage.py runserver