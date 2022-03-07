const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const tweet = urlParams.get('tweet');
// alert(tweet);
const destination = "https://flask-app-b6jw7kny2q-wm.a.run.app/predict?tweet=" + tweet;

function processData(data) {
    data.sort(function(first, second) {
        return second.score - first.score;
    });
    console.log(data[0]['label']);
    document.getElementById("result").innerHTML = data[0]['label']
    return data[0]['label']
}

chrome.runtime.sendMessage(
    destination,
    data => processData(JSON.parse(data))
); 
// fetch(destination, {mode: 'cors'}).then(r => r.text()).then(result => {
//     // Result now contains the response text, do what you want...
//     alert(result);
// })