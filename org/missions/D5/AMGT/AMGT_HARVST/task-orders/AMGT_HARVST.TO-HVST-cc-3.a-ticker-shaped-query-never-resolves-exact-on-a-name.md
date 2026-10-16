# AMGT_HARVST task order -- `HVST-cc-3` -- ROUND 88, workstream S29-RESOLVE: A TICKER-SHAPED QUERY THAT MATCHES NO TICKER SLOT NEVER RESOLVES `exact` ON A NAME (D1-S29 defect 3; CTO round-87 analysis section 1 and ERRATUM 1 @74515c1f4a)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cc-3.a-ticker-shaped-query-never-resolves-exact-on-a-name</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cc-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~152</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and tests only. NO S3 call, NO AWS call, NO network, NO deploy, NO edit outside `<paths>`. The tests use the in-memory fakes the existing gateway identity tests use.
comp-adversary: RUN at L5 -- the adversary is a rule so wide that a real company name typed in capitals ("VISA") stops resolving, a rule so narrow that "PG" still answers exact, a ticker that matches a ticker slot being demoted, and a test that passes whatever the code does.
</preflight>

## 0. THE CELL

`harvest_resolve_security("PG")` (live, 2026-10-16) returns status `exact`, `security_key` `PCG_US_Equity` ("PG&E Corp"), `matched_on` `name`. The harvest universe holds 243 securities and Procter & Gamble is NOT one of them (live: "Procter & Gamble" and "PG US Equity" both answer `none`), so "PG" matches no ticker slot and falls through to the NAME rule (`infra/aws/ec2/opal-gateway/app/harvest_identity.py` lines 436-441, `_name_hit` word-start at 248-251), which finds the word "PG" at the start of "PG&E". A two-letter ticker-shaped query then answers `exact` on the wrong company. The CTO ruled (ERRATUM 1): **a ticker-shaped query that matches no ticker slot never returns `exact` on a name; "PG" gives `none` or `candidates`, and PCG still resolves by its own ticker. Whether to add Procter & Gamble to the universe is NOT part of this cell.**

## 1. THE BUILD (LOCAL, about 80 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `infra/aws/ec2/opal-gateway/app/harvest_identity.py` add a module regex `TICKER_SHAPE` (an all-uppercase query of 1 to 5 letters, optionally one `.` or `-` plus 1 to 2 letters: `^[A-Z]{1,5}([.-][A-Z]{1,2})?$`, tested against the raw query text with its spaces stripped only if the query has none inside; a query containing a space, `&`, a digit or a lowercase letter is NOT ticker-shaped). In `harvest_resolve_security`, in the name branch (after the `len(needle) < 2` check, at `named = ...`): when the raw query is ticker-shaped AND `named` is non-empty, return `_candidates(named, "name", index)` with `reason` set to `"no ticker matches %r; these companies have a name that starts with it" % raw` and status `candidates` (NEVER `exact`, even when `named` holds one key and even when several keys share one issuer). Every other query keeps today's path unchanged. Edit nothing else in the file.
b. New test `infra/aws/ec2/opal-gateway/tests/test_cc3_ticker_shaped_never_exact_on_name.py`, offline, following the harness of the existing identity tests (`tests/test_og_gt1.py` lines 130-229 hold the cases; copy the fixtures you need, edit nothing in that file). Fixture: a crosswalk and universe holding `PCG_US_Equity` ("PG&E Corp", ticker `PCG US`), `KMB_US_Equity` ("Kimberly Clark KMB"), `V_US_Equity` ("Visa Inc", ticker `V US`) and no Procter & Gamble:
   - (1) `"PG"` -> status `candidates` (not `exact`), `candidates` includes `PCG_US_Equity`, `matched_on` `name`;
   - (2) `"PCG"` and `"PCG US"` and `"PCG_US_Equity"` -> `exact` `PCG_US_Equity` (matched on a ticker or identifier level, unchanged);
   - (3) `"PG&E"` and `"PG&E Corp"` -> unchanged (`exact` `PCG_US_Equity` on name: they are not ticker-shaped);
   - (4) `"Kimberly Clark"` -> unchanged `exact` `KMB_US_Equity`; `"visa"` (lowercase) -> unchanged `exact` `V_US_Equity` on name; `"V"` -> `exact` on its ticker;
   - (5) `"VISA"` (all capitals) -> `candidates` (it is ticker-shaped and matches no ticker slot), NOT `exact`, and the reason text names the query;
   - (6) **A MUTANT:** with the new branch disabled (monkeypatch `TICKER_SHAPE` to a pattern that never matches), arm (1) FAILS (assert that it does). It proves arm (1) discriminates.
