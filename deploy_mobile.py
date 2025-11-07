#!/usr/bin/env python3
"""
Mobile Deployment Helper for Botanical Notebooks

This script helps convert Jupyter notebooks to mobile-friendly web apps
using Mercury framework.

Usage:
    python deploy_mobile.py notebook.ipynb
    python deploy_mobile.py --all  # Convert all notebooks
    python deploy_mobile.py --serve notebook.ipynb  # Run locally
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

def install_mercury():
    """Ensure Mercury is installed"""
    try:
        import mercury
        print("✅ Mercury is already installed")
    except ImportError:
        print("📦 Installing Mercury...")
        subprocess.run([sys.executable, "-m", "pip", "install", "mercury"], check=True)
        print("✅ Mercury installed successfully")

def add_mobile_metadata(notebook_path):
    """Add Mercury metadata to notebook for mobile optimization"""
    import json

    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Add Mercury configuration
    if 'mercury' not in nb.get('metadata', {}):
        nb.setdefault('metadata', {})['mercury'] = {
            'title': Path(notebook_path).stem.replace('_', ' ').title(),
            'description': 'Mobile-optimized botanical analysis tool',
            'show_code': False,
            'show_prompt': False,
            'share': 'public'
        }

        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1)

        print(f"📱 Added mobile metadata to {notebook_path}")

def run_mobile_app(notebook_path):
    """Run notebook as Mercury web app"""
    install_mercury()

    if not os.path.exists(notebook_path):
        print(f"❌ Notebook not found: {notebook_path}")
        return

    add_mobile_metadata(notebook_path)

    print(f"🚀 Starting mobile web app: {notebook_path}")
    print("📱 Open http://localhost:8000 in your mobile browser")
    print("Press Ctrl+C to stop")

    try:
        subprocess.run([
            sys.executable, "-m", "mercury", "run",
            notebook_path, "--port", "8000", "--host", "0.0.0.0"
        ], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Mobile app stopped")

def deploy_to_mercury_cloud(notebook_path):
    """Deploy to Mercury Cloud for public mobile access"""
    install_mercury()
    add_mobile_metadata(notebook_path)

    print("☁️ Deploying to Mercury Cloud...")
    print("This will create a shareable mobile-friendly link")

    try:
        subprocess.run([
            sys.executable, "-m", "mercury", "deploy", notebook_path
        ], check=True)
        print("✅ Deployed successfully! Check your Mercury dashboard for the link.")
    except subprocess.CalledProcessError:
        print("❌ Deployment failed. Make sure you're logged in: mercury login")

def find_notebooks():
    """Find all notebooks in the project"""
    notebooks = []
    for root, dirs, files in os.walk('notebooks'):
        for file in files:
            if file.endswith('.ipynb'):
                notebooks.append(os.path.join(root, file))
    return notebooks

def main():
    parser = argparse.ArgumentParser(description='Deploy notebooks as mobile web apps')
    parser.add_argument('notebook', nargs='?', help='Path to notebook file')
    parser.add_argument('--all', action='store_true', help='Process all notebooks')
    parser.add_argument('--serve', action='store_true', help='Run as local web app')
    parser.add_argument('--deploy', action='store_true', help='Deploy to Mercury Cloud')
    parser.add_argument('--setup', action='store_true', help='Setup mobile deployment environment')

    args = parser.parse_args()

    if args.setup:
        install_mercury()
        print("📱 Mobile deployment environment ready!")
        return

    if args.all:
        notebooks = find_notebooks()
        print(f"📓 Found {len(notebooks)} notebooks")

        for nb in notebooks:
            if args.deploy:
                deploy_to_mercury_cloud(nb)
            else:
                add_mobile_metadata(nb)

        print("✅ Processed all notebooks")
        return

    if not args.notebook:
        parser.print_help()
        return

    notebook_path = args.notebook

    if args.serve:
        run_mobile_app(notebook_path)
    elif args.deploy:
        deploy_to_mercury_cloud(notebook_path)
    else:
        add_mobile_metadata(notebook_path)
        print(f"📱 Prepared {notebook_path} for mobile deployment")
        print("💡 Run with: python deploy_mobile.py --serve notebook.ipynb")

if __name__ == '__main__':
    main()