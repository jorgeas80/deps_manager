import pytest


class TestInputFileRead:
    @pytest.fixture
    def file_input_path(self):
        return "/this/is/a/fake/path.txt"

    def test_file_does_not_exist(self, file_input_path):
        assert False

    def test_file_is_not_plain_text(self, file_input_path):
        assert False

    def test_file_can_be_properly_read(self, file_input_path):
        assert False
