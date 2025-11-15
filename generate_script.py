#!/usr/bin/env python3
"""Main script to generate voice call scripts for aging program."""

import json
import argparse
import sys
from pathlib import Path
from user_data import UserData
from voice_call_script import VoiceCallScriptGenerator


def load_user_from_json(json_file: str) -> UserData:
    """Load user data from JSON file.
    
    Args:
        json_file: Path to JSON file containing user data
        
    Returns:
        UserData object
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If JSON is invalid or missing required fields
    """
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    return UserData(**data)


def save_script_to_file(script: str, output_file: str):
    """Save generated script to a file.
    
    Args:
        script: The generated script text
        output_file: Path to output file
    """
    with open(output_file, 'w') as f:
        f.write(script)
    print(f"Script saved to: {output_file}")


def main():
    """Main entry point for the voice call script generator."""
    parser = argparse.ArgumentParser(
        description="Generate personalized voice call scripts for aging care program"
    )
    parser.add_argument(
        'user_file',
        help='Path to user data JSON file'
    )
    parser.add_argument(
        '--type',
        choices=['wellness', 'medication', 'emergency', 'social'],
        default='wellness',
        help='Type of call script to generate (default: wellness)'
    )
    parser.add_argument(
        '--time',
        choices=['morning', 'afternoon', 'evening'],
        default='morning',
        help='Time of day for medication reminders (default: morning)'
    )
    parser.add_argument(
        '--reason',
        default='No response from user',
        help='Reason for emergency contact (default: "No response from user")'
    )
    parser.add_argument(
        '--output',
        help='Output file path (default: print to console)'
    )
    
    args = parser.parse_args()
    
    try:
        # Load user data
        user = load_user_from_json(args.user_file)
        
        # Create script generator
        generator = VoiceCallScriptGenerator(user)
        
        # Generate appropriate script
        if args.type == 'wellness':
            script = generator.generate_wellness_check()
        elif args.type == 'medication':
            script = generator.generate_medication_reminder(args.time)
        elif args.type == 'emergency':
            script = generator.generate_emergency_contact_script(args.reason)
        elif args.type == 'social':
            script = generator.generate_social_engagement_script()
        else:
            print(f"Unknown script type: {args.type}", file=sys.stderr)
            return 1
        
        # Output the script
        if args.output:
            save_script_to_file(script, args.output)
        else:
            print(script)
        
        return 0
        
    except FileNotFoundError:
        print(f"Error: User file '{args.user_file}' not found", file=sys.stderr)
        return 1
    except (ValueError, KeyError) as e:
        print(f"Error: Invalid user data - {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
