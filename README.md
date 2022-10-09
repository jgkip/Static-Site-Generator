## Overview 

A static site generator implemented in Python. 

## What is a static site generator?

A static site generator constructs static webpages from some input data. This SSG takes markdown files as that input. 

## Usage 

Due to its simplicity, this generator should only be used to create blogs and very basic websites (if that's your jam). 

This SSG takes a directory of markdown files and constructs their corresponding HTML. 

**To use:**

- Input files should be in their own directory i.e. 'tests' or name of your choice
  **NOTE:** `tests` in the filepath specified in `main.py` should be changed if you use a different directory 
- cd into `src` and run `python main.py`
- Resulting HTML will be pushed to output folder 
