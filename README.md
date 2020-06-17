# 1. 启动celery
```angular2
1.启动worker
celery worker -A test01 -l info -P eventlet
2.启动beat
celery beat -A test01 -l info -S django  &&
celery -A test01 beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
3.ORM增加动态任务
from django_celery_beat.models import PeriodicTask
PeriodicTask.objects.create(name=1,task="base.task.add1",interval_id=2)
```

