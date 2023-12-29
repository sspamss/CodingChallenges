// Pam Kitsuwan
// 12/28/2023
// Solution to Codility: Tape Equilibrium

import java.util.*;

class Solution
{
    public int solution(int[] A)
    {
        int curSolution = 0, finSolution = Integer.MAX_VALUE;
        int arrSum = 0, frontSum = 0, backSum = 0;

        // Get the sum of the given array
        for (int i = 0; i < A.length; i++) arrSum += A[i];

        // Loop through array up to A.length - 1 (front "half" at A[0], back "half" at A[1])
        for (int j = 0; j < A.length - 1; j++)
        {
            // Get sum of array from front "half" of array up to index
            frontSum += A[j];
            // Get sum of array from index + 1 to back "half" of array
            backSum = arrSum - frontSum;
            // Get the difference between front "half" and back "half"
            curSolution = Math.abs(frontSum - backSum);
            // Compare the current minimal difference with the final minimal difference
            finSolution = Math.min(curSolution, finSolution);
        }

        // Return tape minimal difference
        return finSolution;
    }
}
