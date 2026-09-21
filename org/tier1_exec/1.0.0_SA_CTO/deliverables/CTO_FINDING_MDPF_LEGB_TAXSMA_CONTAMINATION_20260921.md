# CTO FINDING -- 2026-09-21 ~19:5xZ: a raw CLOUD push would ship unrelated, unreviewed MDPF_TAXSMA code via LEG B

**Context:** Andrew asked for a CLOUD push (SITEZ integration reason); `0.0.0_AB_MSTR` caught that the push's
safe-deploy sync would also move 4 unsigned Cottonwood MDPF files (msg 99187); Andrew ruled "sign first, then push"
(record `@1ab93ec740`) and named that the sign-off must cover the EC2 `mdpf-daily-runner`'s S3 script sync (LEG B)
alongside the Lambda pin (LEG A). `4.0.0_SA_CRO` then asked whether CLOUD HEAD's four files are byte-identical to
what the reviewed hotfix branch carries (msg 99203, item 1) -- this record answers that question.

## MEASUREMENT

`git diff hotfix/mdpf-cottonwood-autocustom-20260921-cto:<path> HEAD:<path>` for all four LEG-B files:

| File | CLOUD HEAD vs reviewed hotfix branch |
|---|---|
| `data/assets/scripts/gold/build_cottonwood_mdpf_pair.py` | byte-identical |
| `data/assets/scripts/gold/build_cottonwood_mdpf_slice.py` | byte-identical |
| `data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py` | byte-identical |
| `data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py` | **DIFFERS -- +~270 lines** |

## WHAT THE DIFFERENCE IS

CLOUD HEAD's copy of `dim_mdpf_aggregate_aua_timeseries.py` carries a complete, unrelated feature: the
MDPF_TAXSMA project's TX-a-1 Tax-member additive overlay (`org/missions/D8/MDPF/MDPF_TAXSMA` decomp s.3,
`org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` v0.5.0). New imports (`hashlib`, `mdpf_category_registry`,
`taxsma_assets`) and five new functions (`tax_coverage_entry`, `tax_additive_overlay`, `tax_additive_for_global`,
`apply_tax_to_global`, `tax_arithmetic_control`). This is a DIFFERENT D9 member project's work, landed on CLOUD
independent of and concurrent with this seat's Phase A/B Cottonwood commits -- explains CRO's separate observation
that this file "was re-served TODAY at 08:55Z" (a different, unrelated write).

## WHY IT MATTERS

- **LEG A (the Lambda) is unaffected.** `0.7.0_AE_CloudOps~V`'s build reads bytes via `git show <pin>:<path>`
  against the isolated hotfix branch, never CLOUD HEAD -- the Tax-overlay code cannot reach that package regardless
  of CLOUD's state.
- **LEG B (a raw `git push` triggering safe-deploy's sync) is NOT safe as currently scoped.** It ships CLOUD HEAD's
  actual bytes, which for this one file means the Tax overlay rides along -- code this seat has not reviewed, that
  is no part of Call 1/Call 2, and whose own readiness-to-ship is unknown here.

## DISPOSITION

This seat cannot sign LEG B against a raw CLOUD push while this holds. Two paths, not adjudicated here (not this
seat's call alone): (a) LEG B ships via a scoped sync of the reviewed hotfix-branch bytes for exactly these 4
files, mirroring LEG A's own isolation, never a full push; or (b) the Tax-overlay work gets its own review/sign-off
so a plain push is safe on this file too. Andrew's "sign first, then push" is exactly the mechanism that caught
this before it shipped by accident, not after.

Broadcast same-turn to `0.0.0_AB_MSTR`, `4.0.0_SA_CRO`, `0.7.0_AE_CloudOps~V` (msgs 99209/99210/99211).

**PUSH STATE:** LOCAL on CLOUD; `origin/CLOUD` `d32d3ad8b8` per `ls-remote` read this write; only `0.0.0_AB_MSTR`
pushes.
