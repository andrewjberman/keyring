# IRPT_ANLREQ round 31, workstream ~G (ENGINE) -- decomposition: the irpt-status source rows for the failure-code release

Issuer `2.0.0_SA_COO~G2`, 2026-10-16.

**Input:** C-HOP-FAILURE (PRD v0.21), CTO msgs 8907 and 8971. Round 28 merged the writer half (`AR-g-109`, `bc0e7e96c4`) and round 30 the reader half (`AR-g-111`, `766ec706ee`). `irpt-status` stages `status.py` and `durable_job.py` from pins in `lambda-source-map.json`; both pins are older than the merged work, so a build today would ship the old bytes.

## What this cut decides (ruled by the issuer, inside its own decomposition)

- **Two rows re-pin, the way `AR-g-102` re-pinned r33's:** `status.py` and `durable_job.py` of the function `irpt-status` (the same names exist under other functions and are NOT touched). `owned_status.py` is native to the function and rides with the tree. The expected delta of the next package against the r33 build: exactly `status.py`, `durable_job.py` and `owned_status.py` (3 members).
- **The release is staged as: this source cell, then a BUILD ONLY worker cell (`r35L`, a Lambda build like `AR-g-103`), a pair (with the resident r35 and the commentary role, the CTO decides how the three are packeted), and an AQ2 apply.** The resident writers (`AR-g-109`) ship in r35; `irpt-status` is applied first so the reader exists before any writer writes.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-113` | two re-pinned rows in `lambda-source-map.json` | the map only | WORLD (floor of an infrastructure path; source only) |

## Edges and chains

- ONE chain, depends on `AR-g-109` and `AR-g-111` (merged); feeds the `irpt-status` build cell.

## Four-postulate record

(i) Domain: two rows of one function. (ii) One pin rule (last commit touching the path). (iii) One intent. (iv) What this cut does NOT move: the `files` list, `last_deployed_*`, any other function, any live byte.

fanout: 1 of 1 chains, cap 8, reason: one worker cell (slot 254).
