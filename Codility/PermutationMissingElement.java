// Pam Kitsuwan
// 12/28/2023
// Solution to Codility: Permutation Missing Element

import java.util.*;

class Solution
{
    public int solution(int[] A)
    {
        Arrays.sort(A);

        int check = 1;

        for (int i = 0; i < A.length; i++)
        {
            // Check if we are missing a value by matching it against the counter
            if (A[i] != check) return check;

            check++;
        }

        // The array is not missing any consecutive numbers
        return check;
    }
}
