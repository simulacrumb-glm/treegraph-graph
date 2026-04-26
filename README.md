# Treegraph Graph: Conflux Network Web3 Entities Visualization

This repository contains an interactive graph visualization of Web3 entities within the Conflux Network ecosystem. The visualization displays relationships between dapps, bridges, centralized exchanges (CEX), wallets, coins, and networks using Cytoscape.js.

## Overview

The graph is built from CSV data files that define nodes (entities) and links (relationships). The data is processed into JSON format for the web application.

## Data Structure

### Nodes (poc/nodes.csv)
Each node represents a Web3 entity with the following format:
```
id|type|fields
```

- **id**: Unique UUID for the entity
- **type**: Entity type (bridge, dapp, cex, wallet, coin, network)
- **fields**: JSON string containing entity details (name, url, features, icon)

### Links (poc/links.csv)
Links define relationships between entities:
```
source|dest|predicate
```

- **source**: Source entity ID
- **dest**: Destination entity ID
- **predicate**: Relationship type (see Predicates section below)

## Predicates

The graph uses bidirectional relationships. Each predicate has an inverse:

- **contract_deployed_on** / **has_contract**
  - Direction: Contract → Network / Network → Contract
  - Meaning: A contract is deployed on a network / A network has a contract

- **has_listed_member_of** / **has_member**
  - Direction: Network → List / List → Member
  - Meaning: A network has a listed member in a token list / A list has a member entity

- **has_native_coin**
  - Direction: Network → Coin
  - Meaning: A network has a native coin

- **has_signer**
  - Direction: Network → Entity
  - Meaning: A network has a signer entity

- **has_transactor**
  - Direction: Network → Entity
  - Meaning: A network has a transactor entity

- **operates_on** / **has_member**
  - Direction: CEX → Network / Network → CEX
  - Meaning: A CEX operates on a network / A network has a CEX as a member

## Adding New Links

To add a new relationship between entities:

1. **Identify entity IDs**: Find or add the source and destination entity IDs in `poc/nodes.csv`
2. **Add bidirectional links**: Add two rows to `poc/links.csv`:
   - Forward relationship: `source_id|dest_id|predicate`
   - Inverse relationship: `dest_id|source_id|inverse_predicate`
3. **Regenerate data**: Run `python poc/csv_to_json.py` to update `poc/data.json` and `data.js`
4. **Test**: Reload the web app to see the new links

### Example: Adding a CEX-Network Relationship

To add that MEXC operates on Conflux eSpace:

```
# Forward link
aa2df60b-1739-4e48-b746-26731e6ba8fd|7b760c3b-f49f-4cd8-8ab0-57e06cc0e484|operates_on

# Inverse link
7b760c3b-f49f-4cd8-8ab0-57e06cc0e484|aa2df60b-1739-4e48-b746-26731e6ba8fd|has_member
```

## Running the Application

1. Start a local server: `python -m http.server 8000`
2. Open `http://localhost:8000` in your browser
3. Use the filter buttons to show/hide different entity types

## Dependencies

- Python 3 with pandas
- Cytoscape.js libraries (loaded via CDN)

## File Structure

```
/
├── index.html          # Main web application
├── data.js            # Processed graph data (generated)
├── poc/
│   ├── nodes.csv      # Entity definitions
│   ├── links.csv      # Relationship definitions
│   ├── data.json      # Processed data (generated)
│   └── csv_to_json.py # Data processing script
```