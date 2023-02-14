
// =================  wrapper  =============================

var el = document.getElementById("wrapper");
var toggleButton = document.getElementById("menu-toggle");

toggleButton.onclick = function () {
    el.classList.toggle("toggled");
};

// ==================== Data Tables ============================

$(document).ready(function() {
    $('#mytable').DataTable({    
        order: [[0, 'desc']], 
        responsive: true,
      "aLengthMenu": [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
      "iDisplayLength": 10
       } 
    );
} );



$(document).ready(function() {
    $('#mytable2').DataTable({    
        responsive: true,
      "aLengthMenu": [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
      "iDisplayLength": 10
       } 
    );
} );