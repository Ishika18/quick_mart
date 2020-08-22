import cv2
import requests
import pyzbar.pyzbar as pyzbar
from cv2.cv2 import destroyWindow


def find_labels(user_profile) -> list:
    """
    Find labels selected by current user.

    :return: list of selected labels.
    """
    return list(user_profile.diet_restrictions)


def match_labels(user_labels: set, barcode: bytes) -> dict or None:
    """
    Check if users label match the food product.

    :param user_labels: list of labels chosen by the user.
    :param barcode: string representing scanned barcode.
    :return: True if labels match, else False.
    """
    api_key = '5662d0b86ebc4a9ba83d11e51856b339'
    upc = barcode.decode('utf-8')[1:]
    res = requests.get(f'https://api.spoonacular.com/food/products/upc/{upc}?apiKey={api_key}')
    if res.status_code == 200:
        try:
            inbuilt_labels = set(res.json()['badges'] + res.json()['importantBadges'])
            print(user_labels - inbuilt_labels)
            return {'unmatched_labels': user_labels - inbuilt_labels}
        except KeyError:
            return None


def scan_code(user_profile) -> set or None:
    """
    Scan the barcode and check user restrictions using helper functions.

    :param user_profile: profile of the current user.
    :return: set containing label requirements which are not met.
    """
    cap_device = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        _, frame = cap_device.read()

        decoded_objects = pyzbar.decode(frame)

        cv2.imshow("Frame", frame)

        cv2.waitKey(1)
        if decoded_objects:
            labels = set(find_labels(user_profile))
            destroyWindow("Frame")
            cap_device.release()
            return match_labels(labels, decoded_objects[0].data)
