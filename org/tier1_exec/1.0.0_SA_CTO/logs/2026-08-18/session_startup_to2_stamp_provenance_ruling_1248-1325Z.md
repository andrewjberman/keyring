# CTO session log -- startup after 3.5 dark days · TO-2 stamp (K3 gate open) · MDPF provenance canonical-form ruling · TO-4 (iii) withdrawn on an executing-bytes find -- 2026-08-18 1248-1325Z

**archetype:** GATE
**secondary_archetypes:** DIAGNOSE, VALIDATE

## Window

Fresh session (seat dark since 08-14 2035Z). /watcher armed (task b8u0x8i1e, /cygdrive/c prefix, no orphan, no
legacy watcher); XXX.md startup run in full (serial file, audit-archive minted @a8757ab067+@0b0bd68f8a with 3
routine findings, PATH 96/97 + exercised, TO census, owned-paths hook, agent_context). Live seats: MSTR, COO, AE, me.
Andrew not at this terminal; all rulings below are mine on routed asks.

## Startup ground truth (Step 2b, scoped)

- 61 commits since my last session (COO 30 / AE 13 / MSTR 11 / DT 2 / DE 2 / CRO 1 / me 2 automated): OPAL_GWRENAME
  P0-P3 accepted, MDPF_EVR FE-2 on PROD v2.1.162, FE-1 cancelled (Andrew-direct 08-15 ~0350Z, LD-0417), NODEGAP.7
  superseded. COO measured 139/203 aged TOs 30d+ and holds it at Andrew -- I did NOT open a wholesale reconciliation;
  my 6 open TOs all sit in that aged NFRA cluster.
- **OPAL_MDPFCLEANUP wave-2 had slipped off the 08-15/16 wrap calendar** (zero project commits, TO-2 proof unstamped)
  -- flagged to COO+MSTR under the no-hanging-items order; COO re-dated 08-18/19 @62bd311d16 and owned it; MSTR
  owned the allocation call.
- Surfaced, not touched: the shared index carries **230 foreign staged files** (scratch dirs, `.s_m.json`,
  `cred-read.ps1`, deck prompts) pre-dating this session. The automated snapshot committed only its own 16.

## Delivered at this seat

1. **OPAL_MDPFCLEANUP.TO-2 STAMPED ACCEPT** @9f287b5d14 (`deliverables/OPAL_MDPFCLEANUP_TO-2_ACCEPTANCE_STAMP_20260818.md`).
   Own reads: object-version census of the cot dim key 08-14..08-18 + CW log-stream census of
   `mdpf-daily-trigger` and `mdpf-gold-lambda`. Canonical floor: 3 unattended cycles (08-15/16/17 13:30Z); value tie
   at equal value_date to the cent. **Producer discriminator exercised both ways on known 08-14 versions: legacy EC2
   = parquet-cpp-arrow 21.0.0, canonical Lambda = 20.0.0.** COO's 12:47Z timing observation resolved = the K3 legacy
   chain itself (trigger 12:44:42Z), which fired 4/4 days since 08-15 and wrote 2/4. **K3 gate OPEN**; COO GO'd AE
   (sequenced after the bd-platinum restore per COO 1307Z, which I accepted).
2. **MDPF served-provenance CANONICAL FORM RULING** @fc74f8f6b4 (`docs/architecture/MDPF_PROVENANCE_CANONICAL_FORM_RULING_20260818.md`).
   Measured on all four served scopes: `cohort_provenance` = THREE shapes / THREE intents (per-firm 49f+inflection =
   index-aligned SOURCE NAMES per Andrew 07-21 "the path is the provenance"; cottonwood = dated CLASS ENUMS per CRO
   s1a; global = dated PER-PARTNER composition per the 08-04 edict); `point_class[]` (W-7 one law) present and aligned
   everywhere. Rule-24 one-key-three-intents. RULED: `point_class[]` canonical class carrier at every grain (R-1 reader
   precedence flip, DE, first; adopt `carried` as a known 5th member); producer renames `cohort_source[]` /
   `partner_provenance[]` + emits the s1a class shape per-firm (R-2, DS); CRO s1a amended one clause (R-3). No pixel
   changes; LD-0417 untouched. **49F "count-identical to cottonwood" LOOK FALSIFIED** on the artifact at three
   versions (wrong-firm read on the measurement side). Global 3,178-warn class = per-firm reader misapplied at
   Global, not a producer defect. MSTR's bd-platinum "shared root" hypothesis falsified from the mdpf end (mdpf
   content ADVANCED correctly, T-1 on a Monday).
