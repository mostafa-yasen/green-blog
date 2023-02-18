from django.test import TestCase


class TestUserRegistration(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get("/accounts/create")

    def test_status_code_is_200(self) -> None:
        self.assertEqual(self.response.status_code, 200)

    def test_view_has_login_link(self) -> None:
        self.assertContains(self.response, "login", 1)

    def test_view_has_register_link(self) -> None:
        self.assertContains(self.response, "Register Account", 1)

    def test_view_doesnt_contain_logout_link(self) -> None:
        self.assertNotContains(self.response, "logout")
