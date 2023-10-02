#!/bin/bash

# Define the repository URL and destination directory
REPO_URL="https://github.com/AwuyaDaniel/IBL.git"
DESTINATION_DIR="/openedx/edx-platform/"

# Check if the "IBL" folder exists in the destination directory
if [ -d "$DESTINATION_DIR/IBL" ]; then
    echo "IBL folder already exists. Going into it and running git pull..."
    cd "$DESTINATION_DIR/IBL"
    git pull
else
    # Clone the repository
    echo "Cloning the IBL repository..."
    git clone "$REPO_URL" "$DESTINATION_DIR/IBL"
fi

# Copy the "IBL" folder to the specified location
cp -r "$DESTINATION_DIR/IBL" "$DESTINATION_DIR/lms/djangoapps"

# Navigate to the edx-platform directory
cd "$DESTINATION_DIR"
#
# Run the following commands
#python manage.py lms makemigrations
#python manage.py lms migrate
cd ..
source venv/bin/activate
pip install git+https://github.com/AwuyaDaniel/IBL-openedx-tutor.git
cd "$DESTINATION_DIR"
python manage.py lms makemigrations
python manage.py lms migrate