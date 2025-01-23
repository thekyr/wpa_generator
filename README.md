# Wi-Fi QR Code Generator

This script generates a Wi-Fi QR code that can be scanned by mobile devices to quickly connect to a wireless network. The QR code is saved as an image file and printed in Console during script execution. It can also be customized for different Wi-Fi security protocols, password complexities, and lengths.

---

## Features
- Generate a random Wi-Fi password (PSK) with customizable length and complexity.
- Specify the Wi-Fi security type (WPA, WPA2, WPA3).
- Save the QR code as an image file named `<SSID>_qrcode.png`.
- Defaults to WPA2 security and a 32-character alphanumeric password if no options are provided.

---

## Requirements
- Python 3.10 or later
- Install the required libraries using pip:
  ```bash
  pip install qrcode
  ```

---

## Usage
### Running the Script
Script argumentsto customize the QR code generation. Below are the details:

### Arguments
1. **Required**:
   - `wifi_ssid`: The SSID (name) of the Wi-Fi network.
     ```bash
     python generate_wifi_qr.py <wifi_ssid>
     ```

2. **Optional**:
   - `--psk_length`: Length of the Wi-Fi password (default is `32`). Must be between `8` and `63`.
     ```bash
     python generate_wifi_qr.py <wifi_ssid> --psk_length 16
     ```

   - `--complexity`: Define the complexity of the password. Options:
     - `alphanumeric` (default): Letters and digits.
     - `letters`: Letters only (uppercase and lowercase).
     - `digits`: Digits only.
     - `complex`: Includes letters, digits, and special characters.
     ```bash
     python generate_wifi_qr.py <wifi_ssid> --complexity complex
     ```

   - `--security`: Define the Wi-Fi security type. Options:
     - `WPA` (default if not specified).
     - `WPA2`: Modern WPA2 security.
     - `WPA3`: Latest WPA3 security standard.
     ```bash
     python generate_wifi_qr.py <wifi_ssid> --security WPA3
     ```

### Examples
#### Generate a QR Code with Default Settings (WPA2, 32-character alphanumeric password):
```bash
python generate_wifi_qr.py MyNetworkSSID
```

#### Generate a QR Code with a 16-character password and WPA3 security:
```bash
python generate_wifi_qr.py MyNetworkSSID --psk_length 16 --security WPA3
```

#### Generate a QR Code with a digits-only password:
```bash
python generate_wifi_qr.py MyNetworkSSID --complexity digits
```

---

## Output
1. **Password**:
   - The script will display the generated password (PSK) in the terminal.

2. **QR Code Image**:
   - The QR code is saved in the current working directory with the filename `<SSID>_qrcode.png`.

Example output for `MyNetworkSSID`:
```plaintext
Generated PSK: AbC123dEfGhI456JkLmNo789PqRsTUVW
QR code saved as: MyNetworkSSID_qrcode.png
```

---

## Notes
- Ensure the Wi-Fi security type (`WPA`, `WPA2`, or `WPA3`) matches your router's configuration.
- Password length must be between `8` and `63` characters.
- Special characters in the SSID will be preserved but ensure they are valid for filenames.

---

## License
This script is open-source and available under the MIT License. Feel free to modify and use it as needed.

