class QuotaError(Exception):
    pass

class Mortgage:
    def __init__(self, property_value: int, owner_age: int, marital_status: str, spouse_age: int, interest_rate: float):
        self.property_value = int(property_value.replace(".","").replace(",","").replace("'",""))
        self.owner_age = owner_age
        self.marital_status = marital_status
        self.spouse_age = spouse_age
        self.interest_rate = interest_rate

    def reverse_mortgage_calculator(self):
        try:
            self.verify_value()
        except QuotaError as e:
            print(f"Error {e}")
        try:
            self.verify_age()
        except QuotaError as e:
            print(f"Error {e}")
        try:
            self.verify_marital_status()
        except QuotaError as e:
            print(f"Error {e}")
        try:
            self.verify_rate()
        except QuotaError as e:
            print(f"Error {e}")
        new_marital_status = self.convert_marital_status()

        life_expectancy_colombia = 73
        monthly_interest_rate = self.interest_rate / 12
        life_expectancy = 1
        if monthly_interest_rate >= 0:
            if self.interest_rate > 0:
                if new_marital_status == "single" and self.owner_age < life_expectancy_colombia:
                    life_expectancy = life_expectancy_colombia - self.owner_age
                elif new_marital_status == "married" and self.spouse_age < life_expectancy_colombia:
                    life_expectancy = life_expectancy_colombia - self.spouse_age
                monthly_payment = (self.property_value * monthly_interest_rate) / (life_expectancy * 12)
            else:
                if life_expectancy_colombia > self.owner_age:
                    life_expectancy = life_expectancy_colombia - self.owner_age
                elif life_expectancy_colombia > self.spouse_age:
                    life_expectancy = life_expectancy - self.spouse_age
                monthly_payment = self.property_value / (life_expectancy * 12)
            return monthly_payment
        else:
            if self.interest_rate < 0:
                if new_marital_status == "single" and self.owner_age < life_expectancy_colombia:
                    life_expectancy = life_expectancy_colombia - self.owner_age
                elif new_marital_status == "married" and self.spouse_age < life_expectancy_colombia:
                    life_expectancy = life_expectancy_colombia - self.spouse_age
                monthly_payment = (self.property_value * monthly_interest_rate) / (life_expectancy * 12)
                return monthly_payment


    def verify_rate(self):
        if self.interest_rate > 34.97 or self.interest_rate < 0:
            raise QuotaError(f"The interest rate exceeds the limits. The error is: {self.interest_rate}. The maximum interest rate in Colombia is 34.97% and the minimum is 0%")

    def verify_age(self):
        if self.owner_age < 65 or self.owner_age < 0:
            raise QuotaError(f"The owner's age is not suitable for this process. The error is: {self.owner_age}. The owner's age must be 65 or older")

    def verify_value(self):
        if type(self.property_value) != int:
            raise QuotaError(f"The value was entered with special characters. The error is: {self.property_value}. You must input the value without periods or commas.")
        elif self.property_value < 650000000 or self.property_value > 800000000 or self.property_value < 0:
            raise QuotaError(f"The property value does not meet the established parameters. The error is: {self.property_value}. The property value must be between 650 and 800 million")
        

    def verify_marital_status(self):
        new_marital_status = self.convert_marital_status()
        if new_marital_status != "soltero" and new_marital_status != "casado":
            raise QuotaError(f"The marital status is incorrect. The error is: {self.marital_status}. The marital status must be soltero or casado")

    def convert_marital_status(self):
        return self.marital_status.lower()
