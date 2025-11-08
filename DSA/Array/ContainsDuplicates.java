import java.util.HashSet;

public class ContainsDuplicates {
    public static void main(String[] args) {
        int[] nums = { 1, 4, 3, 5, 4 };
        System.out.println(containsDuplicate(nums));
    }

    public static boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seenNumbers = new HashSet<>();

        for (int num : nums) {
            if (seenNumbers.contains(num)) {
                return true;
            }
            seenNumbers.add(num);
        }
        return false;
    }
}
