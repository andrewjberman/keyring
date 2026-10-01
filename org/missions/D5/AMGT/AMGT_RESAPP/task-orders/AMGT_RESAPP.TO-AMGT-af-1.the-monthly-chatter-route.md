# AMGT_RESAPP task order -- `AMGT-af-1` -- THE MONTHLY CHATTER ROUTE (FWD-32, the Friday bubble chart's dependency)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-af-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~197</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a read route.
comp-iam: RUN by the issuer at the cut -- the scoped API role already reads gold chatter_daily and article_security_mention (infra/aws/terraform/harvest/scoped-amgt-api.tf:203-205) and lists research_dossier/ (:213-226). No grant is added.
comp-adversary: RUN by the issuer at the cut -- AC2 FAILS at the base (400 refused at C1); PASSES on a simulated post-state built from the gold snapshots; FAILS on a planted zero month cell (C5) and on 51 of 95 rows (C2).
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/r56-197` (branch `wk-AMGT_RESAPP-197`, cut from the issuance commit). Work and commit only there.

## 1. THE ACT -- `AMGT-af-1` (round 56, decomposition s.64)

Serve `GET /api/scoped/amgt/lead-panel/timeseries/collected/chatter`. The template `timeseries/{movement}/{subject}` is already
mounted (18 routes); today `movement=collected` is refused 400 by `movement_gate.normalise_movement`. Do NOT add a movement to
`movement_gate` (COLLECTED is not a ranking axis) and do NOT add a route or touch terraform.

1. **New module** `lib/research/api/monthly_chatter.py`, one public function `read_monthly_chatter() -> dict`:
   - Universe: `lib.research.coverage.covered_universe.covered_security_keys()` (fresh, 95 at the cut; never pinned).
   - Collected: the newest gold `chatter_daily` snapshot via `lib.research.coverage.pool_reader._gold_latest_snapshot_rows("chatter_daily")`
     (one object = the full window, 2026-01-01..as_of). Per name per calendar month (`day[:7]`): `collected` = sum of `articles_total`.
   - By publisher: the newest gold `article_security_mention` snapshot through the same function; de-duplicate on
     (`article_key`, `security_key`); count per `publisher` per month of `published_utc`; only months inside the `chatter_daily` window.
   - `as_of` = the newest `day` in the `chatter_daily` snapshot; `months` = every calendar month from the window's first month to the
     `as_of` month, ascending; `partial_months` = `[as_of month]` unless `as_of` is that month's last day.
   - Response (the shared CONTRACT section 1 shape):
     `{"as_of", "source": "harvest gold chatter_daily", "months", "partial_months", "rows": [{"security_key", "display_name", "by_month": {"YYYY-MM": {"collected": n, "by_publisher": {"sa": n, "wsj": n, "bbg": n, "ft": n, "barrons": n}}}}]}`
     plus `"vintage"`: the S3 keys of the two snapshot objects read.
   - **One row for EVERY covered name.** A month in which nothing was collected for a name is ABSENT from its `by_month`, never a zero
     cell (CTO ruling msg 27527; CONTRACT s.1). A covered name with nothing collected at all has `by_month: {}`.
   - `display_name`: the name the existing ranking rows use (`_fill_names_from_crosswalk` in `scoped_amgt.py`, or the crosswalk it calls);
     the security key when none resolves. No coverage gate of any kind.
2. **Dispatch** in `lib/research/api/scoped_amgt.py` `handler()`, the timeseries block only (`:4460-4468` at the cut): when `rest[2]`
   (case-insensitive) is `collected` and `rest[3]` is `chatter`, return `_response(200, monthly_chatter.read_monthly_chatter())` BEFORE
   `read_rank_series`. `collected` with any other subject stays a 400 refusal with a reason. Touch no other function in `scoped_amgt.py`
   (a sibling cell, af-2, edits its read functions in parallel).
3. **Test** `lib/research/api/tests/test_monthly_chatter.py`: stub both snapshots; prove the absent-month rule, the every-covered-name
   rule, the publisher de-duplication, `partial_months`, and the `collected/price` refusal.

**Measured at the cut:** 51 of 95 covered names appear in `chatter_daily`, 23 in the mention table; on every 2026 name-month with
collected > 0 the two agree (147 of 147). `BA_US_Equity` September = 20. If the route's per-publisher sum ever differs from `collected`
on a 2026 month, report it as a ROW; do not reconcile it in code.

## 2. BOUNDS

1. Write only the paths below. No terraform, no gateway, no deploy (af-5 deploys), no S3 write, no vendor call, no `movement_gate` edit.
2. Standing: no S3 delete, no push of shared branches, no portal change.

## 3. SURFACES

<paths>
lib/research/api/monthly_chatter.py
lib/research/api/scoped_amgt.py
lib/research/api/tests/test_monthly_chatter.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~197/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-af-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/; echo "exit=$?"</invocation><expect>every test passes, test_monthly_chatter.py included (314 passed at the cut, before the new file), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-af-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round56/checks/af_1_route.py; echo "exit=$?"</invocation><expect>C1-C8 PASS; THE MONTHLY CHATTER ROUTE SERVES EVERY COVERED NAME FROM GOLD: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~197 <0.9.0_WK_AMGT_RESAPP~197@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~197/AMGT_RESAPP.TO-AMGT-af-1.the-monthly-chatter-route.proof_of_spec.json`.
Report once: the commit hash, both criteria's output lines, the response's row count and as_of, and any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** addendum D FWD-32; placement s.3 (cut FIRST). The route is served only after af-5's redeploy; this order's AC2 is the
local handler run against live gold. Base: AC2 FAIL at C1 (400). Positive arm: PASS on a body built from the snapshots; negatives: a
zero month cell FAILS C5, 51 rows FAILS C2.

<status>pending</status>
<round>56</round>
<slot>0.9.0_WK_AMGT_RESAPP~197</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-01 ~06:2xZ):** AC2 YES (worker ~197, 45e4ac9009/8b16478c44); AC1 graded by the issuer on the full tree after the drains (CLOUD 78167bb8fc): 342 passed, exit=0 -- row Z-S327 resolves W197-S1. Drained cb1f56de68. Served only after round 57's redeploy.

<status>complete</status>
