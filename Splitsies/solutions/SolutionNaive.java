import java.io.*;
import java.util.*;
/*if you are trying to run this in your IDE,
either rename this file to Solution.java
or rename the line below to 
public class SolutionNaive {


*/
public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for(int i = 0; i < n; i++){
            nums[i] = sc.nextInt();
        }
        //naive: bubble sort
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n-1; j++){
                if(nums[j] > nums[j + 1])
                {
                    int temp = nums[j + 1];
                    nums[j + 1] = nums[j];
                    nums[j] = temp;
                }
            }
        }
        

        for(int i = 0; i < n; i++){
            if (nums[i] % 2 == 0){
                System.out.print(nums[i] + " ");
            }
        }
        for(int i = 0; i < n; i++){
            if (nums[i] % 2 != 0){
                System.out.print(nums[i] + " ");
            }
        }
    }
}