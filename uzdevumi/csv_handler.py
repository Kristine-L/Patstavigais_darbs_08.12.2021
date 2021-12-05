import csv

from .models import User


def read_and_decode_csv(csv_file, encoding='utf-8'):

    decoded_file = csv_file.read().decode(encoding).splitlines()
    return decoded_file


def create_user_from_csv_row(csv_row):

    user = User(
        username=csv_row['username'],
        e_mail=csv_row['e_mail'],
    )

    user.save()


def user_csv_rows_to_db(decoded_csv_file):

    csv_reader = csv.DictReader(decoded_csv_file)

    for row in csv_reader:
        create_user_from_csv_row(row)

    © 2021 GitHub, Inc.
    Terms
    Privacy
    Security
