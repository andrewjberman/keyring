# AMGT_HARVST task order -- `HVST-cm-3` -- ROUND 98, workstream PATHKEY-WRITERS-2: THE WRITER CENSUS IS RE-RUN AFTER THE `pull_enqueue` DEPLOY AND NO WRITER OF THE PATH-COMPONENT PREFIXES WRITES THE RAW SPELLING (CTO round-97 analysis item 3: "Re-run the writer census over the 16 writers. Grade: 0 raw-spelling writers")

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cm-3.the-writer-census-is-re-run-and-no-writer-of-the-path-component-prefixes-writes-the-raw-spelling</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cm-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~177</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- READ-ONLY: you read schedule names only through the repository's own registers (`org/devices/`, `infra/**/schedule*`, `.tools/*schedule*`, `docs/`); you never create, change or run a schedule.
comp-iam: RUN at L5 -- READ-ONLY S3 list calls (and head/get of at most 50 objects) under the path-component prefixes, through `lib.research.harvest.store._default_client()` or the same client the gateway's `harvest_typed` helpers use; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 1500 requests and 100 MiB. NO writer is RUN, NO edit of any source file, NO edit outside `<paths>`; you DO NOT call the live gateway.
comp-adversary: RUN at L5 -- the adversary is a search that finds only the READERS of the prefixes and calls them writers, a search of `lib/` alone, a writer classified `canonical` because it calls a helper whose rule was not read (the Lambda `pull_enqueue` now carries its OWN stdlib copy `_slash_safe_key` of the rule: read it and the equality test beside it), a count without its denominator (files scanned), a negative control whose literal is typed in a file the scan reads (use a token the script generates at run time), a spelling `unknown` hidden inside `canonical`, and a census whose expectation is edited to match.
</preflight>

## 0. THE CELL

