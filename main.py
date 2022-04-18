# This is the Tax Software made by QIn Yang 400420584, April 9th 2022

# Section 1: Input personal information, using 2021 Income Tax and Benefit Return Form T1
# [using while loop to validate input information; use dictionary to gather sections of information]
def input_personal_information():
    user_info = {}
    first_name = str(input("Please provide your first name \n"))
    while not first_name.isalpha():
        first_name = str(input("Your first name is invalid please insert again,  \n"))
    user_info["first_name"] = first_name

    last_name = str(input("Please provide your last name \n"))
    while not last_name.isalpha():
        last_name = str(input("Your last name is invalid please insert again,  \n"))
    user_info["last_name"] = last_name

    mailing_address = str(input("Please provide your mailing address \n"))
    user_info["mailing_address"] = mailing_address

    email_address = str(input("Please provide your email address \n"))
    user_info["email_address"] = email_address

    postal_code = str(input("Please provide your postal code \n"))
    user_info["postal_code"] = postal_code

    SIN_number = str(input("Please provide your SIN number \n"))
    while not len(SIN_number) == 9 or not SIN_number.isdigit():
        SIN_number = str(input("Your SIN number is invalid please insert again,  \n"))
    user_info["SIN_number"] = SIN_number

    Date_of_birth = str(input("Please provide your Date of Birth (Year Month date) \n"))
    while not len(Date_of_birth) == 8 or not Date_of_birth.isdigit():
        Date_of_birth = str(input("Your Date of Birth is invalid please insert again,  \n"))
    while int(Date_of_birth[0:4]) >= 2022:
        Date_of_birth = str(input("Your Date of Birth YEAR is invalid please insert again,  \n"))
    while not 12 >= int(Date_of_birth[4:6]) >= 1:
        Date_of_birth = str(input("Your Date of Birth MONTH is invalid please insert again,  \n"))
    while not 31 >= int(Date_of_birth[6:8]) >= 1:
        Date_of_birth = str(input("Your Date of Birth DAY is invalid please insert again,  \n"))
    user_info["Date_of_birth"] = Date_of_birth

    Marital_status = int(input("Please provide your marital status 0-Single 1-Married \n"))
    while not Marital_status == 0 and not Marital_status == 1:
        Marital_status = str(input("Your input is invalid Please provide your marital status 0-Single 1-Married \n"))
    if Marital_status == 0:
        user_info["Marital_status"] = "Single"
    else:
        user_info["Marital_status"] = "Married"

    return user_info

# Section 2:  This section is to collect and calculate Total taxable income
class TaxableIncome:
    def __init__(self):
        self.employment_income = float(input('What is your employment income? Line 10100 \n'))
        self.self_income = float(input('What is your self-employment income? Line 15000  \n'))
        self.RRSP_claim = float(input("What is your RRSP claim for this tax year? Line 20800 \n"))

    def calculate(self):
        self.total_taxable_income = self.employment_income + self.self_income - self.RRSP_claim

    def get(self):
        return self.total_taxable_income

# Section 3: To calculate Federal Tax rates , Data using from year 2021 CRA website
class FederalTax:
    def __init__(self):
        self.federal_rates_less_50197 = 0.15

        self.federal_tax_base_between_50197_100392 = 7529.55
        self.federal_rates_between_50197_100392 = 0.205

        self.federal_tax_base_between_100392_155625 = 17819.53
        self.federal_rates_between_100392_155625 = 0.26

        self.federal_tax_base_between_155625_221708 = 32180.11
        self.federal_rates_between_155625_221708 = 0.29

        self.federal_tax_base_above_221708 = 51344.18
        self.federal_rates_above_221708 = 0.33

    def calculate(self, total_taxable_income):
        if total_taxable_income <= 50197:
            self.federal_tax = total_taxable_income * self.federal_rates_less_50197
        if 50197 < total_taxable_income <= 100392:
            self.federal_tax = (total_taxable_income - 50197) * self.federal_rates_between_50197_100392 \
                               + self.federal_tax_base_between_50197_100392
        if 100392 < total_taxable_income <= 155625:
            self.federal_tax = (total_taxable_income - 100392) * self.federal_rates_between_100392_155625 \
                               + self.federal_tax_base_between_100392_155625
        if 155625 < total_taxable_income <= 221788:
            self.federal_tax = (total_taxable_income - 155625) * self.federal_rates_between_155625_221708 \
                               + self.federal_tax_base_between_155625_221708
        if 221708 < total_taxable_income:
            self.federal_tax = (total_taxable_income - 221708) * self.federal_rates_above_221708 \
                               + self.federal_tax_base_above_221708

    def get(self):
        return self.federal_tax


