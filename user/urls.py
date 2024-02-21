from django.urls import path
from .users.views.signin import SignIn
from .users.views.login import Login
from .users.views.account import Account
from .users.views.list_users import ListUser
from .users.views.administration import Administration
from .users.views.web_scraper import WebScraper
from .users.views.box import Box
from .users.views.send_message import SendMessage
from .users.views.PMessage import PMessage
from .users.views.Message import Message
from .users.views.register import Register
from .users.views.message_title import MessageTitle

urlpatterns = [
    path("sign-in/", SignIn.as_view(), name="signin"),
    path("register/", Register.as_view(), name="signin"),
    path("login/", Login.as_view(), name="login"),
    path("account/", Account.as_view(), name="account"),
    path("box/", Box.as_view(), name="box"),
    path("message_title/",MessageTitle.as_view(), name="box"),
    path("list_users/", ListUser.as_view(), name="list_user"),
    path("send_message/", SendMessage.as_view(), name="send_message"),
    path("administration/", Administration.as_view(), name="administration"),
    path("administration/web-scraper/", WebScraper.as_view(), name="web_scraper"),
    path("administration/PMessage/", PMessage.as_view(), name="web_scraper"),
    path("administration/PMessage/Message/<str>", Message.as_view(), name="web_scraper")
]
