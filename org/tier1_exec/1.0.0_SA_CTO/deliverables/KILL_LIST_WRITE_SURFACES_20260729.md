# KILL LIST — dead write surfaces (comp-legacywriter census, live-verified)

**Author:** `1.0.0_SA_CTO~C` · 2026-07-29 · **archetype:** DIAGNOSE
**Andrew-direct:** *"That's what we're looking for is a kill list, we want to clear debt"* + *"go way,
way harder ... check their last invocation, run comp-heat and comp-dups on them"* + *"I feel like we
have way more dead code and write surfaces than 32"*

**He was right about the population.** The prior "32" was the estate intersected with a 44-day-old
snapshot's 59 keys — a denominator inherited from a stale artifact. Measured from live source:

| measure | value |
|---|---|
| files scanned | 8,913 |
| write / read / probe sites | 857 / 1,226 / 181 |
| distinct `(bucket,key)` locations | 643 (437 written) |
| **written, zero AST reader** | **353** |
| locations with a **silent-default** reader | 66 |

---

## READ THIS FIRST — two false-positive classes, one of which nearly shipped

### 1. TRANSIENT KEYS LOOK EXACTLY LIKE DEAD KEYS

An existence check cannot distinguish **never written** from **written-then-consumed-and-deleted**.
Four Tier-A entries are trigger markers, and they are among the *most live* objects in the estate:

```
opal-data-inf/gold/trigger-pending.json        <- inf-gold-trigger/lambda_function.py:68
opal-data-inf/gold/trigger-mode.json           <- inf-gold-trigger/lambda_function.py:53
opal-data-inf/orion/bronze-trigger-mode.json   <- inf-bronze-trigger/lambda_function.py:40
opal-data-bd/gold/trigger-*.json               <- bd-gold-trigger/lambda_function.py
```

> **A MARKER THAT IS WRITTEN, READ, AND DELETED IS ABSENT AT EVERY MOMENT YOU LOOK AT IT.**
> Retiring one of these writes would break a live pipeline trigger. They are **EXCLUDED** below,
> and any future run of this census must exclude the marker class before publishing a list.

`gold/meta/pipeline-complete.json` is the same family and carries its own separate prohibition
(hand-writing it is a forged completion signal).

### 2. MY OWN SWEEP RETURNED 81/81 FALSE ABSENCE, AND TWO PASSING CONTROLS DID NOT CATCH IT

The first existence sweep reported **every** candidate absent. That was a **CRLF bug**: native
Python wrote `cands.tsv` with `\r\n`, bash's `read` kept the `\r`, so every AWS call asked for
`key\r`. `cat -A` showed `^M` *inside the key field*.

What makes this worth recording is what did **not** save me:

- the **mechanism control passed** (listing found a known-present key)
- the **per-bucket control passed** (8 of 9 buckets provably listable)

Both controls were typed literally in the shell, so neither carried the corruption. **A control that
does not travel through the same argument path as the target cannot detect argument corruption.**
The oracle that worked was the banked one: *echo the argument back*. After the fix: **61 EXIST, 21
ABSENT** — not 81.

Also, separately: `head-object` failed on a key `list-objects-v2` had just returned. CLAUDE.md
already says *"HeadObject IS s3:GetObject, never the acceptance instrument — landing verification is
LISTING-based."* I used the instrument the law names, and the law was right.

---

## TIER A — DEAD WRITE PATH (retire the CODE; there is no object to delete)

Evidence bar per entry: concrete literal key · bucket **independently proven listable** · no object
under that key (listing-based) · zero reader in the scanned AST population · **not** a trigger marker.

**Blast radius is near-zero by construction: there is no object to break and no reader to re-point.**
The debt is the write statement.

The population concentrates hard, and the concentration is the story:

| dead targets | producer | class |
|---|---|---|
| 2 | `data/black_diamond/scripts/diagnostics/adhc_histry_006_rps_matching.py` | DIAGNOSTIC |
| 1 | `data/black_diamond/scripts/diagnostics/adhc_histry_005_schwab_crossref.py` | DIAGNOSTIC |
| 1 | `data/black_diamond/scripts/diagnostics/diag_acat_correlation_summary.py` | DIAGNOSTIC |
| 1 | `data/black_diamond/scripts/diagnostics/diag_aua_correction_matrix.py` | DIAGNOSTIC |
| 1 | `data/black_diamond/scripts/diagnostics/_schwab_bd_account_match.py` | DIAGNOSTIC |
| 1 | `data/black_diamond/archive/silver_layer/llm_ticker_matcher.py` | ARCHIVE |
| 1 | `data/black_diamond/archive/analysis/generate_hybrid_aua_chart.py` | ARCHIVE |
| 1 | `data/black_diamond/archive/fargate/.../08_generate_timeseries_chart.py` | ARCHIVE |
| 1 | `data/black_diamond/archive/fargate/.../11_generate_clients_tab.py` | ARCHIVE |
| 1 | `data/black_diamond/archive/fargate/.../12_generate_aua_chart.py` | ARCHIVE |
| 1 | `data/black_diamond/archive/fargate/.../13_generate_flows_chart.py` | ARCHIVE |
| 1 | `data/find/imo/scripts/bronze/test_crawl_linkedin_bronze.py` | TEST |
| 2 | `infra/aws/globgrph/fedobs/fedobs_emit.py` | PROBE (`__fedobs_boundary_probe__`) |

