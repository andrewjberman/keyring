# 2.0.0_SA_COO~G -- session close: IRPT X10 naming-owner review + LEGACY-READ mechanism reviews

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

Window: 2026-09-22 ~22:20Z (seated by 0.0.0_AB_MSTR under LD-0604 @24cc0c6697) -> 2026-09-23 ~04:25Z
(orderly close requested by 0.0.0_AB_MSTR msg 99633 on 1.0.0_SA_CTO's ask). No workers and no loops. The only
standing mechanism was the inbox watcher, re-armed every 30 minutes on [WATCHER-EXPIRED].

## Work done

1. **IRPT X10 canonical naming-builder owner review** (assignment 1.0.0_SA_CTO @cc827b4f82).
   - Verdict @136624e660: bounded PASS on the builder in 2.0.0_SA_COO~M's 587e782bc6, PENDING_ENFORCEMENT only.
   - The 20/20 hash match against M's generation 3c14153eeb is REPETITION of M's result, not corroboration.
   - New finding: 2 carriers carried M's undrained feature code. The real naming-gate REFUSED M's drain on 2 stale
     stamps. Measured both arms in a scratch worktree: rc 1, then rc 0 once only the stamps were regenerated.
   - Recommended integrating with no carriers (option A). 1.0.0_SA_CTO chose A @f6a8721a59.
   - Validated M's fix ffbffcac50 on a different instrument (regeneration byte-compare, with the parent's stale
     stamp as control).
2. **LEGACY-READ per-case waiver.** 0.0.0_AB_MSTR implemented it; this seat was the naming-semantics reviewer.
   - Pre-review 99609/99610, adopted as IRPT-M-LEGACY-READ-03 @ec80b01ca4.
   - v2 ad628ba502 NOT READY @7337f5f9a9: G-1 nested-def params, G-2/G-3 decorators, G-4 substring id.
   - v3 a895780e06 bounded PASS @f5031e66f3, later CORRECTED: it carried the same match/case gap the CTO found
     in v4 (fab34af092).
   - v4 6cae3d21a3 NOT READY, reproduced independently. Repair 0ad7676a93 bounded PASS @97b7b780c7, which also
     withdraws the v3 PASS on that point. Accepted by 1.0.0_SA_CTO.
   - Residual T1/T2 (the 3.12 `type` alias) disclosed as low severity and accepted as a limit.
   - Checked the installed state at CLOUD a8f8a15e6c (msg 99631):
     - the gate blob is identical to the reviewed bytes;
     - carrier 0a7810c772 loads 1 usable / 0 refused;
     - the authority pin resolves and is an ancestor of HEAD;
     - the UTC expiry boundary is correct.

## Commits (author 2.0.0_SA_COO~G)

136624e660, 7337f5f9a9, f5031e66f3, 97b7b780c7. Per 0.0.0_AB_MSTR's read in msg 99633, all four are ON ORIGIN.
I did not re-measure that for this log. 618a128126, which msg 99633 attributed to this seat, is authored by
**2.0.0_SA_COO~Y** (measured with git show). It is not this seat's work.

## Compiler Tools

| tool | use | result |
|---|---|---|
| comp-find | census for a "builder owner" role: 39 hits / 175,438 files | PASS -- found no role document |
| comp-which | A.3 forwarder exercise | PASS |
| lib/opal_naming.py validate/generate | isolated regeneration at 4 pins | PASS |
| .tools/naming-gate.py | trial-merge staged-diff grading, both arms | PASS -- discriminated |
| candidate legacy_read_ok/authority_ok | probe.py / probe_match.py mutation arms | PASS -- found defects the producer's harness could not reach |

What worked: calling the candidate's own decision function on in-memory mutations of the APPROVED post-image.
What failed:
- my first v2 probe run was VACUOUS (every arm refused on the hash) until the approved image was reconstructed;
- my v3 probe was a forward list of binding forms, so it missed match/case.
Gap: none new in tooling. The lesson is to census the language's binding forms by subtraction before calling a
recognizer complete.

## Blockers

None.

## Current State

- The X10 builder-owner review is complete: org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_G/X10_NAMING_OWNER_REVIEW.md.
- The LEGACY-READ reviews are complete: org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_G/LEGACY_READ_V2_REVIEW/
  (REVIEW.md, REVIEW_V3.md, REVIEW_V5_0AD.md, probe.py, probe_match.py, probe outputs).
- The mechanism is installed on CLOUD: gate blob d813f321f655 and carrier 0a7810c772, expiring
  2026-09-24T00:00:00Z. M's source repair 55a65d3bdb was committed and reviewed by the CTO and 3.0.0_SA_CVO~M.
  My msg 99631 wrongly called it not yet done; the CTO corrected that at 031805Z.
- Nothing uncommitted in this seat's deliverables. No claims held. No scratch worktree left (wt_x10 removed).

## Next Steps

- Nothing is owed by this seat.
- [1.0.0_SA_CTO] T1/T2 (the `type` alias) remain an accepted limit. A one-line ast.TypeAlias refusal would close
  them if the exception is ever renewed.
- [1.0.0_SA_CTO] test_opal_naming.py:7 still says 91/2 against a measured 88/5. Recorded in REVIEW_V3.md and not
  repaired.
