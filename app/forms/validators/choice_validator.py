from wtforms import ValidationError

class ChoiceValidator(object):

    def __init__(self, validChoices, message = None):
        self.validChoices = validChoices
        self.message = message

    def __call__(self, form, field):
        for validChoice in self.validChoices:
            if validChoice[0] == field.data:
                return
        raise ValidationError(self.message)
