import pandas as pd

df = pd.read_excel('Merr.Customer.Survey (2).xlsx', sheet_name='Andrew.data')

class GeneralizeData:
    def gen_age(self):
        age_generalization = {
        (1, 10): '1-10',
        (11, 20): '11-20',
        (21, 30): '21-30',
        (31, 40): '31-40',
        (41, 50): '41-50',
        (51, 60): '51-60',
        (61, 70): '61-70',
        (71, 80): '71-80',
        (81, 90): '81-90'
    }
        df['Age'] = df['Age'].apply(lambda x: next((v for k, v in age_generalization.items() if k[0] <= x <= k[1]), 'Null' if x > 90 else x))

    def gen_income(self):
        income_generalization = {
        (0, 25): '0-25',
        (26, 50): '26-50',
        (51, 75): '51-75',
        (76, 100): '76-100',
        (101, 125): '101-125',
        (126, 150): '126-150',
        (151, 175): '151-175',
        (176, 200): '176-200',
        (201, 225): '201-225'
    }
        df['HouseholdIncome'] = df['HouseholdIncome'].apply(lambda x: next((v for k, v in income_generalization.items() if k[0] <= x <= k[1]), 'Null' if x > 225 else x))

    def gen_education(self):
        education_generalization = {
        (0, 12): '0-12',
        (12, 14): '12-14',
        (16, 19): '16-19'
    }
        df['EducationYears'] = df['EducationYears'].apply(lambda x: next((v for k, v in education_generalization.items() if k[0] <= x <= k[1]), 'Null' if x > 20 else x))

    def gen_townsize(self):
        townsize_generalization = {
        (0, 1): '0-1',
        (2, 3): '2-3',
        (4, 5): '4-5'
    }
        df['TownSize'] = df['TownSize'].apply(lambda x: next((v for k, v in townsize_generalization.items() if k[0] <= x <= k[1]), 'Null' if x > 6 else x))

def main():
    gen_data = GeneralizeData()
    gen_data.gen_age()
    gen_data.gen_income()
    gen_data.gen_education()
    gen_data.gen_townsize()

    df.to_excel('deidentified_data.xlsx', index=False)

    age_classes = df['Age'].value_counts()
    print("Equivalence class sizes for Age:")
    print(age_classes)

    household_income_classes = df['HouseholdIncome'].value_counts()
    print("Equivalence class sizes for HouseholdIncome:")
    print(household_income_classes)

    educationYears_classes = df['EducationYears'].value_counts()
    print("Equivalence class sizes for EducationYears:")
    print(educationYears_classes)

    townsize_classes = df['TownSize'].value_counts()
    print("Equivalence class sizes for TownSize:")
    print(townsize_classes)

    
    print("Complete")

main()