// Pam Kitsuwan
// 12/28/2023
// Solution to Codility: Frog Jump

import java.util.*;

class Solution
{
    public int solution(int X, int Y, int D)
    {
        // FIRST SOLUTION: O(n)
        // int curPosition = X, solution = 0;

        // // Frog already at desired destination
        // if (X == Y) return X;

        // while (curPosition < Y)
        // {
        //     curPosition += D;
        //     solution++;
        // }
        
        // // Return minimal jump number
        // return solution;

        // --------------------------------------------------

        // SECOND SOLUTION: O(1)
        // Y - X: Total frog distance
        // + D - 1: Basically fancy Math.ceil/floor
        // / D: Gets the minimum jump number
        return (Y - X + D - 1) / D;
    }
}
