#!/usr/bin/env python3
import requests


def availableShips(passengerCount):
    url = "https://swapi-api.alx-tools.com/api/starships/"
    ships = []

    while url:
        res = requests.get(url)
        data = res.json()

        for ship in data.get('results', []):
            passengers = ship.get('passengers', '0')

            if passengers not in ['unknown', 'n/a']:
                passengers = passengers.replace(',', '')

                if passengers.isdigit() and int(passengers) >= passengerCount:
                    ships.append(ship.get('name'))

        url = data.get('next')

    return ships
