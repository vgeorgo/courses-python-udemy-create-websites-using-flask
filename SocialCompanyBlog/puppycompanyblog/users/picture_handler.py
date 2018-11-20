import os
from PIL import Image
from flask import url_for,current_app

def add_profile_pic(pic_upload,username):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    # saves profile picture as the name of the user
    storage_filename = str(username)+'.'+ext_type
    filepath = os.path.join(current_app.root_path,'static\profiles_pics',storage_filename)

    pic = Image.open(pic_upload)
    pic.thumbnail((200,200))
    pic.save(filepath)

    return storage_filename
