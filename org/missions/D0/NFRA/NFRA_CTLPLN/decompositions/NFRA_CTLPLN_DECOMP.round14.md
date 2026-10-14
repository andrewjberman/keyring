# NFRA_CTLPLN decomposition -- round 14: the round-13 batch repair, the commit path's project derivation, the calendar-copy measure, the census freshness check, the act-row rule (issuer 2.0.0_SA_COO~C; cut 2026-10-14)

**Status: ISSUED in one issuance. FROZEN at the cut.**

**Input.** `ledger/ROUND_ANALYSIS.round13.md` (1.0.0_SA_CTO, @7d271cb57b) section 3 (rulings) and section 4 (the ENRICHMENT LIST), plus ADDENDUM 1 @ad8da57abc (`D2-S3`, from the CVO's L10 slug `REMEDIATION_v7.md` @0acc4f9c86); the issuer's `deliverables/2.0.0_SA_COO~C/ROUND13_INPUTS_FOR_ROUND_ANALYSIS.md` and `L8_PACKET_ROUND13.md`. **PRD:** unchanged. **Standing:** Andrew ~18:4xZ, the laptop drives CTLPLN at normal pace.

## Cells

| cell | what | serves | risk | workstream / round | issued to |
|---|---|---|---|---|---|
| `CT-ad-1` | ONE batch repair (worker-light): `W87-S2` (the `routes.tf` comments that name the deleted simulator); `W89-S2` (the fence check's docstring premises); `W91-S2` (`coverage-frame` prints as `NOTE:`, not `VIOLATION:`); `W8-S7` (`dell_fence_census.py --live` refuses without an explicit `--out`). Three criteria. | FWD-2, FWD-5 | WORLD (path floor; no AWS call, comment text only) | BATCH / 2 | `0.9.0_WK_NFRA_CTLPLN~92` |
| `CT-ad-2` | the safe-commit derivation (row `NFRA_MCPINDEX-Z-W34-S8`, CTO ruling 1): pass the FULL staged path set to the naming gate for committing-project DERIVATION only; grading stays on the eight extensions; five negative controls. | FWD-2 | LOCAL (the commit path every seat uses; negative controls are the acceptance) | COMMITPATH / 1 | `0.9.0_WK_NFRA_CTLPLN~93` |
| `CT-ad-3` | the calendar-copy measure (row `W12-S1`, ruling 3): which Lambda-vendored `trading_calendar.py` copies exist and whether their 2026-2027 holiday sets differ from the library's; read-only, no copy edited; deploy cells only if a set differs. | FWD-2 | LOCAL | CALENDAR / 1 | `0.9.0_WK_NFRA_CTLPLN~94` |
| `CT-ad-4` | `derive_reached_roles.py --check-fresh` bounded and resumable (`--budget`, `--checkpoint`; ruling 4); tested only with an injected fake, no AWS. | FWD-2, FWD-10 | WORLD (path floor; injected fake only, no AWS call) | CENSUS / 1 | `0.9.0_WK_NFRA_CTLPLN~95` |
| `CT-ad-5` | the act-row rule (row `D2-S3`, ADDENDUM 1): in `crossbox-deploy-check.py` a `kind` `act` row matches only the roots its own `roots` field names; seven arms; the issuer reads the real `f61b` row against `irpt-status` after the merge. | FWD-2, FWD-5 | LOCAL | CROSSBOX / 1 | `0.9.0_WK_NFRA_CTLPLN~96` |

## WITHHELD, with the reason and the owner

- **`W89-S3`** (the lgic firm-bucket fence `s3-lgic-firm-buckets.tf` never appends `fence_scoped_allow_statements`; inflection carries 0 of 4, cottonwood 0 of 2). The CTO listed it in the batch with the note "coordinated with ADVI_FIRMBKTS M02". NOT cut, on the issuer's reading: a source edit to a shared-infra file rides ANY later apply of that root, and the edit widens a live bucket policy (an Allow on `opal-data-inflection`, whose single writer is M02 per the CTO's 2026-10-14 ~19:5xZ trade-form ruling, and on cottonwood's). That is a never-widen act with a COO half and a CTO half and a sequencing with M02, not a LOCAL batch edit. The issuer asks the CTO for the route (one ask, message to `1.0.0_SA_CTO`); the cell is cut as its own order after the answer.
- **`Z-S8`**: owned by `1.0.0_SA_CTO~Z` (CTO addendum), the capture belongs in `.tools/spawn-agent.ps1`; not this issuance.

## Carried with an OWNER and the CONDITION that un-parks each

- **FWD-11:** a qualified wait on Andrew's word (open call `laptop-20261014T205216Z-7841`); the restart is cut FRESH in the round after he names the hour.
- **FWD-9:** PARKED. **FWD-27:** the laptop local account waits on Andrew's "another time".
- **`S9118` / `S9117`:** the CVO reads at its next pass whether `CT-ac-2` closed the remaining half for `kill-maint.ps1`; if not, one cell next round.
- **`S9119`:** read when a dell2 lane is live (owner `0.0.0_AB_MSTR~DELL2`). **`S9103`:** the kit provider mirror, no cell. **`S9120`, `S9122`:** per the CVO. **`Z-S3`:** regenerate before 2028, carried.

## Rule 24

**Domain:** the CTO's round-13 section 4 items 1-5 and ADDENDUM 1. Every item is a cell above, withheld with an owner, or carried with a condition. **Same grain; one intent per cell; disjoint write surfaces:** `CT-ad-1` writes `routes.tf`, the fence check, the census tool and `proof-of-spec-check.py`; `CT-ad-2` writes `safe-commit.sh` and `naming-gate.py`; `CT-ad-3` writes a new measure tool and one record; `CT-ad-4` writes `derive_reached_roles.py` and its new test; `CT-ad-5` writes `crossbox-deploy-check.py` and its new test. **State coherence:** no cell applies anything and none makes an AWS call; the one Terraform edit is comment text.

## Dependency chains and fan-out

Five chains, no dependency among them. `fanout: 5 of 5 chains, cap 8, reason: five laptop worker cells with disjoint write sets and no shared dependency`

## Amendment 1 (2026-10-14 ~22:1xZ, issuer 2.0.0_SA_COO~C; gate limb: none graded this modification, no cell and no criterion changed)

`W89-S3` is ROUTED by the CTO (msg 109260, reply to the issuer's withhold) to `ADVI_FIRMBKTS` (dell1): appending `fence_scoped_allow_statements` on the lgic firm buckets rides the same never-widen apply as the trade-form exemptions (`org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261014_195xZ_TCKT_TRADE_FORM_FIRM_BUCKET_ACCESS_ROUTE.md`), because the scoped rows need their matching Allow statements or the ticket API stays refused on inflection and cottonwood. It is not a CTLPLN cell; the CTO reads the row as routed. Nothing else in this document changes.
