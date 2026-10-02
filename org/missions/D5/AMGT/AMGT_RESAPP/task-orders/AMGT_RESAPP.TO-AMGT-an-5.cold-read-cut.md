# AMGT_RESAPP task order -- `AMGT-an-5` -- THE COLD READ: COLUMN PROJECTION + SECURITY FILTER ON BOTH GOLD READS, WITH SEGMENT TIMINGS (c1 vs 5 s)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-an-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~214</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; every pool or table access is a read the function already makes.
comp-adversary: RUN by the issuer at the cut -- r63_served c1 deployed: cold 11.5-12.8 s at 1769/3538/10240 (round 63, ruled NOT MET); local cold profile 3.55 of 4.4 s in two whole gold reads.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r64-214` (branch `wk-AMGT_RESAPP-214`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r64-214`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-an-5` (round 64, decomposition s.72; c1, track C)

CTO ruling 3 of the round-63 leg-2 addendum @4d0f049203. A cold BA `/timeline/day/2026-09-08` took 11.5-12.8 s at every memory (the curve
is flat, so the cost is not CPU). A local cold profile spends 3.55 s of 4.4 s on two WHOLE gold snapshot reads for one security-day:
`chatter_daily` (58,300 rows) and `article_security_mention` (23,691 rows).
1. **Both reads** (`publication_gold._latest_gold_snapshot_rows_cached` and the timeline loaders in `scoped_amgt.py` about :4784-4809)
   read only the columns the route serves, plus a security filter: pyarrow row-group statistics or `filters=`, or an index keyed by
   security if the snapshot's layout allows it. Measure which works on the real snapshot and say so.
   - Every other caller keeps today's bytes. The served bytes of the day route and its controls are unchanged.
2. **Segment timings.** The handler logs one line per stage, `AMGT_SEGMENT <stage>=<ms>` (import, each gold read, assembly), so the
   deployed grade can see where a cold request spends its time.
3. Report the local cold profile (a fresh process, first call) before and after, per stage.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W214-S<k>`, `disarm_owner`
`2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/harvest/
lib/research/api/
lib/research/coverage/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-an-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/ lib/research/harvest/tests/ lib/research/coverage/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-an-5"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c1 --where local; echo "exit=$?"</invocation><expect>C1 PASS (BA Sept 8 serves every headline from gold, no reason, with the silver reader planted to raise); R63 C1 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~214 <0.9.0_WK_AMGT_RESAPP~214@opal.agent>" -F <msgfile> -- <paths>` (message file written
with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~214/AMGT_RESAPP.TO-AMGT-an-5.cold-read-cut.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

## 6. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~22:0xZ) -- the round-63 analysis @8642d76ceb

**Package watch (analysis section 3):** the artifact is at 96.8% of the 262,144,000 B ceiling. In your worktree, after your commit, run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only /c/tmp/r64-pkg-<slot>.zip` and report its `SIZE:` line and `CONTENT-DIFF SUMMARY`. A build past the ceiling is a STOP: report it, and do not trim to fit.

**Publisher-terms note:** the HARVST card is open at Andrew. Add NO new processing of publisher article text. Serving what gold already holds is unchanged.

Gate limb that graded this modification: none (LIMB 6 fires only on a newly-added order; GATE (viii) does not apply, `<placeholders>NONE</placeholders>`).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO ruling 3 @4d0f049203 (re-graded at an-7 against the same 5 s cold bound, Init Duration proven); package at 96.8% of the ceiling: measure the build size at cut. Served by an-7.

<status>pending</status>
<round>64</round>
<slot>0.9.0_WK_AMGT_RESAPP~214</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
