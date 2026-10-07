# TO MDPF_SECCLASS.TO-SC-e45 -- round 9 SC-e-45: FWD-5 -- the three old-list writer stops re-presented after the readers switch

<to_id>MDPF_SECCLASS.TO-SC-e45</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~31</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** DELL1 | **Decomp cell:** `SC-e-45` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-5 | **depends_on:** MDPF_SECCLASS.TO-SC-e41, TO-SC-e42, TO-SC-e43, TO-SC-e44 drained AND the issuer act "producer live"
(TO-SC-e44's module deployed, then a run with a live canonical write count above 0) -- start only when the issuer hands you this order.
Slot ~31's second order, after `TO-SC-e41`.

---

## WORKER FACE

### THE CELL

`SC-e-45`: re-present round 8's three old-list writer stops at the round-9 base: bring their served work onto your branch, re-prove it,
and re-write their three half requests so each names every real reader's switch and the canonical producer's live write count.

- Why: round 8 built the stops (TO-SC-e35 Black Diamond, TO-SC-e36 Cottonwood, TO-SC-e37 Inflection) but they were superseded and carried:
  1.0.0_SA_CTO~DELL1 REFUSED the SC-e-35 half because readers outside the BD tree were unnamed, and round 8's trace then found 5
  NEEDS-OLD-LIST readers with no canonical producer. The round-8 analysis section 2.10: no old-list writer stop uploads until every real
  reader resolves canonical-first and names a canonical producer with a live write count above 0. Round 9's TO-SC-e41 (census),
  TO-SC-e42 (a07), TO-SC-e43 (resolve_tickers) and TO-SC-e44 (the producer's input) are that condition's cells.
- **Bring the work over:** the served commits sit on branch `wk-MDPF_SECCLASS-27`, off every pushed range:
  `42239a4f2a` (BD: B_01b leaves `data/black_diamond/scripts/gold/gold_dispatch.sh`; five writers exit 3 with `RETIRED:`),
  `b8b17cbbdd` (Cottonwood: B_01b leaves `data/cot/scripts/gold/gold_dispatch.sh`; its writer exits 3),
  `6a996787eb` (Inflection: `data/inf/scripts/classification/classify_assets.py` exits 3).
  Run `git cherry-pick 42239a4f2a b8b17cbbdd 6a996787eb` onto your branch, in that order, and nothing else from that branch. A conflict
  is resolved to the cherry-picked side only where the base file is otherwise unchanged; any other conflict is a stop and a row.
- **Re-prove:** the three round-8 issuer checks pass (`R10_CHECKS/r10_{bd,cot,inf}_old_list_writer(s)_check.py`), and the BD and
  Cottonwood gold tests still pass (two separate pytest processes: the two trees share test file names and a `lib` package).
- **Re-write the three half requests** (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_{BD_OLD_LIST_WRITERS,COT_OLD_LIST_WRITER,INF_OLD_LIST_WRITER}_20261007.md`):
  bring each up to date with its round-8 content (the BD one carries the issuer's COO half and the CTO's refusal: keep both, and add a
  dated re-presentation note), and add a `## Readers switched` section with one `READER:` line per real reader of
  `M/OLD_LIST_READER_TRACE_20261007.md` and the newest `M/OLD_LIST_READER_TRACE_BD_*.md` (verdict NEEDS-OLD-LIST or REPOINTABLE): the
  reader, its switch (the round-9 order and commit, or "canonical-first already"), and its served result for a newly held security
  after the switch; and one `PRODUCER-LIVE-WRITES: <n>` line, the canonical producer's live write count from a read-only scan of
  `etf-classifications` by `updated_by` for the producer's own value after the issuer's "producer live" run. Every rollback VersionId
  is re-read with `list-object-versions` at your run, not copied from round 8.

### ACCEPTANCE

<criterion id="SC9-e45-AC1" cell_refs="SC-e-45"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/issuer_check_sc_e45.py</invocation><expect>SC-E45-STOPS ok=True</expect></criterion>
`SC9-e45-AC1` -- the three stops are re-proved, and each half names every real reader's switch and a live producer write count above 0.

<criterion id="SC9-e45-AC2" cell_refs="SC-e-45"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e45-AC2` -- control: the Black Diamond gold tests still pass with the BD stop applied.

<criterion id="SC9-e45-AC3" cell_refs="SC-e-45"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/cot/scripts/gold/tests</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e45-AC3` -- control: the Cottonwood gold tests still pass with the Cottonwood stop applied.

<expected_criteria>SC9-e45-AC1,SC9-e45-AC2,SC9-e45-AC3</expected_criteria>

Dry-run at the base 2026-10-07: AC1 FAIL as expected (`ok=False checks=0 of 3 halves=0 of 3 readers=5`); AC2 PASS as expected (control,
76 passed); AC3 PASS as expected (control, 21 passed).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding under `.scratch/`, uncommitted.
  The issuer checks under `R10_CHECKS/` and `R11_CHECKS/issuer_check_sc_e45.py` are READ-ONLY to you.
- **SHIPPED FILES.** The BD and Cottonwood gold scripts are uploaded by the pre-push deploy gate at a push. Your commits stay on YOUR
  branch; the issuer holds them off every pushed range until both halves of each stop sign. Never push.
- **No deploy, upload, trigger change, table or S3 write, no model or vendor call.**
- **NO package install and NO download of any kind** (row S49).
- Lint that predates an edit on a file you own: fix annotation- or comment-only, no runtime change; say so in a row.
- **Refusal clause.** If a criterion cannot be met as written (for instance the producer has no live writes yet), stop, write the reason
  in your report and a surprise row (id `MDPF_SECCLASS-W31-S<k>`), and do not weaken the test.

<paths>
data/black_diamond/scripts/gold/gold_dispatch.sh
data/black_diamond/scripts/gold/B_01b.classify_new_securities.py
data/black_diamond/scripts/classification/classify_bd_securities.py
data/black_diamond/scripts/classification/seed_bd_securities.py
data/black_diamond/scripts/classification/seed_canonical_securities.py
data/black_diamond/scripts/classification/backfill_name_aliases.py
data/cot/scripts/gold/gold_dispatch.sh
data/cot/scripts/gold/B_01b.classify_new_securities.py
data/inf/scripts/classification/classify_assets.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_OLD_LIST_WRITERS_20261007.md
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_OLD_LIST_WRITER_20261007.md
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_INF_OLD_LIST_WRITER_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-45`.
<owned_cells>SC-e-45</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e45-AC1, SC9-e45-AC2, SC9-e45-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~31/MDPF_SECCLASS.TO-SC-e45.writer-stops-represented.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e45-AC1,SC9-e45-AC2,SC9-e45-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the cherry-picked commits as they land on your branch, the three round-8 check lines, the readers named in each half with
their switch, the producer's live write count and how it was read, every re-read rollback VersionId, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN -- the BD stop's first affected run is bd-gold-nightly-fallback (cron(0 23 ? * MON-SAT *)); Cottonwood's live chain is SSM opal-cot-gold-run, which skips B_01b (row W27-S3); the halves re-read the schedules at the act.
comp-iam: DECLARED-NOT-APPLICABLE no grant changes; the uploads are the issuer's acts under each stop's own pair.
comp-adversary: RUN -- the stops wait on every real reader's switch and a live producer (ruling 2.10; the CTO's SC-e-35 refusal @a92652a41a); the check re-derives the reader set from both traces, so a reader the halves skip fails AC1; cherry-pick of exact commits keeps unsigned bodies out. BLIND: an out-of-repo caller of a writer (each exits 3 with RETIRED: if invoked).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.13 @90f99888cd (FWD-5); CTO round-8 analysis @1ca9e97fc9 sections 2.10 and 4 item 1; DECOMP_R9 @5d70aab6c9; R8 orders TO-SC-e35/36/37 (superseded @5b55dce508).
