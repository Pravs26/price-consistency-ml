session_prices = {}
def lock_price(user_id, product_id, price):
    key = f"{user_id}_{product_id}"
    session_prices[key] = price
def get_locked_price(user_id, product_id):
    key = f"{user_id}_{product_id}"
    return session_prices.get(key)
