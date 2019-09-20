    function enviarTexto(){
        event.preventDefault();
        document.getElementById("texto").innerHTML = document.getElementById("textbox").value;
        document.getElementById("textbox").value=""
    }