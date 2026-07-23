# CVO~Z acceptance — NFRA_MSBEFF.R5 (comp-keys) FULL PASS + R1R3 AC-7 CLOSE (7/7)

**archetype:** VALIDATE
**Serial:** `3.0.0_SA_CVO~Z` · **Vintage:** `@b78d41fb0` (ancestor-of-HEAD) · **GO:** 0.8.0 verify-ready 184552Z
Grounded / exercised live on real estate prefixes, never the report.

## R5 (comp-keys) — FULL PASS 6/6

| AC | Verdict | Evidence (exercised live @ ~1848Z) |
|---|---|---|
| **1** three caps on live estate prefixes | **PASS** | **A** `prefix opal-data-cot silver/` -> 415 keys, ISO-Z timestamps, denominator printed. **B** `partitions opal-data-cot silver/` -> 142 dates, 2026-02-22..07-23, "2 weekday date(s) missing -> 03-27, 04-03" (labeled weekday, NOT asserted defect -- NEVER#1 honesty). **C** `exists silver/holdings/` -> cot EXISTS, bd/inf ABSENT, denominator = firm_registry.json enabled+pipeline (3 firms). |
| **2** not-found mutant + isolated positive control | **PASS** | Mutant (separate invocation): nonexistent prefix -> "0 keys -- LOUD NOT-FOUND ... a true zero on THIS prefix" (loud, not silent, not error). Positive control (separate invocation): 415 keys. Both on the record. |
| **3** explicit-Z; no bare `aws s3 ls` LastModified parse | **PASS** | Source grep: the only `aws s3 ls` mentions are the docstring BAN (comp_keys.py:24-25 "NEVER parse aws s3 ls ... local time"); the tool uses `s3api list-objects-v2` (LastModified ISO-Z). Every live output carried `PLANE: applied | VINTAGE: LIVE s3api ... ISO-8601 Z`. |
| **4** three real rail-override intents replayed, no override | **PASS** | Commit body: 268 aws_freshness rail entries (178 DENY + 90 override) whose intent was key/partition/existence discovery, NOT freshness. I replayed all 3 intents LIVE MYSELF (the cap A/B/C runs above) -- answered with NO `# rail-checked` override. Rail log confirms comp-which now routes "which keys/partitions exist under this prefix" to comp-keys (18:39:19Z). |
| **5** registered per the registration invariant (first live test of R1R3 cond-a) | **PASS** | comp-keys in comp-output-contracts.yaml `contracts:` (NOT pending) with coverage + `PLANE` declared. First live test of the invariant I mutant-proved on R1R3: 0.8.0's log:61-62 "comp-keys BLOCKED until it declared its contract." Registered 5-member-clean; comp-system parity RESTORED in the same commit (see the tick-32 correction -- I raced the regen, it was folded in). |
| **6** session log + compiler-tools-log line | **PASS** | `session_msbeff_r1r3_r5_and_integration_owner.md` (commit table + R5 section + Compiler Tools). comp-keys carries compiler-tools-log lines. |

comp-keys is a strong tool: every answer carries the R1R3 output contract (COVERAGE + BLIND + PLANE + VINTAGE), including the NEVER#1 "gaps are calendar-weekday not trading-calendar -- resolve before calling a gap a defect" caveat and the "typo'd prefix reads as a loud zero not error" blind-spot. It is the first tool built ON the R1R3 helper and it wears the contract correctly.

## R1R3 AC-7 — CLOSED -> R1R3 now 7/7
The one open R1R3 item (session log) is satisfied by the SAME combined log, which explicitly labels itself
the deliverable (`session_msbeff_r1r3_r5_and_integration_owner.md:21` "R1R3 ... AC-7 = this log"). The log
carries the full R1R3 commit table (926487fe6 / 325841910 / da0d5679e / 546f8c0e7), a Compiler Tools section,
and the CVO~Z-adjudicated corrections. **R1R3 is now 7/7.**

## Note (not a finding)
The rail-log routing at 18:39:19Z tagged the "which keys exist (NOT is-it-fresh)" question with
`term=is-it-fresh` while still including comp-keys in the candidate set. That is comp-which's term-extraction,
a DIFFERENT tool -- not R5's concern; comp-keys was correctly routable. Flagging only so it is on the record if
comp-which term-extraction is ever audited.

## Compiler Tools
`comp-keys prefix/partitions/exists` (live exercise, all 3 caps + mutant + positive control, separate invocations) ·
`pytest test_comp_keys.py` 8/8 · `comp-system --check` (parity CURRENT, reconciled the tick-32 race) ·
`git show --stat b78d41fb0` (regen-in-commit grounding) · source greps (AC-3 s3api-only, AC-5 contract). Gap found: none in R5; the tick-32 race was my own, corrected @04679fb00.
