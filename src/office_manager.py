from uuid import UUID

import models

__all__ = ('OfficeManagerService',)


class OfficeManagerService:

    def __init__(self, http_client: models.HTTPClient):
        self._http_client = http_client

    def go_to_office_manager_domain(self) -> models.HTML:
        response = self._http_client.get('/')
        return models.HTML(response.text)

    def send_sign_in_oidc_form_data(
            self,
            sign_in_oidc_form_data: models.SignInOidcFormData,
    ) -> models.HTML:
        request_data = {
            'code': sign_in_oidc_form_data.code,
            'scope': sign_in_oidc_form_data.scope,
            'state': sign_in_oidc_form_data.state,
            'session_state': sign_in_oidc_form_data.session_state,
        }
        url = '/signin-oidc'
        response = self._http_client.post(
            url=url,
            data=request_data,
        )
        return models.HTML(response.text)

    def send_select_role_form_data(
            self,
            *,
            select_role_form_data: models.SelectRoleFormData,
            selected_role_id: int | None = None,
    ) -> models.HTML:
        request_data = {
            'roleId': selected_role_id,
            '__RequestVerificationToken': select_role_form_data.request_verification_token,
        }
        url = '/Infrastructure/Authenticate/SelectRole'
        response = self._http_client.post(url, data=request_data)
        return models.HTML(response.text)

    def send_select_department_form_data(
            self,
            *,
            select_department_form_data: models.SelectDepartmentFormData,
            selected_department_uuid: UUID | None = None,
    ) -> models.HTML:
        request_data = {
            'uuid': selected_department_uuid,
            '__RequestVerificationToken': select_department_form_data.request_verification_token,
        }
        url = '/Infrastructure/Authenticate/SelectDepartment'
        response = self._http_client.post(url, data=request_data)
        return models.HTML(response.text)
