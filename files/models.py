from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class File(models.Model):
    owner = models.ForeignKey('auth.User', related_name='files')
    title = models.CharField(max_length=100, blank=True, default='')
    image_source = models.TextField(default='')


    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code product.
        """
        lexer = get_lexer_by_name(self.language)
        options = self.title and {'title': self.title} or {}

        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(File, self).save(*args, **kwargs)


    class Meta:
        ordering = ('created',)