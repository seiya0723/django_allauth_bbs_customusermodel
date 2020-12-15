from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    class Meta(AbstractUser.Meta):
        db_table    = 'custom_users'

    age = models.IntegerField(verbose_name="年齢",default=20)


#TIPS:下記のようにまず最初にカスタムユーザーのマイグレーションファイルを作る、その次に通常アプリのマイグレーションを実行し、反映させなければならない。プロジェクト作成直後にカスタムユーザーモデルを作らないといけないわけはこれにある。
"""
python3 manage.py makemigrations users
python3 manage.py migrate
↓
python3 manage.py makemigrations bbs
python3 manage.py migrate
"""

#forms.pyにて、models.pyで定義したageの指定をする
