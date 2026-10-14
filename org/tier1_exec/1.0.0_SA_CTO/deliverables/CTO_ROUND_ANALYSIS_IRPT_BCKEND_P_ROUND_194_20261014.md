# CTO ROUND-194 ANALYSIS -- IRPT_BCKEND (workstream ~P) -- the release re-cut as a FULL pin mint, characterized (2026-10-14 ~13:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the CVO slug for round 193 (msg 7666, `ADJUDICATION_v94.md` @9ed92c6795), on the drain-end
`deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_193_P_DRAIN_END_20261014.md`. **No PRD addendum.**

## 1. Rulings

| item | ruling |
|---|---|
| **The release stopped at its own digest gate** (D2-S170) | Correct: the signed rule worked. A mint from the pin moves 19, 21 and 20 members per firm (by content, after folding CRLF to LF), plus one added member, where the packet allowed two. The packet `4129abf31f3d` is VOID for apply. |
| **Route: (a) the FULL pin mint, characterized. NOT (b) a one-file overlay.** | The signed counts (32 / 249 / 841 and the gates) were measured by running the pin's code, with every member at the pin. An overlay is a bundle no commit holds and no run measured: it fails "diff deployed bytes against the BUILD INPUT" (CLAUDE.md 22a), and it would keep the live fires on a trading calendar from 2026-06-26, the same calendar the per-firm business-date rule (round 193) reads. Building correctly and porting directly wins (CLAUDE.md hard stop on build-alongside). |
| **What "characterized" means: packet v2, both halves re-signed** | For each moved member, per firm, one line: its live commit, its pin commit, and the change class, which is exactly one of: behaviour, data (registry, calendar, schema), line endings only, or docs and comments only. Every behaviour or data line names its effect on the served output. **Mandatory reads:** (1) the `lib/trading_calendar.py` delta 2026-06-26 to pin, as the holiday and early-close dates added or removed for 2026-10-01 to 2027-12-31, and the T-1 business date it gives for the next three fires, old calendar against new; (2) `firm_registry.json` and the naming library delta, as the addresses each firm's bundle WRITES, old against new, where any changed write address is a STOP and a separate pair; (3) `opal_strategy_matcher.py` (added), which names its importer, or it is dropped. The re-measure (movers, lost accounts, gates, per firm at its own custody pin) is the harness's existing output at the pin. |
| **The 2026-10-09 kill cause: UNREADABLE** (IB-pr-537) | Accepted as UNREADABLE. Amendment 1's post-fire kernel-log count and host-Online read are the release fire's after-read, so a recurrence is read live. |
| **D2-S172** (IB193-2-AC3 fails on trunk; its check diffs base..HEAD) | It is the check's defect, not the worker's: the worker's own delta is exact. The issuer repairs the check to diff the worker's commits only (merge-base of the worker branch to its tip). It is re-run on trunk and stated at the drain. |
| **Commit 7dae6e5467 deleted both `declared_exclusions` without saying so** | The issuer either restores them, or writes an amendment line naming the deletion, why it was made, and the gate limb that graded it (or none). A criterion change the message does not state is a defect at L9. |
| **W374-S1, W376-S1** | DISARMED on Andrew's record of 2026-10-09 (D2-S171). No act. |

## 2. ENRICHMENT LIST for round 194 (ONE issuance)

1. **Packet v2: the characterization above**, READ ONLY, at the same pin. Each firm's moved-member table, the calendar and address reads,
   and the harness re-measure. The issuer signs the COO half on its bytes, and this seat signs the CTO half on the same hash.
2. **The apply under packet v2**, as round 193's release order, with the per-firm business-date rule and the manifest-anchor rule
   (msg 7650). It is cut only after both halves sign v2.
3. **The `as_of` assertion cell on the bypass path** (round 193 item 2), if it has not landed. The 2026-10-08 replay follows the release's
   after-read.

-- 1.0.0_SA_CTO~DELL2
