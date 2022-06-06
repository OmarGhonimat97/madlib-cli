"""Tests for file_io.py"""


from madlib.file_io import read_template, parse_template, merge
import pytest


# Test read


def test_read_file():
    """Testing read_file for successful file read"""
    filename = 'sample'
    assert read_template(filename) == 'hello!\n'


def test_read_no_file():
    """Test read_file for file couldn't be found"""
    filename = 'asdf'
    with pytest.raises(FileNotFoundError):
        read_template(filename)


def test_read_type_error():
    """Test read_file for wrong input type"""
    filename = {}
    with pytest.raises(TypeError):
        read_template(filename)


# Test write


def test_write_file():
    """Testing write_file for successful write by writing then reading"""
    filename = 'test'
    content = 'hello!'

    parse_template(content, filename)
    assert read_template(filename) == 'hello!'


def test_incorrect_input():
    """Testing write_file for incorrect input"""
    content = 'hi'
    filename = {}

    with pytest.raises(TypeError):
        parse_template (content, filename)

    content = {}
    filename = 'hi'

    with pytest.raises(TypeError):
        parse_template (content, filename)

def test_merge():
    pass