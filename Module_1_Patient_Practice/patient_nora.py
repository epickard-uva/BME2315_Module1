import csv

#defining a class of "patient objects"
class Patient:
    #list of every patient object 
    all_patients = []

#constructor that lists different patient attributes 
    def __init__(self, donor_id, age, sex, abeta42, ttau, cognitive_status, apoe, braak): 
        self.donor_id = donor_id
        self.age = age
        self.sex = sex
        self.abeta42 = abeta42
        self.ttau = ttau
        self.cognitive_status = cognitive_status
        self.apoe = apoe
        self.braak = braak

        Patient.all_patients.append(self)

#representer that defines what is shown when you print a patient
    def __repr__(self):
        return f"{self.donor_id}: Age={self.age}, Sex={self.sex}, Cognitive Status={self.cognitive_status}, APOE={self.apoe}, Braak={self.braak}"

#gets the braak value for sorting 
    def get_braak(self): 
        return self.braak

#class method for creating objects from the csv
    @classmethod 
    def instantiate_from_csv(cls, filename: str):

#the code below will open the .csv file and create a list of all the rows in your spreadsheet
        
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)
        
#the code below will create a patient object for each row, based on the data: 
        
        for row in rows_of_patients:
            Patient(
                donor_id = row['Donor ID'],
                age = float(row["Age at Death"]),
                sex = row["Sex"],
                abeta42 = float(row["ABeta42 pg/ug"]),
                ttau = float(row["tTAU pg/ug"]),
                cognitive_status=row["Cognitive Status"],
                apoe=row["APOE Genotype"],
                braak=row["Braak"]
            )

#class method for filtering objects based on certain attributes
    @classmethod
    def filter(cls, list, sex="any", age="any", cognitive_status="any", apoe="any", braak="any"):
        all_patients = list
        remove_list = []
        attr_list = (
            sex, 
            age, 
            cognitive_status,
            apoe, 
            braak
        )
        attr_name = (
            "sex",
            "age",
            "cognitive_status",
            "apoe",
             "braak"
        )
        for attr in range(len(attr_list)):
            if attr_list[attr] != "any":
                for patient in all_patients:
                    if getattr(patient,attr_name[attr]) != attr_list[attr]:
                        remove_list.append(patient)
                all_patients = [patient for patient in all_patients if patient not in remove_list]
                remove_list.clear()

        return all_patients

#Citation: I used AI to help clarify Python concepts, troubleshoot errors, and improve code documentation. 
#I wrote and adapted the code myself and reviewed the final code to ensure I understood it.