var button = document.getElementById("full_website");
button.addEventListener("click", function(){
    chrome.tabs.create({url:"https://share.streamlit.io/anfals/emotify/main/interface.py"});
});