import socket
import ipaddress
from datetime import datetime


def obtener_ip_local():
    # Consulta la IPv4 que usaría el equipo para conectarse.
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as conexion:
            conexion.connect(("192.0.2.1", 80))
            direccion = conexion.getsockname()[0]

        ip = ipaddress.IPv4Address(direccion)

        if not ip.is_loopback and not ip.is_unspecified:
            return str(ip)

    except (OSError, ipaddress.AddressValueError):
        pass

    return None


def pedir_ip():
    direccion_local = obtener_ip_local()

    print()

    if direccion_local:
        print(f"IP detectada: {direccion_local} (IP DEL EQUIPO LOCAL)")
    else:
        print("No se pudo detectar la IPv4 del equipo local.")
        print("Para analizar este equipo puedes utilizar 127.0.0.1.")

    while True:
        entrada = input("\nDirección IP a analizar: ").strip()

        try:
            return str(ipaddress.IPv4Address(entrada))
        except ipaddress.AddressValueError:
            print("IP inválida. Ejemplo: 127.0.0.1")


def pedir_puerto(mensaje):
    # Revisa que el puerto sea un número válido.
    while True:
        try:
            puerto = int(input(mensaje))

            if 1 <= puerto <= 65535:
                return puerto

            print("Ingresa un puerto entre 1 y 65535.")

        except ValueError:
            print("Ingresa un número entero.")


def pedir_datos():
    ip = pedir_ip()
    inicial = pedir_puerto("Puerto inicial: ")
    final = pedir_puerto("Puerto final: ")

    while final < inicial:
        print("El puerto final no puede ser menor que el inicial.")
        final = pedir_puerto("Puerto final: ")

    return ip, inicial, final


def realizar_analisis(ip, inicial, final):
    abiertos = []
    analizados = 0
    total = final - inicial + 1
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    estado = "Completado"

    print("\n" + "-" * 60)
    print(f"Analizando {ip}")
    print(f"Rango: {inicial} - {final}")
    print("Presiona Ctrl + C para cancelar el análisis.")
    print("-" * 60, flush=True)

    try:
        # Incluye todos los puertos del rango solicitado.
        for puerto in range(inicial, final + 1):
            with socket.socket(
                socket.AF_INET, socket.SOCK_STREAM
            ) as conexion:
                conexion.settimeout(0.5)
                resultado = conexion.connect_ex((ip, puerto))

            # Un cero indica que se pudo establecer la conexión.
            if resultado == 0:
                abiertos.append(puerto)
                mensaje = "ABIERTO"
            else:
                mensaje = "SIN CONEXIÓN TCP"

            analizados += 1

            print(
                f"[{analizados}/{total}] Puerto {puerto}: {mensaje}",
                flush=True
            )

    except KeyboardInterrupt:
        estado = "Cancelado por el usuario"
        print("\nAnálisis cancelado.")

    except OSError as error:
        estado = "Detenido por un error de red o del sistema"
        print(f"\nError: {error}")

    # Conserva los resultados obtenidos antes de cancelar.
    print("\n" + "=" * 60)
    print("RESUMEN DEL ANÁLISIS".center(60))
    print("=" * 60)
    print(f"Estado             : {estado}")
    print(f"Fecha y hora       : {fecha}")
    print(f"Dirección IP       : {ip}")
    print(f"Rango solicitado   : {inicial} - {final}")
    print(f"Puertos analizados : {analizados}")
    print(f"Puertos pendientes : {total - analizados}")
    print(f"Puertos abiertos   : {len(abiertos)}")
    print(f"Sin conexión TCP   : {analizados - len(abiertos)}")
    print("-" * 60)

    if abiertos:
        print("Puertos abiertos encontrados:")

        for puerto in abiertos:
            print(f"  {puerto} - ABIERTO")
    else:
        print("NO SE DETECTARON PUERTOS ABIERTOS DURANTE EL ANALISIS")

    print("=" * 60, flush=True)


def menu_resultados():
    print("\n1. Analizar otra IP o rango")
    print("2. Repetir análisis con la misma IP y rango")
    print("3. Terminar el programa")

    while True:
        opcion = input("Selecciona: ").strip()

        if opcion in ("1", "2", "3"):
            return opcion

        print("Opción inválida. Ingresa 1, 2 o 3.")


def main():
    print("\n" + "=" * 60)
    print("TRABAJO PRÁCTICO EXPERIMENTAL 2 - GRUPO 5".center(60))
    print("ESCÁNER DE PUERTOS TCP".center(60))
    print("=" * 60)

    print("\n1. Iniciar análisis")
    print("2. Salir")

    while True:
        opcion = input("Selecciona: ").strip()

        if opcion == "2":
            print("\nPrograma finalizado.")
            return

        if opcion == "1":
            break

        print("Opción inválida. Ingresa 1 o 2.")

    ip, inicial, final = pedir_datos()

    while True:
        realizar_analisis(ip, inicial, final)
        opcion = menu_resultados()

        if opcion == "1":
            ip, inicial, final = pedir_datos()

        elif opcion == "2":
            # Repite el análisis completo con los datos anteriores.
            print(f"\nRepitiendo análisis de {ip}: {inicial} - {final}")

        else:
            print("\nPrograma finalizado.")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")