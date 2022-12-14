from src.Person import Person


class PlayerRegistration(Person):
    def __init__(self, gsm, address, education_status, job, mail, acting_education, experience,
                 name, surname, age, gender, identification_number, size, weight, hair_color, eye_color,
                 marital_status, date_of_birth):
        super().__init__(self, name, surname, age, gender, identification_number, size, weight, hair_color, eye_color,
                         marital_status, date_of_birth)

        self.gsm = gsm
        self.address = address
        self.education_status = education_status
        self.job = job
        self.mail = mail
        self.acting_education = acting_education
        self.experience = experience
