from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import List


@dataclass
class Experience:
    title: str
    company_name: str
    start_date: str
    end_date: str = None
    duration: str = None
    location: str = None
    company_url: str = None
    description: str = None


@dataclass
class Education:
    school: str
    school_url: str = None
    degree: str = None
    major: str = None
    grade: str = None


@dataclass
class LinkedinProfile:
    name: str
    linkedin_url: str
    profile_image_url: str
    headline: str = None
    about: str = None
    experience: List[Experience] = None
    education: List[Education] = None

    @classmethod
    def from_payload(cls, payload: Dict[str, Any]) -> LinkedinProfile:
        experience_list = [Experience(**exdata) for exdata in payload.pop("experience")]
        education_list = [Education(**eddata) for eddata in payload.pop("education")]
        return cls(experience=experience_list, education=education_list, **payload)