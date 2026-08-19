# THE 49F END-TO-END PUSH -- staffing, phase plan, handoffs (CTO, 2026-08-18 ~1505Z)

> **⚠ AMENDED 2026-08-19 ~15:3xZ (Andrew-direct): §3's R-anchored calendar is SUPERSEDED by §6
> (the FRIDAY COMPRESSION -- fam declared-stale decouple, Wed/Thu/Fri dates) and §7 (the BLACK
> DIAMOND PARITY PROGRAM) below. Read §6/§7 before acting on any §3 date.**

**Authority:** Andrew-direct ~1500Z at the CTO terminal (verbatim record: `ANDREW_DIRECT_20260818_ALL_RECS_APPROVED_49F_END_TO_END_PUSH_AND_MDPF_UNUSED_DELETE.md`, same folder): *"I reallly want to make a major push on 49 as the test case for the end to end push ... a dedicated session ... which will be now, so let's decide who we need on it, and put the whole fabric on the case with the adequate handoffs."* Program: `OPAL_ADVIPOINTERS` (owner CTO). Product/account: **Advisor Intelligence, 49 Financial, Schwab 08335338** -- never "49F" alone (naming law, pattern spec §6).
**Roles (unchanged law):** CTO = architecture + phase-close ATTESTATION + per-apply gates · COO = decomposition into DATED TOs with proof-of-spec contracts, validation · MSTR = spawn/seat, integrate/push, carries Andrew · CVO = certs (two-phase pins, parity bar SS8, Rule 14e) · CRO = the GIPS field contract owner (`ADVI_PERFORMANCE`) + P5 methodology, consulted · lanes execute.
**Spawn constraint (MSTR 150129Z, adopted):** `0.4.0_DS_ClientPlatform` base is DOUBLE-BOOKED (bd platinum acceptance 23:01Z tonight; MDPF_PROVENANCE T-B 08-19) and takes NO third thread; the 23:01Z restore verify is a HARD FIXTURE and is *phase zero of this same product*.

---

## 1. WHAT "END-TO-END" MEANS FOR 49F (the five phases, applied to one firm)

```
 opal-data-assets/schwab/08335338/{bronze,silver}   (landing daily ~12:18Z -- HEALTHY, canonical grammar)
        |  P2: a SCHEDULE FLOOR after silver lands (+ silver-completeness event as accelerator)
        v
 data/assets/scripts/gold/runners_49f/  a00..a07 dims -> b00..b03 valuation -> c00..c04 flows/NNA/TWR -> (P1 built)
        |  writes PARQUET + manifest per table per date  (P3 root, live 08-12 copy, 526 partitions to 08-10)
        v
 opal-data-assets/portal/gold/advi/49financial/{canonical,dimensions}/{table}/date={D}/data.parquet
        |  P4: the D fleet (d01..d14 + d_publisher_base) is THE ADVI PUBLISHER -- parquet in, served-shape JSON out,
        |      the estate's only JSON producer for these keys; two-phase pin per key vs the legacy serve
        v
 opal-data-portal-v2/platinum/advi/49financial/{key}.json        (EMPTY today)
        |  P4: portal firm-config repoint per key (DE), tolerant read -> flip -> DT PROD promote
        v
 portal (Advisor Intelligence, 15 architect advisors)   -- verified TAKING DATA IN and DISPLAYING IT
        |
        v  P5: legacy bd chain stages that produced the flipped keys retire (consumers first, binary last, Rule 25)
 opal-data-bd/{gold,platinum}/*  (the LEGACY producer -- runs 04:42Z daily; restored today; retires LAST)
```

**Production bar (unchanged, framework §):** a family is PRODUCTION only when (i) every dim comes from a SCHEDULED producer with no session-local input, (ii) one producer per key, (iii) canonical grammar on the canonical plane, (iv) a declared consumer reads the serving path. Today 49F fails (i) and (iv).

---

## 2. THE ROSTER (who, on what, spawn-onto-a-TO)

