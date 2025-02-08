import os
import logging
import pytest
from bs4 import BeautifulSoup
from unittest.mock import MagicMock
from kiwifarmer import base
from workflow.EA_insert_trophies import PAGE_DIR, DATABASE

import mysql.connector

# Mocking os.getenv for tests
@pytest.fixture(autouse=True)
def mock_os_getenv(monkeypatch):
    monkeypatch.setenv('KIWIFARMER_USER', 'test_user')
    monkeypatch.setenv('KIWIFARMER_PASSWORD', 'test_password')

@pytest.fixture
def mock_cursor():
    cursor = MagicMock()
    return cursor

@pytest.fixture
def mock_cnx():
    cnx = MagicMock()
    return cnx

@pytest.fixture
def mock_trophy_page():
    trophy_page = MagicMock()
    trophy_page.trophy_insertions = [('trophy1', 'user1'), ('trophy2', 'user2')]
    return trophy_page

def test_database_connection_success(monkeypatch, mock_cnx, mock_cursor):
    monkeypatch.setattr(mysql.connector, 'connect', MagicMock(return_value=mock_cnx))
    mock_cnx.cursor.return_value = mock_cursor
    try:
        cnx = mysql.connector.connect(
            user=os.getenv('KIWIFARMER_USER'),
            password=os.getenv('KIWIFARMER_PASSWORD'),
            host='127.0.0.1',
            database=DATABASE,
            charset='utf8mb4',
            collation='utf8mb4_bin',
            use_unicode=True
        )
        cursor = cnx.cursor()
        assert cnx is not None
        assert cursor is not None
    except mysql.connector.Error as err:
        pytest.fail(f"Database connection failed: {err}")

def test_database_connection_failure(monkeypatch):
    monkeypatch.setattr(mysql.connector, 'connect', MagicMock(side_effect=mysql.connector.Error("Failed to connect")))
    with pytest.raises(SystemExit) as excinfo:
        try:
            cnx = mysql.connector.connect(
                user=os.getenv('KIWIFARMER_USER'),
                password=os.getenv('KIWIFARMER_PASSWORD'),
                host='127.0.0.1',
                database=DATABASE,
                charset='utf8mb4',
                collation='utf8mb4_bin',
                use_unicode=True
            )
        except mysql.connector.Error as err:
            assert str(err) == "Failed to connect"
            raise SystemExit(1)
    assert excinfo.value.code == 1

def test_trophy_page_processing_success(monkeypatch, mock_cursor, mock_cnx, mock_trophy_page):
    monkeypatch.setattr(mysql.connector, 'connect', MagicMock(return_value=mock_cnx))
    mock_cnx.cursor.return_value = mock_cursor
    monkeypatch.setattr(os, 'listdir', MagicMock(return_value=['test_page.html']))
    monkeypatch.setattr(BeautifulSoup, '__init__', MagicMock(return_value=None))
    monkeypatch.setattr(BeautifulSoup, 'read', MagicMock(return_value="<html></html>"))
    monkeypatch.setattr(base, 'TrophyPage', MagicMock(return_value=mock_trophy_page))
    mock_cursor.executemany = MagicMock()
    mock_cnx.commit = MagicMock()
    mock_cursor.close = MagicMock()
    mock_cnx.close = MagicMock()

    try:
        cnx = mysql.connector.connect(
            user=os.getenv('KIWIFARMER_USER'),
            password=os.getenv('KIWIFARMER_PASSWORD'),
            host='127.0.0.1',
            database=DATABASE,
            charset='utf8mb4',
            collation='utf8mb4_bin',
            use_unicode=True
        )
        cursor = cnx.cursor()
        pages = os.listdir(PAGE_DIR)
        for i, page_file in enumerate(pages):
            with open(os.path.join(PAGE_DIR, page_file), 'r') as f:
                user_page = BeautifulSoup(f.read(), 'lxml')
            trophy_page = base.TrophyPage(user_page=user_page)
            cursor.executemany("TEMPLATE", trophy_page.trophy_insertions)
        cnx.commit()
    except Exception as e:
        pytest.fail(f"Processing failed: {e}")

    mock_cursor.executemany.assert_called()
    mock_cnx.commit.assert_called()
    mock_cursor.close.assert_called()
    mock_cnx.close.assert_called()

def test_trophy_page_processing_failure(monkeypatch, mock_cursor, mock_cnx):
    monkeypatch.setattr(mysql.connector, 'connect', MagicMock(return_value=mock_cnx))
    mock_cnx.cursor.return_value = mock_cursor
    monkeypatch.setattr(os, 'listdir', MagicMock(return_value=['test_page.html']))
    monkeypatch.setattr(BeautifulSoup, '__init__', MagicMock(return_value=None))
    monkeypatch.setattr(BeautifulSoup, 'read', MagicMock(side_effect=Exception("Failed to read HTML")))
    mock_cursor.close = MagicMock()
    mock_cnx.close = MagicMock()

    try:
        cnx = mysql.connector.connect(
            user=os.getenv('KIWIFARMER_USER'),
            password=os.getenv('KIWIFARMER_PASSWORD'),
            host='127.0.0.1',
            database=DATABASE,
            charset='utf8mb4',
            collation='utf8mb4_bin',
            use_unicode=True
        )
        cursor = cnx.cursor()
        pages = os.listdir(PAGE_DIR)
        for i, page_file in enumerate(pages):
            with open(os.path.join(PAGE_DIR, page_file), 'r') as f:
                user_page = BeautifulSoup(f.read(), 'lxml')
            trophy_page = base.TrophyPage(user_page=user_page)
            cursor.executemany("TEMPLATE", trophy_page.trophy_insertions)
        cnx.commit()
    except Exception as e:
        assert str(e) == "Failed to read HTML"

    mock_cursor.close.assert_called()
    mock_cnx.close.assert_called()

def test_database_commit_failure(monkeypatch, mock_cursor, mock_cnx):
    monkeypatch.setattr(mysql.connector, 'connect', MagicMock(return_value=mock_cnx))
    mock_cnx.cursor.return_value = mock_cursor
    monkeypatch.setattr(os, 'listdir', MagicMock(return_value=['test_page.html']))
    monkeypatch.setattr(BeautifulSoup, '__init__', MagicMock(return_value=None))
    monkeypatch.setattr(BeautifulSoup, 'read', MagicMock(return_value="<html></html>"))
    monkeypatch.setattr(base, 'TrophyPage', MagicMock())
    mock_cnx.commit = MagicMock(side_effect=mysql.connector.Error("Commit failed"))
    mock_cursor.close = MagicMock()
    mock_cnx.close = MagicMock()

    try:
        cnx = mysql.connector.connect(
            user=os.getenv('KIWIFARMER_USER'),
            password=os.getenv('KIWIFARMER_PASSWORD'),
            host='127.0.0.1',
            database=DATABASE,
            charset='utf8mb4',
            collation='utf8mb4_bin',
            use_unicode=True
        )
        cursor = cnx.cursor()
        pages = os.listdir(PAGE_DIR)
        for i, page_file in enumerate(pages):
            with open(os.path.join(PAGE_DIR, page_file), 'r') as f:
                user_page = BeautifulSoup(f.read(), 'lxml')
            trophy_page = base.TrophyPage(user_page=user_page)
            cursor.executemany("TEMPLATE", trophy_page.trophy_insertions)
        cnx.commit()
    except mysql.connector.Error as e:
        assert str(e) == "Commit failed"
    finally:
        mock_cursor.close.assert_called()
        mock_cnx.close.assert_called()