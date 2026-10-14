# CTO ROUND-193 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- the holdings-producer release apply, the per-firm business date, the 2026-10-08 route (2026-10-14 ~12:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the CVO slug for round 192 (msg 7612, `ADJUDICATION_v93.md` @b956283de1; 6 of 6 PASS, 9 rows
dismissed), on the drain-end `deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_192_P_DRAIN_END_20261014.md` @a93d73e6e8. **No PRD addendum.**
The pair for IB-pr-532 stays signed on both halves at sha256 `4129abf31f3d`. This analysis adds rulings, not a re-sign.

## 1. Rulings

| item | ruling |
|---|---|
| **The Inflection pin** (W380-S1) | The release's step-0 re-measure pins EACH firm to the custody partition its packet row used. For Inflection that is the partition that builds the packet's candidate, not 2026-10-12, which builds 2026-10-09. The harness takes a per-firm pin, so this is one read. Its outcome must equal the packet's (PUBLISHED), or the stop rule applies. |
| **The business date** (W380-S3; CTO half condition 8) | **The condition is graded PER FIRM at the fire, not as one precondition of the apply.** For each firm, the after-read accepts exactly one of two outcomes: (a) a publication stamped T-1 by `lib/trading_calendar.py`; or (b) no new publication, where the producer's own gate refused or held because that firm's T-1 custody partition is absent, the absence is read (partition listing) and named, and the served frontier is unchanged. **A STOP and rollback:** any firm stamped with a date other than T-1, or a publication with no T-1 partition under it. One firm's late upstream does not roll back the other two. |
| **The 2026-10-08 replay route** (W381-S2, S3) | **The operator bypass for ONE firm (49financial) and ONE date (2026-10-08).** No gap-fill exemption in `evaluate_publish_gate`: that would move the gate for every firm and every later fire to fill one day. **Before the bypass,** a LOCAL build cell makes the bypass path assert that the landed date equals `as_of`, and refuse otherwise, with a mutant that fails. The replay packet (`ONE_DATE_REPLAY_PACKET_49F_20261008.md`) is re-written on that path. Both halves are signed after the release's after-read, and it applies under its own NEVER-2 ledger. |
| **W381-S1** (the 2026-10-09 kill mechanism) | Accepted. The fire was marked TimedOut at about 310 s of an explicit 3600 s window, exit 137. The issuer corrects the round-191 packet's wording with an erratum line. No timing rule in the release uses the 3600 s window as a cause. |

## 2. ENRICHMENT LIST for round 193 (ONE issuance)

1. **The release apply (IB-pr-532) under the signed pair, with section 1's per-firm rules.** Its first scheduled fire is the next
   10:15 ET fire after the after-read: the 2026-10-14 fire if the apply's after-read lands before it, else the 2026-10-15 fire with T-1
   2026-10-14. The releasing seat states the business date per firm before the fire.
2. **The `as_of` assertion on the bypass path** (LOCAL build, three mechanical criteria at most, one mutant).
3. **The cause of the 2026-10-09 kill (read, LOCAL):** the host's own record for that invocation's window (the kernel log or the journal for
   an OOM kill, and the instance's memory at the time, if retained). One line: OOM, or not, or unreadable. If it is OOM, the release's
   fire carries a memory read in its after-read.

## 3. Carried

- **IB-pr-456, the `commentary_requested` release:** built; its COO half is signed; it waits on Andrew's own PROD submission execution
  ID (act `f61b`, his choice (a) of 2026-10-13 ~17:0xZ). **It is now on the O1 critical path:** IRPT_ANLREQ's FWD-1 run waits on it
  (round-40 analysis @abdbb85058, step 4). This seat signs the CTO half on receipt.
- **D2-W374-S1, D2-W376-S1:** the commit-time client-data check is ABSENT on dell2, logged again by both round-192 workers. The box
  manager's repair (`0.0.0_AB_MSTR~DELL2`); this seat re-asks it once in this turn.
- **D2-S158:** this seat's, until the release's after-read.
- **TO-APPLY-Y77's proof file name** (round-close-check REFUSED without the workstream filter): `2.0.0_SA_COO~Y2`'s to rename.

-- 1.0.0_SA_CTO~DELL2
