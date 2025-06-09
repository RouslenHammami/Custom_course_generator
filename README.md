# Custom Course Generator

A FastAPI backend paired with a Python Tkinter GUI to generate personalized beginner-level course outlines using OpenRouter's LLM API.

---

## Project Overview

This application enables users to create custom courses by specifying a topic and duration.  
The backend (`main.py`) handles API requests, communicates with OpenRouter’s language model, and returns a structured course outline.  
The frontend (`gui.py`) provides a simple desktop interface for users to input parameters and view generated courses.

---

## Features

- Generate day-by-day course outlines tailored to user input  
- Asynchronous FastAPI backend for efficient API calls  
- User-friendly Tkinter GUI client  
- Integration with OpenRouter’s language model

---

## Prerequisites

- Python 3.8 or higher  
- An API key from [OpenRouter](https://openrouter.ai/)

---

## Setup Instructions

1. **Create .env file**

In the project root, create a .env file : 
OPENROUTER_API_KEY=your_api_key_here

2. **Install dependencies**

pip install fastapi uvicorn httpx python-dotenv requests

3. **Install dependencies**

uvicorn main:app --reload

4. **Run the GUI client**

python gui.py


## Usage

---

1. Launch the GUI application.
2. Enter the desired course topic and duration (e.g., "Python Basics", "7 days").
3. Click Generate Course.
4. View the generated course outline in the scrollable text area.
