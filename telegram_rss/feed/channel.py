import attr
from telegram_rss.utils import sanitize_text


@attr.dataclass
class Channel:
    title: str
    link: str
    description: str

    def __attr_post_init__(self) -> None:
        self.title = sanitize_text(self.title)
        self.description = sanitize_text(self.description)

    def __str__(self):
        return self.title

    @property
    def text(self) -> str:
        text = f'<a href="{self.link}">{self.title}</a>\n'
        text += self.description
        return text