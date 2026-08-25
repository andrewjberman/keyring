# 1.0.0_SA_CTO -- session 18:00-19:25Z: the PERFRP shape pinned from Andrew's recording; three 49F PRDs reviewed one-at-a-time and APPROVED; the Bloomberg law pointer landed after its target resolved; Andrew dictated D1's view tree, D3 onto ADVI, the ADVI partner-uniformity law and the pipeline census -- all recorded, four projects registered

**archetype:** COORDINATE
**secondary_archetypes:** SCRIBE, EXPLORE, VALIDATE

Continues `session_1510-1800Z_open_calls_rulings_49f_program_registered.md` (@7e52760e26). Andrew at the
terminal throughout, dictating; CRO off every 49F/ADVI subject by his ~16:1xZ word.

## 1. ADVI_PERFRP shape PINNED (v0.2 @7864960ed1) -- from two HARs + 13 screenshots
Inputs kept LOCAL (HARs carry tokens, gitignored; screenshots carry client PII; paths only in the repo).
Two BD surfaces map to two of ours (Advisor BI dashboard -> Book view + Books L2; Client View portfolio
dashboard -> Books L3/L4); the per-period figure keys of /portfolioreporting/api/* map near one-to-one
onto the ratified daily account fact; s.6 rectangle with HAVE / BUILD / GAP / DEFERRED dispositions; s.8
candidate cells B1-B9 / F1-F6; run P1-P16. Committed after MSTR's merge-window CLOSE (both fabrics at
parity e97c6673c8 -- their A4/A4.1 script landed on site Z the same window).

## 2. One-at-a-time PRD review with Andrew (his method: breakdown, /draw, ambiguity cards with recs)
- ADVI_INSURE v0.2 @ee2c15686f -- "Agreed with all recs this one is good to go" (10 rulings, s.11:
  in-grammar prefix, both source modes, bd_account_id key, NO class-axis change -> a new Total Assets
  element, header subtext form, v1 fields, daily idempotent pull, DEV from QA emission, pattern note,
  owners).
- ADVI_STITCH v0.2 @1d3fd19511 -- his item-1 word fixes the landing grammar: bronze_legacy/ +
  silver_legacy/ (unmistakably distinct from live tiers); items 2-3 approved; all others approved
  (xref = key of record; R1-R4 rule skeleton; census-first; UNKNOWN(elsewhere-candidate) until
  Fidelity; two labelled SI segments; Phase A now, Phase B later).
- ADVI_PERFRP v0.3 @17710c4640 -- "approved all" (14 rulings, s.11: v1 card set, periods, groupings,
  Book view, Gain/Loss last, paged transactions, in-Books panels, CSV v1, BD footnotes, SI from the
  floor, PROD rides the switch promote, parity on first emission, method extensions never asked of
  the contract's author, owners).

## 3. The Bloomberg law pointer -- doc first, pointer second (@7216cd9836, ON origin)
MSTR flagged (66279) that MSTR~Z's target integrations/bloomberg/READ_HERE.md existed only on
origin/SITEZ; I gave the merge word (SITEZ->CLOUD @cdca350eac, zero deploy), verified the target resolves
at my seat with a negative control, then landed the CLAUDE.md line (three things not to re-derive +
do-not-mint data/bloomberg/). MSTR's corrected merge-window rule (announce on COLLISIONS, not duration)
and the generalised pointer rule (a pointer lands after its target resolves on the READER'S fabric) are
carried.

## 4. Laptop directive state + dependency order delivered (D0/D1/D2/D3/D5); Andrew: "This all looks good"

## 5. Andrew's dictation (each recorded VERBATIM in its own file; broadcast same turn; not to CRO)
- D1 view tree (~18:5xZ) @90bdc913ef: L0 {Client, Models, SMAs, Alternatives} (Insurance out -- no
  fees); Client L1 Supervised/Unsupervised = fee-taking; Models L1 Primary {UST ST INT LT ULT} / Custom
  (L2); SMAs L1 {Tax, Muni, DIVZ, PFOE} open; Alternatives deferred -> D1 PRD s.8.6 + run RV1; the CVO
  cert @d2706b2849 marked SUPERSEDED-PENDING-ABSORPTION on the D1 JSON @633360c6b2 (MSTR 66298 flag).
- D3 onto ADVI (~19:0xZ) @90bdc913ef -> PRD v1.1 s.4b @b85c472767: the per-partner models plane
  MEASURED (49F + Inflection daily on the MDPF feeder contract model_aua_positions at account grain;
  Cottonwood NOT on it -- BD-side fact_model_assignment + dim_model_portfolio); four-level additive
  runner contract; Books placement; run rows #14-#18. Breakdown/draw/cards -> "all recs approved"
  -> s.4c rulings @5194584763; D3_MODELOVERLAY.json minted (register gap).
- ADVI partner uniformity (~19:1xZ) @5194584763: INSURE ports to Cottonwood (PORT MEANS RE-INSTANTIATE,
  NEVER REFERENCE -- MSTR 66306 explicitness taken); PERFRP binds all three (ONE IMPLEMENTATION, THREE
  FIRM-PINNED INVOCATIONS); Tier A 49F / Tier B Inflection = Cottonwood + insurance option by partner
  fact -> D2 PRD s.11; Cottonwood keying investigation -> ADVI_COTKEY REGISTERED.
- Pipeline census (~19:2xZ) @5194584763: DATA_PIPMAP REGISTERED -- {ADVI, MDPF} x {49F, INF, COT} x
  code/data/trigger/served/IAM on Rule 22a's layers; proposals only. First cell (MSTR 66312, one cell,
  labelled): Cottonwood MDPF code home = a DECLARED per-firm deploy destination
  (opal-data-mdpf/code/scripts/assets_gold/) over an in-pattern shared repo home
  (data/assets/scripts/gold) -- the inverse of his suspicion; a design to evaluate, not a drift.

## MCP traffic
Sent 16 (broadcasts of five Andrew-direct records; law-edit broadcast; push pings; merge word; ACKs).
Received 9 significant from MSTR (66263/66267 merge window; 66279/66281/66298 pointer sequence;
66285 rule correction; 66306 explicitness; 66312 census datum) -- all READ-acked and acted on.

## Compiler Tools
| tool | invocation | result |
|---|---|---|
| comp-pipescript io | build_mdpf_spine.py / mdpf_gold_consolidator.py --pipeline mdpf | PASS (dynamic-key warning honest; fact_model_assignment surfaced) |
| comp-pipescript deployed | all-trees sweep | RUNNING in background (b3tlxs1c8) -- not quoted |
| comp-find -i / --name | prior-art censuses (insurance, session/token, frontend surfaces, radial/pie, EXACT_JOIN spec) | PASS; measured zeros stated with denominators |
| HAR parse (python, sanitized) | endpoint census, enum vocab, response key shapes -- no headers/cookies/bodies retained | PASS |
| raw s3api / s3 ls (rail-checked) | MDPF feeds presence; smartx silver tables; portal/gold/mdpf tables | PASS -- presence only; one HUD gate hit re-run with the marker |
| safe-commit -F | x10 this window | PASS (risk-reflex WARN read on the CLAUDE.md edit) |
| agentbus | (none this window) | -- |

What failed: nothing. Gap: the deployed sweep exceeds the 240s tool budget (backgrounded; result pending).

## Blockers
**None at this seat.** At Andrew: DATA_PIPMAP's directive home (D0 rec); the D1 per-partner
composition rulesets (offered); who cuts the TOs (COO on spawn vs CTO); the spawn order. Register edits
at MSTR: D3 += D3_MODELOVERLAY, D2 += ADVI_COTKEY, D0 += DATA_PIPMAP (pending his word).

## Current State -- for a reader with zero context
Fabric: MSTR, CRO, CTO live; all lanes + COO + CVO closed-out; site Z on the ETFs directive today (leg
1a derived layer landed). 49F program (D2): ADVI_INSURE v0.2 / ADVI_STITCH v0.2 / ADVI_PERFRP v0.3 all
APPROVED FOR STAGE 3 with rulings tables; ADVI_49FSRC parked; ADVI_COTKEY registered; the uniformity law
in D2 PRD s.11. D3_MODELOVERLAY v1.1 approved (JSON minted). D1_CATVIEWS: view tree ruled (s.8.6); cert
superseded-pending-absorption. DATA_PIPMAP registered. CLAUDE.md Bloomberg pointer ON origin. Push
state: 5194584763 LOCAL (1 ahead of 633360c6b2); MSTR pinged.

## Next Steps
- **[Andrew]** the three words above; next PRD dictation or the cut.
- **[0.0.0_AB_MSTR]** push 5194584763 + this log; the three register edits; spawns on his word.
- **[2.0.0_SA_COO on spawn]** D1 absorb-then-recert; INSURE / STITCH-A / PERFRP / D3 / PIPMAP decomps;
  COTKEY stage-2 PRD is CTO's first.
- **[1.0.0_SA_CTO]** ADVI_COTKEY + DATA_PIPMAP stage-2 PRDs (census matrices as runs); read the
  backgrounded sweep when it returns.
