#Patient py for creating class methods and attributes

import csv

with open("/Users/ellepickard/Documents/Computational BME/Module 1/Module1_CompBME/Metadata and Protein Data for Module 1.csv", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader) # Get the first row
        for h in headers:
            print(h)


#OOP and Class of Patient Objects
class Patient: 
    all_patients = [] 

    def __init__(
        self,
        donor_id,
        primary_study_name,
        secondary_study_name,
        age_at_death,
        sex,
        race_white,
        race_black,
        race_asian,
        race_american_indian,
        race_native_hawaiian,
        race_unknown,
        race_other,
        specify_other_race,
        hispanic_latino,
        highest_level_of_education,
        years_of_education,
        apoe_genotype,
        cognitive_status,
        age_of_onset_cognitive_symptoms,
        age_of_dementia_diagnosis,
        known_head_injury,
        neuroimaging,
        last_casi_score,
        interval_last_casi,
        last_mmse_score,
        interval_last_mmse,
        last_moca_score,
        interval_last_moca,
        pmi,
        rapid_frozen_tissue_type,
        ex_vivo_imaging,
        fresh_brain_weight,
        brain_ph,
        overall_ad_neuropathological_change,
        thal,
        braak,
        cerad_score,
        overall_caa_score,
        highest_lewy_body_disease,
        total_microinfarcts_gross,
        total_microinfarcts_screening,
        atherosclerosis,
        arteriolosclerosis,
        late,
        rin,
        severely_affected,
        abeta40,
        abeta42,
        ttau,
        ptau,
    ):

        # Basic information
        self.donor_id = donor_id
        self.primary_study_name = primary_study_name
        self.secondary_study_name = secondary_study_name
        self.age_at_death = age_at_death
        self.sex = sex

        # Race
        if race_white:
            self.race = "White"
        elif race_black:
            self.race = "Black/African American"
        elif race_asian:
            self.race = "Asian"
        elif race_american_indian:
            self.race = "American Indian/Alaska Native"
        elif race_native_hawaiian:
            self.race = "Native Hawaiian or Pacific Islander"
        elif race_unknown:
            self.race = "Unknown or unreported"
        elif race_other:
            self.race = specify_other_race
        else:
            self.race = "Not reported"

        self.hispanic_latino = hispanic_latino
        self.highest_level_of_education = highest_level_of_education
        self.years_of_education = years_of_education

        # Genetics and cognitive information
        self.apoe_genotype = apoe_genotype
        self.cognitive_status = cognitive_status
        self.age_of_onset_cognitive_symptoms = age_of_onset_cognitive_symptoms
        self.age_of_dementia_diagnosis = age_of_dementia_diagnosis
        self.known_head_injury = known_head_injury
        self.neuroimaging = neuroimaging

        # Cognitive test scores
        self.last_casi_score = last_casi_score
        self.interval_last_casi = interval_last_casi
        self.last_mmse_score = last_mmse_score
        self.interval_last_mmse = interval_last_mmse
        self.last_moca_score = last_moca_score
        self.interval_last_moca = interval_last_moca

        # Brain/tissue information
        self.pmi = pmi
        self.rapid_frozen_tissue_type = rapid_frozen_tissue_type
        self.ex_vivo_imaging = ex_vivo_imaging
        self.fresh_brain_weight = fresh_brain_weight
        self.brain_ph = brain_ph

        # Neuropathology
        self.overall_ad_neuropathological_change = overall_ad_neuropathological_change
        self.thal = thal
        self.braak = braak
        self.cerad_score = cerad_score
        self.overall_caa_score = overall_caa_score
        self.highest_lewy_body_disease = highest_lewy_body_disease

        # Vascular pathology
        self.total_microinfarcts_gross = total_microinfarcts_gross
        self.total_microinfarcts_screening = total_microinfarcts_screening
        self.atherosclerosis = atherosclerosis
        self.arteriolosclerosis = arteriolosclerosis

        # LATE
        self.late = late
        self.rin = rin
        self.severely_affected = severely_affected

        # Protein measurements
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ttau = ttau
        self.ptau = ptau

        Patient.all_patients.append(self) # Add the patient instance to the all_patients list

    ##Used ChatGPT above to help me copy the headers into attributes for the self object. I also had it help me create conditional statements for the race attribute, since there were multiple race attributes in the csv. 


