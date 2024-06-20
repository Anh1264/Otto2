from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Robot
from .utils import notify_mcu
from django.db import transaction


# @receiver(pre_save, sender=Robot)
# def notify_mcu_on_status_change(sender, instance, **kwargs):
#     # Check if the status has changed
#     print(instance.__dict__['status'],instance.status)
#     if 'status' in instance.__dict__ and instance.__dict__['status'] != instance.status:
#         notify_mcu(instance.robot_id, instance.status)


# @receiver(post_save, sender=Robot)
# def handle_robot_status_change(sender, instance, created, **kwargs):
#     if not created:
#         previous_instance = sender.objects.get(pk=instance.pk)
#         print(previous_instance.status, instance.status)
#         if previous_instance.status != instance.status:
#             notify_mcu(instance.robot_id, instance.status)


# @receiver(post_save, sender=Robot)
# def handle_robot_status_change(sender, instance, created, **kwargs):
#     if not created:
#         @transaction.on_commit
#         def callback():
#             previous_instance = sender.objects.get(pk=instance.pk)
#             print(previous_instance.status, instance.status)
#             if previous_instance.status != instance.status:
#                 notify_mcu(instance.robot_id, instance.status)

#         # Execute the callback after the transaction is committed
#         callback()


# def handle_robot_status_change(instance):
#     previous_instance = Robot.objects.get(pk=instance.pk)
#     print(previous_instance.status, instance.status)
#     if previous_instance.status != instance.status:
#         notify_mcu(instance.robot_id, instance.status)

# @receiver(post_save, sender=Robot)
# def post_save_robot(sender, instance, **kwargs):
#     if not kwargs.get('created'):
#         transaction.on_commit(lambda: handle_robot_status_change(instance))

@receiver(pre_save, sender=Robot)
def capture_previous_status(sender, instance, **kwargs):
    try:
        previous_instance = sender.objects.get(pk=instance.pk)
        instance._previous_status = previous_instance.status
        return instance._previous_status
    except sender.DoesNotExist:
        # This is a new instance, so there's no previous status
        instance._previous_status = None

@receiver(post_save, sender=Robot)
def notify_mcu_on_status_change(sender, instance, **kwargs):
    previous_status = getattr(instance, '_previous_status', None)
    current_status = instance.status

    print(previous_status, current_status)

    if previous_status != current_status:
        notify_mcu(instance.robot_id, current_status)