#1. 启动celery
```angular2
1.启动worker
celery worker -A test01 -l info -P eventlet
2.启动beat
celery beat -A test01 -l info -S django  &&
celery -A test01 beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

