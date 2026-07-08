# 0.4.0_DS_ClientPlatform — Current state: 49F Schwab-SSOT mesh design + SCHWABAUTO Gate-2 relay

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, COORDINATE

**Date:** 2026-07-08 | **Window:** session start (registration) -> now | **Serial:** 0.4.0_DS_ClientPlatform (base)

## Summary
Session opened on `/watcher` + org/XXX.md startup, found `ADVI_COTETL.AUAFIX-L6` (cot AUA exclusion
rule) as the standing pending TO and began Phase-1 grounding on part (b) (automate the manual
`aua_overrides.json` ghost-account list). Andrew redirected mid-investigation to a higher-priority
question: why does 49 Financial show $1.66B on ADVI vs $1.62B on MDPF. Fully source-grounded that
(all-custodian BD book vs Schwab-scoped-but-BD-valued), which opened into an extended plan-mode design
dialogue with Andrew on migrating 49F to a Schwab-precedence, BD-fallback-flagged blended architecture
("mesh/stitch"). That surfaced the live SCHWABAUTO Gate-2 (SDD REST capturer) blocker + a proven
silent-miss bug in the current Schwab ingest automation; Andrew directed a relay to CTO, which resolved
same-session (CTO signaled Gate-2 GO to AE, ruled the design-brief section 6 sequence authoritative,
routed TO-hygiene to COO; COO owned the TO-consolidation reissue).

## Work done (chronological)
1. `/watcher`: was NOT REGISTERED (fresh session) -> registered, armed persistent inbox Monitor (task
   `b26dnuuzi`), inbox pull empty, no stale `/watcher` cron found.
2. org/XXX.md startup: read README.md + prompt.md + pending TO (`ADVI_COTETL.AUAFIX-L6`) + recent logs
   (all `~B`-lane, confirmed do-not-grab per that lane's own 07-08 log note).
3. AUAFIX-L6 Phase-1 grounding (part b, automate snapshot-zeroed predicate): `comp-pipescript io` on
   D_04, read `lib/exclusions.py` + `aua_overrides.json` + `E_00.decompose_aua_gap.py`. Found the manual
   4-account ghost list does NOT fit a naive `<$100` auto-predicate (2 of 4 have silver_aua $6,430 /
   $922 -- well above $100; a silver/cube RATIO test is needed instead). **PAUSED here** by Andrew's
   explicit redirect -- no code touched, finding preserved in this log + the TO file for whoever resumes.
4. Andrew: "why $1.66B (ADVI) vs $1.62B (MDPF) for 49F, should both be the Schwab number ($1.66B)?"
   Grounded via `pipescript mdpf` / `pipescript advi-bd` (producer architecture) + direct reads of the
   MDPF WS-E feeder (`build_mdpf_wse_49f_non_model_aua.py`) + bd's `D_01.partner_analytics.py` + a raw
   S3 sum of `schwab/silver/rps/date=20260706`. **Delivered, inverted the hypothesis:** MDPF's $1.621B
   (`partner_custody_total`) already matches the raw Schwab feed to $18K (0.001%) -- it IS the Schwab
   number, just BD-valued-not-Schwab-valued. ADVI's $1.658B is the one that's off-basis: all-custodian
   BD book (`D_01` "AUA by Tax Status" donut, no custodian filter). certified_aua (silver, all-custodian,
   context only) = $1.837B.
5. Entered plan mode: Andrew's ask -- interview him on 49F Schwab-migration/meshing goals, build a
   cohesive plan (Schwab = definitive source, BD = flagged fallback for non-Schwab accounts, eventual
   Fidelity-direct). Grounded extensively before asking anything: found this is NOT greenfield --
   `DATA_SSOTMG` (06-29 GO) + a CVO custodian-native sovereign directive (06-30, `555712b6c`) already
   ratify almost exactly Andrew's ask (3-way fence: custodian core / fenced curated advisor-metadata /
   surplus non-custodial). A full canonical Schwab-native gold stack (G1-G14) already exists, proven to
   the cent against Schwab (holdings 0/5892 breaks, lots 0/3793), but is UNSERVED -- runs in a separate
   parallel tree, nothing wired to production ADVI/MDPF. `DATA_SSOTMG.json` phase text shows it HELD
   behind `ADVI_BREAKS` since 2026-06-30 and that hold was never confirmed formally lifted (flagged, not
   resolved). Also read the SDD/SI2 auth-flow memories + the ADVI_BDAPIMIG thin-tether design + the
   census-bounded ~$243M non-Schwab residual ($166.3M fully-non-Schwab/Fidelity + $76.5M
   held-away-in-Schwab-not-in-RPS).
