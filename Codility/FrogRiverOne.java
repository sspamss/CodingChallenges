// Pam Kitsuwan
// 12/29/2023
// Solution to Codility: Frog River One

import java.util.*;

class Solution
{
    public int solution(int X, int[] A)
    {
        // Boolean array (1 byte) is less space expensive than integer arrays (4 bytes)
        boolean[] leafFreq = new boolean[X];
        int leafCount = 0;

        for (int i = 0; i < A.length; i++)
        {
            // Check if froggy has already seen the leaf
            if (leafFreq[A[i] - 1] == false)
            {
                // Froggy has seen leaf!
                leafFreq[A[i] - 1] = true;
                leafCount++;
            }
            // Froggy made it to the other side!
            if (leafCount == X) return i;
        }

        // Froggy never gonna make it to the other side :(
        return -1;
    }
}
