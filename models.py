from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

@dataclass
class VideoMetadata:
    title: str
    publication_date: datetime
    channel: str
    quality: str
    views: int
    video_length: int

    def to_dict(self):
        return asdict(self)

@dataclass
class Transcription:
    text: str

    def to_dict(self):
        return asdict(self)