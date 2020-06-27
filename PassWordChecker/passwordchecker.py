import requests
import hashlib


# The pwnedpasswords API receives only the first 5 characters of a hached password and return a text list.
def request_api_data(query_parameter):
    url_api = 'https://api.pwnedpasswords.com/range/' + query_parameter
    response = requests.get(url_api)
    if response.status_code != 200:
        raise RuntimeError(f'It was an error on the API: {response.status_code}. Please check and try again later...')
    return response


def password_checker(password):
    hashed_password = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()  # password converted to hash and in uppercase
    reduced_hashed_password = hashed_password[0:5]  # Take the first 5 characters of the hashed password
    response_api_data = request_api_data(reduced_hashed_password)
    # The response_api_data is a text with a new line between each item. Splitlines creates a list where each item is
    # a new line
    passwords_list = response_api_data.text.splitlines()
    for item in passwords_list:
        password_item = item.split(':')
        entire_password = reduced_hashed_password + password_item[0]
        if entire_password == hashed_password:
            return f'This password was PWNED {password_item[1]} times...'
    return 'This password was never PWNED!!!'


input_password = input('Insert the password to be checked: ')
result = password_checker(input_password)
print(result)
