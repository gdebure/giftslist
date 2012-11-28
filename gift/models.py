from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class List(models.Model):
    '''A list of gifts'''

    name = models.CharField(max_length=128)
    target_date = models.DateField()
    owner = models.ForeignKey(User)
    comment = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_gifts(self):
        return self.gift_set.all()

    def get_absolute_url(self):
        url = reverse("detail_list", kwargs={'pk': self.id})
        return url




class Gift(models.Model):

    STATUS_CHOICES = (
                       ('W','Wished'), # Not Offered Yet
                       ('R','Reserved'), # Someone committed to offer it, making it unavailable for others
                       ('O','Offered'), # This gift has been offered,  making it unavailable for others
                    )

    name = models.CharField(max_length=256)
    description = models.TextField()
    lists = models.ManyToManyField(List)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)

    def __unicode__(self):
        return self.name

    def get_lists(self):
        return self.lists.all()

    def get_links(self):
        return self.giftlink_set.all()

class GiftLink(models.Model):

    gift = models.ForeignKey(Gift)
    url = models.URLField()

    def __unicode__(self):
        return self.url

