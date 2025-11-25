# Unit Converter

**A Simple and Interactive Unit Conversion Tool**

---

## Project Information

**Student Name:** Abhra Banerjee  
**Registration Number:** 25BCY10118  
**Institution:** VIT Bhopal  
**Department:** Computer Science and Engineering (CSE)  
**Faculty Mentor:** Professor Sandeep Monga  
**Project Date:** November 2025

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [System Requirements](#system-requirements)
4. [Installation & Setup](#installation--setup)
5. [Usage Guide](#usage-guide)
6. [Code Architecture](#code-architecture)
7. [Functionality Details](#functionality-details)
8. [Pseudocode](#pseudocode)
9. [Flowchart](#flowchart)
10. [How to Run](#how-to-run)
11. [Example Output](#example-output)
12. [Future Enhancements](#future-enhancements)
13. [Troubleshooting](#troubleshooting)

---

## Overview

The **Unit Converter** is a command-line based Python application that provides a user-friendly interface for converting between different units of measurement. The application currently supports three categories of conversions:

- **Temperature:** Celsius ⟷ Fahrenheit
- **Length:** Kilometers ⟷ Meters
- **Weight:** Kilograms ⟷ Grams

This project demonstrates fundamental Python programming concepts including functions, conditional statements, user input handling, and menu-driven programming.

---

## Features

✓ **Interactive Menu System** - User-friendly interface with clear options  
✓ **Multiple Conversion Categories** - Temperature, Length, and Weight conversions  
✓ **Error Handling** - Input validation to prevent incorrect conversions  
✓ **Flexible Input** - Accepts both numeric inputs and keyword-based selections  
✓ **Precise Output** - Temperature conversions rounded to 2 decimal places  
✓ **Loop-Based Navigation** - Continuous operation until user exits  
✓ **Clean Display** - Decorative separators and clear prompts for readability  

---

## System Requirements

- **Python Version:** 3.6 or higher
- **Operating System:** Windows, macOS, or Linux
- **Memory:** Minimal (< 50 MB)
- **Dependencies:** None (uses only Python Standard Library)

---

## Installation & Setup

1. **Clone or Download the Project**
   ```bash
   # If using Git
   git clone <repository-url>
   cd unit-converter
   
   # Or manually download the converter.py file
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   ```

3. **No Additional Dependencies Required**
   This project uses only Python's built-in libraries.

---

## Usage Guide

### Running the Application

```bash
python converter.py
```

### Main Menu Navigation

Upon running the application, you'll see:

```
o=o=o=o=o=o=o=o=o=o=o=o
1 temp
2 length
3 weight
4 quit
o=o=o=o=o=o=o=o=o=o=o=o

what do u want >
```

### Input Options

The application accepts flexible input:

- **Numeric Input:** Enter `1`, `2`, `3`, or `4`
- **Keyword Input:** 
  - For Temperature: `temp` or `temperature`
  - For Length: `len` or `length`
  - For Weight: `w` or `weight`
  - For Quit: `quit`, `exit`, `bye`, or `q`

---

## Code Architecture

### Module Structure

The application is organized into four main functions:

| Function | Purpose | Parameters |
|----------|---------|------------|
| `temp_converter()` | Handles temperature conversions | None |
| `length_stuff()` | Handles length conversions | None |
| `weight_converter()` | Handles weight conversions | None |
| `main()` | Controls program flow and menu navigation | None |

### Design Pattern

The application uses a **Menu-Driven Architecture** with the following characteristics:

- **Separation of Concerns:** Each conversion type has its own function
- **While Loop Pattern:** Continuous operation until user selects exit
- **Input Validation:** Basic error checking for invalid inputs
- **User-Friendly Output:** Clear prompts and formatted results

---

## Functionality Details

### 1. Temperature Converter

**Purpose:** Converts between Celsius and Fahrenheit

**Conversions:**
- Celsius to Fahrenheit: \(F = C \times \frac{9}{5} + 32\)
- Fahrenheit to Celsius: \(C = (F - 32) \times \frac{5}{9}\)

**Features:**
- Accepts both positive and negative values
- Rounds Fahrenheit results to 2 decimal places
- Displays results with proper unit symbols (°C, °F)

### 2. Length Converter

**Purpose:** Converts between Kilometers and Meters

**Conversions:**
- Kilometers to Meters: \(meters = km \times 1000\)
- Meters to Kilometers: \(km = meters \div 1000\)

**Features:**
- Handles decimal values (e.g., 2.5 km)
- Direct mathematical conversion without rounding
- Displays results with proper unit labels

### 3. Weight Converter

**Purpose:** Converts between Kilograms and Grams

**Conversions:**
- Kilograms to Grams: \(grams = kg \times 1000\)
- Grams to Kilograms: \(kg = grams \div 1000\)

**Features:**
- Accepts decimal values for precise conversions
- Provides feedback on invalid inputs with a unique message
- Displays results with proper unit labels

---

## Pseudocode

### Main Program Flow

```
FUNCTION main():
    DISPLAY "Welcome message"
    WHILE TRUE:
        DISPLAY menu options
        INPUT user choice
        
        IF choice is "1" or "temp" or "temperature":
            CALL temp_converter()
        ELSE IF choice is "2" or "len" or "length":
            CALL length_stuff()
        ELSE IF choice is "3" or "w" or "weight":
            CALL weight_converter()
        ELSE IF choice is "4" or "quit" or "exit" or "bye" or "q":
            DISPLAY "bye bye"
            BREAK from loop
        ELSE:
            DISPLAY "invalid input message"
    END WHILE
END FUNCTION
```

### Temperature Converter Function

```
FUNCTION temp_converter():
    DISPLAY menu for temperature options
    INPUT user choice
    
    IF choice == "1":
        INPUT celsius value as FLOAT
        CALCULATE fahrenheit = celsius * 9/5 + 32
        DISPLAY converted value (rounded to 2 decimal places)
    ELSE IF choice == "2":
        INPUT fahrenheit value as FLOAT
        CALCULATE celsius = (fahrenheit - 32) * 5/9
        DISPLAY converted value (rounded to 2 decimal places)
    ELSE:
        DISPLAY error message
    END IF
END FUNCTION
```

### Length Converter Function

```
FUNCTION length_stuff():
    DISPLAY menu for length options
    INPUT user choice
    
    IF choice == "1":
        INPUT kilometers as FLOAT
        CALCULATE meters = kilometers * 1000
        DISPLAY result
    ELSE IF choice == "2":
        INPUT meters as FLOAT
        CALCULATE kilometers = meters / 1000
        DISPLAY result
    ELSE:
        DISPLAY error message
    END IF
END FUNCTION
```

### Weight Converter Function

```
FUNCTION weight_converter():
    DISPLAY menu for weight options
    INPUT user choice
    
    IF choice == "1":
        INPUT kilograms as FLOAT
        CALCULATE grams = kilograms * 1000
        DISPLAY result
    ELSE IF choice == "2":
        INPUT grams as FLOAT
        CALCULATE kilograms = grams / 1000
        DISPLAY result
    ELSE:
        DISPLAY error message
    END IF
END FUNCTION
```

---

## Flowchart

```
START
  |
  v
DISPLAY Welcome Message
  |
  v
WHILE NOT (exit condition)
  |
  +---> DISPLAY Main Menu
  |
  +---> INPUT User Choice
  |
  +---> [Decision: Which option?]
        |
        +---> [Option 1: Temperature]
        |     |
        |     +---> DISPLAY Temp Menu
        |     |
        |     +---> [C to F / F to C]
        |     |
        |     +---> PERFORM Conversion
        |     |
        |     +---> DISPLAY Result
        |
        +---> [Option 2: Length]
        |     |
        |     +---> DISPLAY Length Menu
        |     |
        |     +---> [KM to M / M to KM]
        |     |
        |     +---> PERFORM Conversion
        |     |
        |     +---> DISPLAY Result
        |
        +---> [Option 3: Weight]
        |     |
        |     +---> DISPLAY Weight Menu
        |     |
        |     +---> [KG to G / G to KG]
        |     |
        |     +---> PERFORM Conversion
        |     |
        |     +---> DISPLAY Result
        |
        +---> [Option 4: Quit]
        |     |
        |     +---> DISPLAY Goodbye
        |     |
        |     +---> EXIT Loop
        |
        +---> [Invalid Option]
              |
              +---> DISPLAY Error Message
  |
  v
END
```

---

## How to Run

### Step 1: Save the Code
Save the provided code as `converter.py` in your desired directory.

### Step 2: Open Terminal/Command Prompt
Navigate to the directory containing `converter.py`:

```bash
cd /path/to/your/project
```

### Step 3: Execute the Program
```bash
python converter.py
```

### Step 4: Interact with the Application
Follow the on-screen prompts and enter your choices.

### Step 5: Exit the Program
Type `4`, `quit`, `exit`, `bye`, or `q` when prompted, then press Enter.

---

## Example Output

```
Guys welcome to my unit Converter

o=o=o=o=o=o=o=o=o=o=o=o
1 temp
2 length
3 weight
4 quit
o=o=o=o=o=o=o=o=o=o=o=o

what do u want > 1

Temperature converter
1 - Celsius to Fahrenheit
2 - Fahrenheit to Celsius


pick 1 or 2: 1
celsius ? 25
25.0 °C is 77.0 °F

o=o=o=o=o=o=o=o=o=o=o=o
1 temp
2 length
3 weight
4 quit
o=o=o=o=o=o=o=o=o=o=o=o

what do u want > 2

Length converter
1. Kilometers to meters
2. meters to Kilometers
choose: 1
how many km ? 5
5.0 km = 5000.0 meters

o=o=o=o=o=o=o=o=o=o=o=o
1 temp
2 length
3 weight
4 quit
o=o=o=o=o=o=o=o=o=o=o=o

what do u want > 4
bye bye
```

---

## Future Enhancements

### Potential Features to Add

1. **Additional Conversion Categories**
   - Speed (km/h to m/s, mph to knots, etc.)
   - Volume (liters to milliliters, gallons to liters, etc.)
   - Energy (joules to calories, BTU to kWh, etc.)

2. **User Interface Improvements**
   - GUI implementation using Tkinter or PyQt
   - Graphical display of conversion ratios
   - History of recent conversions

3. **Functionality Enhancements**
   - Batch conversion support
   - Save/load conversion history
   - Custom unit definitions
   - Multi-language support

4. **Technical Improvements**
   - Implement unit conversion using a dictionary/database
   - Add logging functionality
   - Create unit test cases
   - Add docstrings to functions

5. **Performance Optimization**
   - Centralized conversion factors management
   - Reduced code duplication through refactoring

---

## Troubleshooting

### Issue: "Python command not found"
**Solution:** Ensure Python is installed and added to your system's PATH. Download from [python.org](https://www.python.org)

### Issue: Program crashes with "ValueError"
**Solution:** This occurs when you enter non-numeric values in a conversion prompt. Always enter valid numbers for temperature, length, and weight values.

### Issue: Invalid input message appears repeatedly
**Solution:** Ensure you're entering `1`, `2`, `3`, `4`, or their keyword equivalents exactly as shown in the menu.

### Issue: Temperature conversion gives unexpected results
**Solution:** Verify you're entering the correct option (1 for C→F, 2 for F→C) and entering numeric values only.

---

## Learning Outcomes

This project demonstrates proficiency in:

- **Python Fundamentals:** Functions, conditionals, loops, and type conversion
- **User Input Handling:** Accepting and validating user input
- **Control Flow:** Menu-driven programming with branching logic
- **Problem Solving:** Breaking down conversion logic into manageable functions
- **Code Organization:** Modular function design and separation of concerns
- **Mathematical Implementation:** Implementing real-world conversion formulas

---

## Additional Notes

- The application uses `.lower().strip()` methods for flexible input handling
- Temperature values are rounded to 2 decimal places for readability
- Length and weight conversions maintain precision as per mathematical calculation
- The program runs indefinitely until the user explicitly selects the exit option

---

**Last Updated:** November 25, 2025  
**Project Status:** Complete
