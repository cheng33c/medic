from .models import User

class EmailBackend(object):
    '''邮件推送'''
    def authenticate(self, request, **credentials):

        email = credentials.get('email', credentials.get('username'))
        print(email)
        try:
            user = User.objects.get(email=email)
            print(user)
        except User.DoesNotExist:
            pass
        else:
            if user.check_password(credentials["password"]):
                return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
