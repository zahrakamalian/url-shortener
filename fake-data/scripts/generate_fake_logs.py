from faker import Faker
import csv
import random

fake = Faker()

ROWS = 3_000_000

with open(
    "fake-data/data/logs.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "url_id",
        "clicked_at",
        "ip_address"
    ])

    for _ in range(ROWS):

        writer.writerow([
            random.randint(1, 1_000_000),
            fake.date_time_this_year(),
            fake.ipv4()
        ])

print("Done!")
