# AMGT_RESAPP task order -- `AMGT-an-6` -- REPAIRS: THE SLASH-TICKER CLASSIFICATION (Z-S339), THE OFFICER FACE'S READER WORDS, object_as_of

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-an-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~215</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; every pool or table access is a read the function already makes.
comp-adversary: RUN by the issuer at the cut -- r64_served c14 FAILS at the base: BP/NG untrue reason; ASML source_item/pool_read.reason/fallback.label carry COMPANY_EXEC_OFFICERS/ABSENT/RESOLVED; object_as_of absent 3 of 3.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r64-215` (branch `wk-AMGT_RESAPP-215`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r64-215`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-an-6` (round 64, decomposition s.72; repairs)

Issuer ruling R4, s.72: three repairs batched into one cell.
1. **Z-S339.** `_classification_for_ticker` (`scoped_amgt.py` about :617, bare = first space-separated token) asks etf-classifications for
   'BP/' and 'NG/'. The table holds 'BP' (BP PLC, equity, Energy) and 'NG' (name null, equity, Utilities).
   - Resolve a trailing-slash ticker to its slash-free form ONLY when the table's row is confirmed as the same company: its `name`
     matches the security's crosswalk or model-block name, case- and punctuation-insensitive. The bare key collapses exchanges (NG US is
     a different company).
   - Otherwise serve `sector` null with a TRUE reason, e.g. "the classification row for NG cannot be confirmed as this company". Never
     serve "holds no classification" when it holds one.
2. **The officer face** (CTO msg 28730). The served reader text carries raw codes. Serve reader words at serve time from one map, so
   stored objects need no rewrite:
   - `management.source_item` "Bloomberg COMPANY_EXEC_OFFICERS (fallback: no RESOLVED filing roster)" becomes, e.g., "Bloomberg officer
     list (no filing roster could be read)";
   - `management.pool_read.reason` "... are ABSENT" becomes, e.g., "tenure is not served: Bloomberg's officer list carries no role start";
   - `management.fallback.label` likewise.
   - Machine fields (`roster_source`, `fallback.field`, `*_status`, `role_start_basis`) keep their values.
3. **object_as_of.** The management route serves `object_as_of` = the served object key's as_of (e.g. `2026-10-02T1840Z`) beside the
   body's date `as_of`. Two objects for one name on one day are then told apart (6501_JP and 2317_TT tie today).
4. Tests for all three.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W215-S<k>`, `disarm_owner`
`2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-an-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-an-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c14 --where local; echo "exit=$?"</invocation><expect>C1 PASS for BP/_LN and NG/_LN (sector resolved with its source, or a true reason); C2 PASS (no raw code in ASML_NA's reader text); C3 PASS for ASML_NA, 6501_JP and 2317_TT (object_as_of 2026-10-02T1840Z); R64 C14 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~215 <0.9.0_WK_AMGT_RESAPP~215@opal.agent>" -F <msgfile> -- <paths>` (message file written
with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~215/AMGT_RESAPP.TO-AMGT-an-6.repairs.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Rows Z-S339; CTO msg 28730 (officer face); am-7 A3 close (as_of tie). Served by an-7.

<status>pending</status>
<round>64</round>
<slot>0.9.0_WK_AMGT_RESAPP~215</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
