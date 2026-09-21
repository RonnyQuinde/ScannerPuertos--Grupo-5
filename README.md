# Escáner de puertos TCP en Python

**Trabajo Práctico Experimental 2 - Grupo 5**  
**Asignatura: Seguridad Informática**

## Descripción

Aplicación de consola desarrollada en Python que permite ingresar una dirección IPv4 y un rango de puertos para comprobar cuáles aceptan conexiones TCP.

Al finalizar, presenta un resumen y la lista de puertos abiertos. También permite cancelar el proceso y repetir el análisis sin reiniciar la aplicación.

## Funcionalidades

- Mostrar una IPv4 local detectada como referencia.
- Validar la dirección IP ingresada.
- Seleccionar y validar el rango de puertos.
- Mostrar el avance y el resultado de cada intento.
- Presentar un resumen de los resultados.
- Cancelar el análisis con Ctrl + C.
- Analizar otra IP o rango.
- Repetir el análisis con los mismos datos.

## Herramientas utilizadas

- **Python 3:** desarrollo y ejecución.
- **Visual Studio Code:** edición del código y uso de la terminal.
- **GitHub:** publicación del proyecto y su documentación.
- **socket:** conexiones de red.
- **ipaddress:** validación de direcciones IPv4.
- **datetime:** registro de fecha y hora.

Las bibliotecas utilizadas están incluidas en Python. No se requieren paquetes externos.

## Archivos del proyecto

| Archivo o carpeta | Contenido |
|---|---|
| `scanner_puertos.py` | Código principal del escáner. |
| `README.md` | Presentación general del proyecto. |
| `MANUAL_USO.md` | Instrucciones para preparar y utilizar la aplicación. |
| `capturas/` | Imágenes del funcionamiento del programa. |

## Ejecución

Descargar y extraer el proyecto. Abrir una terminal en la carpeta que contiene `scanner_puertos.py` y ejecutar:

```powershell
py scanner_puertos.py
```

Si la instalación utiliza el comando `python`, ejecutar:

```powershell
python scanner_puertos.py
```

Seleccionar **1. Iniciar análisis** e ingresar la IP y el rango de puertos.

Las instrucciones detalladas están en el [Manual de uso](MANUAL_USO.md).

## Prueba realizada

La prueba documentada se realizó el 21 de septiembre de 2026 sobre el equipo local.

| Elemento | Resultado |
|---|---|
| Dirección IP | 192.168.1.22 |
| Rango | 100–200 |
| Puertos analizados | 101 |
| Puertos pendientes | 0 |
| Puertos abiertos | 5 |
| Sin conexión TCP | 96 |
| Puertos abiertos detectados | 110, 119, 135, 139 y 143 |

![Resultados del análisis completado](capturas/05_resultados.png)

También se comprobó la cancelación con Ctrl + C en el rango 100–299. El programa mostró 8 puertos analizados y 192 pendientes, conservando el resumen parcial.

Los resultados corresponden a las pruebas realizadas y pueden variar en otros equipos o momentos.

## Alcance

El programa comprueba conexiones TCP sobre IPv4. No realiza análisis UDP ni identifica vulnerabilidades o aplicaciones asociadas a los puertos.

El mensaje **SIN CONEXIÓN TCP** indica que no se estableció la conexión durante el intento; no confirma por sí solo que el puerto esté cerrado.

La IP local detectada se muestra como referencia y puede variar según las interfaces de red activas.

## Uso responsable

Utilizar únicamente en equipos propios, máquinas virtuales o entornos autorizados.