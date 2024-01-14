from enum import Enum

class GovernmentType(Enum):
    DEMOCRACY = "Democracy"
    REPUBLIC = "Republic"
    AUTOCRACY = "Autocracy"
    MIXED_SYSTEM = "Mixed_system"


class Country:
    def __init__(self, name, capital, code, population, area, gpd, govern):
        #population in a million, area in km^2, gpd in a billion
        self.name = name
        self.capital = capital
        self.code = code
        self.population = population
        self.area = area
        self.gpd = gpd
        self.govern = govern


class Land:
    def __init__(self, name):
        self.name = name
        self.countries = []

    def add_country(self, country):
        self.countries.append(country)


def density(countries):
    for country in countries:
        density = country.population * 10 ** 6 / country.area # multiply by 10^6, cause country.population I saved in million
        print(f"{country.name}: Density - {round(density, 2)} people per square km")
    print()

def sort_countries_by_gdp(countries):
    sorted_countries = sorted(countries, key=lambda country: country.gpd, reverse=True)
    return sorted_countries


def selected_countries(countries, criteria):
    selected_countries = [country for country in countries if criteria(country)]
    return selected_countries

def main():
    """
    Creating Main function for storing data
    """
    country1 = Country("Ukraine", "Kyiv", "+380", 33.2, 603628, 173.413, "Mixed_system")
    country2 = Country("USA", "Washington", "+1", 333.287, 9833520, 26950, "Republic")
    country3 = Country("Qatar", "Doha", "+974", 2.795, 11581, 328.134, "Autocracy")
    country4 = Country("Honduras", "Tegucigalpa", "+504", 9.571, 112492, 33.992, "Republic")

    land1 = Land("Asia")
    land2 = Land("Europe")
    land3 = Land("Africa")
    land4 = Land("America")

    lands = [land1, land2, land3, land4]
    countries = [country4, country1, country3, country2]

    for i in range(len(lands)):
        lands[i].add_country(countries[i])

    density(countries)

    sorted_countries = sort_countries_by_gpd(countries)

    for i, country in enumerate(sorted_countries, 1):
        print(f"{i}. Country: {country.name}, GPD: {country.gpd}")
    print()

    selected_criteria = lambda country: len(country.name) > 5
    selected_countries_result = selected_countries(countries, selected_criteria)

    for i, country in enumerate(selected_countries_result, 1):
        print(f"{i}. Selected country: {country.name}")


if __name__ == "__main__":
    main()
