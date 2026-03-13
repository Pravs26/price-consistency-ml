price_history = {}
def check_price(product_id, predicted_price):
    if product_id in price_history:
        previous_price = price_history[product_id]
        if abs(predicted_price - previous_price) > 5:
            return False, previous_price
        return True, previous_price
    price_history[product_id] = predicted_price
    return True, predicted_price
