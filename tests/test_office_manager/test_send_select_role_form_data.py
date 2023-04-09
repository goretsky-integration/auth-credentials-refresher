import models


def test_send_select_role_form_data(httpx_mock, office_manager):
    httpx_mock.add_response(text=models.HTML('response'))
    select_role_form_data = models.SelectRoleFormData(
        request_verification_token='CfDJ8JIVAtoTAL1Bq_ajCWf_96zfO4RT7yKRuMb7FAk'
                                   'DNoV34TrZGvocTRVXPDuqKG81v6G6C4fKicDFhiI_bk'
                                   'KGmZU9OyPMzTGUopk4S5dA5FN3oEM_BUqfINdSMJYim'
                                   '-pPKO1j1-iKBsTPVaRmyRKpD6Y0jy3SHHrc4Wytz3Ws'
                                   'mAwpcEcEkmEhaezuZS85pbzCAw'
    )
    response = office_manager.send_select_role_form_data(
        select_role_form_data=select_role_form_data,
        selected_role_id=models.RoleId.OFFICE_MANAGER,
    )
    assert response == models.HTML('response')
