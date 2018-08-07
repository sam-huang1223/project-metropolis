import logging

from ..src import test_scraping, extract_google_sheets, test_database_connection

logger = logging.getLogger(__name__)

def test_metropolis():
    print('Testing Google Drive API access -------------------')
    logger.info('Testing Google Drive API access -------------------')
    extract_google_sheets()
    logger.info('Success!')

    print('Testing Facebook Graph API access -----------------')
    logger.info('Testing Facebook Graph API access -----------------')
    test_scraping()
    logger.info('Success!')

    print('Testing Neo4j database connection -----------------')
    logger.info('Testing Neo4j database connection -----------------')
    test_database_connection()
    logger.info('Success!')