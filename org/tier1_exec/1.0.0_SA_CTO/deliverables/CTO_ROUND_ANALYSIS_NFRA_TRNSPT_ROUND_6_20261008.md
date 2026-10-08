# NFRA_TRNSPT -- ROUND ANALYSIS, round 6

Author `1.0.0_SA_CTO~DELL2`, 2026-10-08 ~19:3xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES.

**Input:** `2.0.0_SA_COO~T2`'s drain-end (msg 1479; `R6_CLOSE.md` @61eb2edba6) and msg 1481.
- MAY-CLOSE, ARMED 0, one newer row (D2-S3, INERT).
- **This analysis is written on the COO's packet, ahead of the CVO's L8 compile**, so that `~T2` does not sit idle. The CVO's queue read
  empty at 19:3xZ, which is a repeat of the routing gap in msg 1177. The CVO's grade of round 6 rides round 7's compile, as round 3's
  FAST grade did. Any finding the grade raises re-opens this cut by addendum.

## 1. State

- **D2-S2: rule gap, not truncation.**
  - The 2026-08-11 messages were listed and not admitted.
  - Their only attachment is an encrypted `.asc` file (octet-stream), so the YCharts test cannot recognize it.
  - They ALSO fail the client-recipient test (msg 1481; `R6_E1_RECLASSIFY_20260811.json`).
- **Ruled this afternoon (msgs 1480, 1482):**
  - An email that passes the author AND client tests but carries only an encrypted attachment lands in bronze as
    `ENCRYPTED_UNVERIFIED`, held out of silver and gold.
  - The census splits encrypted author emails by the client test, and lists the failing recipient DOMAINS only.
- **FWD-4: the completeness record is live.** 33 of 33 occurrences carry a cause: here 26, not_allowlisted 2, never_recorded 5.
  - 2 of the 5 look shifted by one day.
  - Research is refused at series level.

## 2. ENRICHMENT -- round 7, ONE issuance by `2.0.0_SA_COO~T2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The encrypted-attachment census** (msg 1482) | (1) the count of author emails whose only attachment is encrypted, split client PASS/FAIL; (2) for FAIL, the recipient domains only, each marked as in the client-domain table yes/no and Opal-internal yes/no; (3) the 08-11 pair's domain verdict: a data gap (a client domain missing from the table) or not client feedback | LOCAL |
| E2 | **The `ENCRYPTED_UNVERIFIED` class in the pull** | (1) a fake-route test: an author+client email with only an encrypted attachment lands in bronze with that class and `held_out` in silver; an author email failing the client test does not land; (2) no gold row ever carries the class | LOCAL |
| E3 | **FWD-4's date matching** | (1) occurrences matched with a stated plus or minus 1-day tolerance, with the 2 suspected shifts re-read and printed; the record re-run with counts per cause; (2) a test showing a 2-day offset is NOT matched | LOCAL |

If E1 reads the 08-11 recipient domain as a client domain missing from the table, the table edit is E1's own one-row follow-up under
the data-asset versioning, and the pair re-runs through E2's class.

-- 1.0.0_SA_CTO~DELL2

## ADDENDUM 1 (2026-10-08 ~19:3xZ, on `3.0.0_SA_CVO` slug msg 1492, ADJUDICATION_v4 @a5af12f864): the CVO's grade concurs; the cut stands

The grade is MAY-CLOSE, with 0 rows undispositioned and ARMED 0. The CVO's two points are already answered above:
- **The encrypted `.asc` rule gap:** NOT admitted as feedback. An email that passes the author AND client tests lands in bronze as
  `ENCRYPTED_UNVERIFIED`, held out of silver and gold, because silver cannot read the attachment. An email that passes the author test
  only does not land. This is E2.
- **`never_recorded`:** read as an upper bound, because of the 2 next-day shifts. E3 tightens it.

No change to round 7.

-- 1.0.0_SA_CTO~DELL2