3. **TO-4 condition (iii) ADJUDICATED -- WITHDRAWN as unsatisfiable AND insufficient (my own condition; owned).**
   The canonical `mdpf-gold-lambda` READS `json/mdpf/49financial/aggregate-aua-timeseries.json` on every 49f build
   (`load_served_account_count`, FLAG-2 count carry, C2 fail-loud raise) -- verified at the EXECUTING package
   (CodeSha256 GAVTyWBw..., spine member sha ce9c0284537e == HEAD). An internal SDK read never traverses CloudFront,
   so the CF-log instrument (iii) named -- and the one we were about to ask Andrew to authorise -- would have read
   clean for a week and blessed a delete that breaks the nightly gold. Substituted a three-legged STRUCTURAL oracle
   (route negative + LIVE-policy principal census + executing-package reader census); served-key delete leg HELD on
   the FLAG-2 re-point prerequisite (gold self-carry from {D-1}); TO-4 PASS_WITH_DISCLOSURE for the rest. MSTR
   carrying the near-miss + "CF logging would NOT have seen this" verbatim to Andrew's card. Memory:
   `feedback_zero_access_oracle_must_match_the_reader_plane.md`.
4. **Decomposition answered:** DS lane = 0.4.0_DS_ClientPlatform (68/99 commits on data/mdpf/scripts/gold since
   07-15; owned-paths data/** = ANY), DE = 0.4.0_DE_ClientPlatform (10/10 reader commits); issue T-A/T-B/T-C now as
   dated+owned awaiting spawn; two amendments (FLAG-2 re-point = own criterion + ships first; T-A inverse mutant).
5. Banked as PROPOSAL only (not implemented): AE's `aws_security_group` create_before_destroy lint candidate.

## Corrections to my own positions this session (on the record)

- TO-4 (iii) was mis-instrumented from the day I wrote it (08-14): a CF-log condition can only prove EXTERNAL
  zero-access; the load-bearing reader was internal. Withdrawn, owned in the ruling record.
- 08-15 "satisfiable on trailing history" (COO's read of my window arithmetic) was true of the WINDOW and false of
  the INSTRUMENT -- shared ownership recorded by COO.

## Compiler Tools

| tool | use | result |
|---|---|---|
| comp-find (x3) | cohort_provenance producers/consumers (DEF+SURFACED bands), aggregate-aua-timeseries producer | PASS; denominators printed (777 hits / 26,406 files) -- located publisher, consolidator, spine, FE reader in one pass |
| comp-trigger | opal-smartx-ingestion-pipeline triggers | NO MATCH (136 rules + 15 schedules) -- correctly a match-miss, recorded not chased |
| to-check.py --all --assignee | startup census | 18 TOs / 13 projects; project scope for OPAL_MDPFCLEANUP 6 TOs |
| live primitives (rail-checked) | list-object-versions x6, get-object by VersionId x7, describe-log-streams x3, lambda get-function + package download, s3 cp x5 | every absence read paired with a found/negative control (nonexistent scope prefix = 0; known-producer parquet versions for the arrow discriminator) |
| pyarrow metadata read | producer discriminator on the dim parquet | created_by 21.0.0 vs 20.0.0, exercised both ways |
| Gap noted | no comp-tool reads DEPLOYED PACKAGE BYTES (Rule 22a CODE layer) -- done by hand (get-function -> curl -> zip member sha) | candidate for CTO residual bank, not built |

## Blockers

**NONE at this seat.** K3 applies arrive event-driven (I gate per-apply); T-A/T-B await COO issue + MSTR spawn.

## Next steps

1. Gate K3 applies as they land (expected-rows-bounded, sha-identity, consumers-first + last-invocation history;
   runner EC2 stop names Andrew's per-class word).
2. Read T-A's before/after on the live artifacts; arch-gate T-B (rename + s B3 key-set + harness exemption + FLAG-2
   re-point proof on a scheduled run).
3. TO-5 close RAVC + residual-bank conversion when the combined post-kill read lands (08-19 per COO).
4. Residual bank: deployed-package reader comp-tool candidate; SG create_before_destroy lint (proposal, Andrew's word).
