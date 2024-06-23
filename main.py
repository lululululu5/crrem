import questionary
from assessment import Assessment
from classes import Building
import json


def save_to_json(data, filename="property.json"):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")


def load_from_json(filename="property.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Error loading data: {e}")
        return {}


def main():
    data = load_from_json()
    while True:
        decision = questionary.select("What would you like to do next?", choices=[
            "Building assessment",
            "Energy assessment",
            "Exit"
        ]).ask()

        if decision == "Building assessment":
            new_building = Assessment().building_assessment()
            data['building'] = vars(new_building)
            save_to_json(data)
            print(f"Building was successfully added: \n{repr(new_building)}")

        if decision == "Energy assessment":
            energy_assessment = Assessment().energy_assessment()
            data['energy'] = vars(energy_assessment)
            save_to_json(data)
            print(f"""Energy assessment successfully completed: \n{
                  repr(energy_assessment)}""")

        if decision == "Exit":
            break


if __name__ == "__main__":
    main()
