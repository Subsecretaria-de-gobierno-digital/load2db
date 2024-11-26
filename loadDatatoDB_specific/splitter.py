def split_centro_gestor(centro_gestor):
    centro_gestor = centro_gestor[:10] if centro_gestor else '' 
    return [centro_gestor[0] if len(centro_gestor) > 0 else '',
            centro_gestor[1:3] if len(centro_gestor) > 1 else '',
            centro_gestor[3:5] if len(centro_gestor) > 3 else '',
            centro_gestor[5:8] if len(centro_gestor) > 5 else '',
            centro_gestor[8:10] if len(centro_gestor) > 8 else '']

def split_fondo(fondo):
    fondo = fondo[:8] if fondo else ''
    return [fondo[0:2] if len(fondo) > 0 else '',
            fondo[2] if len(fondo) > 2 else '',
            fondo[3] if len(fondo) > 3 else '',
            fondo[4:6] if len(fondo) > 4 else '',
            fondo[6:8] if len(fondo) > 6 else '']

def split_posicion_presupuestaria(posicion):
    posicion = posicion[:6] if posicion else ''
    return [posicion[0:5] if len(posicion) > 0 else '',
            posicion[5] if len(posicion) > 5 else '']

def split_area_funcional(area):
    area = area[:16] if area else ''
    return [area[0] if len(area) > 0 else '',
            area[1] if len(area) > 1 else '',
            area[2:4] if len(area) > 2 else '',
            area[4:6] if len(area) > 4 else '',
            area[6:8] if len(area) > 6 else '',
            area[8] if len(area) > 8 else '',
            area[9:11] if len(area) > 9 else '',
            area[11:14] if len(area) > 11 else '',
            area[14] if len(area) > 14 else '',
            area[15] if len(area) > 15 else '']