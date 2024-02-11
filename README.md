# EPL PREDICTOR

This project aims to predict future matches that will be played in English Premier League.

# OPERATION

Past result data is scraped from https://www.espn.com/soccer/scoreboard/_/date/20240130/league/eng.1 Data is stored in local database usin PostgreSQL

# REQUIREMENTS

Before using the program, requirements.txt should be installed in your computer. Installation can be done by copying the command below to terminal.

```bash
pip install -r requirements.txt
```

# USAGE

Clone this repository into your computer by

```bash
git clone https://github.com/anitdevrim/EPL-Match-Predictor
```

Go into the directory by

```bash
cd EPL-Match-Predictor
```

Make sure that you change the values in funcs.py in order to connect the PostgreSQL database. After doing that run the scrape_and_create.py by

```bash
python3 scrape_and_create.py
```

This command will scrape all the data from the website, create a table and insert the data to database.

After that simply run

```bash
python3 main.py
```

to run the program.

Use terminal to give inputs and the output will be printed through terminal.