# Section 4: Calculate Ontario Tax Rates, Data using 2021 CRA website
class OntarioTax:
    def __init__(self):
        self.ontario_rates_less_46226 = 0.0505

        self.ontario_base_between_46226_92454 = 2334
        self.ontario_rates_between_46226_92454 = 0.0915

        self.ontario_base_between_92454_150000 = 6564
        self.ontario_rates_between_92454_150000 = 0.1116

        self.ontario_base_between_150000_220000 = 12986
        self.ontario_rates_between_150000_220000 = 0.1216

        self.ontario_base_above_220000 = 21499
        self.ontario_rates_above_220000 = 0.1316

    def calculate(self, total_taxable_income):
        if total_taxable_income <= 46226:
           self.ontario_tax = total_taxable_income * self.ontario_rates_less_46226

        if 46226 < total_taxable_income <= 92454:
            self.ontario_tax = self.ontario_base_between_46226_92454 + \
                               (total_taxable_income - 46226) * self.ontario_rates_between_46226_92454
        if 92454 < total_taxable_income <= 150000:
            self.ontario_tax = self.ontario_base_between_92454_150000 + \
                               (total_taxable_income - 92454) * self.ontario_rates_between_92454_150000
        if 150000 < total_taxable_income <= 220000:
            self.ontario_tax = self.ontario_base_between_150000_220000 + \
                               (total_taxable_income - 150000) * self.ontario_rates_between_150000_220000
        if 220000 < total_taxable_income:
            self.ontario_tax = self.ontario_base_above_220000 + \
                               (total_taxable_income - 20000) * self.ontario_rates_above_220000

    def get(self):
        return self.ontario_tax


# Section 5: Calculate Total tax credit using inheritance function
class TaxCredit:
    def __init__(self, expense, rate, maximum_limit):
        self.__expense = expense
        self.__rate = rate
        self.__limit = maximum_limit

    def calculate(self):
        self.credit = self.__expense * self.__rate
        if self.credit > self.__limit:
            self.credit = self.__limit

    def get(self):
        return self.credit


class TuitionCredit(TaxCredit):
    def __init__(self):
        self.expense = float(input('What is your total tuition? T2202 Line 32300. \n If you are not student, '
                                   'please Enter zero. \n'))
        TaxCredit.__init__(self, self.expense, 0.15, 5000)


class VFACredit(TaxCredit):
    def __init__(self):
        self.expense = float(input('What is your total Volunteer amount ? T4 Line 31220. \n If you are not volunteer, '
                                   'please Enter zero. \n'))
        TaxCredit.__init__(self, self.expense, 1, 3000)


class EmploymentAmount(TaxCredit):
    def __init__(self):
        self.expense = float(input('What is your total employment expense? T2202 Line 32300. \n '
                                   'If you are not employee, please Enter zero. \n'))
        TaxCredit.__init__(self, self.expense, 1, 1257)


# Section 6: RUN
personal_information = input_personal_information()

total_taxable_income = TaxableIncome()
total_taxable_income.calculate()

total_federal_tax = FederalTax()
total_federal_tax.calculate(total_taxable_income.get())

total_ontario_tax = OntarioTax()
total_ontario_tax.calculate(total_taxable_income.get())

tuition_credit = TuitionCredit()
tuition_credit.calculate()

VFACredit = VFACredit()
VFACredit.calculate()

EmploymentAmount = EmploymentAmount()
EmploymentAmount.calculate()

total_credit = tuition_credit.get() + VFACredit.get() + EmploymentAmount.get()
total_payment = total_federal_tax.get() + total_ontario_tax.get() - total_credit

# Section 7: Final Output
print("Your first name is: ", personal_information["first_name"])
print("Your last name is: ", personal_information["last_name"])
print("Your mailing address is: ", personal_information["mailing_address"])
print("Your email address is: ", personal_information["email_address"])
print("Your postal code is: ", personal_information["postal_code"])
print("Your Date of birth is: ", personal_information["Date_of_birth"])
print("Your Marital status is: ", personal_information["Marital_status"])
print("Total taxable income is", total_taxable_income.get())
print("Total Federal Tax is", format(total_federal_tax.get(), ".1f"))
print("Total Ontario Tax is", format(total_ontario_tax.get(), ".1f"))
print("Total Tax credit you can apply is", format(total_credit, ".1f"))
print("Total Payment for this is", format(total_payment, ".1f"))

