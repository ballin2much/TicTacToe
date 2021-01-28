let player = "X"
let done = false
let started = false
let AItype = "MiniMax"

$(document).ready(function() {    
    $(".cell").text(" ");
    $(".AI").click(function(){
        let s = $(this).data("type");
        $(".selected").html("<h1>" + s + " currently selected</h1>");
        AItype = s;
    })

    $("#aifirst").click(function(){
        if (!started) {
            $(".cell").css('pointer-events', 'none');
            getResponse(AItype).then(() => {
                $(".cell").css('pointer-events', 'auto');
            })
        }
    })

    $("#X").click(function(){
        if (!started) player = "X";
    })

    $("#O").click(function(){
        if (!started) player = "O";
    })

    $(".cell").click(function(){
        if (!done) {
            started = true;
            let space = $(this);
            if (space.is(':empty') || space.html() == " ") {
                space.text(player);
                $(".cell").css('pointer-events', 'none');
                let winner = getWinner(getBoard()).then(winner => {
                    if (winner != false) {
                        done = true;
                        $('#winner').html(winner);
                    } else {
                        getResponse(AItype).then(() => {
                            $(".cell").css('pointer-events', 'auto');
                            winner = getWinner(getBoard()).then(winner => {
                                if (winner != false) done = true;
                                $('#winner').html(winner);
                            })
                        })
                    }
                })
            }
        }
    })

    $("#reset").click(function(){
        resetBoard();
        $('#winner').empty();
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
    return new Promise((resolve, reject) => {    

        if (player == "X") {
            ai = "O";
        } else if (player == "O") {
            ai = "X";
        }
        
        for (i = 0; i < 3; i++) {
            if ((board[i][0] == player && board[i][1] == player && board[i][2] == player)
            || (board[0][i] == player && board[1][i] == player &&  board[2][i] == player)) {
                resolve("You Win");
            } else if ((board[i][0] == ai && board[i][1] == ai && board[i][2] == ai)
            || (board[0][i] == ai && board[1][i] == ai && board[2][i] == ai)) {
                resolve("AI Wins");
            }
        }  
        
        if ((board[1][1] == player && board[0][0] == player && board[2][2] == player)
        || (board[0][2] == player && board[2][0] == player && board[1][1] == player)) {
            resolve("You Win");
        }
            
        if ((board[1][1] == ai && board[0][0] == ai && board[2][2] == ai)
        || (board[0][2] == ai && board[2][0] == ai && board[1][1] == ai)) {
            resolve("AI Wins");
        }


        for (r=0; r < 3; r++) {
            for (c=0; c < 3; c++) {
                if (board[r][c] == " " || board[r][c] == null) resolve(false)
            }
        }    
        resolve("Tie");
    })
}

function updateBoard(board) {
    for (r=0; r < 3; r++) {
        for (c=0; c < 3; c++) {
            let s = "#" + r.toString() + c.toString(); 
            $(s).html(board[r][c]);
        }
    }
}

function getResponse(ai) {
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
                symbol: player,
                AI: ai
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
    done = false;
    started = false;
    $(".cell").css('pointer-events', 'auto');
}
