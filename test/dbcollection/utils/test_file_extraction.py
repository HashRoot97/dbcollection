#!/usr/bin/env python

"""
Test dbcollection/utils/file_extraction.py
"""


import os
import sys
import pytest
from unittest.mock import patch

dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = os.path.abspath(os.path.join(dir_path, '..', '..', '..'))
sys.path.append(lib_path)

from dbcollection.utils import file_extraction


@pytest.mark.parametrize('ext, method', [
    ('tar', file_extraction.extract_file_tar),
    ('gz',  file_extraction.extract_file_tar),
    ('zip', file_extraction.extract_file_zip),
])
def test_get_extractor_method__succeed(ext, method):
    assert file_extraction.get_extractor_method(ext) == method


@pytest.mark.parametrize('ext', [
    ('xml'), ('7zip'), ('ini'),
])
def test_get_extractor_method__raise(ext):
    with pytest.raises(KeyError):
        file_extraction.get_extractor_method(ext)


@patch('dbcollection.utils.file_extraction.get_extractor_method')
def test_extract_file__succeed(mock_get):
    def mock_return(a,b):
        return True

    mock_get.return_value = mock_return
    file_extraction.extract_file('fname1.test', 'path/dir/', False)
    assert mock_get.called


def test_extract_file__raise():
    with pytest.raises(KeyError):
        file_extraction.extract_file('fname1.test', 'path/dir/', False)
