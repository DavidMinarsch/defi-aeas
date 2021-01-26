## CapitalAllocationSkill

(WIP)

The role of this skill is to continuously allocate capital to the most profitable pool whilst ensuring overall profitability (i.e. accounting for gas costs).

<div class="mermaid" id="capital">
    classDiagram
        CapitalAllocationSkill <|-- Model
        CapitalAllocationSkill <|-- Behaviour
        CapitalAllocationSkill <|-- Handler
        Model <|-- Strategy
        Model <|-- Tokens
        Model <|-- Pools
        Tokens : whitlisted_tokens()
        Tokens : List[Token]
        Strategy : List~Token~ _tokens
        Strategy : +bool is_active
        Strategy : +Pool active_pool
        Strategy : +Pool next_active_pool
        Strategy : +get_pool_with_highest_apr_forecast() : Pool
        Strategy : +is_rebalancing_profitable(Pool, Pool)
        Tokens .. Token
        Strategy .. Tokens
        Token : +String address
        Token : +String name
        Token : +String symbol
        Pools : +List[Pool]
        Pools .. Pool
        Pool : +String address
        Pool : +Tuple[Token, Token] pair
        Pool : +PoolStatus status
        Pool .. Token
        Pool .. PoolStatus
        PoolStatus : NO_PROVISION
        PoolStatus : PROVISION_PENDING
        PoolStatus : PROVISION_ACTIVE
        PoolStatus : WITHDRAWAL_PENDING
        Behaviour <|-- CapitalAllocationBehaviour
        Handler <|-- LedgerApiHandler
        Handler <|-- ContractApiHandler
        CapitalAllocationBehaviour : +int tick_interval
        CapitalAllocationBehaviour : +act()

</div>

The `act` implementation can be along the lines of the following (pseudo-)code:

``` python
if not strategy.is_active:
    # nothing to do
    return

new_pool = strategy.get_pool_with_highest_apr_forecast()
# we assume sync retrieval here as APR for all pools is
# locally stored and updated continuously

if new_pool == strategy.active_pool:
    # already in best pool
    return

if new_pool is not None and not strategy.is_rebalancing_profitable(active_pool, new_pool):
    # here we assume sync retrieval as gas costs for rebalancing must
    # be continuously monitored and locally stored, although we
    # need to ensure this estimate is recent enough
    return

active_pool = strategy.active_pool
strategy.next_active_pool = new_pool
self.initiate_withdrawal(active_pool)
# this will request withdrawal transaction flow
```

....TBC
