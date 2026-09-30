# TO MDPF_SECCLASS.TO-SC-t3 -- thread hops 3-4: BD composition artifacts and client portal summary carry the canonical class; the thread's half

<to_id>MDPF_SECCLASS.TO-SC-t3</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~3</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~M</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `SC-t-3` (`decompositions/MDPF_SECCLASS_DECOMP.md`) |
**outcome_ref:** FWD-1 | **depends_on:** SC-t-2

---

## WORKER FACE

### THE CELL

`SC-t-3`, thread hops 3-4 (PRD section 2):
- "BD assets dimension -> BD gold composition artifacts (`data/black_diamond/scripts/gold/D_03.composition_artifacts.py:116`)
  carry the canonical class per holding"
- "-> the served BD client surfaces (the advisor-facing composition artifacts and the client portal summary the BD gold
  chain serves) read on the page for one real client on the latest trading day".

Your previous orders moved the library (SC-t-1) and the assets dimension (SC-t-2) onto `etf-classifications`, with no
fold, no guess, and unclassified by name. Build on your branch.

The gold readers of the library:
- `D_03.composition_artifacts.py` (`classify_series` :116, "with cash/other post-processing");
- `D_04.client_portal_summary.py` (`_classify` near :1235, and its mix snapshot from C_06's `gold/views/mix_daily_summary.json`);
- `C_06.client_mix_timeseries.py`.
Any caller fallback that turns unknown into a class ("caller fallback (typically equity)", the library's own
docstring) is a guess, and it goes: unknown stays unclassified, by name, in each artifact.

**Build (LOCAL build + record: no upload, no deploy):**
1. `D_03`, `D_04` and `C_06` carry each holding's canonical class and sub-class, plus a `class_source`, and fall back
   to no class. Keep the cash rules (cash is not a class copy).
2. **Tests** in `data/black_diamond/scripts/gold/tests/test_composition_canonical.py`:
   - GLD, PHYS and VXX in the composition and the summary carry their canonical classes;
   - an unknown holding is unclassified by name, not equity;
   - the cash line is unchanged.
3. **Census** from a REAL local build of C_06, D_03 and D_04 on the latest BD day, written to
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_GOLD_CENSUS_20260929.json` as
   `{"as_of", "artifacts": [...], "rows", "class_sources": {...}, "unclassified", "unclassified_names": [...],
   "client_page": {"client": <a real BD client id holding GLD, PHYS or VXX where one exists>, "values": [{"ticker",
   "asset_class", "sub_asset", "class_source", "weight"}]}, "moves": [{"ticker", "before", "after", "artifacts"}]}`.
4. **The thread's half.** Write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_20260929.md`
   (`## The act`, `## Blast radius`, `Rollback per key`), for deploying SC-t-1..3 on the BD chain. It covers:
   - every BD-held ticker whose class moves, including GLD, PHYS and VXX, from the three censuses, read back after;
   - the served artifacts and their readers (the advisor composition, the client portal summary, the mix timeseries);
   - the IAM read on `etf-classifications` the BD principal needs (named in SC-t-1's census), as desired, not applied;
   - the deploy mechanics (DS lane `.tools/safe-deploy.sh`, firm tree kept);
   - the release order: after SC-k-1's backfill write, so that holdings the backfill resolves are not shown
     unclassified in between;
   - rollback per artifact key, from the prior object versions.

### ACCEPTANCE

<criterion id="SC1-t3-AC1" cell_refs="SC-t-3"><invocation>python -m pytest data/black_diamond/scripts/gold/tests/test_composition_canonical.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`SC1-t3-AC1` -- the gold surfaces carry canonical classes, and an unknown is not equity.

<criterion id="SC1-t3-AC2" cell_refs="SC-t-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_CHECKS/r1_bd_build_census.py gold</invocation><expect>BUILD-CENSUS</expect></criterion>
`SC1-t3-AC2` -- a real local gold build, with one real client's page values each sourced from the canonical table.

<criterion id="SC1-t3-AC3" cell_refs="SC-t-3"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_20260929.md</invocation><expect>HALF-READY</expect></criterion>
`SC1-t3-AC3` -- the thread's half, for the issuer to sign and send.

<expected_criteria>SC1-t3-AC1,SC1-t3-AC2,SC1-t3-AC3</expected_criteria>

Dry-run at the base 2026-09-29 22:0xZ: AC1 "no tests ran", AC2 NOT-CENSUSED, AC3 NOT-READY -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** Reads `opal-data-bd`; no upload, no deploy.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W3-S<k>`), and do not weaken the test to pass.

<paths>
data/black_diamond/scripts/gold/D_03.composition_artifacts.py
data/black_diamond/scripts/gold/D_04.client_portal_summary.py
data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py
data/black_diamond/scripts/gold/tests/test_composition_canonical.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_GOLD_CENSUS_20260929.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_THREAD_20260929.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP.md</decomp_doc> (round 1), cell `SC-t-3`.
<owned_cells>SC-t-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC1-t3-AC1, SC1-t3-AC2, SC1-t3-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~3/MDPF_SECCLASS.TO-SC-t3.bd-gold-surfaces-canonical.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC1-t3-AC1,SC1-t3-AC2,SC1-t3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three scripts' changes, the gold census (rows, sources, unclassified, the client page, moves), the
half's path, the pytest line, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the BD gold schedule is unchanged.
comp-iam: RUN -- 1 file read (infra/aws/terraform/bd-pipeline/iam.tf, the BD role definitions); BLIND: whether the production principal of the gold scripts can read etf-classifications is unmeasured at the cut; this cell's half drafts the grant (desired only).
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; decomposition findings inlined (the three gold readers; caller fallback to equity).
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.1 section 2 hops 3-4 (S05; D_04 and C_06 as the library's served readers).
