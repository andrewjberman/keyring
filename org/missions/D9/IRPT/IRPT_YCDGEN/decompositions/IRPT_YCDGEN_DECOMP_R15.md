# IRPT_YCDGEN round 15 -- decomposition: the binding's pair, the stale map entry, and a close count that names its orders

Issuer `2.0.0_SA_COO~G2`, 2026-10-11.

**Input:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_15_20261011.md` @c3cf777f3b, section
3 (four items). It answers this seat's round-14 drain-end read @8e099e4110. No PRD addendum. FWD-1 waits on the sitting or
Andrew's word on a measuring identity. **Nothing is cut on the vendor path.**

## Cells (round 15)

| cell | lane | item | what EXISTS at the end |
|---|---|---|---|
| `YCD-a-15` | ~G2 (a pair; the apply is the applier's, later) | 1 | The binding's never-widen packet, COO half, for the CTO to read before it signs. It states the five things section 2 of the analysis names: the waiting test message accounted for at the pre-read with BOTH branches of what the bound resident does with it, never a purge; that the binding causes no vendor sign-in and no vendor call, read in the code path it enables; every consumer of what the bound resident writes, with one read through each; the rollback per key and what a half-bound host does; and its order, after NFRA_OPSWKF's FWD-8 release is applied and read. WRITTEN, NOT APPLIED |
| `YCD-b-15` | ~G2 | 3 | The source map's entry for `irpt-ycharts-generate` corrected from the live digest and the build input, by content. Row IRPT_YCDGEN-D2-S63 filed in this commit |
| `YCD-c-15` | ~G2, DONE in this commit | 4 | The twentieth order of the round-14 close count, named (below) |
| -- | no cell | 2 | Row S16's disarm stays on the sitting; nothing is cut for it |

## `YCD-c-15`: the twentieth order (measured)

`round-close-check.py --round 14` counts 20 seat-folder orders, every `IRPT_YCDGEN.TO-APPLY-*` this seat ever issued,
because none carries a `<round>` tag (the tool says so: "counted in EVERY round's check until the issuer tags them"). 19
read `<status>complete</status>`. **The twentieth is `IRPT_YCDGEN.TO-APPLY-st28.svc-49financial-f1-release-dell2`,
`<status>superseded</status>`** (last changed @afec47791f, 2026-10-09): terminal, not complete, superseded by st29. So the
round-14 close stood on 4 orders of its own (j4, x1dry, j5, j6, all complete) and 16 from earlier rounds. The count was
right; what it counted was wider than the round. Tagging the twenty with their rounds is hygiene for the drain and is not
cut here.

## Dependencies

- `YCD-a-15`'s APPLY waits on NFRA_OPSWKF's FWD-8 release (the analysis: one served change at a time on the path a service
  token walks). The packet itself waits on nothing.
- `YCD-b-15` waits on nothing.

fanout: 0 tree orders; 2 cells worked directly by the issuer, 1 done in this commit; cap 8.

## Not cells

- Anything that changes how the vendor is reached; any request down the YCharts path.
- Any redrive of the eight (row D2-S45).
- Parked as before: the one-equity store row, fund allocations, the 70 rule-less elements.

## AMENDMENT 1 (2026-10-11, the issuer, on CTO msg 5727): cell `YCD-d-15`, cut BEFORE the binding's PART 2

`1.0.0_SA_CTO~DELL2` ruled on the binding's packet PART 1 (@4fdc20b233): not bound as built; first a cell so that the chain
stops for a request with no ticket BEFORE `analysis_ready` is sent, with tests asserting the drafter is not called.

| cell | lane | what EXISTS at the end |
|---|---|---|
| `YCD-d-15` | ~G2, one build order `IRPT_YCDGEN.TO-YCD-d-15.analysis-ready-is-sent-only-for-a-request-filed-under-a-ticket` to `0.9.0_WK_IRPT_YCDGEN~17`, `<risk>WORLD</risk>` | The worker sends `analysis_ready` only for a request whose accepted record carries a ticket id; both send sites obey one rule; a skipped send marks nothing as sent and prints one line; five test groups. Dormant on the host until a release binds the queue |

**What this cell does NOT do, and it is named for the CTO:** the ruling also says "a ticket whose type does not ask for
commentary stops the same way". The worker cannot decide that: the accepted record carries the ticket's id and nothing of
its type (`acceptance.py` lines 120-121), and the worker has no ticket read and is ordered not to gain one. That half is
decidable where the ticket is read: at submission (the generate function validates the ticket id it is given) or in the
drafter. It is put to the CTO as one question; it is not cut here.

`YCD-a-15`'s PART 2 now depends on `YCD-d-15` merged, as well as on FWD-8. fanout: 1 of 1 chains, cap 8. Gate limb:
`to-pipeline-gate.py` graded the new order at this commit.
