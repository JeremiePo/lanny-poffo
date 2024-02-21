from django.contrib.auth.models import User


def request_user(user):

    user_name = User.objects.get(username=user)

    if user_name.is_staff == False:
        raise Exception
    else:
        print("non")
