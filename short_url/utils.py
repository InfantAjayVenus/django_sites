from nanoid import generate


def get_random_id(size=5):
    ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#'
    
    return generate(ALPHABET, size)