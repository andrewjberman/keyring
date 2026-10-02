# AMGT_RESAPP task order -- `AMGT-ak-3` -- PLAIN SERVED REASONS: THE LUSHA SKIP REASON AND THE PEERS ABSENT-COLUMN REASONS IN WORDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ak-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~201</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; served-text code and a read-only plan.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read or write by the served code; the plan builder only READS the pool.
comp-adversary: RUN by the issuer at the cut -- AC2 FAILS at the base: C1 11 of 26 strings (10 peers absent-column reasons across BA and VLO, 1 VLO Lusha reason); C2 the producer still answers the domains.json sentence.
EGRESS CLASS, declared: NONE. No Lusha call, no vendor call of any kind.
</preflight>

**Your worktree:** `C:/tmp/r61-201` (branch `wk-AMGT_RESAPP-201`, cut from the issuance commit; full checkout). Work and commit only there.

## 1. THE ACT -- `AMGT-ak-3` (round 61, decomposition s.69; DSGN round-21 analysis section 3B cell B2)

The page prints two served strings that carry codes. Rewrite each AT THE FUNCTION THAT BUILDS IT, as words a reader of the page
understands: never a security key (`VLO_US_Equity`), a field code (`ey_ntm`, `cash_mv`, `ebit_est_rev_45d`), a file name
(`domains.json`) or a status token (`ABSENT`). Do not strip words in a post-filter. Keep each sentence's meaning.

