import phonenumbers
from phonenumbers import geocoder, carrier, PhoneNumberType


def get_number_type(number):
    number_type = phonenumbers.number_type(number)

    types = {
        PhoneNumberType.MOBILE: "MOBILE",
        PhoneNumberType.FIXED_LINE: "FIXED_LINE",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "FIXED_LINE_OR_MOBILE",
        PhoneNumberType.TOLL_FREE: "TOLL_FREE",
        PhoneNumberType.PREMIUM_RATE: "PREMIUM_RATE",
        PhoneNumberType.VOIP: "VOIP",
        PhoneNumberType.PAGER: "PAGER",
        PhoneNumberType.UAN: "UAN",
        PhoneNumberType.VOICEMAIL: "VOICEMAIL",
    }

    return types.get(number_type, "UNKNOWN")


def analyze_number(number):

    try:
        parsed = phonenumbers.parse(number, None)

        valid = phonenumbers.is_valid_number(parsed)
        possible = phonenumbers.is_possible_number(parsed)

        return {
            "valid": valid,
            "possible": possible,
            "country": geocoder.description_for_number(
                parsed, "en"
            ),
            "carrier": carrier.name_for_number(
                parsed, "en"
            ) or "Unknown",
            "type": get_number_type(parsed),
            "international": phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.INTERNATIONAL
            ),
            "e164": phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.E164
            )
        }

    except Exception as error:

        return {
            "error": str(error)
        }
