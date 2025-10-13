# Pomodoro Timer

This is a simple Pomodoro Timer application built with Python's tkinter library for the graphical user interface and pygame for audio playback. The Pomodoro Technique is a time management method that uses a timer to break down work into intervals, traditionally 25 minutes in length, separated by short breaks. This application helps users implement this technique to improve focus and productivity.

## Description

The Pomodoro Timer allows users to set custom work and break durations. It provides a clean and intuitive interface to start, pause, resume, and reset the timer. The application also keeps a log of completed Pomodoro sessions, which can be viewed and managed. Additionally, it features an optional focus music player to aid concentration during work sessions.

## Features

*   **Customizable Timers:** Set your own durations for work sessions and breaks.
*   **Session Tracking:** The application counts and logs completed Pomodoro sessions.
*   **History Log:** View a history of your completed sessions, including the day, date, and time.
*   **History Management:** Delete individual session records from the history log.
*   **Focus Music:** Play and pause background music to help you concentrate.
*   **User-Friendly Interface:** A simple and intuitive graphical user interface.
*   **Persistent History:** Session history is saved to a file (`pomodoro_sessions.txt`) and loaded on startup.

## Requirements

To run this application, you will need to have Python installed on your system, along with the following libraries:

*   **tkinter:** This is the standard GUI library for Python and usually comes with the Python installation.
*   **pygame:** This library is used for playing audio. You can install it using pip:
    ```
    pip install pygame
    ```
You will also need an audio file named `focus_music.mp3` in the same directory as the Python script for the focus music feature to work.

## How to Use

1.  **Run the script:** Execute the Python script to launch the Pomodoro Timer application.
2.  **Set Durations:**
    *   Click the "Start" button to open a new window.
    *   Enter your desired work session duration in minutes and seconds.
    *   Enter your desired break duration in minutes and seconds.
    *   Click "OK" to start the timer with your custom durations, or click "Default Value" to use the standard 25-minute work and 5-minute break intervals.
3.  **Timer Controls:**
    *   **Pause:** Stop the timer.
    *   **Resume:** Continue the timer from where it was paused.
    *   **Reset:** Stop the timer and reset it to zero.
    *   **Skip:** End a break session early and start the next work session.
4.  **History Log:**
    *   Click the "History log" button to view a record of your completed sessions.
    *   In the history window, you can select a session and click "Delete" to remove it.
5.  **Focus Music:**
    *   Click the "Focus music OFF" button to start playing the background music. The button text will change to "Focus music ON".
    *   Click the "Focus music ON" button to stop the music.
6.  **Exiting the Application:** Close the main window and confirm that you want to quit in the dialog box.

## Files

*   **`your_script_name.py`:** The main Python script for the Pomodoro Timer application.
*   **`pomodoro_sessions.txt`:** A text file that stores the history of completed Pomodoro sessions. This file is created automatically when you complete your first session.
*   **`focus_music.mp3`:** An audio file for the focus music feature. You may change if you like.

# This project is an original work developed by  [**Winson**](https://github.com/Winson5552). <br> *Please be aware that this application is a simulator created for demonstration and educational purposes only. <br> *It is not a final, production-ready product. Its purpose is to showcase specific functionalities, concepts, and technical skills. <br> *As a simulation, it may contain simplified features, mock data, or incomplete functionality. <br> *It is NOT intended for commercial use or deployment in a live environment.
