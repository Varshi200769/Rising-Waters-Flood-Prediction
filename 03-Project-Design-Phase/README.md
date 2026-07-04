# Project Design Phase

## System Architecture

The Flood Prediction System consists of the following layers:

- User Interface
- Flask Application
- Machine Learning Model
- Dataset
- Prediction Output

The user enters weather information through the web application. Flask processes the input, loads the trained Machine Learning model, predicts flood risk, and displays the result.

## Entity Relationship Diagram

The ER Diagram consists of two main entities:

1. User
2. Prediction

A user enters weather parameters, and the system generates a flood prediction result based on those values.
