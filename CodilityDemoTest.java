// Pam Kitsuwan
// 12/26/2023
// Solution to Codility Demo Test

import java.util.*;

class Solution
{
    public int solution(int[] A)
    {
        // If the length of A is zero, then there is no array
        if (A.length == 0) return 1;

        Arrays.sort(A);

        // If the array is filled with negatives, then we return 1
        if (A[A.length - 1] < 1) return 1;

        int check = 1;

        for (int i = 0; i < A.length; i++)
        {
            // If we encounter a negative number, then we skip over that
            if (A[i] < 1) continue;

            // If we have duplicated numbers in the array, then we skip over that
            if (0 < i && A[i - 1] == A[i]) continue;

            // We can check if we are missing a value by checking it against the loop
            if (A[i] != check) return check;

            check++;
        }

        // Getting here means the array is not missing any consecutive numbers
        // Codility wants you to return the last number of the array plus one
        return check;
    }
}
