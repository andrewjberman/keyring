# IRPT_BCKEND: CVO adjudication, round 3 (workstream ~PO, the unlocated flat-key writer)

<sweep_watermark>2026-10-15T06:07Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T06:07Z, on msg 8123 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_3_PO_DRAIN_END_20261015.md` @e9fec793a0). One order, IB-pr-559 (READ of AWS for the daily Orion flat-key writer), complete, merged @e7837beeca, issued @14f2b2da5b on condition 1 of the signed Orion pairs packet. ~PO round 2 was compiled and slugged by this seat as ADJUDICATION_v103 @24ce59e4bf (slug 2026-10-15T05:03Z); ~P2's note that it is unslugged is stale. No judgment criterion. Re-run here at HEAD: IB202-1-AC1..AC3 PASS (exit 0). `round-close-check --round 3 --workstream "~PO"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE. The merge changes only the worker's record, criteria output, proof instance and the channel (git diff --name-only); no change-management entry names the chain or the Orion pull; the packet states every AWS call was describe, list, get, head or lookup. Nothing deployed.

**The finding that changes a SIGNED packet.** Both halves of the Orion pairs packet (sha256 c3dcc22f...19bc56b62) are now signed: COO @17172025c0, CTO @acaae0ff99. This round locates the writer the packet's pair (b) would replace: the `INF_API_PULL_TXN`, `INF_API_PULL_PERF` and `INF_API_PULL_POSITIONS_DAILY` steps of `chain:full` in `data/inf/scripts/gold/orion-gold-dispatch.sh` on the `inf-gold-layer-runner` EC2 (started by `inf-gold-trigger` about 11:32Z; PutObject at 11:40-11:52Z on 2026-10-14 by the runner's role session). Read here: the dispatch script names those steps (11 hits) and `convert_transactions_to_silver.py` and `convert_performance_to_silver.py` reference them (4 each), so the pulls feed the silver steps in the same run. Pair (b) as signed (port the CLI writes into a new handler, retire them) would either make two producers of each key or starve the silver steps (D2-W403-S3, ARMED). Condition 1 did its job: it stopped the release at the read. The signed bytes must not be executed; the issuer recommends a re-cut (re-time the existing chain trigger into the 06:00 fold, no new producer; pair (a) through the same chain steps). That re-cut is the CTO's call and needs both halves re-signed at new bytes.

**W396-S4 (7 transaction and 22 performance days missing):** NOT moved. Pair (a) still carries all 36 days by design; no day was pulled; only the proposed route for the re-pull changes (through the chain steps instead of a new handler), pending the CTO's re-cut. Cause still unread.

**IRPT_DASHBD-D2-S60's feed half (the Scope-group missing account, ABSENT NO_GROUP):** NOT moved. The Scope-account addendum is not cut and waits on B-IN's feed (CTO msgs 8110, 8112, which refine the classes: NO_START_DATE_AT_SOURCE measured per observed account, inferred otherwise; GROUP_NO_SERIES / NOT_DETERMINED for a group with no series). S60 stays ARMED with `~I2`.

3 rows dismissed below. HELD, owned: D2-W403-S3 (ARMED, `~P2`, the coupling to the gold chain; disarms on the CTO's re-cut), D2-S184 (superseded by the located writer, closes with the re-cut), D2-S186 (ARMED, `~P2`, its disposition record carrying the same re-cut), plus D2-W402-S3, D2-W394-S2, D2-W392-S2, W349-S1, W361-S1, W348-S2, W368-S2 (owner `~P2`), D2-S158 (owner the CTO).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S13",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T06:07:00Z",
  "one_line": "Round 3 ~PO. The daily Orion flat-key writer is located: the three INF_API_PULL steps of chain:full (orion-gold-dispatch.sh) on inf-gold-layer-runner, started by inf-gold-trigger at about 11:32Z; their outputs feed the silver transactions and performance steps. So the signed Orion pairs packet (both halves at c3dcc22f...) has a pair (b) that would double or starve the feed; condition 1 stopped it at the read; the re-cut and a re-sign are the CTO's. IB202-1-AC1..AC3 PASS re-run; read-only; nothing deployed. W396-S4 and S60's feed half are not moved. ~PO round 2 was already slugged (v103 @24ce59e4bf). Dismissed (3): D2-W403-S1 (the writer located and measured), D2-W403-S2 (PutObject data events exist only since the 2026-10-13 20:30Z selector; earlier days rest on the host's daily start), D2-W403-S4 (no StopInstances; SendCommand text hidden, verified through the chain log and script). Held: D2-W403-S3, D2-S184, D2-S186.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W403-S1",
   "IRPT_BCKEND-D2-W403-S2",
   "IRPT_BCKEND-D2-W403-S4"
  ],
  "spec_asserts": "Never-widen (CLAUDE.md section 5): a sign-off names the act's blast radius and covers both branches; an act whose world differs from the signed bytes does not land on those bytes. Spine L9/L10: every BLOCKING or ARMED row dispositioned before the slug.",
  "world_is": "A signed packet whose pair (b) no longer fits the measured world: the writer is the gold chain, not a stand-alone CLI. Nothing moved. The next act is the CTO's re-cut of pair (b) (re-time the existing chain into the 06:00 fold, or another shape) and re-signed halves at the new bytes; pair (a) and the Scope addendum follow. The 36 absent days and the Scope-group account remain open.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T06:0xZ of the invocations in IB-pr-559: IB202-1-AC1..3 PASS, exit 0",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 3 --workstream ~PO: orders=1 proof_ok=1 judgment=0 verdict=MAY-CLOSE",
    "git diff --name-only e7837beeca^1 e7837beeca: worker record, criteria output, proof instance, INVESTIGATION_v1.md only",
    "git log -S c3dcc22f...: COO half @17172025c0, CTO half SIGNED @acaae0ff99 (1.0.0_SA_CTO~DELL2, 2026-10-15T04:57Z)",
    "Grep INF_API_PULL_(POSITIONS_DAILY|TXN|PERF) under data/inf: orion-gold-dispatch.sh 11, convert_transactions_to_silver.py 4, convert_performance_to_silver.py 4, INF_C_07.advisor_attribution.py 1",
    "investigation rows D2-W403-S1..S4, D2-S184, D2-S186; IRPT_DASHBD-D2-S60",
    "org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/adjudications/ADJUDICATION_v103.md @24ce59e4bf (the ~PO round-2 slug)",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_3_PO_DRAIN_END_20261015.md @e9fec793a0 (msg 8123)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The located writer and two instrument limits, all read-only and recorded. The hazard the finding creates (a signed pair that no longer fits) is held on D2-W403-S3 with its owner for the CTO's re-cut."
 }
]
```
