let playlistResults = document.getElementsByClassName("yt-simple-endpoint style-scope ytd-playlist-video-renderer");

let links = [];

for(let i = 0; i < playlistResults.length; i++) {
  links.push(playlistResults[i].href);
}

const formattedLinks = links.toString().split(",").join("\n");
