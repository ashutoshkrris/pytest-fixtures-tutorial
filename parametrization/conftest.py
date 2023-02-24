import pytest

from notes_app import NotesApp


@pytest.fixture
def app():
    """Returns an instance of the NotesApp class."""
    app = NotesApp()
    return app


@pytest.fixture
def app_without_notes(app):
    """Returns an instance of the NotesApp class with zero notes."""
    return app


@pytest.fixture
def app_with_notes(app):
    """Returns an instance of the NotesApp class with two notes."""
    app.add_note("Test note 1")
    app.add_note("Test note 2")
    return app


@pytest.fixture(params=[("Test note 1", "Note added successfully"),
                        ("Test note 2", "Note added successfully")])
def note_data(request):
    """Returns a tuple containing an input value and an expected output value for the add_note method."""
    return request.param
