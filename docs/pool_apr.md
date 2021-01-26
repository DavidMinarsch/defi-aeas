## PoolAPRSkill

(WIP)

The role of the skill is to continuously monitor a set of pools for their APR.

<div class="mermaid" id="apr">
    classDiagram
        PoolAPRSkill <|-- Model
        PoolAPRSkill <|-- Behaviour
        PoolAPRSkill <|-- Handler
        Model <|-- Strategy
        Model <|-- Tokens
        Model <|-- Pools
        Tokens : whitlisted_tokens()
        Tokens : List[Token]
        Strategy : List~Pools~ _pools
        Strategy : +get_pools_to_monitor()
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
        Behaviour <|-- PoolAPRBehaviour
        Handler <|-- HttpHandler
        PoolAPRBehaviour : +int tick_interval
        PoolAPRBehaviour : +act()

</div>

The `act` implementation can be along the lines of the following (pseudo-)code:

``` python
pools = strategy.get_pools_to_monitor()
self.request_latest_APR_forcecast(pools)
```

....TBC