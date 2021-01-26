
This repo explores using the AEA framework in DeFi.

The idea is to explore how we can use the AEA framework and its primitives (skills, connections, contracts and protocols) to build a set of abstract packages which can then be instantiated for specific protocols in AEAs to automate common user interactions with these on-chain protocols.

The first AEA integrates with [Uniswap](https://uniswap.org/), that is we focus on liquitidy provision.

## Rough flow:

1. user funds AEA with ETH and list of whitelisted tokens with an existing uniswap trading pair (see [official docs](https://uniswap.org/docs/v2/core-concepts/pools/))

2. AEA establishes which pool (ETH-token X pair) provides highest APR; say token A

3. AEA establishes how much token A needs to be purchased to supply liquidity in pool with availabke ETH (keeping some ETH for gas); then purchases that amount of A

4. first time AEA buys token A it makes an infinite approval tx for Uniswap for token A

5. AEA supplies liquidity for ETH-token A pair and gets pool token in return

6. At certain tick rate, AEA establishes which pool (ETH-token X pair) provides highest APR; if token A no longer provides highest APR then AEA withdraws from pool and liquidates A, continues at 3.;

## Deterministic and probabilistic elements

The above flow is largely deterministic. There are a number of probabilistic elements which require forecasting models to be maintained:

- gas estimation for tx execution; can use standard Infura API to start with
- gas price estimation; can start with API like gas station (https://docs.ethgasstation.info/)
- APR estimation; can start with 3rd party API, then try to estimate ourselves eventually (https://www.liquidityfolio.com/# or https://docs.blocklytics.org/apis/pools-api or https://info.uniswap.org/pairs)

## Alternative approaches

The v1 design approach assumes no additional smart contract deployment. It is out-of-the-box ready to use with default uniswap contracts.

Alternatively, one could deploy further on-chain elements, like proxy contracts to optimise and safe-guard some interactions. However, this also adds complexity and cost, which makes it less user friendly. It is also a less agile approach as it requires more investment in smart contract development.
