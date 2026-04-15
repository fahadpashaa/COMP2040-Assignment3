# Los Angeles Crime Data Analysis

## Project Overview
This project analyzes crime data from the City of Los Angeles. The goal is to load the dataset, explore its structure, clean it thoroughly, and prepare it for deeper analysis and visualizations. All work is done in a structured Jupyter notebook with clear sections and documented decisions.

## Dataset
The dataset contains detailed crime reports, including:
- Dates of occurrence and reporting
- Crime codes and descriptions
- Victim information
- Location coordinates
- Status codes
- Premise codes

The raw CSV required several cleaning steps before it could be used for analysis.

## Work Completed So Far

### 1. Initial Exploration
- Loaded the dataset into a pandas DataFrame.
- Reviewed the shape, column names, and basic structure.
- Wrote initial observations about patterns and issues in the data.
- Created analytical questions to guide the rest of the project.

### 2. Data Cleaning
A step-by-step cleaning process was completed to make the dataset consistent and usable.

#### 2.1 Fixing Invalid Ages
- Removed rows where the victim age was not realistic (negative values or extremely large numbers).

#### 2.2 Removing Invalid Longitude Values
- Dropped rows where longitude was `0`, since that is not a valid coordinate for Los Angeles.

#### 2.3 Dropping Empty Columns
- Removed `Crm Cd 2`, `Crm Cd 3`, and `Crm Cd 4` because they were almost entirely empty and provided no analytical value.

#### 2.4 Converting Date Columns
- Converted `Date Rptd` and `DATE OCC` into proper datetime format.
- Added a note explaining the parser warning and why no manual format specification was needed.

#### 2.5 Handling Missing Values
- Filled missing `Premis Cd` with `-1` to keep the column numeric and avoid dropping rows.
- Filled missing `Status` with `"UNKNOWN"` to keep the column readable and consistent.
- Added a short explanation about why different placeholders were used for numeric vs. text columns.

## Current Status
The dataset is now fully cleaned and ready for analysis. All major issues—invalid coordinates, empty columns, inconsistent dates, and missing values—have been addressed.

## Next Steps
The next phase will focus on:
- Creating a helper module (`helpers.py`)
- Building reusable functions
- Starting the analysis section
- Generating visualizations and insights

