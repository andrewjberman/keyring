# AMGT_HARVST task order -- `HVST-cj-1` -- ROUND 95, workstream SLASH-CENSUS: A READ-ONLY CENSUS OF EVERY SLASH KEY IN THE CORPUS, PRINTING WHICH TABLES HOLD IT UNDER WHICH KEY FORM (row `W170-S3`; CTO round-94 analysis item 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cj-1.census-of-slash-keys-which-table-holds-which-key-form</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cj-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~171</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY S3 reads of the buckets and prefixes the harvest uses (`opal-data-harvest`, under `amgt/harvest/` and `bloomberg/harvest/`): list and head/get, through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 12000 requests and 1 GiB in all, counted in the census's last line (a list call returns up to 1000 keys; most cells need one or two requests; a `get` is needed only to read a silver row's `security_key`, so prefer a list, or a head, wherever it answers). NO writer is RUN: no `write_one`, no `gold_put`, no `--write`, no rename or copy of any object. NO deploy, NO edit of any source file, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a census that finds the slash keys from a typed list (the two known ones are `BP/_LN_Equity` and `NG/_LN_Equity`; the census must FIND them, and any others), a census that lists only the form the gateway builds (the raw key) and calls the encoded form absent, a census that prints a count without its denominator, a classifier that cannot tell the raw form from the encoded (it has a negative control), a "none" cell read as "absent from the world" when the table has no partitions at all, and a census whose expectation is edited to match.
</preflight>

## 0. THE CELL

