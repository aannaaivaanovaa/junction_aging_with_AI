# Junction Aging Program - Voice Call Script Generator

A Python program to generate personalized voice call scripts for aging care programs. This tool helps caregivers and automated systems create natural, empathetic scripts for wellness checks, medication reminders, emergency contacts, and social engagement calls.

## Features

- **Wellness Check Scripts**: Generate comprehensive health check-in scripts
- **Medication Reminders**: Create personalized medication reminder scripts
- **Emergency Contact Scripts**: Generate scripts for contacting emergency contacts
- **Social Engagement Scripts**: Create scripts to promote social connection and activities
- **User Data Management**: Store and manage user information including medications, health conditions, and emergency contacts
- **Customizable**: Support for different times of day and personalized notes

## Installation

This is a standalone Python program with no external dependencies (uses only Python standard library).

Requirements:
- Python 3.7 or higher

## Usage

### Basic Usage

Generate a wellness check script:
```bash
python generate_script.py example_users/user_margaret.json
```

### Command Line Options

```bash
python generate_script.py <user_file> [options]

Options:
  --type {wellness,medication,emergency,social}
                        Type of call script to generate (default: wellness)
  --time {morning,afternoon,evening}
                        Time of day for medication reminders (default: morning)
  --reason REASON      Reason for emergency contact (default: "No response from user")
  --output OUTPUT      Output file path (default: print to console)
```

### Examples

1. **Generate a wellness check script:**
   ```bash
   python generate_script.py example_users/user_margaret.json --type wellness
   ```

2. **Generate a morning medication reminder:**
   ```bash
   python generate_script.py example_users/user_robert.json --type medication --time morning
   ```

3. **Generate an emergency contact script:**
   ```bash
   python generate_script.py example_users/user_margaret.json --type emergency --reason "User reported feeling unwell"
   ```

4. **Generate a social engagement script:**
   ```bash
   python generate_script.py example_users/user_robert.json --type social
   ```

5. **Save script to file:**
   ```bash
   python generate_script.py example_users/user_margaret.json --type wellness --output wellness_script.txt
   ```

## User Data Format

User data should be stored in JSON format with the following structure:

```json
{
  "name": "Margaret Smith",
  "age": 78,
  "medications": [
    "Lisinopril 10mg - for blood pressure",
    "Metformin 500mg - for diabetes"
  ],
  "health_conditions": [
    "Hypertension",
    "Type 2 Diabetes"
  ],
  "emergency_contact_name": "Sarah Johnson (daughter)",
  "emergency_contact_phone": "+1-555-0123",
  "preferred_call_time": "10:00 AM",
  "language_preference": "English",
  "special_notes": "Prefers calls in the morning. Hard of hearing in left ear."
}
```

### Required Fields
- `name`: User's full name
- `age`: User's age (must be positive)
- `medications`: List of medications (can be empty list)
- `health_conditions`: List of health conditions (can be empty list)
- `emergency_contact_name`: Name of emergency contact
- `emergency_contact_phone`: Phone number of emergency contact
- `preferred_call_time`: Preferred time for calls

### Optional Fields
- `language_preference`: Preferred language (default: "English")
- `special_notes`: Any special instructions or notes

## Project Structure

```
junction_aging_with_AI/
├── README.md                    # This file
├── user_data.py                 # User data model
├── voice_call_script.py         # Script generator
├── generate_script.py           # Main CLI application
└── example_users/               # Example user data files
    ├── user_margaret.json
    └── user_robert.json
```

## Script Types

### 1. Wellness Check
Comprehensive health and wellness check-in including:
- General health status
- Specific health condition monitoring
- Daily activities (meals, hydration, sleep)
- Social connection check

### 2. Medication Reminder
Medication reminder script including:
- List of medications to take
- Confirmation questions
- Supply check
- Important reminders about proper medication use

### 3. Emergency Contact
Emergency notification script for contacting caregivers including:
- Alert reason
- User health information
- Current medications
- Recommended actions

### 4. Social Engagement
Social connection and activities script including:
- Activity engagement questions
- Social connection check
- Community activity suggestions
- Mental wellness check

## Development

### Running Tests

(No tests are currently implemented as this is a minimal working implementation)

### Contributing

This is a Junction hackathon project. Feel free to fork and extend with additional features.

## License

This project is open source and available for use in aging care programs.

## Support

For questions or issues, please open an issue on the GitHub repository.
