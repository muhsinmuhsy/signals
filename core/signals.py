from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_new_user_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New User Registered'
        message = 'A new user has registered with the username: {}'.format(instance.username)
        from_email = 'admin@example.com'  # Your admin email
        to_email = ['admin@example.com']  # Admin's email(s)
        # send_mail(subject, message, from_email, to_email)
        print(subject, message, from_email, to_email)

