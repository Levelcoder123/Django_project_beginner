from time import sleep

from celery import shared_task


@shared_task(bind=True)
def my_task(self):
    for i in range(10):
        print(i)
        sleep(1)

    return "Hi I am Muaz the great"
