# NFRA_TRNSPT decomposition -- ROUND 18 (2026-10-09, issuer 2.0.0_SA_COO~T2, dell2, box/dell2)

Cut on `1.0.0_SA_CTO~DELL2` msg 2894, `CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_12_20261008.md` ADDENDUM 6 @7558d41da5: "round 18 is a COVERAGE
round" -- TR-g-18 (one evidence row per ungraded FWD), FWD-8 (the second named reader's principal via name(), under a pair, routed via MSTR if
laptop IAM), FWD-2 (the Research Meeting read from the scheduled run). FWD-10/11 moved to IRPT_ANLREQ: no cell here.

| cell | item | outcome | placement | risk | worker_class | depends on |
|---|---|---|---|---|---|---|
| `TR-g-18` | one evidence row per ungraded FWD (1-6, 8, 9): the on-demand act, its invocation and its read, or the missing hop; `R18_COVERAGE.md` | FWD-1..6, 8, 9 | dell2 worker (read-only) | LOCAL | worker | -- |
| `TR-p-18` | FWD-8: the second named reader's AWS principal, minted by `lib/opal_naming.py name()`, added to the transcripts key's named readers; DESIRED Terraform | FWD-8 | dell2 worker | WORLD | worker | -- |
| `TR-a-18` | FWD-8 apply: the pair on TR-p-18's bytes, then the apply by the laptop (IAM identity) routed through MSTR | FWD-8 | ISSUER (served) | WORLD | -- | TR-p-18 |
| `TR-s-18` | FWD-2: the latest Research Meeting read as arrived by the ORDINARY scheduled Teams pull (the schedule read by name; the run's own record, not a seat-started run) | FWD-2 | ISSUER (read-only) | SERVED | -- | -- |

**Chains.** A = TR-g-18 (worker slot ~1); B = TR-p-18 -> TR-a-18 (worker slot ~2, then issuer). TR-s-18 is the issuer's read. Fan-out 2 of 2
worker chains, cap 8.

**Issuer rulings.**
1. **The second named reader** is Andrew's second account, `opalbloomberg@opalinvest.com`
   (`ANDREW_DIRECT_20260929_19xxZ_TRANSCRIPTS_LAYOUT_APPROVED_PRIVATE_TWO_ACCOUNTS.md`); FWD-8's amended text calls it "the terminal seat's account".
   Today `reader_principal_arns` holds only `user/Andrew_Berman` (`infra/aws/terraform/transcripts/main.tf:57-60`).
2. **An IAM user `Opal_Terminal` already exists** (issuer read 08:2xZ: 9 users, 291 roles; also `opal-bloomberg-tunnel-instance-role`). Its name is
   typed, not builder output, and nothing in the record maps it to the named account. Per ADDENDUM 6 the principal is MINTED via `name()`; whether
   `Opal_Terminal` is the same reader is asked of the CTO as a row, never assumed.
3. **TR-g-18 names, it does not run, served acts:** a row whose act needs AWS or a person names the invocation and the read; the issuer or the CTO
   runs it when grading.

## Rule 24 record

Domain: ADDENDUM 6's three items. (1) = TR-g-18; (2) FWD-8 = TR-p-18 + TR-a-18; (2) FWD-2 = TR-s-18. Remainder: none (FWD-10/11 named as MOVED).

## Battery

Checks `org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_TRNSPT_T2/R18_CHECKS/r18_checks.py` at base box/dell2 c2d3f143d3: g18 FAIL (absent), p18
FAIL (absent).
