using System;
using static System.Console;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/* Gabriel Breeding
 * 
 * ToDoList:
 *      Create a multidimensional array for the minesweeper board.
 *      Make an input so the user can manipulate the board.
 *      add function to place mines randomly on the board.
 *      add function to accurately depict how many mines are in a specified area.
 *      add win/lose conditions.
 *      add feature that will stop the scenario where a user instantly loses on their first move.
 *      add score counter.
 *      add a way to keep track of score even after the program ends.
 * 
 * 1/14/2021:
 * 
 * 
 * 
 */

namespace minesweeper
{
    class Program
    {
        // get boards
        string[,] f_board = new string[5, 5];
        string[,] b_board = new string[5, 5];

        // functions
        public string[,] GetBoard(char board, int size, string difficulty)
        {
            string[,] array = new string[size, size];
            if (board == 'f')
            {
                for (int i = 0; i <= size - 1; i++)
                {
                    for (int k = 0; k <= size - 1; i++)
                    {
                        array[i, k] = "#";
                    }
                }
            }
            else if (board == 'b')
            {
                int mines = 0;
                if (difficulty == "easy") { mines = 5; }
                for (int i = 0; i <= size - 1; i++)
                {
                    for (int k = 0; k <= size - 1; i++)
                    {
                        
                    }
                }
            }
        }




        static void Main(string[] args)
        {
          
        }
    }
}
