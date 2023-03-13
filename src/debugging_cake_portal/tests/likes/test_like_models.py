import pytest
from like.models import Like


class TestChatRoom:
    @pytest.mark.django_db
    def test_create_like(self):
        """
        Tests the creation of a chat room.
        """
        like = Like.objects.create(
            user=1,
            post=2,
            value=True,
        )

        like.save()
        assert like.user == 1
        assert like.post == 2
        assert like.value == True
