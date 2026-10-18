# AMGT_HARVST task order -- `HVST-ck-1` -- ROUND 96, workstream PATHKEY-CENSUS: A READ-ONLY CENSUS OF THE PATH-COMPONENT PREFIXES UNDER BOTH SPELLINGS OF EVERY SLASH KEY (rows `D1-W171-S4` and `-S6`; CTO round-95 analysis section 3 item 3 and enrichment item 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ck-1.census-of-the-path-component-prefixes-under-both-slash-key-spellings</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ck-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~172</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- READ-ONLY S3 reads (list and get) of the buckets and prefixes the gateway's harvest tools read, through `lib.research.harvest.store._default_client()` or the same client the gateway's `harvest_typed` helpers use (read `infra/aws/ec2/opal-gateway/app/harvest_typed.py` and `deliverables/0.9.0_WK_AMGT_HARVST~171/cj2_replay.py`, whose S3 shim you may reuse); never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 4000 requests and 400 MiB in all, counted in the census's last line. NO writer is RUN, NO deploy, NO edit of any source file, NO edit outside `<paths>`; you DO NOT call the live gateway.
comp-adversary: RUN at L5 -- the adversary is a census that lists only the raw spelling (the gateway's), a census that compares object NAMES but not BYTES, a same-name pair read as equal because only the size or the ETag was compared on a multipart object, a prefix list typed from memory instead of read from the code, a slash key list typed instead of found, a classifier that cannot tell equal from different (it has a negative control), and a census whose expectation is edited to match.
</preflight>

## 0. THE CELL

`HVST-cj-2` and `HVST-cj-6` made the gateway read the `security_key=<...>/` PARTITION tables of the two slash keys (`BP/_LN_Equity`, `NG/_LN_Equity`) from their one stored form. The tools that address a key by PATH COMPONENT instead of a `security_key=` partition (the peers, scores and posture reads and the filings, drafting and management reads of `harvest_research.py`; the model-block reads of `harvest_figures.py`; the coverage and publication-link templates of `harvest_identity.py`) still build their prefix from the caller's spelling, and the stored tables hold BOTH spellings (the `cj-2` replay: `peers/v1/BP/_LN_Equity/` 7 objects and `peers/v1/BP-SLASH-_LN_Equity/` 10; NG 7 and 10; posture, scores and filings 1 and 1). **The CTO ruled (round-95 analysis, section 3): the split is NOT accepted; readers will resolve to the canonical spelling and read the UNION of the canonical prefix and the legacy raw prefix, canonical winning a same-name collision; no stored object is renamed or deleted; a read-only census comes first, and a same-name pair whose bytes differ is a row (two different objects claiming one name).** This cell is that census. It writes nothing and changes no file.

## 1. THE BUILD (a read-only script; no product code)

Work in your worktree. Change only the files named in `<paths>`.
a. **Find the prefixes (read, never typed).** From `deliverables/0.9.0_WK_AMGT_HARVST~171/cj2_sites.out` and `cj6_sites.out` (their `CONST` and `SITE` lines, classes `OTHER`) and from the code itself (`infra/aws/ec2/opal-gateway/app/harvest_research.py`, `harvest_figures.py`, `harvest_identity.py`), list EVERY prefix or key template that is built from a caller's `security_key` and is NOT a `security_key=<...>/` partition: the starting list is `management/v1/%s/`, `filings/v1/%s/`, `drafting/v1/%s.json`, `peers/v1/%s/`, `scores/v1/%s.json`, `posture/v1/%s/`, the model-block prefixes of `harvest_figures.py` (`MODEL_PREFIX`, `FYE_PREFIX`) and the coverage and publication-link templates of `harvest_identity.py` (`_segment` and its templates, `packs/%s/input_ledger.json`). **The CTO counts 8 tools; print every prefix you find with its source `file:line`, its shape (a directory of objects, or one object `<key>.json`) and the tool that reads it, and the number found; do not force it to 8.** Print `PREFIX <name> template=<the format string> source=<file:line> shape=<dir|object> tool=<tool name>`.
b. **Find the slash keys (read, never typed).** Take the slash keys from `deliverables/0.9.0_WK_AMGT_HARVST~171/cj1_census.out` (`SLASHKEY-FOUND` lines; 2 today), and confirm by listing that no other key under any of the prefixes contains a slash or `-SLASH-` (print the count of keys listed per prefix as the denominator).
c. **The census.** Write `ck1_census.py` in your deliverables folder (start from `cj2_replay.py` for the S3 shim and `cj1_census.py` for the listing and budget handling; read both) and run it once in the FOREGROUND with `python -u`, stdout to `ck1_census.out` (open it with `newline="\n"`). For EVERY slash key and EVERY prefix, list the objects under the RAW spelling (`<key>` as typed, `BP/_LN_Equity`, a nested path) and under the CANONICAL spelling (`security_key_partition`'s slash-safe form of the key, `BP-SLASH-_LN_Equity`; call `crosswalk.slash_safe_key`, never type the encoding): for a directory prefix the objects under each; for an object prefix (`<key>.json`) the one object each, if present. Match objects by their NAME relative to the prefix. For EVERY same-name pair (present under both spellings) GET both bodies and compare their SHA-256 (not the size, not the ETag); print one line per cell `CELL <key> <prefix> raw_objects=<n> canonical_objects=<n> same_name=<n> same_name_equal=<n> same_name_differ=<n> raw_only=<n> canonical_only=<n>` and, for EVERY same-name pair, `PAIR <key> <prefix> <name> raw_sha256=<first 12> canonical_sha256=<first 12> equal=<yes|no> raw_bytes=<n> canonical_bytes=<n> raw_last_modified=<utc> canonical_last_modified=<utc>`.
d. **The controls (rule 22: a census needs both).** POSITIVE: for the NON-slash key `UNH_US_Equity`, print `CONTROL-POSITIVE UNH_US_Equity raw_equals_canonical=yes` when the raw prefix and the canonical prefix the census builds for every prefix are the SAME string (so a key without a slash is read once). NEGATIVE: run the census's own pair classifier on four synthetic pairs (same name and same bytes; same name and different bytes; a name under the raw spelling only; a name under the canonical spelling only) and print `CONTROL-NEGATIVE synthetic equal=equal differ=differ raw_only=raw_only canonical_only=canonical_only` (each word is the classifier's output).
e. The final line, exactly: `CENSUS-PATHKEY slash_keys=<n> prefixes=<n> cells=<keys x prefixes> raw_objects=<n> canonical_objects=<n> same_name=<n> same_name_differ=<n> gets=<requests> bytes=<bytes>`. **The issuer expects `slash_keys=2` and `prefixes` near 8.** The counts are the FINDING: do not change anything to make them read anything. If the census would exceed its budget, STOP at the budget, print `BUDGET-EXCEEDED gets=<n>` and file a row.
f. **Rows:** file ONE surprise row summarising the matrix (per prefix: objects under each spelling, same-name pairs, how many differ) and ONE row for EVERY same-name pair whose bytes differ (two different objects claiming one name, the CTO's rule), each with the reason you can read (two objects with different `LastModified` and content; do not guess a reason you cannot read). Do not touch any source file. A surprise is a row; keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~172/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ck-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~172/ck1_census.out</invocation><expect>(?m)^CENSUS-PATHKEY slash_keys=([2-9]|\d\d+) prefixes=\d+ cells=\d+ raw_objects=\d+ canonical_objects=\d+ same_name=\d+ same_name_differ=\d+ gets=\d+ bytes=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ck-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~172/ck1_census.out</invocation><expect>(?m)^CONTROL-POSITIVE UNH_US_Equity raw_equals_canonical=yes$</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ck-1"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~172/ck1_census.out</invocation><expect>(?m)^CONTROL-NEGATIVE synthetic equal=equal differ=differ raw_only=raw_only canonical_only=canonical_only$</expect></criterion>
</proof_of_spec>

- AC1 is the shape (and the 2 or more slash keys the issuer expects); its counts are the finding. AC2 and AC3 are the controls. **If a control prints another line, DO NOT edit the expectation or the code to match: print the actual line, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-18 ~12:0xZ):** all three FAIL as expected (`cat` of a file that does not exist). If a base state differs, say so and do not weaken a pattern.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W172-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~172/AMGT_HARVST.TO-HVST-ck-1.census-of-the-path-component-prefixes-under-both-slash-key-spellings.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ck-1.census-of-the-path-component-prefixes-under-both-slash-key-spellings` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ck-1.census-of-the-path-component-prefixes-under-both-slash-key-spellings.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line (a commentary on the matched line breaks the `$` anchor).
- A foreground command must finish inside the tool's ten-minute limit: if the census would not, run it in slices by prefix, appending to a parts file and merging in a `--final`, as `ci3_census.py` does for names.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-95 analysis (`ledger/ROUND_ANALYSIS.round95.md` @031ac46589, msg 8025) section 3 item 3 and enrichment item 1.
- Chain A of round 96: this cell, then `HVST-ck-2` (the union-read change, same worker queue `~172`), then the release `HVST-ck-3` (seat SC1, DEFINED and held).
- Slot ~172, worktree `C:/dev/wk-harvst-172`, branch `wk-AMGT_HARVST-172`. **Sparse set at provision (checked against `<paths>` and the files named in the face this time): `lib/research`, `.claude/agents`, `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922`, `infra/aws/ec2/opal-gateway/app`, `infra/aws/ec2/opal-gateway/tests` and `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~171`** (for the `cj1`, `cj2` and `cj6` scripts and outputs).
- **SENT:** with the round-96 issuance.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>96</round>
<workstream>PATHKEY-CENSUS</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
