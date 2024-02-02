import requests

# create random person
def generate_person():
    url = "https://randomuser.me/api/?nat=us"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def extract_date(timestamp):
    from datetime import datetime

    # Convert the string to a datetime object
    dt_object = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))

    # Extract year, month, and date
    year = dt_object.year
    month = dt_object.month
    day = dt_object.day

    date = f"{month}/{day}/{year}"

    return date




if __name__ == "__main__":
    person = generate_person()
    
    print(person['results']) #gender, name['first', 'last'], location['street']['number', 'name'], location['city'], location['state'], location['postcode'], email, login['username', 'password'], dob['date', 'age'], registered['date', 'age'], phone, cell, id['name', 'value'], picture['large', 'medium', 'thumbnail'], nat
