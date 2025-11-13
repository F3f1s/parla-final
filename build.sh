#!/usr/bin/env bash

# Build script para Render
echo "Building application..."

# Install dependencies
pip install -r requirements.txt

# Initialize database if needed
python -c "from utils.db import init_db; init_db()"

echo "Build complete!"
