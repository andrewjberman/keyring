# AMGT_HARVST task order -- `HVST-ce-1` -- ROUND 90, workstream S43-MEASURE: WHY THE UNH DOSSIER'S `fund_of_record` AND `last_stated_position` READ ABSENT BESIDE A REPORT THAT STATES FUND PFOE, AND HOW A SINGLE SECURITY'S DOSSIER IS REBUILT (row D1-S43; CTO round-89 analysis items 1 and 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ce-1.why-unh-fund-of-record-reads-absent-and-how-a-dossier-is-rebuilt</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ce-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~155</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY S3 reads of the bucket `opal-data-harvest` through the repo shim `.tools/aws` (`s3api list-objects-v2` and `get-object` on named keys or prefixes; never `put`, `delete`, `copy`, `sync`, a recursive `cp` or a bare `aws` call). Budget: at most 200 GET requests and 120 MiB in all, counted in `ce1_measure.out`. NO builder or producer script is RUN against S3 (reading its code is free; running a pure function on documents you fetched is allowed). NO deploy, NO Secrets Manager, NO publisher host, NO browser, NO scheduled task, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a cause named from the code alone without reproducing it on the real documents, a cause named from one report read as the cause for all securities, a "rule miss" declared when the stored object is merely older than the report, and a rebuild method described from a docstring instead of from the entry point's code.
</preflight>

## 0. THE CELL

The served gateway tool `harvest_get_research(security_key)` reads gold objects: a `research_dossier` object and a `research_continuation` object per security. The CRO read the control security `UNH_US_Equity` on 2026-10-17 and found: `fund_of_record` and `last_stated_position` read absent with the reason `"no report carries a non-empty RECOMMENDATION line"` (for the fund: `"no report's RECOMMENDATION line names a fund token (IDVZ|PFOE|DIVZ)"`), while the same response's `research_reports` holds report `48d81f053e5076e8` (class B, period 2Q26) with `fund` `PFOE` and `fund_evidence` `"Recommendation: Maintain positions in PFOE"`. The derivation of those two fields is `_resolve_fund_and_position(items)` in `lib/research/corpus/continuation.py` (lines 342-413; the label regex `_RECOMMENDATION_LABEL_RE = (?i)^\s*recommendation\s*:?\s*(.*)$` at line 132; the module docstring section "RULED -- RECOMMENDATION-LINE RESOLUTION" at line 47). The silver row's `fund` and `fund_evidence` come from a DIFFERENT step. The CTO asks two things: (1) WHY does the derivation miss UNH's PFOE report: the rule, the report's class, an older stored object, or the report missing from the derivation's inputs; (2) HOW is ONE security's dossier rebuilt, so a later order can rebuild KMB's without the two excluded Mexico reports (`report_id` `fbd50086c4065785` and `1a3b56044db679a5`, listed in `infra/aws/ec2/opal-gateway/app/harvest_research.py` `MISFILED_REPORTS`). This cell only MEASURES and REPORTS; it changes no product file.

## 1. THE WORK (read-only; the output is `ce1_measure.out`)

