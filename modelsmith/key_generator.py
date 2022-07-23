from django.utils.crypto import get_random_string

def get_key():

    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    key = get_random_string(50, chars)
    return str(key)