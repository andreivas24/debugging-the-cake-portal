from django import urls
import pytest
from chats.views.chatrooms_view import chatrooms_view
from chats.views.room_view import room_view


@pytest.mark.parametrize('param', [chatrooms_view])
def test_render_chatroom_view(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 302


@pytest.mark.parametrize('param', [room_view])
def test_render_room_view(client, param):
    temp_url = urls.reverse(param,  args=['slug'])
    resp = client.get(temp_url)
    assert resp.status_code == 302
