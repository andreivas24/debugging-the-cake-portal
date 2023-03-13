

from django import urls
import pytest


@pytest.mark.parametrize('param', [
    'cake_user:home',
    'cake_user:login',
])
def test_render_cake_user_200_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.parametrize('param', [
    'cake_user:logout'
])
def test_render_cake_user_logout_view(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 302


@pytest.mark.django_db
@pytest.mark.parametrize('param', [
    'cake_user:register'
])
def test_render_cake_user_register_view(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200

