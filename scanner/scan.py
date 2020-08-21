import cv2
import requests
import pyzbar.pyzbar as pyzbar
from cv2.cv2 import destroyWindow


def find_labels(user_profile) -> list:
    """
    Find labels selected by current user.

    :return: list of selected labels
    """
    return list(user_profile.diet_restrictions)


def match_labels(labels: list, barcode: str) -> bool:
    """
    Check if users label match the food product.

    :param labels: list of labels
    :param barcode: string representing scanned barcode
    :return: True if labels match, else False
    """
    res = requests.get(f'https://api.edamam.com/api/food-database/v2/parser?upc={barcode}&'
                       'app_id=f2514fb9&app_key=f2b0522e8674bf0ab1ec55bb2d7f99cb')
    if res.status_code != 200:
        print("cry")
    print(res.json())
    print(labels)
    pass


def scan_code(user_profile):
    """
    Scan the barcode and check user restrictions using helper functions.
    """
    cap_device = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        _, frame = cap_device.read()

        decoded_objects = pyzbar.decode(frame)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if decoded_objects:
            labels = find_labels(user_profile)
            match_labels(labels, decoded_objects[0].data)
            print(decoded_objects[0].data)
            destroyWindow("Frame")
            cap_device.release()
            break
