{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7eab68bb",
   "metadata": {},
   "source": [
    "DISPLAYING INFORMATION:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "42d8ec13",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "print([1,2,3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5fa5b665",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3]\n",
      "[4, 5, 6]\n",
      "[7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "print([1,2,3])\n",
    "print([4,5,6])\n",
    "print([7,8,9])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "89f3aa2e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def display (r1,r2,r3):\n",
    "    print(r1)\n",
    "    print(r2)\n",
    "    print(r3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8be42280",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3]\n",
      "[1, 2, 3]\n",
      "[1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "example_row=([1,2,3])\n",
    "display(example_row,example_row,example_row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e1416f85",
   "metadata": {},
   "outputs": [],
   "source": [
    "row1=[' ',' ',' ']\n",
    "row2=[' ',' ',' ']\n",
    "row3=[' ',' ',' ']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "58508b84",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[' ', ' ', ' ']\n",
      "[' ', ' ', ' ']\n",
      "[' ', ' ', ' ']\n"
     ]
    }
   ],
   "source": [
    "display(row1,row2,row3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8c1794f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "row2[1]='X'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4bd6eafc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[' ', ' ', ' ']\n",
      "[' ', 'X', ' ']\n",
      "[' ', ' ', ' ']\n"
     ]
    }
   ],
   "source": [
    "display(row1,row2,row3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "774e7122",
   "metadata": {},
   "source": [
    "ACCEPTING USER INPUT:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0f3eac02",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "please enter a value : 2\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'2'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "input('please enter a value : ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d2d260ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "please enter a value : 2\n"
     ]
    }
   ],
   "source": [
    "result=input('please enter a value : ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1fe9cefe",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2'"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "70835412",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(result)    #input function is always going to return a string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "de007146",
   "metadata": {},
   "outputs": [],
   "source": [
    "result_int=int(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "18574066",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(result_int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "35590d26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "choose an input position: 1\n"
     ]
    }
   ],
   "source": [
    "position_index=int(input('choose an input position: '))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "925f286d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(position_index)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d9b8c615",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' '"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "row1[position_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54fda88f",
   "metadata": {},
   "outputs": [],
   "source": [
    "result=input('enter a number: ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8cfc7c14",
   "metadata": {},
   "outputs": [],
   "source": [
    "2+2   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2c80bd05",
   "metadata": {},
   "outputs": [],
   "source": [
    "# It happened because python is still waiting for the user interaction from the input. So only when the value \n",
    "    # is entered in the input box the rest of the cells will execute.\n",
    "# Also if we try to run the cell twice, the input box will disappear and the upcoming cells will also not execute since\n",
    "    # it is still waiting for the first execution to give the input."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b6241e1a",
   "metadata": {},
   "source": [
    "VALIDATING USER INPUT:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a158593e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "choose an input position: two\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'two'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_16832/2707752964.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mposition_index\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'choose an input position: '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: 'two'"
     ]
    }
   ],
   "source": [
    "position_index=int(input('choose an input position: '))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ac41430",
   "metadata": {},
   "source": [
    "In order to avoid such errors we validate user input using while loop to ask the user for the correct input "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f56ba67d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def user_choice():\n",
    "    choice=input('Please enter a number (0-10) : ')\n",
    "    return int(choice)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "012a546f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a number (0-10) : 2\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user_choice()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f7748f32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a number (0-10) : two\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "invalid literal for int() with base 10: 'two'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_16832/2296594588.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0muser_choice\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_16832/3301810541.py\u001b[0m in \u001b[0;36muser_choice\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mdef\u001b[0m \u001b[0muser_choice\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[0mchoice\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Please enter a number (0-10) : '\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m     \u001b[1;32mreturn\u001b[0m \u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mchoice\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: invalid literal for int() with base 10: 'two'"
     ]
    }
   ],
   "source": [
    "user_choice()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "17f6920b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def user_choice():\n",
    "    choice='wrong'\n",
    "    while choice.isdigit()==False:\n",
    "        \n",
    "        choice=input('Please enter a number (0-10) : ')\n",
    "        if choice.isdigit()==False:\n",
    "            print('Sorry that is not a digit!')\n",
    "    return int(choice)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8befa200",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a number (0-10) : two\n",
      "Sorry that is not a digit!\n",
      "Please enter a number (0-10) : ef\n",
      "Sorry that is not a digit!\n",
      "Please enter a number (0-10) : 2\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user_choice()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "bc9c987a",
   "metadata": {},
   "outputs": [],
   "source": [
    "result='wrong value'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "49fe4eed",
   "metadata": {},
   "outputs": [],
   "source": [
    "acceptable_value=[0,1,2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "79135dad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result in acceptable_value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "92ee5bb8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result not in acceptable_value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b6b7358a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def user_choice():\n",
    "    \n",
    "    #VARIABLES\n",
    "    \n",
    "    #initial\n",
    "    choice='wrong'\n",
    "    acceptable_range=range(0,10)\n",
    "    within_range=False\n",
    "    \n",
    "    #TWO CONDITIONS TO CHECK\n",
    "    #DIGIT OR WITHIN_RANGE==False\n",
    "    while choice.isdigit()==False or within_range==False:\n",
    "        \n",
    "        choice=input('Please enter a number (0-10) : ')\n",
    "        \n",
    "        #DIGIT CHECK\n",
    "        if choice.isdigit()==False:\n",
    "            print('Sorry that is not a digit!')\n",
    "        \n",
    "        #RANGE CHECK\n",
    "        if choice.isdigit()==True:\n",
    "            if int(choice) in acceptable_range:\n",
    "                within_range=True\n",
    "            else:\n",
    "                print('Sorry you are out of acceptable range')\n",
    "                within_range=False\n",
    "                \n",
    "    return int(choice)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "36b8d644",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a number (0-10) : two\n",
      "Sorry that is not a digit!\n",
      "Please enter a number (0-10) : 11\n",
      "Sorry you are out of acceptable range\n",
      "Please enter a number (0-10) : 9\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "9"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "user_choice()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "35ecc68f",
   "metadata": {},
   "source": [
    "SIMPLE USER INTERACTION:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "6cafbd45",
   "metadata": {},
   "outputs": [],
   "source": [
    "game_list=[0,1,2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f4c4dee1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_game(game_list):\n",
    "    print('Here is the current list: ')\n",
    "    print(game_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "425f6d28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here is the current list: \n",
      "[0, 1, 2]\n"
     ]
    }
   ],
   "source": [
    "display_game(game_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "118270c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def position_choice():\n",
    "    choice='wrong'\n",
    "    \n",
    "    while choice not in ['0','1','2']:\n",
    "        choice=input('Pick a position (0,1,2): ')\n",
    "        if choice not in ['0','1','2']:\n",
    "            print ('Sorry invalid choice!!')\n",
    "            \n",
    "    return int(choice)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "7949e0bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pick a position (0,1,2): two\n",
      "Sorry invalid choice!!\n",
      "Pick a position (0,1,2): 24\n",
      "Sorry invalid choice!!\n",
      "Pick a position (0,1,2): 2\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "position_choice()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "327ae870",
   "metadata": {},
   "outputs": [],
   "source": [
    "def replacement_choice(game_list,position):\n",
    "    user_placement=input('Type a string to place at position: ')\n",
    "    game_list[position]=user_placement\n",
    "    return game_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "32516f6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Type a string to place at position: hyy\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[0, 'hyy', 2]"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "replacement_value(game_list,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a35016c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "def gameon_choice():\n",
    "    \n",
    "    choice='wrong'\n",
    "    \n",
    "    while choice not in ['Y','N']:\n",
    "        choice=input('Keep playing (Y or N): ')\n",
    "        if choice not in ['Y','N']:\n",
    "            print ('Sorry I dont understand, please choose Y or N: ')\n",
    "    if choice=='Y':\n",
    "        return True\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "3ce03ef7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Keep playing (Y or N): t\n",
      "Sorry I dont understand, please choose Y or N: \n",
      "Keep playing (Y or N): Y\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gameon_choice()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "6114c7de",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Here is the current list: \n",
      "[0, 1, 2]\n",
      "Pick a position (0,1,2): 1\n",
      "Type a string to place at position: to\n",
      "Here is the current list: \n",
      "[0, 'to', 2]\n",
      "Keep playing (Y or N): Y\n",
      "Here is the current list: \n",
      "[0, 'to', 2]\n",
      "Pick a position (0,1,2): 2\n",
      "Type a string to place at position: India\n",
      "Here is the current list: \n",
      "[0, 'to', 'India']\n",
      "Keep playing (Y or N): Y\n",
      "Here is the current list: \n",
      "[0, 'to', 'India']\n",
      "Pick a position (0,1,2): 0\n",
      "Type a string to place at position: Welcome\n",
      "Here is the current list: \n",
      "['Welcome', 'to', 'India']\n",
      "Keep playing (Y or N): N\n"
     ]
    }
   ],
   "source": [
    "game_on=True\n",
    "game_list=[0,1,2]\n",
    "\n",
    "while game_on:\n",
    "    display_game(game_list)\n",
    "    position= position_choice()\n",
    "    game_list=replacement_choice(game_list,position)\n",
    "    display_game(game_list)\n",
    "    game_on=gameon_choice()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef083516",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
