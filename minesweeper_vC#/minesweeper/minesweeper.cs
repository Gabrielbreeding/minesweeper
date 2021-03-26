using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace minesweeper
{
    class Minesweeper
    {
        // create the Front and Back Boards. Front is for the user to interact with and masks the Back Board,
        // and the Back Board
        public char[,] FrontBoard { get; set; }
        public char[,] BackBoard { get; set; }
        public bool fail { get; set; }
        int size { get; set; }
        
        public Minesweeper()
        {
            fail = false;
            size = 5;
            FrontBoard = fillFrontBoard('#');
            fillBackBoard();
        }

        public Minesweeper(int x)
        {
            fail = false;
            size = x;
            FrontBoard = fillFrontBoard('#');
            fillBackBoard();
        }

        private char[,] fillFrontBoard (char mask)
        // This Method will fill the Front Board will a masking Char.
        /* Should give a value like this:
         * 
         *          FrontBoard = {{'#','#','#'},
         *                        {'#','#','#'},
         *                        {'#','#','#'}}
         */
        {
            char[,] newBoard = new char[size, size];
            for (int i = 0; i < size; ++i)
            {
                for (int k = 0; k < size; ++k)
                {
                    newBoard[i, k] = mask;
                }
            }
            return newBoard;
        }
        private void fillBackBoard()
        {
            fillBackBoard('#');
            placeMines((size*size)/8);
            placeNumbers();
        }
        private void fillBackBoard(char mask)
        {
            char[,] newBoard = new char[size, size];
            for (int i = 0; i < size; ++i)
            {
                for (int k = 0; k < size; ++k)
                {
                    newBoard[i, k] = mask;
                }
            }
            BackBoard = newBoard;
        }

        private void placeMines (int totalMines)
        // This Method will place mines randomly throughout the Backboard until the target amount of mines is reached.
        {
            Random random = new Random();
            while (count(BackBoard, 'M') <= totalMines)
            {
                BackBoard[random.Next(0, size), random.Next(0, size)] = 'M';
            }
        }
        public char countMines(string lst)
        // This Method will count all of the mines in a string
        {
            int mines = 0;
            for (int i = 0; i < lst.Length; ++i)
            {
                if (lst[i] == 'M')
                {
                    ++mines;
                }
            }
            if (mines == 0)
            {
                return ' ';
            }
            else
            {
                return Convert.ToString(mines)[0];
            }
            
        }
        public int count(char[,] board, char term)
        // This Method will count all of the mines on the specified Board
        {
            int mines = 0;
            char instance = ' ';
            for (int i = 0; i < size; ++i)
            {
                for (int k = 0; k < size; ++k)
                {
                    instance = board[i, k];
                    if (instance == term)
                    {
                        ++mines;
                    }
                }
            }
            return mines;
        }

        
        private void placeNumbers()
        // This Method will place numbers according to how many mines are in the area around a select point and place the number there.
        // 
        // at 0,0: M|#|    at 0,1: #|M|#    at 0,2: |#|M
        //         #|#|            #|#|#            |#|#
        //
        //
        // at 1,0: #|#|    at 1,1: #|#|#    at 1,2  |#|#
        //         M|#|            #|M|#            |#|M
        //         #|#|            #|#|#            |#|#
        //
        // at 2,0:         at 2,1:          at 2,2:
        //         #|#|            #|#|#            |#|#
        //         M|#|            #|M|#            |#|M
        //
        {  
            string select = "";         // the selected area.
            for (int i = 0; i < size; ++i)
            {
                for (int k = 0; k < size; ++k)
                {
                    select = "";
                    if (BackBoard[i,k] != 'M')
                    {
                        if (i == 0)// at top row
                        {
                            select += BackBoard[i + 1, k]; // Get the vAlue Below selected point.
                            if (k == 0)
                            {
                                select += BackBoard[i, k + 1];// get value on the Right.
                                select += BackBoard[i + 1, k + 1];// get value at bottom rIght.
                            }
                            else if (k == size-1)// at the vEry right of the board.
                            {
                                select += BackBoard[i, k - 1]; // get value on the Left.
                                select += BackBoard[i + 1, k - 1];// get value at bottom left.
                            }
                            else
                            {
                                select += BackBoard[i, k + 1];
                                select += BackBoard[i + 1, k + 1];
                                select += BackBoard[i, k - 1];
                                select += BackBoard[i + 1, k - 1];
                            }
                        }
                        else if (i == size-1)// at bottom row
                        {
                            select += BackBoard[i - 1, k];// get value above selected point.
                            if (k == 0)
                            {
                                select += BackBoard[i, k + 1];// get value on the Right.
                                select += BackBoard[i - 1, k + 1];// get value at top rIght.
                            }
                            else if (k == size-1)// at the vEry right of the board.
                            {
                                select += BackBoard[i, k - 1]; // get value on the Left.
                                select += BackBoard[i - 1, k - 1];// get value at top left.
                            }
                            else
                            {
                                select += BackBoard[i, k + 1];
                                select += BackBoard[i - 1, k + 1];
                                select += BackBoard[i, k - 1];
                                select += BackBoard[i - 1, k - 1];
                            }
                        }
                        else// in the middle somewhere.
                        {
                            select += BackBoard[i - 1, k];// get value above selected point.
                            select += BackBoard[i + 1, k];// get value below selected point.
                            if (k == 0)
                            {
                                select += BackBoard[i, k + 1];// get value on the Right.
                                select += BackBoard[i - 1, k + 1];// get value at top rIght.
                                select += BackBoard[i + 1, k + 1];// get value at bottom right.
                            }
                            else if (k == size-1)// at the vEry right of the board.
                            {
                                select += BackBoard[i, k - 1]; // get value on the Left.
                                select += BackBoard[i - 1, k - 1];// get value at top left.
                                select += BackBoard[i + 1, k - 1];// get value at bottom left.
                            }
                            else
                            {
                                select += BackBoard[i, k + 1];
                                select += BackBoard[i - 1, k + 1];
                                select += BackBoard[i + 1, k + 1];
                                select += BackBoard[i, k - 1];
                                select += BackBoard[i - 1, k - 1];
                                select += BackBoard[i + 1, k - 1];
                            }
                        }
                        // place number depending on the amount of mines found around the point.
                        BackBoard[i, k] = countMines(select);
                    }  
                }
            }
        }

        public void reveal(int x, int y)
        // this method will replace a point in the front board with the matching point in the backboard
        {
            FrontBoard[x,y] = BackBoard[x, y];
            if (FrontBoard[x,y] == 'M')
            {
                fail = true;
            }
            else if (FrontBoard[x,y] == ' ')
            {
                    if (x == 0)
                    {
                        if (FrontBoard[x+1,y] == '#') {reveal(x + 1, y); }
                        if (y == 0)
                        {                           
                            if (FrontBoard[x + 1, y + 1] == '#') {reveal(x + 1, y + 1); }
                            if (FrontBoard[x, y + 1] == '#') {reveal(x, y + 1); }
                        }
                        else if (y == size - 1)
                        {
                            if (FrontBoard[x,y-1]=='#') { reveal(x, y - 1); }
                            if (FrontBoard[x+1,y-1]=='#') { reveal(x + 1, y - 1); }
                        }
                        else
                        {
                            if (FrontBoard[x, y + 1] == '#') {reveal(x, y + 1); }
                            if (FrontBoard[x + 1, y + 1] == '#') {reveal(x + 1, y + 1); }
                            if (FrontBoard[x, y - 1] == '#') {reveal(x, y - 1); }
                            if (FrontBoard[x + 1, y - 1] == '#') {reveal(x + 1, y - 1); }
                        }
                    }
                    else if (x == size - 1)
                    {                       
                        if (FrontBoard[x - 1, y] == '#') {reveal(x - 1, y); }
                        if (y == 0)
                        {                                                     
                            if (FrontBoard[x, y + 1] == '#') {reveal(x, y + 1); }
                            if (FrontBoard[x - 1, y + 1] == '#') {reveal(x - 1, y + 1); }
                        }
                        else if (y == size - 1)
                        {
                            if (FrontBoard[x, y - 1] == '#') { reveal(x, y - 1); }
                            if (FrontBoard[x - 1, y - 1] == '#') { reveal(x - 1, y - 1); }
                        }
                        else
                        {
                            if (FrontBoard[x, y + 1] == '#') { reveal(x, y + 1); }
                            if (FrontBoard[x - 1, y + 1] == '#') { reveal(x - 1, y + 1); }
                            if (FrontBoard[x, y - 1] == '#') { reveal(x, y - 1); }
                            if (FrontBoard[x - 1, y - 1] == '#') { reveal(x - 1, y - 1); }
                        }
                    }
                    else
                    {
                        if (FrontBoard[x - 1, y] == '#') {reveal(x - 1, y); }
                        if (FrontBoard[x + 1, y] == '#') {reveal(x + 1, y); }
                        if (y == 0)
                        {
                            if (FrontBoard[x, y + 1] == '#') {reveal(x, y + 1); }
                            if (FrontBoard[x - 1, y + 1] == '#') {reveal(x - 1, y + 1); }
                            if (FrontBoard[x + 1, y + 1] == '#') {reveal(x + 1, y + 1); }
                        
                        }
                        else if (y == size - 1)
                        {
                            if (FrontBoard[x, y - 1] == '#') {reveal(x, y - 1); }
                            if (FrontBoard[x - 1, y - 1] == '#') {reveal(x - 1, y - 1); }
                            if (FrontBoard[x + 1, y - 1] == '#') {reveal(x + 1, y - 1); }
                        }
                        else
                        {
                            if (FrontBoard[x, y + 1] == '#') { reveal(x, y + 1); }
                            if (FrontBoard[x - 1, y + 1] == '#') { reveal(x - 1, y + 1); }
                            if (FrontBoard[x + 1, y + 1] == '#') { reveal(x + 1, y + 1); }
                            if (FrontBoard[x, y - 1] == '#') { reveal(x, y - 1); }
                            if (FrontBoard[x - 1, y - 1] == '#') { reveal(x - 1, y - 1); }
                            if (FrontBoard[x + 1, y - 1] == '#') { reveal(x + 1, y - 1); }
                        }
                    }
                }
        }
        public void flag(int y, int x)
        // this metod will place a flag at a point in the front board
        {
            if (FrontBoard[x,y] == '#')
            {
                FrontBoard[x, y] = 'F';
            }
            else
            {
                FrontBoard[x, y] = '#';
            }
            
            
        }
        public override string ToString ()
        {
            int[,] xs = new int[size.ToString().Length, size]; // as wide as size, and as tall as the amount of digits size is.
            string screen = "";
            Console.Clear();
            screen += "+";
            for (int i = 0; i < (size*2)-1; ++i)
            {
                screen += "-";
            }
            screen += "+\n";
            for (int i = 0; i < size; ++i)
            {
                screen += "|";
                for (int k = 0; k < size; ++k)
                {
                    screen += FrontBoard[i,k];
                    screen += "|";
                    if (k == size - 1)
                    {
                        screen += " " + ((size - Convert.ToInt32(i)).ToString()); // at the end of the line, place a number to show the user.
                    }
                }
                screen += "\n";
            }
            screen += "+";
            for (int i = 0; i < (size*2)-1; ++i)
            {
                screen += "-";
            }
            screen += "+\n ";
            for (int i = 0; i<size.ToString().Length; ++i)
            {
                for (int k = 1; k<=size; ++k)
                {
                    try
                    {
                        screen += k.ToString()[i] + " ";
                    }
                    catch
                    {
                        screen += "  ";
                    }
                }
                screen += "\n ";
            }
            return screen;
        }

    }
}
