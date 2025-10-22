from fasthtml.common import *

# Initialize FastHTML app
app, rt = fast_app()

# Top 50 Jazz Standards with YouTube video IDs
# Note: These are some of the most iconic jazz standards
jazz_standards = [
    {"name": "Autumn Leaves", "youtube_id": "rsz6TE6t6-M", "composer": "Joseph Kosma", "year": "1945"},
    {"name": "All of Me", "youtube_id": "mQR0bXO_yI8", "composer": "Gerald Marks & Seymour Simons", "year": "1931"},
    {"name": "All the Things You Are", "youtube_id": "8FsLSdRDrnM", "composer": "Jerome Kern", "year": "1939"},
    {"name": "Blue Bossa", "youtube_id": "WZod5FZy2kg", "composer": "Kenny Dorham", "year": "1963"},
    {"name": "Blue Monk", "youtube_id": "vFHV8VsCbt8", "composer": "Thelonious Monk", "year": "1954"},
    {"name": "Body and Soul", "youtube_id": "Y4XDrGCcYkU", "composer": "Johnny Green", "year": "1930"},
    {"name": "Bye Bye Blackbird", "youtube_id": "6wIbYhWrR-0", "composer": "Ray Henderson", "year": "1926"},
    {"name": "Caravan", "youtube_id": "aJoo79OwZEI", "composer": "Duke Ellington", "year": "1936"},
    {"name": "Cantaloupe Island", "youtube_id": "8B1oIXGX0Io", "composer": "Herbie Hancock", "year": "1964"},
    {"name": "Cherokee", "youtube_id": "2c5dRGj2x6U", "composer": "Ray Noble", "year": "1938"},
    {"name": "Come Rain or Come Shine", "youtube_id": "eHFa99iS6ps", "composer": "Harold Arlen", "year": "1946"},
    {"name": "Confirmation", "youtube_id": "KNcHnEwGv8c", "composer": "Charlie Parker", "year": "1946"},
    {"name": "Days of Wine and Roses", "youtube_id": "CgwVWyxhwDM", "composer": "Henry Mancini", "year": "1962"},
    {"name": "Don't Get Around Much Anymore", "youtube_id": "J86atk1k4ZM", "composer": "Duke Ellington", "year": "1940"},
    {"name": "Donna Lee", "youtube_id": "4Qb4ImxVxRA", "composer": "Charlie Parker", "year": "1947"},
    {"name": "Embraceable You", "youtube_id": "HW-RpUHDfl8", "composer": "George Gershwin", "year": "1928"},
    {"name": "Fly Me to the Moon", "youtube_id": "ZEcqHA7dbwM", "composer": "Bart Howard", "year": "1954"},
    {"name": "Footprints", "youtube_id": "HQDm92c3v9g", "composer": "Wayne Shorter", "year": "1966"},
    {"name": "Georgia on My Mind", "youtube_id": "fRgWBN8yt_E", "composer": "Hoagy Carmichael", "year": "1930"},
    {"name": "Giant Steps", "youtube_id": "30FTr6G53VU", "composer": "John Coltrane", "year": "1959"},
    {"name": "Girl from Ipanema", "youtube_id": "UJkxFhFRFDA", "composer": "Antonio Carlos Jobim", "year": "1962"},
    {"name": "How High the Moon", "youtube_id": "xScKFHRUKhA", "composer": "Morgan Lewis", "year": "1940"},
    {"name": "I Got Rhythm", "youtube_id": "VAOWg6R5q_I", "composer": "George Gershwin", "year": "1930"},
    {"name": "I'll Remember April", "youtube_id": "rz7QXdGVX0k", "composer": "Gene de Paul", "year": "1941"},
    {"name": "In a Sentimental Mood", "youtube_id": "sCQfTNOC5aE", "composer": "Duke Ellington", "year": "1935"},
    {"name": "It Could Happen to You", "youtube_id": "s8yAyOgV_hw", "composer": "Jimmy Van Heusen", "year": "1944"},
    {"name": "Just Friends", "youtube_id": "lv51EjH79WA", "composer": "John Klenner", "year": "1931"},
    {"name": "Maiden Voyage", "youtube_id": "hwmRQ0PBtXU", "composer": "Herbie Hancock", "year": "1965"},
    {"name": "Misty", "youtube_id": "P9uxEZl2sec", "composer": "Erroll Garner", "year": "1954"},
    {"name": "My Favorite Things", "youtube_id": "qWG2dsXV5HI", "composer": "Richard Rodgers", "year": "1959"},
    {"name": "My Funny Valentine", "youtube_id": "jRdkrDk0BQ0", "composer": "Richard Rodgers", "year": "1937"},
    {"name": "Night and Day", "youtube_id": "9CjPVyvSn9A", "composer": "Cole Porter", "year": "1932"},
    {"name": "On Green Dolphin Street", "youtube_id": "EyYzXB2ta8w", "composer": "Bronisław Kaper", "year": "1947"},
    {"name": "Oleo", "youtube_id": "P_NCYYBnXos", "composer": "Sonny Rollins", "year": "1954"},
    {"name": "Over the Rainbow", "youtube_id": "PSZxmZmBfnU", "composer": "Harold Arlen", "year": "1939"},
    {"name": "Perdido", "youtube_id": "3GaOj2rCJyE", "composer": "Juan Tizol", "year": "1942"},
    {"name": "Recorda Me", "youtube_id": "nJ4cE5PoKhk", "composer": "Joe Henderson", "year": "1963"},
    {"name": "Round Midnight", "youtube_id": "vSjS4d72RU0", "composer": "Thelonious Monk", "year": "1944"},
    {"name": "Satin Doll", "youtube_id": "E5EGOezNgkw", "composer": "Duke Ellington", "year": "1953"},
    {"name": "So What", "youtube_id": "zqNTltOGh5c", "composer": "Miles Davis", "year": "1959"},
    {"name": "Solar", "youtube_id": "1rTBp5eoFTY", "composer": "Miles Davis", "year": "1954"},
    {"name": "Someday My Prince Will Come", "youtube_id": "4tAi-lu4-2w", "composer": "Frank Churchill", "year": "1937"},
    {"name": "Stella by Starlight", "youtube_id": "GhaYWk4_fSM", "composer": "Victor Young", "year": "1944"},
    {"name": "Summertime", "youtube_id": "MIDOEeKvsLU", "composer": "George Gershwin", "year": "1935"},
    {"name": "Take Five", "youtube_id": "vmDDOFXSgAs", "composer": "Paul Desmond", "year": "1959"},
    {"name": "Take the A Train", "youtube_id": "cb2w2m1JmCY", "composer": "Billy Strayhorn", "year": "1939"},
    {"name": "There Will Never Be Another You", "youtube_id": "uGfHbxWEPPs", "composer": "Harry Warren", "year": "1942"},
    {"name": "The Nearness of You", "youtube_id": "GnEmD17kYsE", "composer": "Hoagy Carmichael", "year": "1938"},
    {"name": "Tune Up", "youtube_id": "Cdf0wSPJ7Pk", "composer": "Miles Davis", "year": "1953"},
    {"name": "Wave", "youtube_id": "bZv6d-IJDzE", "composer": "Antonio Carlos Jobim", "year": "1967"},
]

def create_song_card(song, index):
    """Create a card for each jazz standard"""
    return Div(
        Div(
            H2(f"{index}. {song['name']}", cls="song-title"),
            P(
                f"Composer: {song['composer']} • Year: {song['year']}",
                cls="song-info"
            ),
            cls="song-header"
        ),
        Div(
            # YouTube embed
            Iframe(
                src=f"https://www.youtube.com/embed/{song['youtube_id']}",
                width="100%",
                height="315",
                frameborder="0",
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
                allowfullscreen=True,
                cls="youtube-video"
            ),
            cls="video-container"
        ),
        Div(
            H3("Lyrics", cls="lyrics-header"),
            P(
                "For licensed lyrics, please visit: ",
                A("Genius Lyrics", href=f"https://genius.com/search?q={song['name'].replace(' ', '%20')}%20jazz", target="_blank"),
                " or ",
                A("Musixmatch", href=f"https://www.musixmatch.com/search/{song['name'].replace(' ', '%20')}", target="_blank"),
                cls="lyrics-note"
            ),
            cls="lyrics-section"
        ),
        cls="song-card",
        id=f"song-{index}"
    )

@rt('/')
def get():
    """Main page with all jazz standards"""
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

if __name__ == "__main__":
    serve()