Work in your worktree. Write only the files named in `<paths>`. Print every number with its denominator.
a. **The stored UNH objects.** List and read the UNH gold objects: prefixes `amgt/harvest/gold/research_dossier/security_key=UNH_US_Equity/` and `amgt/harvest/gold/research-continuation/security_key=UNH_US_Equity/` (the gateway's `P_DOSSIER` and `P_CONTINUATION` in `infra/aws/ec2/opal-gateway/app/harvest_research.py` give the exact forms; read them). Record per object: key, LastModified, `as_of`, `method_version`, and the entries of `fund_of_record` and `last_stated_position`.
b. **The report.** Find report `48d81f053e5076e8` in the silver research-report parts (`amgt/harvest/silver/research-report/`, 5 parts; filter the parquet rows by `report_id`; also print every other UNH row's `report_id`, `report_class`, `period`, `fund`, `fund_evidence`, `bronze_key`, `extract_key`, `source_relpath`). Record the row of 48d81f053e5076e8 whole (no free text beyond 300 characters per field).
c. **The extraction.** Fetch the extraction document named by that row's `extract_key` (and, if needed, the bronze key's sibling extraction), and print its locators and the first 160 characters of each locator whose text matches `(?i)recommend` (a count and the list). State whether ANY locator would match the label regex of line 132 exactly as written.
d. **The inputs of the derivation.** Read how `items` (the `[(row, document), ...]` argument) is built for a security: find the caller of `_resolve_fund_and_position` and the function that selects which reports and extractions enter `items` (a class filter, a period filter, an extraction-present filter). State, with file and line, whether report 48d81f053e5076e8 would enter `items`.
e. **Reproduce.** Run the PURE function `_resolve_fund_and_position` (import it from `lib/research/corpus/continuation.py`) in a Python session on the documents you fetched, first on `items` built as the caller builds them from UNH's silver rows and extractions, and print the resulting `fund_of_record` and `last_stated_position`. Compare with the stored object of step a. State whether the stored object equals what the code produces today for the same inputs.
f. **The cause.** Write the line `CAUSE=<rule_miss|stale_object|report_not_in_items|no_stated_position|other>` and its evidence in one paragraph. `rule_miss`: the report states a recommendation in a form the label regex or the locator reading does not accept (name the text). `stale_object`: today's code on today's inputs yields PFOE and the stored object is older than the report or than the code. `report_not_in_items`: a filter keeps the report out of the inputs. `no_stated_position`: the extraction really carries no recommendation line (then `fund_evidence` of the silver row comes from somewhere else: name it). `other`: say what.
g. **The rebuild method for ONE security.** From the code, not the docstrings: find the entry point that writes a security's `research_dossier` and `research_continuation` gold objects (script or function; the gold producer family `amgt-corpus-dossier/15` named by `method_version`), and write: `REBUILD_ENTRY=<path::function or script with its arguments>`; its inputs (silver rows, extractions, any exclusion or filter input); `REBUILD_ONE_SECURITY=yes|no` (can it be run for KMB alone); `REBUILD_NEEDS_EXCLUSION_INPUT=yes|no` (does it know the misfiled-reports list: it must not, today, because that list lives only in the gateway); the S3 keys it writes for ONE security and whether it overwrites or versions (read the writer's code); and any lock, trigger or schedule it is part of. DO NOT RUN IT.
h. Anything odd: one row, then keep working. End `ce1_measure.out` with exactly these three lines: `CAUSE=...` (as in f), `REBUILD_ENTRY=...` (as in g) and `MEASURE gets=<n> bytes=<n> objects=<n>`.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~155/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ce-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~155/ce1_measure.out</invocation><expect>(?m)^CAUSE=(rule_miss|stale_object|report_not_in_items|no_stated_position|other)\b</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ce-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~155/ce1_measure.out</invocation><expect>(?m)^REBUILD_ENTRY=\S+</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ce-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~155/ce1_measure.out</invocation><expect>(?m)^MEASURE gets=\d+ bytes=\d+ objects=\d+$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1):** AC1, AC2 and AC3 FAIL as expected (`cat` of a file that does not exist). The issuer reads the content, not only the lines.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W155-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~155/AMGT_HARVST.TO-HVST-ce-1.why-unh-fund-of-record-reads-absent-and-how-a-dossier-is-rebuilt.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ce-1.why-unh-fund-of-record-reads-absent-and-how-a-dossier-is-rebuilt` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ce-1.why-unh-fund-of-record-reads-absent-and-how-a-dossier-is-rebuilt.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-89 analysis (`ledger/ROUND_ANALYSIS.round89.md` @fa28a5790e, msg 7642) items 1 and 3; row `D1-S43` (mine, from the CRO's read, msg 7635). The CTO's wording: name why the derivation misses UNH's PFOE report, "either the RECOMMENDATION-line rule, or the report's class"; if the rule's miss, fix it and prove it on the live gateway with a control name; if the report rightly carries no stated position, write the one-line rule into the order. The KMB dossier rebuild is graded on the live read.
- **Why a measurement cell first:** the fix, the `parts_absent.dossier` wording nit, the KMB rebuild and the gateway release under its own pair each need ce-1's answer to be written as an order a worker can execute without asking (cause, entry point, whether the rebuild can run for one security and whether it needs the exclusion list as input). They are DEFINED in decomposition section 120 and NOT CUT; this seat cuts them the tick `ce-1` closes.
- **Class:** `<paths>` names deliverables and the channel file only, so the floor is LOCAL; the cell is a measurement and a direct act (`<direct_act>true</direct_act>`, no L2, L4-R or L8 to L10; its close is the issuer's reading of `ce1_measure.out`). The S3 reads are READ-ONLY and bounded in the preflight.
- Slot ~155, worktree `C:/dev/wk-harvst-155`, branch `wk-AMGT_HARVST-155`. Widen the sparse set at provision with `lib/research` and `.claude/agents`.
- **SENT:** with the round-90 issuance.

**COMPLETE 2026-10-17T15:5xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~155` (worker, haiku, high), branch `wk-AMGT_HARVST-155`, commits `a6d080aeb4`, `7116ebe68b`, `7b0991ea26`, merged `0dfc96bdd1` (safe-merge fast lane, index check 0 of 5 paths differ); worktree and branch removed. Read by this seat: `ce1_measure.out` in full (119 lines), the last three lines AC1 to AC3, proof instance VALID rc 0 (re-run here).
- **`CAUSE=rule_miss`** (layout level): the report `48d81f053e5076e8` is in the inputs (1 of 1 items); the stored continuation equals today's code on today's inputs (5 of 5 compared fields); the anchored label regex (`continuation.py` line 132) is applied to a whole pdf PAGE whose text starts with a page number and a title block, so `Recommendation: Maintain positions in PFOE and DIVZ` at offset 75 is never tested. The silver `fund` comes from `typed.py::_find_fund`, an unanchored search, which is why the silver row says PFOE. **`REBUILD_ENTRY`:** `continuation.py::write_one(security_key)` then `dossier.py::write_one(security_key)` (dossier CLI `--security-key`; the continuation CLI has no one-name write); gold writes never overwrite (a new name beside the old); neither writer takes an exclusion input (`REBUILD_NEEDS_EXCLUSION_INPUT=yes`). **`MEASURE gets=47 bytes=1626460 objects=24`** (cap 200 and 120 MiB; 21 of the 47 were NoSuchKey misses from a key-list defect of the worker, corrected on a second pass).
- **Rows** `D1-W155-S1` (ARMED, disarm owner `1.0.0_SA_CTO`), `D1-W155-S2` (ARMED, disarm owner this seat), `D1-W155-S3` (INERT): the recut `ce-2` and `ce-6` answer S1 and S2; the issuer dispositions them after the round's merges.
- **What this does NOT prove:** the population effect of a fix (`ce-2`'s census) or any served read.

<risk>LOCAL</risk>
<direct_act>true</direct_act>
<worker_class>worker</worker_class>
<status>complete</status>
<round>90</round>
<workstream>S43-MEASURE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
