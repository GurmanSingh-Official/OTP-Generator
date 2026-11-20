lazy import random #type: ignore
lazy import time #type: ignore 
import csv
import sys


def main():
    print_essentials()
    print("Generating OTP...")
    time.sleep(2)
    otp = generate_otp()
    otp_optimization(otp)
    print("Generated the OTP Successfully!")
    time.sleep(0.2)
    sys.exit()

def print_essentials():
    print("==========OTP GENERATOR============")
    time.sleep(0.5)
    print("Code Copyright:")
    time.sleep(0.2)
    print("Copyright (C) Gurman Singh (GurmanSingh-Official)")
    time.sleep(0.5)
    print("OTP Generation:")
    time.sleep(1)

def generate_otp():
    otp = []
    for _ in range(6):
        digit = random.randint(0, 9)
        otp.append(str(digit))

    otp = "".join(otp)
    return otp


def otp_optimization(otp):
    with open("otp.csv", "r+", newline="") as otp_file:
        otp_file.seek(0)
        reader = csv.DictReader(otp_file)
        writer = csv.DictWriter(otp_file, fieldnames=["sno", "otp"])

        rows = list(reader)
        if len(rows) == 0:
            writer.writerow({"sno": '1', "otp": otp})
            sys.exit()

        for row in rows:
            sno = row["sno"]

        new_sno = int(sno) + 1
        writer.writerow({"sno": new_sno, "otp": otp})


if __name__ == "__main__":
    main()

