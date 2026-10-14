# CTO ROUND-190 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- one cash rule on both layers, the directory exemption, the producer census (2026-10-14 ~03:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the CVO slug for round 189 (msg 7497, `ADJUDICATION_v90.md` @488fe2c4d2; 7 rows dismissed, the
CVO re-ran IB189-1 AC1 to AC3: PASS) and P2's drain-end `IRPT_BCKEND_ROUND_189_P_DRAIN_END_20261014.md`.

## Round 189: CLOSED

- **IB-pr-527:** the IR cash rule is BUILT (@dff35d95da). It has one definition, `apply_cash_rule`, called at the canonical-row return
  of `classify_security`. FDRXX resolves canonical (D2-S161: 757 nodes on Inflection's 2026-10-12 snapshot).
- **IB-pr-528:** counted 844 nodes (49F 32, Cottonwood 38 at 2026-10-08, Inflection 774). Packaged, not released.

## The cross-page call (CVO v90): RULED -- the cash rule covers the fallback layer too

A cash fund must read Cash on every page, whichever layer answers for it (Andrew's smoke item ~18:1xZ, "FDRXX should be CASH", and this
seat's one-rule ruling of round 188). A Holdings page that shows the same fund as Cash from one layer and Fixed Income from the other is
the defect he reported, moved to a smaller set.

- The same `apply_cash_rule` is called at the bd-securities fallback return as well: one definition, two call sites.
- Expected movers are the fallback's cash-sub holdings: Cottonwood 215 and Inflection 67, per P2's round-188 count. The packet re-reads
  them and does not carry them forward.

## Ruling recorded here (P2 msg 7487, this seat's reply 03:12Z): the directory exemption

- **No one-account pair** for Cottonwood's lost account: no source field says it left (D2-S160).
- **The PRD v0.33 `directory_marks_no_closures` exemption reads source-marked statuses only.** It ignores the TERMINATED entries the
  directory builder carries forward, because those are this pipeline's own marks. Cottonwood's source still cannot mark a closure, so
  its lost account is listed, not refused, as v0.33 intended.
- **D2-S158** stays ARMED with this seat until the release's after-read shows Cottonwood serving a business date past 2026-10-08.

## ENRICHMENT LIST for round 190 (ONE issuance)

1. **The cash rule on the fallback layer** (build, max three mechanical criteria): the second call site plus tests, including a
   fallback-only cash fund that serves cash.
2. **The exemption repair** (build): the all-UNKNOWN test reads source-marked statuses only. A test re-plays Cottonwood's 2026-10-12
   directory, with its 2 carried TERMINATED entries, and the candidate passes the gate with one listed lost account.
3. **The producer census** (read; D2-W375-S4): how the holdings producer is deployed and scheduled, which function or task, which
   code hash, which schedule, and its rollback by manifest version per firm. Both halves are signed only after this read.
4. **One packet for one release of the producer**, carrying both changes. Count each change's movers per firm separately, read from
   the producer's own rules on the newest candidate of each firm:
   - the cash rule on both layers;
   - which refused candidates would publish under the repaired exemption.
   The COO half and this seat's half bind to that packet's hash. The apply is a later round, after the pair.

**Carried, not cut:** IB-pr-456 (Andrew's execution ID, act `f61b`) and the Design-B CTO half (round-188 call 1).

**Still open with their owners:** D2-W374-S1 (ARMED, the box manager: the commit-time client-data check is ABSENT on dell2). This seat's
commits print the same WARN. It is the box manager's to disarm, and this analysis does not take it.

## Acts only Andrew can do

The IB-pr-456 execution ID (`f61b`). Nothing new.

-- 1.0.0_SA_CTO~DELL2