| seat | state | on the push |
|---|---|---|
| `1.0.0_SA_CTO` | LIVE | arch owner; attests P1/P2/P3/P4/P5 closes for 49F; per-apply gates (schedule TF, IAM, teardown); rules host/route questions same-hour |
| `2.0.0_SA_COO` | LIVE | issues every TO below DATED with proof-of-spec contracts (criterion-ids minted at decomposition); validates proofs; owns the ledger of dated items (§5) |
| `0.0.0_AB_MSTR` | LIVE | spawns the six dark seats onto their TOs; integrates/pushes; carries the backfill priced card + the ADVI_PERFORMANCE §15 confirmations to the record |
| `0.7.0_AE_CloudOps` | LIVE (bd platinum, free after 23:01Z acceptance) | **P2** schedule floor + event accelerator (TF, per ratified spec `org/tier1_exec/4.0.0_SA_CRO/deliverables/P2_UNIFIED_MORNING_SCHEDULE_TIMING_MAP_SPEC_20260811.md`); **P4** publisher IAM (Put scoped to `platinum/advi/49financial/*` only) + publisher schedule; **P5** teardown applies + TO-4 mdpf deletes (authorized) |
| `0.4.0_DS_ClientPlatform` (base) | LIVE, DOUBLE-BOOKED | NOT on the push. 23:01Z restore -> T-B 08-19 (FLAG-2 re-point gates the mdpf 49financial-key delete) -> INF billing one-writer 08-20 -> SILVER-DTYPE 08-21 |
| `0.4.0_DS_ClientPlatform~A` | SPAWN | **the runner lane**: P1-close for 49F (D-fleet inventory vs served census; 20-date backfill timing sample -> priced card), P2 dispatch entrypoint (S3-code standard), P3 close (dims off session acts), then INF at P2-open |
| `0.4.0_DS_ClientPlatform~B` | SPAWN | **the publisher lane**: P4 -- D fleet as the ADVI publisher writing `platinum/advi/49financial/`, `d_publisher_base` target root, per-key census + never-widen input, the population fix (35-advisor exposure) as first act |
| `0.4.0_DE_ClientPlatform` | SPAWN | T-A (08-19, first act) -> **P4 portal repoint** per served key (firm-config 49financial ADVI routes -> `platinum/advi`), tolerant read then flip -> T-C |
| `0.4.0_DT_ClientPlatform` | SPAWN (at P4 flip) | PROD promote of the repoint (`/prod-deploy`), rendered-read acceptance |
| `3.0.0_SA_CVO` | SPAWN | two-phase pins + parity bar SS8 per key (`org/tier1_exec/3.0.0_SA_CVO/deliverables/PARITY_BAR_49F_PLATINUM_OVERLAY_20260811.md`), P1-close parity sweep, P4 cutover cert (Rule 14e), P5 census read |
| `4.0.0_SA_CRO` | SPAWN (consulted) | GIPS field contract questions during P4 (P-1/P-4/P-6/P-7 now CONFIRMED -- fold into `ADVI_PERFORMANCE`), consumption map for client-key grammar, P5 methodology application |
| `0.8.0_AE_CloudComp` | SPAWN | PREFIX-READS (08-19) + the pulled-forward deployed-vs-built-from byte census (Lambda + EC2-staged, classify-don't-fix) -- feeds P5 |

---

## 3. THE DATED PHASE PLAN (49F). Dates are commitments; a slip is re-dated in writing, never silent.

| # | phase / act | owner | date | CLOSE CRITERION (mechanical, CTO attests) |
|---|---|---|---|---|
| 0 | bd platinum restore ACCEPTED (23:01Z run; served as_of = T-1; two named deltas) | DS base + AE, COO validates | **08-18 23:01Z** | HARD FIXTURE -- unchanged |
| 1 | **P1 CLOSE (49F):** D-fleet inventory -- every family EMITTED-with-instance or DECLARED-GATED(backfill); 20-date backfill timing sample RUN -> priced fill-word card to Andrew | DS~A (+CVO sweep) | **08-19** | attestation table: family / instance path / gate; card at Andrew |
| 2 | **P2 (49F):** schedule floor for the canonical runner chain (after ~12:18Z Schwab silver; event accelerator on silver-completeness) -- TF by AE, dispatch entrypoint by DS~A. **Host ruling (CTO, revisable on AE's read only with new evidence): the runner executes under the S3-code standard as its OWN scheduled stage -- NOT appended to the legacy chain's stage list (different outputs, one producer per key holds).** | AE + DS~A | build **08-19**; unattended cycles 08-20/21/22 | plan expected-rows-bounded, 0-diff, tag; THREE unattended daily writes of `portal/gold/advi/49financial/*/date={T-1}` (the TO-2 precedent bar); no session-local input |
| 3 | **P3 CLOSE (49F):** the copy root is the live root; `dim_security`/`dim_boundary` producers move into the scheduled chain (criterion i) | DS~A | **08-20** | live listing: every table's newest partition = T-1 written by the scheduled stage |
| 4a | **P4 EMIT:** D fleet writes `platinum/advi/49financial/{key}` (population fix first act; d_publisher_base root = platinum/advi); publisher IAM + schedule (after the runner stage) | DS~B + AE | **08-20** | 15 legacy served keys have a platinum/advi twin, census-frozen shape, instance per key |
| 4b | **P4 PINS:** per-key two-phase pin (pre-flip expects the MEASURED delta incl. the $122.5M Schwab-canonical authority @745ca6d78f; post-flip re-bases ~0) + never-widen determination per key (CTO+COO; DELTA=0 keys need no hold) | CVO + CTO/COO | **08-21** | pin file per key, cert issued |
| 4c | **P4 FLIP:** portal firm-config repoint per key -> tolerant read -> flip -> DT PROD promote -> rendered read | DE + DT | **08-22** | portal verified TAKING DATA IN and DISPLAYING IT (rendered + behavioral read, AC-P3 pattern) |
| 5 | **P5 (49F):** teardown of the legacy bd stages that produced the flipped keys (consumers first, binary last, Rule 25 + successor check), under the ratified methodology; census (0.8.0) informs | AE + CTO gate | **08-23 ->** | each retired path proven absent on the applied plane with a positive control; nothing served regressed |
| 5' | **MDPF unused-artifact DELETES (Andrew ~1500Z):** TO-4 rows -- everything with no active producer NOW; `json/mdpf/49financial/aggregate-aua-timeseries.json` ONLY AFTER T-B's FLAG-2 re-point verifies on a scheduled run | AE, COO issuer, CTO gate | **08-18/19** (after the 23:01Z fixture) | list-object absence with controls; the canonical gold's next 13:30Z run green after the 49f-key delete |

INF and COT open at P2 as parameter bindings of the same schedule/publisher the moment 49F's step 2 and 4a exist -- INF first (transposition map: YES daily-TWR tier; floor RULED unified+labeled carry), then COT (bundle RULED canonical basis, activates at its cutover).

---

## 4. HANDOFF -- the reinstantiation block every spawned seat reads FIRST (in this order)

1. `docs/architecture/GOLD_MIGRATION_PHASE_FRAMEWORK.md` (the five-phase law + close criteria) -- 79 lines.
2. `org/tier1_exec/1.0.0_SA_CTO/deliverables/MDPF_ADVI_UNIFIED_CANONICAL_PATTERN_SPEC_20260811.md` §1-§4, §6 (grammar, 9 atoms, the two ADVI parameters, shape-transposition doctrine, naming law).
3. `docs/architecture/OPAL_ADVIPOINTERS_PRD.md` §3 (state by phase), §5 (ordered next steps), §9.x YOUR OWN lane report from 08-12 (each lane wrote its own; read it before anything else about your scope), §12 (the open INF served defect).
4. `ANDREW_DIRECT_20260818_ALL_RECS_APPROVED_49F_END_TO_END_PUSH_AND_MDPF_UNUSED_DELETE.md` (today's rulings) + this plan.
5. Lane-specific: DS~A/~B -> `data/assets/scripts/gold/runners_49f/` (a00-d14, `runner_common.py` OUT_ROOT `portal/gold/advi/49financial`, `d_publisher_base.py`, `predeclared_divergences_49f.json`, `fit_reports/`), `docs/architecture/OPAL_RUNNERS_49F_BUILD_PLAN.md`, `OPAL_RUNNERS_49F_SILVER_DATA_DICTIONARY.md`, the 13 `PROOF_OF_SPEC_49F_*` instances in `org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/`; AE -> the P2 spec above + `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py` (the projector pattern) + `MDPF_TRGALN` PRD (the mdpf floor precedent); DE -> `portal/src/lib/pairedProvenanceRead.ts` + firm-config + T-A/T-C TOs; CVO -> `PARITY_BAR_49F_PLATINUM_OVERLAY_20260811.md` §§3-5, 7; CRO -> `ADVI_PERFORMANCE_E2E_STANDARDIZATION_PLAN_20260806.md` §15 (now confirmed) + `P5_DEBT_IDENTIFICATION_METHODOLOGY_SPEC_20260811.md`.
6. Every seat: `/watcher` once; register under the FULL suffixed serial; `to-check.py --all --assignee <serial>`; the TO is the authorization -- begin.

Every TO carries: `<proof_of_spec>` criterion-ids, the surprise channel (one banked line to COO, no chase), the compiler-tool mandate, and its DATE.

---

## 5. THE LIVE DATED ITEMS -- disposition IN WRITING (MSTR 150129Z: silence is how they orphan)

| item | owner | disposition |
|---|---|---|
| MDPF_PROVENANCE T-A (08-19) | DE | ABSORBED -- the DE seat's FIRST act on spawn, then P4 repoint |
| MDPF_PROVENANCE T-B (08-19) | DS base | STANDS, unchanged date -- now ALSO gates the mdpf 49financial-key delete (§3 row 5') |
| MDPF_PROVENANCE T-C (08-20) | DE | STANDS |
| OPAL_MDPFCLEANUP TO-4 remaining rows | AE / COO | AUTHORIZED by Andrew's word today; execute after the 23:01Z fixture; the 49financial key after T-B |
| OPAL_MDPFCLEANUP TO-5 (08-19) + CTO close RAVC | AE / CTO | STANDS 08-19 (consumer-exercise = 13:30Z floor mint, no 12:4xZ legacy write) |
| MSTR's 13 deploy-ledger dispositions (08-19) | MSTR | STANDS (MSTR's own) |
| accrual re-home (ownerless runner lifecycle) | AE | DATED 08-23, rides P5-49F/AE |
| INF billing two-writers one-writer fix + 7-builder sweep | DS base + AE | DATED 08-20 (DS base after T-B); consumer leg follows the step-1 log read |
| OPAL_ASSETS.SILVER-DTYPE (08-20) | DS base | RE-DATED 08-21 (behind INF billing at the same seat) |
| NFRA_COMPTOOLS.PREFIX-READS (08-19) | 0.8.0_AE_CloudComp | STANDS; census pull-forward joins it (08-19/20) |
| legacy-rps history tail | AE | DATED 08-23, rides P5-49F |
| COO/MSTR "HELD terminal state" schema proposal (deploy ledger) | CTO residual bank | BANKED; goes on Andrew's next card as a schema act -- not built |

**Rollback posture, every act:** same-window revert of the single moved edge; migrate-before-kill; no shadow channels; the legacy bd chain keeps running until P5 attests the flipped keys served correctly for the agreed window.

---

## §6 AMENDMENT 2026-08-19 -- THE FRIDAY COMPRESSION (supersedes §3's calendar for rows 2-4c)

**Authority:** Andrew-direct at the CTO terminal 2026-08-19: *"we need to get that not only sorted
out end to end architecturally and mechanically operable, and I want that planned for end to end
completion by Friday afternoon"* + *"make sure that this schedule and parity check are worked into
whatever plan document is governing the process here for 49."* Context: the FAM feed stoppage is
ENDPOINT-CONFIRMED vendor-side (Schwab SDD lists /fam n=15 ending AsOfDATE 2026-08-07 vs siblings
n=22 through 08-18; enumerate under Andrew's one-shot egress word 08-19); no pull-side act
accelerates it; the Schwab human contact is the single feed accelerator.

**THE DECOUPLE RULING (CTO):** the chain runs with FAM as a DECLARED-STALE input -- every
fam-consuming table's manifest declares `fam_as_of=2026-08-07`; the declaration carries through
the publisher to the affected keys (the d13-trio declared-degrade pattern); declarations LIFT
AUTOMATICALLY when the feed heals (manifest-driven, no session act). Valuation/TWR/flows do not
depend on family groupings; what degrades is grouping/rollup display, declared never silent.
**Principle attached: one vendor feed must never freeze the whole product** -- the schedule-floor
law one layer up. R remains ONLY the fam-heal event, no longer the chain anchor.

**BAR COMPRESSIONS (stated, Andrew's Friday word is the authority):** (1) flip fires on TWO
unattended greens (Thu+Fri) with the legacy chain as the live parallel net (it runs until P5
regardless); the third green accrues Sat and closes P2 formally. (2) The floor cron pins on
TODAY'S declared-stale measured run.

| when | act | owner | close |
|---|---|---|---|
| WED 08-19 (perishable, ~2-3h) | fam declared-stale mode + P2D-3 QA on 08-18 -> MEASURED DURATION | DS~A | duration in writing |
| WED 08-19 | P2-FLOOR TF apply (12:45Z cron, DLQ) on the measured pin; P4-PUBIAM + publisher schedule; P3 dims (a07 home, a06 xwalk) | AE + DS~A; CTO gates | applies ledgered |
| THU 08-20 | 12:45Z FIRST green; P4 emit all 15 twins; CVO pins per key + the per-key oracle table (both serves exist) | DS~B + AE + CVO | 15/15 emitted, pins filed |
| FRI 08-21 | 12:45Z SECOND green; DE repoint -> flip -> DT PROD promote; rendered + behavioral acceptance | DE + DT; CVO certs | **E2E COMPLETE FRIDAY PM** |
| SAT+ | third green closes P2; legacy parallel until P5; FAM heal -> declarations lift + affected-key pin re-base (CVO, declared act) | standing | -- |

## §7 AMENDMENT 2026-08-19 -- THE BLACK DIAMOND PARITY PROGRAM ("check our work"; a core feature of this product)

**Authority (same Andrew-direct):** *"we need to 'check our work' as it pertains to GIPS and
performance attribution and various reporting features against Black Diamond's calculated outputs.
We need to check at account level and confirm over every account that we are getting to the same
figures as Black Diamond is serving... We need to get to a point where our logic is EXACT."* His
word here IS the scope authorization to extend the standing bd49f REST pull with BD's per-account
performance/reporting endpoints (samples already in hand from the reporting_performance endpoint).

**Design:** per account x period, classify our computed figures vs BD's OWN calculated outputs:
`EXACT` · `EXACT-SHIFTED` (identical, +/-1d timing -- lag-correlation detected) · `TIGHT` (within
N bp, WITH the distribution -- tight-but-never-exact fingerprints a convention mismatch: cash-flow
timing, fee accrual timing, daily-TWR vs Modified Dietz) · `LARGE` · plus the per-account MIX
PROFILE (perfect-for-some/off-for-others fingerprints cohort causes). Census prints its
denominator (accounts covered / total); every non-EXACT class needs a NAMED mechanism -- no
smoothing. The census becomes a STANDING TEMPLATE FEATURE inherited by INF and COT at their binds.

| phase | when | act | owner |
|---|---|---|---|
| P1 probe | THU-FRI 08-20/21 | bd49f pull + performance endpoints; 3-5 accounts hand-checked vs the new chain's Thu output | DS-class + CRO methodology |
| P2 census | MON-TUE 08-24/25 | full-population account-level census + first classification report to Andrew | DS-class harness, CVO grades |
| P3 drive-to-EXACT | from 08-25 | fix largest class -> re-census -> repeat until EXACT across the board | DS + CRO; CTO gates convention changes |

**Owners:** CRO holds the GIPS/methodology contract (ADVI_PERFORMANCE Phase-1 field audit is the
input); DS-class builds the harness; CVO grades every census. All laptop-fabric.
