
#### Generate random WPA pasword and QRCODE for SSID
import random
import string
import qrcode
import argparse

def generate_simple_psk(length=63):
    """
    Generate a random PSK.

    :param length: Length of the PSK.
    :return: Randomly generated PSK.
    """
    if not (8 <= length <= 63):
        raise ValueError("PSK length must be between 8 and 63 characters.")

#    # Use only letters and digits
#    characters = string.ascii_letters + string.digits

    # Define character sets based on complexity
    if complexity == "alphanumeric":
        characters = string.ascii_letters + string.digits
    elif complexity == "letters":
        characters = string.ascii_letters
    elif complexity == "digits":
        characters = string.digits
    elif complexity == "complex":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity. Choose from 'alphanumeric', 'letters', 'digits', or 'complex'.")

    # Generate a random PSK of the desired length
    psk = ''.join(random.choice(characters) for _ in range(length))
    return psk

def create_wifi_qr(ssid, psk, security_type="WPA"):
    """
    Create a QR code for a Wi-Fi network.

    :param ssid: Wi-Fi SSID.
    :param psk: Wi-Fi password (PSK).
    :param security_type: Security type (default is WPA).
    :param filename: File name to save the QR code image.
    """
    # Construct Wi-Fi QR code data
    qr_data = f"WIFI:S:{ssid};T:{security_type};P:{psk};;"
    
    # Generate QR code
    qr = qrcode.make(qr_data)

    # Save the QR code as an image file
    filename = f"{ssid}_qrcode.png"
    qr.save(filename)
    print(f"QR code saved as {filename}")

def display_qr_in_terminal(data):
    """
    Display the QR code in the terminal.
    :param data: Data to encode in the QR code.
    """
    qr = qrcode.QRCode(border=2)
    qr.add_data(data)
    qr.make(fit=True)

    # Print the QR code as ASCII
    qr.print_ascii(invert=True)  # Inverts colors for better terminal visibility

# Example usage
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a Wi-Fi QR code.")
    parser.add_argument("wifi_ssid", type=str, help="The SSID of the Wi-Fi network.")
    parser.add_argument("--psk_length", type=int, default=32, help="Length of the Wi-Fi password (default is 32) max lengh is 63.")
    parser.add_argument("--complexity", type=str, default="alphanumeric",
                        choices=["alphanumeric", "letters", "digits", "complex"],
                        help="Password complexity (default is 'alphanumeric'). Options: 'alphanumeric', 'letters', 'digits', 'complex'.")
    parser.add_argument("--security", type=str, default="WPA2",
                        choices=["WPA", "WPA2", "WPA3"],
                        help="Wi-Fi security type (default is 'WPA2'). Options: 'WPA', 'WPA2', 'WPA3'.")


    # Parse the arguments
    args = parser.parse_args()

    # Get the SSID and password length
    wifi_ssid = args.wifi_ssid
    psk_length = args.psk_length
    complexity = args.complexity
    security = args.security

    # Generate the PSK
    psk = generate_simple_psk(psk_length)
    print(f"SSID name: {wifi_ssid}")
    print(f"Generated PSK: {psk}")

    # Create the QR code
    create_wifi_qr(wifi_ssid, psk)

    # Construct the Wi-Fi QR data
    wifi_qr_data = f"WIFI:S:{wifi_ssid};T:{security};P:{psk};;"

    # Display the QR code in the terminal
    print("\nScan the QR code below to connect to the Wi-Fi network:")
    display_qr_in_terminal(wifi_qr_data)
