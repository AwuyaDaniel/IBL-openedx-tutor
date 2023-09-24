#!/bin/bash

# Define the repository URL and destination directory
REPO_URL="https://github.com/yourusername/yourrepo.git"
DESTINATION_DIR="/openedx/edx-platform"

# Clone the repository
git clone "$REPO_URL" "$DESTINATION_DIR"
