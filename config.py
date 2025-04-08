import pyodbc

DATABASE_CONFIG = {
    'DRIVER': '{MySQL ODBC 8.0 Driver}',  # Make sure this driver is installed inside the container
    'SERVER': 'vamsi-databse.cxue66ieak7c.ap-south-1.rds.amazonaws.com',
    'DATABASE': 'userdb',
    'UID': 'admin',
    'PWD': 'Svamsi79955',
}

try:
    conn = pyodbc.connect(
        f"DRIVER={DATABASE_CONFIG['DRIVER']};"
        f"SERVER={DATABASE_CONFIG['SERVER']};"
        f"DATABASE={DATABASE_CONFIG['DATABASE']};"
        f"UID={DATABASE_CONFIG['UID']};"
        f"PWD={DATABASE_CONFIG['PWD']};"
        "OPTION=3;"  # For default behavior
    )
    print("✅ Database Connection Successful!")
except Exception as e:
    print(f"❌ Database Connection Failed: {e}")
