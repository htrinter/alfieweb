from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

from forms.validators.choice_validator import ChoiceValidator

class CreateForm(FlaskForm):

    FORMAT_CHOICES = [
        ("pocket",      u'Pocket'),
        ("personal",    u'Personal'),
        ("a6",          u'A6'),
        ("a5",          u'A5'),
    ]

    LAYOUT_CHOICES = [
        ("w1p",         u'Week on one page with notes'),
        ("w2p",         u'Week on two pages'),
        ("w2pwf",       u'Week on two pages with emphasis on weekdays'),
        ("w4p",         u'Week on four pages, with dot indicators'),
        ("wg",          u'Week on four pages with room for notes'),
        ("1d2p",        u'Day on two pages with notes')
    ]

    LANGUAGE_CHOICES = [
        ("en",  u'English'),
        ("sv",  u'Swedish'),
        ("de",  u'German')
    ]

    BOOLEAN_CHOICES = [
        ("yes", u'Yes'),
        ("no",  u'No')
    ]

    YEAR_CHOICES = []
    for year in range(2019, 2031):
        YEAR_CHOICES.append((str(year), str(year)))

    format = SelectField(
        u'Format',
        choices = FORMAT_CHOICES,
        validators=[ChoiceValidator(FORMAT_CHOICES)]
    )
    layout = SelectField(
        u'Layout',
        choices = LAYOUT_CHOICES,
        validators=[ChoiceValidator(LAYOUT_CHOICES)]
    )
    language = SelectField(
        u'Language',
        choices = LANGUAGE_CHOICES,
        validators=[ChoiceValidator(LANGUAGE_CHOICES)]
    )
    year = SelectField(
        u'Year',
        choices = YEAR_CHOICES,
        validators=[ChoiceValidator(YEAR_CHOICES)]
    )
    submit = SubmitField('Create PDF')
