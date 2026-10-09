# ANDREW-DIRECT 2026-10-09 ~06:2xZ -- close NFRA_SPRINTWIN

**Channel:** the `1.0.0_SA_CTO~Z` terminal, site Z, during the site-Z wind-down for a reboot. Recorded the same turn by `1.0.0_SA_CTO~Z`.

## His words, VERBATIM AND ENTIRE

> "Close this project: NFRA_SPRINTWIN"

## What it rules

NFRA_SPRINTWIN is CLOSED on his word. It is not graduated by a round: it closes at `dep_stage: PRD` (PRD admitted, L5 never cut).

## State at close, read by this seat at 06:2xZ

| read | result |
|---|---|
| tree row | `org/missions/D0/NFRA/NFRA_SPRINTWIN/project.json`: `active`, `PRD`, `coo_lane: 2.0.0_SA_COO~SW` (seated ~05:xxZ) |
| open orders | `to-check --all --project NFRA_SPRINTWIN`: 0 active |
| open deploy ledgers | 0 |
| surprise rows | 6, all `hazard_standing: INERT` |
| uncommitted edits under the project tree | 0 |

## Carriers moved with this record (L3, the CTO's)

- The tree row: `status: closed`, `closed: 2026-10-09`, `closed_by:` this record, the same shape as NFRA_CLDGRPH's close.
- The generated index, by `missions-tree-index.py derive --write`, in the same commit.
- Unchanged by design: the DIRECTIVES.yaml D0 members line (closed members stay listed, as NFRA_CLDGRPH does), and `SEQUENCE.yaml`,
  which holds placement, not status. The sequence reader stops queueing the project for a COO slot once its row reads closed.
- `2.0.0_SA_COO~SW` has no work. `0.0.0_AB_MSTR~Z` drops it from the site-Z autolaunch roster for the reboot.

-- 1.0.0_SA_CTO~Z
