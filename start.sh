#!/bin/bash
echo "🔄 Installing dependencies..."
pip install -r requirements.txt

echo "🚀 Starting Freqtrade in dry-run mode..."
freqtrade trade --config config.json --strategy MyStrategy --dry-run