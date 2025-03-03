chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "updateRPC") {
        fetch("http://localhost:5000/update_presence", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(message.data)
        });
    }
});
