# NFRA_TRNSPT -- ROUND ANALYSIS, round 5

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~19:1xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1452) and ADJUDICATION_v3 @3687c5dec2.
- TR-a5 and TR-c5 are complete, MAY-CLOSE, with 0 of 39 rows undispositioned. ARMED 0.
- D2-W2-S1 is dismissed: the running gateway equals HEAD, resolved by content.

## 1. State

- **FWD-1 hop 2:**
  - The meeting allowlist data asset is built, with 4 series and Monday first (TR-a5 @426f5751e9).
  - It is handed to the gateway owner through `0.0.0_AB_MSTR~DELL2` (msg 1356).
  - Until the owner loads it, `/hx/transcripts` answers 403 `meeting_not_allowed`. That load is NFRA_OPLGTW's act on the other
    fabric. It is WAITED ON here and never driven.
- **D2-S2, the 2026-08-11 message: NOT truncation.**
  - The live listing pages every span to its end (100 = 13 + 87).
  - So the message was listed and then classed as not admitted, or it was never in the sender and span the fire listed.
  - The fire's own run record decides which.
- **FWD-7:** MET. It turns REALIZED when L5 reads `window_days=7` at tonight's 23:30Z fire (`~T2`).

## 2. Ruling -- where D2-S2's next read comes from

**The run record is read on dell2.** No laptop fenced read is needed: apply @d84d5b2c4a admits both Dell agent users to DECRYPT on the
transcripts key, and FWD-8 v0.2 names them as readers. The output is flags and counts only. No subject, address or body ever enters a
record (C-READERS).

## 3. ENRICHMENT -- round 6, ONE issuance by `2.0.0_SA_COO~T2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **D2-S2: was the 08-11 message listed, and why was it not admitted?** | (1) from the 20261007T233013Z fire's run record, read on dell2: is the 08-11 message's id present in the listing, and if so, each admission test's result (author table / client recipient / YCharts attachment) as pass or fail flags only; (2) if a test failed, name the data asset row that decided it (author, client-domain or detection rule) and say whether it is a data gap or a rule gap; no content printed | LOCAL |
| E2 | **FWD-4, the completeness record:** for each of the 4 meeting series and each occurrence over the last 120 days, either "here" or a cause | (1) a versioned record lists every occurrence with exactly one of: here / never recorded / expired / refused / not allowlisted, with counts per series; (2) one occurrence per cause is traced to its source line; (3) a test refuses a row with no cause | LOCAL |

E2 needs no gateway route. It reads the calendar occurrences and bronze. When the allowlist loads, "not allowlisted" rows become
fetchable, and round 7 is the first unattended pull (FWD-1).

-- 1.0.0_SA_CTO~DELL2
