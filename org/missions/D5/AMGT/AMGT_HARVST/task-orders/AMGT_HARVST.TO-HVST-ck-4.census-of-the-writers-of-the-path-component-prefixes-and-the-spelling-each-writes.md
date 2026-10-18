# AMGT_HARVST task order -- `HVST-ck-4` -- ROUND 96, workstream PATHKEY-WRITERS: A READ-ONLY CENSUS OF EVERY WRITER OF THE PATH-COMPONENT PREFIXES AND THE SPELLING OF A SLASH KEY EACH WRITES (CTO round-95 analysis section 3 item 1 and enrichment item 3)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ck-4.census-of-the-writers-of-the-path-component-prefixes-and-the-spelling-each-writes</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ck-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~173</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- READ-ONLY: you read scheduled-task and Lambda/ECS schedule names only through the repository's own registers (`org/devices/`, `infra/**/schedule*`, `.tools/*schedule*`, `docs/`); you never create, change or run a schedule.
comp-iam: RUN at L5 -- READ-ONLY S3 list calls (and head/get of at most 50 objects) under the path-component prefixes, through `lib.research.harvest.store._default_client()` or the same client the gateway's `harvest_typed` helpers use; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 1500 requests and 100 MiB. NO writer is RUN, NO edit of any source file, NO edit outside `<paths>`; you DO NOT call the live gateway.
comp-adversary: RUN at L5 -- the adversary is a search that finds only the READERS of the prefixes (the gateway constants) and calls them writers, a search of `lib/` alone (a writer may live in `infra/`, `.tools/`, `integrations/`, `org/` scripts or a scheduled job's repository), a writer classified `canonical` because it calls a helper whose rule was not read, a count without its denominator (files scanned), a search whose negative control cannot return zero, a spelling "unknown" hidden inside "canonical", and a census whose expectation is edited to match.
</preflight>

## 0. THE CELL

The CTO ruled (round-95 analysis, section 3): writers of the path-component prefixes write the CANONICAL spelling of a slash key (`slash_safe_key`, as `crosswalk` and the gateway's `harvest_keys` do); a writer that writes the RAW spelling today is changed, under its own pair if it is a scheduled producer. **First the facts: which code writes the eight path-component prefixes** (the peers, scores and posture reads and the filings, drafting and management reads of the gateway's `harvest_research.py`; the model-block reads of `harvest_figures.py`; the coverage and publication-link templates of `harvest_identity.py`), **under which spelling of a slash key, and whether anything still writes the RAW spelling today.** The stored tables hold BOTH spellings (`peers/v1/BP/_LN_Equity/` 7 objects and `peers/v1/BP-SLASH-_LN_Equity/` 10; NG 7 and 10). This cell is read-only and changes no file.

## 1. THE BUILD (a read-only script and a table; no product code)

Work in your worktree. Change only the files named in `<paths>`. **You search the SHARED repository checkout at `C:/Dev/ajb_workspace` read-only (your own worktree is sparse); never edit or create a file there.**
a. **The prefixes (read, never typed):** from `deliverables/0.9.0_WK_AMGT_HARVST~171/cj2_sites.out` and `cj6_sites.out` (the `CONST` and `SITE` lines of class `OTHER`) and the three gateway modules (`infra/aws/ec2/opal-gateway/app/harvest_research.py`, `harvest_figures.py`, `harvest_identity.py`) list every path-component prefix or key template the gateway READS from a caller's key (starting list: `management/v1/`, `filings/v1/`, `drafting/v1/`, `peers/v1/`, `scores/v1/`, `posture/v1/`, the model-block prefixes `MODEL_PREFIX` and `FYE_PREFIX`, the coverage and publication-link templates and `packs/<key>/input_ledger.json`). Print `PREFIX <name> literal=<the fixed leading path, for example peers/v1/> source=<file:line>`.
b. **The writers (a controlled read-only scan, `ck4_writers.py`, run in the FOREGROUND with `python -u`, stdout to `ck4_writers.out` with `newline="\n"`):** walk the shared checkout (skip `.git`, `node_modules`, `__pycache__`, any `*.pyc`, and files over 2 MiB) over `*.py`, `*.sh`, `*.ps1`, `*.js`, `*.ts`, `*.tsx`, `*.tf`, `*.yaml`, `*.yml`, `*.json` (config only), `*.md` (docs only, counted separately) and print the number of files scanned per extension (the DENOMINATOR). For EVERY prefix, find every occurrence of its literal leading path (a quoted string or a format string, for example `"peers/v1/` and `peers/v1/%s`), and for each occurrence classify it by reading the code around it (open the file and read the function): `WRITER` (a `put_object`, `upload_file`, `gold_put`, `write`, an `s3 cp`/`sync` command, or a helper whose body does one: print the helper's `file:line` and what it calls), `READER` (a `get_object`, `list_objects`, `ht.list_keys`, `_list_json`, a `read`), `DOC` or `TEST` or `OTHER`. Print `OCCURRENCE <prefix> <file:line> class=<WRITER|READER|DOC|TEST|OTHER> function=<name>`.
c. **For EVERY WRITER occurrence:** read the function and print the SPELLING of a slash key it writes: `canonical` (it builds the key with `slash_safe_key`, `crosswalk.security_key_partition` or `store.entity_partition`; name the call you read), `raw` (it puts the caller's key into the path as typed), `refuses` (it raises on a `/` as `store.entity_partition` does for a non-`security_key` entity) or `unknown` (you could not read it; say what stopped you). Print `WRITER <prefix> <file:line> <function> spelling=<canonical|raw|refuses|unknown> schedule=<the scheduled task, Lambda, ECS task, GitHub workflow or CLI that runs it, from a repository register, or none|unknown>`.
d. **What the stored objects say (read-only S3 lists):** for each prefix and each of the two slash keys list the objects under the RAW spelling and under the CANONICAL spelling (`crosswalk.slash_safe_key`; never type the encoding) and print `NEWEST <prefix> <key> raw_n=<n> raw_newest=<LastModified utc or none> canonical_n=<n> canonical_newest=<LastModified utc or none>`: a spelling whose newest object is recent is written TODAY, one whose newest object is old is a legacy.
e. **The controls (rule 22):** POSITIVE: the scan must find the gateway's own READER of `peers/v1/` (the constant in `harvest_research.py`): print `CONTROL-POSITIVE reader_found prefix=peers/v1/ file=<path> class=READER`. NEGATIVE: scan for a literal that exists nowhere, `ZZ_NO_SUCH_PREFIX_ZZ/v1/`, with the SAME scan code and print `CONTROL-NEGATIVE ZZ_NO_SUCH_PREFIX_ZZ/v1/ occurrences=0`.
f. The final line, exactly: `CENSUS-WRITERS prefixes=<n> occurrences=<n> writers=<n> raw_writers=<n> canonical_writers=<n> unknown_writers=<n> files_scanned=<n> gets=<requests>`. **The issuer expects `prefixes` near 8; the counts are the FINDING** (a raw-spelling writer becomes a later cell; do not change anything to make a count read 0). If a prefix has NO writer in the checkout, say so in a line `NO-WRITER <prefix>` with the places you looked (a writer outside the repository would be invisible: name that limit).
g. File ONE surprise row summarising the table (per prefix: its writers, their spelling and schedule, and which spelling holds the newest objects) and ONE ARMED-class row ONLY for a `raw` writer that a `NEWEST` line shows is writing TODAY. Do not touch any source file. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~173/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ck-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~173/ck4_writers.out</invocation><expect>(?m)^CENSUS-WRITERS prefixes=\d+ occurrences=\d+ writers=\d+ raw_writers=\d+ canonical_writers=\d+ unknown_writers=\d+ files_scanned=\d+ gets=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ck-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~173/ck4_writers.out</invocation><expect>(?m)^CONTROL-POSITIVE reader_found prefix=peers/v1/ file=\S*harvest_research\.py class=READER$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ck-4"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~173/ck4_writers.out</invocation><expect>(?m)^CONTROL-NEGATIVE ZZ_NO_SUCH_PREFIX_ZZ/v1/ occurrences=0$</expect></criterion>
</proof_of_spec>

- AC1 is the shape; its counts are the finding. AC2 and AC3 are the controls: the scan sees a reader that exists and finds nothing for a literal that exists nowhere. **If a control prints another line, DO NOT edit the expectation or the code to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~12:0xZ):** all three FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W173-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~173/AMGT_HARVST.TO-HVST-ck-4.census-of-the-writers-of-the-path-component-prefixes-and-the-spelling-each-writes.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ck-4.census-of-the-writers-of-the-path-component-prefixes-and-the-spelling-each-writes` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ck-4.census-of-the-writers-of-the-path-component-prefixes-and-the-spelling-each-writes.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- A foreground command must finish inside the tool's ten-minute limit: scan in slices by directory if the walk would not, appending to a parts file and merging in a `--final`.
- Run every script from the repo root of YOUR worktree (it reads the shared checkout by absolute path). Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-95 analysis (`ledger/ROUND_ANALYSIS.round95.md` @031ac46589, msg 8025) section 3 item 1 ("writers write the canonical spelling; a writer that writes the raw spelling today is changed, under its own pair if it is a scheduled producer") and enrichment item 3 ("name every writer of those 8 prefixes and the spelling it writes; a raw-spelling writer becomes a cell").
- Chain B of round 96: independent of `HVST-ck-1` (a different question: who writes, not what is stored); its own worker `~173`. A raw writer found today becomes a cell in round 97 (or a recut of this round if it is writing now and the CTO says so).
- Slot ~173, worktree `C:/dev/wk-harvst-173`, branch `wk-AMGT_HARVST-173`. **Sparse set at provision: `lib/research`, `.claude/agents`, `infra/aws/ec2/opal-gateway/app` and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~171`; the search itself reads the shared checkout read-only.**
- **SENT:** with the round-96 issuance.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>96</round>
<workstream>PATHKEY-WRITERS</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
