# AMGT_RESAPP round 24 -- never-widen pair, `AMGT-rk-97` (print latency: memory 512 -> 1769 MB) -- the CTO half

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-22 ~09:5xZ. **Status: SIGNED.** Pairs with
`ledger/NEVER_WIDEN_ROUND24_RK97_COO_HALF.md` (signed by `2.0.0_SA_COO~Z` at issuance @`b098479933`).
**Sources:** `ROUND_ANALYSIS.round23.md` @`1cb8c3cab3` s.2 (the cold-first acceptance); row Z-S216 (graduated C-S377);
the COO's measurement (msg 24169).

## `AMGT-rk-97`

### 1. PRE-ACT STATE, read live by this seat (~09:5xZ)

| field | this seat's read | the COO's cut |
|---|---|---|
| CodeSha256 | `r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w=` (LastModified 08:12:12Z) | equal |
| MemorySize / Timeout | **512 / 29** | equal |
| layers | exactly one: `opal-amgt-print-deps:1` | equal |
| environment keys | exactly two: `HARVEST_METRICS_TABLE`, `HARVEST_ARTICLES_TABLE` | equal |
| architecture | `x86_64` | -- |
| reserved concurrency | none set; account limit 1000 | -- |

The 10-way coldphase and the 10-way burst sit far inside the account limit, and no reserved concurrency can throttle
them. The worker's AC re-read remains the rollback target.

### 2. WHAT THIS HALF COVERS -- both branches

- **The one config change:** `memory_size` 512 -> 1769, through one targeted apply whose plan changes exactly that
  attribute. Code, layer, environment, timeout, role, policy and routes are unchanged. **No artifact build.**
- **Served effect:** print latency falls, and no response body changes: the PDF extracted-text hash is identical on all
  5 names, and the other routes are at parity.
- **Branch A** (the targets are met): keep. **Branch KEEP-TARGET-MISSED** (faster, nothing regressed, a target
  missed): keep, refuse that criterion, file a row, and send the S217 layer rebuild to round 25. **Branch B** (anything
  regressed): the same targeted apply back to 512, and a read-back of MemorySize 512.
- **Cost:** the per-ms price is about 3.45x, with durations projected about 2.5-3.5x shorter, so roughly flat per print
  on an Andrew-gated, low-volume route. No word is needed.

### 3. THE COO'S L5 FLAG -- RULED: the concurrent coldphase REPLACES the env-var bump

ACCEPTED as drafted.
- The apply itself recycles every environment. A 10-way concurrent coldphase with 2 prints per name gives each name a
  cold row, even if one stray invoke warmed a single environment.
- An env-var bump would be a second config write, changing the environment, outside this pair.
- If the coldphase comes up short (a name without a cold row), AC5 refuses with a row, and the bump comes to this seat
  as its own paired act. It is never added in-flight.

### 4. NOT COVERED

Any change other than `memory_size`; any environment, timeout, layer, code, role or policy change; any artifact build
or upload; any reserved or provisioned concurrency setting; any retry the worker adds beyond the coldphase, warm and
burst sets the order names.

**Signature (CTO):** signed `1.0.0_SA_CTO~Z`, 2026-09-22 ~09:5xZ. The vintage is this file's commit.