#Making a representer to call when printing the object
    def __repr__(self):
        return ( f"Patient {self.donor_id}: "
        f"({self.primary_study_name} | "
        f"{self.secondary_study_name} | "
        f"{self.age_at_death} | "
        f"{self.sex} | "
        f"{self.race} | "
        f"{self.hispanic_latino} | "
        f"{self.highest_level_of_education} | "
        f"{self.years_of_education} | "
        f"{self.apoe_genotype} | "
        f"{self.cognitive_status} | "
        f"{self.age_of_onset_cognitive_symptoms} | "
        f"{self.age_of_dementia_diagnosis} | "
        f"{self.known_head_injury} | "
        f"{self.neuroimaging} | "
        f"{self.last_casi_score} | "
        f"{self.interval_last_casi} | "
        f"{self.last_mmse_score} | "
        f"{self.interval_last_mmse} | "
        f"{self.last_moca_score} | "
        f"{self.interval_last_moca} | "
        f"{self.pmi} | "
        f"{self.rapid_frozen_tissue_type} | "
        f"{self.ex_vivo_imaging} | "
        f"{self.fresh_brain_weight} | "
        f"{self.brain_ph} | "
        f"{self.overall_ad_neuropathological_change} | "
        f"{self.thal} | "
        f"{self.braak} | "
        f"{self.cerad_score} | "
        f"{self.overall_caa_score} | "
        f"{self.highest_lewy_body_disease} | "
        f"{self.total_microinfarcts_gross} | "
        f"{self.total_microinfarcts_screening} | "
        f"{self.atherosclerosis} | "
        f"{self.arteriolosclerosis} | "
        f"{self.late} | "
        f"{self.rin} | "
        f"{self.severely_affected} | "
        f"{self.abeta40} | "
        f"{self.abeta42} | "
        f"{self.ttau} | "
        f"{self.ptau})"
    )

    #Class method to create subset of patients with at least two specific attributes 
    @classmethod
    def create_subset(cls, attribute1, value1, attribute2, value2):
        subset = []
    
        for patient in cls.all_patients:
            if (getattr(patient, attribute1) == value1 and
                getattr(patient, attribute2) == value2):
                subset.append(patient)
    
        return subset

#Again, used ChatGPT above to help me create the representer method; copying all the attributes 

#Creating patient objects from the csv file using DictReader to read the csv. 
with open("/Users/ellepickard/Documents/Computational BME/Module 1/Module1_CompBME/Metadata and Protein Data for Module 1.csv", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        Patient(
            row["Donor ID"],
            row["Primary Study Name"],
            row["Secondary Study Name"],
            float(row["Age at Death"]),
            row["Sex"],
            row["Race (choice=White)"],
            row["Race (choice=Black/ African American)"],
            row["Race (choice=Asian)"],
            row["Race (choice=American Indian/ Alaska Native)"],
            row["Race (choice=Native Hawaiian or Pacific Islander)"],
            row["Race (choice=Unknown or unreported)"],
            row["Race (choice=Other)"],
            row["specify other race"],
            row["Hispanic/Latino"],
            row["Highest level of education"],
            row["Years of education"],
            row["APOE Genotype"],
            row["Cognitive Status"],
            row["Age of onset cognitive symptoms"],
            row["Age of Dementia diagnosis"],
            row["Known head injury"],
            row["Have they had neuroimaging"],
            row["Last CASI Score"],
            row["Interval from last CASI in months"],
            row["Last MMSE Score"],
            row["Interval from last MMSE in months"],
            row["Last MOCA Score"],
            row["Interval from last MOCA in months"],
            row["PMI"],
            row["Rapid Frozen Tissue Type"],
            row["Ex Vivo Imaging"],
            row["Fresh Brain Weight"],
            row["Brain pH"],
            row["Overall AD neuropathological Change"],
            row["Thal"],
            row["Braak"],
            row["CERAD score"],
            row["Overall CAA Score"],
            row["Highest Lewy Body Disease"],
            row["Total Microinfarcts (not observed grossly)"],
            row["Total microinfarcts in screening sections"],
            row["Atherosclerosis"],
            row["Arteriolosclerosis"],
            row["LATE"],
            row["RIN"],
            row["Severely Affected Donor"],
            row["ABeta40 pg/ug"],
            row["ABeta42 pg/ug"],
            row["tTAU pg/ug"],
            row["pTAU pg/ug"]
        )

#Again used ChatGPT to help me paste the headers into the correct format above ^^ 

#Ran into a bunch of errors due to using ChatGPT to help me create the patient objects from all the headers; it was misreading headers and separating them incorrectly so I had to go in and fix them. 
#The two main headers that were the biggest issues were the "LATE" and "RIN" headers, which were being read as one header by ChatGPT. I also had to fix the "Rapid Frozen Tissue Type" header, which was being read as "Rapid Frozen Tissue" and "Tissue Type". 
#After going back to fix my init and following through with fixing the rest of the code, it now runs smoothly.

