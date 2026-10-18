# AMGT_HARVST task order -- `HVST-cj-6` -- ROUND 95, workstream SLASH-OTHER: THE OTHER GATEWAY HARVEST TOOLS THAT BUILD A `security_key=` PARTITION FROM THE CALLER'S KEY RESOLVE A SLASH KEY TO ITS ONE STORED FORM (row `D1-W171-S5`; CTO round-94 analysis item 1 "the gateway's harvest tools normalize the requested key"; code and offline tests only, no release)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cj-6.the-other-gateway-harvest-tools-resolve-a-slash-key-to-its-one-stored-form</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cj-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~171</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests, plus READ-ONLY S3 reads of the bucket `opal-data-harvest` in the replay step ONLY, through `lib.research.harvest.store._default_client()`; never `put`, `delete`, `copy`, `sync` or a bare `aws` call. Budget: at most 3000 requests and 300 MiB in all, counted in the replay's last line. NO writer is RUN, NO deploy, NO edit outside `<paths>`; you DO NOT call the live gateway.
comp-adversary: RUN at L5 -- the adversary is a fix that changes `harvest_figures.py` and leaves `harvest_identity.py` (or the reverse) on the raw key, a THIRD copy of the normalizer (there is one copy in the app, in `harvest_research.py`; import it, or move the one copy to a module every harvest tool imports and have `harvest_research.py` import it from there, with the equality test of `HVST-cj-2` still holding), a change to a prefix that is NOT a `security_key=` partition (the peers, posture, scores, filings, drafting and management prefixes hold BOTH spellings and stay on the caller's spelling: the CTO decides that), a normalizer that changes a key with no slash (it must be the identity there), a test that passes whatever the code does (it has a mutant), a change to `tools.py` or any file outside `<paths>` (a surprise row instead), and a replay run against the live gateway.
</preflight>

## 0. THE CELL

`HVST-cj-2` (merged `c692c5dfbb`) made the three tools of `harvest_research.py` read a slash key (`BP/_LN_Equity`, `NG/_LN_Equity`) from its ONE stored form: the partition form `security_key=BP-SLASH-_LN_Equity/`, with the canonical raw key for the silver column; its replay reads the whole record in all four calls (raw and encoded, both keys). Your own rows found the same defect in two other gateway modules: `harvest_figures.py` (the bestdata, refdata, histdata and segments tables: lines about 186-192, 228, 248, 259, 278 and 440) and `harvest_identity.py` (line about 454) build `security_key=%s/` prefixes from the caller's raw key, while those tables hold the ENCODED spelling only (`cj1_census.out`: bestdata BP 15 and NG 15, refdata 16 and 16, histdata 16 and 16, segments 1 and 1, raw 0 in each), so those tools reach no stored object for BP or NG. **The CTO's spec is that the gateway's harvest tools normalize the requested key through the one rule before reading.** This cell applies the SAME normalizer to every remaining gateway module that builds a `security_key=` partition from a caller's key. It changes nothing for a key with no slash, and it does NOT touch the prefixes that are not `security_key=` partitions. It does not release anything.

## 1. THE BUILD (LOCAL code; about 40 product lines)

Work in your worktree (the same as `HVST-cj-2`). Change only the files named in `<paths>`. If the fix needs a file outside `<paths>` (`app/tools.py` is in another lane), STOP, file a row naming the file and why, and finish the rest.
a. **Audit first (`cj6_sites.out`, read-only):** list EVERY `app/harvest_*.py` module (`harvest_figures.py`, `harvest_identity.py`, `harvest_press.py`, `harvest_published.py`, `harvest_read.py`, `harvest_typed.py`; `harvest_research.py` is done) and every site where a prefix or key is built from a caller's `security_key` (print `file`, `line`, the function, the prefix constant or format string, and a class: `PARTITION` for a `security_key=<key>/` partition, `OTHER` for any other shape such as a path component, a column compare or a free-form key). The census of the stored tables is `deliverables/0.9.0_WK_AMGT_HARVST~171/cj1_census.out`; the CTO's two key spellings are `crosswalk.slash_safe_key` and its inverse (read `harvest_research.py` `canonical_security_key` and `slash_safe_key`, your own `HVST-cj-2` change).
b. **The change:** at the ENTRY of every tool of the modules the audit classes `PARTITION` (the two named above, and any other it finds), compute the canonical raw key and the partition form with THE existing normalizer (`canonical_security_key`, `slash_safe_key`; one definition in the app, never a third copy: import it, or move the one definition to a module that every harvest tool imports and import it from there in `harvest_research.py` too, keeping `HVST-cj-2`'s equality test green), build every `PARTITION` prefix from the PARTITION form, use the canonical raw key for any column compare and for the key the tool prints, and return the existing `harvest_bad_argument` refusal for a malformed key (the `_bad_key` shape of `harvest_research.py`). A `security_key=` prefix inside a module the audit finds `OTHER`, and every non-partition prefix, stays on the caller's spelling and is NAMED in a row, not changed.
c. New test `infra/aws/ec2/opal-gateway/tests/test_cj6_slash_key_other_tools.py`, offline (a fake `ht` listing in the style of `test_cj2_slash_key_one_form.py`; change nothing in any existing test). Arms: (1) **the difference-controlled test:** for each changed tool, a fake store holding objects ONLY under `security_key=BP-SLASH-_LN_Equity/`: the tool called with `BP/_LN_Equity` AND with `BP-SLASH-_LN_Equity` returns the stored objects both ways; the OLD behaviour (the normalizer monkeypatched to the identity) returns nothing for the raw call; (2) a key with no slash (`UNH_US_Equity`) is byte-for-byte unchanged in every prefix and in the body; (3) every `PARTITION` site the audit lists reads the PARTITION form (assert the prefix each `ht` call receives); (4) a malformed key is refused with the existing shape; (5) **A MUTANT:** with the normalizer monkeypatched to the identity, arm (1) FAILS (assert that it does); (6) there is ONE normalizer definition in the app (assert that `harvest_figures`, `harvest_identity` and `harvest_research` resolve `canonical_security_key` to the same function object).
d. **The replay (read-only, `cj6_replay.py`, stdout to `cj6_replay.out` with `newline="\n"`):** run the CHANGED tool code of each changed tool against the REAL stored objects without calling the gateway, with an S3 read-only `ht` shim as `cj2_replay.py` did, for `BP/_LN_Equity` and `NG/_LN_Equity` in BOTH spellings (every changed tool x 2 keys x 2 forms). For each print `REPLAY-OTHER <tool> <requested key> objects_reached=<n>` (the number of stored objects the tool's body names) and `REPLAY-OLD <tool> <requested key> objects_reached=<n>` from the OLD prefix building (kept in the replay as a small copy), then, as the LAST lines, `REPLAY-OTHER-WHOLE cells=<n> reached_both_forms_equal=<n of n whose raw and encoded calls reach the same non-zero number of objects>` and `REPLAY-OTHER-TOTALS gets=<requests> bytes=<bytes>`. **The issuer expects `reached_both_forms_equal` equal to `cells`** (the counts are the FINDING; do not change anything to make them read so; a tool the stored tables give zero objects for in both forms is reported as such, with its table, and is not counted as a failure of the fix). Print one `REPLAY-CONTROL UNH_US_Equity ...` line per changed tool from the SAME code path.
e. Do not edit `tools.py`, the stored objects, `lib/research`, `harvest_research.py`'s peers, posture, scores, filings, drafting or management prefixes, or any other file. A surprise is a row; keep working.

<paths>
infra/aws/ec2/opal-gateway/app/harvest_*.py
infra/aws/ec2/opal-gateway/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~171/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cj-6"><invocation>python -m pytest infra/aws/ec2/opal-gateway/tests/test_cj6_slash_key_other_tools.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cj-6"><invocation>python -m pytest infra/aws/ec2/opal-gateway/tests/test_ce3_parts_absent_wording.py infra/aws/ec2/opal-gateway/tests/test_cd1_dossier_misfiled.py infra/aws/ec2/opal-gateway/tests/test_cc1_model_basis.py infra/aws/ec2/opal-gateway/tests/test_cc2_research_misfiled.py infra/aws/ec2/opal-gateway/tests/test_cc3_ticker_shaped_never_exact_on_name.py infra/aws/ec2/opal-gateway/tests/test_og_gt1.py infra/aws/ec2/opal-gateway/tests/test_og_gt3.py infra/aws/ec2/opal-gateway/tests/test_og_gt4.py infra/aws/ec2/opal-gateway/tests/test_cg4_report_fund_relation.py infra/aws/ec2/opal-gateway/tests/test_cj2_slash_key_one_form.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^56 passed in</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cj-6"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~171/cj6_replay.out</invocation><expect>(?m)^REPLAY-OTHER-WHOLE cells=(\d+) reached_both_forms_equal=\1$</expect></criterion>
</proof_of_spec>

- AC1 is the difference-controlled test with its mutant. AC2 is the unchanged-behaviour check: the ten existing gateway test files (56 tests at the base, issuer dry run 2026-10-18 ~08:1xZ, after the `HVST-cj-2` merge) must still pass; do not change any of them. AC3's `\1` makes the replay grade itself: every changed tool reaches the same number of stored objects for the raw and the encoded request, for each key.
- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`56 passed in 3.04s`); AC3 FAIL as expected (`cat` of a file that does not exist). If your base count differs, say so with both counts and do not weaken the pattern.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- **The release applies this diff onto the live gateway (`DEPLOY_BASE_REF=aa2efa2cf3`).** Keep the diff small and confined to the sites of step a so it applies cleanly.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id follows your last (`AMGT_HARVST-D1-W171-S<n+1>`). The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~171/AMGT_HARVST.TO-HVST-cj-6.the-other-gateway-harvest-tools-resolve-a-slash-key-to-its-one-stored-form.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cj-6.the-other-gateway-harvest-tools-resolve-a-slash-key-to-its-one-stored-form` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cj-6.the-other-gateway-harvest-tools-resolve-a-slash-key-to-its-one-stored-form.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Put commentary on its own line in the instance's `output_evidence`, never on the matched line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: the CTO's round-94 analysis item 1; the worker's row `D1-W171-S5` (ARMED, disarm owner me) found the two modules. **The claim of my `cj-1` note ("the corpus holds exactly two slash keys, stored only under the encoded partition in every keyed table") was bounded by the census's two roots and by `security_key=` partitions, and the worker's `cj-2` replay found tables outside both (peers, posture, scores, filings hold BOTH spellings); I corrected the `cj-1` note.** This cell is inside the CTO's spec and needs no ruling; the peers, posture, scores, filings, drafting and management prefixes (row `D1-W171-S4`) are NOT in this cell: they hold both spellings and the CTO decides which spelling a reader takes.
- Slot ~171, worktree `C:/dev/wk-harvst-171` (the same as `cj-1` and `cj-2`; its sparse set carries the gateway `app` and `tests` folders), branch `wk-AMGT_HARVST-171`. The order file on the worker's branch is the grant.
- **Why one more cell before the release:** `HVST-cj-3` is ONE gateway release; shipping `cj-2` alone would leave the figures and identity tools blind to the two keys and need a second release.
- **SENT:** with the round-95 recut (the issuer continues the same worker).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>95</round>
<workstream>SLASH-OTHER</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
