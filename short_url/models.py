from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['account_name', 'url_name'], name='unique_url_name')
        ]
        
    account_name = models.CharField(max_length=50)
    full_url = models.URLField()
    url_name = models.CharField(max_length=50)
    slug = models.SlugField()
    
    def __str__(self):
        return '%s/%s'%(self.account_name, self.url_name)
    
    def getRedirectURL(self, rootURL):
        return '%s/%s'%(rootURL, self.slug)
    
    
    