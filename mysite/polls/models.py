from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
        
    def __unicode__(self):  
        return u'%s , %s' % (self.question_text, self.pub_date) 
        
    def was_published_recently(self):
        return self.pub_date >= timezone.now()
    
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_question = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):  
        return u'%s' % (self.choice_question)