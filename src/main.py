# This is a sample main file for the project

import os
from logger.main import setup_logging

def main():
    log_file = os.path.join(os.path.dirname(__file__), "..", "logs", "app.log")
    setup_logging(log_file)

    try:
        # Your main project code goes here

        # Example: Database connection
        logging.info("Connecting to the database...")
        # Your database connection code here

        # Example: API request
        logging.info("Making API request...")
        # Your API request code here

        logging.info("Project execution successful.")
    except Exception as e:
        # Log any exceptions
        logging.exception("An error occurred: %s", str(e))
        print("Error: Check the logs for details.")

if __name__ == "__main__":
    import logging
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    main()
