import requests

# Se hai una API Key di TMDB puoi metterla qui per avere i titoli veri, 
# altrimenti lo script userà titoli generici.
def get_movie_data(movie_id):
    url = f"https://api.themoviedb.org{movie_id}?api_key=844dba0bfd8f3a4f3799f6130ef9e335&language=it-IT"
    try:
        r = requests.get(url, timeout=5).json()
        title = r.get('title', f"Film {movie_id}")
        poster = f"https://image.tmdb.org{r.get('poster_path')}" if r.get('poster_path') else ""
        return title, poster
    except:

return f"Film {movie_id}", ""

def main():
    with open("film_id.txt", "r") as f:
        ids = f.read().splitlines()

    with open("lista.m3u", "w", encoding="utf-8") as m3u:
        m3u.write("#EXTM3U\n")
        for fid in ids:
            if not fid.strip(): continue
            title, poster = get_movie_data(fid)
            link = f"https://vixsrc.to{fid}?lang=it"
            m3u.write(f'#EXTINF:-1 tvg-id="{fid}" tvg-logo="{poster}" group-title="Vix Movies",{title}\n')
m3u.write(f"{link}\n")

if __name__ == "__main__":
    main()
