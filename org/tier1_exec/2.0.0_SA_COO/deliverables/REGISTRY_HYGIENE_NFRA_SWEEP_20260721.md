# Registry-Hygiene Sweep -- NFRA macro (2026-07-21)

**Lane:** 2.0.0_SA_COO~A (Andrew-direct registry-hygiene AUDIT lane; MSTR brief 20260721T154847Z). OPAL done first (@f84733697).
**Instrument gate:** `comp-state --self-test` = PASS 3/3.
**Grounding bar (Rule 22, HARD):** a close/TO-flip is a real state change -> grounded on commits + TO status + served artifacts, never the registry's own say-so. UNCERTAIN/non-obvious -> FLAG, don't act.
**Enumeration:** 63 NFRA_* project JSONs; **all 63 parse clean.** Owner/phase-less records (LIVELEARN, some COMP*) use lean schemas by design -- NOT defects.

## Edit made this pass (1)
- **NFRA_GCONTR -> SUSPENDED-INDEFINITE** (committed @8373263bc): status `on-hold`->`suspended-indefinite` (Andrew-direct sovereign 2026-07-20 ~14:35 ET, verbatim in suspend_directive: *"...rendered as indefinite/suspended i do not want to fucking hear about it again"*); the 2 still-PENDING TOs (COO `closeout.ratify-rows` + CVO `TO-3`) marked `cancelled-suspended` per the record's own "DROPPED-as-suspended"; TO-2/4/5 were already complete. Project + all its TOs now reflect the suspension; nothing re-surfaces. (These 2 were the sweep-brief's named pre-existing COO/CVO TOs -- handled AS the sweep.)

## FINDING A -- "complete" projects carrying open-classified TOs (17): mostly instrument artifact + some real stale-staged remnants -> FLAG, do NOT bulk-flip
17 NFRA projects statused **complete** show open (ACTIVE/PENDING) TOs in `/to-check`:
COMPAWS(2), COMPILERKIT(3), COMPPROOF(2), COMPRAIL(1), COMPROUTE(3), COMPUNIFY(5), DEBTSCAN(3), GLOBGRPH(3), GRAPHDEPTH(2), GRAPHUNI(6), INFRPT(2), INTEGRATIONS(2), MOTIF(4), PROMOTE(3), SEMCTL(2), SYSTEM(5), TSGRAPH(2).

**Ground-truth on 2 heaviest (COMPUNIFY, GRAPHUNI): the count is inflated by TWO causes, only one of which is real drift:**
- **(1) to-check classifier artifact (NOT drift):** COMPUNIFY S0/S1/S2/S3 carry `<status>PASS -- ...</status>` / `<status>DELIVERED, ...</status>` -- the work IS done (CTO arch-gate PASS, committed artifacts cited in-status), but `PASS`/`DELIVERED`/`dispatched`/`staged` are absent from `.tools/to-check.py:47` COMPLETE_WORDS, so they mis-classify as active. Records are fine; the tool over-counts. (See INSTRUMENT FINDING below.)
- **(2) genuine stale-staged remnants (real drift):** GRAPHUNI completed its P2/P3 via a **consolidated** TO (`P2-P3.repoint-onto-marker-head-and-retire` = complete) but the OLD granular `P2.shared-readapi-repoint` / `P3.retire-and-d4-assert` / `V1.cvo-acceptance` / `SFNBRIDGE` are still `staged`. Those granular staged TOs are superseded remnants.

**WHY I DID NOT bulk-close them:** GRAPHUNI also has `P1.d1-fill-derive` (staged, "single-gated on CVO fixture-lock") + `V1.cvo-acceptance` (staged) -- resolving whether those are *superseded* vs *genuinely-open* needs owner commit/served-graph grounding I can't do from an audit lane. And **NFRA_TOOLHEALTH's own record is the cautionary precedent**: it was *"flipped status=complete while its blocking field read [not done]"* and had to be REOPENED. Bulk-flipping stale-staged TOs on a "complete" project risks either hiding a real open phase or repeating that premature-close error.
**REC (-> owning lanes 0.8.0_AE_CloudComp / CTO / CVO):** run a grounded TO-closeout across these 17 -- for each open-classified TO, ground the deliverable against commits/served artifacts; mark done ones complete, superseded remnants `superseded`, and if a genuinely-open TO surfaces, the PROJECT status is what's wrong, not the TO. Low-harm (stale-open TOs are noise, not a served-data risk), so appropriate as an owner batch, not an audit-lane guess.

## FINDING B -- close candidates (older-active / near-terminal), FLAG with evidence
| Project | Status | Age | Evidence it may be done | Open TOs | Rec |
|---|---|---|---|---|---|
| NFRA_COSTAWS | active | 36d | "R2 noncurrent-tighten COMPLETE 06-11; all 9 buckets APPLIED + SERVED-VERIFIED at 14d (Andrew GO)" | 3 ACTIVE | Owner verify 3 TOs vs live S3 lifecycle -> close if done |
| NFRA_GRAPHS | active | 34d | "D7 COMPLETE 06-12, AC7 met, 0 SEV1" | 4 ACTIVE | Owner ground the 4 TOs -> close if done |
| NFRA_GENESIS | active | 2d | "P0-P5 (in-scope) COMPLETE + EXERCISED (Andrew plan-approved 07-18)" | 0 | Recent -- likely wrapping; owner confirm in-scope close |
| NFRA_LOCALROOT | active | 12d | "Phase 3 SUBSTANTIVELY COMPLETE 07-09" | 1 UNKNOWN | Resolve the 1 UNKNOWN-status TO; then close-eligible |
| NFRA_OPLMCP | build-complete | 25d | "BUILD COMPLETE 06-24, all 4 legs DONE, Andrew-de-prioritized (NOT fabric-work)" | 3A+1P (gateway `.08` redirected to ~Z) | Status already accurate; gateway follow-on is genuine open work -> LEAVE build-complete |
I did **not** close any: each carries open TOs and/or needs live-infra grounding beyond an audit lane; the grounding bar + TOOLHEALTH precedent make owner-verify the right path.

