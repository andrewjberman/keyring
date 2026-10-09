# Post-reboot re-seat; two slugs, a never-widen half and three L4-R signs -- 3.0.0_SA_CVO~Z (site Z)

**archetype:** VALIDATE
**Date:** 2026-10-09
**Task Order:** ad-hoc (L8/L9 compile, L4-R, never-widen half)
**Status:** COMPLETE (seat IDLE, event-driven)

---

## Objective

Re-seat after the site Z reboot: run /watcher and the org/XXX.md startup, then work the four messages queued before the
reboot and the asks that arrived during the session.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| round-close-check.py | `--project NFRA_REPORT --round 4`; `--project NFRA_MCPMSP --round 2` | PASS | both MAY-CLOSE; MCPMSP after C-S5 graded AC5 |
| comp-surprise | `--project <CODE> --armed --json` | PASS | NFRA_REPORT ARMED 8 -> 0; NFRA_MCPMSP OPEN 13 -> 0 |
| comp-surprise (text mode) | `--project NFRA_REPORT --armed` | FAIL | UnicodeEncodeError (cp1252) on a row's non-ASCII; use `--json` with `PYTHONIOENCODING=utf-8` |
| surprise-row-gate (via safe-commit) | 4 attempts on the NFRA_REPORT slug | PASS | refused a missing `closure`, 7 GRADUATED items without rows, and a CARRIED_BY pointer that was not a path; each refusal was correct |
| prd-signoff.py | `sign` x2, `status` x3 | PASS | the first NFRA_REPORT stamp commit failed once (rc=1, shared-index race); the retry landed |
| comp-which | `"list open ARMED surprise rows..."` | WARN | no curated rule; found `comp-surprise` by listing `.tools` |

**What worked:** the row gate's refusals named exactly which rows the slug owed.
**What failed:** comp-surprise's text mode on cp1252.
**Gap found:** comp-which does not route surprise-channel census questions to comp-surprise.

## Work Completed

1. **Startup.** Registered; watcher armed (script pid 4620, then re-armed on each expiry); acked 32437, 32440, 32446
   and 32458. Delivery ledger since 10-08: 50 of 50 READ. The session-serial file was written. No CVO~Z log or commit
   after 04:22Z, so no work was lost to the reboot. No cron armed (launch order: zero crons; the July SYSPARITY row in
   LIVE_ARMS was not re-armed).
2. **NFRA_REPORT round 4 slug** @95d711f592 (`REMEDIATION_v4.Z.md`, 16 rows): 8 ARMED rows disarmed on rulings
   already filed. I re-read the live Lambda (CodeSha256 `iU6tKUas...`, 2026-09-17T14:54:07Z). Z-S26 is OPEN with
   `2.0.0_SA_COO~C`. Slug sent to `1.0.0_SA_CTO~Z`. The CTO answered with PRD v0.9 (FWD-13/15 retired, enrichment
   list empty). I signed it at 1ebbf7ecdf (review d4a0ae2121), so the project closes.
3. **NFRA_MCPINDEX v0.8** ratified-text half SIGNED, review @4e919a5c3c. FWD-19's fixture fields equal the ACCEPT
   lists. Three carried notes: post model update rec is `unowned` with no reason; the FA items' read half is not an
   alert; the brief half's status reads auto while the addendum says owed.
4. **NFRA_OPLGTW r29 CVO half** @c348b51df9: 4 exact domains, a second mail-bearer holder signed as a named widening,
   Alyssa at 13 months. The send to `2.0.0_SA_COO~O` was refused by the L8 guard, so I sent one ask to
   `1.0.0_SA_CTO~O`: addend C7 :694 for two holders and relay the half.
5. **NFRA_MCPMSP round 2** @126e355873: ADJUDICATION_v2.Z (10 dismissed, 3 graduated, and the MS-dn-1 AC5 grade:
   PASS, with a live under-Deny read through `mdpf_get_aum_metrics`) plus REMEDIATION_v2.Z. Slug sent to
   `1.0.0_SA_CTO~Z`.

## Current State

Push state: origin box/sitez at 1ebbf7ecdf (ls-remote read 08:1xZ), which contains every commit above. The seat is
IDLE.

## Next Steps

1. [1.0.0_SA_CTO~Z] Round-2 analysis for NFRA_MCPMSP (G-MSPID is Andrew's).
2. [1.0.0_SA_CTO~O] C7 addendum for the second holder; relay the r29 half to `2.0.0_SA_COO~O`. The window opens
   11:00Z.
3. [2.0.0_SA_COO~C] Z-S26 / NFRA_MCPMSP-Z-S4: round-close-check's id fallback.
