from faker import Faker
import csv
import random
import string

fake = Faker()

ROWS = 1_000_000


def random_short_code():
    return "".join(
        random.choices(
            string.ascii_letters + string.digits,
            k=8
        )
    )


with open(
    "fake-data/data/urls.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "user_id",
        "campaign_id",
        "original_url",
        "short_code",
        "views"
    ])

    for _ in range(ROWS):

        writer.writerow([
            random.randint(1, 10000),
            random.randint(1, 200),
            fake.url(),
            random_short_code(),
            random.randint(0, 5000)
        ])

print("Done!")
