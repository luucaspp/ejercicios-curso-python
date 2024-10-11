usuarioDia1 = input()
horario1 = input()
usuarioDia2 = input()
horario2 = input()

for caracter in range(len(usuarioDia1)):
    if usuarioDia1[caracter] == " ":
        dia1 = int(usuarioDia1[caracter + 1:])
        break

for caracter in range(len(usuarioDia2)):
    if usuarioDia2[caracter] == " ":
        dia2 = int(usuarioDia2[caracter + 1:])
        break

hora1 = int(horario1[:2])
hora2 = int(horario2[:2])

minuto1 = int(horario1[5:7])
minuto2 = int(horario2[5:7])

segundo1 = int(horario1[10:])
segundo2 = int(horario2[10:])

segundosTotal1 = dia1 * 86400 + hora1 * 3600 + minuto1 * 60 + segundo1
segundosTotal2 = dia2 * 86400 + hora2 * 3600 + minuto2 * 60 + segundo2
diferencia = segundosTotal2 - segundosTotal1

dia = int(diferencia / 86400)
diferencia = diferencia - (dia * 86400)

hora = int(diferencia / 3600)
diferencia = diferencia - (hora * 3600)

minuto = int(diferencia / 60)
diferencia = diferencia - (minuto * 60)

segundo = int(diferencia)

print(str(dia), "dia(s)")
print(str(hora), "hora(s)")
print(str(minuto), "minuto(s)")
print(str(segundo), "segundo(s)")