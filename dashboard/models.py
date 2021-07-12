from django.db import models

from django.db import models



from django.contrib.auth.models import User

from io import BytesIO
from django.db.models.fields import EmailField
from django.http import HttpResponse
from django.template.loader import get_template



from xhtml2pdf import pisa

# Create your models here.

CATEGORY = (
    ('Bulk', 'Bulk'),
    ('Pallet', 'Pallet')
)

class Inward(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveBigIntegerField(null=True)
    #date = models.DateTimeField('date published')
    #itemcode = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Inward'

    def __str__(self):
        return f'{self.name}-{self.quantity}-{self.category}'


class Chamber(models.Model):
    #name = models.CharField(max_length=100)
    inward = models.ForeignKey(Inward, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Chamber'

    def __str__(self):
        return f'{self.category} ordered at {self.date}'

class Dispatch(models.Model):
    inward = models.ForeignKey(Inward, on_delete=models.CASCADE, null=True)
    client = models.ForeignKey(User, models.CASCADE, null=True)
    product_quantity = models.PositiveBigIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Dispatch'


    def __str__(self):
        return f'{self.inward} ordered by {self.client}'


class Client(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    
    class Meta:
        verbose_name_plural = 'Client'

    def __str__(self):
        return f'{self.name}-{self.email}'



def render_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
 
     #This part will create the pdf.
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None


