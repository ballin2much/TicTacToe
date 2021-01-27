let player = "X"
let done = false

$(document).ready(function() {    
    $(".cell").text(" ");
    $(".cell").click(function(){
        if (!done) {
            if (getWinner(getBoard()) != false) {
                done = true;
            } else {
                let space = $(this);
                if (space.is(':empty') || space.html() == " ") {
                    space.text(player);
                    getResponse();
                }
            }
        }
    })

    $("#reset").click(function(){
        resetBoard();
    })
})

function getBoard() {
    let board = [];
    for (r=0; r < 3; r++) {
        let row = []
        for (c=0; c < 3; c++) {
            let s = "#" + r.toString() + c.toString(); 
            s = $(s).html();
            if (s == "") s = " ";
            row.push(s);
        }
        board.push(row);
    }
    return board;
}

function getWinner(board) {
    let ai = "X";

    if (player == "X") {
        ai = "O";
    }
    
    for (i = 0; i < 3; i++) {
        if ((board[i][0] == player && board[i][1] == player && board[i][2] == player)
        || (board[0][i] == player && board[1][i] == player &&  board[2][i] == player)) {
            return "Player";
        } else if ((board[i][0] == ai && board[i][1] == ai && board[i][2] == ai)
        || (board[0][i] == ai && board[1][i] == ai && board[2][i] == ai)) {
            return "AI";
        }
    }  
    
    if ((board[1][1] == player && board[0][0] == player && board[2][2] == player)
    || (board[0][2] == player && board[2][0] == player)) {
        return "Player"
    }
        
    if ((board[1][1] == ai && board[0][0] == ai && board[2][2] == ai)
    || (board[0][2] == ai && board[2][0] == ai)) {
        return "AI"
    }


    for (r=0; r < 3; r++) {
        for (c=0; c < 3; c++) {
            if (board[r][c] == " " || board[r][c] == null) return false
        }
    }    
    
    return "Tie"
}

function updateBoard(board) {
    for (r=0; r < 3; r++) {
        for (c=0; c < 3; c++) {
            let s = "#" + r.toString() + c.toString(); 
            $(s).html(board[r][c]);
        }
    }
}

function getResponse() {
    return new Promise((resolve, reject) => {   
        let board = getBoard();
        console.log(board);
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/make-move/",
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            data: JSON.stringify({
                board: board,
                symbol: player
            }),
            success: (response, textStatus, jqXHR) => {
                updateBoard(response.board);
                resolve()
            },
            error: (error) => {
                reject(error)
            }
        });
    });
}

function resetBoard() {
    $(".cell").html(" ");
}