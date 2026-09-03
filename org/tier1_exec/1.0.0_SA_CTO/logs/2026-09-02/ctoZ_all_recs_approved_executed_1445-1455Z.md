# CTO~Z delta log -- Andrew "all recs approved": four calls executed

**serial:** 1.0.0_SA_CTO~Z   **window:** 2026-09-02T14:45Z -> 14:55Z   **archetype:** IMPLEMENT (sovereign
rulings executed)   **secondary:** RECORD (verbatim ruling), VALIDATE (fresh-scan + proven-red suite)

## Andrew-direct, VERBATIM AND ENTIRE
> all recs approved
On the /open-calls cards at this seat. Record: deliverables/ANDREW_DIRECT_20260902_ALL_RECS_APPROVED_
OPEN_CALLS_CTOZ.md @98fd4ca0d4. Broadcast 19337-19341 same turn.

## DONE
- **CALL 1** 8 accounts email-MFA via conditional update-item (same act as the 13 and the 9). APPLIED 8 /
  SKIP 0 / ERR 0. Fresh full scan: 48 PROFILE rows, 32 mfaEnabled all email, 8/8 ON, 0 stray; the 16
  still OFF are exactly the excluded set (13 test/demo/fixture, 2 service, 1 disabled).
- **CALL 2** SITEZ into never-rules-gate SHARED_BRANCHES @98fd4ca0d4. 13 of 15 dead rebase arms went
  green on this device; GATE 1 + GATE 5 now fire on SITEZ. The session serial file (XXX.md A.1) is now
  load-bearing for any push from this device; UNRESOLVED fails closed.
- **CALL 3** DT carve-out PROD -> PROD|DEV in the portal repo; /prod-deploy Step 1a gains the
  only-your-own-commits payload check and names GATE 5 for the first time.
- **CALL 4** no caller widening; Andrew-directed non-DT uses the audited never-override; recorded in
  SKILL.md Step 0 and the deny text.
- Suite: 94 PASS / 2 FAIL (was 76/15). PROVEN-RED against the pre-change hook: DT-on-DEV DENY (want
  PASS); SITEZ rebase / push / pull PASS (want DENY).

## Findings surfaced, not chased
- **NEVER#7 evasion on every device:** `git -c pull.rebase=true pull origin CLOUD` (and the
  --no-pager form) render PASS (want DENY) -- GATE 1's -c pull.rebase one-shot matcher does not fire.
  Masked on site Z until SITEZ became shared. To 3.0.0_SA_CVO~Z (19347).
- **Editing a live hook in place is a fabric-wide deploy** -- my python write of never-rules-gate.sh
  crashed every Bash call at 0.0.0_AB_MSTR~Z mid-save (19342). Banked as memory; next hook edit is
  scratch copy + atomic mv. The carve-out condition at 5fb8143d72 also lost its continuation
  backslashes to heredoc mangling (valid bash, one long line; left as-is).

## Compiler Tools
- test_never_rules_gate.sh on new hook (94/2) and NRG_HOOK=old (74/22, proven-red). bash -n on both
  shell files before staging. aws dynamodb scan (pre + post, LastEvaluatedKey absent both) +
  update-item x8. safe-commit x1 (4 files), commit-msg ASCII gate clean.

## Current State
- opal-users-v2: 32/48 email-MFA. Nothing at Andrew on MFA. SMS: G-7, SP-1 gated.
- 98fd4ca0d4 LOCAL at this write; push leg named to 0.0.0_AB_MSTR~Z (19345). Gate is live by reading.
- Zero crons. Watcher ba9ps95uv live.

## Next Steps
- **[0.0.0_AB_MSTR~Z]** push 98fd4ca0d4 + this log.
- **[3.0.0_SA_CVO~Z]** class the -c pull.rebase evasion; disarm the SITEZ ARMED item on landing.
- **[0.4.0_DE_ClientPlatform~Z]** stale-bundle hazard now covers 17 partner users; SF-2 part 2/2.
- **[Andrew]** nothing open at this seat.
