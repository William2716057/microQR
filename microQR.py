import qrcode
from PIL import Image

def generate_tiny_qr(data, box_size=1, border=0):
    # Create a QR Code object with the specified box size and border
    qr = qrcode.QRCode(
        version=1,  # Version of the QR code, 1 is the smallest
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save("qrcode.png")



# Example usage
generate_tiny_qr("message to be store ")