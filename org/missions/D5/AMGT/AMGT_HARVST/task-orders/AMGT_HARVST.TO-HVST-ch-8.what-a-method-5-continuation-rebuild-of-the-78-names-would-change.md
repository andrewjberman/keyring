# AMGT_HARVST task order -- `HVST-ch-8` -- ROUND 93, workstream REBUILD-CENSUS: A READ-ONLY CENSUS OF WHAT A METHOD-5 CONTINUATION REBUILD OF THE 78 NAMES WITHOUT A CURRENT CONTINUATION WOULD CHANGE (the measurement the never-widen pair of `HVST-ch-7` needs; CTO round-92 analysis item 4)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ch-8.what-a-method-5-continuation-rebuild-of-the-78-names-would-change</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ch-8</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~168</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY S3 reads of the bucket `opal-data-harvest` ONLY: list and get under `amgt/harvest/gold/research-continuation/`, `amgt/harvest/silver/research-report/` and the extraction objects the silver rows name, through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 5000 requests and 1 GiB in all, counted in the census's last line (the sister censuses needed 363 to 1,672 requests and 100 to 137 MiB; this one builds 78 continuations in memory). NO gold or silver writer is RUN: `continuation.write_one`, `gold_put`, `dossier.write_one`, `--write` are NEVER run; only `continuation.build` (in memory). NO deploy, NO edit of any source file, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a comparator that cannot see a changed field (it has a negative control), a comparator that reports a change where only key order or whitespace differs (compare parsed values, not bytes), a census that compares the build with an object that is NOT the one the gateway serves (use the gateway's rule, copied from `harvest_research.py` line 349), a `write_one` that slips in beside `build`, and a census whose expectation is edited to match.
</preflight>

## 0. THE CELL

The CTO's round-92 item 4: a `/5` rebuild of the names that have no continuation at the current method (`continuation.METHOD_VERSION`, `amgt-corpus-continuation/5`) goes under its own never-widen pair, and the standing no-rebuild instruction lifts when it lands. `HVST-ch-1` measured 78 such names (of 95 with a continuation partition; 17 are at `/5`). **A never-widen pair names what the act may touch; this cell measures it, read-only: for each of the 78 names, the continuation that `continuation.build(security_key)` builds in memory today, compared FIELD BY FIELD with the continuation the gateway serves today.** It writes nothing and changes no source file.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`.
a. Write `ch8_census.py` in your deliverables folder (start from `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~165/ch1_census.py`, which already lists the 95 partitions, reads every object and applies the gateway's pick; read it) and run it once in the FOREGROUND with `python -u`, stdout to `ch8_census.out` (open the output file with `newline="\n"` so line endings are LF).
b. The census: for EVERY security with a continuation partition under `amgt/harvest/gold/research-continuation/`: apply the gateway's rule (`max` over ALL objects of the partition by (LastModified as an ISO string, or "" when missing, then the key), copied from `infra/aws/ec2/opal-gateway/app/harvest_research.py` line 349; read it) to get the SERVED object; if the served object's `method_version` equals `continuation.METHOD_VERSION` the name is AT_CURRENT (count it; no build). For each name NOT at current ("the 78"): `built = continuation.build(security_key)` (in memory; NEVER `write_one`) and compare `built["fields"]` with `served["fields"]` FIELD BY FIELD over the union of the two key sets, comparing PARSED values with `==` (never bytes). Print one line per name: `NAME <security_key> served=<first 8 characters of the object name>/<method_version integer> fields_changed=<n> list=<comma-separated field names or none> inputs_equal=<yes|no> name_exists=<yes|no>` where `inputs_equal` compares `built["inputs"]` with `served["inputs"]`, and `name_exists` is yes when an object named `<continuation._inputs_sha16(built["inputs"])>.json` already exists in that name's partition. Then one line per field that changed anywhere: `FIELD <name> names_changed=<n>`.
c. **The controls (rule 22: a census needs both).** POSITIVE: `MNST_US_Equity` is at the current method (`HVST-cf-4`); build it in memory and compare it with its served object by the SAME comparator: print `CONTROL-POSITIVE MNST_US_Equity fields_changed=<n>` (expected 0). NEGATIVE: take the served object of `UNH_US_Equity`, copy it in memory, change ONE field's value in the copy, and compare the copy with the original by the same comparator: print `CONTROL-NEGATIVE fields_changed=<n>` (expected exactly 1).
d. The final line, exactly: `CENSUS-CONT-REBUILD partitions=<n> at_current=<n> names=<n not at current> unchanged=<names with fields_changed=0> changed=<names with fields_changed>0> fields_changed=<total over names> inputs_equal=<names with inputs_equal=yes> name_exists=<names with name_exists=yes> gets=<requests> bytes=<bytes>`. **The issuer expects `names=78`.** The counts `changed`, `unchanged` and `fields_changed` are the FINDING: do NOT change anything to make them read 0; print every changed name and field plainly.
e. For EVERY name with `fields_changed` above 0, print under it one line per changed field `DIFF <security_key> <field> served=<first 70 characters of the served value or absent> built=<first 70 characters of the built value or absent>`. File ONE surprise row summarising them (counts per field and the name list) with the reason you can read for each kind of change (a newer extraction, the pdf rule, the stance rule, the lexicon). Do not guess a reason you cannot read.
f. Do not touch any source file. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~168/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ch-8"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~168/ch8_census.out</invocation><expect>(?m)^CENSUS-CONT-REBUILD partitions=\d+ at_current=\d+ names=78 unchanged=\d+ changed=\d+ fields_changed=\d+ inputs_equal=\d+ name_exists=\d+ gets=\d+ bytes=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ch-8"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~168/ch8_census.out</invocation><expect>(?m)^CONTROL-POSITIVE MNST_US_Equity fields_changed=0$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ch-8"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~168/ch8_census.out</invocation><expect>(?m)^CONTROL-NEGATIVE fields_changed=1$</expect></criterion>
</proof_of_spec>

- AC1 is the shape (and the 78 the issuer expects); its counts are the finding. AC2 and AC3 are the controls: the comparator sees no change where there is none and exactly one where one is planted. **If a control prints another number, DO NOT edit the expectation or the comparator to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~04:4xZ):** all three FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W168-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~168/AMGT_HARVST.TO-HVST-ch-8.what-a-method-5-continuation-rebuild-of-the-78-names-would-change.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ch-8.what-a-method-5-continuation-rebuild-of-the-78-names-would-change` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ch-8.what-a-method-5-continuation-rebuild-of-the-78-names-would-change.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-92 analysis item 4 ("a /5 rebuild of the names without a /5 continuation goes under its own pair"); the pair needs a measured blast radius (per-name, per-field). The scope question (continuations only, or dossiers too) is asked of the CTO (my msg of 04:31Z); this cell measures the CONTINUATIONS, which every scope includes.
- **The never-widen pair of `HVST-ch-7` is written from this census, not before.**
- Slot ~168, worktree `C:/dev/wk-harvst-168`, branch `wk-AMGT_HARVST-168`. Widen the sparse set at provision with `lib/research`, `.claude/agents`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922`, `infra/aws/ec2/opal-gateway/app` and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~165`.
- **SENT:** with the round-93 recut.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>93</round>
<workstream>REBUILD-CENSUS</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
