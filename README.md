Freex Documentation
The gist:
The bot determines the success of a crypto wallet using the ratio of successful output transactions to the total number of output transactions (winrate) and the ratio of investment to output (Raise of income). I used the eth protocol when requesting via web3
ROI:

The bot requests transactions for a year for a specific wallet.

IMPORTANT: for this reason, the bot may not match some sources due to its period and orientation of the eth protocol.

The eth protocol describes the cost of a token in gwei. To calculate the cost of a token, we will convert gwei to eth. (line 65).
For a more competent calculation of ROI, we will take into account the fluctuation of the eth exchange rate. To do this, save the eth price for the year

We will convert eth to dollars and determine what kind of transaction this is:

At the end, we sum up the annual turnover and use the output to input ratio.

We get ROI
FAQ:
Will transfer transactions affect roi?
Rarely will non-investment transactions increase or decrease the ROI. Their impact will be minimal. Moreover, trader wallets will have a large ROI (more than 1), while non-trader wallets will not. For example, Buterin's wallet has an annual ROI of 0.85, indicating that he is not using the wallet to increase his capital
What if the code shows an ROI greater than 10 or greater than 100?
This means that the investment is long-term (more than one year). It is worth looking at the winrate or increasing the investment period estimate (more than one year)

Winrate:
Request information using the same protocol, but now takes into account the price change relative to gwei to balance the wallet rating and combine it with ROI.

FAQ:

What if the winrate is 100, 50 or 25?
There is a certain share of technical wallets on the market that are used for price speculation. They belong to funds, currency developers and other institutional investors. Such wallets are useful because they can predict the movement of currencies. This is great for insider trading. However, it can also be a dormant wallet. It is worth looking at transactions and volume
Transactions
Transactions are also taken into account using the same protocol, but they are more accurately scheduled and their information is classified

If there are no or few transactions per year, it is recommended not to use a dormant wallet.
The csv database contains wallets with an ROI greater than 1.
