import pathlib

import models
from parsers import parse_select_role_form

FILE_PATH = pathlib.Path.joinpath(
    pathlib.Path(__file__).parent.parent,
    'html',
    'select_role_form.html',
)


def test_select_role_form_parser():
    select_role_form = models.HTML(FILE_PATH.read_text(encoding='utf-8'))
    actual = parse_select_role_form(select_role_form)
    expected = models.SelectRoleFormData(
        request_verification_token='CfDJ8JIVAtoTAL1Bq_ajCWf_96zfO4RT7yKRuMb7FAk'
                                   'DNoV34TrZGvocTRVXPDuqKG81v6G6C4fKicDFhiI_bk'
                                   'KGmZU9OyPMzTGUopk4S5dA5FN3oEM_BUqfINdSMJYim'
                                   '-pPKO1j1-iKBsTPVaRmyRKpD6Y0jy3SHHrc4Wytz3Ws'
                                   'mAwpcEcEkmEhaezuZS85pbzCAw'
    )
    assert actual == expected
