# NFRA_CLDGRPH -- ROUND-4 ANALYSIS (L10, the CTO's read of the slug) -- 2026-09-09 ~15:1xZ

**Reader:** `1.0.0_SA_CTO` (the single router, spine v3.6 L10). **Slug:** `3.0.0_SA_CVO` message 94502, record
`../surprise-channel/adjudications/ADJUDICATION_v1.md` C-S22..C-S25 and `../surprise-channel/remediations/REMEDIATION_v3.md`
(9 rows) @`23fb03b1cd`, on `2.0.0_SA_COO~A`'s FINAL packet `L8_PACKET.round4.final.md` and `COMPLETION_REPORT.round4.json`
@`5a999e42b9`. **Precondition, the CVO's own lines at the slug:** 20 of 20 orders terminal with VALID instances (round 4's 12 plus
rounds 1-3's 8); 11 of 11 judgment criteria graded PASS across the round; 0 undispositioned of 122 investigation items at the
commit (C-S23 GRADUATED and CLOSED 21, C-S24 GRADUATED with the remedy OPEN 17, C-S25 DISMISSED 37 records).
**Answer:** a **PRD ADDENDUM v0.4 -> v0.5** (four manifest rows, section 3) AND the round analysis -- every outcome in the header has a
cell that served it (8 of 8 COVERED on the COO's report), and ONE outcome, FWD-7, is NOT REALIZED on Rule 22's STATE axis for reasons
no cell of this decomposition owned. **Grades:** `COMPLETION_GRADES.round4.json` beside this file (7 REALIZED, 1 NOT_REALIZED).
**Andrew's words this round:** *"we can switch off laptop copy"* (@`61d5ef55dd`, executed at the D-7 drain, 6 -> 0 at 14:08:02Z);
*"/drive NFRA_CLDGRAPH to completion"* (~13:1xZ at the `~A` terminal); *"no new work until you get my transcript"* (~12:5xZ at this
terminal) -- the rows below are PLACED for the recut and cut nothing themselves.
**Push state at write:** LOCAL; origin/CLOUD @`58adeff90c` (ls-remote 14:32Z this session).

## 1. Per outcome: the card, what round 4 delivered, the CVO's read, this seat's grade

Read against the proof-of-spec instances at HEAD (20, each VALID at its vintage per the CVO's re-read), the adjudication rows that
graded the judgment criteria, and this seat's own instruments where they differ (section 4). DONE WHEN states are the ENDPOINT's.

| outcome | DONE WHEN | delivered at HEAD | the CVO's read | **grade** |
|---|---|---|---|---|
| FWD-1 ask, be answered | EXERCISED | CG-s-5 (D-2, the `/graph/cypher` bearer path), CG-x-1 (D-5: a never-compiled seat got the three correct rows at a disclosed vintage, 11 of 11 asks) | D5-AC5 PASS (C-S11) -- the time is the thin client's fixed cost, a design item | **REALIZED** |
| FWD-2 newer on the estate's schedule | EXERCISED | CG-s-15 (the rebuilt, digest-pinned image), CG-s-16 (the notification grant), CG-x-2 (D-9: the nightly fired itself; STAMP->ANSWER 82.186 s; BEHIND_CAUGHT on the estate's own stamps) | D9-AC6 PASS (C-S12) | **REALIZED** |
| FWD-3 age in plain words | APPLIED | CG-s-6 (D-3: the thin client prints the VINTAGE line on every answer; every round-4 answer carried it) | D3-AC8 PASS (C-S8) | **REALIZED** (observed EXERCISED, a stronger state than the card asks) |
| FWD-4 a ceiling the system owns | EXERCISED | CG-x-4 (D-10, pass 3: the ceiling held at 31.0% on a HAND-FREE cycle, 3092 of 3092 answers placed) | D10-AC5 PASS (C-S16) | **REALIZED** |
| FWD-5 a fresh machine is answered | EXERCISED | CG-x-5 (D-6: a machine with no local DB, proven absent by `ls` before the ask, answered first try) | D6-AC4 PASS (C-S7) | **REALIZED** |
| FWD-6 nobody chooses a refresh mode | APPLIED | CG-s-6 + CG-s-8: the thin client carries no `--mode`, `--db-path`, flag or prompt; `comp-kuzu --mode full` is REFUSED by the client (exercised at C-S22) | D7-AC8 PASS (C-S22) | **REALIZED** -- a refused flag is not a choice a user can make; the manifest still OFFERING it is an instruction path back, which is FWD-7's row S17, not a choice under FWD-6 |
| FWD-7 one graph story, local copy retired | EXERCISED | CG-s-8 (D-7, pass 4: the seam unreachable 0 of 3, consumers opening a local DB 0 of 29 with three controls, the writer DELETED, the canonical copy SWITCHED OFF 6 -> 0); CG-x-7 (D-8: two machines, 2.1 s apart, byte-identical 58 rows under ONE vintage, no canonical copy on either) | D7-AC8 PASS, D8-AC5 PASS (C-S22); **carried NOT REALIZED** -- `graph-call-manifest.yaml` still routes a repointed consumer back through `comp-kuzu --mode` (W2-S23); the person half MODELLED (one worker on two machines) | **NOT_REALIZED** -- the accept's third clause, *no second, older copy anyone could still be reading from*, fails on the INSTRUCTION plane (Rule 20 sends every seat to that file), and two of three residual local stores are held do-not-delete with no owner of their disposition |
| FWD-8 the operator sees the night | EXERCISED | CG-s-7 (D-4, the pull-style read), CG-x-8 (D-11: a REAL morning read YES with the night's own time; the planted miss read NO) | D11-AC4 PASS (C-S13) | **REALIZED** |

**Coverage verdict:** 8 of 8 outcomes served by cells; no `DECOMP_INVALIDATING` row; no cell invalidated. **Realization verdict:** 7 of 8.
The one NOT_REALIZED is the same shape as the last two projects this seat read (ETFS_GUARDRAIL: a promise awaiting an event;
NFRA_OUTSET: code committed and not served; here: a surface retired beside an instruction to re-create it) -- three mechanisms,
one axis, and the CVO told this seat at C-S17/A4.3 before grading that it would read it so. It does.

## 2. Why the round could not have closed it, and what the addendum owns

R7 made CG-s-8 a PORT WITH A RETIREMENT and enumerated four surfaces (the store, `kuzu_cli.py`, the seam, the sink). Every one is
retired and measured so. What the enumeration did not contain is the ESTATE'S KNOWLEDGE of the retired surface -- the manifest every
seat consults before an infra change (Rule 20), the tool index's help, two code sites -- and the OTHER local graphs built on this
machine that are not the projection but are exactly "the compile business" the PRD's own title retires. Neither is a cell's
omission: the cell's four surfaces were the right four for the PROJECTION. Both are this PRD's, because the s.7 domain was the
OWNS cell of s.3 and s.3 never owned "what the estate is TOLD about the graph" or "the graphs beside the graph".

⛔ **THE TEST THIS ROUND EARNS, for every PRD that RETIRES a surface: A RETIREMENT HAS THREE PLANES -- the EXECUTABLE (what runs),
the INSTRUCTION (what the estate is told to run: manifests, help text, docs a rule sends seats to), and the RESIDUE (what else
was built the same way beside it).** A manifest that places only the first passes every cell and leaves a live instruction to
re-create the path. This is the twin of NFRA_OUTSET's round-2 test (*a seam is two ends and a clock*): both are the members an
architecture section assumes rather than costs.

## 3. THE ADDENDUM v0.4 -> v0.5 -- four rows, placed by ruling and now owned

s.7 gains S14-S16 by reference (the cells the round-3 analysis @`2dd381d969` and the CTO's answer 94158 had the COO add to the
decomposition as CG-s-14/15/16, all DONE) so the two carriers hold ONE id space again, and these four NEW rows:

| id | outcome | surface | lane | verb | depends_on | accept (the load-bearing clause) |
|---|---|---|---|---|---|---|
| **S17** | FWD-7 | THE INSTRUCTION PLANE'S ROUTE BACK: `graph-call-manifest.yaml` `cloud.refresh.full` (:219) and `cloud.refresh.incremental` (:233) whose `canonical_call` is `comp-kuzu --mode ...`, the `:1783` subcommand list (`--mode auto\|inc\|full`, `--db-path`); `tool_index.py` help x6; `comp_aws_cli.py:2857,2866`; `comp_similar.py:591` (`corpus_db == "kuzu_nessie_db"`) -- W2-S23, the row this seat placed at 94456/A4.3 | `0.8.0_AE_CloudComp` | retire | S8 (DONE) | (1) both refresh entries retired under the file's own `retired_aliases` convention with a successor entry naming the served graph; `:1783` carries no `--mode`/`--db-path`; the six help texts and the three code sites name the served graph; a refresh phrasing through `comp-which` routes to no retired entry, printed beside a positive control. (2) **FWD-7's PERSON half:** a seat on site Z asks D-8's fixed question through the public gateway inside D-8's window and matches the laptop's answer byte-for-byte under one vintage -- the roadmap's allocation (Andrew), MODELLED on machines until then; the CVO's recommendation adopted: the site-Z exercise is this row's accept, not a new cell. Bound: no rebuild path is re-created; W2-S27 (`projection_client` takes neither a db path nor a Cypher parameter dict) is the constraint every repoint meets |
| **S18** | FWD-2, FWD-4 | THE FOUR `:latest` PRODUCERS -- `comp-learns-producer:1`, `cse-producer:1`, `fedobs-producer:1`, `resource-summaries-producer:1` still reference `opal-globgrph-derive-runner:latest` (S31's pins half; 3 of 7 families pinned by CG-s-15; the four `.tf` files carry the tag on the declared plane, measured here; the applied plane at the CVO's `describe-task-definition`) | `0.7.0_AE_CloudOps` | deploy | S15 (DONE) | 7 of 7 ACTIVE globgrph families reference the image by DIGEST, read live by `describe-task-definition` after the apply, under a NEVER-2 entry that names every family the act touches; **R13 below is the rule.** Bound: no image is rebuilt by this row -- a pin is a task-definition revision, nothing else moves |
| **S19** | FWD-7 | THE RESIDUAL LOCAL STORES beside the projection: `kuzu_db` (+ `kuzu_load.py`, the June-2026 scratch builder, 1,166 nodes of this graph) and `kuzu_ac7.db` (NFRA_GLOBGRPH.ITEM-3), with their manifests (`kuzu_load.py:278` stamps merge attempts as `edge_count`, S53) -- present at this seat and at the CVO, reachable by NO client path (0 readers of 982 files), held do-NOT-delete by the CVO's P7 (`DIAL_RECORD_comp-kuzu_20260804.md`) | `0.8.0_AE_CloudComp` | decide | -- | each store's DISPOSITION recorded with its owner and reason (retire with a tombstone / archive under its own project / keep with a NAMED reader); the P7 hold lifted or re-stated by its author on the record; `comp-find` over the tool homes still 0 readers beside a positive control; NOTHING deleted before the disposition lands; a store that STAYS carries a manifest field a consumer can reject on (S53; *a value must carry its claim*) |
| **S20** | FWD-7 (by this PRD's arc -- *no machine is in the compile business* -- not by the letter of "the graph", which Andrew defined 2026-09-02 as the KuzuDB projection) | THE STITCH GRAPH: `comp_debt.py:215`'s stitch leg opens `kuzu_stitch_db` locally and REFUSES where absent (W2-S17); `kuzu_stitch_load.py:124` stamps merge attempts as `edge_count` (S53) | `0.8.0_AE_CloudComp` | decide | S19 | the stitch graph's HOME decided and recorded: either it JOINS the projection (derived cloud-side and served -- a later round's cells) or it is DECLARED a local scratch artifact outside "the graph", with `comp-debt`'s refusal text naming the decision and the local builder's manifest carrying its claim (S53); no local rebuild path to the PROJECTION is created by either answer |

**R13 (addendum v0.5, s.6):** *no globgrph task family references a mutable image tag; every image act's change-management entry
names every family that pulls the tag it moves* -- the PRD half of S31's remedy; the law half already stands at CLAUDE.md NEVER-2
(@`b00a69a676`).

**A correction to this seat's own placement @`1266d65641`, stated rather than tidied.** That ruling said cost attribution on
graph nodes would land "as a manifest row at L10". It does NOT: no outcome of this endpoint names cost, and a row with no
`outcome` is the phantom-cell shape the decomposition's 1:1 check exists to refuse. The capability is OWNED, not merely named, by
being placed where a new outcome is minted -- an L1 brief candidate at `4.0.0_SA_CRO` (*cost attribution on the served graph,
producer-side, with a Cost Explorer vintage*), lane `0.8.0_AE_CloudComp`, carried on the roadmap's allocation. Adding FWD-9 here
would widen an endpoint Andrew ratified at eight, under his same-session "no new work".

## 4. Instruments, so repetition can be told from corroboration

This seat's own reads before grading, each a different instrument from the CVO's on the same fact: `git ls-files` on the writer
(0 -- untracked at HEAD; the CVO used `git log --diff-filter=D`); `ls -d` over `infra/aws/globgrph/kuzu_*` (the canonical store
ABSENT; `kuzu_db`, `kuzu_ac7.db`, `kuzu_stitch_db` PRESENT with their manifests; the CVO used `test -e`); a count of
`derive-runner:latest` over the globgrph `.tf` files (the four producers on the DECLARED plane; the CVO read the APPLIED plane with
`describe-task-definition` on 9 families); `Grep` over `graph-call-manifest.yaml` for `--mode|cloud\.refresh|retired_aliases`
(`:219`, `:233`, `:1783`, and the file's own `retired_aliases` convention at `:35-49`; the CVO EXERCISED the call and read the
refusal). Not re-run here: any battery, any gateway ask, any live AWS read -- the CVO's are cited with their instrument.

## 5. What travels, and to whom -- named with an owner, none a row of this project

- **At this seat (design surface), carried behind Andrew's "no new work":** S34 (the drain destroys a worker's untracked
  NEVER-2 sentinel; `safe-merge.sh` carries no sentinel handling), S35 (a seat swept by another seat's drain cannot tell; 14b is
  policy not mechanism), W1-S11 (the halt gate reads only the session-keyed serial file, never `OPAL_AGENT_SERIAL`), W3-S3/S4/S5
  (a worker DOES write telemetry; a linked-worktree read cannot see it; rows land under a sibling slot's serial), W2-S18
  (`pipescript-suite-check.sh:195` writes under `.git/` and cannot run in any linked worktree), W2-S19 (proof-of-spec-check's
  `introduces` substring limb), W2-S20 (`test_comp_cluster_cli`'s page-count oracle). Every one is a spine-tooling mechanism, and
  the brief-to-cut chain (DONE WHEN confirmed today @`6ccebb9ae5`) is where the cut-time family lands; the rest queue at this seat.
- **S26 (the user-bin shim DACLs):** DISARMED on the CVO's unscoped Get-Acl after today's provisioning run (211 files, 0 protected,
  0 deny-bearing), REMEDIATED at the writer @`e4167f3c3b`; its acceptance is a FRESH Codex seat through `ajb2`, which Andrew's
  ~14:3xZ word (*~Y work later, off the carried calls*) defers. Stays open on the record, honestly.
- **To `0.7.0_AE_CloudOps`:** the four live-plane drifts W2-S2, W1-S3, W1-S8, W2-S10 -- each a ruling that lane owes on its own
  Terraform surface; and S18 above.
- **To their owners as historical records, not rows:** the two out-of-lane `_canonical` importers that now fail loud rather than
  rebuild -- `0.4.0_DS_ClientPlatform`'s `NFRA_EDGES_P3_c3_subgraph.py:427` and `0.8.0_AE_CloudComp`'s
  `sensor_kuzu_schema_residue.py:216` (S62).
- **To `4.0.0_SA_CRO`, an L1 candidate on the roadmap:** cost attribution on the served graph (section 3's correction); and, still
  standing from round 3, the ~2,256 duplicate edge identities in the derive SOURCE (S8's second-order question).
- **W1-S17** (STAMP->ANSWER's two readings): a wording rule for any future face -- *the clock stops when the served answer first
  carries the vintage*, ruled at C-S12; carried into the next cut by the issuer.

## 6. Handoff

`dep_stage: ROUND_CLOSE` on this commit (the row owner). Not CLOSED: FWD-7 grades NOT_REALIZED and R6 is right to refuse --
**the estate runs one graph and still tells its seats how to rebuild the old one.** This file, `COMPLETION_GRADES.round4.json` and
the PRD v0.5 go to `2.0.0_SA_COO~A` in the CTO's one message of the round; the COO recuts as ONE issuance covering S17-S20 (S17
and S19 at `0.8.0_AE_CloudComp`, S18 at `0.7.0_AE_CloudOps`, S20 after S19), `dep_stage: EXECUTING` is the COO's flip in the
issuance commit, and S17's clause (2) reads EXERCISED only on the roadmap's site-Z allocation. Nothing here returns to Andrew.
