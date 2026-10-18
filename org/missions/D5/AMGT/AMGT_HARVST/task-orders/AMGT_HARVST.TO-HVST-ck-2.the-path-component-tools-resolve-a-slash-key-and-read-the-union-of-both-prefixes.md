# AMGT_HARVST task order -- `HVST-ck-2` -- ROUND 96, workstream PATHKEY-UNION: THE PATH-COMPONENT TOOLS RESOLVE A SLASH KEY TO ITS CANONICAL SPELLING AND READ THE UNION OF THE CANONICAL AND THE LEGACY RAW PREFIX, CANONICAL WINNING A SAME-NAME COLLISION (rows `D1-W171-S4` and `-S6`; CTO round-95 analysis section 3 item 2 and enrichment item 2; code and offline tests, no release)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ck-2.the-path-component-tools-resolve-a-slash-key-and-read-the-union-of-both-prefixes</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ck-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~172</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests, plus READ-ONLY S3 reads in the replay step ONLY (the same client and S3 shim as `deliverables/0.9.0_WK_AMGT_HARVST~171/cj2_replay.py`); never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 4000 requests and 400 MiB in all, counted in the replay's last line. NO writer is RUN, NO deploy, NO edit outside `<paths>`; you DO NOT call the live gateway.
comp-adversary: RUN at L5 -- the adversary is a union that lets the LEGACY object win a same-name collision, a union that drops a name present under only one spelling (nothing stored under either spelling may stop being reachable), a change that moves, copies or writes any object, a change to a key without a slash (it must read the same prefix once, byte-equal to today, with NO new field), a tool of the eight that is left on the caller's spelling, a second normalizer (use `harvest_keys.canonical_security_key` and `slash_safe_key`), an object served without saying which spelling it came from, a test that passes whatever the code does (it has a mutant), a change to `tools.py` or any file outside `<paths>` (a surprise row instead), and a replay run against the live gateway.
</preflight>

## 0. THE CELL

`HVST-cj-2` and `HVST-cj-6` (merged `34fb405b29`, live in the gateway release `6575999df5` since 10:52:49Z) made the `security_key=<...>/` partitions of the two slash keys (`BP/_LN_Equity`, `NG/_LN_Equity`) read from their one stored form. The tools that address a key by PATH COMPONENT still read the caller's spelling, and the stored tables hold BOTH (`peers/v1/BP/_LN_Equity/` 7 objects and `peers/v1/BP-SLASH-_LN_Equity/` 10; NG 7 and 10; posture, scores and filings 1 and 1; the two coverage cells differ: BP raw 129 and canonical 150, NG 109 and 128). **The CTO's ruling (round-95 analysis, section 3):** the split is NOT accepted; each reader resolves the requested key to the canonical spelling (`slash_safe_key` through `harvest_keys`) and reads BOTH the canonical prefix and the legacy raw prefix: the UNION, the canonical winning a same-name collision; each object served carries which spelling it came from; so nothing stored under either spelling stops being reachable and no object is moved, copied or deleted. Your earlier order `HVST-ck-1` (same worker queue) printed the prefixes (`PREFIX` lines) and the same-name pairs of the census in `ck1_census.out`: read it first. This cell changes the readers, proves it offline and by a read-only replay, and does NOT release anything.

## 1. THE BUILD (LOCAL code; about 60 product lines)

