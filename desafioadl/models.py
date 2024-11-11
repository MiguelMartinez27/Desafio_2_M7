from django.db import models


class Tarea(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    descripcion = models.TextField(primary_key=True, default="", null=False)
    eliminada = models.BooleanField(default=False)


class SubTarea(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    descripcion = models.TextField(default="", null=False)
    eliminada = models.BooleanField(default=False)
    tarea_id = models.ForeignKey("Tarea", on_delete=models.CASCADE)
