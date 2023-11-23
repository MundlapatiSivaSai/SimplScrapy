from app import app
import os

if __name__ == "__main__":
    # Get the PORT environment variable (set by Render), default to 5000 if not set
    port = int(os.environ.get('PORT', 5000))
    
    # Bind to 0.0.0.0 to make the application accessible on all public IPs
    # Set debug to False for production deployment
    app.run(host='0.0.0.0', port=port, debug=False)
