Tic-Tac-Toe AI implemented using both a Q-Learning model and simple Minimax algorithm. Web interface where you can play against the Minimax AI and the Q-Learning models with various levels of training. Built using Django-Rest-Framework with a simple webpage built with plain HTML and JQuery.

Site is hosted [here](https://ml-tac-toe.herokuapp.com/).

If you want to run on your local machine simply download the repository and run the following Docker command from the root directory:
```CMD
sudo docker-compose up
```

Currently I have saved out Q-tables for AI's that have played 10, 100, 1,000, and 100,000 of games. If you want to further train and save a Q-table, edit the following line of code in the train.py file under "backend > Models" to loop the amount of games you want the AI to train:
```Python
for i in range(10):  
```

It will save the file using whatever name is passed in line 16 of code:
```Python
p1.save("10GamesAI")
```

To start training run the following command from within the Models folder:
```CMD
python3 train.py
```
