import questionary


class Building():
    def __init__(self, address, size, construction_year, property_type, air_con, renn, renn_year=None):
        self.address = address
        self.size = size
        self.construction_year = construction_year
        self.property_type = property_type
        self.air_con = air_con
        self.rennovation = renn
        self.renn_year = renn_year

    def __repr__(self) -> str:
        return f"""Building: Address: {self.address} \nSize: {self.size} \nConstruction Year: {self.construction_year} \nProperty Type: {self.property_type} \nAir Con: {self.air_con} \nRennovated: {self.rennovation} \nRennovation Year: {self.renn_year}"""


class EnergyConsumption():
    def __init__(self, energy_type, energy_amount, ren_energy_type=None, ren_energy_amount=None):
        self.energy_type = energy_type
        self.energy_amount = energy_amount
        self.ren_energy_type = ren_energy_type
        self.ren_energy_amount = ren_energy_amount

    def __repr__(self) -> str:
        return f"""Energy Type: {self.energy_type} \nEnergy Consumption: {self.energy_amount} \nRenewable Energy Type: {self.ren_energy_type} \nRenewable Energy Consumption: {self.ren_energy_amount}"""


class Settings():
    def __init__(self, low_scenario=True):
        self.low_scenario = low_scenario


class CrremGraph():
    def __init__(self):
        # Build command line or Tkinter graph that user can manipulate
        pass


class Portfolio:
    # Build an aggregated portfolio overview
    pass
