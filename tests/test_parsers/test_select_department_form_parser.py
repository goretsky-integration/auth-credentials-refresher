import pathlib

import models
from parsers import parse_select_department_form

FILE_PATH = pathlib.Path.joinpath(
    pathlib.Path(__file__).parent.parent,
    'html',
    'select_department_form.html',
)


def test_select_department_form_parser():
    select_department_form = models.HTML(FILE_PATH.read_text(encoding='utf-8'))
    actual = parse_select_department_form(select_department_form)
    expected = models.SelectDepartmentFormData(
        request_verification_token='CfDJ8JIVAtoTAL1Bq_ajCWf_96xulH5FIwulyIakm1N'
                                   'uQZcPuFoi7Y4quXX790R2K5pFKKTk4maag0IsS8TJRT'
                                   '6pEZ0faSZfYT8o4bZYCojkc__zpwQN36om-KlDCDhyW'
                                   'vojJQ_IRbD7XGtIHm5dBOf-NqZBRrAOtmdFKyD_o1pt'
                                   'fYR1cnAk6qhIqOh5CXV7RXpjsw',
    )
    assert actual == expected
