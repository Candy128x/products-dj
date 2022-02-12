heroku ps:scale web=1
git push heroku deploy_heroku
# heroku config:set DISABLE_COLLECTSTATIC=1
# python3 projproducts/manage.py runserver
web: gunicorn projproducts.wsgi --log-file -