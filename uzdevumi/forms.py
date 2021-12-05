from django.forms import(
    Form,
    CharField,
    FileField
)

class UserForm(Form):

    username = CharField()
    e_mail = CharField()

class FilterUser(Form):

    user = CharField()

class FileForm(Form):

    csv_file = FileField()
