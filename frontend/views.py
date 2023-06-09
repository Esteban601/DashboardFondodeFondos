from django.shortcuts import render
from django.utils.translation import gettext as _


# Create your views here.

def index(request):
    context = {
        'page': _('index')
    }
    return render(request, 'frontend/index.html', context)


##################
# Económicos
##################

def operacion(request):
    context = {
        'page': _('operacion'),
        'section': _('economicos')
    }
    return render(request, 'frontend/economicos/operacion.html', context)


def financieros(request):
    context = {
        'page': _('financieros'),
        'section': _('economicos')
    }
    return render(request, 'frontend/economicos/financieros.html', context)


def impuestos_utilidad(request):
    context = {
        'page': _('impuestos_utilidad'),
        'section': _('economicos')
    }
    return render(request, 'frontend/economicos/impuestos_utilidad.html', context)


def utilidad_neta(request):
    context = {
        'page': _('utilidad_neta'),
        'section': _('economicos')
    }
    return render(request, 'frontend/economicos/utilidad_neta.html', context)


def salario_min(request):
    context = {
        'page': _('salario_min'),
        'section': _('economicos')
    }
    return render(request, 'frontend/economicos/salario_min.html', context)


def inversiones_comunitarias(request):
    context = {
        'page': _('inversiones_comunitarias'),
        'section': _('economicos')
    }
    return render(request, 'frontend/economicos/inversiones_comunitarias.html', context)


def inversion_ausencias(request):
    context = {
        'page': _('inversion_ausencias'),
        'section': _('economicos')
    }
    return render(request, 'frontend/economicos/inversion_ausencias.html', context)


def inversion_prestaciones(request):
    context = {
        'page': _('inversion_prestaciones'),
        'section': _('economicos')
    }
    return render(request, 'frontend/economicos/inversion_prestaciones.html', context)


def invertido_iniciativas(request):
    context = {
        'page': _('invertido_iniciativas'),
        'section': _('economicos')
    }
    return render(request, 'frontend/economicos/invertido_iniciativas.html', context)


def perdidas_demandas(request):
    context = {
        'page': _('perdidas_demandas'),
        'section': _('economicos')
    }
    return render(request, 'frontend/economicos/perdidas_demandas.html', context)


###############
# Ambientales
##############


def consumo_energetico(request):
    context = {
        'page': _('consumo_energetico'),
        'section': _('ambientales')
    }
    return render(request, 'frontend/ambientales/consumo_energetico.html', context)


def consumo_energia_renobable(request):
    context = {
        'page': _('consumo_energia_renobable'),
        'section': _('ambientales')
    }
    return render(request, 'frontend/ambientales/consumo_energia_renobable.html', context)


def reduccion_consumo_energia(request):
    context = {
        'page': _('reduccion_consumo_energia'),
        'section': _('ambientales')
    }
    return render(request, 'frontend/ambientales/reduccion_consumo_energia.html', context)


#############################
#sociales
#############################


def empleados_funcion(request):
    context = {
        'page': _('empleados_funcion'),
        'section': _('sociales')
    }
    return render(request, 'frontend/sociales/empleados_funcion.html', context)


def satisfaccion_empleados(request):
    context = {
        'page': _('satisfaccion_empleados'),
        'section': _('sociales')
    }
    return render(request, 'frontend/sociales/satisfaccion_empleados.html', context)


def rotacion_empleados(request):
    context = {
        'page': _('rotacion_empleados'),
        'section': _('sociales')
    }
    return render(request, 'frontend/sociales/rotacion_empleados.html', context)

#############################
#gobierno_corporativo
#############################


def accionistas_mayoritarios(request):
    context = {
        'page': _('accionistas_mayoritarios'),
        'section': _('gobierno_corporativo')
    }
    return render(request, 'frontend/gobierno/accionistas_mayoritarios.html', context)


def consejo_admon(request):
    context = {
        'page': _('consejo_admon'),
        'section': _('gobierno_corporativo')
    }
    return render(request, 'frontend/gobierno/consejo_admon.html', context)


def consejo_admon_independientes(request):
    context = {
        'page': _('consejo_admon_independientes'),
        'section': _('gobierno_corporativo')
    }
    return render(request, 'frontend/gobierno/consejo_admon_independientes.html', context)


def areas_direccion(request):
    context = {
        'page': _('areas_direccion'),
        'section': _('gobierno_corporativo')
    }
    return render(request, 'frontend/gobierno/areas_direccion.html', context)


def directivos_relevantes(request):
    context = {
        'page': _('directivos_relevantes'),
        'section': _('gobierno_corporativo')
    }
    return render(request, 'frontend/gobierno/directivos_relevantes.html', context)


def compensacines_personal_clave(request):
    context = {
        'page': _('compensacines_personal_clave'),
        'section': _('gobierno_corporativo')
    }
    return render(request, 'frontend/gobierno/compensacines_personal_clave.html', context)
