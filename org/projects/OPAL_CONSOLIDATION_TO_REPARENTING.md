# OPAL_CONSOLIDATION — TO Re-parenting Map

**Author:** 2.0.0_SA_COO, 2026-07-15 ~15:4xZ (the sec-8 execution surface).
**Authority:** Andrew ratification ~15:31Z (verbatim in OPAL_CONSOLIDATION_PRD.md sec-1) + the
CTO/COO confer (closed 152528Z). Master PRD v0.2 @ bf8f24728.

**Denominator (stated per Rule 22 retrieval discipline):** `.tools/to-check.py` scan 2026-07-15T15:41Z —
**15 open TOs under OPAL_ASSETS + 3 under OPAL_ASSETS_49METATABLES + 0 under OPAL_RUNNERS = 18 re-parented.**
(OPAL_RUNNERS carries no open TO files; its work rides the Andrew-ratified A-to-D build plan @ baba79230,
which remains authoritative for build ACs, cited from WS-C4.)

## Governance rules (how re-parenting works)

1. **TO files stay in place, unmodified** — they are REFERENCE POINTS: authoritative for their own ACs at
   granularity the master PRD does not restate (PRD sec-2). Status flips still record in the original file
   at close; the close evidence cites the WS-AC it satisfies.
2. **New TOs issue under `OPAL_CONSOLIDATION`** (workstream-prefixed: e.g. `OPAL_CONSOLIDATION.WS-A1.*`).
3. **Priority: P0 fabric-wide** — dispatch + staffing priority only; **no standing hold, gate bar, or
   sovereign carve-out is compressed** (PRD sec-6/sec-8). Latest + most-restrictive binds.
4. Rows marked SUBSTANTIVELY-COMPLETE below lag their file status; they close on evidence cited to the
   WS-AC, no new work.

## The map

| TO (file id) | Assignee | -> Workstream AC | Note |
|---|---|---|---|
| OPAL_ASSETS.V2-1.etf-channel-level-up | 0.5.0 | **WS-A2** | V2-1 GO re-arms on tonight's 22:00Z post-fix fire (COO-confirmed 230300Z) |
| OPAL_ASSETS.C4.etf-bronze-retarget-one-bucket | 0.5.0 | **WS-A1** | Guarded flip: complete ONLY on populated vendor-prefix listing (tonight's fire) |
| OPAL_ASSETS.C5.smartx-holdings-activity-etl | 0.5.0 | **WS-A3** | Builds 1-3 executing; feeds 8+9 on yaliu bundle (Andrew option-a) |
| OPAL_ASSETS.V2-2.schwab-channel-level-up-and-0824-completion | 0.6.2 | **WS-A1** | (b) grant closed @ v1.4.0; 0824 ratchet ~74%+ |
| OPAL_ASSETS.C3.0833-puller-one-bucket-landing | 0.6.2 | **WS-A1** | SUBSTANTIVELY-COMPLETE (C3(c) closed both masters); file status lags — close on evidence |
| OPAL_ASSETS.V2-7.silver-container | 0.7.0 | **WS-A2** | SUBSTANTIVELY-COMPLETE (applied live 09:5xZ 07-14, tag opal-assets-v0.7.0); close on evidence |
| OPAL_ASSETS.V2-9.silver-backfill-p2 | DS (+0.7.0 drain leg) | **WS-A1/A2** | Orion tail 57 units draining (4,583/4,640 @ 15:26Z); leg closes on 0.7.0's A4 drain manifest + CTO listing==4,640 |
| OPAL_ASSETS.V2-5.bronze-closeout-certificate | DS + 0.7.0 | **WS-A2** | Cert skeleton + 22a IAM-sweep half delivered; completes with the parity cert wave |
| OPAL_ASSETS.V2-8.silver-converters | DS + 0.6.2 (+0.5.0 smartx) | **WS-A2** | LIVE on all authored families; ETF family = WS-A4 (schemas pin on tonight's bytes) |
| OPAL_ASSETS.C6.silver-parser-registry | DS | **WS-A5** | External-gated leg (silver trigger-model ruling at CTO) |
| OPAL_ASSETS.C7.schwab-silver-conversion-scheduled | DS (+AE deploy hand) | **WS-A5** | External-gated leg |
| OPAL_ASSETS.C10.cottonwood-aua-cohort | DS | **WS-A5** | External-gated leg |
| OPAL_ASSETS.C11.emitter-one-bucket-only | DS | **WS-A5** | Staged (C3+C6) |
| OPAL_ASSETS.C12.legacy-prefix-inventory | DS | **WS-A5** | Doc-only leg |
| OPAL_ASSETS.P0-A (daily-AUM bucket skeleton) | 0.8.0_AE_CloudComp | **WS-A5** | STAFFING RULED (CTO 155711Z): ABSORB into the C11/emitter path; do NOT re-staff 0.8.0 pre-emptively -- decide at the wave that actually needs it, with the work in front of us |
| OPAL_ASSETS_49METATABLES.D1.bd-advisor-fee-dim-build | DS | **WS-B2** | THE LAST convergence finding (bridge proof on live data); P0 critical path to WS-C2 (arch session lock) |
| OPAL_ASSETS_49METATABLES.D1-CELL3.allocation-floor-parser | 0.7.0 | **WS-B2** (x-ref WS-A5) | RULED (CTO 163633Z): STAGE-NOW-SWAP-AFTER-TONIGHT -- parity path stays one-variable through the binding window; feeds D1. (Single authority = CTO; the prior 'tracked-behind-parity' note derived from his board language.) |
| OPAL_ASSETS_49METATABLES.D2.feed9-lane-rebadge | 0.5.0 | **WS-B (D2 tail)** | Thin wrapper; D2 findings delivered @ 826a44082; feed-8 question = WS-B1 (S2 sitting) |

## Not re-parented (deliberate)

- **WS-D (inf-AoR):** NO open TOs exist and none issue from this map — the WORK is covered in WS-D,
  but **LD-0277, the INF hold doc, and the stamp-order records stay STANDALONE-AUTHORITATIVE safety law**
  (the ratified law-vs-scope split, PRD sec-2/sec-6a). WS-D actions are event-gated on their own chain
  (fold-with-real-data -> lock; CVO~B re-spawn event-armed on the hold-lift; V4 = post-cutover re-take).
- **Inherited tails already homed in WS-C8** (SCHWABAUTO prod-repoint; BDAPIMIG closed-superseded 07-15
  on the 02:30Z scheduled-fire evidence; C9(b) manual-monthly cadence) — carried by the build plan, not TO files.
- **Other-project TOs** (ADVI_*, NFRA_*, delegate lanes) are OUT OF SCOPE — the supersede covers the three
  constituent bodies only.
