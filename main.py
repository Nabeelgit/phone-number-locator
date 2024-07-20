import phonenumbers
from phonenumbers import geocoder, PhoneNumberFormat, NumberParseException

def get_phone_number_location(country_code, phone_number):
    full_phone_number = country_code + phone_number
    try:
        # Parse the full phone number
        parsed_number = phonenumbers.parse(full_phone_number)
        
        # Validate the phone number
        if not phonenumbers.is_valid_number(parsed_number):
            return "Invalid phone number"
        
        # Get the location of the phone number
        location = geocoder.description_for_number(parsed_number, "en")
        return f"The phone number {full_phone_number} is located in: {location}"
    except NumberParseException:
        return "Error parsing the phone number. Please check the format."

# User input
country_code = input("Enter the country code (include +): ")
phone_number = input("Enter the phone number: ")

# Get location
result = get_phone_number_location(country_code, phone_number)
print(result)
