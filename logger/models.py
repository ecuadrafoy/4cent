from django.db import models
from django.urls import reverse
from django.utils import timezone

# Class for Casualties report?


class CompletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='completed')


class VerifyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='to_verify')


class Country(models.Model):
    name = models.CharField(max_length=20)
    continent = models.CharField(max_length=10)
    capital = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

class PIR(models.Model):
    PIR_number = models.CharField('PIR Number and Value', max_length=50, blank=True)
    description = models.CharField(max_length=40, help_text='Describe the PIR')
    class Meta:
        verbose_name = "PIR"
        verbose_name_plural = "PIR"
    def __str__(self):
        return self.PIR_number


class event_type(models.Model):
    event_type = models.CharField(max_length=40, help_text='Write the type of event, e.g. IED, protest, ambush, etc')
    class Meta:
        verbose_name = "Type of Event"
        verbose_name_plural = "Type of Event"
    def __str__(self):
        return self.event_type


letter = ["A", "B", "C", "D", "E", "F"]
number = list(range(7))
#rel = list(map(lambda tup: ''.join(list(tup)), zip(letter,number)))
rel = list(zip(letter, number))


class Source(models.Model):
    """Model representing the soruce of traffic"""
    source_name = models.CharField(verbose_name='Source name', max_length=40)
    reliability = models.CharField(
        verbose_name='Reliability level', max_length=40, choices=rel, blank=True)
    nationality = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        """Returns the url to a particular source"""
        return reverse('source-detail', args=[self.source_name])

    def __str__(self):
        """String for representing the Model object"""
        return self.source_name

class Traffic(models.Model):
    """Class that takes a piece of traffic and adds it to the database"""
    STATUS_CHOICES = (
        ('live', 'Live'),
        ('completed', 'Completed'),
        ('to_verify', 'To Verify')
    )
    #Entry = models.IntegerField(primary_key=True, default=1)
    docname = models.CharField(max_length=100,
                               help_text='Enter title of document',
                               default="")
    traffic_slug = models.SlugField(max_length=250,
                                    unique_for_date='docdate')
    docdate = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(event_type,
                                 on_delete=models.CASCADE, blank=True, null=True)
    fulltext = models.TextField(help_text='Enter the full traffic text if possible')
    grids = models.CharField(max_length=40, help_text='Assign grid location', 
                            blank=True)
    source = models.ForeignKey(Source, on_delete=models.CASCADE,
                               blank=True, null=True)
    PIR = models.ForeignKey(PIR, blank=True, 
                            on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,
                              default='to_verify')

    #completed = CompletedManager()
    #verify = VerifyManager()

    class Meta:
        ordering = ('-docdate',)
        verbose_name = "Traffic"
        verbose_name_plural = "Traffic"

    def __str__(self):
        """String for representing the Traffic model object"""
        return self.docname

    def get_absolute_url(self):
        """Returns the url to access an instance of a model."""
        return reverse('logger:traffic_detail',
                       args=[self.docdate.year,
                             self.docdate.month,
                             self.docdate.day, self.traffic_slug])


class Organizations(models.Model):
    """Model to represent the organizations encountered"""
    name_org = models.CharField(
        max_length=40, help_text='Please enter the name of this organization')
    members = models.IntegerField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name_org

class Equipment(models.Model):
    name = models.CharField(
        max_length=40, help_text='Please enter the name of the piece of equipment observed')
    role = models.CharField(max_length=40, 
                            help_text='Write the role for this piece of equipment (e.g. MBT, APC, IFV, etc.)',
                            blank=True)
    # An equipment can belong to one or many organizations
    unit = models.ManyToManyField(Organizations)
    origin_manufacture = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class EventMatrix(models.Model):
    """
    This database in theory should display an event matrix, however I'm thinking of making this into a 
    view instead
    """
    reference = models.ForeignKey(
        "Traffic", on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(
        "event_type", on_delete=models.SET_NULL, null=True)
    actor_1 = models.ForeignKey(Organizations, on_delete=models.CASCADE,
                               blank=True, null=True, related_name='attacker')
    actor_2 = models.ForeignKey(Organizations, on_delete=models.CASCADE,
                               blank=True, null=True, related_name='victim')
    location = models.CharField(max_length=40)
    deceased = models.IntegerField()
    wounded = models.IntegerField()
    class Meta():
        verbose_name_plural = "Event Matrix"

    def __str__(self):
        return self.reference
