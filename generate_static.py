#!/usr/bin/env python3
"""
Generate static HTML file from FastHTML components
This allows us to maintain one source of truth and generate both dynamic and static versions
"""

from fasthtml.common import *

# Import data and components from app.py
from app import jazz_standards, create_song_card

def generate_page():
    """Generate the complete HTML page using FastHTML components"""
    return Html(
        Head(
            Title("Top 50 Jazz Standards"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            Style("""
                * {
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }

                body {
                    font-family: 'Georgia', serif;
                    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                    color: #333;
                    line-height: 1.6;
                    padding: 20px;
                }

                .container {
                    max-width: 1200px;
                    margin: 0 auto;
                    background: #fff;
                    border-radius: 10px;
                    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
                    padding: 40px;
                }

                .header {
                    text-align: center;
                    margin-bottom: 50px;
                    padding-bottom: 30px;
                    border-bottom: 3px solid #1e3c72;
                }

                .header h1 {
                    font-size: 3em;
                    color: #1e3c72;
                    margin-bottom: 10px;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
                }

                .header p {
                    font-size: 1.2em;
                    color: #666;
                    font-style: italic;
                }

                .song-card {
                    background: #f9f9f9;
                    border-radius: 8px;
                    padding: 30px;
                    margin-bottom: 40px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    transition: transform 0.3s ease, box-shadow 0.3s ease;
                }

                .song-card:hover {
                    transform: translateY(-5px);
                    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
                }

                .song-header {
                    margin-bottom: 20px;
                }

                .song-title {
                    color: #1e3c72;
                    font-size: 2em;
                    margin-bottom: 10px;
                }

                .song-info {
                    color: #666;
                    font-size: 1em;
                    font-style: italic;
                }

                .video-container {
                    margin: 20px 0;
                    border-radius: 8px;
                    overflow: hidden;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }

                .youtube-video {
                    display: block;
                    border-radius: 8px;
                }

                .lyrics-section {
                    margin-top: 20px;
                    padding: 20px;
                    background: #fff;
                    border-radius: 8px;
                    border-left: 4px solid #1e3c72;
                }

                .lyrics-header {
                    color: #1e3c72;
                    margin-bottom: 10px;
                }

                .lyrics-note {
                    color: #666;
                    line-height: 1.8;
                }

                .lyrics-note a {
                    color: #2a5298;
                    text-decoration: none;
                    font-weight: bold;
                }

                .lyrics-note a:hover {
                    color: #1e3c72;
                    text-decoration: underline;
                }

                .toc {
                    background: #f0f4f8;
                    padding: 25px;
                    border-radius: 8px;
                    margin-bottom: 40px;
                }

                .toc h2 {
                    color: #1e3c72;
                    margin-bottom: 15px;
                }

                .toc-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                    gap: 10px;
                }

                .toc-item {
                    padding: 8px;
                    background: white;
                    border-radius: 4px;
                    transition: background 0.2s;
                }

                .toc-item:hover {
                    background: #e8f0ff;
                }

                .toc-item a {
                    color: #2a5298;
                    text-decoration: none;
                    font-size: 0.95em;
                }

                .toc-item a:hover {
                    text-decoration: underline;
                }

                @media (max-width: 768px) {
                    .container {
                        padding: 20px;
                    }

                    .header h1 {
                        font-size: 2em;
                    }

                    .song-title {
                        font-size: 1.5em;
                    }

                    .toc-grid {
                        grid-template-columns: 1fr;
                    }
                }
            """)
        ),
        Body(
            Div(
                Div(
                    H1("🎺 Top 50 Jazz Standards 🎵"),
                    P("A curated collection of the most iconic jazz standards of all time"),
                    cls="header"
                ),
                Div(
                    H2("Quick Navigation"),
                    Div(
                        *[Div(
                            A(f"{i+1}. {song['name']}", href=f"#song-{i+1}"),
                            cls="toc-item"
                        ) for i, song in enumerate(jazz_standards)],
                        cls="toc-grid"
                    ),
                    cls="toc"
                ),
                *[create_song_card(song, i+1) for i, song in enumerate(jazz_standards)],
                cls="container"
            )
        )
    )

def main():
    """Generate and save the static HTML file"""
    print("Generating static HTML from FastHTML components...")

    # Generate the page
    page = generate_page()

    # Convert to HTML string with proper doctype
    html_content = "<!DOCTYPE html>\n" + to_xml(page)

    # Write to index.html
    output_file = "index.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Static HTML generated successfully: {output_file}")
    print(f"📄 File size: {len(html_content):,} bytes")
    print(f"🎵 Songs included: {len(jazz_standards)}")

if __name__ == "__main__":
    main()
