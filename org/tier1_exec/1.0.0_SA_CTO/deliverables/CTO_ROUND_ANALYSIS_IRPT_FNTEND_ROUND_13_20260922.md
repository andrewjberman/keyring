# CTO ROUND ANALYSIS -- IRPT_FNTEND round 13 -- 2026-09-22 ~14:1xZ

**Input:** `3.0.0_SA_CVO~F`'s L10 slug `surprise-channel/remediations/REMEDIATION_v10.md` @`66cf49b513`. The L9 is
`ADJUDICATION_v5`, C-S167..177. The review is `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_FNTEND_ROUND13_L8_L9_20260922.md`.

This is the second of the three L10 acts. `2.0.0_SA_COO~F` cuts round 14 in ONE issuance, and `3.0.0_SA_CVO~F` grades it.

## Coverage read: round 13 closes; FWD-12 stays NOT_REALIZED

**Proofs and suite**
- 5 proofs, 30 criteria, all VALID: 26 mechanical and 4 judgment. 84 of 84 orders are terminal.
- The grader's own suite run reads **648 pass / 27 skip / 2 FAIL**.
- Both failures are committed-output omissions: the sibling fixtures `fe-s-13-wire.json` (0 of 9) and `fe-s-14-print-v1.json` (0 of 2) lack `unprojected_grant`. The generator source landed; its outputs did not.

**Judgment criteria**

| criterion | grade | what it closes |
|---|---|---|
| F82-AC6 | PASS, bounded | W17-S1 and C-S164 |
| F83-AC6 | PASS; the CVO supplied the keyboard exercise | C-S165 |
| F84-AC7 | PASS, bounded | F78-AC7's evidence gap (a scrolled pair now exists) |
| F80-AC6 | **FAIL** | nothing |

F80-AC6 fails because the prefix classifier accepts `holdings/A-0001/not-a-declared-operation`, a trailing operation no template declares.

**OPEN remedies:** W25-S1, C-S147, C-S150, and the new C-S176. **Eight bounded closures are accepted.**

**PRD addendum v0.10 (this seat, the same act).** CONTRACTS gains the print-route render-delegate branch owed to `IRPT_BCKEND` v0.17 item 5; F9 owns it. It is the only outcome no cell served. The ratified-text half re-opens and goes to `3.0.0_SA_CVO~F`. The brief half is unchanged.

## Round 14: ONE issuance (L8/L9 to `3.0.0_SA_CVO~F`)

**W25-S1: commit the generated outputs.**
- Regenerate, then commit `fe-s-13-wire.json` and `fe-s-14-print-v1.json` so they carry `unprojected_grant`.
- The acceptance is read from the GIT OBJECT, not the worktree: `git show <commit>:<path>` counts must be 9/9 and 2/2, and default must stay 12/12.
- The full suite must read 0 fail.

**C-S147 / F80-AC6: full-template classifier.**
- A concrete key is valid only when it matches a declared `consumed.ts` template SEGMENT FOR SEGMENT: same segment count, each literal equal, each `{param}` matching one non-empty segment. No prefix matching.
- Four required controls:
  1. concrete `holdings/A-0001` -> valid;
  2. `holdings/A-0001/not-a-declared-operation` -> INVALID;
  3. a static-only suffix -> invalid;
  4. `status/{jobId}` concrete -> valid (it IS declared, so it is not a negative control).
- The denominator must be printed.

**C-S150: AnswerStatus weights under C1.**
- Ready/Partial goes from 600 to **700**, and the qualifier from 500 to **400**.
- This follows the same rule as this seat's round-11 breadcrumb ruling: emphasis is carried by weight, and the only weights are 400 and 700.
- The acceptance is measured computed weight on the fixture-fed report, together with an absent-selector control.

**C-S176: the common acceptance contract (CTO ruling).**
- Every visual criterion carries its five controls.
- A control that cannot apply is declared NOT APPLICABLE, with its reason, **in the task order at cut time**. It is never waived in the result.
- A result reports two figures separately:
  - **declared-key validity**: the proof's keys parse;
  - **exercised fulfilment**: which controls actually ran, n of N.
- No retroactive N/A.
- The COO's cut applies this to every visual criterion in round 14.

**F9 (v0.10): the print-route render-delegate branch.**
- Acceptance arms: (a) a render-claim token renders the print route from its fixture; (b) the same token on a non-print route is redirected like any non-internal token; (c) human internal and advisor tokens are unchanged on the print route.
- **It rides round 14 only if v0.10 reads ADMITTED when the COO cuts.** Otherwise it rides round 15, and the round is not held for it. LIMB 6 refuses a new order against an unsigned half.
- The `IRPT_BCKEND` IB-rti-6 latency re-cut waits on this branch landing.

## Carried, not cut

- **C-S146:** its closure test is the absent-selector control on the fixed instrument, now exercised in F82/F83/F84; the CVO disposes of it at round-14 L9.
- **S70 `surfaceBase` weight:** PARKED outside IRPT.
- **Older rows:** no bulk close.

**PUSH STATE:** LOCAL on CLOUD. `0.0.0_AB_MSTR` pushes.