The round-96 writer census (`HVST-ck-4`, merged `a6b4cf1179`) found 16 writer sites of the 13 path-component prefixes: 15 wrote the CANONICAL spelling of a slash key and ONE wrote the RAW spelling, the `opal-research-pull-enqueue` Lambda (`infra/aws/lambda/research/pull_enqueue/lambda_function.py:129`). `HVST-cl-1` and `HVST-cl-2` changed it (merged `349e7ee0da`, deployed 2026-10-18 15:24Z) so that it writes the canonical spelling through a stdlib copy `_slash_safe_key` of `crosswalk.slash_safe_key`. **The CTO wants the census re-run to grade the result: 0 raw-spelling writers.** Your tools exist: the script `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~173/ck4_writers.py` and its output `ck4_writers.out`, and its negative-control helper `ck4_negative2.py` and Lambda check `ck4_lambda_check.py` in the same folder. This cell writes nothing and changes no source file.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`.
a. **Start from the round-96 script.** Copy `0.9.0_WK_AMGT_HARVST~173/ck4_writers.py` to `deliverables/0.9.0_WK_AMGT_HARVST~177/cm3_writers.py` and change ONLY: the output file name (`cm3_writers.out`), the header line, and, if the script cannot classify a writer that carries its own copy of the rule, the classifier for that one case (read how it decides `canonical`; a writer whose key builder is a verified copy of the rule is `canonical`, with the copy's `file:line` and the equality test's path printed; do not loosen the classifier for any other site). Read the script, `ck4_writers.out` (its 16 `WRITER` lines and what each classification rested on), and the Lambda source and `test_cl1_status_key_canonical.py` first. The scan walks the SHARED checkout at `C:/Dev/ajb_workspace` (read-only; your own worktree is sparse); never edit or create a file there.
b. **Run it once in the FOREGROUND with `python -u`**, stdout to `cm3_writers.out` (open it with `newline="\n"`): the prefixes read from the three gateway modules, the denominator (files scanned per extension), every `OCCURRENCE`, every `WRITER` (with its spelling and schedule), the `NEWEST` lines (the S3 lists of the newest object per spelling for the two slash keys), the controls and the final line. Print the writers whose classification CHANGED against `ck4_writers.out` as `WRITER-CHANGED <prefix> <file:line> was=<spelling> now=<spelling>` (expected: the Lambda, `raw` to `canonical`) and any NEW writer site that was not in the round-96 census as `WRITER-NEW <prefix> <file:line> <function> spelling=<...>`, any writer site that DISAPPEARED as `WRITER-GONE ...`.
c. **The controls (rule 22):** POSITIVE: `CONTROL-POSITIVE reader_found prefix=peers/v1/ file=<path> class=READER` (the scan finds the gateway's own reader). NEGATIVE: a literal that exists nowhere, a TOKEN YOUR SCRIPT GENERATES AT RUN TIME (`ZZ_NO_SUCH_` + 16 random lowercase hex digits + `_ZZ/v1/`, never typed in any file), scanned with the SAME walker and scan function: `CONTROL-NEGATIVE-2 token=<the token> occurrences=0`.
d. The final line, exactly: `CENSUS-WRITERS prefixes=<n> occurrences=<n> writers=<n> raw_writers=<n> canonical_writers=<n> unknown_writers=<n> files_scanned=<n> gets=<requests>`. **The issuer expects `writers=16` (or more, with each new one printed) and `raw_writers=0`; the counts are the FINDING: do not change anything to make them read so.**
e. File ONE surprise row summarising the table (the writers, any CHANGED, NEW or GONE, and what each classification rested on) and ONE row per `raw` or `unknown` writer (an ARMED-class row only for a `raw` writer that a `NEWEST` line shows is writing TODAY). Do not touch any source file. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~177/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cm-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~177/cm3_writers.out</invocation><expect>(?m)^CENSUS-WRITERS prefixes=\d+ occurrences=\d+ writers=\d+ raw_writers=0 canonical_writers=\d+ unknown_writers=0 files_scanned=\d+ gets=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cm-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~177/cm3_writers.out</invocation><expect>(?m)^CONTROL-POSITIVE reader_found prefix=peers/v1/ file=\S*harvest_research\.py class=READER$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cm-3"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~177/cm3_writers.out</invocation><expect>(?m)^CONTROL-NEGATIVE-2 token=ZZ_NO_SUCH_[0-9a-f]{16}_ZZ/v1/ occurrences=0$</expect></criterion>
</proof_of_spec>

- AC1 is the CTO's grade (0 raw-spelling writers, no unknown ones); its other counts are the finding. AC2 and AC3 are the controls: the scan sees a reader that exists and finds nothing for a literal that exists nowhere. **If a line reads otherwise (for example `raw_writers=1`), DO NOT edit the expectation, the classifier or the code to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~16:3xZ):** all three FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your first row id is `AMGT_HARVST-D1-W177-S1`. The channel file has MIXED line endings and is append-only: READ ITS TAIL for the id sequence, append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body AND run the gate against your row WITHOUT the override first.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~177/AMGT_HARVST.TO-HVST-cm-3.the-writer-census-is-re-run-and-no-writer-of-the-path-component-prefixes-writes-the-raw-spelling.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cm-3.the-writer-census-is-re-run-and-no-writer-of-the-path-component-prefixes-writes-the-raw-spelling` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cm-3.the-writer-census-is-re-run-and-no-writer-of-the-path-component-prefixes-writes-the-raw-spelling.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- A foreground command must finish inside the tool's ten-minute limit (the round-96 scan took about 86 seconds): if it would not, scan in slices by directory, appending to a parts file and merging in a `--final`.
- Run every script from the repo root of YOUR worktree (it reads the shared checkout by absolute path). Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-97 analysis (msg 8125) item 3. The round-96 census is `HVST-ck-4`.
- **The negative control is a run-time random token** (my `ck-4` defect: a typed literal sat in the order the scan reads).
- Chain C of round 98 (its own worker `~177`: no dependency on chains A, B or D; disjoint write set). Slot ~177, worktree `C:/dev/wk-harvst-177`, branch `wk-AMGT_HARVST-177`. **Sparse set at provision (each named file CHECKED BY NAME after the add):** `.claude/agents`, `lib/research`, `infra/aws/ec2/opal-gateway/app` and the deliverables folders `0.9.0_WK_AMGT_HARVST~173` and `0.9.0_WK_AMGT_HARVST~171`; the scan itself reads the shared checkout read-only.
- **COMPLETE (issuer, 2026-10-18 ~17:0xZ):** worker `~177`, branch merged `e8583524b3` (census `1564c2d60a`, six rows `d0b4286670`, proof `beb4dabeea` VALID). No blocking row. The worker's graded run was at shared HEAD `e97c43e97b` (HEAD moved during its session; `D1-W177-S6`). THE GRADE (the CTO's: 0 raw-spelling writers): `CENSUS-WRITERS prefixes=13 occurrences=4992 writers=16 raw_writers=0 canonical_writers=16 unknown_writers=0 files_scanned=108256 gets=52`; `CONTROL-POSITIVE reader_found prefix=peers/v1/ file=...harvest_research.py class=READER`; `CONTROL-NEGATIVE-2 token=ZZ_NO_SUCH_12da89019229a139_ZZ/v1/ occurrences=0`; the one `WRITER-CHANGED`: the Lambda (`lambda_function.py:150`) `was=raw now=canonical`; no `WRITER-NEW`, no `WRITER-GONE`. READ BY ME: I RE-RAN `cm3_writers.py` myself from the worker's worktree (read-only, 52 requests): `writers=16 raw_writers=0 canonical_writers=16 unknown_writers=0`, the same single `WRITER-CHANGED` line and a control token that reads 0; `occurrences` 5019 against 4992 and `files_scanned` 108287 against 108256 because the shared checkout grew between the two runs (my own new files), which does not move a writer. The Lambda is classified `canonical` by the worker's `verify_lambda_copy` (`key_mismatches=0`, `probe_mismatches=0`: its stdlib copy against `crosswalk.slash_safe_key`, run, not read), not by the round-96 table. WHAT THE GRADE RESTS ON (the worker's own limits, rows `D1-W177-S3` and the note): the other 15 writers' `canonical` verdicts are the round-96 hand reads, not re-read this round; four canonical lines (`enrich.py:782`, `catalog.py:74`, `uploads.py:165` and `:180`) carry no `slash_safe_key` call and are graded canonical on an identity claim (the keys they write are opaque or have no slash: the census's own note) that was not re-measured; `D1-W177-S5` (the NEWEST probe builds a double slash for the `publication-links` ROOT template: a read-probe quirk, those prefixes hold no objects) and `D1-W177-S2`/`-S4` (the round-96 table pinned the Lambda to raw by a hand-read verdict; now derived at run time; the round-96 control counted its own typed literal, my `ck-4` defect, already recorded). No raw or unknown writer, so no per-writer row and no ARMED row: raw `packs/` newest is 2026-09-25 and canonical `packs/` newest is 2026-10-18T15:27:00Z (the `cl-2` invoke).
- **SENT:** with the round-98 issuance.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>98</round>
<workstream>PATHKEY-WRITERS-2</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
