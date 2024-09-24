# Domain Checker

This project is a **Domain Checker** tool that checks a list of domains against a list of valid domains stored in a CSV file. It then outputs the verification results to an Excel file with invalid domains highlighted in red.

## Features

- Reads domains from a text file (`domains.txt`).
- Checks each domain against a pre-defined list of valid domains in `free-domains-2.csv`.
- Outputs results to `results.xlsx` with invalid domains highlighted.
- Uses Python libraries such as `pandas` and `xlsxwriter`.

## Domain List Source

The project leverages a list of free email domains provided by HubSpot as a reference for valid domains:

- **Source**: [HubSpot - Free Domains List](https://knowledge.hubspot.com/forms/what-domains-are-blocked-when-using-the-forms-email-domains-to-block-feature)
- **Last Updated**: August 2024

## Requirements

Make sure you have the following installed:

- Python 3.x
- Required Python packages: `pandas`, `xlsxwriter`

You can install the required libraries using:

```bash
pip install pandas XlsxWriter
```

## How to Use

1. **Clone or Download the Project and Prepare your Data**

   - Clone the repository:
     `bash 
     git clone https://github.com/evitadasy/domain-checker.git 
     `
     or Alternatively, download the project:
   - Go to the GitHub repository and click on "Code" > "Download ZIP".
   - Extract the ZIP file to your desired location.

   Make sure you have a text file that contains the domains you want to analyze.

2. **Run the script:**

   - Navigate to the project directory:
     ```bash
     cd domain-checker
     ```
   - Execute the script using Python:
     ```bash
     python domain_checker.py
     ```
   - Replace `domains.txt` with your actual input file path. The `results.xlsx` will be the output file where the results will be stored.

3. **Script Options:**

   - `--input`: Specifies the path to your input text file.
   - `--output`: Specifies the path where you want the output file to be saved (default is `results.xlsx`).

4. **Understanding the output:**
   - The script will create a CSV file (`results.xlsx`) containing all email addresses with a status indicating whether the domain is valid or invalid.
