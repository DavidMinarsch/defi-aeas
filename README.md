# defi-aeas

A repo to explore AEA implementations for DeFi

## Development

Setup development environment:

```bash
make new_env
pipenv shell
```

## Build latest AEA:

```bash
aea fetch defi_aeas/uniswap_aea:latest
cd uniswap_aea
aea install
```

Start AEA:
```bash
aea run
```

Navigate in browser to `localhost:8000/status`.

## Docs

Run docs server:

```bash
make docs
```


