# Lyft Task Project

This project models a car service with multiple components like **battery**, **engine**, and **tyres**, along with a factory for car creation. It aims to simulate a system similar to a Lyft vehicle management system. Each module is responsible for a specific car part, with varying battery and engine models and tire options.

## Project Structure:

- **battery**: Contains different battery models for the car, including the `nuubbin_battery.py`, `spindler_battery.py`, and an abstract `battery.py` for common battery functions.
  - `__init__.py`: Initialization file to make the folder a Python package.
  - `battery.py`: Defines the base battery structure and properties.
  - `nuubbin_battery.py`: A specific implementation of a battery model.
  - `spindler_battery.py`: Another battery model variant.
  
- **engine**: Includes various engine models such as `capulet_engine.py`, `sternman_engine.py`, and `willoughby_engine.py` for different types of engines.
  - `__init__.py`: Initialization file for engine package.
  - `capulet_engine.py`: Defines one type of engine.
  - `sternman_engine.py`: Another engine model.
  - `willoughby_engine.py`: A third engine option.

- **tyre**: Contains different tire models and functionalities for handling tires in the system.
  - `__init__.py`: Initialization file for tyre module.
  - `carigantyre.py`: A specific tyre model.
  - `octopryime_tyre.py`: Another tyre type.
  - `tyres.py`: A base file defining common tire functionality.

- **test**: Contains test scripts to verify functionality across all components and modules.
  - `__init__.py`: Initialization for test package.
  
- **car_factory**: Contains the logic to construct and assemble the full car from available components.

- **serviceable.py**: Contains methods to check if cars are serviceable based on components' conditions (e.g., battery health, engine status, tyre wear).

- **utils.py**: Includes helper functions used across the project.

- **car.py**: The main file representing a car object, integrating batteries, engines, and tyres.

- **README.md**: Documentation about the project (this file).

- **.gitignore**: Specifies files and directories that should be ignored by Git.

## Getting Started:

### Prerequisites:
Make sure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).

### Installation:

- * Clone the repository:
```
- *git clone https://github.com/yourusername/Lyft-Task.git
```

- * Navigate to the project folder:
```
cd Lyft-Task
```
- * Install any dependencies (if applicable) using:
```
pip install -r requirements.txt
```

### Running the Project:
- *To create a car and test the components, you can run the car.py script. It will simulate assembling a car with different engines, batteries, and tyres.

- *python car.py
 ### Testing:
Use pytest or another testing framework to test the components:

 ### pytest test
- Usage:
- *Battery Models: You can choose different battery models like NuubbinBattery or SpindlerBattery.
- *Engine Models: Choose between CapuletEngine, SternmanEngine, or WilloughbyEngine.
- *Tyre Models: Select from CariganTyre, OctopryimeTyre, and others.
 ### License
This project is licensed under the MIT License - see the LICENSE file for details.
