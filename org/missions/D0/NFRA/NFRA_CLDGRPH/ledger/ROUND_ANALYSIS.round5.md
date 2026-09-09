# NFRA_CLDGRPH -- ROUND-5 ANALYSIS (L10, the CTO's read of the slug) -- 2026-09-09 ~17:4xZ

**Reader:** `1.0.0_SA_CTO` (the single router, spine v3.6 L10). **Slug:** `3.0.0_SA_CVO` message 94599, record
`../surprise-channel/adjudications/ADJUDICATION_v1.md` C-S26..C-S39 and `../surprise-channel/remediations/REMEDIATION_v3.md`
@`8678d0018d`, on `2.0.0_SA_COO~A`'s FINAL packet `L8_PACKET.round5.final.md` and `COMPLETION_REPORT.round5.json` @`25040e93f2`.
**Precondition, the CVO's own lines:** 4 of 4 round-5 orders terminal (TO-CG-E-1..E-4), 24 of 24 project orders terminal with VALID
instances; 4 of 4 judgment criteria graded PASS (E3-AC6 C-S26, E2-AC7 C-S29, E4-AC6 C-S33, E1-AC7 C-S36; the project's 15 of 15 across
rounds 3-5); investigation items open 0 of 151 after commit; S31 CLOSED on the measured 7 of 7 pins. **Prior:** ROUND_ANALYSIS.round4
@`707ba2a4c9` (*a retirement has three planes*), PRD v0.5 @`707ba2a4c9`, Andrew's words: *"we can switch off laptop copy"* @`61d5ef55dd`,
*"/drive NFRA_CLDGRAPH to completion"* (~13:1xZ at the `~A` terminal), **"Recs approved" ~17:3xZ at this terminal** (the site-Z exercise
ALLOCATED FIRST, record `ANDREW_DIRECT_20260909_173xZ_RECS_APPROVED_SITEZ_FIRST_PY314_RESIDUE_LEFT_M2M3_AFTER_ROADMAP.md`).
**Answer:** a **PRD ADDENDUM v0.5 -> v0.6** (eight rows, section 3, and two rulings ratified into s.6) AND the round analysis:
8 of 8 outcomes served by cells, 7 of 8 REALIZED, FWD-7 NOT_REALIZED by two OWNED acts, one of which Andrew allocated today.
**Grades:** `COMPLETION_GRADES.round5.json` beside this file. **Push state at write:** LOCAL; origin/CLOUD @`7e35640ec8` (ls-remote 17:35Z).

## 1. The three planes, as the record reads after round 5

| plane | round-4 state | round-5 delivery | the CVO's read |
|---|---|---|---|
| EXECUTABLE | clean (seam 0 of 3; consumers opening a local DB 0 of 29; the writer deleted; the canonical copy switched off 6 -> 0; two machines byte-identical under one vintage) | unchanged | unchanged |
| INSTRUCTION | the manifest routed a repointed consumer back through `comp-kuzu --mode`; six help texts and three code sites sold the retired surface | CG-s-17 / E-1 (two passes @`ed674cd511`): the two refresh entries RETIRED under the file's own per-entry schema (`status: retired` + `superseded_by`/`retired:`/`why:`) with the READ successor `cloud.read.served_vintage`; `comp-which`'s curated routes and every registry carrier repointed; the compiled index REGENERATED from a classification whose population is the coverage map (the SOLE authority by this seat's ruling), never hand-edited; LIVE_ROUTES_BACK 0 of 126, RETIRED_ROUTES 0 of 3 phrasings, HELP_ROUTES_BACK 0 of 8 | E1-AC7 PASS (C-S36), verified at HEAD by its own enumerate: `:251`/`:268` `status: retired`, the historical call form kept one grain up in `retired_aliases` only; `tool_index.py` 0 hits of the store in 6,647 lines |
| RESIDUE | two local stores held do-not-delete by the CVO's P7; the stitch graph's home undecided; four `:latest` producers | CG-s-19 / E-3 @`d3a03a7b7b`: the four local artifacts DISPOSITIONED from a closed vocabulary, nothing deleted, 0 readers of 487 files by AST, the S53 claim stamped by both builders; CG-s-20 / E-4 @`49fea6980a`: the stitch graph's HOME = JOIN_PROJECTION with four later-round cells named with lanes and an ORDER; CG-s-18 / E-2 @`a302d9ebb8`: 7 of 7 families by DIGEST, the apply set measured at TEN addresses (the launcher roles' revision-scoped RunTask grants -- a four-address apply would have gone green and failed three nightlies), the ECR tag's digest unchanged, R13 in force | E3-AC6 PASS **and the P7 hold LIFTED by its author** (C-S26: `kuzu_db` is a June-12 copy of THIS graph, 0 readers by two instruments, REPRODUCIBLE from `snapshots/20260612/graph-20260612.tar.gz` in S3; RETIRE_WITH_TOMBSTONE, owner CloudComp; `kuzu_ac7.db` archived under NFRA_GLOBGRPH.ITEM-3); E4-AC6 PASS (C-S33); E2-AC7 PASS (C-S29, 7 of 7 live); S31 CLOSED |

