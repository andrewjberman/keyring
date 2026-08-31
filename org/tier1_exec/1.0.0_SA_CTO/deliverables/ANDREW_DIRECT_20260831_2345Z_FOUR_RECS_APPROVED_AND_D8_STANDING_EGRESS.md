# ANDREW-DIRECT 2026-08-31 ~23:4xZ -- all four /open-calls recs APPROVED + D8 standing vendor egress

**Seat:** 1.0.0_SA_CTO (Andrew at this terminal, FIRST-HAND)
**Recorded:** same turn as receipt, per `org/XXX.md`
**Channel:** Claude Code terminal, session `1.0.0_SA_CTO`, registered LIVE PID 93716

## VERBATIM

> all recs are approved but one comment, all agents on this session working on the D8 issue have
> standing egress for vendor calls to validate. I want to validate now, i do not want to wait, all
> testing is allowe.d

Context: this answers the `/open-calls` card set issued at 23:42Z, four cards, each carrying a REC.

## WHAT IS APPROVED -- EACH CARD, ITS REC, AND WHAT IT UNLOCKS

**CALL 1 -- APPROVED (REC was YES).** Release the **2026-08-19 `DEPLOY-SERVE-HELD` hold** on
`perfrp_emit_core.py`, `perfrp_rollup.py`, `perfrp_transactions.py`.
- UNLOCKS: sentinel removal under a `SERVE-RELEASE-ACK: <reason>` authorizing commit, then completion
  of the `advi:gold _code/` sync (3 of 6 rows still STALE).
- The mechanism: `.tools/safe_deploy_core.py` `SERVE_HELD_RE` refuses while the sentinel is present;
  removing it IS the authorizing act and is gated behind the ACK. Both regexes FAIL CLOSED and the
  `[ \t]*`-not-`\s*` form is load-bearing -- **nobody may loosen either.**

**CALL 2 -- APPROVED (REC was YES, on the CORRECTED understanding).** Authorize **serving the
canonical perfrp key**.
- ⛔ **APPROVED ON THE CORRECTED FRAME, NOT MY FIRST ONE.** I initially put this as a "DEV-scoped
  serve." `0.7.0_AE_CloudOps~G` measured that **no DEV serving plane exists** -- `SERVE_BUCKET` /
  `SERVE_ROOT` are module-level constants with no env dimension, and there is exactly **1 CloudFront
  distribution in the estate** (1 hit / 11,329 files, complete census). I corrected the card to Andrew
  BEFORE he answered, and this is the frame he approved:
  > *Authorize serving the canonical perfrp key -- accepting that it becomes authenticated-fetchable
  > estate-wide while remaining unrendered on PROD?*
- UNLOCKS: the **P4I-3 publish activation**. The **2026-08-21 49F-flip hold is DISCHARGED** for this act.
- **THE ACCEPTED RESIDUAL, in his hands when he answered:** serving the key makes it fetchable by an
  **authenticated principal** through that one distribution. *"PROD users cannot see the panels"* is
  true of the RENDERED UI and is NOT the same claim as *"the data is not exposed."* PROD carries no
  perfrp fetchers in source (`origin/PROD` advisor-intelligence.ts, 1,564 lines read, ZERO perfrp
  matches), so no PROD bundle renders them.
- ⛔ **NOT APPROVED, AND NOBODY ASKED FOR IT: the PROD portal promote.** That is a separate act on a
  separate branch. PROD UI exposure remains gated by it.
- ⚠ UNMEASURED AND CARRIED: the PROD claim is about `origin/PROD` SOURCE, not DEPLOYED BYTES. A stale
  deployed bundle reads identical. If PROD exposure becomes load-bearing, read the deployed artifact.

**CALL 3 -- APPROVED (REC was DIAGNOSE FIRST, no blind re-fire) AND THEN MODIFIED BY THE COMMENT.**
The comment grants standing egress to validate and says he does not want to wait. So: diagnosis of the
`Core | Satellite 60` 15-vs-14 discrepancy MAY now spend vendor calls, and testing is permitted.
**What does NOT change: no blind re-fire.** The approved rec is diagnose-first; the comment removes the
egress constraint on diagnosis, it does not convert "diagnose" into "re-fire and see."

**CALL 4 -- APPROVED (REC was WAIT for W2).** The three-account BD spot check waits on the 00:00Z mint.
⚠ **TENSION SURFACED, NOT ADJUDICATED:** "I want to validate now, i do not want to wait" sits against
CALL 4's approved WAIT. **His comment scopes itself to "the D8 issue"; CALL 4 is ADVI_BDPARITY under
D2.** I am therefore reading the standing grant as D8-scoped and CALL 4 as approved-to-wait -- and
asking rather than widening, because W2 fires at 00:00Z and the wait costs ~15 minutes.

## ⛔ THE STANDING EGRESS GRANT -- SCOPE, VERBATIM-BOUNDED

> "all agents on this session working on the D8 issue have standing egress for vendor calls to
> validate ... all testing is allowe.d"

```
  WHO      agents on THIS SESSION working on THE D8 ISSUE
  WHAT     standing egress for vendor calls
  PURPOSE  TO VALIDATE / testing
```
**This is a STANDING grant, which is a departure from the per-use word CLAUDE.md otherwise requires.
It is his to give and he gave it. Its BOUNDS are the three rows above and no wider:**
- It is scoped to **D8** (`AUTH_SELFHEAL` / `MDPF_HEALGAP` / the cot rebalancer auth surface). It is
  **NOT** a general vendor-egress grant, and it does **NOT** cover D2 / `ADVI_BDPARITY` / the 49F
  reporting pull.
- It is for **VALIDATION AND TESTING**. It is not authorization for production writes that are not
  part of validating, nor for backfills, nor for other dates.
- ⛔ **A seat not working the D8 issue has no grant. A seat working D8 has no grant for a non-D8 call.**
- The `AUTH_SELFHEAL` scope already includes the ad hoc rerun (LD-0492 A2); this grant lets that work
  proceed on validation without returning for a per-use word each time.

## WHAT THIS RECORD DOES NOT DO

It does not lift the PROD portal promote, does not authorize a backfill or any date other than those
already named, does not widen the grant beyond D8, and does not close any face. Two long-standing
holds ARE discharged by CALLs 1 and 2 and every seat must stop reporting them as STANDING.
