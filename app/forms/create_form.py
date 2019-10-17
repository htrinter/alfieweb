from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from datetime import datetime

from forms.validators.choice_validator import ChoiceValidator

class CreateForm(FlaskForm):

    FORMAT_CHOICES = [
        ("pocket",      u'Pocket',      True),
        ("personal",    u'Personal',    False),
        ("a6",          u'A6',          False),
        ("a5",          u'A5',          False),
    ]

    LAYOUT_CHOICES = [
        ("w1p",         u'Week on one page with notes',                     True),
        ("w2p",         u'Week on two pages',                               False),
        ("w2pwf",       u'Week on two pages with emphasis on weekdays',     False),
        ("w4p",         u'Week on four pages, with dot indicators',         False),
        ("wg",          u'Week on four pages with room for notes',          False),
        ("1d2p",        u'Day on two pages with notes',                     False)
    ]

    LANGUAGE_CHOICES = [
        ("en",  u'English', True),
        ("sv",  u'Swedish', False),
        ("de",  u'German',  False)
    ]

    BOOLEAN_CHOICES = [
        ("yes", u'Yes', True),
        ("no",  u'No',  False)
    ]

    YEAR_CHOICES = []
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    default_choice_year = current_year if current_month < 7 else current_year + 1
    for year in range(current_year, current_year + 10):
        default_choice = year == default_choice_year
        YEAR_CHOICES.append((str(year), str(year), default_choice))

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
