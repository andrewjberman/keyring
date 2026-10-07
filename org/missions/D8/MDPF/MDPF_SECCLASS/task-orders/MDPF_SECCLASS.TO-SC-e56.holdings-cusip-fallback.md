# TO MDPF_SECCLASS.TO-SC-e56 -- round 9 SC-e-56: S27 (folds R8 SC-e-39): the Holdings producer falls back to CUSIP:<security_id> after a symbol miss

<to_id>MDPF_SECCLASS.TO-SC-e56</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~38</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-56` (`decompositions/MDPF_SECCLASS_DECOMP_R9.md`) |
**outcome_ref:** FWD-13 | **depends_on:** none (slot ~38 queue: after TO-SC-e55 and TO-SC-e57)

---

## WORKER FACE

### THE CELL

`SC-e-56`, which FOLDS round 8's `SC-e-39` (laptop 1.0.0_SA_CTO msg 106191, relayed by 0.0.0_AB_MSTR~DELL1 msg 213: "SC-e-39 is
PLACED on dell1, folded into R9's SC-e-56 under 2.0.0_SA_COO~M1; both edit
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py and one file takes one writer ... its RELEASE goes through
IRPT_BCKEND's path and halves").

**The cell, as folded:** R8 SC-e-39: "The Holdings producer tries `CUSIP:<security_id>` after a symbol miss; the 187 securities it
newly places listed before; the producer's `multi_asset` line removed; the half request". Round-8 analysis section 3, S27: "YES. After
a symbol miss the producer falls back to `CUSIP:<security_id>` (C-IDENTITY: the CUSIP rows exist for exactly this). It is a served move
under never-widen."

**Measured at the cut (5d70aab6c9):**
- `holdings_snapshot.py` `_NarrowedClassifier.canonical_lookup(ticker)` (~:882-887) asks the canonical table by the upper-cased symbol
  only; `classify_security()` (~:938-962) is canonical-first, then the bd-securities fallback; its only caller,
  `annotate_classification()` (~:999-1010), passes the node's display symbol and description. Nodes already carry `security_id`
  ({namespace, value}): `holdings_49f.py` `_security_identifier()` (~:163-169) puts CUSIP first; read `holdings_inf.py`'s and the
  Cottonwood builder's (`_cot_security_identifier`, ~:1968) identifiers before you rely on one. Neither firm builder calls the
  classifier: they are READ-ONLY context here.
- `ASSET_CLASS_VALUES` (~:846-847) still admits `multi_asset` ("CTO batch 164 (readers first)"); the table holds 0 `multi_asset` rows
  (rule-B remap) and the six-class module is live.
- The firm buckets deny this box's principal (row W25-S1) until NFRA_CTLPLN's read-only fence join applies: the "held" read is a LOCAL
  producer build per firm, without `--upload`, marked `inferred` (as TO-SC-e26 and TO-SC-e33 did).

**Build:**
1. After a symbol miss, a node whose `security_id.namespace` is CUSIP is looked up as `CUSIP:<value>` (upper-cased) in the canonical
   table; a hit is served exactly as the canonical row holds it, `class_source` canonical; a miss goes on to the fallback as today.
   Never the reverse order, never blended.
2. `multi_asset` leaves `ASSET_CLASS_VALUES` (a canonical row reading it would now be refused loudly, which is the six-class rule).
3. The before-list: `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/holdings_cusip_newly_placed.py` builds each firm's held nodes locally (as-of the latest built date),
   and writes `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/HOLDINGS_CUSIP_NEWLY_PLACED_20261007.json` with every security the CUSIP step newly places (symbol misses that the
   CUSIP key answers), shaped as the issuer check reads it, `source` naming the build and `inferred`. Round 8 held 187; re-measure.
4. Tests in `data/assets/scripts/gold/investor_reporting/tests/test_holdings_cusip_fallback.py`: a symbol miss with a CUSIP id is placed
   by the CUSIP row; a symbol hit never consults the CUSIP key; a CUSIP miss falls back; a `multi_asset` canonical row is refused.
   Run `test_holdings_snapshot.py` and `test_holdings_narrowed.py` too and report them.
5. The half request `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_HOLDINGS_CUSIP_LOOKUP_20261007.md`, addressed to IRPT_BCKEND's release path and
   halves (the CTO ruling): the act, the newly placed securities per firm with their dollars (the before-list), every reader of the
   served Holdings snapshot, both branches, rollback, both halves UNSIGNED.

**Shipped file:** `data/assets/scripts/gold/` is a shared home the pre-push deploy gate ships (`.tools/safe_deploy_core.py`
`shared_repo_homes`): your branch stays OFF every pushed range until both halves sign.

### ACCEPTANCE

<criterion id="SC9-e56-AC1" cell_refs="SC-e-56"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/assets/scripts/gold/investor_reporting/tests/test_holdings_cusip_fallback.py</invocation><expect>PYTEST-OK</expect></criterion>
`SC9-e56-AC1` -- the CUSIP fallback, its order, and the multi_asset refusal.

<criterion id="SC9-e56-AC2" cell_refs="SC-e-56"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/sc_e56_newly_placed_check.py</invocation><expect>SC-E56-NEWLY ok=True</expect></criterion>
`SC9-e56-AC2` -- the before-list is true against the table: each listed security misses by symbol and is held by its CUSIP key.

<criterion id="SC9-e56-AC3" cell_refs="SC-e-56"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_HOLDINGS_CUSIP_LOOKUP_20261007.md</invocation><expect>HALF-READY</expect></criterion>
`SC9-e56-AC3` -- the half request to IRPT_BCKEND's release path carries the act, blast radius, both branches, rollback, two UNSIGNED halves.

<expected_criteria>SC9-e56-AC1,SC9-e56-AC2,SC9-e56-AC3</expected_criteria>

Dry-run at the base (5d70aab6c9, 2026-10-07): SC9-e56-AC1 FAIL as expected (PYTEST-BAD, no test file); SC9-e56-AC2 FAIL as expected (no HOLDINGS_CUSIP_NEWLY_PLACED file); SC9-e56-AC3 FAIL as expected (NOT-READY: half absent).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, curl or tool fetch, into any environment; row S49).
- No upload, no publish, no S3 write: local builds run without `--upload`.
- Never push: a shipped shared-home file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W38-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test.

<paths>
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/investor_reporting/tests/test_holdings_cusip_fallback.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/holdings_cusip_newly_placed.py
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/HOLDINGS_CUSIP_NEWLY_PLACED_20261007.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_HOLDINGS_CUSIP_LOOKUP_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R9.md</decomp_doc> (round 9), cell `SC-e-56`.
<owned_cells>SC-e-56</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC9-e56-AC1, SC9-e56-AC2, SC9-e56-AC3. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~38/MDPF_SECCLASS.TO-SC-e56.holdings-cusip-fallback.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC9-e56-AC1,SC9-e56-AC2,SC9-e56-AC3` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the lookup before and after, each firm's newly placed count and dollars, the existing Holdings tests' results, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE the producer's schedule is unchanged; the release follows IRPT_BCKEND's path.
comp-iam: DECLARED-NOT-APPLICABLE no grant; the local builds read with the box's existing access and stop where the fence denies.
comp-adversary: RUN -- R8's battery named holdings_49f.py and holdings_inf.py to read first (read-only here); canonical-first order (CTO ruling 103169) kept; the before-list is inferred until the fence join; BLIND: the served snapshot's readers outside the repo.
lane: the <paths> block IS the grant.
</preflight>

Source: round-8 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md` @1ca9e97fc9; PRD v0.13 @90f99888cd (ADMITTED); DECOMP_R9 @5d70aab6c9.
