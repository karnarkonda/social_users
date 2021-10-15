from random import randint
## Receivers ##
def set_user_code(sender, **kwargs):
    _user = kwargs.get('instance')
    _user.user_code = f"User{randint(0, 300)}"