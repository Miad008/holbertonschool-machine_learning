#!/usr/bin/env python3
"""Module for finding home planets of sentient species."""

import requests


def sentientPlanets():
    """Return a list of home planets for all sentient species."""
    url = "https://swapi-api.alx-tools.com/api/species/"
    planets = []

    while url:
        res = requests.get(url)
        data = res.json()

        for species in data.get("results", []):
            classification = species.get("classification", "")
            designation = species.get("designation", "")

            if classification == "sentient" or designation == "sentient":
                homeworld = species.get("homeworld")

                if homeworld:
                    planet_res = requests.get(homeworld)
                    planet_data = planet_res.json()
                    planets.append(planet_data.get("name"))

        url = data.get("next")

    return planets
