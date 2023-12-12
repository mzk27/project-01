#!/bin/bash

# Step 0: Create a sudo non-root user
echo "Creating sudo non-root user..."
adduser mzk
usermod -aG sudo mzk
echo "User 'mzk' created. Please set a password for 'mzk'."

# Step 1: Install the required packages
echo "Installing required packages..."
sudo apt update
sudo apt install -y python3-pip python3-dev nginx

# Step 2: Create a directory and set up a virtual environment
echo "Setting up the Flask application..."
mkdir myFlaskApp && cd myFlaskApp
virtualenv env
source env/bin/activate

# Step 3: Clone your Flask application code from GitHub
echo "Cloning your Flask application code from GitHub..."
git clone https://github.com/mzk27/project-01.git .
pip3 install -r requirements.txt  # Modify this line if you have a requirements file

# Step 4: Create a sample project and WSGI entry point
echo "Creating WSGI entry point..."
cat > wsgi.py <<EOL
from app import app

if __name__ == "__main__":
    app.run()
EOL

echo "Testing Gunicorn's ability to serve the project..."
gunicorn --bind 0.0.0.0:5000 wsgi:app

# Step 5: Create a systemd service
echo "Creating a systemd service..."
cat > /etc/systemd/system/app.service <<EOL
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=mzk
Group=www-data
WorkingDirectory=$(pwd)/
Environment="PATH=$(pwd)/env/bin"
ExecStart=$(pwd)/env/bin/gunicorn --workers 3 --bind unix:app.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
EOL

sudo systemctl start app
sudo systemctl enable app

# Step 6: Configure Nginx
echo "Configuring Nginx..."
cat > /etc/nginx/sites-available/app <<EOL
server {
    listen 80;
    server_name <server_ip or domain_name>;

    location / {
        include proxy_params;
        proxy_pass http://unix:$(pwd)/app.sock;
    }

    location /static {
        include /etc/nginx/mime.types;
        root $(pwd)/;
    }
}
EOL

sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
sudo systemctl restart nginx

# Step 7: Provide necessary Permissions
echo "Setting up necessary permissions..."
sudo chmod 775 -R $(pwd)
sudo systemctl restart nginx

echo "Deployment completed successfully!"
