let searchResults = document.getElementsByClassName("yt-simple-endpoint style-scope ytd-video-renderer");

let links = [];

for(let i = 0; i < searchResults.length; i++) {
  links.push(searchResults[i].href);
}

const formattedLinks = links.toString().split(",").join("\n");
