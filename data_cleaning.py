

import logging
import re

def clean_data(input_path, output_path, regex=None):
    """
    Cleans the data in a given file, optionally removing patterns with regex.
    """
    logging.info(f"Starting data cleaning for {input_path}...")
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        cleaned_lines = []
        for line in lines:
            line = line.strip()
            if regex:
                line = re.sub(regex, '', line) # Remove the pattern
            if line: # Keep non-empty lines after regex removal
                cleaned_lines.append(line)

        # Remove duplicate lines
        cleaned_lines = list(set(cleaned_lines))

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(cleaned_lines))

        logging.info(f"Successfully cleaned data and saved to {output_path}")
    except FileNotFoundError:
        logging.error(f"File not found at {input_path} during cleaning.")
    except Exception as e:
        logging.error(f"An unexpected error occurred during cleaning: {e}")

