import csv
from collections import Counter

FILE = "/var/log/asterisk/cdr-csv/Master.csv"

def branch(number):
    if number in ("1001", "1002", "1003"):
        return "Dhaka"
    elif number in ("2001", "2002"):
        return "Chattogram"
    elif number in ("3001", "3002"):
        return "Sylhet"
    return "Service"

with open(FILE, newline="") as file:
    records = [r for r in csv.reader(file) if len(r) >= 17]

print("=" * 110)
print("NOVACONNECT ENTERPRISE - CDR REPORT")
print("=" * 110)

print(f"{'Caller':<8}{'Receiver':<10}"
      f"{'From':<13}{'To':<13}"
      f"{'Start Time':<22}{'Duration':<10}"
      f"{'Billsec':<10}{'Status':<14}")

print("-" * 110)

for r in records[-20:]:
    print(f"{r[1]:<8}{r[2]:<10}"
          f"{branch(r[1]):<13}{branch(r[2]):<13}"
          f"{r[9]:<22}{r[12]:<10}"
          f"{r[13]:<10}{r[14]:<14}")

stats = Counter(r[14] for r in records)

print("=" * 110)
print("CDR SUMMARY")
print("Total Records :", len(records))
print("Answered      :", stats["ANSWERED"])
print("Busy          :", stats["BUSY"])
print("No Answer     :", stats["NO ANSWER"])
print("Failed        :", stats["FAILED"])
print("Congestion    :", stats["CONGESTION"])
print("=" * 110)
