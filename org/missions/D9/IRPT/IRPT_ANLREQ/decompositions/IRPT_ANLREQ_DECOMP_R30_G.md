# IRPT_ANLREQ round 30, workstream ~G (ENGINE) -- decomposition: irpt-status returns the closed failure code and its words (C-HOP-FAILURE, the reader half)

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** PRD v0.20/v0.21 contract C-HOP-FAILURE clauses (1) and (2) and CTO msgs 8907 and 8971: the ticket page reads the status route; `irpt-status` returns a closed failure code beside the state, with one words table in `status.py`; `~G2` owns the code and words in `status.py` and `owned_status.py`; `~V2` owns the page read and parks until this shape is merged (msg 8974). Round 28 merged the writer half (`AR-g-109`, `bc0e7e96c4`: `HOP_FAILURE_CODES`, `mark_hop_failure`, `get_state` carrying `hop_failure`, the keyed writer for the commentary hop).

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **No new envelope field, no schema change.** The closed failure code travels as the existing `public_reason_code` (regex `^[A-Z0-9_]+$`), the words as the description of one safe `NONE` action (an existing action in the contract). The page reads code = `public_reason_code`, words = that action's description, step = named in the words. The shape is stated in the merge commit message, as `~V2` asked.
- **A FAILED or ATTENTION job also gets the generate step's words** (the contract: an unmapped code reads as its step's generic words, never blank), and keeps its state and its reason code. Two existing assertions in `ops/tests/test_owned_status.py` therefore change (listed in the order).
- **The `at` timestamp and any detail text are never echoed;** only fixed strings from one literal table.
- **The Lambda leg is a later cell and pair:** `lambda-source-map.json` re-pins `status.py`, `owned_status.py` and `durable_job.py` for `irpt-status`, built and applied like r33. The resident carries `durable_job.py` and the writers in r35.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-111` | `FAILURE_STEP_WORDS`, `FAILURE_WORDS`, `failure_words` in `status.py`; `_failure` and the reader change in `owned_status.py`; two existing assertions updated; one new test file | the three product files, one test file | WORLD (floor of an infrastructure path; source only) |

## Edges and chains

- ONE chain. Depends on `AR-g-109` (merged). Feeds the irpt-status release (map re-pin, build, pair, AQ2 apply) and `~V2`'s page cell.

## Four-postulate record

(i) Domain: the five hop codes plus `DELIVERIES_EXHAUSTED`, four steps. (ii) One words table read by one reader; the issuer test cross-checks the writers' `HOP_FAILURE_CODES` against it. (iii) One intent. (iv) What this cut does NOT move: the envelope schema, the state mapping, IAM, any Lambda until its release.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 253).
