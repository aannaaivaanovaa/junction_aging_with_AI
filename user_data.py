"""User data model for the aging program."""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class UserData:
    """Represents user information for personalized voice calls."""
    
    name: str
    age: int
    medications: List[str]
    health_conditions: List[str]
    emergency_contact_name: str
    emergency_contact_phone: str
    preferred_call_time: str
    language_preference: str = "English"
    special_notes: Optional[str] = None
    
    def __post_init__(self):
        """Validate user data."""
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        if not self.name:
            raise ValueError("Name is required")
        if not self.emergency_contact_name:
            raise ValueError("Emergency contact name is required")
        if not self.emergency_contact_phone:
            raise ValueError("Emergency contact phone is required")
