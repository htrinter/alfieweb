from flask import render_template, request
from alfieweb import app

from forms.create_form import CreateForm
from services.insert_file_resolver import get_file

@app.route(
    "/",
    methods=['GET', 'POST']
)
def index():
    createForm = CreateForm();
    if request.method == 'POST':
        if createForm.validate():
            format = createForm.format.data
            layout = createForm.layout.data
            language = createForm.language.data
            year = createForm.year.data
            return get_file(format, layout, language, year)
        else:
            return "Error 400: Bad Request", 400
    return render_template('index.html', form = createForm)
