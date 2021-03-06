from django.db import models

class DataSelect(models.Model):
    filename = models.CharField(max_length = 50, verbose_name = 'filename')
    colname = models.CharField(max_length = 50, verbose_name = 'colname')
    check_status = models.CharField(max_length = 4, verbose_name = 'col_status',choices = (('C','Checked'),('U','Unchecked')))
    create_time = models.DateTimeField(verbose_name= 'create_time',auto_now_add= True)
    create_date = models.DateTimeField(verbose_name= 'create_time',auto_now_add= True)
    # status = models.CharField(verbose_name = 'status', choices = )

    def __str__(self):
        return self.filename


    class Meta:
        verbose_name = 'DataSelect'
        verbose_name_plural = verbose_name    