window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let alexa = new SpeechRecognition();
let przycisk = document.querySelector('input')

function sluchaj(e) {
    console.log("wiem co robisz")
    console.dir(e.results [0] [0].transcript)

}


alexa.addEventListener('result', sluchaj)
//alexa.addEventListener('end', alexa.start)


przycisk.addEventListener('click', function (e) {
    e.preventDefault();
    console.log("odpalam Drona...............");
    alexa.start()

 })
