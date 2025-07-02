
import logging
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.tokenize import word_tokenize

def preprocess_data(input_path, output_path, language='english'):
    """
    Preprocesses the data in a given file with language-specific settings.
    """
    logging.info(f"Starting data preprocessing for {input_path} in {language}...")

    # Map friendly language names to nltk's internal names
    lang_map = {
        'english': 'english',
        'spanish': 'spanish',
        'portuguese': 'portuguese',
        'italian': 'italian',
        'french': 'french',
        'german': 'german'
    }

    if language not in lang_map:
        logging.error(f"Unsupported language: '{language}'. Supported languages are: {list(lang_map.keys())}")
        return

    nltk_lang = lang_map[language]

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            text = f.read()

        # 1. Tokenization
        tokens = word_tokenize(text)

        # 2. Lowercasing and keeping alphabetic tokens
        tokens = [token.lower() for token in tokens if token.isalpha()]

        # 3. Stopword removal
        try:
            stop_words = set(stopwords.words(nltk_lang))
            tokens = [token for token in tokens if token not in stop_words]
        except OSError:
            logging.warning(f"Stopwords for '{nltk_lang}' not found. You may need to download them using: python -m nltk.downloader stopwords")
            # Continue without stopwords if not available
            pass


        # 4. Stemming or Lemmatization
        if language == 'english':
            # Use Lemmatization for English for better results
            lemmatizer = WordNetLemmatizer()
            tokens = [lemmatizer.lemmatize(token) for token in tokens]
        else:
            # Use Stemming for other supported languages
            stemmer = SnowballStemmer(nltk_lang)
            tokens = [stemmer.stem(token) for token in tokens]

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(" ".join(tokens))

        logging.info(f"Successfully preprocessed data and saved to {output_path}")

    except FileNotFoundError:
        logging.error(f"File not found at {input_path} during preprocessing.")
    except Exception as e:
        logging.error(f"An unexpected error occurred during preprocessing: {e}")
