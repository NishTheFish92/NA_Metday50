# BP Medicine Advisor 💊

## Motivation

This project was created to provide a simple and reliable blood pressure (BP) advisor for my grandmother, who experiences frequent fluctuations in her BP. The goal is to make daily BP management easier.

## Features

- **Easy-to-use interface:** Enter systolic and diastolic BP readings and select the time of measurement (morning or night).
- **Configurable thresholds:** BP thresholds and advice logic can be easily updated in the config file.
- **Accessible anywhere:** Hosted online for quick access from any device.

## How it works

1. Enter your systolic and diastolic BP readings.
2. Select whether the reading was taken in the morning or at night.
3. Click "Get Advice" to receive a recommendation on medication or dietary actions.

## Live Demo

Try it here: [https://nametday50.streamlit.app/](https://nametday50.streamlit.app/)

## Setup

To run locally:

1. Clone this repository.
2. Install dependencies:

``` 
pip install -r requirements.txt 
```
3. Start the app:
```
streamlit run main.py
```

## Customization

- BP thresholds and advice logic are defined in `app/config.py` for easy editing.


## Disclaimer

This project is for personal use and educational purposes only.