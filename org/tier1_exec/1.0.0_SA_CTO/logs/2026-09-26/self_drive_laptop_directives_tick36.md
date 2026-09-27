# SELF-DRIVE laptop directives -- ticks 35-36 (2026-09-27 ~05:47Z and ~06:17Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`
@`ce6aa15a17`. **Covers:** the ticks since the ticks 33-34 log (@`9fbbc83ef0`, ~05:18Z). **State: ARMED.**

## Scope

9 laptop directives of 15 live. IRPT first: IRPT_BCKEND and DSGN_IRPTV1, both active / EXECUTING. Unread at the tick: 0.

## Acts (1.0.0_SA_CTO lane)

1. **Window 9** (~D's read-only round-7 walk; ~P 101813, blob `6dd81fbf`): CTO half SIGNED @`6e774db803`.
   - Named: the walk records the COT retained report's start.
   - CRO half @`3cc285b2a7`: the byte-proof of the local build (HEAD, porcelain, 0 `/__mockcot/`).
   - Principal created 05:37:40Z; window CLOSED @`eade2ba0f5`. The COT reopen face read 01-02, as W9-2 stated.
2. **COT retained face:** RPT-b683f188 states 01-02..09-22 over a 07-21..09-22 series. The CTO asked for a row; ~P filed
   IRPT_BCKEND-S157 @`52f078fe1e`.
3. **Window 10** (K8, the FIRST real export; ~P 101823, blob `a15c2ffb`): CTO half SIGNED @`4392c7ab8f`.
   - Named: the download response BODY stays out of the HAR, and the PDF is never committed.
   - CRO half @`5e2f9b7ad4`: no new *.pdf/*.png/*.har from window 10 in `git ls-files`.
4. **DSGN_IRPTV1-S19** (CRO @`0b69c1cf16`, ARMED, disarm owner ~D): 34 walk screenshots with real client data are
   committed in three `.shots` folders. 28 are on origin/CLOUD (prod-uiwalk 20, prod-walk 8) and 6 are local
   (w9-round7); this seat measured both.
   - ~D untracks the folders and adds an ignore rule.
   - The history purge is put to Andrew as a card (CARRIED; REC: keep history, untrack + ignore now).
5. **Served since the last log (read, not this seat's acts):**
   - resident `fe64236bbb-wf`, the WAF refresh (CTO 101792 (c)), live 05:54:14Z (@`85b4dedb9e`);
   - adapter `bOefL9nx` (COT actual_start), closed @`19355a8141`.
6. **Watcher** re-armed on each expiry.

## Open calls in scope

One, CARRIED at Andrew:
- **The call:** purge the 34 client-data screenshots from git history (a force push of CLOUD, a destructive git act),
  or keep history and untrack going forward.
- **REC:** keep history for now; untrack + ignore (under way at ~D); purge in a planned quiet window if repo access
  ever widens.

## Completion test

NOT DONE: 0 of 2 IRPT projects complete. D10 is UNMEASURABLE (no members).

## Waiting on other seats

| seat | owes |
|---|---|
| ~P / ~D | window 10: K7 + ONE export to READY (or a named NOT_READY), the token ParameterNotFound, the audit |
| ~D | S19 untrack + ignore; IV-e-50; the round-7 L8 packet to 3.0.0_SA_CVO; the round 7 push |
| ~M | Monday 09-28: R1, then the COT cash-line act (S155 alone) |
| 3.0.0_SA_CVO | round 7 L9 grades (on window 9's walk); the round-5 slug |

## Compiler Tools

`git hash-object` against `git rev-parse <pin>:<path>` (6dd81fbf, a15c2ffb, 4b68468e, 32c85e40); `git ls-files` and
`git ls-tree -r origin/CLOUD` over `*.shots/` (counts per folder).

state: ARMED
