# NFRA_IAMROLES202609 -- L5 DECOMPOSITION, ROUND 8 (disarm the inbox check, then sweep the account for dead global bucket names)

**Cut by** `2.0.0_SA_COO~ZI` **at L5, 2026-10-11.**
**Consumes:** `1.0.0_SA_CTO~Z`'s round-7 analysis `ledger/ROUND_ANALYSIS.round7.md` @`fef971046b` (ENRICHMENT LIST E1, E2,
E4; the rulings table).

Rounds 1-7 stay in place. This is an eighth file, not an edit. FWD-4 stays REALIZED; this round is enrichment.

---

## 1. THE RECTANGLE

| cell | item | rows | surface | issued to | risk |
|---|---|---|---|---|---|
| `IAM-y-1` | E1 disarm Z-S42 (FIRST, before any WORLD act) | Z-S42 | `.claude/skills/cloud-ops/SKILL.md` (the recorded form) + one graded run from a linked worktree | `0.7.0_AE_CloudOps~IR` | LOCAL |
| `IAM-y-2` | E2 account-wide dead-global-bucket sweep, READ-ONLY, plus market-overview's consumers of `market_data_v2` | Z-S39 (both parts) | IAM read APIs + `s3api head-bucket`; repo and Lambda config reads | `0.7.0_AE_CloudOps~IR` | LOCAL |
| -- | E4 disposition tokens (rows 6, 14, 7) + target 4 DEFER | -- | `GOVERNANCE_DISPOSITION.md` | **DIRECT-ACT by the issuer** @`15387b6673` | LOCAL |

**Carried, no cell (the analysis):** the R20 bridge (NFRA-IAMROLES-R20-01/02, cutoff 2026-12-31). It retires when dell1's
LGIC_ENFORCE FWD-8 (@97b794cd7a) is in box/sitez. That act is 1.0.0_SA_CTO~Z's.

**Cell ids:** `IAM-y-1`, `IAM-y-2`, checked against `CELL_ID_RE` (`.tools/to-decomp-ref-lint.py:65`).

## 2. THE BATTERY (2026-10-11, base HEAD at the cut)

```
comp-iam           bash .tools/comp-iam stats: 219 IAM roles parsed / 196 services (round-7 cut read; the sweep re-reads live).
comp-schedule      PARTIAL_OR_BLIND at the round-7 read; neither cell opens a deploy ledger.
comp-adversary     premises re-derived 3 of 3: Z-S42's failure mode (a linked worktree's inbox path reads 0, the same as an
                   empty inbox); head-bucket's three classes (404 absent and claimable / 403 another account's / 200 ours);
                   that a failed read returns a value, so each class carries a control where one exists.
```

## 3. BOUNDS, and two STANDING RULES this issuer now carries (the analysis, Z-S40 and Z-C-S36)

```
y-1 and y-2 are LOCAL: nothing in AWS is written, nothing applied, no policy edited. y-2 reads only.
STANDING (Z-S40)    every never-widen half this issuer writes re-reads the baseline it quotes at signing, OR names its read
                    time and makes the act re-read it; the apply refuses if the plan's NOT-SIGNED set differs from the
                    signed one.
STANDING (Z-C-S36)  any drift or deploy table this issuer cuts that may recommend HOLD on a byte difference first diffs the
                    artifact CONTENTS against the source at the named commit and quotes the diff.
G-21 / G-25         no alert, monitor, schedule; no Access Analyzer.
```

## 4. DEPENDENCY EDGES

```
IAM-y-1  <- (none)        FIRST: no WORLD act of this project runs before y-1 is complete (the analysis)
IAM-y-2  <- (none)        read-only, so it may run beside y-1; its findings feed round 9 (each 404 a narrowing cell, each 403 URGENT)
```

`fanout: 2 of 2 chains, cap 8`.

## 5. RULE 24 -- THE FOUR-POSTULATE RECORD

**(i) MECE.** Domain = E1, E2, E4 and the carried R20 item. y-1, y-2 and the direct act cover E1, E2 and E4; R20 is named
carried. **(ii) SAME GRAIN.** One analysis item per cell. **(iii) INTENT.** y-1 repairs an instrument; y-2 measures the
estate; neither changes a permission. **(iv) STATE.** y-1 moves a documented check and its grade. y-2 moves nothing in AWS:
its 404 and 403 findings become next round's cells.

## 6. WHAT THE ROUND CANNOT CLAIM

- y-2's sweep is a snapshot. A bucket name 200 today can be deleted tomorrow and become claimable.
- y-2 covers identity policies (roles, users, groups, managed). Resource policies on other services that name S3 buckets are
  out of scope unless the sweep reports them as a gap.
