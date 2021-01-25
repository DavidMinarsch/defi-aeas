
The first DeFi AEA will automate optimal liquidity provision to Uniswap.

Below we give an overview of the design of this AEA.

(WIP)

## Main Elements

<div class="mermaid" id="overview">
    sequenceDiagram
        activate Frontend
        activate AEA
        activate Blockchain
        Frontend-->AEA: HTTP
        AEA-->Blockchain: RPC/HTTP
        deactivate Frontend
        deactivate AEA
        deactivate Blockchain
</div>

### AEA

Built with AEA framework.
We need multiple skills:

- PoolAPRSkill
- CapitalAllocationSkill

And contracts:

- UniswapPoolContract

### Frontend

Built with framework of our choice. Talks to AEA directly (using http server connection) or to its own server and server talks to AEA via connection of choice.
