def calculate_total_revenue(transactions):

    total = 0.0
    for t in transactions:
        total += t['Quantity'] * t['UnitPrice']
    return total


def region_wise_sales(transactions):
    """
    Analyzes sales by region
    """
    region_data = {}
    grand_total = 0.0

    for t in transactions:
        region = t['Region']
        sales = t['Quantity'] * t['UnitPrice']
        grand_total += sales

        if region not in region_data:
            region_data[region] = {
                'total_sales': 0.0,
                'transaction_count': 0
            }

        region_data[region]['total_sales'] += sales
        region_data[region]['transaction_count'] += 1

    for region in region_data:
        region_data[region]['percentage'] = round(
            (region_data[region]['total_sales'] / grand_total) * 100, 2
        )

    return dict(
        sorted(
            region_data.items(),
            key=lambda x: x[1]['total_sales'],
            reverse=True
        )
    )
