let active = "X"

$(document).ready(function() {    
    $(".cell").click(function(){
        let space = $(this);
        if (space.is(':empty')) {
            space.text(active);
            if (active == "X") {
                checkWinner("X");
                active = "O";
            } else {
                checkWinner("O");
                active = "X";
            }
        }
    })
})

