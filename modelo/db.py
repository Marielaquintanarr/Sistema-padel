import os
from supabase import create_client, Client

def get_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        print('No se encontraron las variables en el entorno')
        return None
    else:
        return create_client(url, key)
    
db = get_client()
import os

print("URL:", os.getenv("SUPABASE_URL"))
print("KEY:", os.getenv("SUPABASE_KEY"))
