# NFRA_CTLPLN -- ROUND-21 ANALYSIS (1.0.0_SA_CTO, 2026-10-15 ~18:4xZ)

**On:**
- the issuer's drain end `deliverables/2.0.0_SA_COO~C/L8_PACKET_ROUND21.md` and `ROUND21_INPUTS_FOR_ROUND_ANALYSIS.md` @445bca4969;
- the CVO's L10 slug `surprise-channel/adjudications/ADJUDICATION_v26.md` @98ddb8c1a9.

**PRD:** v0.31 (ADMITTED).

## 1. FWD coverage

| grade | count | FWDs |
|---|---|---|
| REALIZED | 3 | 1, **5 (new)**, 28 |
| ADVANCED | 21 | 2, 3, 4, 6, 7, 8, 10, **11 (was GATED)**, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 27 |
| GATED on Andrew | 0 | -- |
| PARKED | 1 | 9 |
| MOVED | 3 | 13, 20, 26 |

**FWD-5 is REALIZED,** on the CVO's own reads:
- the earlier pushes wrote two real HELD rows and deployed nothing;
- the trunk merge at 17:53Z deployed nothing;
- the signed push changed 1 of 190 code and gold keys, and the latest ETag equals the committed md5.

**FWD-11 moved off Andrew:** he restarted dell1 at 15:46Z. What is left to read is which round was where.

## 2. Rulings

1. **S9132 stands as ruled (msg to the issuer, ~18:1xZ).** The CLAUDE.md push clause ends: "Who may push where stays with
   `.tools/hooks/never-rules-gate.sh`". LD-0367/0368 is that gate, and it lets only the integrator push `box/laptop`. "Push at will"
   means no word from Andrew; it never meant any seat on any branch. The CVO's refused push today was the gate working.
   **No law edit.** The sentence already carries the reconciliation.
2. **FWD-3: "the managers" are each box's `0.0.0_AB_MSTR` lane.** An acknowledgement by a CTO or CloudOps lane is not a manager
   acknowledgement. **Cut the refusal:** `crossbox-call.py ack` refuses any serial that is not the receiving box's MSTR lane.
   - The cell proves it with one non-manager ack refused and one manager ack admitted.
   - The CVO then re-reads the matrix for today's six non-manager acknowledgements: each one either gets a manager ack or is named.
   - FWD-3 grades on that re-read.
3. **FWD-11, one read per owner:** each of dell1's 18 open ledger entries is classed as interrupted by the 15:46Z restart or
   ordinary. The seats that held a round at 15:46Z, and each one's state after the restart, are read through
   `0.0.0_AB_MSTR~DELL1`. If every interrupted entry resumed or was closed with nothing lost, FWD-11 meets its outcome.
4. **FWD-14, read before tonight:**
   - each target's event 1149 for the laptop's address `100.96.167.100`, plus the laptop's own outbound remote-desktop history;
   - in the same read, each target's event 1149 for the MacBook's tailnet address (ruling of ~16:4xZ). An earlier MacBook session
     may grade that arm before Andrew's session tonight (`c9a4`).
   - The refused attempt from off the tailnet stays an arm, run from a seat outside the tailnet if one exists; otherwise it waits
     on Andrew's MacBook off the tailnet.
5. **The package journey:**
   - Correction to inputs 1.1: the CRO's co-decision is NOT outstanding. It exists as a file,
     `org/tier1_exec/4.0.0_SA_CRO/deliverables/CRO_CODECISION_INTAKE_DUCKDB_REQ-20261015T171032Z_20261015.md` @8b63d5772c.
     `intake_request.py` admits one decision per request by design, and FWD-16 needs one decision read back by an outsider.
   - The chain runs as the inputs list it: the tag (call `6bd5`), then fetch, check, pack, taildrop, install from the file, the
     lane's read, and the CVO's read-back.
6. **The read-test fallback** (inputs 1.3) is one small worker cell, in the hygiene batch.
7. **The danger map is this seat's, and W117-S1/S2/S3 are fixed as one change in the reflex, with no new scheduled task:**
   - S1: the map carries its build time inside the file, and the reflex reads that, never the file's mtime.
   - S3: the reflex rebuilds the map itself when it is older than its threshold.
   - S2: a sparse worktree never builds the map. It reads the main tree's map, or reports BLIND.

   This is a tool artifact with no served consumer, so a self-refreshing read is enough. The no-alarms moratorium also argues
   against a new scheduled job.
8. **W117-S4:** the issuer's FIXTURE classing stands unless the CVO overrules it in the next slug.
9. **33 owned remediation rows unmoved for 2 or more rounds:** the round-22 packet lists them by owner. Each owner dispositions its
   own rows: resolve, dismiss with a reason, or carry with a named outcome. This seat dispositions its own rows in the round-22
   analysis. A row nobody moves for a third round is dismissed as INERT by its owner, with the reason stated.
10. **Noted, no act:**
    - `check_inbox` re-prints the accumulated inbox on every call. This is MSTR's `org/mcp/server.py` and its DESIRED
      acked-never-rides clause, so the issuer files one row in MSTR's lane.
    - U7 stays dead; `0.7.0_AE_CloudOps~CT2` is the deploy seat.

## 3. ENRICHMENT LIST for round 22 (one issuance; fan-out per the issuer's chains, cap 8)

1. The package journey from the tag to the CVO's read-back (ruling 5).
2. FWD-3's manager-only ack refusal and the matrix re-read (ruling 2).
3. FWD-11's per-owner read of dell1's 18 entries (ruling 3).
4. FWD-14's event-1149 reads, laptop and MacBook (ruling 4).
5. One hygiene batch: the danger-map change (ruling 7), the read-test fallback (ruling 6), and the 33-row listing (ruling 9).

## ADDENDUM 1 (1.0.0_SA_CTO, 2026-10-15 ~19:3xZ) -- ruling 2 WITHDRAWN; v0.31's FWD-3 bullet was this seat's misreading

On `0.0.0_AB_MSTR` msg 109493. `crossbox-call.py ack --by 0.0.0_AB_MSTR~DELL2` refuses "not the named seat"; the tool has no
manager path.

FWD-3's ACCEPT, at the PRD's line 51, printed: "a message from a seat on one box goes to its own box's fabric manager, which passes
it to the other box's fabric manager, which delivers it to the right seat; the sender can show that it was read, not only delivered.
No other seat talks across boxes."

- **The managers CARRY the message. The seat it is addressed to READS it.** The acknowledgement is that read, so the named seat
  acknowledges. That is what the tool already enforces.
- v0.31's bullet ("each crossbox acknowledgement is run by the receiving box's manager seat") and this analysis's ruling 2 put the
  managers in the reader's place. **Both are withdrawn.** No tool change is made, and no manager-ack path is added.
- **FWD-3 grades per pair on two things:** the call travelled manager to manager, and the named, non-worker seat acknowledged it.
  The six acknowledgements the CVO set aside (by CTO and CloudOps lanes) count, wherever their delivery went through the managers.
- **Round 22's FWD-3 cell is therefore a READ, not a build:** for each of the 12 pairs, its path through the managers and its named
  seat's acknowledgement. The 8 manager-ack asks in msg 109491 are withdrawn.
