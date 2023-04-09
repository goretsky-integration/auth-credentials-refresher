import models


def test_send_sign_in_oidc_form_data(httpx_mock, office_manager):
    httpx_mock.add_response(text=models.HTML('response'))
    sign_in_oidc_form_data = models.SignInOidcFormData(
        code='CD5407889B73F5457865BADD4D29DAE54D80D67643E80291EC3F92E09AA505E2',
        scope='openid employee profile ext_profile roles email phone users'
              ' offline_access dodo_staff_api accounting.admin inventory.admin',
        state='CfDJ8JIVAtoTAL1Bq_ajCWf_96zmxKlqO_jyC_MP9IyZDjO6QcJbCcmTOBjaQDus'
              'ytMRURgwRITOy7zAb7qS_XZgdMwqbEBssX7wvG4RbzW8Q47L0UVSYLL7pSJq0gEB'
              'KM4Ir0rqZdiUTA4uftNhMiA04kXkTIMQEt0R4ZduDChpWX21Y23MZ3Kr2_P_AUEB'
              '7huz7RkPZ46uiTct78wDfm25hKLzLnWLPHIkLE5Lg-qFsx7BMcX6pfEEJNvgB7v1'
              'r2oPI9MJmMicOyTY9BwDAgxP6cZimGx1C53CQ2-TeiCJJOesigrwvKq3siX6M8GF'
              'JgavzvOsaQIqeN0IZMpgeoOKDQDfIoi9IKi1GcmMoDFFKXov0OZwk0WnxB58O8jz'
              'Wr74dQ',
        session_state='-r5W7NRyzka-1JTEFiZemAS2xiStTj_bwngojuoYVio'
                      '.3D7DEF99DADC71B3396048F6D85526A1',
    )
    actual = office_manager.send_sign_in_oidc_form_data(
        sign_in_oidc_form_data=sign_in_oidc_form_data,
    )
    assert actual == models.HTML('response')
