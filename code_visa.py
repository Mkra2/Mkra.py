import requests
import jso
# WESTON
def generate_combo(bin):
  
    
    api_endpoint = 'https://api.stripe.com/v1/issuing/cards'

    
    api_key = 'your_api_key_here'

    
    headers = {
      'Authorization': 'Bearer ' + api_key,
      'Stripe-Account': 'your_stripe_account_id_here',
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    
    data = {
      'type': 'physical',
      'billing[address][line1]': '',
      'billing[address][city]': '',
      'billing[address][state]': '',
      'billing[address][postal_code]': '',
      'billing[address][country]': '',
      'currency': 'usd',
      'spending_controls[allowed_categories][0][is_whitelisted]': True,
      'spending_controls[allowed_categories][0][spending_limits][interval_unit]': 'all_time',
      'spending_controls[allowed_categories][0][spending_limits][amount]': 50000,
      'spending_controls[allowed_categories][1][is_whitelisted]': True,
      'spending_controls[allowed_categories][1][spending_limits][interval_unit]': 'all_time',
      'spending_controls[allowed_categories][1][spending_limits][amount]': 50000,
      'spending_controls[spending_limits_window]:': 'rolling_window'
    }

    
    data['card[request_three_d_secure]'] = 'no_preference'
    data['card[number]'] = bin
    data['card[expiration_month]'] = '12'
    data['card[expiration_year]'] = '2025'

    
    response = requests.post(api_endpoint, data=data, headers=headers)

    
    if response.status_code == 200:
        response_data = json.loads(response.text)
        card_number = response_data['number']
        card_expiry_month = response_data['exp_month']
        card_expiry_year = response_data['exp_year']
        card_cvc = response_data['cvc']
        combo = f"{card_number}|{card_expiry_month}|{card_expiry_year}|{card_cvc}"
        return combo
    else:
        return None
  

bin = '482857'
combo = generate_combo(bin)
print(combo)
