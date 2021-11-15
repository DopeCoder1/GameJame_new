from mongoengine import Document,StringField,EmailField,IntField


class StudentReg(Document):
    teamName = StringField(required=True, max_length=50)
    phone = IntField(unique=True, required=True, max_length=12)
    email = EmailField(unique=True, required=True, max_length=50)
    fioOne = StringField(required=True, max_length=40)
    fioTwo = StringField(required=True, max_length=40)
    fioThree = StringField(max_length=40)
    fioFour = StringField(max_length=40)
    fioFive = StringField(max_length=40)
    universityName = StringField(max_length=40)
