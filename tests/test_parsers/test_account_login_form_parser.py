import pathlib

import models
from parsers import parse_account_login_form_data

FILE_PATH = pathlib.Path.joinpath(
    pathlib.Path(__file__).parent.parent,
    'html',
    'account_login_form.html',
)


def test_account_login_form_parser():
    account_login_form = models.HTML(
        FILE_PATH.read_text(encoding='utf-8')
    )
    actual = parse_account_login_form_data(account_login_form)
    expected = models.EmptyAccountLoginFormData(
        return_url='/connect/authorize/callback?client_id=dodo-office-manager&r'
                   'edirect_uri=https%3A%2F%2Fofficemanager.dodois.test%2Fsigni'
                   'n-oidc&response_type=code&scope=openid%20employee%20profile'
                   '%20ext_profile%20roles%20email%20phone%20users%20offline_ac'
                   'cess%20dodo_staff_api%20accounting.admin%20inventory.admin&'
                   'code_challenge=VavF5ma--X3oDBTyUns7pMiuz7bb3D_k_VicS5_wQhU&'
                   'code_challenge_method=S256&response_mode=form_post&nonce=63'
                   '8166454148826158.ZTc5MGI4YTEtMTc3NC00MzdiLWExODktMTA2ZDNmNj'
                   'Y2Y2U3ZWFmZDc2NTUtMjFhYi00ZmIwLThlMTMtN2ZiZTA4NmFjN2Vl&stat'
                   'e=CfDJ8JIVAtoTAL1Bq_ajCWf_96wLZMoeKAtfo90eTpZVK1hQegycBi1u0'
                   'W3dhT9PtbtiEQLeMnFTxhMmirsIGg81_NOecjv-7qYutvYjEsDyQD9qHrNR'
                   'UexxEFgpsqWpEjuSlfIukDDMXhvShonIGkXONQZbTYRAmTLoJyl4NxHgP1V'
                   'jsx68Ao_ARupLdFEpwn-qfGsuQ1Bd3S854ken-dwHUNa_cHAEQfXF8u4flq'
                   'o_pAglv2c-fMQQjpt1298eZYJd9UQK6vAVoYJouxiII2TrbPcrQzT1P3KhY'
                   '_vIz_i10U88C8B8d_MIB657P8NT56rdAVtuJ3vEr6cPLq5P-_Cmpy--XJnr'
                   'ufAzonKdFkpKSS5OLPGzJ1HmzmfcGk9SYLaQhw',
        request_verification_token='CfDJ8LdWR5S65pFFhlxr81cPG8OzTWDY194hUqJjKFL'
                                   'AEc5KLbmj5_yZyZn6oGaG7u6Wl0TMogB1WAlb8LoJWG'
                                   'FTFW3mxDHU_klT9M0uUISmr9KZ3uXNKfcO_7RQFB2vZ'
                                   'ZIzl2ZCVkOsOukqIDN0t1Qx_AY',
    )
    assert actual == expected