A security key that contains a slash (for example `BP/_LN_Equity`) has two spellings in S3: the RAW key as typed (`security_key=BP/_LN_Equity/`, a nested path) and the ENCODED partition that `lib/research/identity/crosswalk.py::security_key_partition` returns (`security_key=BP-SLASH-_LN_Equity/`; `lib/research/harvest/store.py::entity_partition` goes through it, and `write_one` partitions with it). The CTO measured, live, through the gateway: for `BP/_LN_Equity` the RAW key returns reports but no dossier, continuation or ai_fill; the ENCODED key returns those three but no reports. **So writers and readers disagree on how a slash key is spelled, and a reader of either form gets an incomplete record that does not say it is incomplete.** This cell measures, read-only, for EVERY slash key in the corpus, which table holds objects under which spelling. It writes nothing and changes no file.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`.
a. Read first: `lib/research/identity/crosswalk.py` (`security_key_partition`), `lib/research/harvest/store.py` (`entity_partition`), `lib/research/corpus/gold.py` (`table_prefix`, how a gold table is addressed) and the prefix constants of `infra/aws/ec2/opal-gateway/app/harvest_research.py` (lines 40-60: `P_DOSSIER`, `P_CONTINUATION`, `P_AI_FILL`, `P_REPORT`, `P_EXEC`, and the others it names) so you know which prefixes the gateway builds from the raw key. Note that the gateway's constants spell some tables with an underscore (`research_dossier`) and the stored gold tables are the hyphenated and underscored spellings the producers write: the census uses the table names it FINDS by listing, never a typed list.
b. Write `cj1_census.py` in your deliverables folder and run it once in the FOREGROUND with `python -u`, stdout to `cj1_census.out` (open the output file with `newline="\n"`). Start from `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~170/ci3_census.py` for the client and budget handling (read it; do not run it).
c. **The tables:** under each root `amgt/harvest/` and `bloomberg/harvest/`, list the layers (`bronze`, `silver`, `gold`, and any other the listing shows) and each layer's tables with a delimiter listing; a TABLE is "keyed by security" when at least one of its immediate children starts with `security_key=`; print one line per table found `TABLE <root>/<layer>/<table> keyed_by_security=<yes|no> security_partitions=<n>` (a table of date partitions, such as the silver research-report, is `no`; it holds the security in a COLUMN and is handled by step e).
d. **The slash keys (found, never typed):** a security key is a SLASH KEY when it contains `/` once DECODED (`-SLASH-` back to `/`). Find them from the listings of step c: for every keyed-by-security table, the immediate children `security_key=<X>/` whose `<X>` contains `-SLASH-` are encoded partitions, and the children whose listing continues one more level before any object (a nested raw key such as `security_key=BP/` holding `_LN_Equity/`) are raw ones. Print `DENOMINATOR slash_keys=<n> found_in_tables=<n>` and one line `SLASHKEY-FOUND <decoded key>`. A key found only in one table is still a key.
e. **The matrix:** for EVERY slash key and EVERY keyed-by-security table print one line `SLASHKEY <decoded key> table=<table> form=<raw|encoded|both|none> raw_objects=<n> encoded_objects=<n>` where RAW is the prefix `security_key=<decoded key>/` and ENCODED is `security_key=<security_key_partition(decoded key)>/` (call the module's function; never type the encoding), counting objects by a listing under each prefix (a nested raw key lists the objects below it). For a date-partitioned table that holds the security in a column (the silver research-report), print `SLASHKEY <decoded key> table=<table> column_form=<raw|encoded|both|none> rows=<n>` after reading ONLY the `security_key` column of the parquet parts (a get of each part is allowed within the budget; print the number of parts read) and counting the distinct values that equal the raw key and the encoded partition string. Print `none` only for a table that HAS security partitions and holds neither form of that key.
f. **The controls (rule 22: a census needs both).** POSITIVE: for the NON-slash key `UNH_US_Equity`, print `CONTROL-POSITIVE UNH_US_Equity raw_equals_encoded=yes` when the raw prefix and the encoded prefix the census builds are the SAME string (the two spellings of a key with no slash must be one). NEGATIVE: run the census's own classifier (the function that decides `raw|encoded|both|none` from two object counts) on four synthetic pairs and print `CONTROL-NEGATIVE synthetic raw_only=raw encoded_only=encoded both=both neither=none` (each word is the classifier's output for the pair (3,0), (0,3), (2,2), (0,0)).
g. The final line, exactly: `CENSUS-SLASH slash_keys=<n> tables=<n keyed by security> cells=<keys x tables> raw=<n> encoded=<n> both=<n> none=<n> gets=<requests> bytes=<bytes>` (`raw`, `encoded`, `both` and `none` count the matrix cells by `form`, and the silver column cells by `column_form`). **The issuer expects `slash_keys=2` or more** (the two known keys; print any others plainly). The counts are the FINDING: do not change anything to make them read anything. If the census would exceed its budget, STOP at the budget, print `BUDGET-EXCEEDED gets=<n>` and file a row.
h. File ONE surprise row summarising the matrix: which tables hold which keys under which form, in a sentence per table, and which stored objects sit under a form the gateway's raw-key prefixes would not reach. Do not guess a reason you cannot read. Do not touch any source file. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~171/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cj-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~171/cj1_census.out</invocation><expect>(?m)^CENSUS-SLASH slash_keys=([2-9]|\d\d+) tables=\d+ cells=\d+ raw=\d+ encoded=\d+ both=\d+ none=\d+ gets=\d+ bytes=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cj-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~171/cj1_census.out</invocation><expect>(?m)^CONTROL-POSITIVE UNH_US_Equity raw_equals_encoded=yes$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cj-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~171/cj1_census.out</invocation><expect>(?m)^CONTROL-NEGATIVE synthetic raw_only=raw encoded_only=encoded both=both neither=none$</expect></criterion>
</proof_of_spec>

- AC1 is the shape (and the 2 or more slash keys the issuer expects); its counts are the finding. AC2 and AC3 are the controls. **If a control prints another line, DO NOT edit the expectation or the code to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~07:2xZ):** all three FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W171-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~171/AMGT_HARVST.TO-HVST-cj-1.census-of-slash-keys-which-table-holds-which-key-form.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cj-1.census-of-slash-keys-which-table-holds-which-key-form` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cj-1.census-of-slash-keys-which-table-holds-which-key-form.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line (a commentary on the matched line breaks the `$` anchor).
- A foreground command must finish inside the tool's ten-minute limit: if the census would not, run it in slices by table (a `--table-start` and `--table-stop`), appending to a parts file and merging in a `--final`, as `ci3_census.py` does for names.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-94 analysis (`ledger/ROUND_ANALYSIS.round94.md` @428b762698, msg 7946) item 1 ("first, a census over every slash key in the corpus, printing the denominator: for each, which tables hold it under which form ... any stored object left under the wrong form becomes a row, never a rename or a delete") and graduated row `W170-S3`.
- Chain A of round 95: this cell, then `HVST-cj-2` (the unification), `HVST-cj-3` (its gateway release) and `HVST-cj-5` (the slash-key dossiers): all DEFINED and held on this census (decomposition section 125): the direction of the fix (which spelling every reader and writer takes) depends on what this census shows about where each table's objects sit, and the stored reports may sit under the RAW form while the writers partition by the encoded one.
- Slot ~171, worktree `C:/dev/wk-harvst-171`, branch `wk-AMGT_HARVST-171`. Widen the sparse set at provision with `lib/research`, `.claude/agents`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922`, `infra/aws/ec2/opal-gateway/app` and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~170`.
- **SENT:** with the round-95 issuance.

