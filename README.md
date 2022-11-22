# Sunai

Proyecto de postulación

## Uso

### Ejecución

```command
$ python sunai_challenge.py <source data folder> <output folder>
```
> Para ejecutar desde el repositorio, sustituir `sunai_challenge.py` por
> `__main__.py`.

Por ejemplo, teniendo una carpeta `data` con archivos _xlsx_ y usando `output`
como carpeta de destino:

```command
$ python sunai_challenge.py data output
```

La estructura resultante de los ficheros generados será la siguiente:

```command
Demo
├── data
│   ├── powerplant_data_01.xlsx
│   ├── powerplant_data_02.xlsx
│   └── ...
├── output
│   ├── images
│   │   ├── 0186_2022-12-21.jpg
│   │   ├── 0186_2022-12-22.jpg
│   │   └── ...
│   ├── 0186_2022-12-21_summary.txt
│   ├── 0186_2022-12-22_summary.txt
│   └── ...
└── sunai_challenge.py
```
> En este caso de ejemplo, 0186 es la id de la planta y la fecha corresponde
> a la fecha de lectura contenida en el archivo de entrada.

### Ayuda

```command
$ python sunai_challenge.py -h
```

### Tests

Para ejecutar los unittest:

```command
sunai_proyect_folder $ python -m unittest discover . -b
```

Para ejecutar el test de desempeño:

```command
test $ ./performance_test.py
```

### Dependencias

- Python 3.10.8
- Pandas
- Pillow (para unit tests)

## Diseño

![Diseño básico](/docs/basic_design.png)

### Instrucciones y consideraciones:

- Cada archivo tiene la generación de energía de 1 día completo de una planta.
- En cada planta puede haber 1 o más inversores (columna id_i).
- El archivo tiene la energía generada dividia por inversor.
- Considerar inputs de 1000 archivos (días).

Por cada archivo/input:

1. Generar un gráfico (es 1 para cada archivo, o sea 1 gráfico por día/archivo):
  - **Título:** YYYY/MM/DD\_planta\_idPlanta
  - **X:** Date. Ya que es diario no poner la fecha en x_label sino hh:mm
  - **Y:** Active power
2. Generar **txt**:
  - Suma diaria del _active power_ (La suma de toda la _Series_ en el archivo)
  - **Min y max** _active power energy_ del día.
  - Path absoluto al gráfico diario generado.

Global:

3. Output consola:
  - Suma total del active power por día de **todas las plantas**. Se obtiene la
    suma del active power del día de cada planta y se suma. Se muestra esa info
    para todos los días procesados.
  - El requisito anterior considera la info de todos los archivos, por lo tanto
    se mostrará solo 1 vez en lugar de repetir la misma salida por cada archivo
    (por ejemplo, 1000 veces los mismo).


## Árbol de directorios del proyecto

```command
Sunai
├── docs
│   ├── basic_design.png
│   └── LICENSE.md
├── src
│   ├── power_plant_day.py
│   └── sunai_challenge.py
├── test
│   ├── cases
│   │   ├── subfolder
│   │   │   └── dummy.xlsx
│   │   ├── data_plantas_python_1_1.xlsx
│   │   ├── data_plantas_python_2.xlsx
│   │   ├── dummy.xlsx
│   │   ├── ignore.file
│   │   └── small_data.xlsx
│   ├── __init__.py
│   ├── test_unit_graph_output_format.py
│   ├── test_unit_power_plant_day.py
│   └── test_unit_sunai_challenge.py
├── __main__.py
├── performance_test.py
├── README.md
```

-------------------------------------------------------------------------------


## Instrucciones textuales

**Descripción del desafío**

La solución debe ser presentada en github, en un repositorio público por lo que
una vez finalizado, nos deben enviar el link a: reclutamiento@sunai.cl

En esta oportunidad, contarás con 2 archivos (`.xlsx`), donde cada uno
representa la generación de energía en una planta solar de 1 día completo,
dividida por inversor. La relación entre inversor y planta es de muchos a uno,
es decir, una planta está relacionada a 1 o más inversores.

El desafío es poder procesar los archivos disponibles en recursos, tomando en
cuenta que en la realidad pueden haber 1000 archivos a procesarse.

Para cada archivo, se solicita lo siguiente:

1. Generar un gráfico, un line chart donde el eje x sea la fecha y el eje y sea
   el active power para finalmente guardarlo.
2. Guardar en un (.txt) la suma por día del active power, el valor máximo y
   mínimo del active energy y por último, la ruta donde se encuentra el gráfico
   generado en 1).
3. Imprimir en consola la suma total del active power por día, de todas las
   plantas


