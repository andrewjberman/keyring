# AMGT_RESAPP task order -- `AMGT-am-1` -- TRACK C STEP 2: THE DAY ROUTE READS THE HEADLINE FROM GOLD

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-am-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~204</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code, tests and (where named) a read-only plan.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; any pool access is a read.
comp-adversary: RUN by the issuer at the cut -- r63_served --cell c1 --where local (the silver read planted to RAISE) FAILS at the base: 502, because gold carries no title yet.
EGRESS CLASS, declared: NONE. No vendor or model call of any kind (no Bloomberg, Lusha, SEC, Anthropic call): stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r63-204` (branch `wk-AMGT_RESAPP-204`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there.

## 1. THE ACT -- `AMGT-am-1` (round 63, decomposition s.71)

**BEGIN ONLY WHEN** the newest gold `article_security_mention` snapshot (read it through
`lib/research/coverage/pool_reader._gold_latest_snapshot_rows("article_security_mention")`) carries a `title` column. That is HARVST's
step 1 (order HVST-aj-7) plus gold rebuild #5. Until then, report "WAITING: gold has no title" and stop. This is not a failure.

`lib/research/api/scoped_amgt.py` `_timeline_article_loader` joins each mention to its silver article for `headline` and
`published_precision`. Serve both from the GOLD mention row's own `title` and `published_precision` instead. Then remove the
request-time silver read: `_timeline_silver_articles`, `_timeline_silver_within_deadline`, the 18 s deadline, the worker pool and the
`headline_reason` path (AMGT-al-2), together with their tests. Rewrite `test_timeline_silver_deadline.py` into a gold-sourced test:
- a gold row with a title serves it;
- a gold row without one serves `headline` null and no reason;
- NO silver read occurs (plant the silver reader to raise).
A gold row whose `title` is null keeps `headline` null. Never fall back to a silver read.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.**

## 2. BOUNDS

1. Write only the paths below. No deploy, NO STORE WRITE (am-6 / am-7 serve), no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~204/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-am-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-am-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round63/checks/r63_served.py --cell c1 --where local; echo "exit=$?"</invocation><expect>C1 PASS (BA Sept 8 serves 5 of 5 headlines from gold, no headline_reason, with the silver reader planted to RAISE); R63 C1 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~204 <0.9.0_WK_AMGT_RESAPP~204@opal.agent>" -F <msgfile> -- <paths>` (message file
written with the Write tool; confirm the commit with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~204/AMGT_RESAPP.TO-AMGT-am-1.headline-from-gold.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO track C ruling (A) step 2, @40e1d622aa / @0ce76710dc. Begin-condition R2. Served by am-6, with memory re-measured down there.

<status>pending</status>
<round>63</round>
<slot>0.9.0_WK_AMGT_RESAPP~204</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
