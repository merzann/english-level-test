# English Level Assessment Quiz


## Overview
This Python application assesses a student's English level based on vocabulary, grammar, and text comprehension. Results are recorded in Google Sheets, saved to a JSON file  and then exported to Zapier to automatically send an email to the student with their results.
The application is part of a learning platform from a Homestay Host & English Tutor who uses the results for developping an individual course plan for each student to address their needs in the most efficient way.

## Features
- Import questions from Google Sheets
- Administer quiz via command-line interface
- Calculate and determine CEFR level
- Record and export results

## Validator Testing:

    - PEP8
    

## Deployment
    
This project was deployed using a mock terminal provided by Code Institute for Heroku

    Steps for deployement
    - Clone or fork the repository
    - Install required libraries: `pip install gspread google-auth`
    - Set up a Google Sheets API and update `credentials.json`
    - Create a new Heroku App
    - Set the buildpacks to Python and NodeJS in that order
    - Link the Heroku App to the repository
    - Click on DEPLOY


## Usage

Run the script and follow the instructions to complete the quiz. The application will guide you through a series of questions to determine your English proficiency level. Results are saved in `results.json`.


## Contributing

Please fork the repository and submit pull requests.


## Acknowledgement

    - Reading text: National Geographic Education, Last Updated February 21, 2024, National Geographic Society, National Geographic Society
    - The template used for building this project was provided by Code Institute on Github for student projects [p3-template](https://github.com/Code-Institute-Org/p3-template)
    - the Stack Overflow community for pointing me in the right direction when I ran into the scoring issue


## Author

- [merzann](https://github.com/merzann)


## License
[![MIT License](https://img.shields.io/badge/License%20-%20MIT-olivgreen)](readme_media/LICENSE.md)
