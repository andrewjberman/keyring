# AMGT_RESAPP task order -- `AMGT-am-2` -- FWD-7: THE BLOOMBERG OFFICER FALLBACK FOR ASML_NA, AND MANAGEMENT OBJECTS FOR 6501_JP AND 2317_TT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-am-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~205</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code, tests and (where named) a read-only plan.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; any pool access is a read.
comp-adversary: RUN by the issuer at the cut -- r63_served --cell c2 --where deployed FAILS at the base: ASML_NA ABSENT/ZERO_OFFICERS; 6501_JP and 2317_TT NO_OBJECT.
EGRESS CLASS, declared: NONE. No vendor or model call of any kind (no Bloomberg, Lusha, SEC, Anthropic call): stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r63-205` (branch `wk-AMGT_RESAPP-205`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there.

## 1. THE ACT -- `AMGT-am-2` (round 63, decomposition s.71)

Served management is read from STORED M-1 objects (`management/v1/<key>/<as_of>.json`, the newest per key, by
`scoped_amgt.read_management`). 6861_JP_Equity and CSL_AU_Equity serve `roster_source` BLOOMBERG_FALLBACK when no filing roster
resolves. Find that producer path in `lib/research/management/`, and the stored Bloomberg officer input it reads (for example the
harvest bronze `exec_officers` table). Then:
1. **ASML_NA_Equity:** its 20-F's officer section is EMPTY, so it takes the same Bloomberg fallback, with its source named as for
   6861_JP. If the producer's rule excludes a 20-F filer from the fallback, fix that rule rather than special-casing ASML.
2. **6501_JP_Equity, 2317_TT_Equity:** produce a management object for each through the same producer: officers if the stored
   Bloomberg input has them, otherwise an object with a plain `roster_reason` that says why none is served.
3. **The plan, read-only.** Write the produced objects to a LOCAL pool directory
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~205/m1_pool/management/v1/<key>/2026-10-02.json`, plus
   `m1_fwd7_plan.json`: `{"entries": [{"security_key", "store_key": "management/v1/<key>/2026-10-02.json", "exists_now": bool, "sha256": <of the object bytes>}]}`.
   The plan's keys are NEW keys dated 2026-10-02: the route reads the newest object, so nothing existing is overwritten.
4. Tests in `lib/research/management/tests/`.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.**

## 2. BOUNDS

1. Write only the paths below. No deploy, NO STORE WRITE (am-6 / am-7 serve), no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~205/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-am-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/management/tests/ lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-am-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c2 --where local --pool org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~205/m1_pool; echo "exit=$?"</invocation><expect>C1 PASS (ASML_NA SERVED, BLOOMBERG_FALLBACK, officers > 0); C2 PASS for 6501_JP and 2317_TT (officers, or a stated reason); R63 C2 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~205 <0.9.0_WK_AMGT_RESAPP~205@opal.agent>" -F <msgfile> -- <paths>` (message file
written with the Write tool; confirm the commit with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~205/AMGT_RESAPP.TO-AMGT-am-2.officer-fallback-and-management-objects.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DSGN COMPLETION_GRADES.round26 @0c4c6d6368 (FWD-7 NOT_REALIZED). Served by am-7 (stored write of the frozen plan).

<status>pending</status>
<round>63</round>
<slot>0.9.0_WK_AMGT_RESAPP~205</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
