from unittest import TestCase, mock

from novu.helpers import SentryProxy


class HelpersTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        SentryProxy().import_module()

    @mock.patch("importlib.import_module")
    def test_sentry_proxy_import_module_no_sentry(self, mock_import_module: mock.MagicMock):
        mock_import_module.side_effect = ModuleNotFoundError
        SentryProxy().import_module()
        mock_import_module.assert_called_once_with("sentry_sdk")

        SentryProxy().set_extra("test", "test")

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

        SentryProxy().import_module()
