import pandas as pd
import pdfquery
import os

CHASE_PATH = r"C:\Users\marti\My Drive (martin.prusa777@gmail.com)\Accounts\Chase"
AMEX_PATH = r"C:\Users\marti\My Drive (martin.prusa777@gmail.com)\Accounts\Amex"

def pdf_chase_single():
    chase = pdfquery.PDFQuery(os.path.join(CHASE_PATH, "\Saver\Statement_for_01_April_2024_to_30_April_2024"))
    return chase