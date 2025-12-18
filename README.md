# metro_navigator
Este es un programa de línea de comandos (CLI) en Python diseñado para calcular la ruta más corta y el costo de un viaje entre dos estaciones del Metro de Caracas, teniendo en cuenta las posibles transferencias entre líneas.

## 📝 Descripción

El programa permite al usuario ingresar dos estaciones del metro (origen y destino) y calcular la ruta más corta, ya sea directa o con transferencia entre ellas. También calcula el costo total del viaje basándose en el número de estaciones recorridas y un costo adicional en caso de que sea necesario hacer una transferencia entre líneas.

### Requisitos

- Python 3.x

## ⚙️ Instalación

1. Clona el repositorio en tu máquina local:
   ```bash
   git clone https://github.com/notsirmagic/metro_navigator.git
2. Navega al directorio del proyecto:
   ```bash
   cd metro_navigator

### Uso

El programa se ejecuta desde la línea de comandos con dos argumentos: la estación de origen y la estación de destino. Por ejemplo:
   ```bash
python metro.py 'Propatria' 'Chacao'
```


### Ejemplo de salida

Si las estaciones de origen y destino están en la misma línea:
   ```bash
//////// RUTA ÓPTIMA ////////
Ruta directa entre Propatria y Chacao:
→ Propatria (Línea 1)
→ Pérez Bonalde (Línea 1)
→ Plaza Sucre (Línea 1)
→ Gato Negro (Línea 1)
→ Agua Salud (Línea 1)
→ Caño Amarillo (Línea 1)
→ Capitolio (Línea 1)
→ El Silencio (Línea 1)
→ La Hoyada (Línea 1)
→ Parque Carabobo (Línea 1)
→ Bellas Artes (Línea 1)
→ Colegio de Ingenieros (Línea 1)
→ Plaza Venezuela (Línea 1)
→ Sabana Grande (Línea 1)
→ Chacaíto (Línea 1)
→ Chacao (Línea 1)

Costo Total: 15 unidades
```
Si se requiere una transferencia:

   ```bash

//////// RUTA ÓPTIMA ////////
No hay línea directa, se requiere transferencia.
Ruta con transferencia entre Propatria y Zoológico:
  → Propatria (Línea 1)
  → Pérez Bonalde (Línea 1)
  → Plaza Sucre (Línea 1)
  → Gato Negro (Línea 1)
  → Agua Salud (Línea 1)
  → Caño Amarillo (Línea 1)
  → Capitolio (Línea 1)
  → El Silencio (Línea 1)
  → → Transferencia en El Silencio a Línea 2
  → El Silencio (Línea 2)
  → Capuchinos (Línea 2)
  → Maternidad (Línea 2)
  → Artigas (Línea 2)
  → La Paz (Línea 2)
  → La Yaguara (Línea 2)
  → Carapita (Línea 2)
  → Antímano (Línea 2)
  → Mamera (Línea 2)
  → Caricuao (Línea 2)
  → Ruiz Pineda (Línea 2)
  → Las Adjuntas (Línea 2)
  → Zoológico (Línea 2)

Costo Total: 22 unidades
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, puedes hacerlo mediante pull requests.
- Haz un fork del repositorio.
- Crea una nueva rama para tu contribución.
- Realiza los cambios y crea un pull request.

## ¡Muestra tu apoyo! ❤️

Si te gusto el proyecto, puedes mostrar tu apoyo con una ⭐️
