import pytest


class TestCommands:
    @pytest.fixture
    def install_command(self):
        return "INSTALL item1"

    @pytest.fixture
    def remove_command(self):
        return "REMOVE item1"

    @pytest.fixture
    def list_command(self):
        return "LIST"

    @pytest.fixture
    def end_command(self):
        return "END"

    @pytest.fixture
    def depend_command(self):
        return "DEPEND item1 item2 item3"

    @pytest.fixture
    def wrong_depend_command(self):
        return "DEPEND item1"

    @pytest.fixture
    def unexistent_command(self):
        return "NOPE"
