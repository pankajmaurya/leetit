package arrays_and_strings;

public class BuySellStockOnce {
    public static void main(String[] args) {
	int[] stockPrices = new int[] {310, 315, 275, 295, 260, 270, 290, 230, 255, 250};

	int minSeenSoFar = stockPrices[0];
	int profit = 0;
	for (int i = 1; i < stockPrices.length; i++) {
	    minSeenSoFar = Math.min(minSeenSoFar, stockPrices[i]);
	    profit = Math.max(profit, stockPrices[i] - minSeenSoFar);
	}
	System.out.println("Maximum profit will be " + profit);
    }
}
