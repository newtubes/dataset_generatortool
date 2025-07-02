
import argparse
import logging
from utils import setup_logging
from data_collection import collect_data
from data_cleaning import clean_data
from data_preprocessing import preprocess_data

def main():
    parser = argparse.ArgumentParser(description="Dataset Generator Tool - A tool for collecting, cleaning, and preprocessing data for ML.")
    
    # Global arguments
    parser.add_argument('--log-file', type=str, default='C:/Users/Administrador/dataset_generator/dataset_generator.log', help='Path to the log file.')

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Collect data command
    collect_parser = subparsers.add_parser("collect", help="Collect data from a URL(s)")
    group = collect_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", type=str, help="The URL to collect data from")
    group.add_argument("--url-file", type=str, help="Path to a file containing URLs (one per line)")
    collect_parser.add_argument("output", type=str, help="The path for the output file")

    # Clean data command
    clean_parser = subparsers.add_parser("clean", help="Clean a data file")
    clean_parser.add_argument("input", type=str, help="The path to the input file to clean")
    clean_parser.add_argument("output", type=str, help="The path for the output file")
    clean_parser.add_argument("--regex", type=str, help="Optional: A regular expression pattern to remove from the text.")

    # Preprocess data command
    preprocess_parser = subparsers.add_parser("preprocess", help="Preprocess a data file")
    preprocess_parser.add_argument("input", type=str, help="The path to the input file to preprocess")
    preprocess_parser.add_argument("output", type=str, help="The path for the output file")
    preprocess_parser.add_argument("--language", type=str, default='english', help="The language for preprocessing (e.g., english, spanish, french)")

    args = parser.parse_args()
    
    # Setup logging
    setup_logging(args.log_file)

    logging.info(f"Executing command: '{args.command}'")

    if args.command == "collect":
        urls_to_collect = []
        if args.url:
            urls_to_collect.append(args.url)
        elif args.url_file:
            try:
                with open(args.url_file, 'r', encoding='utf-8') as f:
                    urls_to_collect = [line.strip() for line in f if line.strip()]
            except FileNotFoundError:
                logging.error(f"URL file not found at {args.url_file}")
                return
        collect_data(urls_to_collect, args.output)
    elif args.command == "clean":
        clean_data(args.input, args.output, args.regex)
    elif args.command == "preprocess":
        preprocess_data(args.input, args.output, args.language)
    
    logging.info("Dataset Generator Tool finished.")

if __name__ == "__main__":
    main()
