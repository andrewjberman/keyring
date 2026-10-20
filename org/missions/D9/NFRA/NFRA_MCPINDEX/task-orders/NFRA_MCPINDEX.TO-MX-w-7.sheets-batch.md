# NFRA_MCPINDEX task order -- `MX-w-7` -- cheatsheet.py learns `gen-all`: one cheat sheet per roster person, a person without a profile on the legacy admit set, every sheet narrowed by the person's relevance buckets, a placeholder line for a person whose role is not recorded

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md</decomp_doc>
<owned_cells>MX-w-7</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-w-7.sheets-batch</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~83</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; an edit to one existing script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the mutant controls the issuer ran against a reference are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-w-7` (round 24, workstream GATEWAY; PRD v0.19 FWD-25; CTO round-23 analysis item 7)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). FWD-25 is a cheat sheet for each employee. Round 22 built `cheatsheet.py gen`, which writes ONE person's sheet from a grants file that lists the person. Round 24 needs a sheet for all 17 people on the roster, and 15 of them have NO profile and so appear in no grants file: they are on the gateway's legacy path, whose admit set is read from a measured tier-decisions file. The sheet is then narrowed by the person's relevance (the buckets of tools their job uses); the access itself does not change. You EDIT `workflows/gateway_battery/cheatsheet.py` (add a `gen-all` command; keep `gen` exactly as it is) and add one new test file.

**What to build.** In `workflows/gateway_battery/cheatsheet.py`, a second subcommand:

```
python workflows/gateway_battery/cheatsheet.py gen-all --census F --grants F --tier-decisions F --graded F --connect F --roster F --relevance F --out-dir D
```

and `workflows/gateway_battery/tests/test_cheatsheet_batch.py` with at least 5 tests. The existing `tests/test_cheatsheet.py` must keep passing unchanged, and `gen` must print and write exactly what it does today. Read the script first: `read_census`, `read_grants`, `read_graded`, `read_roster`, `build_sheet`, `Refusal` and `gen` are what you reuse.

### The contract (it is the whole specification)

**Inputs** (all read-only; each unreadable or malformed one is a refusal, see Refusals):
- `--census`, `--grants`, `--graded`, `--connect`, `--roster`: exactly the files `gen` reads today (`gateway_surface_census/1`; `gateway_grants/1` whose `principals[]` carry `who` and `by_channel`; `gateway_battery_graded/1`; the connect text; the roster is a TEXT file, one email per line, blank lines ignored, repeats ignored).
- `--tier-decisions`: `gateway_tier_decisions/1`, `{"schema","claim","guard","tools":[{"tool","channel","path","mutating","write_class","min_tier","tiers":{"read_only":{"admitted":bool,"layer","code"},"standard":{...},"master_admin":{...}}}]}`: for each tool, what the installed entitlement decision admits at each tier for a person with NO profile. A tool with `tiers[T].admitted` true is on the legacy admit set of tier T.
- `--relevance`: `gateway_sheet_relevance/1`, `{"schema","people":[{"who":str,"role":str|null,"buckets":[names],"placeholder":bool,"tier":optional str}]}`. `who` is an email. `buckets` are names from this closed list: `assets`, `schwab`, `blackdiamond`, `harvest`, `etfs`, `portal`, `news`, `m365`. `tier` is one of `read_only`, `standard`, `master_admin` and defaults to `read_only`.

**Emails** are compared lower-cased everywhere (the roster may say `Andrew@x.com` where the grants say `andrew@x.com`). A person's file name is the lower-cased local part (the text before `@`) plus `.md` and `.examples.json`; a local part that is empty or holds `/` or a backslash is a refusal.

**Who is admitted to what (access, never changed by relevance).**
- A roster person who has a principal in the grants file (a PROFILE person) is admitted to the principal's `by_channel`, exactly as `gen` does.
- A roster person with NO principal is on the LEGACY path: the person's tier is their relevance entry's `tier`; their `by_channel` is built from the tier-decisions file: every tool whose `tiers[tier].admitted` is true, grouped under its `channel`. Nothing else is admitted. (So a person without a profile never gets a client, Schwab or Black Diamond tool, and a `read_only` person never gets a sender: the measured decisions say so; do not hard-code any tool or channel name.)

**Narrowing by relevance (applies to every person, profile or not).** Each tool has one bucket: a tool whose name starts with `news_` is bucket `news` whatever its channel; otherwise the bucket is by channel: `opal-data-assets` -> `assets`; `schwab` -> `schwab`; `blackdiamond` -> `blackdiamond`; `opal-data-harvest` -> `harvest`; `opal-data-etfs` -> `etfs`; `opal-data-portal-v2`, `opal-data-mdpf` and `portal_index` -> `portal`; `m365` -> `m365`; any other channel -> `other`. A tool stays on the person's sheet when its bucket is one of the person's `buckets`, or when its bucket is `m365` or `other` (every person keeps their own Microsoft 365 tools and the discovery and general tools). Then the sheet is built with `build_sheet` from the narrowed `by_channel`, so channel headings follow the census order and a channel with no tool left is not listed. The channel ids and the bucket words are the contract's fixed words and may appear in the script.

**The placeholder sheet.** When the person's relevance entry has `placeholder` true, the sheet carries, immediately after the line `Tested <started_at>.` and separated from it by a blank line, exactly this line (the buckets in the order the entry lists them, joined by `, `, then a full stop):

```
PLACEHOLDER SHEET: your role is not recorded yet, so this sheet shows the tools of these buckets: portal, news.
```

No other sheet carries a line that starts `PLACEHOLDER SHEET`.

**Output.** For each distinct roster person, in roster order: `<out-dir>/<local>.md` and `<out-dir>/<local>.examples.json`, produced the way `gen` produces them (same `build_sheet` text and the same examples list). The script writes only under `--out-dir` (creating it), reads no clock and no network, and the same inputs give byte-identical files. Last stdout line (and the only stdout): `SHEETS people=P written=W legacy=L placeholder=H` -- `P` distinct roster people, `W` sheets written, `L` people on the legacy path, `H` people whose entry has `placeholder` true. Exit 0.

**Refusals.** Exit 2 with ONE line on stderr starting `ERROR:`, and NOTHING written (not even the output folder), for: an unreadable or malformed input file; a roster person with no entry in the relevance file; a relevance bucket name outside the closed list; a relevance `tier` outside the three tiers; a legacy person whose tier the tier-decisions file does not carry. Validate everything first, write last. The refusal must come from your code (a line starting `ERROR:`), not from argparse.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/fixtures/w7_census.json`, `w7_tiers.json`, `w7_grants.json`, `w7_graded.json`, `w7_connect.md`, `w7_roster.txt`, `w7_relevance.json` (same folder): a 12 tool, 8 channel census; tier decisions in which a `read_only` person is denied `client_get_holdings`, `schwab_list_files` and `send_email` and a `standard` person is denied the first two; one profile person (`andrew`, all 12 tools); a 4 person roster (the profile person with a mixed-case email, two legacy people with a role, one legacy placeholder person); the relevance entries for them. These are the criteria's inputs; read them to see the shapes, and write your own small inputs inside your tests.
- Real shapes, for orientation (do not read them in the criteria): `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round23/evidence/TIER_DECISIONS_20261019.json` (the real tier decisions), `.../round22/evidence/GATEWAY_GRANTS_20261019_v2.json` (the real grants), `.../round23/evidence/ROSTER_17_20261019.txt` (the real roster, mixed-case emails), `.../round23/sheets/adam.md` (what `gen` wrote for one legacy person).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree already carries the sparse folders `workflows/gateway_battery`, `workflows/gateway_battery/tests`; if another folder you need is missing, `git sparse-checkout add <folder>` is the only sparse change you may make.
1. Read the script, the existing `tests/test_cheatsheet.py` and the fixtures above, then `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w7_check.py` (the arms for your cell). Make the command and the new test file. The test file holds at least 5 tests of its own: they run the script as a subprocess on small inputs you write inside the test with `tmp_path` (not the issuer's fixtures). There is no `__init__.py`: scripts are run by path.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, any other script under `workflows/`, `members.yaml`, the catalog, the emitter, any file under `infra/`, the PRD, or any other file. No AWS call, no network call, no grant, no deploy, no push, no upload and no send: `gen-all` writes local files only.
2. Python 3.9, standard library only. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, firm or vendor is typed as a whole-string literal in the script (the contract's fixed words -- the bucket names, channel ids, the `news_` prefix, the tier names, the placeholder line -- are fine); tests under `tests/` and data files are exempt.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w7.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `.../round24/checks/w7_check.py`). Read `w7_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/cheatsheet.py
workflows/gateway_battery/tests/test_cheatsheet_batch.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~83/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-w-7.sheets-batch.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W83-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-w-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w7.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; gen-all exits 0 and prints SHEETS people=4 written=4 legacy=3 placeholder=1; one .md and one .examples.json per roster person named by the lower-cased local part; each of the four sheets lists exactly its expected tools (the profile person all 12, the legacy people the tier admit set narrowed by their buckets, with news by name prefix and the m365 and other tools kept); the existing gen is unchanged -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-w-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w7.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; no legacy sheet lists a client, Schwab, Black Diamond or sender tool; the placeholder line appears only on the flagged person, after the Tested line; the examples hold only passed questions of listed tools; two runs are byte-identical; nothing outside --out-dir changes; a standard tier in the relevance entry admits the sender; a missing relevance entry, an unknown bucket and an unreadable tier-decisions file each exit 2 with an ERROR line and no file -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-w-7" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/checks/w7.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 5 passed) for `test_cheatsheet_batch.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~83/NFRA_MCPINDEX.TO-MX-w-7.sheets-batch.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 24, workstream GATEWAY, worker ~83. Source: the CTO's round-23 analysis `ledger/ROUND_ANALYSIS.round23.md` item 7 (a sheet for each of the 17; a person without a profile is on the legacy path; the eight with no recorded role get the placeholder relevance; Andrew's yes on calls 5ccb and 8cdf @50bd4a33b4: sheets narrow by relevance, access unchanged; placeholder sheets stand for the eight), PRD v0.19, the CRO's roster map `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/GATEWAY_EMPLOYEE_ROSTER_BUCKET_MAP_20261019.md`. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round24-GATEWAY.md` (R24.3 W7). **The face restates W7 and CORRECTS it** against the real inputs: the roster file is a plain list of emails with no role, so the roles and the placeholder flag come from a new `--relevance` file the issuer builds from the CRO map at the drain; the legacy admit set is read from the measured `--tier-decisions` file (the CRO map says the legacy path reads harvest, ETFs, portal-v2, MDPF, news and the person's own Microsoft 365 tools, so a hard-coded harvest/etfs/portal/portal_index/news set would have been wrong); `gen` has no placeholder text, so the line is fixed in the contract; the bucket `other` and `m365` are kept for everyone (issuer ruling). The decomposition paragraph W7 must be amended to match before the issuance commit. Base dry-runs 2026-10-20: w7.AC1 base: FAIL as expected (1 of 7 arms ok: only the unchanged-gen arm); w7.AC2 base: FAIL as expected (0 of 12 arms ok); w7.AC3 base: FAIL as expected (test file absent). The issuer's scratch reference (a copy of the merged script carrying a reference gen-all, outside the repository) passes w7.AC1 (7 arms), w7.AC2 (12 arms) and w7.AC3 (6 tests); nine planted mutants (legacy ignores the tier decisions; news by channel only; placeholder line for everyone; a missing relevance entry tolerated; case-sensitive roster; m365 not kept; wrong legacy count; tier choice ignored; a stray file next to the inputs) each read FAIL on AC1 or AC2. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>24</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
