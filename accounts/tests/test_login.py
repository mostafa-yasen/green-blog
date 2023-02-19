from django.test import TestCase


class TestLogin(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get("/accounts/login/")

    def test_login_status_code_is_200(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_login_view_has_login_link(self) -> None:
        self.assertContains(self.response, "login", 2)

    def test_login_view_doesnt_contain_logout_link(self) -> None:
        self.assertNotContains(self.response, "logout")
