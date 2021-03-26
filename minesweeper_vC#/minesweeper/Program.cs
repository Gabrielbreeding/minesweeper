using System;
using static System.Console;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/* Gabriel Breeding
 * 
 * ToDoList:
 *      Create a multidimensional array for the minesweeper board. **COMPLETE
 *      Make an input so the user can manipulate the board. **COMPLETE
 *      add function to place mines randomly on the board. **COMPLETE
 *      add function to accurately depict how many mines are in a specified area. **COMPLETE
 *      add win/lose conditions.
 *      add feature that will stop the scenario where a user instantly loses on their first move.
 *      add score counter.
 *      add a way to keep track of score even after the program ends.
 *      add a feature when the user reveals an empty tile, all neighboring empty tiles are revealed as well. **COMPLETE 
 *      add visuals for x and y coordinates.
 * 
 * 
 * 
 * 
 * 
 */

namespace minesweeper
{
    class Program
    {
        const int SIZE = 20;
        static Minesweeper game = new Minesweeper(SIZE);
        static void Main(string[] args)
        {
            string coordinate = "";
            string[] coordinates = new string[2];
            bool fail = false;
            bool win = false;
            int moves = 0;
            while (!fail && !win)
            {
                WriteLine(game.ToString());
                WriteLine("Enter a Coordinate to flip a tile.\nEnter 'x,y' or enter 'flag, x,y' to flag a tile");
                coordinate = ReadLine();
                coordinates = coordinate.Split(',');
                if (coordinates[0].ToUpper().Trim() == "FLAG")
                {
                    if (validate(coordinates[1].Trim()) && validate(coordinates[2].Trim()))
                    {
                        ++moves;
                        game.flag(Convert.ToInt32(coordinates[1]) - 1,SIZE - Convert.ToInt32(coordinates[2]));
                    }
                    else
                    {
                        WriteLine("ERROR\n" +
                                  "The Required format is y,x Ex; 1,1  2,2  6,9  84,7.\n" +
                                  "Press any key to contine.");
                        ReadLine();
                    }
                }
                else if (validate(coordinates[0]) && validate(coordinates[1]))
                {
                    ++moves;
                    game.reveal(SIZE - Convert.ToInt32(coordinates[1].Trim()) , Convert.ToInt32(coordinates[0].Trim())-1);
                    if (game.fail == true)
                    {
                        fail = true;
                    }
                }
                else
                {
                    WriteLine("ERROR\n" +
                              "The Required format is y,x Ex; 1,1  2,2  6,9  84,7.\n" +
                              "Press any key to contine.");
                    ReadLine();
                }
                // check for win
                if (game.count(game.FrontBoard, 'F') + game.count(game.FrontBoard, '#') == game.count(game.BackBoard, 'M'))
                {
                    win = true;
                }
            }
            if (fail)
            {
                WriteLine(game.ToString() + "\nOh No! \nYou Died in {0} moves!!", moves);
                ReadLine();
            }
            else if (win)
            {
                WriteLine(game.ToString() + "\nCongrats! \nYou beat the game in {0} moves!!", moves);
                ReadLine();
            }
            

            
        }

        static bool validate(string num)
        {
            int test = 0;
            return int.TryParse(num, out test);
        }
    }
}
