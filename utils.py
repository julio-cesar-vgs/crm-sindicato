from datetime import datetime
from flask import abort

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date() if date_str else None
    except ValueError:
        abort(400, description='Formato de data inválido. Use YYYY-MM-DD.')
