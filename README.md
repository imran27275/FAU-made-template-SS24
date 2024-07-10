# Assessing the Effects of mountains show depth on air temperature

<img src="project\output.png" width="800" height="400">

## Project Overview

Climate change is a critical issue that affects the earth. This project aims to analyze air temperature data to understand their impacts on mountains snow. The project will explore how these changes influence snow depth in extreme weather events.

## Data Sources

- **Datasource 1: Air Temperature Data:**
  - Metadata URL: <https://data.gov/>
  - Data URL: <https://ndownloader.figshare.com/files/44334659>
  - Data Type: CSV

- **Datasource 2: Snow Depth Data:**
  - Metadata URL: <https://data.gov/>
  - Data URL: <https://ndownloader.figshare.com/files/44334722>
  - Data Type: CSV
  
## Tools and Technologies Used

- Data Analysis: Python (Pandas)
- Visualization: Matplotlib
- Version Control: Git, GitHub

## Installation and Usage

Instructions for setting up the project environment and running the analysis scripts.

```bash
# Clone the repository
git clone https://github.com/imran27275/FAU-made-template-SS24
```

## Data Pipeline and Testing

### Data Pipeline [here](project/pipeline.py)

Our project includes a pipeline that performs the following functions:
1. **Data Fetching**: Automatically retrieves two datasets from specified online sources.
2. **Data Transformation and Cleaning**: Applies a series of transformations and cleaning processes to ensure data quality and fix issues or errors in the datasets. Rename some column name.
3. **Data Loading**: The cleaned and transformed data is then loaded into a SQL database for further analysis and querying.

This pipeline ensures our data is up-to-date and maintains integrity for reliable analysis.

### Test Script [here](project/automated_testing.py)

We have developed a comprehensive test script to ensure the accuracy and efficiency of our data pipeline. The script includes tests for:

- Data fetching and loading processes.
- Data cleaning and transformation rules.
- Overall data integrity and consistency checks.

### Automated Workflow [here](.github/workflows/automated-testing-CI.yml)

To maintain the quality and reliability of our pipeline, we have set up an automated workflow using GitHub Actions. This workflow includes:

- Continuous Integration Tests: Runs our test script automatically every time there is a push to the main branch. This ensures that any new changes do not disrupt the pipeline's functionality.

This automated workflow helps in maintaining a robust and error-free data pipeline, ensuring the high quality of our project deliverables.

## How to Run the Data Pipeline and Tests

Provide detailed instructions on how to execute the data pipeline and run the test scripts. Include any necessary commands or steps to set up the environment.

```bash
# command to run the data pipeline
python pipeline.py

# command to execute the test script
python automated_testing.py
```

## Authors and Acknowledgment

This project was initiated and completed by Md Imran Hossain.

## Special Thanks to Our Tutors

I would like to extend my gratitude to our tutors **Philip Heltweg** and **Georg Schwarz** for their guidance and support throughout this project. Their expertise and insights have been instrumental in shaping my approach and methodologies. This project would not have been possible without their mentorship and encouragement.

## License

This project is licensed under the CC0-1 Universal License - see the [LICENSE](LICENSE) file for details.
