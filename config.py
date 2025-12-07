"""
Configuration for Automated Reporting System
"""

# Database Configuration
DB_HOST = 'localhost'
DB_USER = 'report_user'
DB_PASS = 'password'
DB_NAME = 'energy_data'

# Email Configuration
SMTP_SERVER = 'smtp.office365.com'
SMTP_PORT = 587
EMAIL_ACCOUNT = 'reports@company.com'
EMAIL_PASSWORD = 'password'

# Report Settings
# List of recipients for different report types
RECIPIENTS = {
    'daily': ['manager@company.com'],
    'weekly': ['manager@company.com', 'director@company.com'],
    'monthly': ['director@company.com', 'finance@company.com']
}

# Output Directory
OUTPUT_DIR = './generated_reports'
