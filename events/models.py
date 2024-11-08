from django.db import models

class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip_code', max_length=20)
    phone = models.CharField('Contact Phone', max_length=20)
    web = models.URLField('Website Address', )
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name

class MyClubUser(models.Model):
     first_name = models.CharField('First Name', max_length=120)
     last_name = models.CharField('Last Name', max_length=120)
     email = models.EmailField('Email Address')

     def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    # venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def  __str__(self):
        return self.name




# from django.db import models


# class Venue(models.Model):
#     name = models.CharField('Venue Name', max_length=120)
#     address = models.CharField(max_length=200)
#     zip_code = models.CharField('Zip Code',max_length=20)
#     phone = models.CharField('Contact', max_length=20)
#     web = models.URLField('Website Address')
#     email_address = models.EmailField('Email Address')

#     def __str__(self):
#         return self.name
    

# class MyClubUser(models.Model):
#     first_name = models.CharField('First Name', max_length=20)   
#     last_name  = models.CharField('Last Name', max_length=20)
#     phone = models.CharField('Contact', max_length=20)
#     email = models.EmailField('Email Address')

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name


# class Event(models.Model):
#     name = models.CharField('Event Name', max_length=120)
#     event_date = models.DateTimeField(max_length=20)
#     # venue = models.CharField('Venue' , max_length=60)
#     venue = models.ForeignKey('Venue' , blank=True, null=True, on_delete=models.CASCADE)
#     manager = models.CharField('Organizing Manager', max_length=20)
#     description = models.TextField(blank=True)
#     attendees = models.ManyToManyField(MyClubUser, blank=True)

#     def __str__(self):
#         return self.name