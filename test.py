from unittest.mock import patch

from bson import ObjectId
from commons.utils.test_utils import DefaultTestCase

from resources.handlers.patient_resources import PatientResourceHandler

from commons.utils.http_error import BadRequest, InternalServerError

from test_data.resources.controller_response.test_send_aunt_bertha_referral_repsonse import (
    mock_send_aunt_bertha_referral_reponse,
)


class TestPatientResourceHsndlers(DefaultTestCase):
    """Test handlers for patient resources"""

    @patch("resources.utils.decorators.make_request")
    @patch("resources.helpers.aunt_bertha_helper.make_request")
    @patch("resources.handlers.patient_resources.get_request_attr")
    @patch("resources.helpers.aunt_bertha_helper.get_default_user_info")
    @patch("resources.helpers.aunt_bertha_helper.get_patient_personal_information")
    @patch(
        "resources.models.managers.patient_resources.PatientResourceManager.bulk_create_patient_resource"
    )
    def test_bulk_create_patient_resource(
        self,
        mock_resource_manager,
        mock_get_personal_info,
        mock_get_user_info,
        mock_extract_vars,
        mock_make_request,
        mock_generate_auth_token,
    ):
        def side_effect(arg):
            values = {"user_id": "user_57", "request_id": 2, "auth_token": 3}
            return values[arg]

        mock_extract_vars.side_effect = side_effect
        mock_generate_auth_token.return_value = (
            {"data": {"token": "auth_token"}, "success": True},
            None,
            200,
            None,
        )

        mock_get_personal_info.return_value = {
            "personalInformation": {
                "firstName": "Bobbi",
                "middleName": "A",
                "lastName": "Trehearne",
            }
        }
        mock_get_user_info.return_value = {
            "user_60": {"email": "mandar.gondhalekar@innovaccer.com"}
        }
        mock_make_request.return_value = (
            mock_send_aunt_bertha_referral_reponse,
            None,
            200,
            None,
        )
        mock_resource_manager.return_value = [ObjectId("5e256432f450547c7e03d0c7")]

        expected_response = [ObjectId("5e256432f450547c7e03d0c7")]
        mock_wsgi_req = DefaultTestCase.get_mock_wsgi_request(self)
        response_obj = PatientResourceHandler.bulk_create_patient_resource(
            mock_wsgi_req,
            resource_ids=["5668560948953088"],
            empi="P151024892",
            user_id="user_57",
            categories=["Housing"],
            comment="comment",
            phone_number="8888888888",
            email="btrehearne2wi@un.org",
            preferred_mode_of_contact=["Message", "Email"],
            referral_consent_given=True,
        )
        self.assertEqual(response_obj, expected_response)

    @patch("resources.helpers.aunt_bertha_helper.make_request")
    @patch("resources.handlers.patient_resources.get_request_attr")
    @patch("resources.utils.decorators.make_request")
    @patch("resources.helpers.aunt_bertha_helper.get_default_user_info")
    @patch("resources.helpers.aunt_bertha_helper.get_patient_personal_information")
    @patch(
        "resources.models.managers.patient_resources.PatientResourceManager.bulk_create_patient_resource"
    )
    def test_bulk_create_patient_resource_failure(
        self,
        mock_resource_manager,
        mock_get_personal_info,
        mock_get_user_info,
        mock_generate_auth_token,
        mock_extract_vars,
        mock_make_request,
    ):
        def side_effect(arg):
            values = {"user_id": "user_57", "request_id": 2, "auth_token": 3}
            return values[arg]

        mock_extract_vars.side_effect = side_effect
        mock_generate_auth_token.return_value = (
            {"data": {"token": "auth_token"}, "success": True},
            None,
            200,
            None,
        )
        mock_get_personal_info.return_value = {
            "personalInformation": {
                "firstName": "Bobbi",
                "middleName": "A",
                "lastName": "Trehearne",
            }
        }
        mock_get_user_info.return_value = {
            "user_60": {"email": "mandar.gondhalekar@innovaccer.com"}
        }
        mock_make_request.return_value = (
            mock_send_aunt_bertha_referral_reponse,
            None,
            200,
            None,
        )
        mock_resource_manager.return_value = [ObjectId("5e256432f450547c7e03d0c7")]

        mock_wsgi_req = DefaultTestCase.get_mock_wsgi_request(self)

        with self.assertRaises(BadRequest) as context:
            PatientResourceHandler.bulk_create_patient_resource(
                mock_wsgi_req,
                resource_ids=["5668560948953088"],
                empi="P151024892",
                user_id="user_57",
                categories=["Housing"],
                comment="comment",
                phone_number="8888888888",
                email="",
                preferred_mode_of_contact=["Message", "Email"],
                referral_consent_given=True,
            )

        self.assertEqual(context.exception.status_code, 400)

        with self.assertRaises(BadRequest) as context:
            PatientResourceHandler.bulk_create_patient_resource(
                mock_wsgi_req,
                resource_ids=["5668560948953088"],
                empi="P151024892",
                user_id="user_57",
                categories=["Housing"],
                comment="comment",
                phone_number="",
                email="",
                preferred_mode_of_contact=["Message", "Email"],
                referral_consent_given=True,
            )

        self.assertEqual(context.exception.status_code, 400)

    @patch("resources.utils.decorators.make_request")
    @patch("resources.helpers.aunt_bertha_helper.make_request")
    @patch("resources.handlers.patient_resources.get_request_attr")
    @patch("resources.helpers.aunt_bertha_helper.get_default_user_info")
    @patch("resources.helpers.aunt_bertha_helper.get_patient_personal_information")
    @patch(
        "resources.models.managers.patient_resources.PatientResourceManager.bulk_create_patient_resource"
    )
    def test_send_aunt_bertha_api_failure(
        self,
        mock_resource_manager,
        mock_get_personal_info,
        mock_get_user_info,
        mock_extract_vars,
        mock_make_request,
        mock_generate_auth_token,
    ):
        def side_effect(arg):
            values = {"user_id": "user_57", "request_id": 2, "auth_token": 3}
            return values[arg]

        mock_extract_vars.side_effect = side_effect
        mock_generate_auth_token.return_value = (
            {"data": {"token": "auth_token"}, "success": True},
            None,
            200,
            None,
        )
        mock_get_personal_info.return_value = {
            "personalInformation": {
                "firstName": "Bobbi",
                "middleName": "A",
                "lastName": "Trehearne",
            }
        }
        mock_get_user_info.return_value = {
            "user_60": {"email": "mandar.gondhalekar@innovaccer.com"}
        }
        mock_make_request.return_value = (
            {},
            None,
            500,
            None,
        )
        mock_resource_manager.return_value = [ObjectId("5e256432f450547c7e03d0c7")]

        mock_wsgi_req = DefaultTestCase.get_mock_wsgi_request(self)

        with self.assertRaises(InternalServerError) as context:
            PatientResourceHandler.bulk_create_patient_resource(
                mock_wsgi_req,
                resource_ids=["5668560948953088"],
                empi="P151024892",
                user_id="user_57",
                categories=["Housing"],
                comment="comment",
                phone_number="8888888888",
                email="btrehearne2wi@un.org",
                preferred_mode_of_contact=["Message", "Email"],
                referral_consent_given=True,
            )

        self.assertEqual(context.exception.status_code, 500)
