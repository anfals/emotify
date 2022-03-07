chrome.runtime.onMessage.addListener(
  function(url, sender, sendResponse) {
    console.log(url)
    fetch(url)
        .then(response => response.text())
        .then(responseText => sendResponse(responseText))
    
    return true;  // Will respond asynchronously.
  }
);
