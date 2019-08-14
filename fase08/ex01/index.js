function clique(){
        min=document.getElementById("min").value
        max=document.getElementById("max").value
        var string=""
    if (min!="-"&&max!="-"){
        max=parseInt(max)
        min=parseInt(min)
        if(max<min){
            alert("O valor minimo está menor que o máximo")
        }
        else{
            for(var i=min;i<=max;i++){
                string=string+i.toString()+"<br>"
            }
            document.getElementById("texto").innerHTML=string
        }
    }
    else{
        alert("Escolha os dois valores")
    }
}