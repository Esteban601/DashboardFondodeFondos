from django.urls import path

from . import views

urlpatterns = [
        # path('', views.index, name='index'),
        path('', views.financieros, name='financieros'),

        path('operacion', views.operacion, name='operacion'),
        path('financieros', views.financieros, name='financieros'),
        path('impuestos_utilidad', views.impuestos_utilidad, name='impuestos_utilidad'),
        path('utilidad_neta', views.utilidad_neta, name='utilidad_neta'),
        path('salario_min', views.salario_min, name='salario_min'),
        path('inversiones_comunitarias', views.inversiones_comunitarias, name='inversiones_comunitarias'),
        path('inversion_ausencias', views.inversion_ausencias, name='inversion_ausencias'),
        path('inversion_prestaciones', views.inversion_prestaciones, name='inversion_prestaciones'),
        path('invertido_iniciativas', views.invertido_iniciativas, name='invertido_iniciativas'),
        path('perdidas_demandas', views.perdidas_demandas, name='perdidas_demandas'),

        path('consumo_energetico', views.consumo_energetico, name='consumo_energetico'),
        path('consumo_energia_renobable', views.consumo_energia_renobable, name='consumo_energia_renobable'),
        path('reduccion_consumo_energia', views.reduccion_consumo_energia, name='reduccion_consumo_energia'),

        path('empleados_funcion', views.empleados_funcion, name='empleados_funcion'),
        path('satisfaccion_empleados', views.satisfaccion_empleados, name='satisfaccion_empleados'),
        path('rotacion_empleados', views.rotacion_empleados, name='rotacion_empleados'),

        path('accionistas_mayoritarios', views.accionistas_mayoritarios, name='accionistas_mayoritarios'),
        path('consejo_admon', views.consejo_admon, name='consejo_admon'),
        path('consejo_admon_independientes', views.consejo_admon_independientes, name='consejo_admon_independientes'),
        path('areas_direccion', views.areas_direccion, name='areas_direccion'),
        path('directivos_relevantes', views.directivos_relevantes, name='directivos_relevantes'),
        path('compensacines_personal_clave', views.compensacines_personal_clave, name='compensacines_personal_clave'),


        path('', views.index, name='aviso-privacidad'),
        path('', views.index, name='search'),
        path('', views.index, name='economia')
    ]