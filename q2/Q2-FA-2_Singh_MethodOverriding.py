class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0:
            self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


regular_patient = Patient("Go Mez", 15000)
senior_patient = SeniorPatient("Alwinito Dela Cruz", 15000)
philhealth_patient = PhilHealthPatient("Benjamin Abdul", 15000)

patients = [
    regular_patient,
    senior_patient,
    philhealth_patient
]

for patient in patients:
    print(f"Patient Name: {patient.get_name()}")
    print(f"Original Bill: P{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: P{patient.calculate_bill():,.2f}")
    print("-" * 30)