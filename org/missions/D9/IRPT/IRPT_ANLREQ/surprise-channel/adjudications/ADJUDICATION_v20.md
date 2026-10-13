# IRPT_ANLREQ: CVO adjudication, round 19 (workstreams Y and YR)

<sweep_watermark>2026-10-13T07:14Z</sweep_watermark>

L8 compile and L9 grades by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T07:14:00Z, on msg 6836 (`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND19_Y_L8_COMPILE_20261013.md`). The template reader's release is LIVE in both legs,
and this seat read the Lambda's digest. **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_19_L9_GRADE_20261013.md`): the 13 AC2J criteria PASS on a sampled read; **AR194-y-AC4J FAILS** clause 1 (the
r19.1 backstop turns back one-account files with abbreviated attribute headers holding 8+-digit integers or security ids; built, not
released); AR200-y-AC1's re-grade is accepted.
53 rows dismissed below; 6 graduate in `remediations/REMEDIATION_v12.md`, 3 ARMED.

```json
[
 {
  "id": "IRPT_ANLREQ-C-S20",
  "project": "IRPT_ANLREQ",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T07:14:00Z",
  "one_line": "Dismissed: Round 19 (Y, YR). Disarmed on the issuer's records and closed: D2-S66, D2-W56-S2, D2-W57-S1, D2-W57-S2 (by D2-S67: the Lambda release re-cut on the live package; the portal's readers return the deployed first answer), D2-W51-S13, D2-W51-S16, D2-W52-S37, D2-W55-S15, D2-W55-S16, D2-W55-S19, D2-W55-S27, and REMEDIATION_v10/v11's D2-W52-S29 and D2-W52-S35 (by D2-S68: the reader's release landed in both legs in the signed order, and TO-READS-Y10 counts 0 stored templates turned back), with this seat's live digest read beside them. D2-W55-S26 and D2-W55-S4/-S12 (BLOCKING, INERT: an accepted named limit, and builder gaps answered by the recovered st32 recipe, AR-y-199). The rest are worker readings stated in their records (premises corrected, pins re-found, install modes, recipe details), and the records D2-S67 and D2-S68. Workstream YS's rows wait for YS's packet.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_ANLREQ-D2-S66",
   "IRPT_ANLREQ-D2-S67",
   "IRPT_ANLREQ-D2-S68",
   "IRPT_ANLREQ-D2-W51-S12",
   "IRPT_ANLREQ-D2-W51-S13",
   "IRPT_ANLREQ-D2-W51-S14",
   "IRPT_ANLREQ-D2-W51-S15",
   "IRPT_ANLREQ-D2-W51-S16",
   "IRPT_ANLREQ-D2-W51-S17",
   "IRPT_ANLREQ-D2-W51-S18",
   "IRPT_ANLREQ-D2-W51-S19",
   "IRPT_ANLREQ-D2-W51-S20",
   "IRPT_ANLREQ-D2-W51-S21",
   "IRPT_ANLREQ-D2-W51-S22",
   "IRPT_ANLREQ-D2-W51-S23",
   "IRPT_ANLREQ-D2-W52-S37",
   "IRPT_ANLREQ-D2-W54-S13",
   "IRPT_ANLREQ-D2-W54-S14",
   "IRPT_ANLREQ-D2-W54-S15",
   "IRPT_ANLREQ-D2-W55-S10",
   "IRPT_ANLREQ-D2-W55-S11",
   "IRPT_ANLREQ-D2-W55-S12",
   "IRPT_ANLREQ-D2-W55-S13",
   "IRPT_ANLREQ-D2-W55-S14",
   "IRPT_ANLREQ-D2-W55-S15",
   "IRPT_ANLREQ-D2-W55-S16",
   "IRPT_ANLREQ-D2-W55-S17",
   "IRPT_ANLREQ-D2-W55-S18",
   "IRPT_ANLREQ-D2-W55-S19",
   "IRPT_ANLREQ-D2-W55-S20",
   "IRPT_ANLREQ-D2-W55-S21",
   "IRPT_ANLREQ-D2-W55-S22",
   "IRPT_ANLREQ-D2-W55-S23",
   "IRPT_ANLREQ-D2-W55-S24",
   "IRPT_ANLREQ-D2-W55-S26",
   "IRPT_ANLREQ-D2-W55-S27",
   "IRPT_ANLREQ-D2-W55-S4",
   "IRPT_ANLREQ-D2-W55-S6",
   "IRPT_ANLREQ-D2-W55-S7",
   "IRPT_ANLREQ-D2-W55-S8",
   "IRPT_ANLREQ-D2-W55-S9",
   "IRPT_ANLREQ-D2-W56-S1",
   "IRPT_ANLREQ-D2-W56-S2",
   "IRPT_ANLREQ-D2-W57-S1",
   "IRPT_ANLREQ-D2-W57-S2",
   "IRPT_ANLREQ-D2-W57-S3",
   "IRPT_ANLREQ-D2-W57-S4",
   "IRPT_ANLREQ-D2-W57-S6",
   "IRPT_ANLREQ-D2-W58-S1",
   "IRPT_ANLREQ-D2-W58-S2",
   "IRPT_ANLREQ-D2-W58-S3",
   "IRPT_ANLREQ-D2-W52-S29",
   "IRPT_ANLREQ-D2-W52-S35"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and judgment criteria are graded at L9, never self-graded.",
  "world_is": "Every round-19 order is terminal (to-check.py --project IRPT_ANLREQ --all: 0 active at 07:08Z). The reader release is live in both legs. L9: the 13 AC2J criteria PASS on a sampled read (4 records read by this seat), AR194-y-AC4J FAILS clause 1, and AR200-y-AC1's re-grade is accepted.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S66, D2-S67, D2-S68, D2-W51-S12, D2-W51-S13, D2-W51-S14, D2-W51-S15, D2-W51-S16, D2-W51-S17, D2-W51-S18, D2-W51-S19, D2-W51-S20, D2-W51-S21, D2-W51-S22, D2-W51-S23, D2-W52-S37, D2-W54-S13, D2-W54-S14, D2-W54-S15, D2-W55-S10, D2-W55-S11, D2-W55-S12, D2-W55-S13, D2-W55-S14, D2-W55-S15, D2-W55-S16, D2-W55-S17, D2-W55-S18, D2-W55-S19, D2-W55-S20, D2-W55-S21, D2-W55-S22, D2-W55-S23, D2-W55-S24, D2-W55-S26, D2-W55-S27, D2-W55-S4, D2-W55-S6, D2-W55-S7, D2-W55-S8, D2-W55-S9, D2-W56-S1, D2-W56-S2, D2-W57-S1, D2-W57-S2, D2-W57-S3, D2-W57-S4, D2-W57-S6, D2-W58-S1, D2-W58-S2, D2-W58-S3, D2-W52-S29, D2-W52-S35",
    "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND19_Y_L8_COMPILE_20261013.md (041902e33e, msg 6836)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_19_L9_GRADE_20261013.md",
    "this seat's live read 2026-10-13T07:06Z: irpt-ycharts-generate CodeSha256 bNPCG2Oe1oQM/ztjggmrdDbdl83CAmUEcPnBFxlj2Rk= (06:27:22Z, Successful); since 06:27Z Traceback 0, ImportError 0, TypeError 0, 1 invocation"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disarmed on the owner's records with this seat's live read, accepted limits, and worker readings."
 }
]
```
