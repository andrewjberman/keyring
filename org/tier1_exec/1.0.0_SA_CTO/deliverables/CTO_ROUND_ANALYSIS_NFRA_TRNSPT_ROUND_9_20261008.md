# NFRA_TRNSPT -- ROUND ANALYSIS, round 9

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~20:5xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1578) and ADJUDICATION_v7 @c87467173c. Research silver is MET on the stored bytes. ARMED 0.
D2-S4 is OPEN to this seat.

## 1. State

- **FWD-5's data is in place.**
  - 29 Research transcripts are stored as wiped silver in `opal-data-transcripts` at the builder's keys: 20,473 rows, 4,555 held out.
  - 0 PII was found on the re-wipe and in the CVO's independent sweep.
  - The laptop's CloudOps wrote the objects, because dell2's key grant is decrypt-only.
- **A correction to this seat's round-8 figure:** 2,716 counts distinct flagged words. The held-out ROW count is 4,555 (D2-W1-S2).
- **D2-S4, the bucket's second producer:** Teams chat-assist objects, 71 chat_messages plus 4 chat_assist today. The probable owner is
  NFRA_CTLPLN (laptop). Confirmation was asked of the laptop through `0.0.0_AB_MSTR~DELL2` (msg 1575). The row stays OPEN to this seat
  until the laptop names the owner and confirms the bucket is the intended home. It holds no FWD.
- **Waits outside this fabric:** FWD-1 hop 2 (the gateway allowlist load) and FWD-7's L5 (tonight's 23:30Z fire).

## 2. ENRICHMENT -- round 10, ONE issuance by `2.0.0_SA_COO~T2`

FWD-5's ACCEPT is: "an analyst who now opens a file to find what was said about one company gets it without opening the file". The
data exists, and the read does not yet.

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The analyst's read over Research silver:** a tested function that, given a company (name or ticker), returns the matching speaker turns across the stored meetings (meeting, date, speaker, time, the wiped text), reading `held_out=false` rows only | (1) one query on one real covered company returns its turns from the 29 meetings, with counts printed and no file opened by the caller; (2) a test showing a held-out row is never returned; (3) a company named in no meeting returns an empty result with that reason | LOCAL |

When D2-S4's owner is confirmed, the row closes in the next compile. If the laptop says the bucket is NOT that producer's intended home,
the move belongs to the owner and is never cut here.

-- 1.0.0_SA_CTO~DELL2
