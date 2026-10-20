# NFRA_MCPINDEX task order -- `MX-y-1` -- source compare by class: independent probes for graph, integration and store tools, and the by-key comparison for S3 sources whose keys carry no date

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md</decomp_doc>
<owned_cells>MX-y-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-y-1.source-compare-classes</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~84</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; an edit to one existing script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant. The script only lists (fake listings in the criteria).
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base; the round-24 regression arm of y1.AC2 passes there) and the planted arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-y-1` (round 25, workstream GATEWAY; PRD v0.19 FWD-24; CTO round-24 analysis `ledger/ROUND_ANALYSIS.round24.md` item 1)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The source comparison `workflows/gateway_battery/source_compare.py` (merged, round 24) lists each tool's routed S3 source (list only) and compares the answer's as-of date with the dates in the listed keys. The live run over the 104 tools that have an ok result agreed on 25, disagreed on 1 and could not read 78: graph 31, integration 9, store 4, and S3 with no date token 34. You EDIT the script so that (a) the 44 graph, integration and store tools can be compared with an INDEPENDENT measurement the issuer supplies in a probes file, and (b) an S3 source whose keys carry no date is compared BY KEY. You also add one new test file. Everything the script did before must stay byte for byte when `--probes` is absent and no key rule fires.

**What to build.** Read the script first (`compare_tool`, `list_source`, `answer_strings`, `choose_source`, `run`, `main`). Then:

1. Add the optional option `--probes FILE`. Load it, validate it (rules below), and for every tool that has a probe write its entry from the probe instead of listing anything.
2. Make `list_source` also return the object keys it saw directly under the prefix (the `Contents` keys), so that the by-key rule can reuse the first listing.
3. Add the by-key rule in `compare_tool`, after the listing and before the date rule.
4. Add `workflows/gateway_battery/tests/test_source_compare_classes.py` with at least 8 tests of your own (see the model below).

### The contract (verbatim from the decomposition; it is the whole specification)

**Y1 SOURCE COMPARE BY CLASS.** `source_compare.py` keeps its round-24 contract and gains `--probes FILE` (optional; absent = the round-24 behavior byte for byte). Probes: `{"schema":"gateway_source_probes/1","probes":[{"tool","class":"graph"|"integration"|"store","instrument":str,"fact":str,"value":str,"answer_value":str}]}` written by the issuer from independent reads (a graph tool against the owner's own mailbox, calendar or files read through a second route; an integration against the vendor's own API read once outside the gateway; a store against a direct DynamoDB read). For a tool with a probe, the entry reports `source` as the first source of its set, `instrument` as the probe's, `agrees` true when `value` equals `answer_value` after trimming and case folding, false otherwise, `reason` the fact compared, `source_dates` []. A probe naming a tool absent from the census, a class that does not match the tool's source kind, or two probes for one tool exits 2. S3 sources with no date token are compared BY KEY: when the result's `answer_source` carries an object key (a string with a final path segment containing a dot) and the listing under the source prefix contains exactly that key, `agrees` is true with `reason` "object key present in the listing"; when the listing is non-empty and does not contain it, false; when the answer carries no key, null with the round-24 reason. Counts and stdout line unchanged. Same input, same bytes.

### The settled silences (the issuer's rulings; follow them)

1. **A probe's entry.** `tool` and `case_ids` and `answer_as_of` are filled exactly as in round 24 (`answer_as_of` from the first ok result that carries a non-empty `as_of`). `source` is `{"kind","bucket","prefix"}` (strings) of the FIRST source of the tool's `source_set` in the routing file. `instrument` is the probe's `instrument` string verbatim; `reason` is the probe's `fact` string verbatim; `source_dates` is `[]`; `agrees` is a bool. The entry has exactly the round-24 keys and no other. A tool with a probe is not listed. Counts (`agrees`, `disagrees`, `unreadable`) and the stdout line `SOURCE tools=T agrees=A disagrees=D unreadable=U` are computed over all entries as before.
2. **Probe validation, every failure is exit 2 with `REFUSED: ...` on stderr and NO output file** (the same discipline as the round-24 refusals; an argparse error is not enough, the text must start `REFUSED:`): the file does not exist or is not a JSON object; `schema` is not exactly `gateway_source_probes/1`; `probes` is not a list of objects; a probe lacks any of the six fields as a non-empty string (after stripping); `class` is not one of graph, integration, store; `tool` is not in the census; `tool` has no ok result in the results file (a probe cannot stand for a tool the comparison does not otherwise report); the tool's routing `source_set` is empty or the `kind` of its FIRST source differs from the probe's `class`; two probes name one tool.
3. **The by-key rule applies** when the chosen S3 source's listing is non-empty and holds no date token (round 24's "undated" case), whatever the result's `as_of` says. The object key is the first `answer_source` string of the tool's ok results (a leading `s3://` dropped, as `answer_strings` already does) that starts with `<bucket>/` of the chosen source, whose remainder (the key) starts with the source prefix, and whose final path segment contains a dot. The key's directory is the key up to and including its last `/` (empty if there is none). The key is PRESENT when it is among the object keys listed directly under that directory with Delimiter `/` (`Contents`). When the directory equals the source prefix, reuse the keys of the first listing: do NOT list the same bucket and prefix twice (the fake client serves each page once per `<bucket>|<prefix>`, and a second call raises "no fake page 1"). When the directory differs (the key lies below the listed level), list that directory with the same helper (the fake key is `<bucket>|<directory>`). Present -> `agrees` true, `reason` exactly `object key present in the listing`; absent -> `agrees` false, `reason` exactly `object key absent from the listing`; the `instrument` string then also names the key's directory. A listing error during the key listing gives null with the round-24 style `listing error: <type>: <text>` reason. When the answer carries no such key, nothing changes: null with the round-24 reason. When the source listing HAS date tokens, the round-24 date rule decides, exactly as before.
4. **Nothing else moves.** `--fake` keeps its meaning and format; `partition_windows.py` is imported, never edited; the script still performs list calls only (no object get, put, copy, delete or download call; the criterion greps for such tokens).

