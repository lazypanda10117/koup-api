from app import app

# Enforce strict slashes (redirect '/...' to '/.../').
app.url_map.strict_slashes = True
