# variables para contar incidentes
total_incidentes = 0
leves = 0
graves = 0
eso = 0
post_obligatoria = 0

# bucle principal
registrar = input("¿Desea registrar un nuevo incidente? S (Sí) / N (No): ").upper()
while registrar == "S":
    nivel = input("¿En qué nivel ha ocurrido? E (ESO) / P (Post-Obligatoria): ").upper()
    while nivel != "E" and nivel != "P":
        nivel = input("Nivel inválido. Introduzca E (ESO) o P (Post-Obligatoria): ").upper()

    tipo = input("¿Qué tipo de incidente ha ocurrido? L (Leve) / G (Grave): ").upper()
    while tipo != "L" and tipo != "G":
        tipo = input("Tipo inválido. Introduzca L (Leve) o G (Grave): ").upper()

    total_incidentes += 1
    if tipo == "L":
        leves += 1
    else:
        graves += 1

    if nivel == "E":
        eso += 1
    else:
        post_obligatoria += 1

    registrar = input("¿Desea registrar un nuevo incidente? S (Sí) / N (No): ").upper()

print("Incidentes registrados.")

# cálculo de porcentajes
if total_incidentes > 0:
    porcentaje_eso = int((eso * 100) / total_incidentes) # lo tuve que buscar x,d
    porcentaje_post = 100 - porcentaje_eso
else:
    porcentaje_eso = 0
    porcentaje_post = 0

# informe resumen
print("Se han producido", total_incidentes, "incidentes en el centro:",
      leves, "de ellos Leves y", graves, "Graves, siendo el",
      str(porcentaje_eso) + "% en ESO y el", str(porcentaje_post) + "% en Post-Obligatoria.")
