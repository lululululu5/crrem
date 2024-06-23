from questionary import form
import questionary
from classes import Building, EnergyConsumption
from datetime import datetime


class Assessment():
    def __init__(self):
        pass

    def validate_year(self, year_text):
        try:
            year = int(year_text)
            if 2020 < year <= datetime.now().year:
                return True
            else:
                return "Pleas provide a valid year. No earlier than 2020 or later than the current year."
        except ValueError:
            return "Please provide a valid integer."

    def validate_year_retrofit(self, year_text):
        try:
            year = int(year_text)
            if datetime.now().year <= year <= 2050:
                return True
            else:
                return "Pleas provide a valid year. No later than the current year."
        except ValueError:
            return "Please provide a valid integer."

    def validate_size(self, size):
        try:
            size = int(size)
            if size > 0:
                return True
            else:
                return "Please provide net size in square meter. Value must be larger than zero."
        except ValueError:
            return "Please provide a valid integer"

    def validate_energy_consumption(self, kWh):
        try:
            kWh = int(kWh)
            if kWh > 0:
                return True
            else:
                return "Please provide energy consumption in kWh. Value must be larger than zero."
        except ValueError:
            return "Please provide a valid integer"

    def building_assessment(self):
        self.rennovation = {}
        self.answers = form(
            address=questionary.text("What is the address of your property?", validate=lambda text: True if len(
                text) > 3 else "Address must be at least 3 letters long."),
            construction_year=questionary.text(
                "Enter the year of construction:", validate=self.validate_year),
            property_type=questionary.select("Select property type: ", choices=[
                                             'Residential Multi Family', 'Residential Single Family']),

            size=questionary.text(
                "Please provide us the net square meter size of your propery:", validate=self.validate_size),
            air_con=questionary.select("Do you have an air condition? ", choices=[
                                       "Yes", "No"], instruction="In case of an AC-unit we need to account for coolant emissions"),
            rennovation=questionary.select("Do you plan to retrofit the building in the future? ", choices=[
                                           "Yes", "No"], instruction="Based on the retrofitting we will calculate the sustainability performance of the building"),
        ).ask()

        if self.answers["rennovation"] == "Yes":
            self.rennovation = form(
                year_of_rennovation=questionary.text(
                    "Year of rennovation: ", validate=self.validate_year_retrofit)
            ).ask()

        self.new_building = Building(
            self.answers["address"],
            self.answers["size"],
            self.answers["construction_year"],
            self.answers["property_type"],
            self.answers["air_con"],
            self.answers["rennovation"],
            self.rennovation.get("year_of_rennovation", None)
        )

        return self.new_building

    def energy_assessment(self):
        self.ren_energy = {}
        self.answers = form(
            energy_type=questionary.select("What type of energy do you consume?", choices=[
                                           "Grid Electricity", "Natural Gas", "Fuel oil", "District heating"], instruction="Focus on conventional energy sources. You can add renewable sources at a later stage"),
            energy_amount=questionary.text(
                "How much energy do you consume per year (in kWh)?", validate=self.validate_energy_consumption),
            renewable_energy=questionary.select(
                "Do you have on-site renewable energy?", choices=["Yes", "No"]),
        ).ask()

        if self.answers["renewable_energy"] == "Yes":
            self.ren_energy = form(
                ren_energy_type=questionary.select("What type of renewable energy do you produce and consume?", choices=[
                                                   "PV", "Wind", "Heatpump", "Solar Thermal"]),
                ren_energy_amount=questionary.text("How much renewable energy do you consume?", validate=self.validate_energy_consumption)).ask()

        self.energy_consumption = EnergyConsumption(
            self.answers["energy_type"],
            self.answers["energy_amount"],
            self.ren_energy.get("ren_energy_type", None),
            self.ren_energy.get("ren_energy_amount", None)
        )

        return self.energy_consumption
