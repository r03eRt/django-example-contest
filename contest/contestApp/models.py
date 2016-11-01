from __future__ import unicode_literals

from django.db import models
from datetime import datetime





"""Province model"""
class Province(models.Model):
    # Anadimos  campos al modelo
    name = models.CharField(
        max_length=255,
        verbose_name='Provincia'
    )

    # Como se mostrara en el admin cuando se le referencie
    def __unicode__(self):
        return self.name

    # Como se llama cuando hay varois en el admin
    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'


"""Participant model"""
class Participant(models.Model):

    name = models.CharField(
        max_length=40,
        verbose_name='Nombre'
    )

    surname = models.CharField(
        max_length=70,
        verbose_name='Apellidos'
    )

    dni = models.CharField(
        max_length=15,
        verbose_name='DNI/NIF'
    )

    email = models.EmailField(
        max_length=40,
        verbose_name='Email'
    )

    phone = models.CharField(
        max_length=40,
        verbose_name='Telafono'
    )

    profession = models.CharField(
        max_length=255,
        verbose_name='Profesion',
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        verbose_name='Fecha del alta',
        auto_now_add=True,
        auto_now=False,
        blank=True
    )

    province = models.ForeignKey(
        Province,
        verbose_name='Provincia'
    )


    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'

    def __unicode__(self):
        return self.name



"""Picture model"""
class Picture(models.Model):
    #objects = PictureManager()

    created = models.DateTimeField(
        verbose_name='Fecha creacion',
        default=datetime.now
    )

    url = models.ImageField(
        max_length=255,
        verbose_name='Imagen',
        upload_to='treasure_images',
        default='default.png',
        null=True,
        blank=True
    )

    description = models.CharField(
        max_length=255,
        verbose_name='Descripcion'
    )

    # Access to foreignkey values
    @property
    def get_votes(self):
        return Vote.objects.filter(foto=self.id).count()
    # define verbose name of a property for admin dashboard
    get_votes.fget.short_description = 'Num Votos'

    # Add thumbnail with popup to admin
    def image_img(self):
        if self.url:
            return u'<a onclick="return showAddAnotherPopup(this);" href="http://localhost:8000/media/%s" target="_blank"><img src="http://localhost:8000/media/%s" width="125px" height="auto"/></a>' % (self.url,self.url)
        elif self.url == '':
            return '(Sin imagen)'
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Foto'
    # Allow insert html tags
    image_img.allow_tags = True

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

    def __unicode__(self):
        return "Imagen %s" % self.id



class Vote(models.Model):
    foto = models.ForeignKey(
        Picture,
        verbose_name = 'Foto votada'
    )

    created = models.DateTimeField(
        verbose_name = 'Fecha voto',
        auto_now_add=True
    )

    email = models.EmailField(
        verbose_name = 'Email del votante'
    )

    def __unicode__(self):
        return "voto %s" % self.id

#objects = PictureManager()

#class PictureManager(models.Manager):
#    def get_votes(self):
#        queryset = Participant.objects.all()
#        return queryset.count()
