## Data flow between app and agent

# Control from app:

- Settings, including a) whitelisted tokens, b) gas strategy, c) agent name; submitted with agent startup, not modifiable when agent runs (to begin with)

- Start agent, Stop agent

- Request withdrawal from agent; needs to specify amount only, address should be specified at startup (or at least be in a predefined whitelist) for security reasons;

Ideally, we operate a 'set and forget' model. The initial settings fully determine how the agent runs.

# Updates from agent:

- Liveness state

- Transaction hash of each performed transaction including time, tokens involved, description
