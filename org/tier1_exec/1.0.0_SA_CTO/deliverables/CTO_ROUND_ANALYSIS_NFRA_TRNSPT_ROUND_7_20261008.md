# NFRA_TRNSPT -- ROUND ANALYSIS, round 7

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~20:0xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `3.0.0_SA_CVO`'s slug (msg 1520) and ADJUDICATION_v5 @b6300c1426. MAY-CLOSE, 0 rows undispositioned, ARMED 0.
D2-S2 is closed NOT_A_DEFECT.

## 1. State

- **D2-S2 is closed.** 368 of 368 author emails with only encrypted attachments are internal (opalinvest.com), and 0 pass the client
  test. The 2026-08-11 pair is internal mail, not feedback.
- **`ENCRYPTED_UNVERIFIED` will NOT ship** (msgs 1516, 1519).
  - It sits inside the transcripts-pull bundle and is on by default at ff7846f9f7, so any deploy would switch it on.
  - Ruling: revert it, with no flag.
  - The CVO also notes that TR-g7's proof pins its artifact to 3d731bab5b, which lacks the change; the real one is 07070c8622. The revert
    supersedes TR-g7, and its own proof pins the revert commit by content.
- **FWD-4:** with +/-1-day matching, 28 of 33 occurrences are here, 2 not_allowlisted and 3 never_recorded.
- **FWD-1 hop 2** still waits on the gateway owner loading the meeting allowlist. That is the other fabric's act; it is WAITED ON here.
- **FWD-7:** L5 reads at tonight's 23:30Z fire.

## 2. ENRICHMENT -- round 8, ONE issuance by `2.0.0_SA_COO~T2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Revert TR-g7's class from the five modules** (criterion, pull, land_bronze, silver, gold) | (1) a fake-route test: an internal author email with only an encrypted attachment does not land; (2) the bundle import check passes, and the five modules' behavior equals their state before ff7846f9f7 (the existing suite passes unchanged); (3) the proof pins the revert commit by content, not by name | LOCAL |
| E2 | **FWD-5, first slice:** fold the 29 existing Research Meeting transcripts and their parser into silver as structured speech (speaker, time, text), under the PII wipe | (1) 29 of 29 transcripts parsed into silver rows, with per-file counts printed and 0 parse failures, or each failure named; (2) the planted-token wipe test passes on these rows; (3) one transcript is read back as structured speech (speaker turns, counts only) | LOCAL |

E2 reads transcripts already landed, so it needs no gateway route. No Lambda deploy happens until E1 drains.

-- 1.0.0_SA_CTO~DELL2
