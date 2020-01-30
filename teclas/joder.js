var teclas = {
    UP: 87,
    DOWN: 83,
    LEFT: 65,
    RIGHT: 68,
};
var img = new Image();
img.src = "hola.jpg"

document.addEventListener("keydown", dibujarConTeclado);

var cuadrito = document.getElementById("hola");
var papel = cuadrito.getContext("2d");
//papel.drawImage(img,0,0)
img.onload = function(){
    papel.drawImage(img, 0, 0);
  }
var x = 300;
var y = 300;

dibujarLinea("red", x-1, y-1, x+1, y+1, papel);
dibujarLinea("white", 0,0,600,0,papel)
dibujarLinea("white", 0,0,0,600,papel)
dibujarLinea("white", 0,600,600,600,papel)
dibujarLinea("white", 600,0,600,600,papel)

function dibujarLinea(color, x_inicial, y_inicial, x_final, y_final, lienzo)
{
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.lineWidth = 7;
    lienzo.moveTo(x_inicial, y_inicial);
    lienzo.lineTo(x_final, y_final);
    lienzo.stroke();
    lienzo.closePath();
}

function dibujarConTeclado(hola){
    var colore = "red";
    var movimiento = 5;
    var cola = 1;
    switch (hola.keyCode) {
        case teclas.UP:
            img.onload()
            for (let index = 0; index < 1; index++) {
            dibujarLinea(colore, x, y, x, y - movimiento, papel);
            y = y - movimiento
            }
            break;
        case teclas.DOWN:
            img.onload()
            dibujarLinea(colore, x, y, x, y + movimiento, papel);
            y = y + movimiento
            for (let index = 0; index < cola; index++) {
                dibujarLinea(colore, x - 1, y- 1, x- 1, y + movimiento- 1, papel);
            }
            break;
        case teclas.LEFT:
            img.onload()
            for (let index = 0; index < 1; index++) {
            dibujarLinea(colore, x, y, x - movimiento , y , papel);
            x = x - movimiento
            }
            break;
        case teclas.RIGHT:
            img.onload()
            for (let index = 0; index < 1; index++) {
            dibujarLinea(colore, x, y, x + movimiento, y, papel);
            x = x + movimiento
            }
            break;
        default:
        console.log("Pos otra tecla we ");
        break;
    }
}