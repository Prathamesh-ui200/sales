def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):


    required_fields = {
        'TransactionID', 'Date', 'ProductID', 'ProductName',
        'Quantity', 'UnitPrice', 'CustomerID', 'Region'
    }

    total_input = len(transactions)
    invalid_count = 0
    valid_transactions = []

    for tx in transactions:
        try:
            if not required_fields.issubset(tx.keys()):
                invalid_count += 1
                continue

            if tx['Quantity'] <= 0 or tx['UnitPrice'] <= 0:
                invalid_count += 1
                continue

            if not tx['TransactionID'].startswith('T'):
                invalid_count += 1
                continue

            if not tx['ProductID'].startswith('P'):
                invalid_count += 1
                continue

            if not tx['CustomerID'].startswith('C'):
                invalid_count += 1
                continue

            valid_transactions.append(tx)

        except Exception:
            invalid_count += 1

    regions = sorted({tx['Region'] for tx in valid_transactions})
    amounts = [tx['Quantity'] * tx['UnitPrice'] for tx in valid_transactions]

    print("Available Regions:", regions)
    if amounts:
        print(f"Transaction Amount Range: {min(amounts)} - {max(amounts)}")

    filtered = valid_transactions
    filtered_by_region = 0
    filtered_by_amount = 0

    if region:
        before = len(filtered)
        filtered = [tx for tx in filtered if tx['Region'] == region]
        filtered_by_region = before - len(filtered)
        print(f"After region filter ({region}): {len(filtered)} records")

    if min_amount is not None or max_amount is not None:
        before = len(filtered)
        temp = []

        for tx in filtered:
            amount = tx['Quantity'] * tx['UnitPrice']

            if min_amount is not None and amount < min_amount:
                continue
            if max_amount is not None and amount > max_amount:
                continue

            temp.append(tx)

        filtered = temp
        filtered_by_amount = before - len(filtered)
        print(f"After amount filter: {len(filtered)} records")

    summary = {
        'total_input': total_input,
        'invalid': invalid_count,
        'filtered_by_region': filtered_by_region,
        'filtered_by_amount': filtered_by_amount,
        'final_count': len(filtered)
    }

    return filtered, invalid_count, summary
