function getNowPlaying() {
    let titleElement = document.querySelector(".title.style-scope.ytmusic-player-bar");
    let artistElement = document.querySelector(".byline.style-scope.ytmusic-player-bar");
    let TimeE = document.querySelector(".time-info.style-scope.ytmusic-player-bar");

    if (titleElement && artistElement) {
        let songData = {
            title: titleElement.innerText,
            artist: artistElement.innerText,
            times: TimeE.innerText
        };

        chrome.runtime.sendMessage({ action: "updateRPC", data: songData });
    }
}
setInterval(getNowPlaying, 900);
