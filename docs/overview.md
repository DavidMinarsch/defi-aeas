
The first DeFi AEA will automate optimal liquidity provision to Uniswap.

Below we give an overview of the design of this AEA.

We need multiple skills:

- PoolAPRSkill
- CapitalAllocationSkill

And contracts:

- UniswapPoolContract


Open questions:

- finish v1 design; this approach assumes no additional smart contract deployment. It is out-of-the-box ready to use with default uniswap contracts.
- investigate https://docs.zapper.fi/invest/pooling/uniswap
- investigate having a proxy contract which does the optimal rebalancing on chain; downside: this is less user friendly for the user