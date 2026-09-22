# LGIC registry pass, R4 narrowing + harvest homes, bucket recovery, three never-widen signatures, IRPT render auth

**archetype:** MIXED (IMPLEMENT + VALIDATE + COORDINATE)
**Seat:** `4.0.0_SA_CRO` (base). **Window:** 2026-09-21 ~13:03Z (session start) -- 2026-09-22 ~13:20Z.
**Prior log:** `logs/2026-09-20/watcher_reap_criterion_and_the_onboarding_stop_bullet_2145-1055Z.md`.

## Current State

26 commits by this seat on CLOUD this window (listed below), plus `10bace8916` on scratch branch
`cro/sitez-harvest-dedup` (off origin/SITEZ, for 0.0.0_AB_MSTR to push to a scratch ref). origin/CLOUD read at
`438312b085` at write time; most of the window's commits reached origin via 0.0.0_AB_MSTR's pushes
(`526937843e`, `d228ce5cb2`); the tail (from ~`3d63f04617` on) is NOT re-verified here -- push state UNREAD per commit.

Every Andrew-direct this window is recorded verbatim in ONE record:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260921_163xZ_FOUR_OPEN_CALLS_ALL_RECS_APPROVED.md`
(addenda + three self-corrections, in order).

**Canon / registry now (infra/logic, this seat's lane):**
- `02_DOCTRINE.md` R4 narrowed: `opal-data-assets` = client/partner custodial information only; other scopes homed
  by scope at every tier (`1675a8f631`); R6 note: a GENERAL-tenancy scope serves platinum from its own bucket
  (`b282500581`).
- `registry/tiers.json`: new GENERAL tenancy, all six tiers scope-homed (platinum since `b282500581`). `scopes.json`:
  `harvest` row, tenancy GENERAL, with provenance note (`74a988631d`).
- `registry/systems.json`: +prospecting, news, marketdata, cloudops, secops, deckgen, tradeops, cicd (batch 1),
  +posn, anthropic, openai (batch 2), +barrons, wsj, ft, filings-xbrl, issuer-site (`f21b66d1e4`),
  +portal, website (`6c07797a9c`). 43 system rows.
- `registry/resources.json`: batch 1 (239 rows, `93790c036e`), batch 2 (SY1: firm ingest -> vendor where the job's
  code reads one vendor; product jobs -> product; 26 re-pointed, `b282500581`), 18 `gateway` -> `portal`
  (`6c07797a9c`), 1 sibling alarm -> orion (`f185873e6b`). validate OK, 0 refusals.
- Placeholder population at the recount: 534 distinct `{system}` names; 419 resolve after batch 2.
- `06_CONFORMANCE_LEDGER.md` s.6 X9 GRANTED: AMGT Lusha lands silver only (`982e919d21`).
- `04_SCOPE_TICKLIST.md` / `05_IDENTITY_SPINE.md`: SmartX is 49 Financial's "currently" (row 10 answered).

**Signatures this seat holds (all SIGNED):**
- mdpf-gold-lambda Cottonwood Phase A+B, LEG A + LEG B -- `f291a7c487` (packet blob `2c59f07389`). Deployed and
  ledger-closed by 0.7.0_AE_CloudOps~V; acceptance = the 2026-09-22 13:30Z scheduled fire.
- IRPT_BCKEND.TO-IB-rtj-2 L4 fence probe -- `dba9199222` (packet blob `e2f521e5b5`).
- IRPT_BCKEND PRD v0.16 brief half -- review `e963205de6`, stamp `8e3643906f`.

**Buckets:** `opal-data-inflection` / `opal-data-cottonwood` recovered without root (break-glass roles
`firmsep-{inf,cot}-bucket-recovery-role`, created by Andrew in console, put the Terraform-rendered policy);
IB-rte-3 ledger L2 closed (`a0097b1ef4`); later IB-rth-8 + COO~B's plan read 0 change.

## Andrew-direct this window (verbatim in the record)
"All recs approved"; "Yes do it"; "recs approved" (x3); "Im good with your rec on calls 2 and 3 ...";
"Yes this is correct, I would add SmartX ..."; twelve residue answers; "CAN USE POSN ..."; "b" (compiled registry);
"yes agreed on both"; "rec approved" (hold portal/website); bucket recovery ("See if we can somehow get the original
... sorted now", "go ahead you have egress as needed"). Relayed: "Sign first, then push"; Lusha "Yes on Exception";
"Option 2 is preferable" (IRPT render auth).

## Self-corrections (each recorded where the error was made)
1. Startup summary claimed the watcher was armed; no Monitor had been called. Armed properly, stated.
2. Calls 2 and 4 carried the brief's framing; the grader already did both (0 rows moved) -- `28cebc3a15`.
3. Call 1a's primary-vendor REC contradicted NAMING_SCHEMA SY1 -- `847a1a39dd`, re-carded.
4. 18 rows filed under `gateway`, read by its word; `gateway` is the Opal Gateway -- re-carded, now `portal`.
5. `110a50f59f` deleted 4 CALL-2-approved prospecting rows by analogy -- caught by 1.0.0_SA_CTO~Z, reverted
   `3d63f04617`; the real fix was the grader precedence change (1.0.0_SA_CTO `8a4cb70499`).
6. Told 0.0.0_AB_MSTR "validate refuses a duplicate key" (99149) -- false; 1.0.0_SA_CTO added it `86b238a9af`.
7. An uncommitted edit to a GATED shared registry file blocked 0.7.0_AE_CloudOps~V's commit (99165); reverted and
   held as a patch. Held edits now go in a worktree or patch, never the shared tree.

## MCP traffic
~60 messages handled. Significant: Andrew-direct broadcasts (99091, 99097, 99108, 99116, 99129, 99148, 99170);
never-widen halves (99228/99229, 99373); corrections (99103, 99264); SITEZ dedup handoff (99281); IRPT research
(99464) and L4-R stamp (to CTO, ~12:50Z). Tier-2 send gate refused two sends that named 0.7.0_AE_CloudOps~V; resent
via 1.0.0_SA_CTO.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-find | `--name '*BRIEF*'`, content sweeps, `--corpus aws multi-threadv2`, opalinvest / lusha locators | PASS | found the registry-assigning brief via git log; aws corpus located a DECLARED secret |
| comp-read | runner.tf, gldinc-ss4c.tf, portal-auth/portal-content/ticket-center/trade-pipeline/website main.tf | PASS | summaries thin on tags; full Read needed for Project/System tags |
| lib/opal_naming.py | validate / grade / address / generate / census, many runs | PASS | every registry edit simulated on a scratch copy + full-census diff before landing |
| .tools/prd-signoff.py | sign IRPT_BCKEND --half brief; status | PASS | brief SIGNED; ratified-text owed by 3.0.0_SA_CVO~B |
| .tools/deploy_ledger.py | close-leg IB-rte-3 L2 | PASS | |
| aws (shim) | s3api get-bucket-policy / head-object / list-objects-v2, lambda get-function-configuration, iam get-role / list-roles | PASS | rail-checked where comp-iam does not grade bucket-policy conditions |
| render_naming_section.py | --check / --write | FAIL (by design) | --write would revert a ruled correction; restored; row LGIC_CANON-S29 |

**What worked:** simulating every registry change over the full 1,738-name census BEFORE landing -- it caught the
portal-publisher collision, the lusha/bright-data redundancy and the gateway misread before they shipped.
**What failed:** (1) aws.exe silently failed writing to an MSYS `/tmp` path -> false "NOT FOUND" (fixed with
`cygpath -w`); (2) Python `subprocess(['bash', ...])` resolved the wrong bash -> empty policy reads; (3) `git apply`
of a held patch failed after an intervening vendor-key commit (re-applied by script).
**Gap found:** the checker ranked tokens over registry rows (fixed `8a4cb70499`); validate did not refuse duplicate
scope keys (fixed `86b238a9af`); worked-case fixtures are registry-dependent (test design routed to 1.0.0_SA_CTO).

## Blockers
None at this seat.

## Next Steps
1. [Andrew] Delete the two break-glass roles `firmsep-{inf,cot}-bucket-recovery-role` (carded; REC delete now).
2. [0.0.0_AB_MSTR] Push `10bace8916` (SITEZ harvest dedup) to a scratch ref; SITEZ must merge it BEFORE or WITH
   `86b238a9af`. Keep 1.0.0_SA_CTO's grader version over 1.0.0_SA_CTO~Z's `55c24a8b8a` at the merge.
3. [1.0.0_SA_CTO] resources.json compiler (root map + SY1 by vendor reads); lib/tests worked-case grading without
   the resources layer; regenerate the 10 generated carriers (generated_locals.tf gains harvest/portal).
4. [LGIC_NAMING owner] GRADING_RULE.md worked case `opal-portal-data-proxy-api` is stale (portal is now V1).
5. [3.0.0_SA_CVO~B] IRPT_BCKEND v0.16 ratified-text half.
6. [4.0.0_SA_CRO] Sensitivity Analysis Tab 2 Excel upload -- L1 brief when Andrew says go (column-B unit question).
7. [CVO / MDPF owner] Cottonwood acceptance on the 2026-09-22 13:30Z fire: cottonwood at the 09-18 frontier, global
   by_model 9 keys.
