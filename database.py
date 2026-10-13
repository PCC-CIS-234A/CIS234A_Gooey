
import pyodbc


SERVER = "cisdbss.pcc.edu"
DATABASE = "CIS234A_Gooey"
USERNAME = "CIS234A_Gooey"
DRIVER = "{ODBC Driver 18 for SQL Server}"


def get_connection(password):
    """Connect to the team's PCC SQL Server database."""

    connection_string = (
        f"DRIVER={DRIVER};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        "Connection Timeout=15;"
    )

    return pyodbc.connect(connection_string)
