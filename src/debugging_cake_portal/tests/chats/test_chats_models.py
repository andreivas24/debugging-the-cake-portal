import pytest
from chats.models.chatroom_model import ChatRoom


class TestChatRoom:
    @pytest.mark.django_db
    def test_create_chatroom(self):
        """
        Tests the creation of a chat room.
        """
        chatroom = ChatRoom.objects.create(
            name='Python',
            slug='python'
        )

        chatroom.save()
        assert chatroom.name == "Python"
        assert chatroom.slug == "python"


