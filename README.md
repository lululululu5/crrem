# Building and Energy Assessment Tool

## Overview

This project provides a command-line tool to perform building and energy assessments, saving the results to a JSON file. Users can choose between conducting a building assessment or an energy assessment.

The primary value of the CRREM analysis is to allow users to assess the climate change risk of their portfolio by evaluating energy consumption and emissions data.

## Features

- **Building Assessment**: Collects and stores data about a building.
- **Energy Assessment**: Collects and stores data about the building's energy consumption.
- **Data Persistence**: Saves the collected data to a JSON file (`property.json`) and loads it upon restarting the tool.

## Requirements

- Python 3.x
- `questionary` library for interactive command-line prompts
- `assessment.py` file containing the `Assessment` class
- `classes.py` file containing the `Building` class

## Setup

1. **Install Required Libraries**:
   ```sh
   pip install questionary
   ```
