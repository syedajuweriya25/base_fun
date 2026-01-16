# Base_converter

## Overview
user can give any number in any base(upto 36), specify its original base and desired target base, and it converts seamlessly.

## Features
1. It converts a number of any base may it be **positive or negative** to user desired base.
2. It handles invalid bases 1 and zero by exiting with an error message.
3. It handles bases above 36 by exiting with an error message specifying the range of base.
4. Program completes after each conversion.
5. Clear understandable prompts.

## Tech Stack
**Language:** Python 3.9.2 </br>
**Modules:** Built in python library 'sys' </br>
**Environment:** Standard command line/terminal

## Project Structure
### base_converter.py
It contains 4 self defined functions
+ main function
+ to_b10 function
+ base_digits function
+ base_conversion

## How It Works
1. main function maintains the order in which program proceeds.
2. to_b10 function converts the number to base 10 and handles all errors.
3. base_digits returns the list of digits that is present in the form of number in the desired base.
4. base_conversion function maps and encodes and returns the final answer.

## Installation and Usage
**Installation:** No installation required. </br>
**Usage:** To use run **python base_converter.py** in the terminal.

## Applications
1. Binary or Hexadecimal conversions are essential for memory addressing, MAC addresses and IP configuration.
2. Understanding memory dumps and stack traces while debugging requires base conversions.
3. Useful during encryption as cryptographic systems use different number bases.
4. Base conversions are required in data packet headers and protocol analysis.

## What I Learned
1. Learnt base conversion logic, mapping and encoding logic.
2. The relation between floor division and modulo operator and their usage in base conversions.
3. Translation base conversion logic (mathematical logic) into working code.
4. Clean error handling.
5. Testing and looking for edge cases.

## Future Modifications
### Feature Additions
+ **Session persistence:** Allow multiple conversions without ending.
+ **History features:** Track previous conversions during session.
+ **Step by step conversion:** Show detailed conversion process for learning.
### Extension of Project
+ Unit test file
+ A fun base converter which allow users to select mapping characters(like emojis, special characters etc)
+ Extended base support upto 64 bases

## Contribution
Contributions are welcomed to enhance Base Converter

### How To Contribute
1. **Describe issue or new features:** clear description, steps and comparison.
2. **Make code changes:** fork the repository, create a new branch, make changes, test thoroughly and commit with clear message.
3. **Submit a pull request**



