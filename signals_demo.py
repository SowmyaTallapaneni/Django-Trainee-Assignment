# Import necessary modules
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time
import threading
from django.db import transaction

# Signal receiver function (For Question 1: Synchronous/Asynchronous execution)
@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal started execution (synchronously)")
    time.sleep(5)  # Simulate a delay in the signal handling to prove synchronous execution
    print("Signal finished execution")

# Signal receiver function (For Question 2: Running in the same thread as the caller)
@receiver(post_save, sender=User)
def my_signal_receiver_thread(sender, instance, **kwargs):
    print(f"Signal running in thread: {threading.current_thread().name}")

# Signal receiver function (For Question 3: Running in the same database transaction)
@receiver(post_save, sender=User)
def my_signal_receiver_transaction(sender, instance, **kwargs):
    if transaction.get_autocommit():
        print("Signal running outside of a transaction")
    else:
        print("Signal running inside a transaction")

# Code to create a User object and trigger the signals
if __name__ == '__main__':
    # Creating a new user, which will trigger the post_save signal
    user = User.objects.create(username='testuser')

    print(f"Main thread: {threading.current_thread().name}")
    print("User created")