Work in your worktree. Change only the files named in `<paths>`. If the fix needs a file outside `<paths>` (`app/tools.py` is in another lane), STOP, file a row naming the file and why, and finish the rest.
a. Read first: `ck1_census.out` (its `PREFIX`, `CELL` and `PAIR` lines), `infra/aws/ec2/opal-gateway/app/harvest_keys.py` (`canonical_security_key`, `slash_safe_key`), the path-component sites in `harvest_research.py` (`P_MANAGEMENT`, `P_FILINGS`, `P_DRAFTING`, `P_PEERS`, `P_SCORES`, `P_POSTURE` and every use), `harvest_figures.py` (`MODEL_PREFIX`, `FYE_PREFIX`) and `harvest_identity.py` (`_segment`, the coverage templates, `packs/%s/input_ledger.json`), and `infra/aws/ec2/opal-gateway/tests/test_cj6_slash_key_other_tools.py` (the fake `ht` and style to copy). Print the list of tools and prefixes you change in `ck2_sites.out` (one line per prefix: `file:line`, the prefix, the tool, shape `dir` or `object`).
b. **The change:** one small helper in `harvest_keys.py` (the one normalizer module; no second normalizer) that, for a path-component prefix template and a requested key, returns the prefixes to read: for a key WITHOUT a slash, the one prefix exactly as today (the same `ht` call, byte-equal body, NO new field); for a slash key, the CANONICAL prefix (`slash_safe_key(raw)` in the template) and the LEGACY RAW prefix (the raw key in the template). Every one of the eight tools' path-component reads (the sites of step a) uses it: **directory shape:** list both prefixes, union the objects by NAME relative to the prefix, the canonical object winning a same-name collision, and apply the tool's existing selection (for example "the newest by name") to the UNION; **object shape (`<key>.json`):** the canonical object if it exists, else the legacy raw one. An object read from the legacy raw prefix is never copied or written anywhere. **Each object served carries which spelling it came from:** for a slash key the tool's body gains a field `stored_spelling` mapping each part that read a path-component object to `"canonical"` or `"legacy_raw"`; the `source_keys` keep naming the stored key as stored. A key without a slash gets no `stored_spelling` and an unchanged body.
c. New test `infra/aws/ec2/opal-gateway/tests/test_ck2_path_component_union_read.py`, offline (a fake `ht` listing in the style of `test_cj6_slash_key_other_tools.py`; change nothing in any existing test). Arms: (1) **the difference-controlled test:** for each of the eight tools a fake store with objects of `BP/_LN_Equity` under BOTH spellings (some names only raw, some only canonical, some in both): the tool called with `BP/_LN_Equity` AND with `BP-SLASH-_LN_Equity` returns the SAME objects (the union), and the OLD behaviour (the helper monkeypatched to return only the caller's spelling) returns different sets for the two spellings; (2) a same-name pair with different bytes: the CANONICAL object is served and `stored_spelling` says `canonical`; (3) a name present only under the raw spelling is still served, `stored_spelling` says `legacy_raw`; (4) a key with no slash (`UNH_US_Equity`): the same `ht` calls as before (assert the prefixes) and a body byte-equal to the unchanged tool, with no `stored_spelling`; (5) the union never writes (the fake `ht` has no write); (6) **A MUTANT:** with the helper monkeypatched to the caller's spelling only, arm (1) FAILS (assert that it does); (7) a second mutant: with the legacy object allowed to win a collision, arm (2) FAILS.
d. **The replay (read-only, `ck2_replay.py`, stdout to `ck2_replay.out` with `newline="\n"`):** run the CHANGED tool code against the REAL stored objects without calling the gateway, with the S3 read-only `ht` shim of `cj2_replay.py`, for `BP/_LN_Equity` and `NG/_LN_Equity` in BOTH spellings and EVERY tool of step a (including coverage): print `REPLAY-UNION <tool> <requested key> objects_reached=<n> from_canonical=<n> from_legacy_raw=<n>`, then, as the LAST lines, `REPLAY-UNION-WHOLE cells=<tools x 2 keys> equal=<n of cells whose raw and canonical requests reach the same objects>` and `REPLAY-UNION-TOTALS gets=<requests> bytes=<bytes>`. **The issuer expects `equal` equal to `cells`** (every tool, both spellings, the same objects; coverage included: it closes row `D1-W171-S6`); the counts are the FINDING, do not change anything to make them read so. Also print one `REPLAY-CONTROL UNH_US_Equity <tool> objects_reached=<n>` per tool from the SAME code path and `REPLAY-COLLISIONS same_name_pairs=<n> canonical_served=<n>` (from `ck1_census.out`'s `PAIR` lines: every same-name pair is served from the canonical prefix).
e. Do not edit `tools.py`, the stored objects, `lib/research`, or any other file. Do not run a release or a deploy. A surprise is a row; keep working.

<paths>
infra/aws/ec2/opal-gateway/app/harvest_*.py
infra/aws/ec2/opal-gateway/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~172/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ck-2"><invocation>python -m pytest infra/aws/ec2/opal-gateway/tests/test_ck2_path_component_union_read.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ck-2"><invocation>python -m pytest infra/aws/ec2/opal-gateway/tests/test_ce3_parts_absent_wording.py infra/aws/ec2/opal-gateway/tests/test_cd1_dossier_misfiled.py infra/aws/ec2/opal-gateway/tests/test_cc1_model_basis.py infra/aws/ec2/opal-gateway/tests/test_cc2_research_misfiled.py infra/aws/ec2/opal-gateway/tests/test_cc3_ticker_shaped_never_exact_on_name.py infra/aws/ec2/opal-gateway/tests/test_og_gt1.py infra/aws/ec2/opal-gateway/tests/test_og_gt3.py infra/aws/ec2/opal-gateway/tests/test_og_gt4.py infra/aws/ec2/opal-gateway/tests/test_cg4_report_fund_relation.py infra/aws/ec2/opal-gateway/tests/test_cj2_slash_key_one_form.py infra/aws/ec2/opal-gateway/tests/test_cj6_slash_key_other_tools.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^75 passed in</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ck-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~172/ck2_replay.out</invocation><expect>(?m)^REPLAY-UNION-WHOLE cells=(\d+) equal=\1$</expect></criterion>
</proof_of_spec>

- AC1 is the difference-controlled test with its two mutants. AC2 is the unchanged-behaviour check: the eleven existing gateway test files (75 tests at the base, issuer dry run 2026-10-18 ~12:0xZ) must still pass; do not change any of them. AC3's `\1` makes the replay grade itself: for every tool and both keys the raw and the canonical request reach the same objects. **If it reads less, DO NOT edit the expectation or the code to match: print the actual lines, add a row and report.**
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`75 passed in 4.01s`); AC3 FAIL as expected (`cat` of a file that does not exist). If your base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- **The release applies this diff onto the live gateway (the live commit at the release, `6575999df5` today).** Keep the diff small and confined to the sites of step a so it applies cleanly.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id follows your last (`AMGT_HARVST-D1-W172-S<n+1>`). The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~172/AMGT_HARVST.TO-HVST-ck-2.the-path-component-tools-resolve-a-slash-key-and-read-the-union-of-both-prefixes.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ck-2.the-path-component-tools-resolve-a-slash-key-and-read-the-union-of-both-prefixes` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ck-2.the-path-component-tools-resolve-a-slash-key-and-read-the-union-of-both-prefixes.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-95 analysis @031ac46589 (msg 8025) section 3 items 2 and enrichment items 2 and 4 (this cell's replay is the OFFLINE re-read of coverage for `D1-W171-S6`; the served re-read is part of the release `HVST-ck-3`).
- **Class `WORLD` is the L6 gate's floor for an `infra/` path, not a deploy.**
- Chain A, second order, same worker queue `~172`: depends on `HVST-ck-1` (its census names the prefixes and the same-name pairs). I hand it to the SAME worker by continuing it after `ck-1` merges, with this order file (and the decomposition) on its branch.
- Slot ~172, worktree `C:/dev/wk-harvst-172`, branch `wk-AMGT_HARVST-172`; its sparse set carries the gateway `app` and `tests` folders (checked at provision).
- **SENT:** with the round-96 issuance (the order is cut now; the worker starts it after `ck-1`).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>96</round>
<workstream>PATHKEY-UNION</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
