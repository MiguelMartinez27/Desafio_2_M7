from .models import Tarea, SubTarea


def recupera_tareas_y_sub_tareas():  # a
    tareas = Tarea.objects.all()
    for tarea in tareas:
        print(f"Tarea [{tarea.id}]: {tarea.descripcion} - {tarea.eliminada}")
        sub_tareas = SubTarea.objects.filter(tarea=tarea)
        for sub_tarea in sub_tareas:
            print(
                f"  SubTarea [{sub_tarea.id}]: {sub_tarea.nombre} - {sub_tarea.descripcion}"
            )


def crear_nueva_tarea(nombre, descripcion):  # b
    tarea = Tarea(id=id, nombre=nombre, descripcion=descripcion)
    tarea.save()
    imprimir_en_pantalla()


def crear_sub_tarea(tarea, nombre, descripcion):  # c
    sub_tarea = SubTarea(tarea=tarea, nombre=nombre, descripcion=descripcion)
    sub_tarea.save()
    imprimir_en_pantalla()


def elimina_tarea(tarea):  # d
    Tarea.objects.get(id=tarea.id).delete()
    imprimir_en_pantalla()


def elimina_sub_tarea(sub_tarea):  # e
    SubTarea.objects.get(id=sub_tarea.id).delete()
    imprimir_en_pantalla()


def imprimir_en_pantalla():  # f
    tareas = Tarea.objects.all()
    for tarea in tareas:
        print(f"[{tarea.id}] {tarea.descripcion}")
        sub_tareas = SubTarea.objects.filter(tarea=tarea)
        for sub_tarea in sub_tareas:
            print(f".... [{sub_tarea.id}] {sub_tarea.descripcion}")
