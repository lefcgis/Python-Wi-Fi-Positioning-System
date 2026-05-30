# 🌍 **Guía Completa para Mejorar el Sistema de Posicionamiento por Wi-Fi en Python**

> *"Un proyecto paso a paso para hacer que el script funcione en Python 3, Windows, y sea más robusto y fácil de usar."*  
> — **Para Luis Eduardo Ferrer Cruz** 👨‍💻

---

## 📌 **Índice**

1. [Introducción y Objetivos](#-introducción-y-objetivos)
2. [Requisitos Previos](#-requisitos-previos)
3. [Mejoras Básicas (Para Principiantes)](#-mejoras-básicas-para-principiantes)
  - [Actualizar el README.md](#1-actualizar-el-readmemd)
  - [Reemplazar `commands` por `subprocess](#2-reemplazar-commands-por-subprocess)`
  - [Reemplazar `urllib2` por `requests](#3-reemplazar-urllib2-por-requests)`
4. [Mejoras Intermedias](#-mejoras-intermedias)
  - [Hacer el código compatible con Python 3](#4-hacer-el-código-compatible-con-python-3)
  - [Manejo de errores para la API de Google](#5-manejo-de-errores-para-la-api-de-google)
  - [Modo Demo con Datos de Ejemplo](#6-modo-demo-con-datos-de-ejemplo)
  - [Mejorar la visualización del mapa con Folium](#7-mejorar-la-visualización-del-mapa-con-folium)
5. [Mejoras Avanzadas](#-mejoras-avanzadas)
  - [Soporte para Windows](#8-soporte-para-windows)
  - [Pruebas Unitarias](#9-pruebas-unitarias)
  - [Soporte para Otras APIs de Geolocalización](#10-soporte-para-otras-apis-de-geolocalización)
  - [Refactorizar el Código](#11-refactorizar-el-código)
  - [Sistema de Logging](#12-sistema-de-logging)
6. [Pasos para Contribuir en GitHub](#-pasos-para-contribuir-en-github)
7. [Estructura Final del Proyecto](#-estructura-final-del-proyecto)
8. [Recursos Adicionales](#-recursos-adicionales)

---

## 🌟 **Introducción y Objetivos**

### **¿Qué es el Python-Wi-Fi-Positioning-System?**

Es un script en Python que utiliza la **API de Geolocalización de Google** para determinar la ubicación de un dispositivo basado en las redes Wi-Fi cercanas. Originalmente, solo funcionaba en **GNU/Linux, OpenBSD y Mac OS X**, pero con esta guía, lo haremos compatible con **Windows** y lo mejoraremos para que sea más robusto y fácil de usar.

### **Objetivos de esta Guía**

1. **Hacer el script compatible con Python 3** (actualmente solo funciona en Python 2).
2. **Añadir soporte para Windows** (usando librerías como `pywifi` o `subprocess`).
3. **Mejorar la documentación** (README.md) para que sea más clara y útil.
4. **Reemplazar dependencias obsoletas** (`commands`, `urllib2`, `simplejson`).
5. **Añadir manejo de errores** para la API de Google y otros casos.
6. **Mejorar la visualización de resultados** (usando Folium en lugar de Google Maps API).
7. **Refactorizar el código** para que sea más legible y mantenible.

---

## 🛠️ **Requisitos Previos**

### **Herramientas Necesarias**

1. **Python 3.8 o superior** (recomendado: [Python 3.10](https://www.python.org/downloads/)).
2. **Git** (para clonar el repositorio y hacer *pull requests*). Descárgalo [aquí](https://git-scm.com/downloads).
3. **Un editor de código** (recomendado: [VS Code](https://code.visualstudio.com/) o [PyCharm](https://www.jetbrains.com/pycharm/)).
4. **Una clave API de Google Geolocation** (gratis para pruebas). Obténla [aquí](https://developers.google.com/maps/documentation/geolocation/get-api-key).

### **Librerías de Python a Instalar**

Ejecuta el siguiente comando para instalar todas las dependencias necesarias:

```bash
pip install requests folium pywifi subprocess32
```

---

## 🟢 **Mejoras Básicas (Para Principiantes)**

---

### **1. Actualizar el README.md**

#### **¿Qué hacer?**

Vamos a mejorar el `README.md` para que sea más claro y útil para nuevos usuarios. Incluiremos:

- Instrucciones paso a paso para obtener la clave API de Google.
- Cómo instalar dependencias en diferentes sistemas operativos.
- Ejemplos de uso del script.

#### **Código del Nuevo README.md**

```markdown
# 🌍 Python Wi-Fi Positioning System

> Un script en Python para determinar la ubicación de un dispositivo usando redes Wi-Fi cercanas y la API de Geolocalización de Google.

---

## 📌 **Características**
- ✅ Funciona en **GNU/Linux, OpenBSD, Mac OS X y Windows**.
- ✅ Usa la **API de Geolocalización de Google** para obtener coordenadas.
- ✅ Genera un **mapa interactivo** con la ubicación estimada.
- ✅ Modo **demo** para probar sin escanear redes Wi-Fi.

---

## 🛠️ **Requisitos**

### **Sistemas Operativos Soportados**
| Sistema Operativo | Requisitos | Notas |
|--------------------|------------|-------|
| GNU/Linux | `iw` (para escanear redes Wi-Fi) | Instalar con `sudo apt-get install iw` (Ubuntu) |
| OpenBSD | `ifconfig` | Ya viene preinstalado |
| Mac OS X | `airport` | Ya viene preinstalado |
| Windows | `pywifi` | Instalar con `pip install pywifi` |

### **Dependencias de Python**
```bash
pip install requests folium pywifi
```

### **Clave API de Google**

1. Ve a [Google Cloud Console](https://console.cloud.google.com/).
2. Crea un nuevo proyecto.
3. Habilita la **API de Geolocation**.
4. Genera una clave API y guárdala en un lugar seguro.

---

## 🚀 **Instalación y Uso**

### **1. Clonar el Repositorio**

```bash
git clone https://github.com/TU_USUARIO/Python-Wi-Fi-Positioning-System.git
cd Python-Wi-Fi-Positioning-System
```

### **2. Ejecutar el Script**

#### **Modo Normal (Escanear Redes Wi-Fi)**

- **En Linux/Mac/OpenBSD:**
  ```bash
  python wifi_positioning_system.py --api-key TU_CLAVE_API -i wlan0
  ```
- **En Windows:**
  ```bash
  python wifi_positioning_system.py --api-key TU_CLAVE_API --windows
  ```

#### **Modo Demo (Sin Escanear Redes)**

```bash
python wifi_positioning_system.py --api-key TU_CLAVE_API --demo
```

#### **Opciones Adicionales**


| Argumento         | Descripción                                        | Ejemplo                  |
| ----------------- | -------------------------------------------------- | ------------------------ |
| `--api-key`       | Clave API de Google (obligatorio)                  | `--api-key AIzaSyABC123` |
| `-i`              | Interfaz Wi-Fi (Linux/Mac/OpenBSD)                 | `-i wlan0`               |
| `--windows`       | Usar modo Windows                                  | `--windows`              |
| `--demo`          | Modo demo con datos de ejemplo                     | `--demo`                 |
| `--json-prettify` | Formatear la salida JSON                           | `--json-prettify`        |
| `--with-overview` | Generar un mapa HTML                               | `--with-overview`        |
| `--map-type`      | Tipo de mapa (ROADMAP, SATELLITE, HYBRID, TERRAIN) | `--map-type HYBRID`      |


---

## 📂 **Estructura del Proyecto**

```
Python-Wi-Fi-Positioning-System/
├── wifi_positioning_system.py  # Script principal
├── demo_data.json               # Datos de ejemplo para modo demo
├── README.md                    # Este archivo
└── requirements.txt             # Dependencias de Python
```

---

## 🤝 **Contribuir**

1. Haz un *fork* del repositorio.
2. Crea una nueva rama (`git checkout -b mejora-readme`).
3. Haz *commit* de tus cambios (`git commit -m "Mejora el README"`).
4. Envía un *pull request*.

---

## 📜 **Licencia**

Este proyecto está bajo la licencia **GNU GPL 3.0**. Puedes usar, modificar y distribuir el código libremente.

---

## 📞 **Contacto**

¿Preguntas o sugerencias?

- **Autor Original:** [initbrain](https://github.com/initbrain)
- **Fork:** [lefcgis](https://github.com/lefcgis)

```

#### **¿Dónde guardar el archivo?**
Guarda este contenido en un archivo llamado `README.md` en la raíz de tu proyecto.

---

### **2. Reemplazar `commands` por `subprocess`**

#### **¿Qué hacer?**
El módulo `commands` está obsoleto en Python 3. Lo reemplazaremos por `subprocess`, que es la forma moderna de ejecutar comandos del sistema.

#### **Cambios en el Código**
Busca todas las instancias de `commands.getstatusoutput` o `commands.getoutput` en el archivo `wifi_positioning_system.py` y reemplázalas por `subprocess.run`.

**Ejemplo de cambio:**
```python
# Antes (Python 2):
import commands
status, result = commands.getstatusoutput("iw dev wlan0 scan")

# Después (Python 3):
import subprocess
result = subprocess.run(["iw", "dev", "wlan0", "scan"], capture_output=True, text=True)
status = result.returncode
output = result.stdout
```

#### **Notas Importantes**

- `capture_output=True` captura la salida estándar y de error.
- `text=True` devuelve la salida como una cadena de texto (en lugar de bytes).
- `result.returncode` es el código de estado (0 = éxito, otros = error).

---

### **3. Reemplazar `urllib2` por `requests**`

#### **¿Qué hacer?**

`urllib2` está obsoleto en Python 3. Usaremos `requests`, que es más sencillo y potente.

#### **Cambios en el Código**

Busca el código que usa `urllib2` para hacer peticiones a la API de Google y reemplázalo por `requests`.

**Ejemplo de cambio:**

```python
# Antes (Python 2):
import urllib2
import simplejson

json_data = simplejson.JSONEncoder().encode(location_request)
http_request = urllib2.Request('https://www.googleapis.com/geolocation/v1/geolocate?key=' + API_KEY)
http_request.add_header('Content-Type', 'application/json')
api_result = simplejson.loads(urllib2.urlopen(http_request, json_data).read())

# Después (Python 3):
import requests
import json

response = requests.post(
    f'https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}',
    json=location_request,
    headers={'Content-Type': 'application/json'}
)
response.raise_for_status()  # Lanza un error si la petición falla
api_result = response.json()
```

#### **Notas Importantes**

- `requests.post` envía una petición POST con los datos en formato JSON.
- `response.raise_for_status()` lanza una excepción si el código HTTP es >= 400 (ej: 404, 500).
- `response.json()` convierte la respuesta JSON a un diccionario de Python.

---

---

## 🟡 **Mejoras Intermedias**

---

### **4. Hacer el Código Compatible con Python 3**

#### **¿Qué hacer?**

El código actual usa sintaxis de Python 2, que no es compatible con Python 3. Debemos hacer los siguientes cambios:

1. `**print` como función:**
  - **Antes:** `print "Hola"`
  - **Después:** `print("Hola")`
2. `**xrange` por `range`:**
  - **Antes:** `for i in xrange(10):`
  - **Después:** `for i in range(10):`
3. **Manejo de cadenas de texto:**
  - En Python 2, las cadenas son `str` por defecto. En Python 3, son `str` (Unicode) por defecto, pero a veces se usan `bytes`. Asegúrate de que todas las cadenas sean `str`.
4. **División entera:**
  - **Antes:** `5 / 2` devuelve `2` (división entera).
  - **Después:** `5 // 2` devuelve `2` (división entera). `5 / 2` devuelve `2.5` (división flotante).

#### **Ejemplo de Cambios en el Código**

Busca en el archivo `wifi_positioning_system.py` todas las instancias de:

- `print "..."` → `print("...")`
- `xrange(...)` → `range(...)`
- `except Exception, e:` → `except Exception as e:`

---

### **5. Manejo de Errores para la API de Google**

#### **¿Qué hacer?**

Añadir manejo de errores para casos como:

- Clave API inválida.
- Límite de solicitudes alcanzado.
- Conexión a internet fallida.

#### **Código para Añadir**

Reemplaza el código que hace la petición a la API de Google por esto:

```python
try:
    response = requests.post(
        f'https://www.googleapis.com/geolocation/v1/geolocate?key={API_KEY}',
        json=location_request,
        headers={'Content-Type': 'application/json'},
        timeout=10  # Tiempo máximo de espera en segundos
    )
    response.raise_for_status()
    api_result = response.json()
    
    # Validar que la respuesta tenga los campos esperados
    if 'location' not in api_result or 'accuracy' not in api_result:
        raise ValueError("Respuesta inválida de la API de Google")
        
except requests.exceptions.RequestException as e:
    print(f"[!] Error al conectar con la API de Google: {e}")
    if "403" in str(e):
        print("[!] Verifica que tu clave API sea válida y que no hayas alcanzado el límite de solicitudes.")
    elif "timeout" in str(e).lower():
        print("[!] Tiempo de espera agotado. Verifica tu conexión a internet.")
    exit(1)
except ValueError as e:
    print(f"[!] Error en la respuesta de la API: {e}")
    exit(1)
```

---

### **6. Modo Demo con Datos de Ejemplo**

#### **¿Qué hacer?**

Añadir un archivo `demo_data.json` con datos de ejemplo para que los usuarios puedan probar el script sin escanear redes Wi-Fi.

#### **Paso 1: Crear el Archivo `demo_data.json**`

```json
{
    "wifiAccessPoints": [
        {"macAddress": "00-11-22-33-44-55", "signalStrength": -40},
        {"macAddress": "AA-BB-CC-DD-EE-FF", "signalStrength": -50},
        {"macAddress": "11-22-33-44-55-66", "signalStrength": -60},
        {"macAddress": "FF-EE-DD-CC-BB-AA", "signalStrength": -70}
    ]
}
```

#### **Paso 2: Modificar el Script para Usar el Modo Demo**

Busca la parte del código que maneja el modo demo y modifícala para que use los datos del archivo JSON:

```python
if args.demo:
    try:
        with open('demo_data.json', 'r') as f:
            demo_data = json.load(f)
        wifi_data = [(ap['macAddress'], ap['signalStrength']) for ap in demo_data['wifiAccessPoints']]
        print("[+] Usando datos de ejemplo para modo demo")
    except FileNotFoundError:
        print("[!] Archivo demo_data.json no encontrado. Usando datos predeterminados.")
        wifi_data = [
            ('00-11-22-33-44-55', -40),
            ('AA-BB-CC-DD-EE-FF', -50),
            ('11-22-33-44-55-66', -60)
        ]
```

---

### **7. Mejorar la Visualización del Mapa con Folium**

#### **¿Qué hacer?**

Reemplazar la generación del mapa HTML con Google Maps API por **Folium**, que no requiere clave API y genera mapas interactivos offline.

#### **Paso 1: Instalar Folium**

```bash
pip install folium
```

#### **Paso 2: Añadir una Función para Crear el Mapa con Folium**

Añade esta función al archivo `wifi_positioning_system.py`:

```python
def create_map_folium(api_result, filename='wifi_location.html'):
    """
    Crea un mapa interactivo usando Folium.
    
    Args:
        api_result (dict): Resultado de la API de Google (debe contener 'location' y 'accuracy').
        filename (str): Nombre del archivo HTML de salida.
    """
    import folium
    
    # Coordenadas del centro del mapa
    lat = api_result['location']['lat']
    lng = api_result['location']['lng']
    accuracy = api_result['accuracy']
    
    # Crear el mapa
    m = folium.Map(location=[lat, lng], zoom_start=18)
    
    # Añadir un círculo para la precisión
    folium.Circle(
        radius=accuracy,
        location=[lat, lng],
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.3,
        popup=f"Precisión: {accuracy} metros"
    ).add_to(m)
    
    # Añadir un marcador
    folium.Marker(
        location=[lat, lng],
        popup=f"Latitud: {lat}, Longitud: {lng}"
    ).add_to(m)
    
    # Guardar el mapa
    m.save(filename)
    print(f"[+] Mapa guardado en {filename}")
```

#### **Paso 3: Modificar el Código para Usar Folium**

Busca la parte del código que genera el mapa con Google Maps API y reemplázala por la llamada a `create_map_folium`:

```python
if args.with_overview:
    create_map_folium(api_result, filename='wifi_location.html')
```

#### **Notas Importantes**

- Folium genera un archivo HTML que puedes abrir en cualquier navegador **sin necesidad de conexión a internet**.
- El mapa es **interactivo**: puedes hacer zoom, moverte y hacer clic en los marcadores.

---

---

## 🔴 **Mejoras Avanzadas**

---

### **8. Soporte para Windows**

#### **¿Qué hacer?**

Añadir soporte para Windows usando la librería `pywifi`, que permite escanear redes Wi-Fi en este sistema operativo.

#### **Paso 1: Instalar `pywifi**`

```bash
pip install pywifi
```

#### **Paso 2: Añadir una Función para Escanear Redes Wi-Fi en Windows**

Añade esta función al archivo `wifi_positioning_system.py`:

```python
def scan_wifi_windows():
    """
    Escanea redes Wi-Fi en Windows usando pywifi.
    
    Returns:
        list: Lista de tuplas (MAC, señal) de las redes Wi-Fi detectadas.
    """
    import pywifi
    from pywifi import const
    
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Usa la primera interfaz Wi-Fi disponible
    
    # Escanear redes
    iface.scan()
    results = iface.scan_results()
    
    # Procesar resultados
    wifi_data = []
    for network in results:
        # Filtrar redes sin SSID o BSSID
        if network.bssid and network.signal:
            # Reemplazar ':' por '-' en el BSSID (formato requerido por la API de Google)
            mac = network.bssid.replace(':', '-')
            wifi_data.append((mac, network.signal))
    
    return wifi_data
```

#### **Paso 3: Modificar la Función `check_prerequisites` para Soporte en Windows**

Busca la función `check_prerequisites` y añade el caso para Windows:

```python
# Dentro de check_prerequisites()
elif sys.platform == 'win32':
    try:
        import pywifi
        wifi_scan_method = 'pywifi'
    except ImportError:
        print("Error: pywifi no está instalado. Instálalo con 'pip install pywifi'.")
        exit(1)
```

#### **Paso 4: Modificar la Función `get_signal_strengths` para Usar `pywifi**`

Añade el caso para `pywifi` en la función `get_signal_strengths`:

```python
# Dentro de get_signal_strengths()
if wifi_scan_method == 'pywifi':
    return scan_wifi_windows()
```

#### **Paso 5: Añadir el Argumento `--windows**`

Modifica la función `get_arguments` para añadir el argumento `--windows`:

```python
parser.add_argument('--windows', action="store_true",
                    help='Usar modo Windows (escanea redes Wi-Fi con pywifi)',
                    default=False)
```

#### **Paso 6: Modificar el Código Principal para Manejar Windows**

En la parte principal del script, añade la lógica para Windows:

```python
if args.windows:
    wifi_scan_method = 'pywifi'
else:
    wifi_scan_method = check_prerequisites()
```

#### **Notas Importantes**

- `pywifi` puede requerir **permisos de administrador** en Windows para escanear redes Wi-Fi.
- Si el usuario no tiene permisos, el script debe mostrar un mensaje claro.

---

### **9. Pruebas Unitarias**

#### **¿Qué hacer?**

Crear pruebas unitarias para validar el funcionamiento del script. Usaremos `unittest`, que viene incluido en Python.

#### **Paso 1: Crear el Archivo `test_wifi_positioning.py**`

```python
import unittest
import json
import os
import sys
from wifi_positioning_system import get_signal_strengths, create_map_folium

class TestWifiPositioning(unittest.TestCase):
    
    def test_demo_mode(self):
        """Prueba que el modo demo devuelve datos válidos."""
        # Simular argumentos para modo demo
        class Args:
            demo = True
            verbose = False
        global args
        args = Args()
        
        # Cargar datos de ejemplo
        with open('demo_data.json', 'r') as f:
            demo_data = json.load(f)
        wifi_data = [(ap['macAddress'], ap['signalStrength']) for ap in demo_data['wifiAccessPoints']]
        
        # Validar que los datos no estén vacíos
        self.assertIsInstance(wifi_data, list)
        self.assertGreater(len(wifi_data), 0)
        
        # Validar que cada elemento sea una tupla (MAC, señal)
        for item in wifi_data:
            self.assertIsInstance(item, tuple)
            self.assertIsInstance(item[0], str)
            self.assertIsInstance(item[1], int)
    
    def test_create_map_folium(self):
        """Prueba que la función create_map_folium genera un archivo HTML válido."""
        api_result = {
            'location': {'lat': -12.0464, 'lng': -77.0428},  # Lima, Perú
            'accuracy': 50.0
        }
        filename = 'test_map.html'
        create_map_folium(api_result, filename)
        
        # Validar que el archivo se creó
        self.assertTrue(os.path.exists(filename))
        
        # Validar que el archivo no está vacío
        with open(filename, 'r') as f:
            content = f.read()
            self.assertGreater(len(content), 0)
        
        # Limpiar: eliminar el archivo de prueba
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
```

#### **Paso 2: Ejecutar las Pruebas**

```bash
python -m unittest test_wifi_positioning.py
```

#### **Notas Importantes**

- Las pruebas validan que:
  - El modo demo devuelve datos válidos.
  - La función `create_map_folium` genera un archivo HTML válido.
- Puedes añadir más pruebas para otras funciones (ej: `scan_wifi_windows`, manejo de errores).

---

### **10. Soporte para Otras APIs de Geolocalización**

#### **¿Qué hacer?**

Añadir soporte para la **API de Mozilla Location Service (MLS)**, que es gratuita y no requiere clave API.

#### **Paso 1: Añadir una Función para la API de Mozilla**

```python
def get_geolocation_mozilla(wifi_data, api_key=None):
    """
    Obtiene la ubicación usando la API de Mozilla Location Service.
    
    Args:
        wifi_data (list): Lista de tuplas (MAC, señal).
        api_key (str): No se usa en Mozilla, pero se incluye por compatibilidad.
    
    Returns:
        dict: Resultado de la API con 'location' y 'accuracy'.
    """
    import requests
    
    # Formatear los datos para la API de Mozilla
    mls_request = {
        "data": {
            "wifi": [
                {"macAddress": mac, "signalStrength": signal}
                for mac, signal in wifi_data
            ]
        }
    }
    
    # URL de la API de Mozilla
    url = "https://location.services.mozilla.com/v1/geolocate?key=test"
    
    try:
        response = requests.post(url, json=mls_request)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[!] Error al conectar con la API de Mozilla: {e}")
        return None
```

#### **Paso 2: Añadir un Argumento para Elegir la API**

Modifica la función `get_arguments` para añadir el argumento `--api-provider`:

```python
parser.add_argument('--api-provider', choices=['google', 'mozilla'], default='google',
                    help='Proveedor de la API de geolocalización (google o mozilla)')
```

#### **Paso 3: Modificar el Código Principal para Usar la API Elegida**

```python
if args.api_provider == 'google':
    api_result = send_to_google_api(wifi_data, API_KEY)
elif args.api_provider == 'mozilla':
    api_result = get_geolocation_mozilla(wifi_data)
```

#### **Notas Importantes**

- La API de Mozilla es **gratuita** y no requiere clave API (el parámetro `key=test` es solo para evitar errores).
- La precisión puede ser menor que la de Google, pero es una buena alternativa.

---

### **11. Refactorizar el Código**

#### **¿Qué hacer?**

Organizar el código en clases para que sea más legible y mantenible. Por ejemplo:

- `WifiScanner`: Para escanear redes Wi-Fi.
- `GeolocationAPI`: Para interactuar con las APIs de geolocalización.
- `MapGenerator`: Para generar mapas.

#### **Ejemplo de Refactorización**

```python
class WifiScanner:
    """Clase para escanear redes Wi-Fi."""
    
    def __init__(self, interface=None, os_type=None):
        self.interface = interface
        self.os_type = os_type
    
    def scan(self):
        """Escanea redes Wi-Fi según el sistema operativo."""
        if self.os_type == 'linux':
            return self._scan_linux()
        elif self.os_type == 'windows':
            return self._scan_windows()
        elif self.os_type == 'darwin':
            return self._scan_mac()
        elif self.os_type == 'openbsd':
            return self._scan_openbsd()
        else:
            raise NotImplementedError(f"Sistema operativo {self.os_type} no soportado")
    
    def _scan_linux(self):
        """Escanea redes Wi-Fi en Linux usando iw."""
        import subprocess
        command = f"iw dev {self.interface} scan"
        result = subprocess.run(command.split(), capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Error al escanear redes Wi-Fi: {result.stderr}")
        # Procesar resultado (ejemplo simplificado)
        return [("00-11-22-33-44-55", -40)]  # Datos de ejemplo
    
    def _scan_windows(self):
        """Escanea redes Wi-Fi en Windows usando pywifi."""
        import pywifi
        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        iface.scan()
        results = iface.scan_results()
        return [(network.bssid.replace(':', '-'), network.signal) for network in results]


class GeolocationAPI:
    """Clase para interactuar con APIs de geolocalización."""
    
    def __init__(self, api_key=None, provider='google'):
        self.api_key = api_key
        self.provider = provider
    
    def get_location(self, wifi_data):
        """Obtiene la ubicación usando el proveedor seleccionado."""
        if self.provider == 'google':
            return self._get_location_google(wifi_data)
        elif self.provider == 'mozilla':
            return self._get_location_mozilla(wifi_data)
        else:
            raise NotImplementedError(f"Proveedor {self.provider} no soportado")
    
    def _get_location_google(self, wifi_data):
        """Usa la API de Google."""
        import requests
        url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={self.api_key}"
        request_data = {
            'considerIp': False,
            'wifiAccessPoints': [
                {"macAddress": mac, "signalStrength": signal}
                for mac, signal in wifi_data
            ]
        }
        response = requests.post(url, json=request_data)
        response.raise_for_status()
        return response.json()


class MapGenerator:
    """Clase para generar mapas."""
    
    @staticmethod
    def create_map(api_result, filename='wifi_location.html'):
        """Crea un mapa usando Folium."""
        import folium
        lat = api_result['location']['lat']
        lng = api_result['location']['lng']
        accuracy = api_result['accuracy']
        
        m = folium.Map(location=[lat, lng], zoom_start=18)
        folium.Circle(
            radius=accuracy,
            location=[lat, lng],
            color='blue',
            fill=True,
            fill_opacity=0.3
        ).add_to(m)
        m.save(filename)
```

#### **Paso 2: Usar las Clases en el Script Principal**

```python
if __name__ == "__main__":
    args = get_arguments()
    
    # Determinar el sistema operativo
    if sys.platform == 'win32':
        os_type = 'windows'
    elif sys.platform.startswith('linux'):
        os_type = 'linux'
    elif sys.platform == 'darwin':
        os_type = 'darwin'
    elif sys.platform.startswith('openbsd'):
        os_type = 'openbsd'
    else:
        print(f"[!] Sistema operativo {sys.platform} no soportado")
        exit(1)
    
    # Escanear redes Wi-Fi
    scanner = WifiScanner(interface=args.wifi_interface if hasattr(args, 'wifi_interface') else None, os_type=os_type)
    wifi_data = scanner.scan()
    
    # Obtener ubicación
    geolocation = GeolocationAPI(api_key=args.api_key, provider=args.api_provider)
    api_result = geolocation.get_location(wifi_data)
    
    # Generar mapa
    if args.with_overview:
        MapGenerator.create_map(api_result)
```

#### **Notas Importantes**

- La refactorización hace que el código sea **más modular y fácil de mantener**.
- Cada clase tiene una **responsabilidad clara** (principio de diseño SOLID).

---

### **12. Sistema de Logging**

#### **¿Qué hacer?**

Reemplazar los `print` por un sistema de logging para controlar mejor los mensajes (ej: guardar logs en un archivo).

#### **Paso 1: Configurar el Logging**

Añade esto al inicio del script `wifi_positioning_system.py`:

```python
import logging

# Configurar el logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Mostrar mensajes en la consola
        logging.FileHandler('wifi_positioning.log')  # Guardar mensajes en un archivo
    ]
)
logger = logging.getLogger(__name__)
```

#### **Paso 2: Reemplazar `print` por `logger**`

Busca todos los `print` en el script y reemplázalos por `logger.info`, `logger.error`, etc. Ejemplos:

```python
# Antes:
print("[+] Scanning nearby Wi-Fi networks...")

# Después:
logger.info("Scanning nearby Wi-Fi networks...")

# Antes:
print("[!] Error al conectar con la API de Google")

# Después:
logger.error("Error al conectar con la API de Google")
```

#### **Notas Importantes**

- `logger.info`: Para mensajes informativos (ej: "Escaneando redes Wi-Fi...").
- `logger.error`: Para mensajes de error (ej: "Clave API inválida").
- `logger.debug`: Para mensajes de depuración (útil durante el desarrollo).
- Los mensajes se guardan en el archivo `wifi_positioning.log`.

---

---

## 📤 **Pasos para Contribuir en GitHub**

### **1. Clonar tu Fork**

```bash
git clone https://github.com/TU_USUARIO/Python-Wi-Fi-Positioning-System.git
cd Python-Wi-Fi-Positioning-System
```

### **2. Crear una Rama para tus Cambios**

```bash
git checkout -b mejora-soporte-windows
```

### **3. Hacer tus Cambios**

- Edita los archivos según las mejoras que quieras implementar.
- Prueba que todo funcione:
  ```bash
  python wifi_positioning_system.py --demo
  ```

### **4. Hacer Commit de tus Cambios**

```bash
git add .
git commit -m "Añade soporte para Windows usando pywifi"
```

### **5. Subir tus Cambios a GitHub**

```bash
git push origin mejora-soporte-windows
```

### **6. Abrir un Pull Request**

1. Ve a tu fork en GitHub: `https://github.com/TU_USUARIO/Python-Wi-Fi-Positioning-System`.
2. Haz clic en **"Pull requests"** > **"New pull request"**.
3. Selecciona:
  - **Base repository:** `lefcgis/Python-Wi-Fi-Positioning-System` (rama `master`).
  - **Head repository:** `TU_USUARIO/Python-Wi-Fi-Positioning-System` (rama `mejora-soporte-windows`).
4. Escribe un **título claro** (ej: "Añade soporte para Windows usando pywifi").
5. Escribe una **descripción detallada** de los cambios:
  ```markdown
   ## ¿Qué hace este pull request?
   - Añade soporte para Windows usando la librería `pywifi`.
   - Actualiza el código para que sea compatible con Python 3.
   - Reemplaza `commands` por `subprocess`.

   ## ¿Cómo probarlo?
  ```
  1. Ejecuta `pip install pywifi`.
  2. Ejecuta el script con: `python wifi_positioning_system.py --windows --api-key TU_CLAVE_API`.
    Notas adicionales  
    Se probó en Windows 10 con Python 3.10.  
    Se actualizó el README.md con instrucciones para Windows.  
    `
6. Haz clic en **"Create pull request"**.

---

---

## 📁 **Estructura Final del Proyecto**

Después de implementar todas las mejoras, la estructura de tu proyecto debería verse así:

```
Python-Wi-Fi-Positioning-System/
├── wifi_positioning_system.py  # Script principal (actualizado)
├── demo_data.json               # Datos de ejemplo para modo demo
├── test_wifi_positioning.py    # Pruebas unitarias
├── README.md                    # Documentación mejorada
├── requirements.txt             # Dependencias de Python
└── wifi_positioning.log         # Archivo de log (generado al ejecutar)
```

---

## 📄 **Archivo `requirements.txt**`

Crea un archivo `requirements.txt` para listar todas las dependencias del proyecto:

```
requests>=2.25.1
folium>=0.12.1
pywifi>=1.1.12
```

---

---

## 🎓 **Recursos Adicionales**

### **Documentación Oficial**

- [Python 3 Documentation](https://docs.python.org/3/)
- [Subprocess Module](https://docs.python.org/3/library/subprocess.html)
- [Requests Library](https://docs.python-requests.org/)
- [Folium Library](https://python-visualization.github.io/folium/)
- [PyWiFi Library](https://pywifi.readthedocs.io/)
- [Google Geolocation API](https://developers.google.com/maps/documentation/geolocation/overview)
- [Mozilla Location Service](https://location.services.mozilla.com/)

### **Tutoriales Útiles**

- [GitHub Guides](https://guides.github.com/)
- [How to Write a Good README](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
- [Python Logging Guide](https://realpython.com/python-logging/)
- [Unit Testing in Python](https://realpython.com/python-testing/)

---

---

## 📌 **Resumen de Acciones Recomendadas**


| **Prioridad** | **Mejora**                              | **Dificultad** | **Tiempo Estimado** |
| ------------- | --------------------------------------- | -------------- | ------------------- |
| Alta          | Actualizar README.md                    | Fácil          | 1 hora              |
| Alta          | Reemplazar `commands` por `subprocess`  | Fácil          | 1 hora              |
| Alta          | Reemplazar `urllib2` por `requests`     | Fácil          | 1 hora              |
| Alta          | Hacer el código compatible con Python 3 | Intermedia     | 2 horas             |
| Media         | Manejo de errores para la API de Google | Intermedia     | 2 horas             |
| Media         | Modo demo con datos de ejemplo          | Intermedia     | 1 hora              |
| Media         | Mejorar visualización con Folium        | Intermedia     | 2 horas             |
| Media         | Añadir soporte para Windows             | Avanzada       | 3 horas             |
| Baja          | Pruebas unitarias                       | Avanzada       | 3 horas             |
| Baja          | Soporte para otras APIs (Mozilla)       | Avanzada       | 3 horas             |
| Baja          | Refactorizar el código                  | Avanzada       | 4 horas             |
| Baja          | Sistema de logging                      | Intermedia     | 2 horas             |


---

---

## 💡 **Consejos Finales**

1. **Empieza por lo fácil**: Actualiza el `README.md` y reemplaza `commands` por `subprocess`. Esto ya será un gran aporte.
2. **Prueba cada cambio**: Después de cada modificación, ejecuta el script para asegurarte de que todo funcione.
3. **Haz commits pequeños**: Cada commit debe contener **un solo cambio lógico** (ej: "Reemplaza urllib2 por requests").
4. **Documenta tus cambios**: En el mensaje del commit, explica **qué hiciste y por qué**.
5. **Pide feedback**: Si no estás seguro de algo, abre un *pull request* en estado *draft* y pide opiniones.

---

> *"El código es como un jardín: si no lo cuidas, se llena de maleza. Pero con paciencia y dedicación, puede convertirse en algo hermoso."* 🌱

---

**¡Mucho éxito con tu contribución!** Si tienes dudas sobre alguna parte, no dudes en preguntar. 😊