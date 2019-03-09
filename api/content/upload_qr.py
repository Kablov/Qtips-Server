import cloudinary.uploader


def upload_qr(photo, phone):
    path = "profile/" + str(phone) + "/qr"
    cloudinary_photo = cloudinary.uploader.upload_resource(photo, public_id = path)
    url = cloudinary_photo.url
    secure_url = str(url).replace("http", "https")
    return secure_url
