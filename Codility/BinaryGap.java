// Pam Kitsuwan
// 12/27/2023
// Solution to Codility: Binary Gap

import java.util.*;

class Solution
{
    public int solution(int N)
    {
        boolean seenBoundary = false;
        int currSolution = 0, finSolution = 0;

        // Get binary of a number
        String result = Integer.toBinaryString(N);

        for (int i = 0; i < result.length(); i++) {
            // Boundary encountered
            if (result.charAt(i) == '1') {
                // Keep the current length of the longest gap
                finSolution = Math.max(finSolution, currSolution);
                // Reset the current gap counter
                currSolution = 0;
                // First 1 (gap boundary) has been encountered
                seenBoundary = true;
            }
            // Gap encountered
            if (seenBoundary && result.charAt(i) == '0')
                // Increment our current gap counter
                currSolution++;
        }

        // Return the length of the longest gap
        return finSolution;
    }
}
