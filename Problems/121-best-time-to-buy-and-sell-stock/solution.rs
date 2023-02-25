impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut min_price: i32 = i32::max_value();
        let mut profit: i32 = 0;

        for price in prices {
            if price < min_price {
                min_price = price
            } else if price - min_price > profit {
                profit = price - min_price;
            }
        }

        return profit;
    }
}
