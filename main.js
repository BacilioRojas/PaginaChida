var form = document.querySelector('form');
  var inputs = form.querySelectorAll('input');
  var boton = form.querySelector('#boton');
  var pR = document.querySelector('#resultado');
  var sel = document.querySelectorAll('select');
  
  boton.addEventListener('click', btclic);
  
  function btclic(event) {
    event.preventDefault();
    var op = sel[1].value;
    var amer = Boolean(sel[2].value);
    var tiempo = eval(sel[0].value) * inputs[0].value;
    
    // Resto de tu código
    console.log(tiempo)
    console.log(sel[2].value)
    var arbol =[[inputs[3].value]]
    var rama 
      for(var i = 0; i<inputs[2].value; i++){
        rama =[]
        for(var j=0; j<arbol[i].length;j++){
          rama.push(arbol[i][j]*inputs[5].value)
        }
        rama.push(arbol[i][arbol[i].length-1]*inputs[6].value)
          arbol.push(rama)
          
      }
        console.log(arbol)
        var pre = Math.exp(-1*(tiempo/inputs[2].value)*inputs[1].value)
        console.log(pre)
        
        var p = ((pre**(-1))-inputs[6].value)/(inputs[5].value-inputs[6].value)
        console.log(p)
        var arbolOp =[]
        rama =[]
        for (var k=0; k<arbol[inputs[2].value].length;k++){
          rama.push(Math.max(0,((-1)**op)*(inputs[4].value-arbol[inputs[2].value][k])))
          
        }
          arbolOp.push(rama)
          console.log(rama)
          var aux
          for (var i =0;i<inputs[2].value;i++){
            rama =[]
            for(var j=0;j<arbolOp[i].length-1;j++){
              aux = p*arbolOp[i][j]+(1-p)*arbolOp[i][j+1]
              
              if(amer){
                console.log(aux)
                aux = Math.max(aux,((-1)**op)*(inputs[4].value-arbol[inputs[2].value-i-1][j]))
                
              }
              rama.push(aux)
            }
              arbolOp.push(rama)
          }
            console.log(arbolOp)
            console.log(arbolOp[inputs[2].value])
            pR.innerText ="El valor de la opcion es "+arbolOp[inputs[2].value]
  }
  
  