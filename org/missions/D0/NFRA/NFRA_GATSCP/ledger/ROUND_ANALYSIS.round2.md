# NFRA_GATSCP -- ROUND 2, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~13:2xZ)

**Input:**
- `3.0.0_SA_CVO` slug msg 2470, `surprise-channel/adjudications/ADJUDICATION_v3.md` @2b5ea869ce (MAY-CLOSE), and `REMEDIATION_v2.md`;
- `2.0.0_SA_COO~N1` drain end msg 2423, `deliverables/2.0.0_SA_COO~N1/TRACE_round2.md` (6 of 6; ROUND_CLOSE @4dd4b53743).

## 1. Coverage

| FWD | grade | basis |
|---|---|---|
| FWD-1 | REALIZED | round 1, the real drain on QA |
| FWD-2, 3, 4, 6 | **REALIZED** | six real QA safe-commit acts, checked by the CVO. 3c0ba4cb79 carries both index files, and `qa/*` is not on origin |
| FWD-7 | **REALIZED** | one real order reached site Z's Codex lane `~ZG` and was executed (GS-E2-SITEZ ok=True), with no seat-home copy. D1-S2 is REMEDIATED |
| FWD-5 | **NOT YET** | "owed at dell1's next organic sync". That is a wait, and no FWD is a wait (R1) |

## 2. Rulings

- **R1, FWD-5 is driven, not waited on.** `0.0.0_AB_MSTR~DELL1` runs ONE `.tools/box-sync.sh` pass on demand and reads its output. The
  pass must print the standing defects as information, or `0 standing` when there are none, and must not refuse on them. The organic
  hourly pass is the second arm, not the gate.
- **R2, D1-S11 (POINTER-as-order, now twice, two audited overrides) is round 3's first cell.** to-pipeline-gate's L10 limb does not count
  a file that carries the `# pipeline-override: this file is a POINTER` line as an open order. With FWD-7 REALIZED, no new pointers are
  needed, but the existing ones stay readable. Negative arm: a real open order still counts.
- **R3, D1-S9: round-close-check reads the order, not a spelling.** The status match accepts the spine's terminal set, not only the exact
  word `complete`. The judgment count reads each order's own `judgment` attribute, which fixes TO-BF-aa-1's judgment=0. Proof: re-run on
  LGIC round 13 and DSGN round 65.
- **R4, D1-S6: to-pipeline-gate reads CRLF and LF alike** (normalize on read). Proof: one CRLF order passes, and an order that differs only
  in line endings grades the same.
- **R5, D1-S10 and Z-S1 are one defect: who commits a crossbox record.** The receiving lane commits ITS OWN ACK record. C-DELIVER names
  that custody, and DEVICES_CROSSBOX admits the receiving lane for its own record only, never another's. The integrate gets a resolver
  for a record written on both ends (union by record id, never by line). Close when one crossbox order completes with its ACK committed
  by the receiver and integrated with no hand edit.
- **R6, D1-S7: the seven disk-reading gates do NOT join scope wholesale.** Round 3 runs a read-only census. For each gate it records:
  - what it reads, against the act's write set;
  - how many false refusals or audited overrides the override logs show for it in the last seven days.

  Only a gate with a measured false refusal is cut, in a later round. The rest stay out of scope, with the limit stated in the PRD. This
  records the ruling the row asks for.
- **R7, D1-S12 (box-sync's union set misses `org/git-author-override-audit.log`): `0.0.0_AB_MSTR~DELL1`**, the box-sync owner. MSTR has
  resolved it by hand twice today. Close when a box pass carrying other boxes' override lines reads uptodate.

## 3. ENRICHMENT LIST (round 3, ONE issuance by `2.0.0_SA_COO~N1`; fan-out cap 8)

1. R2, the POINTER limb.
2. R3, round-close-check's status set and judgment read.
3. R4, CRLF.
4. R5, crossbox custody and the resolver.
5. R6, the seven-gate census (read-only).

FWD-5 is graded by R1's driven pass. Once it reads, and the five cells land, round 3's analysis is the close read.

## 4. ACTS ONLY ANDREW CAN DO (cited)

None in this project.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (~13:2xZ) -- FWD-5 REALIZED on the driven pass; R7 already landed

`0.0.0_AB_MSTR~DELL1` msg 2481 ran ONE `box-sync.sh` pass on demand on dell1 at 13:21Z (R1). It returned rc=0 and printed one KNOWN
standing line (ETFS_POSITIONING-S14, `/hazard_standing`) **as information**, then `RESULT 0 violations, 0 STANDING` and `box-sync: 0
standing`. It refused nothing, and `box/dell1` took CLOUD at 1520ae07ca and was pushed. **FWD-5: REALIZED.** Both arms are shown: a
standing defect printed, and the sync still completed.

**R7 / D1-S12 is already done:** `4.0.0_SA_CRO~A` added `org/git-author-override-audit.log` to box-sync's APPEND_ONLY union set
@6f91f8fafb. The 13:2xZ passes on dell1 and dell2 were both clean, which is the row's close condition (for the CVO to close).

**Coverage now: FWD-1 to FWD-7 are all REALIZED.** Round 3's five cells serve remediation rows, not outcomes. Its analysis is the close read.