6. Issued a 4-question `AskUserQuestion` batch -- **rejected by Andrew** ("I want a dialogue, not a
   questionnaire"). Reformulated as plain conversational text.
7. Dialogue: Andrew confirmed the stitch principle -- blended value, Schwab takes precedence on all
   Schwab accounts, BD as flagged fallback, and explicitly do NOT refactor BD's messy patch-laden gold
   monolith wholesale -- shrink it incrementally as accounts migrate to Schwab coverage, since BD's core
   problem is revision-lag + unknown delay (vs Schwab's reliable T-1-complete). Surfaced two concrete
   open design gaps in response: (a) custody attribution is currently rep_code-INFERRED, not exact
   (~$125.7M no-rep-code ambiguous bucket -- a proposed fix, `ADVI_49FRECN.006`, would add an explicit
   custodian column); (b) client/relationship-level partial-flag semantics (one household, mixed
   Schwab/non-Schwab accounts) undecided. **Neither resolved yet.**
8. Andrew: "is the RPS ingest system functioning adequately? go check the SDD REST endpoint structure
   via the SI2 GUI app." Grounded via `comp-freshness chain bd` + a read of
   `docs/briefs/schwab-sdd-rest-ingest-aprime-design-20260702.md`. Answered: freshness gate shows PASS
   (schwab_rps 28.3h, well inside 72h) but that is a FALSE-COMFORT green -- the 07-07 AE log
   (`schwab_07-02_07-06_unfreeze_and_iam_misattribution_correction.md`) documents the automated GUI
   channel silently missing 2 real deliveries across 14 "clean" cycles, caught only by Andrew's manual
   login. Endpoint structure is already substantially documented (SDDServices REST base, LMS SSO OAuth
   flow, known `.aspx` endpoints, and -- from a 07-07 Gate-3 recon -- the live auth material's actual
   location: a WebView2/Chromium profile, NOT Windows Credential Manager as originally assumed). Flagged
   that going further (reading live session material) is deliberately CTO-arch-gated and is
   `0.6.2_AE_PartnerETL`'s lane, not mine -- did not attempt it myself.
9. Andrew: "relay to CTO, structure into the existing recon project, decisively finish it." Before
   acting, my persistent Monitor delivered a live COO inbox routing (`bd_gold_firm_composition` 115h
   FAIL + bd platinum 2-trading-day content-stale, "ground the mechanism") -- pulled + acked per RAVC
   (non-blocking, deferred, promised same-session). Read the governing TO
   (`ADVI_SCHWABAUTO.ae-fetch-by-date-selfheal-finish-the-box.md`, status=pending since 07-02, still
   documenting the SUPERSEDED GUI-driver mechanism). Sent 3 MCP messages: **CTO** (primary ask -- relay
   Andrew's priority + the reliability grounding + a Gate-2 GO ask + the TO/numbering-fragmentation
   flag), **COO** (ack on item 9's routing + SCHWABAUTO consolidation flag, since COO is TO
   issuer/RAVC owner), **AE** (FYI-only, no new work asked).
10. Same-session resolution: **CTO** reviewed the Gate-3 finding, **signaled Gate-2 GO to AE** (security
    conditions + "show-me-before-live-capture" bound intact), explicitly credited the false-freshness
    catch, and **ruled the design brief's section-6 (0-6) sequence is now the authoritative structure**
    (Gate-1/2/3 shorthand + the TO's stale LEG body retire onto it), routing the actual TO-rewrite to
    COO. **COO** confirmed ownership, will reissue the TO onto the new numbering **timed to the Gate-2
    GO** (which had just landed), flagged the current TO body SUPERSEDED in the interim so nobody
    executes off the dead legs, and will name the Schwab-SSOT mesh dependency explicitly in the reissue.
    Reported the full resolution back to Andrew.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-pipescript io` | D_04.client_portal_summary.py (cot) | PASS | AUAFIX-L6 Phase-1 grounding (27 reads/22 writes mapped); investigation paused mid-stream, not resumed |
| `comp-freshness` | `chain cot` | PASS/WARN mixed | cot silver PASS; platinum MTIME-FRESH/CONTENT-STALE (07-06 content, 2td behind) -- confirms AUAFIX-L6's served-verify gate is still open |
| `comp-which` | "is the served Cottonwood cot AUA artifact fresh..." | PASS | routed correctly to `comp-freshness chain cot` |
| `comp-grep` | aua_overrides/exclusions/AUAFIX-L6 logs, ghost-exclusion consumers | PASS (multiple) | located `E_00.decompose_aua_gap.py` + all 8 cot-wide ghost-exclusion consumer sites |
| `pipescript` | `--list`, `mdpf`, `advi-bd` | PASS | mapped MDPF WS-E + ADVI D_01 producer architecture -- the load-bearing evidence for the 49F ADVI-vs-MDPF diagnosis |
| `comp-freshness` | `chain bd` | PASS (24/25 rows) | grounded `schwab_rps` as PASS-but-false-comfort, cited directly to CTO alongside the 07-07 silent-miss finding |

**Worked:** `pipescript`'s producer/served mapping was the highest-leverage tool this session -- took
the 49F ADVI-vs-MDPF question from "two numbers, unclear why" to an exact mechanism in 3 calls,
cross-checked against a raw S3 sum of the Schwab feed itself. **Failed:** none this session. **Gap
found:** none new -- reconfirmed the existing, already-flagged gap that no comp-tool surface exists for
box-local SDD/SI2 investigation (Cred Manager / WebView2 profile / SSM log reads), consistent with AE's
own 07-07 log note. No code edits or commits this session (all read-only grounding + MCP coordination)
-- `ds-commit-gate` not applicable.

## Blockers
None blocking me directly. `AUAFIX-L6` is PAUSED (not blocked) at Andrew's explicit redirect -- resumes
on signal. `SCHWABAUTO` Gate-2 was blocked pending a CTO signal at the top of this window; it is now
UNBLOCKED (GO signaled this session) -- tracking, not blocking, from here.

## Current State (handoff -- zero prior context)
- **AUAFIX-L6:** part (a) landed 07-07 (`fa7792b70`, AP no-activity gate removed cot-wide), served-verify
  still pending (co-gated with L1 chain-freeze -- cot platinum content-stale as of this session). Part
  (b) automation design PAUSED mid-Phase-1: naive `<$100` snapshot-zeroed floor does NOT fit the
  validated 4-account ghost list (2 of 4 have silver_aua in the hundreds/thousands, not near-zero) --
  needs a silver/cube RATIO predicate instead of an absolute floor. Part (c) (phantom `<$100` gate
  removal) not started. No code touched.
- **49F ADVI-vs-MDPF discrepancy:** RESOLVED + delivered to Andrew. ADVI $1,657,919,550 (`D_01
  partner_analytics`, all-custodian BD book, no Schwab filter) vs MDPF $1,621,251,574 (`partner_custody_total`,
  Schwab-scoped but still BD-valued) vs raw Schwab RPS truth $1,621,269,643 (direct sum,
  `schwab/silver/rps/date=20260706`, matches MDPF to $18K). `certified_aua` (silver, all-custodian,
  context only) = $1,837,159,866.
- **Schwab-SSOT mesh/stitch plan:** IN DIALOGUE, no plan file written yet (plan mode was exited by the
  system mid-Phase-3, before the Phase-4 write; `~/.claude/plans/here-is-how-i-partitioned-firefly.md`
  does not contain a finished plan). Confirmed the already-ratified 3-way-fence architecture
  (`DATA_SSOTMG_PRD.md` section 0, CVO directive `555712b6c`) matches Andrew's blended/Schwab-precedence
  ask closely; the actual gap is that the built canonical Schwab-native gold (G1-G14,
  `data/canonical/schwab/gold/`) is unserved/unwired to production. Two open design questions, unresolved
  with Andrew: (1) fix rep_code-inferred custody attribution first (~$125.7M ambiguous bucket) or build
  the blend on inferred custody now; (2) client/relationship-level partial-flag semantics for mixed
  Schwab/non-Schwab households. `DATA_SSOTMG.json` phase text shows it HELD behind `ADVI_BREAKS` since
  2026-06-30, hold never formally confirmed lifted -- open governance question, not yet routed.
- **SCHWABAUTO / Schwab Box:** Gate-1 (firm-sep DenyPlane) closed 07-06. Gate-3 (recon -- SI2 auth
  material lives in `SI2Desktop.Container`'s embedded WebView2/Chromium profile, NOT Windows Credential
  Manager as originally assumed) done 07-07. THIS SESSION: **Gate-2 GO signaled by CTO to
  `0.6.2_AE_PartnerETL`** (security conditions + "show-me-before-live-capture" bound intact); CTO ruled
  the design brief's section-6 (0-6) sequence authoritative over the TO's stale LEG numbering and AE's
  informal Gate-1/2/3 shorthand; **COO owns the TO reissue**, timed to this Gate-2 GO, on
  `org/tier2_senior/0.6.2_AE_PartnerETL/task_orders/ADVI_SCHWABAUTO.ae-fetch-by-date-selfheal-finish-the-box.md`
  (currently flagged SUPERSEDED in the interim). Root motivating finding (AE, 07-07; cited by me to
  CTO): the current GUI-automation channel silently missed 2 real Schwab deliveries across 14 "clean"
  cycles -- `comp-freshness` PASS on `schwab_rps` was a false-comfort green (CTO's own characterization:
  "exactly the false-freshness class").
- **Separate, unrelated open item:** COO routed a live BD-lane freshness question this session
  (`bd_gold_firm_composition` FAIL 115h vs 48h threshold; bd platinum 2-trading-day content-stale) --
  ACKED, explicitly deferred (COO confirmed non-blocking), NOT yet grounded. Immediate next action.

## Next Steps
- **[0.4.0_DS_ClientPlatform -- me]** Ground `bd_gold_firm_composition` (115h stale, FAIL) + bd platinum
  2-trading-day content-lag mechanism for COO -- July-4th-holiday/weekend lag vs a real D_03 nightly gap.
  Promised same-session.
- **[0.4.0_DS_ClientPlatform -- me, on Andrew signal]** Resume the Schwab-SSOT mesh/stitch dialogue: get
  Andrew's answer on the two open design questions above, then write the actual plan file (Phase 4 was
  never reached).
- **[0.6.2_AE_PartnerETL]** Build the Gate-2 capturer per CTO's GO (SQLite `Cookies` decrypt via
  DPAPI/os_crypt + a leveldb `Local Storage` reader) + the session-liveness alarm (built BEFORE relying
  on the standing session, per design-brief section 6), then the Rule-22a exercise-confirm (REST-refetch
  a known-missed date, e.g. 07-02/07-06 RPS) before any production reliance.
- **[2.0.0_SA_COO]** Reissue/amend `ADVI_SCHWABAUTO.ae-fetch-by-date-selfheal-finish-the-box.md` onto the
  CTO-ruled section-6 sequence, retiring the stale GUI-driver LEG body, timed to this session's Gate-2
  GO; name the 49F Schwab-SSOT mesh dependency explicitly per her own note.
- **[1.0.0_SA_CTO / 2.0.0_SA_COO]** Unresolved governance flag: `DATA_SSOTMG`'s own project-JSON phase
  text says it is HELD behind `ADVI_BREAKS` (2026-06-30) and that hold was never confirmed formally
  lifted, even though `ADVI_BREAKS`' own record shows the underlying pipelines were fixed same-day.
  Andrew's direct engagement on the Schwab-SSOT plan this session may function as an implicit
  resume-authorization, but this has not been formally closed/recorded -- flagging for whoever writes the
  plan file.

## MCP traffic
~7 messages this window. Significant: relayed Andrew's SCHWABAUTO Gate-2 priority to CTO (primary ask,
with the reliability grounding) + COO (ack + TO-consolidation flag) + AE (FYI); received + acted on
COO's `bd_gold_firm_composition` routing (acked, deferred); received CTO's Gate-2 GO + section-6-authoritative
ruling; received COO's TO-consolidation ownership confirmation. No RAVC loop fully closed this window --
the SCHWABAUTO Gate-2 relay is IN PROGRESS (GO signaled, capturer build not yet started/reported back).
