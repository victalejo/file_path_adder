# File Path Adder - Documentación
## Índice
1. [Descripción General](#descripción-general)
2. [Requisitos del Sistema](#requisitos-del-sistema)
3. [Instalación](#instalación)
4. [Guía de Usuario](#guía-de-usuario)
5. [Características Técnicas](#características-técnicas)
6. [Solución de Problemas](#solución-de-problemas)
7. [Preguntas Frecuentes](#preguntas-frecuentes)

## Descripción General
File Path Adder es una aplicación de escritorio desarrollada en Python que permite agregar automáticamente la ruta relativa al inicio de archivos de código y texto. Esta herramienta es especialmente útil para proyectos que requieren mantener un registro de la ubicación de los archivos dentro de su estructura de directorios.

### Principales Características
- Interfaz gráfica intuitiva
- Procesamiento por lotes de archivos
- Soporte para múltiples tipos de archivo
- Exclusión configurable de directorios
- Sistema de registro en tiempo real
- Manejo de diferentes codificaciones de archivo

## Requisitos del Sistema
- Python 3.6 o superior
- Tkinter (incluido en la mayoría de las instalaciones de Python)
- Sistema operativo: Windows, macOS o Linux
- Espacio en disco: 10MB mínimo
- RAM: 256MB mínimo

## Instalación
1. Descarga el archivo `file_path_adder.py`
2. Asegúrate de tener Python 3.6 o superior instalado
3. Ejecuta el programa usando:
```bash
python file_path_adder.py
```

## Guía de Usuario

### Interfaz Principal
La interfaz se divide en cuatro secciones principales:

1. **Selección de Directorio**
   - Muestra la ruta actual del directorio de trabajo
   - Botón "Examinar" para seleccionar un nuevo directorio

2. **Directorios Excluidos**
   - Lista de directorios que serán ignorados durante el procesamiento
   - Botones para agregar y eliminar directorios de la lista

3. **Extensiones de Archivo**
   - Lista de extensiones de archivo que serán procesadas
   - Botones para agregar y eliminar extensiones

4. **Log de Operaciones**
   - Muestra el progreso en tiempo real del procesamiento
   - Registra errores y éxitos

### Uso Básico
1. Inicia el programa
2. Selecciona el directorio a procesar usando el botón "Examinar"
3. (Opcional) Modifica la lista de directorios excluidos
4. (Opcional) Modifica la lista de extensiones de archivo
5. Haz clic en "Procesar Archivos"
6. Espera a que el proceso termine
7. Revisa el log para verificar los resultados

### Personalización de Directorios Excluidos
- Clic en "Agregar" para incluir un nuevo directorio a excluir
- Selecciona un directorio de la lista y haz clic en "Eliminar" para removerlo
- Por defecto se excluyen: lib, vendor, tmp, .git

### Gestión de Extensiones
- Clic en "Agregar" para incluir una nueva extensión
- Ingresa la extensión con el punto (ejemplo: .php)
- Selecciona una extensión de la lista y haz clic en "Eliminar" para removerla

## Características Técnicas

### Formato de Comentarios por Tipo de Archivo
- PHP: `///ruta/al/archivo.php`
- HTML: `<!-- ruta/al/archivo.html -->`
- JS/CSS: `/* ruta/al/archivo.js */`
- Otros: `# ruta/al/archivo.txt`

### Manejo de Codificación
El programa intenta primero UTF-8 y si falla, usa Latin-1 como fallback.

### Procesamiento de Archivos
1. Crea un archivo temporal
2. Agrega la ruta como comentario
3. Copia el contenido original
4. Reemplaza el archivo original
5. Maneja errores y excepciones

## Solución de Problemas

### Errores Comunes y Soluciones

1. **Error: "El directorio seleccionado no existe"**
   - Verifica que el directorio exista y tengas permisos de acceso
   - Intenta seleccionar el directorio nuevamente usando el botón "Examinar"

2. **Error: "Permission denied"**
   - Verifica los permisos de escritura en los archivos
   - Ejecuta el programa con privilegios de administrador si es necesario

3. **Error de codificación**
   - El programa intentará automáticamente diferentes codificaciones
   - Si persiste, verifica la codificación original del archivo

## Preguntas Frecuentes

**P: ¿El programa modifica el contenido de mis archivos?**
R: Solo agrega la ruta al inicio del archivo, el resto del contenido permanece intacto.

**P: ¿Puedo deshacer los cambios?**
R: Se recomienda hacer una copia de seguridad antes de procesar los archivos. El programa no incluye función de deshacer.

**P: ¿Qué pasa si proceso el mismo directorio dos veces?**
R: La ruta se agregará nuevamente al inicio del archivo. Se recomienda procesar los archivos solo una vez.

**P: ¿El programa afecta el rendimiento de mi sistema?**
R: El impacto es mínimo y depende de la cantidad de archivos a procesar.

**P: ¿Los archivos binarios son afectados?**
R: No, el programa solo procesa los tipos de archivo especificados en la lista de extensiones.