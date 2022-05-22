from celery import shared_task


@shared_task
def charge():
    print("charge per 5 min...")