1. **The Lusha skip reason.** `lib/research/management/enrich.py:domain_for` (line ~153) builds "no declared domain for VLO_US_Equity in
   domains.json (5 name(s) declared): Lusha is scoped by company domain and a guessed domain enriches the wrong company". The served
   Exec tab prints it from `thesis.management.lusha_enrichment.reason`, which is STORED in the name's M-1 object
   (`management/v1/<key>/<as_of>.json` in the pool, read verbatim by `scoped_amgt.read_management`). Rewrite the producer's sentence
   (for example: "Contact enrichment was skipped: no company web domain is on record for this name, and a guessed domain would
   enrich the wrong company"). Keep the technical facts in a field the page does not print if a test or consumer needs them.
2. **The peers absent-column reasons.** The peers route serves `csc_columns.absent[*].reason` built at SERVE time from the factor
   registry (`factor_metadata_registry.json`), e.g. "cash_mv is 'Cash to Market Value', a ratio; no absolute cash level". Rewrite at the
   builder so each reason names the measure by its registry LABEL, never its code.
3. **The rewrite plan for the STORED Lusha reasons.** Write a read-only builder that lists every M-1 object in the pool whose newest
   `lusha_enrichment.reason` matches `[a-z]+_[a-z0-9_]+|_Equity|\.json|ABSENT`, and computes its replacement BY CALLING THE FIXED
   PRODUCER CODE (never a hand-typed string). Emit
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~201/m1_lusha_reason_plan.json`:
   `{"denominator": <M-1 objects scanned>, "entries": [{"security_key", "route": "thesis", "json_path": ".management.lusha_enrichment.reason", "store_key": "<the exact pool key>", "store_field": "lusha_enrichment.reason", "before": "<as stored>", "after": "<the producer's new sentence>"}]}`.
   VLO_US_Equity must be an entry. The builder WRITES NOTHING to the pool.
4. **Tests** in `lib/research/management/tests/` (the producer sentence) and `lib/research/api/tests/` (the peers reasons): the old
   string shape fails, the new passes.

## 2. BOUNDS

1. Write only the paths below. Text only: no figure, rank, field name or officer change. No deploy, NO STORE WRITE (ak-6 writes),
   no Lusha or other vendor call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/management/
lib/research/api/
lib/research/metrics/
lib/research/peers/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~201/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ak-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/ lib/research/management/tests/ lib/research/peers/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0 (AMENDMENT 1: the 3 test_print_format_rich.py setup errors on an unpopulated portal fixture are admitted in a worker worktree; the issuer re-grades on the shared tree)</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ak-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/checks/b_served_text.py --cell b2 --where local --plan org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~201/m1_lusha_reason_plan.json; echo "exit=$?"</invocation><expect>C0 PASS (every plan entry's before equals what the route serves now), C1 PASS (0 of the Lusha and peers absent reasons for BA and VLO carry a code-shaped token), C2 PASS; B2 EVERY SERVED REASON IS WORDS: YES -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-ak-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/checks/b_served_text.py --cell b5 --where local --plan org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~201/m1_ceo_basis_plan.json; echo "exit=$?"</invocation><expect>C0 PASS (every plan entry's before equals what the route serves now), C1 PASS (BA's and VLO's served CEO-search basis says neither SERP nor contract's search), C2 PASS; B5 THE CEO SEARCH BASIS IS WORDS: YES -- and exit=0 (AMENDMENT 2)</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~201 <0.9.0_WK_AMGT_RESAPP~201@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~201/AMGT_RESAPP.TO-AMGT-ak-3.plain-served-reasons.proof_of_spec.json`.
Report once: the commit hash, both criteria's output lines, every function whose text you changed, the plan's denominator and entry
count, and any row. The `<status>` flip is the issuer's.

## 6. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~07:5xZ) -- on row AMGT_RESAPP-Z-W201-S1

The peers absent-column reasons are STORED in `peers/v1/<key>/<as_of>.json` and written by `lib/research/peers/csc.py`
(`_CLAIMED_ABSENT`, used by `build_csc_map`). A served string is fixed at its producer, so `lib/research/peers/` is granted.
5. `csc.build_csc_map` emits the plain, registry-label reason for every absent column. The templates move into
   `lib/research/peers/`, and nothing there imports `lib/research/api/`. The machine fields (`nearest_code`,
   `nearest_registry_name`, `derivable_from`) are unchanged.
6. The plan's peers entries carry exactly what the fixed producer emits, computed by calling it. One entry set per key, on the
   NEWEST object the route reads; the per-key denominator is printed.
AC1 adds `lib/research/peers/tests/`.

## 7. AMENDMENT 2 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~08:4xZ) -- cell B5 (CTO msg 28318, analysis @2b1e921054), on B2's terms

`lib/research/management/enrich.py:ceo_public_profile` (lines ~536-566) writes the CEO search's `basis` into the STORED M-1 object, and
the Exec tab prints it. Today VLO reads "no declared IR domain for this name: a SERP not scoped to the company's own domain is not the
contract's search", and BA reads "the SERP returned 2 url(s) and none on boeing.com -- ABSENT is the honest result, never a page from
another host". The words "SERP" and "contract's search" are not a reader's words.
7. Rewrite EVERY `basis` sentence `ceo_public_profile` writes as words a reader understands. The no-domain case, for example: "No company
   web domain is on file, so the CEO search was not run (a search outside the company's own site could find the wrong person)". Never
   write "SERP", "contract's search", a status token or a code. Keep `status`, `absence_class`, `query` and `ir_domain` as they are.
8. A SEPARATE plan, `deliverables/0.9.0_WK_AMGT_RESAPP~201/m1_ceo_basis_plan.json` (ak-6's three frozen plans are NOT touched). It
   lists every M-1 object whose newest `ceo_public_profile.basis` matches `SERP|contract's search`, with `json_path`
   `.management.ceo_public_profile.basis`, `store_field` `ceo_public_profile.basis`, and `after` computed by the FIXED producer's
   sentence for that object's case (read the case from the stored fields: `ir_domain`, `query`, url counts). An object whose case
   cannot be read from its stored fields is listed under `"unreparseable"` with its key, never hand-typed. BA_US_Equity and
   VLO_US_Equity must be entries. Print the denominator. Also REPORT, not a criterion, whether the served
   `ceo_profile_reading.reason` (built at serve time by `scoped_amgt.ceo_profile_reading`) follows the stored basis or composes its
   own text.
AC3 (section 4) grades B5. B5's served act is a later stored-field act with its own pair.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DSGN r21 3B cell B2 (issuer ruling R3: the census is the analysis's two strings). Served by ak-6 (the stored Lusha
reasons through the frozen plan; the peers code through the redeploy). The base FAILS C1 (11 of 26) and C2.

<status>pending</status>
<round>61</round>
<slot>0.9.0_WK_AMGT_RESAPP~201</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-02 ~08:5xZ):** ACCEPTED (B2 + B5). Worker ~201 commits `042ee0f7a8`, `25ac521b3d` (AMENDMENT 1), `48661ef1f5`/`78b7325369` (AMENDMENT 2); drained `5eb2a8c593`, `067df94e74`. Re-graded on the shared tree: AC1 544 passed exit=0; AC2 graded with the plan pre-write on `5eb2a8c593` (0 of 1178 stale, 0 of 26, exit=0) and without it post-write (local `067df94e74` and deployed: 0 of 26, exit=0) -- its plan-form C0 reads stale after ak-6 wrote the fields, by design (row AMGT_RESAPP-Z-S335 disarms W201-S4); AC3 YES (0 of 7 stale, 0 of 2 bases, C2 PASS). Served: B2 by ak-6 act (A) (accepted `9115f4594b`); B5 by ak-6 act (C) (AMENDMENT 2, its own pair). `ceo_profile_reading` keys its state on fields (status/query/absence_class/url) plus the SEARCH_FAILED prefix; `_SERP_URL_COUNT_RE` ("returned (\d+) url") matches the new sentences, so B5's rewrite moves basis/reason text only.

<status>complete</status>
