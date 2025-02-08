import pytest
from bs4 import BeautifulSoup
import numpy as np
from workflow.DB_get_users_following_list import get_followers, get_following, get_member_id, get_data


def test_get_followers():
    html_content = """
    <div>
        <h4 class="block-textHeader">Followers</h4>
        <div>
            <a class="avatar avatar--s" data-user-id="123"></a>
            <a class="avatar avatar--s" data-user-id="456"></a>
            <a data-xf-click="overlay">Show all 100 »</a>
        </div>
    </div>
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    assert get_followers(soup) == 102

    html_content = """
    <div>
    </div>
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    assert get_followers(soup) == 0


def test_get_following():
    html_content = """
    <div>
        <h4 class="block-textHeader">Following</h4>
        <div>
            <a class="avatar avatar--s" data-user-id="789"></a>
            <a class="avatar avatar--s" data-user-id="101"></a>
            <a data-xf-click="overlay">Show all 200 »</a>
        </div>
    </div>
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    assert get_following(soup) == 202

    html_content = """
    <div>
    </div>
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    assert get_following(soup) == 0


def test_get_member_id():
    html_content = '<meta property="og:url" content="https://kiwifarms.st/members/.12345/"/>'
    soup = BeautifulSoup(html_content, 'html.parser')
    assert get_member_id(soup) == 12345

    html_content = '<meta property="og:url" content="https://kiwifarms.st/members/12345/"/>'
    soup = BeautifulSoup(html_content, 'html.parser')
    assert get_member_id(soup) == 12345

    html_content = '<div></div>'
    soup = BeautifulSoup(html_content, 'html.parser')
    assert get_member_id(soup) is None


def test_get_data():
    html_content = """
    <meta property="og:url" content="https://kiwifarms.st/members/.12345/"/>
    <div>
        <h4 class="block-textHeader">Followers</h4>
        <div>
            <a class="avatar avatar--s" data-user-id="123"></a>
            <a data-xf-click="overlay">Show all 100 »</a>
        </div>
        <h4 class="block-textHeader">Following</h4>
        <div>
            <a class="avatar avatar--s" data-user-id="789"></a>
            <a data-xf-click="overlay">Show all 200 »</a>
        </div>
    </div>
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    data = get_data(soup)
    assert data['member_id'] == 12345
    assert data['followers'] == 101
    assert data['following'] == 201

    html_content = '<div></div>'
    soup = BeautifulSoup(html_content, 'html.parser')
    assert get_data(soup) is None