c. Do not run anything against S3, AWS, a box or a browser; do not edit any other file. A surprise is a row; keep working.

<paths>
infra/aws/ec2/opal-gateway/app/harvest_identity.py
infra/aws/ec2/opal-gateway/tests/test_cc3_ticker_shaped_never_exact_on_name.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~152/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cc-3"><invocation>bash infra/aws/ec2/opal-gateway/tests/run_release_suites.sh tests/test_cc3_ticker_shaped_never_exact_on_name.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cc-3"><invocation>bash infra/aws/ec2/opal-gateway/tests/run_release_suites.sh tests/test_og_gt1.py tests/test_og_gt3.py tests/test_og_gt4.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^16 passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-16 ~15:2xZ):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`16 passed`). If your worktree's base count differs, say so with both counts and do not weaken the pattern. If an existing test in those files asserts the OLD behaviour for a ticker-shaped name query, that is a surprise row (do not edit the file): report which and keep working.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W152-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~152/AMGT_HARVST.TO-HVST-cc-3.a-ticker-shaped-query-never-resolves-exact-on-a-name.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cc-3.a-ticker-shaped-query-never-resolves-exact-on-a-name` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cc-3.a-ticker-shaped-query-never-resolves-exact-on-a-name.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-87 analysis item 2 (c) as corrected by ERRATUM 1 (`ledger/ROUND_ANALYSIS.round87.md` @74515c1f4a, msg 6780): P&G is not in the universe; the cell is "a ticker-shaped query that matches no ticker slot never returns `exact` on a name". Close condition (REMEDIATION_v19): the surfacing seat reads "PG" on the SERVED tool; this cell is LOCAL only, the deploy is `HVST-cc-7` (staged).
- **Live reads by the issuer (2026-10-16 ~15:1xZ):** `PG` -> exact PCG by name; `Procter & Gamble` -> none; `PG US Equity` -> none; `KIMBERA MM` -> none; `Kimberly Clark` -> exact KMB by name (denominator 243, `crosswalk/v1/2026-10-09.json`, `universe/v1/2026-10-06.json`).
- **A named residual:** a real company whose name is a 1-to-5-letter all-capitals word typed in capitals ("VISA", "IBM" where IBM is held as a ticker is unaffected) will answer `candidates` instead of `exact` when it matches no ticker slot; that is the ruled behaviour.
- **Class (gate, spine v3.19 L6):** `<paths>` names `infra/aws/ec2/opal-gateway/app/...`, an infrastructure path, so the floor is WORLD and the order is declared WORLD (the first commit attempt declared LOCAL and was REFUSED by `to-pipeline-gate`). The worker's acts stay LOCAL (code and offline tests, no deploy); the deploy is `HVST-cc-7`. It is not a direct act: it takes the full limbs and its close is the issuer's real run, `HVST-cc-7`'s served read.
- Slot ~152, worktree `C:/dev/wk-harvst-152`, branch `wk-AMGT_HARVST-152`. Widen the sparse set at provision with `org/tier1_exec/4.0.0_SA_CRO/scripts` and `infra/aws/ec2/opal-gateway`.
- **SENT:** with the round-88 issuance.

<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>88</round>
<workstream>S29-RESOLVE</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