**The cleanest debt in the estate is `archive/` + `diagnostics/` + `test_*` producers writing to keys
that do not exist.** Five `json/advisor-intelligence/*` keys are written by
`black_diamond/archive/fargate/scripts/gold_layer/*` — a retired Fargate gold layer still carrying
live-looking `put_object` calls to a served prefix that holds no such object.

**EXCLUDED from Tier A** — trigger markers (transient, see above) and
`opal-code-smartx/lambda-smartx-query.zip` (**bucket not listable → verdict WITHHELD as UNKNOWN, not
absent** — the one bucket whose control failed).

## TIER B — OBJECT EXISTS, NO AST READER (61) — **NOT KILLABLE ON THIS EVIDENCE**

61 surfaces hold a real object and have no reader in the scanned population. That is **not** "no
reader": the AST scan cannot see portal TSX consumers, shell readers, or out-of-root code.

**The axis that closes this is `comp-whoread`** — CloudTrail object-level data events, the only
instrument in the estate that reports who *actually* read a prefix. Its own registry row states the
discipline: the denominator is the coverage window, printed line 1; it **fails closed** on zero
events in range; and its result is *"a floor on reachability, never a ceiling."* So it can retire a
surface only in combination, never alone.

---

## THE REGISTRY SURVEY — which instruments can actually close this

Surveyed `tools_index` for key/object/read/invocation vocabulary rather than recalling it:

| instrument | what it adds | grain | why it matters here |
|---|---|---|---|
| **comp-whoread** | principals that **actually read** (CloudTrail via Athena) | prefix | the only true reader oracle; closes Tier B |
| **comp-icedrill** | version/partition **vintage history** | **key** | last real write per key; empty is a FINDING |
| **comp-xray frozen** | **frozen-but-fresh** content motion | **key** | catches a zombie rewritten with identical bytes |
| **comp-clobber --sweep** | etag-lineage interleave across a prefix | **key** | the OBSERVED contest oracle |
| comp-keys | what exists under a prefix | prefix | existence, denominator-always |
| comp-debris | last invocation / dormancy | **bucket / lambda** | already joined — see grain caveat |
| comp-heat | producer **code** recency (git) | file | already joined |
| comp-dups | exact-dup producer twins | file | already joined |

**The grain column is the finding.** `comp-debris` bands a **bucket**; the three key-grain
instruments (`comp-icedrill`, `comp-xray`, `comp-clobber --live`) are the ones that can say anything
about an individual object. A dormant key inside a hot bucket is precisely the zombie shape, and only
those three can see it.

## RECOMMENDED SEQUENCE

1. **Tier A now** — retire the `archive/` + `diagnostics/` + `test_*` write statements. Near-zero
   blast radius. Owner lane, never-widen, deploy ledger as normal. **Do not touch the markers.**
2. **`comp-whoread` over the Tier-B prefixes** — converts 61 candidates into a real verdict.
3. **`comp-icedrill` + `comp-xray frozen`** on Tier-B survivors — key-grain last-write and frozen
   detection, which is where the *interesting* zombies are (object exists, looks fresh, content dead).
4. Then re-run `comp-legacywriter --census` and the list should shrink measurably. That shrinkage is
   the debt-clearing metric.

**Nothing in this document is a deletion authorization.** comp-legacywriter recommends; the kill
rides the owner's lane, never-widen sign-off, and the deploy ledger.

## Compiler Tools

| tool | use | result |
|---|---|---|
| `comp-legacywriter --census` | the census + dossier join | 437 written surfaces, 353 reader-less |
| `comp-heat freshness --json` | producer code recency | 25,100 paths banded |
| `comp-dups --json` | exact-dup twins | 1 exact-dup group (smartx query lambda) |
| `comp-debris --types lambda,s3` | invocation/dormancy | 229 resources; **bucket-grain** |
| `aws s3api list-objects-v2` | per-key existence (rail-checked) | 61 exist / 21 absent |
| registry survey (`tools_index`) | which tools can close the gap | 18 candidates, 4 key-grain |