### Inputs you read (you do NOT edit them)

- The merged script `workflows/gateway_battery/source_compare.py`, `workflows/gateway_battery/partition_windows.py` (the fake client and `build_client`), and the round-24 test file `workflows/gateway_battery/tests/test_source_compare.py` (the model for a test file: the script is run by path as a subprocess on small inputs written inside the test with `tmp_path`).
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/fixtures/y1_census.json`, `y1_cases.json`, `y1_results.json`, `y1_routing.json`, `y1_fake.json`, `y1_probes.json`, `y1_r24_expected.json` and `y1_r24_expected.stdout`: the criteria's fixtures (10 tools: a dated S3 tool, probes for graph, integration and store tools, undated S3 tools with and without the answer's key in the listing, a key below the listed level, a graph tool with no probe). The round-24 fixtures `round24/fixtures/w1_*.json` serve the byte-identity arm.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. FIRST run `git sparse-checkout add workflows/gateway_battery workflows/atom_decomposition infra/aws/ec2/opal-gateway/app` (the only sparse change you may make; the issuer pre-adds them, and the command is harmless when they are there). Without them the cone can lack the script, its tests or the files the commit gate reads.
1. Read `source_compare.py` and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y1_check.py` (the executable form of this section; read what each arm grades). Make the changes, then the test file: at least 8 tests of your own, on small inputs you write inside the test (not the issuer's fixtures). They cover at least: a probe with equal values after trimming and case folding gives true; unequal gives false and exit 1; a class that does not match the tool's first source kind exits 2; two probes for one tool exit 2; a probe for an unknown tool exits 2; the by-key rule gives true for a present key and false for an absent one; no key in the answer leaves null with the undated reason; a key below the listed level is found through its own directory; a dated listing still uses the date rule.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `partition_windows.py`, any other script or test under `workflows/`, `members.yaml`, `pending_members.yaml`, the catalog or its row files, the emitter, any file under `infra/`, the PRD, or the round-23/24 evidence. No AWS call, no network call, no grant, no deploy, no push. The criteria write their outputs under a temporary directory.
2. Python 3.9, standard library only. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39, and it BLOCKS a strict-utf-8 `open()` of a path whose name or variable contains `log` or `catalog`: write `errors="replace"` on any `open()` you add for reading.
3. No tool name, channel id, firm or vendor is typed as a whole-string literal in the script; tests under `tests/` and data files are exempt.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output (no new key in an entry, no new option beyond `--probes`).
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y1.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `y1_check.py` in the same folder). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/source_compare.py
workflows/gateway_battery/tests/test_source_compare_classes.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~84/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-y-1.source-compare-classes.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W84-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-y-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y1.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (10 fixture tools); the stdout line SOURCE tools=10 agrees=5 disagrees=3 unreadable=2 with rc 1 and the file written; the graph, integration and store probes read true, false, true and false with the probe's instrument and fact; the graph tool with no probe stays null and not read here; the undated S3 tools read true (key present), false (key absent), null (no key in the answer) and true (key below the listed level); the dated S3 tool is still decided by the date rule -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-y-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y1.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; without --probes the round-24 fixtures give the same output bytes and stdout as the frozen round-24 run; the two planted flips read false and the counts follow; the eight refusals each exit 2 with REFUSED on stderr and no file; two runs give the same bytes; the script holds no object read or write call and has a --probes option -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-y-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y1.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 8 passed) for `test_source_compare_classes.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~84/NFRA_MCPINDEX.TO-MX-y-1.source-compare-classes.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes. The checker matches `expect` as a regex against your recorded output: encode the literal printed tokens, and record the output so that `RESULT: PASS` is followed by `exit=0`.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip. Message files are written with the Write tool, ASCII, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 25, workstream GATEWAY, worker ~84. Source: the CTO's round-24 analysis (`1.0.0_SA_CTO~Z`, msg 36225, `ledger/ROUND_ANALYSIS.round24.md` @e03f975441) item 1 and PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md` (contract R25.3 Y1, frozen at the cut). The independent reads that fill a probes file (a graph tool against the owner's mailbox or calendar through a second route, an integration against the vendor's own API, a store against a direct DynamoDB read) are the issuer's drain acts (R25.4 step 3), not this cell: the cell builds the comparator and the by-key rule. Settled silences 1 to 4 above are the issuer's reading of the one-line contract. Round-24 lessons carried into this face: the sparse cone may lack `workflows/gateway_battery`, `workflows/atom_decomposition` and `infra/aws/ec2/opal-gateway/app` (step 0); the commit gate blocks a strict utf-8 `open()` on a path whose name contains `log` or `catalog`; every mutant in the checks is planted from the fixture data actually present; the refusal arms require the script's own `REFUSED:` text so that an argparse error cannot pass them at the base.
Base dry-runs 2026-10-20 (script and test file as merged at the cut; the new test file absent): `y1.AC1` base: FAIL as expected (0 of 15 arms ok: `--probes` is an unrecognized option, rc 2); `y1.AC2` base: FAIL as expected (1 of 13 arms ok, the round-24 byte-identity arm, which passes at the base by design; the 12 others fail); `y1.AC3` base: FAIL as expected (test file absent). The issuer's scratch reference (a copy of the merged script with the change and nine tests, outside the repository, pointed at with `Y1_PKG_DIR`) passes all three (15 of 15, 13 of 13, 9 tests); a reference that skips the class check fails `y1.AC2` on its refusal arm, and a reference that answers every key as present fails `y1.AC1` on three arms and `y1.AC2` on both planted flips.

<status>issued</status>
<round>25</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