## FINDING C -- active projects, real work remains -> LEAVE ACTIVE (one-line remaining)
- **NFRA_AGENTBUS** (3d): Port-2 intra-Andrew-device inter-site trunk in build. | **NFRA_COMPASSURANCE** (7d): comp-which top-k redesign (PRD-2). | **NFRA_COMPLEARN** (10d): REOPENED 07-10, loop-closure amendment (1A+8P TOs). | **NFRA_COMPSIMILAR** (1d): PH1 store-writer gate closed 07-18, ongoing. | **NFRA_COMPTEAM** (13d): A1/B1 closed, B2 remaining. | **NFRA_EDGES** (12d): P1 closed, downstream phases (3 TOs). | **NFRA_GRAPHFEED** (5d): wave dispatched to 0.8.0_AE_CloudComp~Z (6-TO list). | **NFRA_INSTDRILL** (7d): EXECUTING (CTO~Z). | **NFRA_KUZUSPLIT** (3d): P0 delivered 07-17, downstream (1A+1P). | **NFRA_LIVELEARN** (8d): Andrew-direct finalize quality-sensor loop; lean schema, 0 TOs. | **NFRA_MSGRAPH** (5d): S1 complete, ongoing (1A+1P). | **NFRA_NERVES** (7d): L2/L3 shipped, L1/L4 lane-split live. | **NFRA_NESTEDABSTRACT** (1d): P1 settled, loop machine live. | **NFRA_ONTOLOGY** (1d): ratify chain canonized 07-19 (1 TO). | **NFRA_PASSCRAFT** (10d): Phase-0 PRD, 4 staged TOs. | **NFRA_SYSPARITY** (1d): Andrew-direct 07-20 "SYSPARITY is ongoing" -- explicitly active, CVO work outstanding. | **NFRA_TERRAFORM** (11d): Phase-2 remediation GO'd (2 TOs). | **NFRA_TOOLCHECK** (3d): P4 final /seams+/verify sweep. | **NFRA_TOOLGRAPH** (10d): Phase-0 PRD, 3 staged TOs. | **NFRA_TOOLHEALTH** (11d): correctly REOPENED after a premature close -- active. | **NFRA_WEBSITE** (6d): opalinvest.com cutover (1 TO; note CLAUDE.md opalcapital.com prohibition context). | **NFRA_WRKFLW** (27d): Phase-0 PRD/design, old but not abandoned (1 TO).

## FINDING D -- special statuses
- **NFRA_CMTQUE** (on-hold, 7d): TO-4/TO-5F complete; 1 genuine open TO (TO-6R load-test RUN + phased cutover -> AE_CloudOps~B + MSTR + CVO~B) = the gated resumption item. LEAVE on-hold; not audit-lane's to drive.
- **NFRA_EXPAND** (scoping, 25d): a post-carve-out shell -- the MS vertical was elevated out to NFRA_MSGRAPH + EXPAND_MSCLOUD (Andrew-direct 06-26). **FLAG:** confirm residual scope exists or supersede/close; `superseded_by`/carve-out links are not in the structured fields.
- **NFRA_PPL49F / PPLCOT / PPLINF** (dormant, 18d): Phase-0 registered+staged 07-02 (pipeline-audit projects, never started). `dormant` is accurate. LEAVE.

## INSTRUMENT FINDING (for the to-check / comp-tool owner)
`.tools/to-check.py` COMPLETE_WORDS (`:47`) lacks `pass`, `delivered`, `dispatched`, `staged`, `accepted` -> a TO with `<status>PASS -- <evidence>...</status>` counts as ACTIVE. This structurally inflates the open-TO count on already-complete projects (the whole of FINDING-A cause #1). Not a record defect; a classifier gap. Recommend the to-check owner extend COMPLETE_WORDS (or add a "verbose-terminal-status" recognizer) so the drift linter stops crying wolf on done work.

## Net
- **Registration:** 63/63 parse clean; lean-schema records are not defects.
- **Edits:** 1 project + 2 TOs (GCONTR suspension) -- grounded, Andrew-direct-authorized.
- **Closes:** 0 -- close candidates carry open TOs / need live-infra grounding; grounding bar + TOOLHEALTH precedent -> owner-verify, not audit-lane close.
- **Flags:** FINDING-A (17-project TO drift, owner closeout), FINDING-B (5 close candidates), EXPAND residual-scope, + 1 instrument finding.
- **Orphan TO-prefixes w/ NO project JSON anywhere:** NFRA_ALERTSUB, NFRA_GRAPHEXT, NFRA_LAMBDAMAP -- surfaced for owner (register the project or retire the stray TOs). (NFRA_SCTY / NFRA_SCTY_PREMCP TOs are NOT orphans: they map to the SCTY-macro projects SCTY.json / SCTY_PREMCP.json -- a TO-prefix mislabel, and SCTY is a separate macro outside this NFRA sweep.)
