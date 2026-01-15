def parse_transactions(raw_lines):


    transactions = []

    for line in raw_lines:
        parts = line.split('|')


        if len(parts) != 8:
            continue

        try:
            transaction_id = parts[0].strip()
            date = parts[1].strip()
            product_id = parts[2].strip()


            product_name = parts[3].replace(',', '').strip()

            quantity = int(parts[4].replace(',', '').strip())
            unit_price = float(parts[5].replace(',', '').strip())

            customer_id = parts[6].strip()
            region = parts[7].strip()

            transactions.append({
                'TransactionID': transaction_id,
                'Date': date,
                'ProductID': product_id,
                'ProductName': product_name,
                'Quantity': quantity,
                'UnitPrice': unit_price,
                'CustomerID': customer_id,
                'Region': region
            })

        except ValueError:
            continue

    return transactions
