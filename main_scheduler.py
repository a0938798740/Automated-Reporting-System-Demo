import argparse
import logging
from reports.daily_report import DailyReportGenerator
from utils.email_sender import EmailSender
import config

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_daily_job():
    # 1. Generate Report
    generator = DailyReportGenerator()
    report_path = generator.generate()

    # 2. Send Email
    if report_path:
        EmailSender.send_report(
            recipients=config.RECIPIENTS['daily'],
            subject="[Auto] Daily Energy Report",
            body="Please find attached the daily energy consumption report.",
            attachment_path=report_path
        )
    else:
        logging.warning("Skipping email: No report generated.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Reporting Scheduler")
    parser.add_argument('--type', type=str, choices=['daily', 'weekly', 'monthly'], required=True)
    
    args = parser.parse_args()

    if args.type == 'daily':
        run_daily_job()
    elif args.type == 'weekly':
        logging.info("Weekly report logic would run here...")
    elif args.type == 'monthly':
        logging.info("Monthly report logic would run here...")
