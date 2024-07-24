import qrcode
from PIL import Image

def generate_tiny_qr(data, box_size=1, border=0):
    # Split data into chunks of 16 characters each
    chunks = [data[i:i + 16] for i in range(0, len(data), 16)]

    for index, chunk in enumerate(chunks):
        # Create a QR Code object with the specified box size and border for each chunk
        qr = qrcode.QRCode(
            version=1,  # Version of the QR code, 1 is the smallest
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        qr.add_data(chunk)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image with a unique name
        img.save(f"qrcode_{index}.png")

# Example usage
generate_tiny_qr("This is a long message that needs to be split into multiple QR codes.")