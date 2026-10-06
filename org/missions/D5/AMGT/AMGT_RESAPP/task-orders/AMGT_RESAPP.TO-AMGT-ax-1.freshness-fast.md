# AMGT_RESAPP task order -- `AMGT-ax-1` -- /freshness ANSWERS WARM UNDER 2 SECONDS, VALUES EQUAL (CTO RULING 3a)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ax-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~252</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- the same stores the route already reads.
comp-adversary: RUN by the issuer at the cut -- r74 c53 FAILS: /freshness warm 10.7-11.3 s deployed, 20.6-23.6 s local (aw-3 made it read ~105 pack ledgers per request).
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r74-252` (branch `wk-AMGT_RESAPP-252`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r74-252`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ax-1` (round 74, decomposition s.82)

Row Z-S356; CTO ruling 3a. `read_coverage_freshness` (`lib/research/api/scoped_amgt.py` ~`:5027-5108` plus aw-3's pack clock)
reads each stored pack ledger, per name, on every request.
1. **Make the warm read fast.** Either use `lib/research/api/served_cache.py` (version-keyed on the packs listing, or a short TTL like
   au-6's 60 s pointer), or read the dates from the listing's LastModified and the ledgers 16-wide only on a miss. Choose what keeps
   every value EQUAL.
2. **Values equal.** Before any edit, capture `/freshness`'s body into `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~252/before.json`. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~252/after_equal.py`,
   which compares every row (ignoring `generated_at` and any per-request timing field) and prints `EQUAL n of n rows`.
3. **The plant test** `lib/research/api/tests/test_freshness_fast.py`.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W252-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. No served value changes (AC2).
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~252/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ax-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round74/checks/r74_served.py" --cell c53 --where local; echo "exit=$?"</invocation><expect>/freshness warm worst under 2000 ms with status [200] and covered rows 95; C1 PASS; R74 C53 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ax-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~252/after_equal.py"; echo "exit=$?"</invocation><expect>EQUAL n of n rows with n the rows served (292 at the cut); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~252 <0.9.0_WK_AMGT_RESAPP~252@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~252/AMGT_RESAPP.TO-AMGT-ax-1.freshness-fast.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the cache key or method chosen;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-73 analysis item 1, ruling 3a; row Z-S356. Served by ax-5.

<status>pending</status>
<round>74</round>
<slot>0.9.0_WK_AMGT_RESAPP~252</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
