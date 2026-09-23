# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 40 (2026-09-22 13:41Z)

**Arming record:** `c9ccd9f4e3`. **state:** ARMED.

## Since tick 39

**IRPT_BCKEND**
- **Correction to v0.16.** 3.0.0_SA_CVO~B found that v0.16's claim of "no handler change" was false: the renderer resolves UNKNOWN in `classify_principal`.
- **v0.17 (@`1450e05178`).** This seat corrected it by adding CONTRACTS item 8: the RENDER_DELEGATE branch, scoped to the delegator's current grant intersected with the pinned bundle scope, plus acceptance arms (h)-(k).
- **Sign-off.** L4-R reads ADMITTED:
  - ratified-text half signed by 3.0.0_SA_CVO~B, stamp `4f942b7657`;
  - brief half signed by 4.0.0_SA_CRO, review `e963205de6`.
- **Round 17.** 2.0.0_SA_COO~B cut it at 3 cells (@`86ba92ceb5`).

**IRPT_FNTEND**
- **Round 13.** All 5 of 5 cells are terminal. FE-s-84 was drained at `f7b2fbf769`. The L8 packet was sent at 13:24:35Z.
- **CVO~F down.** 3.0.0_SA_CVO~F's Codex driver died again after the 12:00Z fix. `.runtime/codex-operational-driver/3.0.0_SA_CVO~F/` holds only `driver.*.stale-...-pid21876-dead` files. Reported by 2.0.0_SA_COO~F in msg 99497; this seat forwarded it to 0.0.0_AB_MSTR in msg 99498.
- **CTO ruling (the default under the call routing).** If 3.0.0_SA_CVO~F is not consuming its inbox by 14:15Z, round-13 grading moves to 3.0.0_SA_CVO~B as interim grader. This follows the round-12 precedent and keeps one grader per round.

## Off-scope, handled at the CTO terminal
- **mdpf-gold-lambda.**
  - Rolled back on Andrew's "Go".
  - The 13:30Z fire built 8/16.
  - LEG B was ruled by Andrew: "Leave them, cover in the fix".
  - The fix-forward is held by 0.7.0_AE_CloudOps~V. The CTO's never-widen half is conditioned per msg 99491.
- **Bright Data.** The new API key was put into 3 secrets at Andrew's request.

## Completion test
**NOT DONE.** 0 of 2 projects are complete.

**Push state:** LOCAL on CLOUD. 0.0.0_AB_MSTR pushes.
