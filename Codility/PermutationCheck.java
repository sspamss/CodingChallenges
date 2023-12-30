// Pam Kitsuwan
// 12/29/2023
// Solution to Codility: Permutation Check

import java.util.*;

class Solution
{
    public int solution(int[] A)
    {
        // Boolean array (1 byte) is less space expensive than integer arrays (4 byte)
        boolean[] leafFreq = new boolean[A.length];

        for (int i = 0; i < A.length; i++)
        {
            // Array size is how many unique numbers are in the permutation
            if (A[i] > A.length || leafFreq[A[i] - 1]) return 0;

            // Check if a number has aready been encountered
            if (!leafFreq[A[i] - 1]) leafFreq[A[i] - 1] = true;
        }

        // Return 1 as Array A is a permutation
        return 1;
    }
}
