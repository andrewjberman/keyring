# TO MDPF_SECCLASS.TO-SC-e58 -- round 10 SC-e-58: the read-only trace of the Black Diamond pages journey, hop by hop, naming the first failing hop

<to_id>MDPF_SECCLASS.TO-SC-e58</to_id>
<project>MDPF_SECCLASS</project>
<issued_to>0.9.0_WK_MDPF_SECCLASS~41</issued_to>
<issued_by>2.0.0_SA_COO~M1</issued_by>
<issued_date>2026-10-07</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~M1</workstream>

**Directive:** D8 | **Fabric:** laptop (placement DELL1) | **Decomp cell:** `SC-e-58` (`decompositions/MDPF_SECCLASS_DECOMP_R10.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (slot ~41 queue: then TO-SC-e59, TO-SC-e60)

---

## WORKER FACE

### THE CELL

`SC-e-58`. CTO round-9 analysis ruling 2.1: "Round 10 opens with a read-only trace of the BD pages' journey (page, API, platinum key,
producer, classifier source). It names the one failing hop with its evidence, because two rounds of enrichment have not moved FWD-1
there."

FWD-1: "An advisor opens a Black Diamond client's holdings and sees each security's class and sub-class exactly as Opal's one shared
list holds it, on the live Black Diamond outputs. ACCEPT: for a real Black Diamond client, gold funds such as GLD and PHYS read as
commodities and VXX reads as a hedge, the same as Positioning shows them."

The PRD's thread (section 2), as written at L4:
1. canonical table `etf-classifications` -> `data/black_diamond/scripts/gold/lib/etf_classifier.py` (reads it through the one client,
   `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`, instead of scanning `bd-securities`; the `hedge -> alternatives`
   fold near `:99,108` goes);
2. -> `data/black_diamond/scripts/silver/build_bd_assets_dim.py` (~:154, class and sub-class from the canonical row);
3. -> `data/black_diamond/scripts/gold/D_03.composition_artifacts.py` (~:116) and `data/black_diamond/scripts/gold/D_04.client_portal_summary.py`
   (the platinum key `platinum/firm/mix_summary.json` and the per-client summary);
4. -> the served BD client surfaces: the portal page an advisor opens and the API that serves it (find both from the portal source under
   `portal/src/` and the API code under `infra/aws/lambda/`, starting from the platinum keys D_03/D_04 write).

**Build:** walk the journey from the PAGE backwards to the canonical source, in exactly these seven hops: `page`, `api`, `platinum_key`,
`gold_producer`, `silver_dim`, `classifier_lib`, `canonical_source`. For each hop record:
- `name`;
- `grade`: PASS, FAIL or UNREAD. PASS means GLD and PHYS read commodities and VXX reads hedge (the canonical class) at that hop. FAIL
  means a different class, a fold or a non-canonical source. UNREAD means you could not read it; that is a value, never a guess;
- `evidence`: file:line read, and the command and its output for any live read;
- `tickers`: a map of GLD, PHYS and VXX to the class each reads at that hop (omit the map only on UNREAD);
- `claim`: `measured` (live bytes read), `inferred` (a code-path read) or `absent`;
- on a FAIL hop, `fix_file` and `fix_line`: the file and line a fix would change.

Set `first_failing_hop` to the first FAIL in journey order, or `"NONE"`. Write it as JSON to
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_PAGES_THREAD_TRACE_20261007.json`, and a one-page reading beside it
(`...TRACE_20261007.md`): hop table, the first failing hop, and what its fix would be.

**Reads you may take:**
- the repo;
- a read-only scan or get of the DynamoDB table `etf-classifications` (canonical_source; `aws dynamodb get-item` for GLD, PHYS, VXX).
dell1's principal is DENIED the firm S3 buckets (opal-data-bd and others, row W25-S1). A denied read is recorded as such, and that hop is
graded from the code path with claim `inferred`, or UNREAD. Do not hunt for another principal.

### ACCEPTANCE

<criterion id="SC10-e58-AC1" cell_refs="SC-e-58"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/sc_e58_thread_trace_check.py</invocation><expect>SC-E58 ok=True</expect></criterion>
`SC10-e58-AC1` -- the trace record has seven hops in journey order, each graded with evidence, GLD/PHYS/VXX on each read hop, and the
first failing hop named with its fix file and line.

<criterion id="SC10-e58-AC2" cell_refs="SC-e-58" judgment="true"/>
`SC10-e58-AC2` -- judgment (3.0.0_SA_CVO, L9): the named failing hop is the true first break of the journey, and no hop is graded PASS
on a read that could not see it.

<expected_criteria>SC10-e58-AC1,SC10-e58-AC2</expected_criteria>

Dry-run at the base (277fc76bc2, 2026-10-07): SC10-e58-AC1 FAIL as expected (`absent BD_PAGES_THREAD_TRACE_20261007.json`).

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`,
  uncommitted.
- **No package install and no download of any kind** (no pip, npm, bun add, bun install, curl or tool fetch, into any environment;
  rows S49, S54).
- READ-ONLY: no code edit, no table write, no S3 write, no deploy, no run of a producer with an upload flag.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `MDPF_SECCLASS-W41-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the check.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_PAGES_THREAD_TRACE_20261007.json
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_PAGES_THREAD_TRACE_20261007.md
org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R10.md</decomp_doc> (round 10), cell `SC-e-58`.
<owned_cells>SC-e-58</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: SC10-e58-AC1, SC10-e58-AC2. Instance at `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/0.9.0_WK_MDPF_SECCLASS~41/MDPF_SECCLASS.TO-SC-e58.bd-pages-thread-trace.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> SC10-e58-AC1,SC10-e58-AC2` BEFORE the flip. A judgment criterion is recorded
`UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming 3.0.0_SA_CVO, never PASS or FAIL.
</proof_of_spec>

**REPORT:** the hop table (grade, claim), the first failing hop with its fix file and line, every denied read, AC1 output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a read-only trace schedules nothing.
comp-iam: RUN at the cut from rows W25-S1 (dell1 denied the firm buckets) and R9 workers' read-only scans of etf-classifications; the worker records each denied read.
comp-adversary: RUN -- a hop graded PASS on a read that cannot see it (claim field + UNREAD value); a trace that stops at the first plausible hop (all seven graded); BLIND: the served bytes in opal-data-bd (denied to dell1; a laptop seat's read when the fence join applies).
lane: the <paths> block IS the grant.
</preflight>

Source: round-9 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_9_20261007.md` @9b6348f15e section 2.1 and section 3 item 1; PRD v0.14 @9b6348f15e (ADMITTED); DECOMP_R10.