**Beneath the residue plane, the round's finding (W3-S10, C-S34):** the cloud stitch producer `opal-stitch-produce` has NEVER
succeeded -- 67 of 67 CodeBuild builds FAILED from 2026-07-07 to 2026-09-09 on an ENABLED nightly rule, `derive_stitch.py` exit 2 in
~30 s on a July source snapshot never re-pushed; the artifact in S3 was written by a laptop (`producer=stitch-local`). **Silent by
construction: a failed nightly leaves the previous artifact in place, so every consumer sees a plausible object.** The JOIN was decided
on a substrate that produces nothing today, and E-4's record names the repair as the first of its four cells. W3-S11 beside it: the local
stitch store's bytes are 51 days younger than their manifest, the capable mutator inferred as the deleted writer; the remedy is a
manifest field, not a hunt.

## 2. Per outcome: the grade, and why FWD-7 is exactly two acts from REALIZED

| outcome | grade | basis |
|---|---|---|
| FWD-1, FWD-2, FWD-3, FWD-4, FWD-5, FWD-6, FWD-8 | **REALIZED** | unchanged from round 4 (`COMPLETION_GRADES.round4.json` @`707ba2a4c9`); no round-5 cell touched their artifacts; FWD-6's residue (the manifest offering `--mode`) is now gone with E-1 |
| FWD-7 | **NOT_REALIZED** | the three planes are clean, retired and dispositioned; two OWNED acts remain, neither a new cell shape: (i) the EXISTENCE clause -- *no second, older copy anyone could still be reading from* -- is met only when the LIFTED dispositions are EXECUTED (`kuzu_db` retired with a tombstone naming its tarball key; `kuzu_ac7.db` archived and removed; `kuzu_load.py` retired or rescoped -- a builder beside the projection is the path back); (ii) the PERSON half -- *two people on different machines* -- is MODELLED (one worker on two machines, C-S36's four conjuncts named, none exercised) until a site-Z seat asks D-8's fixed question, **which Andrew ALLOCATED FIRST today**. The stitch JOIN is decided, not built; its four cells are FWD-7's by this PRD's arc, and their absence does not put the canonical graph's story in question -- it puts the stitch graph's story in a future round |

**Coverage verdict:** 8 of 8 served; no `DECOMP_INVALIDATING`; no cell invalidated. **Realization verdict:** 7 of 8, and the eighth is
two placed acts away, one of them started by Andrew's word.

## 3. THE ADDENDUM v0.5 -> v0.6 -- eight rows, two rulings, all placed by the record and now owned

| id | outcome | surface | lane | verb | depends_on | accept (the load-bearing clause) |
|---|---|---|---|---|---|---|
| **S21** | FWD-7 (existence) | EXECUTE THE LIFTED DISPOSITIONS: `kuzu_db` RETIRE_WITH_TOMBSTONE naming `snapshots/20260612/graph-20260612.tar.gz`; `kuzu_ac7.db` ARCHIVED under NFRA_GLOBGRPH.ITEM-3 then removed locally; `kuzu_load.py` retired or rescoped to a NAMED reader (C-S26's notes) | `0.8.0_AE_CloudComp` | retire | S19 (DONE) | `ls -d` reads 0 of 2 stores on this device beside a positive control; the tarball and the archive objects present by head-object with their sha256 in the tombstone/manifest; the reader census still 0 with its control; nothing deleted before its archive object is verified |
| **S22** | FWD-7 (person half) | THE SITE-Z EXERCISE, S17 clause (2) lifted into its own row on **Andrew's allocation ~17:3xZ**: a seat on site Z and a seat on this laptop ask D-8's fixed question through the public gateway inside D-8's window and receive byte-identical answers under ONE vintage, with no local copy on either machine | site Z's seat (via `0.0.0_AB_MSTR`'s agentbus) + `2.0.0_SA_COO~A` on the laptop; fabric `site-z` + `laptop` | verify | S17 (DONE), S21 (the exercise reads on a device with no local copy) | two answers from two machines driven by two SEATS, byte-identical, one vintage, WINDOW_S inside D-8's (4.229 s, or the window the face states), each machine's local-copy census 0 with a control; the CVO grades against both records |
| **S23** | FWD-7 (the stitch JOIN, cell 1 of 4) | REPAIR THE CLOUD STITCH PRODUCER: `opal-stitch-produce` 67 of 67 FAILED since 2026-07-07 on a July source snapshot (W3-S10) | `0.7.0_AE_CloudOps` (the producer's Terraform, the source push) with `0.8.0_AE_CloudComp` (`derive_stitch.py`) | repair | -- | the exit 2 REPRODUCED on the snapshot as pulled before any fix (diagnosed on the snapshot, not HEAD); the source re-pushed from HEAD under a NEVER-2 entry; `list-builds` reads SUCCEEDED for a rule-initiated nightly with its artifact's manifest carrying `producer=stitch-cloud` and a `built_at` inside that night; **a night that DID NOT RUN reads differently from one that did** -- with the rule disabled the consumer reads NO-RUN/STALE by vintage, never a plausible object |
| **S24** | FWD-7 (cell 2) | THE PROJECTION CARRIES THE STITCH SOURCE: the derive includes the stitch tables; the served manifest declares a stitch source vintage beside its Nessie one | `0.8.0_AE_CloudComp` | build (an IMAGE act under R13) | S23 | a thin-client query for the stitch node types returns non-zero from the served graph with the stitch vintage on the VINTAGE line; the NEVER-2 entry names all seven families |
| **S25** | FWD-7 (cell 3) | `comp-debt`'s SECOND LEG repointed through the thin client to the served stitch source (W2-S17) | `0.8.0_AE_CloudComp` | port | S24 | `comp-debt` answers its stitch leg from the served graph inside its budget with the vintage disclosed; it opens no local store (census 0 with a control) |
| **S26** | FWD-7 (cell 4, LAST) | THE LOCAL STITCH STORE RETIRED with a CG-s-19-shaped disposition: `kuzu_stitch_db`, `kuzu_stitch_load.py` -- after the repoint, or a labelled refusal becomes a crash (C-S33) | `0.8.0_AE_CloudComp` | retire | S25 | the store absent on this device with its archive object verified; `comp-debt`'s refusal text names the served source; no builder beside the projection remains |
| **S27** | -- (S53's consuming half; W3-S7, W3-S8, W3-S11) | THE MANIFEST CONTRACT: `_provenance.write_manifest` accepts and stamps the claim for all four producers (`edge_count_semantics` stored\|attempted, `content_sha256`, `bytes_written_at`, so bytes newer than a manifest are detectable); `format_provenance_header` prints the claim beside the counts and keeps the `!!` prefix for any `source_kind` beginning UNKNOWN or `provenance_claim: absent` | `0.8.0_AE_CloudComp` | fix | -- | one manifest of each producer read with the field; the rendered header shows the claim beside the counts; a manifest-less store still prints `!! UNKNOWN VINTAGE` (the negative arm W3-S8 measured); a store whose bytes are newer than its manifest reads so |
| **S28** | FWD-7 (instruction residue) | THE LAST TWO DESCRIPTIONS OF THE DEAD ENGINE and the normaliser: `gen_tool_classification.py:80` `REFRESH['GRAPH-DB']` ("auto-refresh on HEAD-advance") fanning to every GRAPH-DB tool in the compiled index (`tool_index.py:2936`); `manifest_check_cli.py:211` ("hit the canonical persisted Kuzu DB"); `gen_tool_registry.norm_tool()` strips `.py` and not `.sh`, so one tool prints as a fifth exclusion that is not a retirement (W2-S35, W2-S37) | `0.8.0_AE_CloudComp` | fix | -- | 0 hits of both phrases in the regenerated index and the checker beside a positive control; the normaliser handles `.sh` so EXCLUDED_NOT_IN_AUTHORITY reads 4 of N; regenerated, never hand-edited |

**Two rulings ratified into s.6 from C-S39:** **R14** -- `graph-call-manifest.yaml`'s per-entry `status: retired` (with `superseded_by`,
`retired:`, `why:`) is the entry-grain retirement value; `deprecated` is tool-grained in its only consumer and is not used for an entry.
**R15** -- every future face's retired-record exemption reads *"a declared retired RECORD (alias-name OR entry)"*, so an honest record is
never scored as an instruction.

## 4. Instruments at this seat, so repetition can be told from corroboration

The slug's facts were read at their commits (`git show` at `8678d0018d` and `25040e93f2`; the grades' instances at their pins), not from
the messages. Not re-run here: the CVO's live `describe-task-definition` over the seven families, its `list-builds`/`batch-get-builds`
census over the 67 stitch builds, its head-object on the June tarball, and its manifest enumerate -- each is cited with its instrument
and its vintage, and this read adds no second instrument on the live plane today; the addendum's accepts are what the next round
measures with fresh ones.

## 5. What travels, and to whom

- **Cut discipline for the issuer, from the round's own rows (not PRD rulings):** a probe's NAME carries its order id (three instances
  of one cut defect this round -- W1-S31, W2-S34, W3-S13); *"together"* at the flip means the PENDING-THIS-COMMIT form or two commits, and
  the face says which (W2-S39); the slot-folder naming rule the issuer adopted at the cut (S65). These ride the brief-to-cut chain's L4 as
  measured instances.
- **At this seat, held behind Andrew's "no new work":** S34 (the drain destroys a worker's untracked NEVER-2 sentinel) and S35 (the
  swept seat cannot tell) -- spine-tooling mechanisms; W1-S27 (the halt gate's identity axis, W1-S11 recurred).
- **S26 (the shim DACLs):** DISARMED and REMEDIATED, closed false on its Codex-seat acceptance -- now reachable, since `1.0.0_SA_CTO~X`
  runs under 3.12 after today's runtime fix; the acceptance is a fresh Codex seat through `ajb2`, Andrew's launch, and it lands the
  first time one is launched for any purpose.
- **To `0.7.0_AE_CloudOps`:** W1-S30 (`serving.tf:11-16`'s comment falsified by the pins) and the four live-plane drifts of round 4.
- **To `0.8.0_AE_CloudComp`:** W2-S35/W2-S37 (S28 above), W3-S7/S8/S10/S11 (S23, S27 above) -- all now rows, not names.
- **To `0.0.0_AB_MSTR`:** carry S22 to site Z over the agentbus when `2.0.0_SA_COO~A` cuts it; the exercise needs a seat there and a seat here.

## 6. Handoff

`dep_stage: ROUND_CLOSE` on this commit (the row owner). Not CLOSED: FWD-7 is NOT_REALIZED by two owned acts and R6 is right to refuse.
This file, `COMPLETION_GRADES.round5.json` and the PRD v0.6 go to `2.0.0_SA_COO~A` in the CTO's one message of the round; the COO recuts
as ONE issuance covering S21-S28 (S21 and S22 first -- S22 on Andrew's allocation, with a site-Z seat via MSTR; S23 on CloudOps; S27 and
S28 beside them; S24 -> S25 -> S26 in order, S26 LAST), `dep_stage: EXECUTING` is the COO's flip in the issuance commit. Nothing here
returns to Andrew: the one thing that was his -- the site-Z allocation -- he gave today.
