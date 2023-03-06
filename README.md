# Space-Exploration

Space Exploration CLI

Introduction

The Space Exploration CLI is a command-line interface tool that allows users to get information on potentially habitable planets discovered by space agencies around the world. With this CLI, users can access information such as the name of the planet, the star system where it is located, and the distance to it.

Getting Started
To get started with the Space Exploration CLI, follow the steps below:

Clone the Repository
Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/<your-username>/space-exploration-cli.git
Install Dependencies
Navigate to the project directory and install the dependencies by running the following command:

bash
Copy code
pipenv install
Set up the Database
Set up the database by running the following command in the lib/db directory:

bash
Copy code
alembic upgrade head
Seed the Database
Seed the database by running the following command in the lib/db directory:

bash
Copy code
python seed.py
Running the CLI
Run the CLI by executing the following command in the project directory:

bash
Copy code
python lib/cli.py
Usage
The Space Exploration CLI allows users to search for potentially habitable planets based on their preferences. Users can filter planets by star system or distance.

Command Line Arguments
The following command-line arguments are available:

--system
Filter planets by the star system where they are located. Usage:

perl
Copy code
python lib/cli.py --system <star system>
--distance
Filter planets by their distance from Earth in light-years. Usage:

bash
Copy code
python lib/cli.py --distance <distance in light-years>
Commands
The following commands are available:

list
List all potentially habitable planets in the database. Usage:

bash
Copy code
python lib/cli.py list
filter
Filter potentially habitable planets by star system or distance. Usage:

python
Copy code
python lib/cli.py filter
exit
Exit the CLI. Usage:

bash
Copy code
python lib/cli.py exit
Dependencies
The Space Exploration CLI relies on the following dependencies:

Python 3.8
SQLAlchemy
Alembic
Click
Contributing
Contributions to the Space Exploration CLI are welcome. To contribute, please follow the steps below:

Fork the repository
Create a new branch for your feature or bug fix
Make your changes and test them thoroughly
Create a pull request
License
The Space Exploration CLI is licensed under the MIT License.
#(using pip install exoplanet from PyPi)