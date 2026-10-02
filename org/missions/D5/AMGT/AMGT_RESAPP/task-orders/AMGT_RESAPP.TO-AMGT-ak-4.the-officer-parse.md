# AMGT_RESAPP task order -- `AMGT-ak-4` -- THE M-1 OFFICER PARSE: THE FULL TITLE, AND NO TRAILING AGE IN THE ROLE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ak-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~202</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; parser code and a read-only plan.
comp-iam: DECLARED-NOT-APPLICABLE -- the plan builder only READS the pool (the stored M-1 objects and their stored filing sources).
comp-adversary: RUN by the issuer at the cut -- AC2 FAILS at the base: C1 VLO's second officer is named "Senior Vice" (role "President and Chief Financial Officer 45"); C2 5 of 5 VLO roles end in an age; C3 PASSES (BA 12 officers).
EGRESS CLASS, declared: NONE. No SEC/EDGAR fetch, no vendor call: re-parse the STORED filing source only.
</preflight>

**Your worktree:** `C:/tmp/r61-202` (branch `wk-AMGT_RESAPP-202`, cut from the issuance commit; full checkout). Work and commit only there.

## 1. THE ACT -- `AMGT-ak-4` (round 61, decomposition s.69; DSGN round-21 analysis section 3B cell B3)

VLO_US_Equity's served officers (`thesis.management.officers`, STORED in its M-1 object `management/v1/<key>/<as_of>.json`, roster
source FILING) read today:
- `R. Lane Riggs` | `Chairman of the Board, Chief Executive Officer and President 60`
- `Senior Vice` | `President and Chief Financial Officer 45`  <- the CFO's name is lost; "Senior Vice" is the start of the title
- `Gary K. Simmons` | `Executive Vice President and Chief Operating Officer 61`
- `Richard J. Walsh` | `Executive Vice President and General Counsel 60`
- `Eric A. Fisher` | `Senior Vice President Product Supply, Trading and Wholesale 57`

1. **Find the parser** in `lib/research/management/` that builds the FILING roster (name / age / position columns of the filing's
   executive-officer table), and fix it so that a name is a person's name, the role is the full title, and an age column is never
   appended to the role. If the filing's own age is useful, carry it in its own field, never in `role`. Do not change how any other
   name's roster parses except where the same defect applies: BA_US_Equity's 12 officers must read exactly as they do today.
2. **The rewrite plan for the STORED officers.** Re-parse the STORED filing source each affected M-1 object names (read it from the
   pool; never fetch it), with the fixed parser. Census every M-1 object for the same two defects (a name made only of title words; a
   role ending in a number) and print that denominator. Emit
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~202/m1_officer_plan.json`:
   `{"denominator": <M-1 objects scanned>, "defective": <objects with either defect>, "entries": [{"security_key", "route": "thesis", "json_path": ".management.officers", "store_key": "<the exact pool key>", "store_field": "officers", "before": <the stored officers list>, "after": <the re-parsed officers list>}]}`.
   VLO_US_Equity must be an entry. An object whose stored filing source is absent is listed under `"unreparseable"` with its key,
   never patched by hand. The builder WRITES NOTHING to the pool.
3. **Tests** in `lib/research/management/tests/`: a fixture shaped like VLO's table (name, age, position) parses to full names and
   titles with no age in the role; BA's shape is unchanged.

## 2. BOUNDS

1. Write only the paths below. No deploy, NO STORE WRITE (ak-6 writes), no vendor call, no portal write. Officer fields only.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/management/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~202/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ak-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/management/tests/ lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ak-4"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round61/checks/b_served_text.py --cell b3 --where local --plan org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~202/m1_officer_plan.json; echo "exit=$?"</invocation><expect>C0 PASS (every plan entry's before equals what the route serves now), C1 PASS (VLO's officers carry person names, none a bare title), C2 PASS (0 VLO roles end in an age), C3 PASS (BA 12); B3 EVERY OFFICER CARRIES A FULL TITLE AND NO AGE: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~202 <0.9.0_WK_AMGT_RESAPP~202@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~202/AMGT_RESAPP.TO-AMGT-ak-4.the-officer-parse.proof_of_spec.json`.
Report once: the commit hash, both criteria's output lines, the parser function you changed, VLO's re-parsed officers, the census
(denominator, defective, unreparseable), and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** DSGN r21 3B cell B3. Served by ak-6 through the frozen plan. The base FAILS C1 and C2; C3 is the regression guard.

<status>pending</status>
<round>61</round>
<slot>0.9.0_WK_AMGT_RESAPP~202</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
