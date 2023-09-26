import multiprocessing

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
# worker_class = "gevent"
timeout = 60
loglevel = "info"
accesslog = "-"
errorlog = "-"
