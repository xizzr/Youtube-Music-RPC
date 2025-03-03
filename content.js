function getNowPlaying() {
    let titleElement = document.querySelector(".title.style-scope.ytmusic-player-bar");
    let artistElement = document.querySelector(".byline.style-scope.ytmusic-player-bar");

    if (titleElement && artistElement) {
        let songData = {
            title: titleElement.innerText,
            artist: artistElement.innerText
        };

        chrome.runtime.sendMessage({ action: "updateRPC", data: songData });
    }
}

setInterval(getNowPlaying, 5000);
