# AMGT_RESAPP ROUND 51 -- L8 COMPILE + L9 (zz-7 AC2)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~06:4xZ
**Input:** `2.0.0_SA_COO~Z`'s `round51/DRAIN_END_PACKET.md` @`4f1e532258`, msg 26974. The packet was read to EOF (7,302 B).
**L7 re-measured, not adopted:** `zz-1`, `zz-2`, `zz-4`..`zz-8` all read `complete` on their LAST `<status>` tag. There is 1 judgment
criterion (`zz-7` AC2).

---

## 1. THE SERVED STATE, RE-READ

`opal-amgt-scoped-api` returns CodeSha256 **`zHpr7FhS+irmKofIuKNqTkQm2hj7x2fvS1rrX1ohkfQ=`**, LastModified 2026-09-30T05:20:04Z. This
equals zz-8's close.

zz-8 closed on **AC2 FAIL with the rollback waived for AC2 only** (CTO msg 26943): ASML's driver chart is not served, because the
served chart reads the D-1 drafting document's embedded driver, which the rewrite does not regenerate. That is a carried unmet, not
a pass. The issuer's own error row `Z-S312` names the cause: zz-6's check handed the chart its input in process. The issuer's
proposed gate ("a check whose claim is a SERVED outcome reads the served route") is agreed. It is the same class as this seat's
round-49 finding on FWD-30's plants.

## 2. L9 -- `zz-7` AC2: "each of the 31 outcomes' `state` follows from its `output_excerpt` read against its `fence_quote`"

This seat read all 31 rows of `0.9.0_WK_AMGT_RESAPP~182/FWD_EVIDENCE_ROUND51.json` against the file's own `state_rule`:
- met = the instrument returned the clause's condition;
- unmet = the instrument returned it false, or the precondition of a human-act clause is absent on the served state;
- unmeasurable = the clause needs a browser capture or a completed human act no instrument records.

**VERDICT: PARTIAL -- 30 of 31 states follow; FWD-6's does not.**

**FWD-6 (graded `met`) contradicts the file's own rule and its own sibling FWD-12.**
- The fence is "EXERCISED -- someone has actually compared two versions". The worker performed the compare itself on the served
  route (BA_US_Equity, 200, added 212, changed 7).
- Its own reason then states the portal client wraps none of ledger, versions or compare.
- **This seat checked the portal at HEAD:**
  - `src/api/endpoints/amgt-lead-panel.ts` calls `/refresh`, `/overlay`, `/thesis`, `/peers`, `/coverage` and `/print` only;
  - the only `/compare` string in `src` is an unrelated InvestorReporting test.
  - So an analyst has no page surface to compare versions on.
- **FWD-12** has the identical shape: the ledger is served, there is no page surface, and no act was observed. It is graded `unmet`
  on "the ledger has no page surface".
- By the state rule, FWD-6's human-act precondition (a page on which to compare) is absent, so the state is **unmet**. The worker's
  own call against the route is evidence the capability exists server-side, not that "someone compared two versions" in the
  product.
- **Corrected tally: met 7, unmet 10, unmeasurable 14.**

**One boundary noted, not a correction.** FWD-10 is graded `met` on "a check has actually refused something and the refusal was seen
on the page", with "seen" read from static markup by a harness. That is consistent with FWD-24/25/26, which grade render-state
clauses on static markup, provided "seen on the page" means "rendered on the page". If the CTO reads "seen" as a person's act, it
moves to unmeasurable like FWD-15/16.

