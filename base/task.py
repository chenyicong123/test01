from celery import shared_task
from celery.task import periodic_task


@shared_task
def add():
    print(1)

@shared_task
def add1():
    print(2)


# @periodic_task(run_every=10, name="task.get.list")
# def add1():
#     print('*')