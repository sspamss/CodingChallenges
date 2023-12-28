// Pam Kitsuwan
// 12/27/2023
// Solution to Codility: Odd Occurrences In Array

import java.util.*;

class Solution
{
    public int solution(int[] A)
    {
        HashSet<Integer> aMap = new HashSet<Integer>();

        // Remove all matched values, this leaves one value in the HashSet (the unpaired value)
        for (int i = 0; i < A.length; i++)
        {
            // Find then remove matched values
            if (aMap.contains(A[i])) aMap.remove(A[i]);
            // Otherwise, add value to the map
            else aMap.add(A[i]);
        }

        // Return the unpaired value
        return aMap.iterator().next();
    }
}
