# Jazz Standards Webpage

A beautiful webpage showcasing the top 50 jazz standards with YouTube videos and links to lyrics.

## Features

- Top 50 iconic jazz standards
- Embedded YouTube videos for each song
- Composer and year information
- Links to licensed lyrics sources
- Responsive design with elegant styling
- Quick navigation table of contents

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python app.py
```

Then open your browser to `http://localhost:5001`

## Usage Options

### Option 1: Static Site (GitHub Pages)

The site is available as a pre-generated static HTML page (`index.html`) that can be:
- Opened directly in your browser
- Hosted on GitHub Pages (instructions below)
- Deployed to any static hosting service

### Option 2: FastHTML Dynamic Application

Run the live FastHTML server:

```bash
pip install -r requirements.txt
python app.py
```

Then open your browser to `http://localhost:5001`

## Generating Static HTML from FastHTML

The `index.html` file is generated from FastHTML components, ensuring a single source of truth. To regenerate the static site:

```bash
pip install -r requirements.txt
python generate_static.py
```

This script:
- Uses FastHTML components from `app.py`
- Generates a standalone HTML file
- Includes all 50 jazz standards with embedded videos
- Requires no dependencies to view (pure HTML/CSS)

**Benefits:**
- Maintain data in one place (app.py)
- Easy to update songs or styling
- Regenerate static site anytime with one command

## Deploying to GitHub Pages

1. Go to your repository settings on GitHub
2. Navigate to "Pages" in the left sidebar
3. Under "Source", select the branch you want to deploy (e.g., `main`)
4. Click "Save"
5. Your site will be published at `https://yourusername.github.io/jazz-standards/`

## Note on Lyrics

Due to copyright restrictions, this webpage does not include full lyrics. Instead, it provides links to licensed lyrics sources like Genius and Musixmatch where you can find the official lyrics.