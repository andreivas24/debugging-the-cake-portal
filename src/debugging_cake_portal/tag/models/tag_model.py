from django.db import models
# from taggit.managers import TaggableManager
from ..validators.tag_validators import validate_tag_type


class Tag(models.Model):
    TAG_CHOICES = (
        ('PYTHON', 'PYTHON'),
        ('JAVA', 'JAVA'),
        ('DRUPAL', 'DRUPAL'),
        ('ANGULAR', 'ANGULAR'),
        ('JOS', 'JOS'),
        ('DOJ', 'DOJ')
    )
    # tag_type = models.CharField(choices=TAG_CHOICES, max_length=20, validators=[validate_tag_type])
    tagname = models.CharField(max_length=100, null=True, choices=TAG_CHOICES)

    def __str__(self):
        return self.tagname

    # def __str__(self):
    #     return self.name

    # color = models.CharField(max_length=20)

    # tags = TaggableManager()

    # def is_python(self):
    #     if self.tag_type == 'PYTHON':
    #         return True
    #     else:
    #         return False
    #
    # def is_java(self):
    #     if self.tag_type == 'JAVA':
    #         return True
    #     else:
    #         return False
    #
    # def is_drupal(self):
    #     if self.tag_type == 'DRUPAL':
    #         return True
    #     else:
    #         return False
    #
    # def is_angular(self):
    #     if self.tag_type == 'ANGULAR':
    #         return True
    #     else:
    #         return False
    #
    # def is_doj(self):
    #     if self.tag_type == 'DOJ':
    #         return True
    #     else:
    #         return False
    #
    # def is_jos(self):
    #     if self.tag_type == 'JOS':
    #         return True
    #     else:
    #         return False
