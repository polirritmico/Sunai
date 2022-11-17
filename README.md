# Sunai

Proyecto de postulación

## Uso

### Script

Instrucciones de uso

### Tests

Para correr los unittest:

```command
$ python -m unittest discover . -b
```

## Diseño

Consideraciones de diseño

## Árbol de directorios

```command
Sunai
├── docs
│   └── LICENSE.md
├── __main__.py
├── README.md
├── src
└── test
└── __init__.py
```

## Instrucciones

**Descripción del desafío**

La solución debe ser presentada en github, en un repositorio público por lo que
una vez finalizado, nos deben enviar el link a: reclutamiento@sunai.cl

En esta oportunidad, contarás con 2 archivos (`.xlsx`), donde cada uno representa
la generación de energía en una planta solar de 1 día completo, dividida por
inversor. La relación entre inversor y planta es de muchos a uno, es decir, una
planta está relacionada a 1 o más inversores.

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


