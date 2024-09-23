import pandas as pd

def fetch_valid_domains_from_csv(csv_file):
    # Read the CSV file without headers
    df = pd.read_csv(csv_file, header=None)
    # Convert the single column to a set of domains
    return set(df[0].str.strip())

def check_domains(input_file, valid_domains):
    with open(input_file, 'r') as file:
        domains = file.read().splitlines()

    results = []

    for domain in domains:
        if domain.strip():  # Check if the domain line is not empty
            is_valid = domain in valid_domains
            results.append({'domain': domain, 'isValid': is_valid})

    return results

def save_to_excel(data, output_file):
    df = pd.DataFrame(data)
    
    # Create a Pandas Excel writer using XlsxWriter as the engine
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Domains')

        # Get the xlsxwriter workbook and worksheet objects
        workbook = writer.book
        worksheet = writer.sheets['Domains']

        # Define a format for invalid cells
        invalid_format = workbook.add_format({'bg_color': 'red', 'font_color': 'white'})

        # Highlight the cells in the 'isValid' column that are False
        for row_num, is_valid in enumerate(df['isValid']):
            if not is_valid:
                worksheet.write(row_num + 1, 1, is_valid, invalid_format)  # +1 to skip header row

if __name__ == "__main__":
    csv_file = 'free-domains-2.csv'  # The CSV file containing valid domains
    valid_domains = fetch_valid_domains_from_csv(csv_file)
     
    # The txt file containing the domains you want to check
    results = check_domains('domains.txt', valid_domains)
    
    # Results are saved on excel file
    save_to_excel(results, 'domains-output.xlsx')
