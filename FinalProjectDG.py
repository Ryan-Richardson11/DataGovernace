import pandas as pd
from openpyxl import Workbook

df = pd.read_excel('CustomerSurvey.xlsx', sheet_name='Andrew.data')

def gen_age():
    age_generalization = {
    (1, 10): '1-10',
    (11, 20): '11-20',
    (21, 30): '21-30',
    (31, 40): '31-40',
    (41, 50): '41-50',
    (51, 60): '51-60',
    (61, 70): '61-70',
    (71, 80): '71-80',
    (81, 90): '81-90',
    (91, 200): '91+'
}
    df['Age'] = df['Age'].apply(lambda x: next((v for k, v in age_generalization.items() if k[0] <= x <= k[1]), x))

def gen_income():
    income_generalization = {
    (0, 25): '0-25',
    (26, 50): '26-50',
    (51, 75): '51-75',
    (76, 100): '76-100',
    (101, 125): '101-125',
    (126, 150): '126-150',
    (151, 175): '151-175',
    (176, 200): '176-200',
    (201, 225): '201-225',
    (226, 1_000_000): '226+'
}
    df['HouseholdIncome'] = df['HouseholdIncome'].apply(lambda x: next((v for k, v in income_generalization.items() if k[0] <= x <= k[1]), x))

def gen_education():
    education_generalization = {
    (0, 12): '0-12',
    (12, 14): '12-14',
    (16, 18): '16-18',
    (19, 100): '19+'
}
    df['EducationYears'] = df['EducationYears'].apply(lambda x: next((v for k, v in education_generalization.items() if k[0] <= x <= k[1]), x))

def gen_townsize():
    townsize_generalization = {
    (0, 1): '0-1',
    (2, 4): '2-4',
    (5, 100): '5+'
}
    df['TownSize'] = df['TownSize'].apply(lambda x: next((v for k, v in townsize_generalization.items() if k[0] <= x <= k[1]), x))