import django
from robot_admin.models import User, QueryLog


def check_auth(open_id):
    try:
        return True if User.objects.get(open_id=open_id) else False
    except:
        return False


def new_query(open_id, uuid, url):
    try:
        q = QueryLog(open_id=open_id, uuid=uuid, url=url)
        q.save()
        return True
    except Exception as e:
        print(e)
        return False


def get_url(open_id, uuid):
    try:
        return QueryLog.objects.get(open_id=open_id, uuid=uuid).url
    except:
        return None
