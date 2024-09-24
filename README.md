# Domain Checker

This project is a **Domain Checker** tool that checks a list of domains against a list of valid domains stored in a CSV file. It then outputs the verification results to an Excel file with invalid domains highlighted in red.

## Features
- Reads domains from a text file (`domains.txt`).
- Checks each domain against a pre-defined list of valid domains in `free-domains-2.csv`.
- Outputs results to `domains-output.xlsx` with invalid domains highlighted.
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
pip install pandas requests XlsxWriter