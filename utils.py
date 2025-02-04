from datetime import datetime
import math

def calculate_points(receipt):
    points = 0

    # 1. One point for every alphanumeric character in the retailer name
    retailer = receipt.get('retailer', '')
    points += sum(c.isalnum() for c in retailer)

    # 2. 50 points if total is a round dollar amount
    total = float(receipt.get('total', 0))
    if total.is_integer():
        points += 50

    # 3. 25 points if total is a multiple of 0.25
    if (total * 100) % 25 == 0:
        points += 25

    # 4. 5 points for every two items on the receipt
    items = receipt.get('items', [])
    points += (len(items) // 2) * 5

    # 5. Item description length multiple of 3
    for item in items:
        description = item.get('shortDescription', '').strip()
        if len(description) % 3 == 0:
            price = float(item.get('price', 0))
            points += math.ceil(price * 0.2)

    # 6. 6 points if purchase day is odd
    purchase_date = receipt.get('purchaseDate', '')
    if purchase_date:
        date_obj = datetime.strptime(purchase_date, '%Y-%m-%d')
        if date_obj.day % 2 != 0:
            points += 6

    # 7. 10 points if purchase time is between 2:00 PM and 4:00 PM
    purchase_time = receipt.get('purchaseTime', '')
    if purchase_time:
        time_obj = datetime.strptime(purchase_time, '%H:%M')
        if 14 <= time_obj.hour < 16:
            points += 10

    return points
