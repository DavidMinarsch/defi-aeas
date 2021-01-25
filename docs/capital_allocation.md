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
        Strategy : +get_pool_with_highest_apr_forecast()
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
        Pool .. Token
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

if strategy.is_
new_pool = strategy.get_pool_with_highest_apr_forecast()
# we assume sync retrieval here as APR for all pools is
# locally stored and updated continuously

if new_pool == strategy.active_pool:
    # already in best pool
    return

if not strategy.is_rebalancing_profitable(active_pool, new_pool):
    # we assume sync retrieval as gas costs for rebalancing must
    # be continuously monitored and locally stored
    return

active_pool = strategy.active_pool
strategy.next_active_pool = active_pool
active_pool.initiate_withdrawal()
# this will request withdrawal transaction
```
