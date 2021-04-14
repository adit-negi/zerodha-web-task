from celery import shared_task

@shared_task
def add():
    print(3+3)
    return True