## CapitalAllocationSkill

(WIP)

The role of this skill is to continuously allocate capital to the most profitable pool whilst ensuring overall profitability (i.e. accounting for gas and reallocation costs).

<div class="mermaid" id="capital">
    classDiagram
        CapitalAllocationSkill <|-- Model
        CapitalAllocationSkill <|-- Behaviour
        CapitalAllocationSkill <|-- Handler
        Model <|-- Strategy
        Model <|-- OnChainItemCollection
        OnChainItem <|-- Token
        Token : +String address
        Token : +String name
        Token : +String symbol
        Pool .. Token
        OnChainItem <|-- Pool
        Pool : +String address
        Pool : +Tuple[Pool, Pool] pair
        OnChainItem <|-- Transaction
        OnChainItem : +String onchain_id
        OnChainItemCollection : -Dict[OnChainItemId, OnChainItem] _items
        OnChainItemCollection : +add(OnChainItem)
        OnChainItemCollection : +get(OnChainItemId)
        OnChainItemCollection : +to_json()
        OnChainItemCollection <|-- Tokens
        OnChainItemCollection <|-- Pools
        OnChainItemCollection <|-- Transactions
        OnChainItemCollection .. OnChainItem
        Tokens .. Token
        Pools .. Pool
        Transactions .. Transaction
        Behaviour <|-- FSMBehaviour
        FSMBehaviour <|-- CapitalAllocationBehaviour
        Handler <|-- HttpHandler
        Handler <|-- LedgerApiHandler
        Handler <|-- ContractApiHandler
        CapitalAllocationBehaviour : +int tick_interval
        CapitalAllocationBehaviour : +Set[String] states
        CapitalAllocationBehaviour : +act()
        Strategy : -List~string~ _token_whitelist
        Strategy : -Dict[Pool,PoolStatus] _pool_statuses
        Strategy : +AgentStatus agent_status
        Strategy : +Pool active_pool
        Strategy : +Pool next_active_pool
        Strategy : +update_pool_status(Pool, PoolStatus)
        Strategy : +add_to_whitelist(List[TokenAddress])
        Strategy : +remove_from_whitelist(List[TokenAddress])
        Strategy : +get_pool_with_highest_apr_forecast() : Pool
        Strategy : +is_rebalancing_profitable(Pool, Pool) : bool
        Strategy .. AgentStatus
        AgentStatus : ACTIVE
        AgentStatus : PAUSED
        Strategy .. PoolStatus
        PoolStatus : NO_PROVISION
        PoolStatus : PROVISION_PENDING
        PoolStatus : PROVISION_ACTIVE
        PoolStatus : WITHDRAWAL_PENDING
        PoolStatus : WITHDRAWAL_COMPLETE
        Transaction : +Int amount
        Transaction : +String denomination
        Transaction : +String currency
        Transaction : +String timestamp
        Transaction : +String from_address
        Transaction : +String to_address
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
