## Synchronizes local music to spotify

>> Idea

If you have a local music folder than you want to have it as a playlist on spotify.

This project takes the music from the folder and searches the track name on spotify.
Once the track is found it adds it to the playlist.


>> .env file contents

CLIENTID="xyz" \
CLIENTSECRET="abc" \
USERNAME="lmn" \
PLAYLISTNAME="def"

>> build docker command

docker build -t <tag_name> <path to Dockerfile>

>> run docker command

````
docker run -v <Local Music directory>:/Spotify/Music --env-file <.env file path> <tag_name>
````

-v will bind your local music directory with the Music directory created in the docker container.

--env-file will provide .env file to the container