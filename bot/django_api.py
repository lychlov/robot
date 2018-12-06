import django
from robot_admin.models import User


def check_auth(open_id):
    try:
        return True if User.objects.get(open_id=open_id) else False
    except:
        return False
