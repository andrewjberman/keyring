# ANDREW-DIRECT 2026-07-28T203435Z -- COTTONWOOD **SHOULD BE INCLUDED** in the aggregate

**Recorded by:** `2.0.0_SA_COO` - **Channel:** Andrew directly at the COO terminal
**Received:** 2026-07-28T203435Z (read from `date -u`, not inferred)
**Recorded + broadcast:** same turn, per `org/XXX.md`

---

## THE QUESTION PUT TO HIM

`1.0.0_SA_CTO` established that `mdpf_aggregate_aua.py` enrolls partners **deliberately, by onboard date**
(`INFLECTION_PARTNER_ONBOARD_DATE = "2026-05-18"`), and explicitly declined to answer from the wiring
whether Cottonwood's absence is a **DEFECT** or a **PENDING ENROLLMENT** -- correctly, because the code
cannot distinguish them. I put it to Andrew as a product-semantics question.

## VERBATIM

> **"Yes, cottonwood should be included"**

**NOT A PARAPHRASE.**

---

## WHAT IT BINDS

1. **COTTONWOOD IS AN AGGREGATE PARTNER.** Its absence from `platinum/mdpf/aggregate_aua/{date}.json` is a
   **DEFECT**, not a deliberate phasing. The contingency CTO flagged is discharged.
2. **THE ROSTER FIX IS NOW REQUIRED, not optional.** Single-source the roster to the authoritative scope
   list (`{scope} = 49financial | inflection | cottonwood | global`, Andrew-locked), have **BOTH** literals
   read it -- `expected_partners_for()` at `:492-500` **and** the independent
   `expected_partners = {"49financial","inflection"}` at `:1132` -- and enroll cottonwood with an onboard
   date, the way inflection was on 2026-05-18. **The enrollment mechanism already exists and works; it was
   never walked for this partner.**
3. **THE LABEL DEFECT WAS NEVER CONTINGENT AND STILL STANDS.** The artifact calls a two-firm number
   `opal_aggregate_aua` and asserts firm-wide completeness (`feeders_missing: []`,
   `rolled_forward_partners: {}`, `status: "current"`). Per the standing 0824/0833 law the ~$168.3mm
   difference from the serve is **TWO QUANTITIES, NOT A GAP** -- and it must be basis-labelled regardless.
4. **THE SENTINEL MUST BE FIXED WITH THE ROSTER, NOT AFTER IT.** `MDPF_ASSETS.019 SENTINEL 2` (`:736`) is
   ERROR-level and currently emits *"all expected partners present"* **truthfully**, because its expectation
   set is one of the two hardcoded literals. **Enrolling cottonwood in the data without single-sourcing the
   sentinel leaves a control that will certify the NEXT omission exactly as it certified this one.**

## A MEASUREMENT I ALREADY HOLD THAT BEARS ON THE ONBOARD DATE

From the served cottonwood artifact (measured 2026-07-28, `json/mdpf/cottonwood/...`):
```
447 dates, 47 NON-NULL model_aua
first non-null: 2026-05-28  (454,064.58)
last  non-null: 2026-07-22  (124,376,009.73)
```
**`2026-05-28` is the natural onboard-date candidate** -- the first date cottonwood carries a real value.
**FLAGGED, NOT PRESCRIBED:** whoever implements should ground the date on the feeder's own first
availability, not on this served-artifact reading. **A wrong onboard date silently truncates history**, and
it is exactly the kind of literal this fix exists to stop hand-picking.

## ⚠ SCOPE OF WHAT THIS DOES **NOT** ANSWER

- **It does not tell us the DDB stall resolves.** The stall is legacy-lineage (Stage 3/WS-A ->
  `platinum/mdpf/*` -> `opal-assets-daily-emitter` -> `opal-assets-daily-aua`). The roster fix addresses
  cottonwood's absence; **whether the remaining 13-of-32 value-stall is fully explained by it is UNVERIFIED.**
- **It does not reach the REVAMP lineage.** Stage 6 writes `gold/mdpf_revamp/*` only (dispatch `:607`).
  **AE~C's grant still cannot affect this.**
- **Feeder discovery on the read path is still unexamined**, and `0` cottonwood tokens is strong, not
  exhaustive -- a feeder arriving under a neutral key would not appear in that grep.

## STATUS

**The work is now sovereign-authorised and STILL UNOWNED.** It is legacy-lineage, `0.7.0_AE_CloudOps` lane;
AE base is STALE at its context limit; the AE-base spawn was requested from MSTR at 183123Z. **A sovereign
answer raises its priority; it does not create capacity.** Escalating the capacity need with this attached.

-- `2.0.0_SA_COO`, 2026-07-28T203435Z
