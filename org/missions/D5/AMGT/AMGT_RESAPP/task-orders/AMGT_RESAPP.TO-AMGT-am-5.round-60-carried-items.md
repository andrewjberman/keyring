# AMGT_RESAPP task order -- `AMGT-am-5` -- ROUND-60 RULING 3'S CARRIED ITEMS: Z-S332, DEAD CHATTER INPUTS, DUPLICATE DOSSIER READS, PAGE UNIVERSES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-am-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~208</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code, tests and (where named) a read-only plan.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; any pool access is a read.
comp-adversary: RUN by the issuer at the cut -- r63_served --cell c5 --where deployed FAILS at the base: a fabricated key (ZZZZ_XX_Equity) overlay answers 200.
EGRESS CLASS, declared: NONE. No vendor or model call of any kind (no Bloomberg, Lusha, SEC, Anthropic call): stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r63-208` (branch `wk-AMGT_RESAPP-208`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there.

## 1. THE ACT -- `AMGT-am-5` (round 63, decomposition s.71)

1. **Z-S332:** `/security/<key>/overlay` answers 200 for a key that resolves to nothing (identity UNRESOLVED, no covered record).
   Answer 404 with a plain message instead. Any key the covered universe or the crosswalk knows still answers 200. Apply the same rule to
   the other `/security/<key>/...` routes only where the code shares one resolution point. Name which routes moved.
2. **Dead chatter legacy inputs:** find the inputs the chatter path still loads that no served field reads, measured by tracing what
   `read_monthly_chatter` and the lead-panel chatter routes actually use. Remove them, and name each with its file:line.
3. **Duplicate dossier reads:** find where one request reads the same `research_dossier/` object (or prefix listing) more than once.
   Read it once. Name each site.
4. **Page universes:** if collapsing the page's universes to one is portal code, do NOT edit it. File ONE row naming the page
   component, the universes it holds, and the one served universe it should read. If a served route serves more than one universe,
   fix the served part.
5. Tests for 1-3 in `lib/research/api/tests/`.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.**

## 2. BOUNDS

1. Write only the paths below. No deploy, NO STORE WRITE (am-6 / am-7 serve), no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
lib/research/coverage/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~208/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-am-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-am-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c5 --where local; echo "exit=$?"</invocation><expect>C1 PASS (a fabricated key overlay answers 404); C2 PASS (BA_US_Equity overlay answers 200); R63 C5 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~208 <0.9.0_WK_AMGT_RESAPP~208@opal.agent>" -F <msgfile> -- <paths>` (message file
written with the Write tool; confirm the commit with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~208/AMGT_RESAPP.TO-AMGT-am-5.round-60-carried-items.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round-60 ruling 3 (carried past Friday). Issuer ruling R3 (page-side is reported, not edited). Served by am-6.

<status>pending</status>
<round>63</round>
<slot>0.9.0_WK_AMGT_RESAPP~208</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-02 ~16:1xZ):** ACCEPTED. Worker ~208 `10b667f446`, drained `eb6cfa6a3e`. The union of the
drained branches failed this order's projected-read test once am-3 landed (it pinned the pre-am-3 row shape); repaired at the drain
`f80b97ca36` to assert projected == full (mutant fails). Re-graded on the shared tree: AC1 in the union run 589 passed exit=0; AC2
c5 local YES (fabricated key 404, BA 200). Rows Z-W208-S1 (page-side, reported per R3) and Z-W208-S2 (dispositioned). Served by am-6.

<status>complete</status>
