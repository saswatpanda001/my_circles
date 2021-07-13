from costumers.models import costumer_model
from social.models import userdt_model
import uuid


def generate_id():
    code = str(uuid.uuid4()).replace('-', '')[:12]
    return code


def get_salesman(val):
    x = userdt_model.objects.get(pk=val)
    return x.user


def get_costumer(val):
    y = costumer_model.objects.get(id=val)
    return y.name
