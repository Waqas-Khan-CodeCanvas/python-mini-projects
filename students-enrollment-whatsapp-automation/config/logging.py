import logging

logging.basicConfig(filename='../output/whatsapp_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info(f"Message sent to {row['Name']} ({phone})")
