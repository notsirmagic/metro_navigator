# CLI Tool para calcular la ruta mas corta y costo entre estaciones del Metro de Caracas
# By: notsirmagic
# GitHub: https://github.com/notsirmagic

import sys

# Costo base entre estaciones y costo de transferencia de linea
travel_cost = 1
transfer_cost = 3

# Lista de todas las estaciones de cada línea de metro
Lineas_Metro = {
    "Linea_1": [
        "Propatria", "Pérez Bonalde", "Plaza Sucre", "Gato Negro", "Agua Salud", "Caño Amarillo", "Capitolio", "El Silencio", 
        "La Hoyada", "Parque Carabobo", "Bellas Artes", "Colegio de Ingenieros", "Plaza Venezuela", "Sabana Grande", "Chacaíto", 
        "Chacao", "Altamira", "Miranda", "Los Dos Caminos", "Los Cortijos", "La California", "Palo Verde"
    ],

    "Linea_2": [
        "El Silencio", "Capuchinos", "Maternidad", "Artigas", "La Paz", "La Yaguara", "Carapita", "Antímano", "Mamera", "Caricuao",  
        "Ruiz Pineda", "Las Adjuntas", "Zoológico"
    ],

    "Linea_3": [
        "Plaza Venezuela", "Ciudad Universitaria", "Los Símbolos", "La Bandera", "El Valle", "Los Jardines", "Coche", "Mercado", "La Rinconada"
    ],

    "Linea_transferencia": [
        "Plaza Venezuela", "El Silencio"
    ]
}

# Funcion para obtener las líneas de una estacion
def get_station_lines(station, lineas_metro):
    lineas = []
    for line_name, stations in lineas_metro.items():
        if station in stations:
            lineas.append(line_name)
    return lineas

# Funcion para verificar si una estacion existe
def does_exist_station(station, lineas_metro):
    return bool(get_station_lines(station, lineas_metro))

# Funcion para calcular la ruta y el costo en caso de una linea directa
def direct_trip_with_route(station_a, station_b, common_line, lineas_metro, travel_cost):
    line_station = lineas_metro[common_line]
    index_a = line_station.index(station_a)
    index_b = line_station.index(station_b)
    stations_quantity = abs(index_a - index_b)
    total_cost = stations_quantity * travel_cost

    route = []
    for i in range(min(index_a, index_b), max(index_a, index_b) + 1):
        route.append(f"{line_station[i]} (Línea {common_line.split('_')[1]})")

    return route, stations_quantity, total_cost

# Funcion para calcular la ruta con transferencia entre líneas
def calculate_transfer(station_a, station_b, lines_a, lines_b, metro_lines, travel_cost, transfer_cost):
    transfer_stations = metro_lines["Linea_transferencia"]

    for transfer in transfer_stations:
        # Buscar la linea de origen que pasa por la estacion de transferencia
        if any(transfer in metro_lines[line] for line in lines_a):
            # Buscar la linea de destino que pasa por la estacion de transferencia
            if any(transfer in metro_lines[line] for line in lines_b):
                origin_line = next(line for line in lines_a if transfer in metro_lines[line])
                segment1 = abs(metro_lines[origin_line].index(station_a) - metro_lines[origin_line].index(transfer))

                # Calcular las estaciones de la estacion de transferencia al destino
                destination_line = next(line for line in lines_b if transfer in metro_lines[line])
                segment2 = abs(metro_lines[destination_line].index(station_b) - metro_lines[destination_line].index(transfer))

                total_stations = segment1 + segment2
                total_cost = total_stations * travel_cost + transfer_cost

                route = []
                for i in range(metro_lines[origin_line].index(station_a), metro_lines[origin_line].index(transfer) + 1):
                    route.append(f"{metro_lines[origin_line][i]} (Línea {origin_line.split('_')[1]})") 
                route.append(f"→ Transferencia en {transfer} a Línea {destination_line.split('_')[1]}") 
                for i in range(metro_lines[destination_line].index(transfer), metro_lines[destination_line].index(station_b) + 1):
                    route.append(f"{metro_lines[destination_line][i]} (Línea {destination_line.split('_')[1]})")

                return route, total_stations, total_cost

    return None, None, None  # No se encontro transferencia

# Funcion para manejar la entrada del usuario y validar las estaciones
def input_station(prompt, lineas_metro):
    station = input(prompt).strip().title()
    while not does_exist_station(station, lineas_metro):
        print(f"La estación '{station}' no ha sido encontrada, por favor intente de nuevo.")
        station = input(prompt).strip().title()
    return station

# Funcion principal para manejar la ejecucion del programa
def main():
    if len(sys.argv) < 3:
        print('Uso: file.py <estacion_origen> <estacion_destino>')
        sys.exit(1)

    station_a = sys.argv[1].strip().title()
    station_b = sys.argv[2].strip().title()

    # Validacion de existencia de estaciones
    if not does_exist_station(station_a, Lineas_Metro) or not does_exist_station(station_b, Lineas_Metro):
        print("Una de las estaciones no existe. Por favor, verifica.")
        sys.exit(1)

    # Obtener las líneas que pasan por las estaciones
    lines_a = get_station_lines(station_a, Lineas_Metro)
    lines_b = get_station_lines(station_b, Lineas_Metro)

    # Buscar una línea común
    def find_common_line(lines_a, lines_b):
        for line in lines_a:
            if line in lines_b:
                return line
        return None

    common_line = find_common_line(lines_a, lines_b)

    print("\n//////// RUTA ÓPTIMA ////////")

    if common_line: # Calcular la ruta si hay linea directa
        route, stations, cost = direct_trip_with_route(station_a, station_b, common_line, Lineas_Metro, travel_cost)
        print(f"Ruta directa entre {station_a} y {station_b}:")
        for station in route:
            print(f"  → {station}")
        print(f"\nCosto Total: {cost} unidades\n")
    else:
        # Si no hay linea directa, calcular la ruta con transferencia
        print("No hay línea directa, se requiere transferencia.")
        route, total_stations, total_cost = calculate_transfer(station_a, station_b, lines_a, lines_b, Lineas_Metro, travel_cost, transfer_cost)
        
        if route:
            print(f"Ruta con transferencia entre {station_a} y {station_b}:")
            for station in route:
                print(f"  → {station}")
            print(f"\nCosto Total: {total_cost} unidades\n")
        else:
            print("No se pudo encontrar una ruta de transferencia.\n")

# Ejecutar la función principal
if __name__ == "__main__":
    main()