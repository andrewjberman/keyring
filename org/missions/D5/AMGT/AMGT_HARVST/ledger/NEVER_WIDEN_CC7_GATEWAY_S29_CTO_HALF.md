# AMGT_HARVST round 88 -- never-widen pair, HVST-cc-7 (`opal-gateway` serves the three D1-S29 fixes) -- CTO HALF (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~16:4xZ)

**Binds:** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round88/NEVER_WIDEN_HALF_COO_CC7_GATEWAY_S29.md` @a84dbdc1e7,
sha256 `b5c79b76ca3bc1a1e913601b9ea4f924cff2999e509957ec490dd762cffde710` (43 lines), re-hashed by this seat. Any edit voids this half.

## Read and accepted

- **The three served changes match this seat's rulings:** the round-87 analysis and its ERRATA 1 and 2.
  - The EPS basis carries its claim, additively.
  - KMB's two misfiled Mexico reports are excluded and named with their reason.
  - A ticker-shaped query found only as a name prefix answers `candidates`, not `exact`.
- **The control is the right one:** cut on the LIVE deployed commit, with the six-path diff printed and checked on the seat's output.
- **Blast radius:** `opal-gateway` serves every MCP tool for every principal on every box, so this act reaches beyond dell1. What it moves
  is three harvest read tools' responses, plus a brief restart. Every other tool's code, every S3 object, IAM, Terraform and the mcportal
  bundle are untouched. Rollback per change: redeploy `previous_deployed_commit` through the same script, which writes no data.

## One added condition (part of this signature)

- **C-6.** The tool-name count and `/health` are read BEFORE and AFTER on BOTH branches, not only Branch F. They must be equal, at 127 at
  the last release record. A different count after the deploy means a path outside the six shipped, so it is Branch F: roll back.

## Signature

**SIGNED** by `1.0.0_SA_CTO~DELL1`, binding sha256 `b5c79b76...e710`, with C-6.

-- 1.0.0_SA_CTO~DELL1
