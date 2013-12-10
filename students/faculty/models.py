# -*- coding: utf-8 -*-
from django.db import models


class Student(models.Model):
    last_name = models.CharField(u"Фамилия", max_length=30)
    first_name = models.CharField(u"Имя", max_length=20)
    middle_name = models.CharField(u"Отчество", max_length=30)
    date_of_birth = models.DateField(u"Дата рождения")
    id_card_number = models.PositiveIntegerField(u"Номер студенческого билета")
    group = models.ForeignKey("Group", verbose_name=u"Группа",
                              null=True, blank=True)

    class Meta:
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенты"

    def __unicode__(self):
        return u"%s %s %s" % (self.last_name,
                              self.first_name,
                              self.middle_name)


class Group(models.Model):
    name = models.CharField(u"Название", max_length=30)
    senior_student = models.OneToOneField(Student,
                                          related_name="senior_student",
                                          null=True, blank=True,
                                          on_delete=models.SET_NULL)

    class Meta:
        verbose_name = u"Группа"
        verbose_name_plural = u"Группы"

    def __unicode__(self):
        return u"%s" % self.name
