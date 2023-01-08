from django.db import models



class ContactModel(models.Model):
    '''
    Contact forms models.
    '''
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)

    class Meta:
        verbose_name = ("Contact Model")

    def __str__(self):
        return str(self.name)