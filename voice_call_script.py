"""Voice call script generator for aging program."""

from typing import List
from datetime import datetime
from user_data import UserData


class VoiceCallScriptGenerator:
    """Generates personalized voice call scripts for elderly care."""
    
    def __init__(self, user: UserData):
        """Initialize with user data.
        
        Args:
            user: UserData object containing user information
        """
        self.user = user
    
    def generate_wellness_check(self) -> str:
        """Generate a wellness check-in script.
        
        Returns:
            Formatted voice call script for wellness check
        """
        script = f"""
=== WELLNESS CHECK-IN CALL SCRIPT ===
Date: {datetime.now().strftime('%Y-%m-%d')}
User: {self.user.name}

INTRODUCTION:
"Hello {self.user.name}, this is your wellness check-in call. I hope you're having a good day!"

HEALTH CHECK:
"How are you feeling today? Are you experiencing any discomfort or unusual symptoms?"
[Wait for response]

"""
        
        if self.user.health_conditions:
            script += f"""SPECIFIC HEALTH MONITORING:
"I'd like to check on your {', '.join(self.user.health_conditions)}. How have you been managing today?"
[Wait for response]

"""
        
        script += """DAILY ACTIVITIES:
"Have you been able to eat your meals today?"
[Wait for response]
"Have you had enough water to drink?"
[Wait for response]
"Did you get some rest or sleep well last night?"
[Wait for response]

SOCIAL CONNECTION:
"Have you spoken with family or friends today?"
[Wait for response]

"""
        
        if self.user.special_notes:
            script += f"""SPECIAL NOTES:
{self.user.special_notes}

"""
        
        script += f"""EMERGENCY CONTACT INFO:
Emergency Contact: {self.user.emergency_contact_name}
Phone: {self.user.emergency_contact_phone}

CLOSING:
"Thank you for taking the time to talk with me today, {self.user.name}. Please remember that help is available if you need it. Take care!"

=== END OF SCRIPT ===
"""
        return script
    
    def generate_medication_reminder(self, time_of_day: str = "morning") -> str:
        """Generate a medication reminder script.
        
        Args:
            time_of_day: Time of day for medication (morning, afternoon, evening)
            
        Returns:
            Formatted voice call script for medication reminder
        """
        script = f"""
=== MEDICATION REMINDER CALL SCRIPT ===
Date: {datetime.now().strftime('%Y-%m-%d')}
User: {self.user.name}
Time: {time_of_day.capitalize()}

INTRODUCTION:
"Hello {self.user.name}, this is your {time_of_day} medication reminder."

"""
        
        if self.user.medications:
            script += f"""MEDICATION LIST:
"It's time to take your medications. Here's what you should take now:"

"""
            for i, med in enumerate(self.user.medications, 1):
                script += f"{i}. {med}\n"
            
            script += """
[Wait for confirmation]

CONFIRMATION:
"Have you taken your medications?"
[Wait for response]

"Do you have enough supply of your medications, or do you need a refill soon?"
[Wait for response]

"""
        else:
            script += """NO MEDICATIONS RECORDED:
"I don't have any medications listed for you at this time. If you are taking any medications, please make sure they're updated in your profile."

"""
        
        script += f"""REMINDER:
"Remember to take your medications with water or food as directed by your doctor."

If you experience any side effects or have questions, please contact your healthcare provider or {self.user.emergency_contact_name} at {self.user.emergency_contact_phone}.

CLOSING:
"Thank you, {self.user.name}. Have a wonderful {time_of_day}!"

=== END OF SCRIPT ===
"""
        return script
    
    def generate_emergency_contact_script(self, reason: str = "No response from user") -> str:
        """Generate an emergency contact notification script.
        
        Args:
            reason: Reason for emergency contact
            
        Returns:
            Formatted voice call script for emergency contact
        """
        script = f"""
=== EMERGENCY CONTACT NOTIFICATION SCRIPT ===
Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
Contact: {self.user.emergency_contact_name}
Phone: {self.user.emergency_contact_phone}

INTRODUCTION:
"Hello, this is the aging care program calling regarding {self.user.name}."

ALERT NOTIFICATION:
"We are calling to inform you that: {reason}"

USER INFORMATION:
Name: {self.user.name}
Age: {self.user.age}

"""
        
        if self.user.health_conditions:
            script += f"""HEALTH CONDITIONS:
{self.user.name} has the following health conditions on record:
"""
            for condition in self.user.health_conditions:
                script += f"- {condition}\n"
            script += "\n"
        
        if self.user.medications:
            script += f"""CURRENT MEDICATIONS:
{self.user.name} is currently taking:
"""
            for med in self.user.medications:
                script += f"- {med}\n"
            script += "\n"
        
        script += f"""RECOMMENDED ACTION:
"We recommend checking on {self.user.name} as soon as possible to ensure their safety and well-being."

CLOSING:
"Please contact us if you need any additional information. Thank you."

=== END OF SCRIPT ===
"""
        return script
    
    def generate_social_engagement_script(self) -> str:
        """Generate a social engagement and activities script.
        
        Returns:
            Formatted voice call script for social engagement
        """
        script = f"""
=== SOCIAL ENGAGEMENT CALL SCRIPT ===
Date: {datetime.now().strftime('%Y-%m-%d')}
User: {self.user.name}

WARM GREETING:
"Hello {self.user.name}! I hope this call finds you well today."

ENGAGEMENT QUESTIONS:
"I wanted to check in and see how you're doing. What have you been up to today?"
[Wait for response]

ACTIVITY SUGGESTIONS:
"Have you had a chance to do any of your favorite activities lately?"
[Wait for response]

"Would you be interested in hearing about some activities happening in your community?"
[Options could include: virtual events, local senior center activities, online classes]
[Wait for response]

SOCIAL CONNECTION:
"Have you been in touch with your family or friends recently?"
[Wait for response]

"Is there anyone you'd like us to help you connect with?"
[Wait for response]

MENTAL WELLNESS:
"How has your mood been lately? Are you feeling happy and engaged?"
[Wait for response]

CLOSING:
"It's been wonderful talking with you, {self.user.name}. We'll check in with you again soon. Remember, you can always reach out if you need anything. Take care!"

EMERGENCY CONTACT (if needed):
Emergency Contact: {self.user.emergency_contact_name}
Phone: {self.user.emergency_contact_phone}

=== END OF SCRIPT ===
"""
        return script
