# AMGT_RESAPP task order -- `AMGT-am-4` -- THE REASON CLASS BESIDE EVERY PEERS ABSENT-COLUMN REASON

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-am-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~207</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code, tests and (where named) a read-only plan.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; any pool access is a read.
comp-adversary: RUN by the issuer at the cut -- r63_served --cell c4 --where deployed FAILS at the base: 0 of 12 absent entries carry reason_class, for BA and for VLO.
EGRESS CLASS, declared: NONE. No vendor or model call of any kind (no Bloomberg, Lusha, SEC, Anthropic call): stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r63-207` (branch `wk-AMGT_RESAPP-207`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there.

## 1. THE ACT -- `AMGT-am-4` (round 63, decomposition s.71)

The page must map an absent column by CLASS, not by exact text. Every `csc_columns.absent[*]` entry the peers route serves gains
`reason_class`, one of a small declared enum, for example `NOT_REPORTED`, `RATIO_ONLY`, `HORIZON_LIMIT`, `DEFINITION_MISMATCH`,
`WINDOW_LIMIT`. Name the enum in the code, and keep it to the members the twelve CSC columns actually need (issuer ruling R1):
1. ONE map `column -> reason_class` lives in `lib/research/peers/csc_plain_reasons.py`. `csc.build_csc_map` writes `reason_class` on
   every absent entry from it.
2. The peers route (`lib/research/api/scoped_amgt.py`, the peers read) fills `reason_class` from the SAME map for any stored entry
   that lacks it. The 234 stored peers objects predate the field and are NOT rewritten.
3. Tests: the producer writes it; a stored entry without it is served with it; an unknown column is served with an explicit
   `UNCLASSIFIED`, never omitted.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.**

## 2. BOUNDS

1. Write only the paths below. No deploy, NO STORE WRITE (am-6 / am-7 serve), no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/peers/
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~207/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-am-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/ lib/research/peers/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-am-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c4 --where local; echo "exit=$?"</invocation><expect>C1 PASS for BA_US_Equity and VLO_US_Equity (12 of 12 absent entries carry a reason_class); R63 C4 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~207 <0.9.0_WK_AMGT_RESAPP~207@opal.agent>" -F <msgfile> -- <paths>` (message file
written with the Write tool; confirm the commit with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~207/AMGT_RESAPP.TO-AMGT-am-4.peers-reason-class.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DSGN round-26 review. Issuer ruling R1 (a served field from one map; no stored rewrite). Served by am-6.

<status>pending</status>
<round>63</round>
<slot>0.9.0_WK_AMGT_RESAPP~207</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-02 ~15:5xZ):** ACCEPTED. Worker ~207 `b4b8ebfc4d`/`972a08bed9`, drained `e0f84f8a23`. Re-graded on the shared tree: AC1 425 passed exit=0 (api + peers); AC2 c4 YES (BA and VLO 12 of 12, classes DEFINITION_MISMATCH / HORIZON_LIMIT / NOT_REPORTED / RATIO_ONLY / WINDOW_LIMIT; UNCLASSIFIED for an unmapped column). Served by am-6.

<status>complete</status>