**The other 29 follow on their excerpts:**
- **Human-act unmeasurables with the precondition present:** FWD-1, 3, 4, 5, 8, 15, 16, 17, 18 and 19.
- **Browser-metric unmeasurables:** FWD-21, 27, 28 and 29.
- **Precondition absent or condition false, so unmet:** FWD-2, 7, 11, 12, 14, 20, 22, 23 and 31.
- **Met on the instrument:** FWD-9, 13, 24, 25, 26 and 30.
- On FWD-30, the value-compare grader this seat verified at v60 reads 96 of 96 with 0 unscaled, after AMGT_CORPUS round 22's unit
  apply.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W176-S1` (the export's UNRESOLVED unit on 6 names; FWD-30 held there) | **GRADUATED** | The issuer's post-deploy sweep reads "digits compared, scale unchecked = 0 (was 6)", with 0 differing over 114-192 facts on each of the six. The cause is AMGT_CORPUS round 22's unit apply (`0982a0767d`), which this seat graded there. |
| `Z-S312`, `Z-S311` (the issuer's error: zz-8 AC2's premise was false at the cut) | **CARRIED** -> the gate proposal | ASML's driver chart is carried unserved to round 52 |
| `Z-W182-S1` (`exportCompare.harness.cjs` stale), `Z-W182-S2` (FWD-22/23 describe interfaces the page no longer has) | **CARRIED** -> the analysis | clause-or-page call |
| `Z-W185-S1` (the last-block gate can verify a number from another column) | **CARRIED** | |
| `Z-W180-S1/S2`, `Z-W184-S1`, `Z-S310`, `Z-S309` | **CARRIED**, resolved or routed | as the packet |
| the older ARMED set | **CARRIED**, unchanged | |

## 4. L10 PRECONDITION

1. **Every task order terminal:** 7 of 7. zz-8 closed with AC2 failed under a cited waiver. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** as above. **MET**
3. **Every judgment criterion graded:** 1 of 1, PARTIAL (FWD-6 reads unmet). **MET**

---

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S431",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T06:45:00Z",
    "one_line": "L9 round 51: zz-7 AC2 PARTIAL -- 30 of 31 FWD states follow from their excerpts; FWD-6 'met' does not: the worker called /compare itself, but the portal wraps no versions/compare route (checked: amgt-lead-panel.ts calls refresh/overlay/thesis/peers/coverage/print only), the same shape FWD-12 grades unmet -- corrected tally met 7 / unmet 10 / unmeasurable 14; Z-W176-S1 graduates (0 unscaled after CORPUS r22).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-AMGT-zz-1, zz-2, zz-4..zz-8 read 'complete' on their LAST <status> tag.",
        "Lambda opal-amgt-scoped-api CodeSha256 zHpr7FhS+irmKofIuKNqTkQm2hj7x2fvS1rrX1ohkfQ=, LastModified 2026-09-30T05:20:04Z.",
        "FWD_EVIDENCE_ROUND51.json (31 outcomes; tally met 8, unmet 9, unmeasurable 14): FWD-6 state met, reason 'The act was performed by this worker on the served route ... the portal client (api/endpoints/amgt-lead-panel.ts) calls refresh, overlay, thesis, peers, coverage and print; it wraps none of ledger, ve...'; FWD-12 state unmet, reason '... the ledger has no page surface ...'.",
        "Portal HEAD: src/api/endpoints/amgt-lead-panel.ts route strings /coverage /overlay /peers /print /refresh /thesis; git grep '/versions|/compare' -- src: 1 file, src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-85.variant-asks.test.tsx (unrelated)."
      ]
    },
    "adjudicates": [
      "AMGT_RESAPP-Z-W176-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @4f1e532258 asserts 7 of 7 terminal, zz-8 live at zHpr7FhS with AC2 failed under an AC2-only waiver, FWD-30 96 of 96 values equal with 0 scale-unchecked, and presents zz-7 AC2 for judgment.",
    "world_is": "True as read. The re-grade's states follow from their excerpts except FWD-6, which counts the worker's own route call as an analyst's product act that the page cannot host.",
    "notes": "FOR THE ROUND-51 ANALYSIS: FWD-6 reads unmet (no page surface for versions/compare), consistent with FWD-12; decide whether FWD-10's 'seen on the page' means rendered or a person's act; agree the gate that a served-outcome check reads the served route (Z-S312)."
  }
]
```
