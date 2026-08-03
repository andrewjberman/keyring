# MDLP_MONPUB closed complete in one day; RCG grant landed; the surgical drive staged

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE, SCRIBE

Continues `w8_w9_battery_complete_velocity_suspension_1600-1705Z.md`. Window 1705-1815Z.

## The closing arc

- **Andrew-direct (~1705Z, my terminal, verbatim in spec 5b):** Yang removed the offending
  "Short Term" portfolio from Bloomberg — race inherently solved at source; rollback/caching/
  monotonicity work CONTINUED THROUGH FIX. **W7 stood down unordered** (compensator
  justification gone). Broadcast to MSTR/COO/CVO.
- **W6 shipped + PROMOTED TO PROD** (portal-v2.1.155, CI-verified): 29-prefix scoped
  invalidation, 13/13 mechanical battery (control [B] sub-prefix scoping = the strongest FE
  acceptance evidence of the day), PLUS the bonus defect — every successful version-based
  rollback rendered as "Rollback was not started" FAILURE (FE required an execution id that
  path never returns) and the failure toast advised the exact cache-rehydrating action. The
  07-31 experience is now fully explained: three compounding UI failures hid a working system.
  Promote sequenced by me (DT sole authority); I verified PROD directly (c6f561b6).
- **W8 witnessed complete** (@624a24c4a3): 3 legs incl. the :146 manifest-arm discriminating
  condition. **The stamp location is LOAD-BEARING** (CVO live-ASL grounding, spec 5b): the SFN
  Parameters top-level whitelist silently drops an event-level force_publish in orchestrated
  mode — a refactor hazard now on permanent record.
- **W5 exercised LIVE on Andrew's direct question** — CVO invoked the production Lambda rather
  than citing the deploy: exec-5a4149176fb6 PRESENT, 25 items time-ordered.
- **W9/W9b closed**: /api/general/* -> 300s policy (custom, managed immutable), advisor-by-firm
  -> 60s aligned to the router stamp (verdict (a); 86400 was dead config on the designed path,
  a trap on any unstamped one — ~F's line). Firm-isolation cache-key params verified intact.
  Denominator self-correction 5->4 (recalled vs measured) banked. Neither injector nor router
  is load-bearing for TTL on the JSON serving path anymore. Dual-regime authenticated header
  proof rode DT's deployed-page pass (Age 81/82 <300; Age 20 <60).
- **Andrew-direct closeout (~1750Z, COO terminal, verbatim in JSON):** visual smoke passes;
  project **CLOSED COMPLETE @dc2826c11c** — 2-step atomic, all 8 TOs evidence-chained. One
  correction I caught: W8's completion understated (witness landed 18 min BEFORE the stamp);
  corrected @2ad3477648 with the why annotated. **Understatement is the same drift class as
  overstatement, pointed the other way.** Live-occasion legs (W6-full + W8-traversal) ride the
  next genuine rollback, COO-tracked, non-blocking.

## RCG staging (Andrew-direct sequence, spec 5c)

- **Grant landed @56ef220877, me as GRANTOR on Andrew's explicit word:** lane RCG_OPERATOR
  (4.0.0_SA_CRO ALONE — deliberately narrower than CRO_WORKSPACE: the folder contract is the
  point, exec write access would dilute it; build-lane staffing arrives as a NEW arch-gated
  amendment) + path rule rcg/** (root enumeration principle). Validator 54/222 OK; positive +
  negative membership controls PASS. SoD held.
- **Ferry answer to CRO:** PRD landing + VELOCITY On-Hold records already done; gate wiring +
  sweep-mechanics ruling deliberately HELD for the drive (P0 step 1 in-sequence, the gate's
  both-directions exercise as first acceptance).
- **RCG PRD read end-to-end**; drive plan staged. Entry gate = Andrew: spec GO + two defaults
  (git rm vs archive-move; folder name) + review cadence. P0 = rcg/ skeleton + MANIFEST gate
  exercised both directions; P1 = engine + cycle-0 comp-tools dependency map (doubles as the
  registry-generation adjudication) + first honest census of 25,273 tracked files.

## Compiler Tools

| tool | result | note |
|---|---|---|
| `git -C portal log origin/PROD` (live fetch) | PASS | promote verified on the branch, not from a report |
| `.tools/owned-paths-validate.py` | PASS 54 lanes/222 rules | + hand-rolled positive/negative membership controls on the new lane |
| `python json/yaml reads` (project close state) | PASS | atomic-close verification |
| comp-* not otherwise run | — | window was closeout coordination; grounding was live git/AWS/file reads |

## Current State / Next Steps

- MDLP_MONPUB: CLOSED COMPLETE AND ACCURATE. Outside-scope tracks continue (~B instrument TOs
  on spawn; CF instrument gaps in CVO register; live-occasion legs COO-tracked).
- [ANDREW] tier-2 seat closeout (in progress, logs being taken) -> then: RCG spec GO + two
  defaults + cadence. Parked non-blocking: ETFS AVGCAP confirmation, Orion
  normalization/restatement decisions, C3L.1.
- [1.0.0_SA_CTO] drive RCG P0 on his word.
