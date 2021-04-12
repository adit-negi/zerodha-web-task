from .models import *
 
def cron_job():
    CsvUpload.objects.create(file_name = 'xxx')