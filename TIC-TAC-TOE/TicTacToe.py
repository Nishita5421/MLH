from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")
board = ['    ' for x in range(10)]
def Empty(board):
      for i in range(0,10):
            board[i]='    '
def isWinner():
      if(board[1] == board[2] and board[2]==board[3] and not board[1].isspace() and not board[2].isspace() and not board[3].isspace()):
            return True
      if(board[4] == board[5] and board[5]==board[6] and (not board[4].isspace()) and (not board[5].isspace()) and (not board[6].isspace())):
            return True
      if(board[7] ==  board[8] and board[8] ==board[9] and (not board[7].isspace()) and (not board[8].isspace()) and (not board[9].isspace())):
            return True
      if(board[1] == board[4] and board[4]== board[7] and (not board[1].isspace()) and (not board[4].isspace()) and (not board[7].isspace())):
            return True
      if(board[2] == board[5] and board[5]==board[8] and (not board[2].isspace()) and (not board[5].isspace()) and (not board[8].isspace())):
            return True
      if(board[3] == board[6] and board[6]==board[9] and (not board[3].isspace()) and (not board[6].isspace()) and (not board[9].isspace())):
            return True
      if(board[1] == board[5] and board[5]==board[9] and (not board[1].isspace()) and (not board[5].isspace()) and (not board[9].isspace())):
            return True
      if(board[3] == board[5] and board[5]==board[7]and (not board[3].isspace()) and (not board[5].isspace()) and (not board[7].isspace())):
            return True
def printBoard(board):
      print('      |    |')
      print('  '  +  board[1]  + '|'  +  board[2]  +  '|' +  board[3])
      print('      |    |')
      print('------------------')
      print('      |    |')
      print('  '  +  board[4]  + '|'  +  board[5]  + '|' +  board[6])
      print('      |    |')
      print('------------------')
      print('      |    |')
      print('  '  +board[7]  + '|'  +  board[8]  + '|' +  board[9])
      print('      |    |')
def printBoard1():
      print('      |    |')
      print('  '  +   '1'  +'  ' + '|'  +'  ' +  '2'  +' ' +  '|' +'  ' +  '3')
      print('      |    |')
      print('------------------')
      print('      |    |')
      print('  '  +  '4'  +'  ' + '|' +'  '  +  '5'   +' '+ '|' +'  ' +  '6')
      print('      |    |')
      print('------------------')
      print('      |    |')
      print('  '  +  '7' +'  '  + '|' +'  '  +  '8' +' '+ '|'+'  '  +  '9')
      print('      |    |')
def compMove(player,i):
      if(i==1):
            positions=[1,3,7,9]
            import random
            pos=random.choice(positions)
            if(board[pos].isspace()):
                  if(player=="x" or player=="X"):
                        board[pos]=" O "
                        print('-----------------------------------------------------------------------------------------------------------------------------')
                        print("Computer Move")
                        printBoard(board)
                  if(player=="o" or player=="O"):
                        board[pos]=" X "
                        print('-----------------------------------------------------------------------------------------------------------------------------')
                        print("Computer Move")
                        printBoard(board)
            else:
                  compMove(player,1)
      if(i==5):
            positions=[5]
            import random
            pos=random.choice(positions)
            if(board[pos].isspace()):
                  if(player=="x" or player=="X"):
                        board[pos]=" O "
                        print('-----------------------------------------------------------------------------------------------------------------------------')
                        print("Computer Move")
                        printBoard(board)
                  if(player=="o" or player=="O"):
                        board[pos]=" X "
                        print('-----------------------------------------------------------------------------------------------------------------------------')
                        print("Computer Move")
                        printBoard(board)
            else:
                  compMove(player,2)
      if(i==2):
            positions=[2,4,6,8]
            import random
            pos=random.choice(positions)
            if(board[pos].isspace()):
                  if(player=="x" or player=="X"):
                        board[pos]=" O "
                        print('-----------------------------------------------------------------------------------------------------------------------------')
                        print("Computer Move")
                        printBoard(board)
                  if(player=="o" or player=="O"):
                        board[pos]=" X "
                        print('-----------------------------------------------------------------------------------------------------------------------------')
                        print("Computer Move")
                        printBoard(board)
            else:
                  if(board[2].isspace() or board[4].isspace() or board[6].isspace() or board[8].isspace()):
                        compMove(player,2)
                  else:
                        compMove(player,1)
def PlayerMove(player):
      pos=int(input("Enter the positions from [1-9]\n"))
      if(board[pos].isspace()):
            if(player=="x" or player=="X"):
                  board[pos]=" X "
                  print('------------------------------------------------------------------------------------------------------------------')
                  printBoard(board)
            if(player=="o" or player=="O"):
                  board[pos]=" O "
                  print('------------------------------------------------------------------------------------------------------------------')
                  printBoard(board)
      else:
            print("Position is already Filled")
            PlayerMove(player)
def PlayAgain():
      a=input("Do You Want To Play Again Type y for YES and n for NO\n")
      a.lower()
      if(a=="y"):
            main()
      else:
            print("Thanks for Playing")
            import sys
            sys.exit(0)
def main():
      Empty(board)
      print("_______________TIC TAC TOE_______________")
      choose=input("Enter your name\n")
      print("Hey" , choose , "What you want to choose X or O")
      player=input()
      if(not(player=="x" or player=="X" or player=="o" or player=="O")):
            print("Please print X or O")
            main()
      printBoard1()
      PlayerMove(player)
      compMove(player,1)
      PlayerMove(player)
      compMove(player,5)
      PlayerMove(player)
      if(isWinner()):
            print("You Win")
            PlayAgain()
      else:
            compMove(player,2)
            if(isWinner()):
                  print("Computer Wins")
                  PlayAgain()
            else:
                  PlayerMove(player)
                  if(isWinner()):
                        print("You Win")
                        PlayAgain()
                  else:
                        compMove(player,2)
                        if(isWinner()):
                              print("Computer Wins")
                              PlayAgain()
                        else:
                              PlayerMove(player)
                              if(isWinner()):
                                    print("You Win")
                                    PlayAgain()
                              else:
                                    print("It's A Tie")
                                    PlayAgain()
      tk.mainloop()
main()


      
      

      



      
