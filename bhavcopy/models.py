from django.db import models

# Create your models here.
class CsvUpload(models.Model):
    file_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = 'CsvUpload'
        verbose_name_plural = 'CsvUploads'
        db_table = 'csv_upload'

    def __str__(self):
        return str(self.id)