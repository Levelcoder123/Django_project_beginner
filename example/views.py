from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from example.tasks import my_task


def celery_task(request):
    my_task.delay()

    return HttpResponse("Task Started")


def schedule_task(request):
    interval, _ = IntervalSchedule.objects.get_or_create(
        every=30,
        period=IntervalSchedule.SECONDS,
    )

    PeriodicTask.objects.create(
        interval=interval,
        name='my_schedule',
        task='example.tasks.my_task',

    )

    return HttpResponse("Task Scheduled!")
