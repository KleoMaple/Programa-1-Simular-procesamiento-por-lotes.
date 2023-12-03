import time
import sys
class Proceso:
    def __init__(self, num_programa, nombre, operacion, datos, tiempo_max):
        self.num_programa = num_programa
        self.nombre = nombre
        self.operacion = operacion
        self.datos = datos
        self.tiempo_max = tiempo_max
        self.tiempo_transcurrido = 0
        self.tiempo_restante = tiempo_max
        self.num_lote = None  # Agregar el atributo num_lote

    def ejecutar(self):
        
        print(f"  Número de Programa: {self.num_programa}")
        print(f"  Nombre: {self.nombre}")
        print(f"  Operación: {self.operacion} {self.datos}")
        print(f"  Tiempo Máximo Estimado: {self.tiempo_max}")
    def progreso(self):
        for i in range(int(self.tiempo_max)):
            time.sleep(1)
            self.tiempo_transcurrido += 1
            imprimir_barra_progreso(self.tiempo_transcurrido, self.tiempo_max)
        print("\nProceso terminado.")
        return eval(f"{self.datos[0]} {self.operacion} {self.datos[1]}")
class Lote:
    def __init__(self):
        self.procesos = []
        self.num_lote = 0  # Agregar el atributo num_lote
        self.procesosterminados = []

    def agregar_proceso(self, proceso):
        self.procesos.append(proceso)

    def ejecutar(self):
        print(f"Lote {self.num_lote} en ejecución:")
        for proceso in self.procesos:
            resultado = proceso.ejecutar()
            print(f"Resultado de la operación: {resultado}")
            print("=" * 40)
        print(f"Lote {self.num_lote} terminado.")
        
def imprimir_barra_progreso(tiempo_transcurrido, tiempo_total, longitud=40):
    porcentaje_completado = tiempo_transcurrido / tiempo_total
    longitud_completada = int(longitud * porcentaje_completado)
    barra_progreso = "|" + "=" * longitud_completada + "-" * (longitud - longitud_completada) + "|"
    sys.stdout.write(f"\rProgreso: {barra_progreso} {porcentaje_completado*100:.2f}%")
    sys.stdout.flush()

def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def es_operacion_valida(operacion):
    return operacion in ('+', '-', '*', '/', '%')

def imprimir_barra_progreso_global(tiempo_transcurrido, tiempo_total, longitud=40):
    porcentaje_completado = tiempo_transcurrido / tiempo_total
    longitud_completada = int(longitud * porcentaje_completado)
    barra_progreso = "|" + "=" * longitud_completada + "-" * (longitud - longitud_completada) + "|"
    sys.stdout.write(f"\rProgreso Global: {barra_progreso} {porcentaje_completado*100:.2f}%")
    sys.stdout.flush()

def main():
    num_lotes = 0
    lotes_pendientes = []
    ids_procesados = set()  # Para almacenar los IDs de los procesos procesados

    num_procesos = None
    while num_procesos is None:
        try:
            num_procesos = int(input("Ingrese el número de procesos: "))
            if num_procesos <= 0:
                print("El número de procesos debe ser mayor que 0.")
                num_procesos = None
        except ValueError:
            print("Ingrese un número válido para el número de procesos.")

    for i in range(num_procesos):
        print("\014")
        num_programa = input("Número de Programa (ID): ")
        num_programa = int(num_programa)
        while num_programa in ids_procesados:
            print(f"El ID {num_programa} ya ha sido utilizado. Ingrese un ID único.")
            num_programa = input("Número de Programa (ID): ")
            num_programa = int(num_programa)
        # Validar que num_programa sea un número y mayor o igual a 0
        while not es_numero(num_programa) or float(num_programa) < 0:
            print("El número de programa (ID) debe ser un número no negativo.")
            num_programa = input("Número de Programa (ID): ")

        
        ids_procesados.add(num_programa)  # Agregar el ID a la lista de IDs procesados

        nombre = input("Nombre de Programador: ")
        operacion = input("Operación (+, -, *, /, %): ")
        
        # Validar operación
        while not es_operacion_valida(operacion):
            print("Operación no válida. Ingrese una operación válida.")
            operacion = input("Operación (+, -, *, /, %): ")

        primer_dato = input("Primer dato: ")
        segundo_dato = input("Segundo dato: ")

        # Validar que los datos sean números
        while not (es_numero(primer_dato) and es_numero(segundo_dato)):
            print("Los datos deben ser números. Ingrese números válidos.")
            primer_dato = input("Primer dato: ")
            segundo_dato = input("Segundo dato: ")

        datos = [float(primer_dato), float(segundo_dato)]

        # Validar división por cero
        if operacion == '/' and datos[1] == 0:
            print("No se puede realizar una división por cero. Ingrese otro segundo dato.")
            segundo_dato = input("Segundo dato: ")
            while not es_numero(segundo_dato):
                print("El segundo dato debe ser un número. Ingrese otro segundo dato.")
                segundo_dato = input("Segundo dato: ")
            datos[1] = float(segundo_dato)
            
          # Validar división por cero
        if operacion == '%' and datos[1] == 0:
            print("No se puede realizar una división por cero. Ingrese otro segundo dato.")
            segundo_dato = input("Segundo dato: ")
            while not es_numero(segundo_dato):
                print("El segundo dato debe ser un número. Ingrese otro segundo dato.")
                segundo_dato = input("Segundo dato: ")
            datos[1] = float(segundo_dato)

        tiempo_max = None
        while tiempo_max is None:
            try:
                tiempo_max = float(input("Tiempo Máximo Estimado: "))
                if tiempo_max <= 0:
                    print("El tiempo máximo estimado debe ser mayor que 0.")
                    tiempo_max = None
            except ValueError:
                print("Ingrese un número válido para el tiempo máximo estimado.")
        proceso = Proceso(num_programa, nombre, operacion, datos, tiempo_max)

        if num_lotes == 0 or len(lotes_pendientes[num_lotes - 1].procesos) >= 5:
            num_lotes += 1
            lote_en_espera = Lote()
            lotes_pendientes.append(lote_en_espera)
        
        lotes_pendientes[num_lotes - 1].agregar_proceso(proceso)
        
        # Asignar el número de lote al proceso
        proceso.num_lote = num_lotes
        
    contador_global = 0
    total_tiempo_maximo = sum(proceso.tiempo_max for lote in lotes_pendientes for proceso in lote.procesos)

    tiempo_transcurrido_global = 0

    for i, lote in enumerate(lotes_pendientes):
        print("\014")
        print("=" * 40)
        num_lotes_pendientes = num_lotes - i
        for proceso in lote.procesos:
            resultado = proceso.ejecutar()
            proceso.progreso()
            print(f"Resultado de la operación: {resultado}")
            print("=" * 40)
            lote.procesosterminados.append(proceso)
            lote.procesos.pop(0)
            print("Procesos pendientes:\n")
            for proceso in lote.procesos:
                resultado2=proceso.ejecutar()
                print("\n")
            print("=" * 40)
            print("Procesos terminados")
            for proceso in lote.procesosterminados:
                resultados3=proceso.ejecutar()
                print("\n")
            tiempo_transcurrido_global += proceso.tiempo_max
            imprimir_barra_progreso_global(tiempo_transcurrido_global, total_tiempo_maximo)
        print(f"Número de lotes pendientes: {num_lotes_pendientes}")
        contador_global += 1
        print(f"\nLote {contador_global} terminado.")
        print("=" * 40)

    print("\nTodos los procesos han sido ejecutados.")

if __name__ == "__main__":
    main()