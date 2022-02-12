from django.conf import settings
from django.utils.html import format_html


def display_profile_pic_helper(file_path):
    s3_path = settings.S3_BKT_PATH
    return format_html(f'<a href="{s3_path}{file_path}" target="_blank"><img src="{s3_path}{file_path}" width=50 height=50 style="border: solid 1px gray;" /></a>&nbsp;')
