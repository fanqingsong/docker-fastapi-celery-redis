import os
import time
from celery import Celery
from celery.utils.log import get_task_logger
import redis



logger = get_task_logger(__name__)


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)



# # Connect Redis db
# redis_db = redis.Redis(
#     host="localhost", port="6379", db=1, charset="utf-8", decode_responses=True
# )

# # Initialize timer in redis
# redis_db.mset({"minute": 0, "second": 0})



# Add periodic tasks
celery_beat_schedule = {
    "time_scheduler": {
        "task": "tasks.timer",
        # Run every second
        "schedule": 1.0,
    }
}


celery.conf.update(
    result_backend=CELERY_RESULT_BACKEND,
    broker_url=CELERY_BROKER_URL,
    timezone="UTC",
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    beat_schedule=celery_beat_schedule,
)


@celery.task(name='tasks.timer')
def timer():
    # second_counter = int(redis_db.get("second")) + 1
    # if second_counter >= 59:
    #     # Reset the counter
    #     redis_db.set("second", 0)
    #     # Increment the minute
    #     redis_db.set("minute", int(redis_db.get("minute")) + 1)
    # else:
    #     # Increment the second
    #     redis_db.set("second", second_counter)

    logger.critical("second")
    logger.critical("222222222222")


@celery.task(name='tasks.add')
def add(x: int, y: int) -> int:
    time.sleep(5)
    return x + y
