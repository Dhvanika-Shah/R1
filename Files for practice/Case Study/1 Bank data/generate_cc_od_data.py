import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Number of customers
num_customers = 500

# Helper functions
def random_date(start_date, end_date):
    """Generate a random date between start_date and end_date."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def random_invalid_date():
    """Return either a valid date or an invalid one like '00/00/0000' or 'LMT NOT SET'."""
    return random.choices(
        ["00/00/0000", "LMT NOT SET", random_date(datetime(2020, 1, 1), datetime(2025, 3, 14)).strftime("%d/%m/%Y")],
        weights=[0.2, 0.1, 0.7], k=1
    )[0]

def random_risk_code():
    """Generate risk codes (0-8), with higher values being less common."""
    return random.choices(
        [0, 1, 2, 3, 4, 5, 6, 7, 8],
        weights=[0.5, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.03, 0.02], k=1
    )[0]

# Define data generation
data = {
    "ACCTNO": [],
    "ACCTDESC": [],
    "CUSTNUMBER": [],
    "CUSTNAME": [],
    "INTRATE": [],
    "LIMIT": [],
    "DP": [],
    "LMTEXPDT": [],
    "ACCTBAL": [],
    "UNCLRBAL": [],
    "IRREGAMT": [],
    "NEWIRAC": [],
    "OLDIRAC": [],
    "SANC_RENDT": [],
    "ARRCOND": [],
    "CURRENCY": [],
    "MAINTBR": [],
    "IRRGDT": [],
    "UNREALINT": [],
    "ACCRINT": [],
    "STRESS": [],
    "SMA_CODE": [],
    "RA": [],
    "RA_DATE": [],
    "WRITE_OFF_FLAG": [],
    "WRITE_OFF_AMT": [],
    "WRITE_OFF_DATE": [],
    "NULL2": [],
    "Column1": [],
    "_1": []
}

# Base data for generation
acct_desc_options = [
    "Eectronic Dealer Fin.Sch", "EB-MSME-CC-USUAL CREDIT D", "EB-MSME-CC-e-DFS",
    "MSME-OD-SECURED", "CC-AUTO FINANCE"
]

# Diverse customer names (first names, last names, and business suffixes)
first_names = [
    "Aarav", "Priya", "Rahul", "Anjali", "Vikram", "Sneha", "Karthik", "Pooja",
    "Aditya", "Neha", "Sanjay", "Riya", "Arjun", "Kavya", "Rohan", "Shreya",
    "James", "Emma", "Michael", "Sophia", "William", "Olivia", "David", "Isabella",
    "Amit", "Deepika", "Nikhil", "Swati", "Rakesh", "Meera", "Vivek", "Ananya"
]
last_names = [
    "Sharma", "Patel", "Singh", "Kumar", "Gupta", "Mehta", "Verma", "Reddy",
    "Nair", "Joshi", "Desai", "Rao", "Iyer", "Chopra", "Malhotra", "Bose",
    "Smith", "Johnson", "Brown", "Taylor", "Wilson", "Davis", "Clark", "Lewis",
    "Kapoor", "Thakur", "Pillai", "Menon", "Saxena", "Bhatia", "Dutta", "Ghosh"
]
business_suffixes = [
    "LLP", "PVT. LTD", "AUTOMOBILES", "EQUIPMENT AN", "INDUSTRIES", "CORP",
    "ENTERPRISES", "SOLUTIONS", "TRADERS", "MOTORS", "GROUP", "ASSOCIATES",
    "INC", "CO", "LTD", "AGENCY", "VENTURES", "SYSTEMS", "TECH", "GLOBAL"
]

sma_code_options = ["", "N", "SMA1", "SMA2", "NPA"]
currency = "INR"
current_date = datetime(2025, 3, 14)

# Generate data for 500 customers
for i in range(num_customers):
    # ACCTNO: Unique account number
    acctno = 30000000000 + random.randint(100000000, 999999999)
    data["ACCTNO"].append(acctno)

    # ACCTDESC: Account description
    data["ACCTDESC"].append(random.choice(acct_desc_options))

    # CUSTNUMBER: Customer number (introduce duplicates)
    custnumber = 80000000000 + random.randint(100000000, 999999999)
    if i % 50 == 0:  # Introduce duplicates every 50th customer
        custnumber = data["CUSTNUMBER"][i - 1] if i > 0 else custnumber
    data["CUSTNUMBER"].append(custnumber)

    # CUSTNAME: Customer name with variety (first name + last name + business suffix)
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    suffix = random.choice(business_suffixes)
    base_name = f"{first_name} {last_name} {suffix}"
    if i % 50 == 0 and i > 0:  # For duplicates, slightly modify the name
        base_name = data["CUSTNAME"][i - 1].split(" ")[0] + " " + data["CUSTNAME"][i - 1].split(" ")[1] + random.choice(["", " LTD", " INC", " GROUP"])
    data["CUSTNAME"].append(base_name)

    # INTRATE: Interest rate (some 0.0, some realistic)
    intrate = random.choices([0.0, round(random.uniform(8.0, 12.0), 2)], weights=[0.3, 0.7], k=1)[0]
    data["INTRATE"].append(intrate)

    # LIMIT: Sanctioned limit (10M to 100M)
    limit = random.randint(10000000, 100000000)
    data["LIMIT"].append(limit)

    # DP: Deposit amount (often equals LIMIT, an anomaly)
    dp = random.choices([limit, 0], weights=[0.8, 0.2], k=1)[0]
    data["DP"].append(dp)

    # LMTEXPDT: Limit expiry date (some expired, some invalid)
    lmtexpdt = random_invalid_date()
    data["LMTEXPDT"].append(lmtexpdt)

    # ACCTBAL: Account balance (some negative, some exceeding LIMIT)
    utilization = random.uniform(0.5, 1.2)  # 50% to 120% of LIMIT
    acctbal = limit * utilization * random.choice([-1, 1])  # Randomly negative or positive
    data["ACCTBAL"].append(round(acctbal, 2))

    # UNCLRBAL: Uncleared balance (mostly 0)
    data["UNCLRBAL"].append(0)

    # IRREGAMT: Irregular amount (mostly 0, some positive)
    irregamt = random.choices([0, random.uniform(10000, 500000)], weights=[0.7, 0.3], k=1)[0]
    data["IRREGAMT"].append(round(irregamt, 2))

    # NEWIRAC and OLDIRAC: Risk assessment codes
    newirac = random_risk_code()
    oldirac = random.choices([newirac, random_risk_code()], weights=[0.6, 0.4], k=1)[0]
    data["NEWIRAC"].append(newirac)
    data["OLDIRAC"].append(oldirac)

    # SANC_RENDT: Sanction and renewal date (combined as date)
    sanc_rendt = random_date(datetime(2020, 1, 1), datetime(2025, 3, 14)).strftime("%d/%m/%Y")
    data["SANC_RENDT"].append(sanc_rendt)

    # ARRCOND: Arrears condition (0 or 602-902 for "Yes")
    arrcond = random.choices([0, random.randint(602, 902)], weights=[0.7, 0.3], k=1)[0]
    data["ARRCOND"].append(arrcond)

    # CURRENCY: Always INR
    data["CURRENCY"].append(currency)

    # MAINTBR: Branch code (mostly 0, some valid)
    maintbr = random.choices([0, 10678, random.randint(10000, 20000)], weights=[0.6, 0.3, 0.1], k=1)[0]
    data["MAINTBR"].append(maintbr)

    # IRRGDT: Irregular date (mostly invalid)
    irrgdt = random_invalid_date()
    data["IRRGDT"].append(irrgdt)

    # UNREALINT and ACCRINT: Unrealized and accrued interest (mostly 0, some positive)
    unrealint = random.choices([0, random.uniform(10000, 100000)], weights=[0.8, 0.2], k=1)[0]
    accrint = random.choices([0, random.uniform(10000, 200000)], weights=[0.8, 0.2], k=1)[0]
    data["UNREALINT"].append(round(unrealint, 2))
    data["ACCRINT"].append(round(accrint, 2))

    # STRESS: Stress indicator (mostly blank or "N")
    stress = random.choices(["", "N", "Y"], weights=[0.5, 0.4, 0.1], k=1)[0]
    data["STRESS"].append(stress)

    # SMA_CODE: Special Mention Account code
    sma_code = random.choices(sma_code_options, weights=[0.4, 0.3, 0.1, 0.1, 0.1], k=1)[0]
    if newirac > 3:  # Higher risk accounts more likely to be NPA
        sma_code = random.choices(sma_code_options, weights=[0.1, 0.1, 0.2, 0.2, 0.4], k=1)[0]
    data["SMA_CODE"].append(sma_code)

    # RA: Risk assessment (blank or 1-9)
    ra = random.choices(["", random.randint(1, 9)], weights=[0.5, 0.5], k=1)[0]
    data["RA"].append(ra)

    # RA_DATE: Risk assessment date (some outdated, some invalid)
    ra_date = random.choices(
        ["00/00/0000", random_date(datetime(2020, 1, 1), datetime(2025, 3, 14)).strftime("%Y-%m-%d")],
        weights=[0.3, 0.7], k=1
    )[0]
    data["RA_DATE"].append(ra_date)

    # WRITE_OFF_FLAG, WRITE_OFF_AMT, WRITE_OFF_DATE: Write-off details (mostly "N" and 0)
    data["WRITE_OFF_FLAG"].append("N")
    data["WRITE_OFF_AMT"].append(0)
    data["WRITE_OFF_DATE"].append("00/00/0000")

    # NULL2, Column1, _1: Placeholder columns (mostly empty)
    data["NULL2"].append("")
    data["Column1"].append(random.choices(["", "STD"], weights=[0.9, 0.1], k=1)[0])
    data["_1"].append(random.choices(["", "0.0"], weights=[0.9, 0.1], k=1)[0])

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("synthetic_cc_od_data.csv", index=False)
print("Synthetic dataset generated and saved as 'synthetic_cc_od_data.csv'.")