**COMPLETE 2026-10-18T07:5xZ (issuer `2.0.0_SA_COO~W1`):**
- **Act:** worker `0.9.0_WK_AMGT_HARVST~171` (haiku, high), branch `wk-AMGT_HARVST-171`; census `7e7a254fc3`, proof `a3fb3c6c3e`; merged `bc1f5233ec` (safe-merge fast lane, index check 0 of 4). No source file changed (deliverables and one surprise row).
- **AC1 PASS:** `CENSUS-SLASH slash_keys=2 tables=15 cells=32 raw=2 encoded=26 both=0 none=4 gets=135 bytes=247364`. **AC2 PASS:** `CONTROL-POSITIVE UNH_US_Equity raw_equals_encoded=yes`. **AC3 PASS:** `CONTROL-NEGATIVE synthetic raw_only=raw encoded_only=encoded both=both neither=none`. **I re-ran `cj1_census.py` myself from the worker's worktree (135 requests): identical to the worker's, line for line.** Proof instance VALID rc 0 (re-run here).
- **THE FINDING (item 1 of the CTO's round-94 analysis):** the corpus holds exactly TWO slash keys (`BP/_LN_Equity`, `NG/_LN_Equity`), found by listing, in 13 of 15 keyed-by-security tables (35 tables found: 15 keyed by security, 14 date-partitioned only, 6 empty). **In every keyed table the keys sit ONLY under the ENCODED partition** (26 cells `encoded`, 2 `raw`, 0 `both`, 4 `none`): 214 objects (BP 116, NG 98), including `research-report` and its extract in bronze, `ai_fill`, both spellings of the dossier table, `research-continuation`, `exec_officers`; the RAW spelling holds 0 objects in every keyed table. The 2 `raw` cells are the silver `research-report` COLUMN (BP 14 rows, NG 2 rows, encoded 0), and the 4 `none` are `histdata_daily_px` and `identity` (neither key in either spelling). **So no stored object sits under a form the writers do not use; the defect is the gateway's raw-key prefixes, which match 0 objects of either key** (the worker's reading of `harvest_research.py` 40-60: `P_DOSSIER`, `P_AI_FILL`, `P_EXEC` listed; `P_CONTINUATION` and `P_REPORT` name table spellings the listing does not show). The reason for any of this is not read.
- **Disclosures:** the first run reported 361 false keys (hash folders under `security_key=<KEY>/` read as nested raw keys); the worker tightened the rule to a canonical key tail and re-ran; only the second run is committed. Budget: about 11,100 requests across its three runs against 12,000 (the committed run is 135). Date-partitioned tables other than the silver research-report were not column-checked, as ordered (`DATE-ONLY-NOT-COLUMN-CHECKED`). Row `D1-W171-S1` (class OBSERVATION, hazard ARMED, disarm owner me, UNDER_INVESTIGATION): **it stays ARMED**: it names the standing condition `HVST-cj-2` fixes and `HVST-cj-3` releases; I disarm it with a served read of both keys in both spellings through the live gateway after `cj-3` (decomposition section 126).
- **What this does NOT prove:** the other tables' date partitions; that no OTHER spelling of a slash key exists (a key with a different token, a lowercase variant); the live gateway's behaviour (read from code and from the CTO's live read, not re-measured today); why the silver holds the raw spelling.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>95</round>
<workstream>SLASH-CENSUS</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
