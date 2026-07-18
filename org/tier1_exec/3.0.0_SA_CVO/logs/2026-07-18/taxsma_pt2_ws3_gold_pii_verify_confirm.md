# CVO -- OPAL_TAXSMA_PT2 WS-3 gold dim_taxsma_report: independent SEV1 PII-safety verify
**archetype:** VALIDATE

**Window:** 2026-07-18 ~03:15Z -> 03:25Z (session start). First log this session.
**Serial:** 3.0.0_SA_CVO (Tier-1 exec, independent verification lane).

## Summary
CTO (1.0.0_SA_CTO) pulled me for an out-of-both-lanes (not build=DS, not gate=CTO) independent
PII-safety verify of the WS-3 gold projection `blackdiamond/49f/gold/dim_taxsma_report`, feeding
his WS-4 IAM go-live SEV1 hard-withhold. Verdict: **CONFIRM -- no PII defect; the PII gate is a
real, mutant-exercised control.** CTO ACCEPTED (0323Z) -> WS-4 PII-safety leg CLEARED; WS-4 now
on its final account-scoped IAM leg (CTO lane).

## What I did (exercised, not read-back-trusted -- Rule 22a)
- **APPLIED grounding:** pulled the served parquet; local MD5 = `62f6e22f8f557780137f519c5b31ba84`
  == ETag exactly (single-part => ETag IS MD5). 31900 B, 45 rows x 86 cols. ListObjectsV2 = 1/1
  served partitions (`account=0027265115/date=2026-07-17`). Coverage denominator = 1 of 1 (Chiles-
  only; Bump/Macy declared follow-on).
- **DESIRED grounding:** read gold script at CTO-cited commit `1ba779e0b`; `git diff 1ba779e0b..HEAD`
  for the script = EMPTY (served == HEAD, no drift).
- **EXERCISED grounding:** imported the DEPLOYED functions (select_report_rows/anonymize/pii_gate)
  and ran them against the REAL silver partition (`fact_taxsma_report/date=2026-07-17`, 304 KB).

## Findings (row/col evidence)
1. **Names absent, absent-SHAPED:** COLBY/CHILES = 0 hits in a whole-table cell sweep. The nodes
   that would carry the name are structurally empty -- Account-level `level_name`+`level_key` NULL
   on exactly the 6 Account rows (Counter{'Account':6} both); `account_name` not a column. Proven
   by a content-scan whose 4 needles are the REAL client name harvested from silver (full 14-char
   name + tokens colby/chiles + masked number) -> 0 hits. Confirmed silver Account-level level_name
   IS the client name (contains both tokens) -- CTO's chosen needles are correct.
2. **Forbidden columns absent:** full FORBIDDEN set clear in the 86 cols (account_name, bd_account_id,
   bd_external_id, bd_account_number_masked, descriptor_json, bridge_*, level_filters_json,
   *_weighted_returns_json, source_hierarchy, ...).
3. **Scrub is Account-level-targeted (correct):** retained non-null level_names are public security
   names (Asset) + GICS sector/asset-class labels (Class/Segment) = report content, not PII.
4. **Whitelist posture verified:** an added un-vetted string col carrying the name was DROPPED by
   default-exclude.
5. **Gate is a REAL control (mutant tests on deployed code path vs real silver):** rebuilt gold =
   (45,86) columns IDENTICAL to served + gate NO_PII_PRESENT (reproduces the served build). M1 full
   name -> FIRES; M2 partial token -> FIRES (tokenized); M3 scrub-regression (Account level_name left
   in) -> FIRES (content-scan is the backstop); discrimination control (random string) -> does NOT
   fire. => a control that can fail, not a no-op.

**Not flagged (per CTO ruling):** `schwab_account_id` = real account in its own IAM-scoped file
(benign business key). **2 non-defect observations recorded:** (a) DS's "scrubbed null" phrasing is
Account-targeted not blanket (correct design); (b) the FORBIDDEN post-projection assertion
(anonymize ~L181-183) is structurally unreachable (keep-loop `continue`s on FORBIDDEN first -- why
mutant M4 re-add didn't raise: silently DROPPED, zero leak) -- redundant belt-and-suspenders, NOT a
gap. CTO agreed: leave it, content-scan is the real backstop; any tidy is DS's cosmetic call.

## Compiler Tools
| Tool | Why | Result |
|---|---|---|
| (none) | This was a SEV1 client-data PII verify demanding direct exercise of the SERVED artifact + the DEPLOYED code path. Rule 22a requires EXERCISE (import the functions, run mutants vs real silver) -- a comp-tool models DESIRED/state, not landed-behavior, and cannot mutant-test a gate. Grounding was aws s3 (list/cp = operational), MD5==ETag, pyarrow reads, and importing the actual module. `comp-*` would have answered a weaker question. | N/A |

What worked: MD5==ETag pinned me to the exact served bytes; importing the deployed functions let me
reproduce the served shape AND mutant-test the gate on the real code path. What failed: nothing. Gap:
none.

## Blockers
None.

## Current State
- WS-3 gold `dim_taxsma_report` served artifact (account=0027265115, date=2026-07-17, ETag 62f6e22f)
  is PII-clean and its gate is genuine. Recorded to CTO @ inbox msg 20260718T031715Z; CTO ACCEPT @
  20260718T032313Z. **WS-4 PII-safety leg CLEARED.**
- No repo writes this session (verification only; scratchpad scripts under session temp).
- Prior-session open items unchanged: NFRA_GCONTR 2 SEV1 rows Andrew-signed, LOAD HELD to MDPF
  (0.7.0 loads post-MDPF -> COO closes); F-006 durable-audit-log fix carried open (CTO-class).

## Next Steps
- [1.0.0_SA_CTO] owns the remaining WS-4 leg: the account-scoped per-employee IAM gate (enumeration
  risk lives there, not in gold content). No CVO action pending.
- [3.0.0_SA_CVO] event-driven; no crons armed (LD-0175). Monitor bzgy30lfe live.
