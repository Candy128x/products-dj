# Commands


---
## Setup Virtual Environment
- Create virtual environment 
- => virtualenv -p python3.8 venv
- Activate virtual environment 
- => source venv/bin/activate



## pip3 install *packages
- Install Django
- => pip3 install django
- => [OR] python -m pip install Django
- Know which package is installed
- => python -m django --version
- Install DRF
- => pip3 install djangorestframework
- [optional] Markdown support for the browsable API.
- => pip install markdown
- [optional] Filtering support
- => pip install django-filter


## To Start, Work on Project 
- Create Project
- => django-admin startproject projdemo
- Create App
- => cd projdemo/
- Note: App name must be in plural
- => django-admin startapp employees

## install packages
- => cd projdemo
- => pip3 freeze > requirements.txt
- To install package dependency
- => pip3 install -r requirements.txt

- => pip install Django==3.2.11
- => pip install djangorestframework
- => x pip install django-elasticsearch-dsl
- => x pip install django-elasticsearch-dsl-drf
- => pip install elasticsearch==7.14.0
- => pip install elasticsearch-dsl==7.4.0
- => pip install django-elasticsearch-dsl==7.2.0
- => x pip3 install psycopg2
- => x pip3 install psycopg2-binary
- => x pip3 install python-decouple
- => pip install django-crontab --> [link](https://pypi.org/project/django-crontab/)
- => pip install django-import-export --> [link](https://www.programink.com/django-tutorial/django-import-export.html)


---
### Note: Some Useful Command's

> - check django version
> - $ django-admin --version

> - make project
> - $ django-admin startproject projdemo

> - make app
> - $ python3 manage.py startapp home

> - make migrations
> - $ python3 manage.py makemigrations
> - migrate
> - $ python3 manage.py migrate

> - create super user
> - $ python3 manage.py createsuperuser

> - To dump data:
> - $ python3 manage.py dumpdata --indent 4 > ../readme_docs/dumpdata/db_dump.json

> - To load data:
> - $ python manage.py loaddata ../readme_docs/dumpdata/db_dump.json

> - To open Interactive Console / Terminal
> - $ python3 manage.py shell

> - set URL globally
> - $ ngrok http 8000

> - collect static
> - $ python3 manage.py collectstatic

> - API status-codes
> - https://www.django-rest-framework.org/api-guide/status-codes/

> - add cron job
> - $ python manage.py crontab add
> - show cron job
> - $ python manage.py crontab show
> - run cron job
> - $ python3 manage.py crontab run c63ba439b21e9b2b401cc79b69da5f26
> - remove cron job
> - $ python manage.py crontab remove



---
## Elastic Search Command's
> - $ service elasticsearch status
> - $ start elastic-search service on system
> - $ sudo systemctl start elasticsearch
> - $ sudo systemctl restart elasticsearch
> - $ sudo systemctl stop elasticsearch

- command to know elastic-search is up & run
```shell
ashishs@lp7981:.../product-crud-es$ service elasticsearch status
● elasticsearch.service - Elasticsearch
   Loaded: loaded (/usr/lib/systemd/system/elasticsearch.service; disabled; vendor preset: enabled)
   Active: active (running) since Sun 2022-01-23 13:00:35 IST; 11s ago
     Docs: https://www.elastic.co
 Main PID: 27096 (java)
    Tasks: 113 (limit: 4915)
   CGroup: /system.slice/elasticsearch.service
           ├─27096 /usr/share/elasticsearch/jdk/bin/java -Xshare:auto -Des.networkaddress.cache.ttl=60 -Des.networkaddress.cache.negative.ttl=1
           └─27385 /usr/share/elasticsearch/modules/x-pack-ml/platform/linux-x86_64/bin/controller
ashishs@lp7981:.../product-crud-es$ 
ashishs@lp7981:.../product-crud-es$ 
ashishs@lp7981:.../product-crud-es$ curl -XGET http://localhost:9200
{
  "name" : "lp7981",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "EoWui3QQTqiHPWIVC55sAw",
  "version" : {
    "number" : "7.14.1",
    "build_flavor" : "default",
    "build_type" : "deb",
    "build_hash" : "66b55ebfa59c92c15db3f69a335d500018b3331e",
    "build_date" : "2021-08-26T09:01:05.390870785Z",
    "build_snapshot" : false,
    "lucene_version" : "8.9.0",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
ashishs@lp7981:.../product-crud-es$ 
```

> - ElasticSearch on local system
> - http://localhost:9200/

> - Kibana on local system
> - http://localhost:5601/

- hit ES records
```shell
(venv) ashishs@lp7981:.../projproduct$ python manage.py shell
>>> 
>>> from products.es_documents import ProductDetailsDocument
>>>
>>> records = ProductDetailsDocument.search().filter("term", name="apple")
>>> 
>>> for record in records:
...     print(f'---Products Details ---name: {record.name} ---price:{record.price} ---quantity: {record.quantity}')
... 
---Products Details ---name: apple ipad - model J1 ---price:50000 ---quantity: 5
---Products Details ---name: apple ipad - model G1 ---price:2000 ---quantity: 5
---Products Details ---name: apple ipad - model E1 ---price:50000 ---quantity: 5
---Products Details ---name: apple ipad - model D1 ---price:40000 ---quantity: 5
---Products Details ---name: apple ipad - model C1 ---price:3000 ---quantity: 20
---Products Details ---name: apple ipad - model B2 ---price:2000 ---quantity: 5
---Products Details ---name: apple ipad - model A1 ---price:40000 ---quantity: 2
>>> 
>>> 
```

> Syncing Django’s database with Elasticsearch indexes:
> > - Create Elasticsearch indexes:
> > - $ python3 manage.py search_index --create -f
> 
> > - Sync the data:
> > - $ python3 manage.py search_index --populate -f
> 
> > - Populate Elasticsearch:
> > - $ python3 manage.py search_index --rebuild


```text

ID: 20201212-162409

Date & Time: 2020-12-12 16:24:09
Module: admins.api.v1.admin_customer_api_view | Severity: MINOR :sweat_smile:
class-fun: NA-listing_csv
URL Method: POST | URL: /admins/api/v1/customer/listing-csv/
Request: {'ids': [21, 11]}
Response: NA
---ex---
Ex-Type: Cannot resolve keyword 'name' into field. Choices are: confirmorder, contact_no, contact_no_dail_code, country, country_id, created_at, created_by, dob, email, extra, first_name, gender, id, last_name, manageorder, profile_pic, status, updated_at, updated_by, user_proof
Traceback: Traceback (most recent call last):
 File "/usr/local/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1863, in add_fields
   join_info = self.setup_joins(name.split(LOOKUP_SEP), opts, alias, allow_many=allow_m2m)
 File "/usr/local/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1566, in setup_joins
   names[:pivot], opts, allow_many, fail_on_missing=True,
 File "/usr/local/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1482, in names_to_path
   "Choices are: %s" % (name, ", ".join(available)))
django.core.exceptions.FieldError: Cannot resolve keyword 'name' into field. Choices are: confirmorder, contact_no, contact_no_dail_code, country, country_id, created_at, created_by, dob, email, extra, first_name, gender, id, last_name, manageorder, profile_pic, status, updated_at, updated_by, user_proofDuring handling of the above exception, another exception occurred:Traceback (most recent call last):
 File "/usr/local/lib/python3.7/site-packages/rest_framework/views.py", line 502, in dispatch
   response = handler(request, *args, **kwargs)
 File "/usr/local/lib/python3.7/site-packages/rest_framework/decorators.py", line 50, in handler
   return func(*args, **kwargs)
 File "/usr/local/lib/python3.7/contextlib.py", line 74, in inner
   return func(*args, **kwds)
 File "/scdj/projsc/admins/api/v1/admin_customer_api_view.py", line 14, in listing_csv
   result = AdminCustomerRepository.listing_generate_csv(request)
 File "/scdj/projsc/customers/repositories/admin_customer_repository.py", line 46, in listing_generate_csv
   resultset = CustomerInfoService.fetch_listing_customer_data(request_data['ids'], csv_columns)
 File "/scdj/projsc/customers/services/customer_info_service.py", line 84, in fetch_listing_customer_data
   customer_object = CustomerInfo.objects.filter(id__in=customer_ids).values(*field_list)
 File "/usr/local/lib/python3.7/site-packages/django/db/models/query.py", line 841, in values
   clone = self._values(*fields, **expressions)
 File "/usr/local/lib/python3.7/site-packages/django/db/models/query.py", line 836, in _values
   clone.query.set_values(fields)
 File "/usr/local/lib/python3.7/site-packages/django/db/models/sql/query.py", line 2172, in set_values
   self.add_fields(field_names, True)
 File "/usr/local/lib/python3.7/site-packages/django/db/models/sql/query.py", line 1886, in add_fields
   "Choices are: %s" % (name, ", ".join(names)))
django.core.exceptions.FieldError: Cannot resolve keyword 'name' into field. Choices are: confirmorder, contact_no, contact_no_dail_code, country, country_id, created_at, created_by, dob, email, extra, first_name, gender, id, last_name, manageorder, profile_pic, status, updated_at, updated_by, user_proof

Extra Data: {'HTTP_HOST': '15.207.40.124', 'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36', 'QUERY_STRING': '', 'REMOTE_HOST': '', 'CONTENT_TYPE': 'application/json', 'SERVER_NAME': '25a87b1a2b3b', 'SERVER_PORT': '80', 'session': {'_SessionBase__session_key': 'qnhtvhk2rls5yn0g1tb0acn3h7ichcsp', 'accessed': True, 'modified': False, 'serializer': <class 'django.core.signing.JSONSerializer'>, 'model': <class 'django.contrib.sessions.models.Session'>, '_session_cache': {'is_authenticated': True, 'session_soon_expire': 1607872246, 'session_is_soon_expire': False, 'session_expire': 1607875846, 'user_session_data': {'username': 'ashish1a', 'email': 'sondagarashish@gmail.com', 'account_type': 'admin', 'user_id': 1, 'acl_slug': ['customer-address-detail', 'customer-address-list', 'customer-address-create', 'customer-address-update', 'customer-address-delete', 'admin-customer-dashboard-detail-by-id', 'create-customer', 'update-customer', 'list-customer', 'detail-customer', 'user-logout', 'customer-pdf', 'customer-csv', 'acl-tree', 'update-product-vendor', 'read-list-product-admin', 'read-detail-product-admin', 'delete-product-admin', 'upgrade-session-user', 'developer-menu', 'create-pro-admin', 'update-pro-admin', 'list-pro-admin', 'detail-pro-admin', 'test-v2b-home', 'request-info-home', 'detail-user-profile-login', 'update-user-profile-login', 'user-change-password', 'user-delete-account', 'product-curd', 'create-product-v2', 'update-product-v2', 'read-list-product-v2', 'read-detail-product-v2', 'delete-product-v2'], 'account_type_user_id': 'admin_1'}, 'customer_id': 21}, 'slacknotify_severity': 4}, 'cookies': "{'csrftoken': '1xYNftuRSoh9gbTfy4yklIzX3MS0bxhQxq77cTbWrzoHT7yiLj29TnAFhcr7kIsX', 'sessionid': 'qnhtvhk2rls5yn0g1tb0acn3h7ichcsp'}", 'remote_addr': '27.4.42.45'}
--- --- ---

```


> - sen_email_salt
> - online-tool - [link](https://10015.io/tools/md5-encrypt-decrypt)
> - Dev2022 -> MD5 encrypt -> `c8063b4a4823f1c542487f67a2557d61`
> - `c8063b4a4823f1c542487f67a2557d61` -> SHA1 encrypt -> `57fef2e83b67478972e611318bd7fc76edcfe5f5`


---
220213 0207p
## Issue:
```
2022-02-13T08:19:57.020948+00:00 app[web.1]:     raise SMTPAuthenticationError(code, resp)

2022-02-13T08:19:57.020993+00:00 app[web.1]: smtplib.SMTPAuthenticationError: (534, b'5.7.14 <https://accounts.google.com/signin/continue?sarp=1&scc=1&plt=AKgnsbv\n5.7.14 0U4lDuCSJuXxon4qOVzqg5qsWlmg9f5gR1X9i7LE5it4BEYv56tYsegiR4fV98gqxmZtH\n5.7.14 _SIHoHH2dtb934SwVHHnR6LCiEFv7lwMGoaTYP_J5uFZzVJXucAqSZ1Tym_E4nfW>\n5.7.14 Please log in via your web browser and then try again.\n5.7.14  Learn more at\n5.7.14  https://support.google.com/mail/answer/78754 o17sm2976192qtv.45 - gsmtp')
```
**Soln**:
- StackOverflow: - [link](https://stackoverflow.com/questions/55569031/django-email-sending-on-heroku)
- Allow less secure apps - [link](https://support.google.com/accounts/answer/6010255?hl=en)
- Display Unlock Captcha- [link](https://accounts.google.com/b/4/DisplayUnlockCaptcha)
