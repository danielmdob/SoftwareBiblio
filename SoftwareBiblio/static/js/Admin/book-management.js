// Get the modal
var modal = document.getElementById('smart-add-modal');
var modal2 = document.getElementById('delete-modal');

// Get the button that opens the modal
var btn = document.getElementById("modal-opener");
var btn2 = document.getElementById("delete-modal-opener");

var accept = document.getElementById('submit-modal');
var accept2 = document.getElementById('delete-submit-modal');

var cancel = document.getElementById('cancel-modal');
var cancel2 = document.getElementById('delete-cancel-modal');

// When the user clicks on the button, open the modal 
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on the button, open the modal 
btn2.onclick = function() {
    modal2.style.display = "block";
}


accept.onclick = function() {
	alert("Libro agregado. Refresque la página para buscarlo");
	modal.style.display = "none";
}

accept2.onclick = function() {
	alert("Libro eliminado");
	modal2.style.display = "none";
}
// When the user clicks on <span> (x), close the modal
cancel.onclick = function() {
    modal.style.display = "none";
}

cancel2.onclick = function() {
    modal2.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

window.onclick = function(event) {
    if (event.target == modal2) {
        modal2.style.display = "none";
    }
}