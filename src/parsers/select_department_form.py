from bs4 import BeautifulSoup

import models

__all__ = ('parse_select_department_form',)


def parse_select_department_form(
        select_department_form_html: models.HTML,
) -> models.SelectDepartmentFormData:
    soup = BeautifulSoup(select_department_form_html, 'lxml')

    request_verification_token = soup.find(
        attrs={'name': '__RequestVerificationToken'},
    )['value']

    return models.SelectDepartmentFormData(
        request_verification_token=request_verification_token,
    )
