


# from sales.models import Sales
# from django.db.models.signals import m2m_changed
# from django.dispatch import receiver
# from sales.utils import generate_id


# @receiver(m2m_changed, sender=Sales.positions.through)
# def sales_price(sender, instance, action, **kwargs):
#     net_price = 0
#     if action == "post_add" or action == "pre_add":
#         for each in instance.get_positions():

#             net_price += each.price

#     instance.net_price = net_price
#     instance.save()
