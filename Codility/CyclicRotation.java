// Pam Kitsuwan
// 12/27/2023
// Solution to Codility: Cyclic Rotation

import java.util.*;

class Solution
{
    public int[] solution(int[] A, int K)
    {
        // There is no array, directly return given array
        if (A.length == 0) return A;

        // No need to shift any numbers, directly return given array
        if (K == 0) return A;

        int[] solution = new int[A.length];

        for (int i = 0; i < A.length; i++)
        {
            // Insertion to solution array will be out of bounds
            if ((i + K) >= A.length)
                // Mod solution array to start placing numbers at the beginning
                solution[(i + K) % A.length] = A[i];
            // Insertion to solution array will not be out of bounds
            else
                // Directly copy number from A[i] to the solution array
                solution[i + K] = A[i];
        }

        // Return A rotated K times
        return solution;
    }
}
