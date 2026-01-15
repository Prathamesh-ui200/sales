def read_sales_data(df):
    encodings = ['utf-8', 'latin-1', 'cp1252']

    for encoding in encodings:
        try:
            with open(df, 'r', encoding=encoding) as file:
                lines = file.readlines()
                return [line.strip() for line in lines[1:] if line.strip()]
        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"Error: File '{df}' not found.")
            return []

    print("Error: Unable to read file with supported encodings.")
    return []
