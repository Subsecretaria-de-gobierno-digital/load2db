from splitter import (
    split_centro_gestor,
    split_posicion_presupuestaria,
    split_fondo,
    split_area_funcional
)


def process(input_data):
    columns = input_data[0]

    output = []
    output.append(columns + ['poder', 'dependencia', 'sector_institucional', 'unidad_responsable', 'centro_de_costos',
                             'ano', 'clasificador_fondo', 'fuente_financiamiento', 'fondo_financiamiento', 'area_geografica',
                             'clasificador_pp', 'tipo_gasto',
                             'finalidad', 'funcion', 'subfuncion', 'eje_trabajo', 'objetivo_estrategico', 'modalidad', 'programa_presupuestario', 'actividad', 'tipo_beneficiario', 'servicios_personales'])
    
    for line in input_data[1:]:
        centro_gestor = split_centro_gestor(line[columns.index('centro_gestor')])
        fondo = split_fondo(line[columns.index('fondo')])
        posicion = split_posicion_presupuestaria(line[columns.index('posicion_presupuestaria')])
        area = split_area_funcional(line[columns.index('area_funcional')])

        line.extend(centro_gestor + fondo + posicion + area)
        output.append(line)

    return output