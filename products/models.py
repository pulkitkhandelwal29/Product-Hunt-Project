from django.db import models
from django.contrib.auth.models import User

#Steps:-

#Create a Product model
class Product(models.Model):
    # title
    title = models.CharField(max_length=255)
    # pub_date (publish date)
    pub_date = models.DateTimeField()
    # body
    body = models.TextField()
    #url
    url = models.TextField()
    # image
    image= models.ImageField(upload_to = 'images/')
    #icon
    icon= models.ImageField(upload_to = 'images/')
    #votes_total
    votes_total = models.IntegerField(default=1)
    #hunter(user)
    #It is referencing to the user stored in database through different model
    #on_delete is that if the user account is deleted, then the products added by him will also delete
    hunter = models.ForeignKey(User,on_delete = models.CASCADE)

    #Providing formatting for pretty products
    def summary(self):
        '''Returns the first 100 characters of the big whole summary '''
        return self.body[:100]

    def pub_date_pretty(self):
        '''Returns the published date in the proper format '''
        return self.pub_date.strftime('%b %e %Y')


    #Also we can change the appearance of name in Admin page like "Product Project 1" to "title"
    #for better remembering
    def __str__(self):
        '''__str__ is the name that is stored on admin page '''
        return self.title





#Add the Product App to the settings (in the settings.py, under INSTALLED_APPS section)

#Create a migration(python manage.py makemigrations)
#Migrate(python manage.py migrate)
#These above steps need to be done in terminal


#Add to the admin
#The model has to be registered in the admin.py file of the particular model
