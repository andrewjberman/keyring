# CTO ROUND ANALYSIS -- DSGN_IRPTV1 -- answering the reviewer's compile from watermark 2026-10-02T03:10Z (2026-10-11 ~05:1xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/remediations/REMEDIATION_v6.md`
@5ee302ea91 (3.0.0_SA_CVO msg 4127). **PRD:** `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` v0.18, ADMITTED.
**No PRD addendum.**

## 1. Where the project stands

The project is placed on dell2 and had no seat. 84 of 84 orders are terminal. The old laptop lane worked it under a FAST
lease until 2026-10-05; the reviewer's last compile before today was 2026-10-02T03:10Z, so three days of landed work had
no review. No round analysis exists past round 4. **No FWD is graded by this analysis:** the slug dispositions rows and
graded no outcome, and this seat holds no per-outcome evidence. Section 4 item 5 produces that table.

## 2. The lane (ruled)

**2.0.0_SA_COO~D2 takes DSGN_IRPTV1 as a second project, on `/canonical-drive` FULL at 60m. No new seat is spawned.**
- Its predecessor `2.0.0_SA_COO~D` held this project beside IRPT_DASHBD under two leases with disjoint surfaces. The
  one-project seating rule binds Tier-2 instances, not a Tier-1 seat.
- IRPT_DASHBD keeps priority; its R45 apply waits on Monday's fire, so the lane has room.
- **No FAST lease.** A lease is armed on Andrew's word while he is present; none is asked here. FULL means orders,
  workers and the reviewer's grade before a page change lands, with this seat reviewing each product-file candidate.
- dell2 runs 15 seats. Andrew's pacing word of 2026-10-10 is the reason this is not a sixteenth.

## 3. Rulings on the rows

| row | ruling |
|---|---|
| W35-S1 | CLOSED by the reviewer (fixed at the DEV tip). Nothing owed. |
| W39-S2 (owner this seat: the contract call) | The mislabel is gone; standing INERT, as the reviewer reads it. **The contract:** the history is the VIEWER's own requests and stays so; it is not re-scoped by route. Each row instead states the client its frozen selection names, from a served field. The read plane already derives that client (`ops/owned_requests.py`, `_selected_client`, "the client the request's frozen selection names"), so the field is an addition to the history row, and the page filters by the header's selected client on it. The served half is IRPT_ANLREQ's (2.0.0_SA_COO~Y2), under its own pair; the page half follows it. Ruled directly as a narrow contract call: no CRO is seated on dell2. |
| W35-S2 | INERT (a missing capability, no served number at risk). Export on the Analysis tab is FWD-9's; one cell, section 4 item 4. |
| S7, W21-S2, W23-S1, W29-S10, W34-S1 | One act, section 4 item 1. |
| W29-S10 (owner this seat: how the bar is graded) | **The bar is the failing SET, not a count.** A suite result is graded by comparing the set of failing test ids across three pinned full runs at one commit. Three identical sets: the suite is deterministic at that commit, and each failing id is then ruled once as REGRESSION, KNOWN-LEGACY (named, with its row) or FLAKE. Sets that differ: the differing ids are the finding, and no count from that commit is cited anywhere. |
| S60 (owner this seat) | Placed: section 4 item 3. |
| S61 (owner this seat) | Placed FIRST among the page cells: section 4 item 2. An advisor reads one ticker beside another security's dollars on a served page. It is INERT by the reviewer's standing because the dollars are right; the label is wrong, and it is the only row here a client could act on. |

## 4. ENRICHMENT LIST (2.0.0_SA_COO~D2 cuts ONE issuance, in this order)

1. **One pinned three-run sample of the Investor Reporting suite at the portal DEV tip.** LOCAL, read-only. Output: the
   three failing sets by test id, whether they are identical, and each failing id ruled per the W29-S10 bar above. It
   closes or re-states S7, W21-S2, W23-S1, W29-S10 and W34-S1. The DEV tip is named by `ls-remote` after a fetch, not
   from a local ref.
2. **S61: the Holding cell names the corrected security on a corrected row,** with the uploaded symbol beside it as
   "uploaded as". A served-page wording fix; candidate to this seat before DEV; `/frontend-dev` screenshot read.
3. **S60: one component test that presses the "Did you mean" button** and asserts the re-post's corrections. LOCAL.
4. **W35-S2: Export on the Analysis tab** (FWD-9). The cell first reads why AnalysisTab passes no export signal; if the
   export needs a served route that does not exist, it stops there with a row and this seat rules the contract.
5. **A per-outcome state table, read-only.** For FWD-1 to FWD-23: DESIRED, APPLIED or EXERCISED, each with the evidence
   that says so (a commit, a walk record, a reviewer grade) or ABSENT. It is the input to the next analysis; it is not
   itself a grade.

Items 1, 3 and 5 are independent and start at once. Each build order carries at most three mechanical criteria. W39-S2's
served half is sent to 2.0.0_SA_COO~Y2 by 2.0.0_SA_COO~D2 with the row id; its page half is a later round's.

## 5. Carriers this seat writes with this analysis

- `org/missions/D13/DSGN/DSGN_IRPTV1/project.json`: `coo_lane` to `2.0.0_SA_COO~D2`; `blocking` restated (the 2026-09-26
  text described a round long drained).
- `org/ref/LIVE_ARMS.md`: the row for 2.0.0_SA_COO~D2's second project.

## 6. What this analysis did not measure

It rests on the reviewer's code reads at portal DEV 26f621d5 and on 2.0.0_SA_COO~D2's report-only measurement (msg 4113).
No suite was run and no page was rendered by anyone today. `_selected_client` was read by this seat earlier tonight at
commit 361c44fa9d for another purpose; that it can serve the history row is inferred from that read, not exercised.

-- 1.0.0_SA_CTO~DELL2
