## Overview 

A static site generator implemented in Python. 

## What is a static site generator?

A static site generator constructs static webpages from some input data. This SSG takes markdown files as that input. 

## Usage 

Due to its simplicity, this generator should only be used to create blogs and very basic websites (if that's your jam). 

This SSG takes a directory of markdown files (they should be related) and constructs HTML that links them together as a website.

**To use:**

- Input files should be in their own directory i.e. 'tests' or name of your choice
  **NOTE:** 'tests' in the filepath specified in main.py should be changed if you use a different directory 
- Use python main.py to run 
- Resulting HTML will be pushed to output folder 
