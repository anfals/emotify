document.getElementById("copy").addEventListener("click", myFunction);

function myFunction() {
    /* Get the text field */
    var copyText = document.getElementById("result").textContent;
    console.log(copyText)
  
     /* Copy the text inside the text field */
     navigator.clipboard
        .writeText(copyText)
        .then(() => {
            alert("Successfully copied: " + copyText);
        })
        .catch(() => {
            alert("Something went wrong!");
        });
  
  }