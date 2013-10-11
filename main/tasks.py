from celery import task


@task(max_retries=3)
def dummy_task(arg):
    return arg + arg
