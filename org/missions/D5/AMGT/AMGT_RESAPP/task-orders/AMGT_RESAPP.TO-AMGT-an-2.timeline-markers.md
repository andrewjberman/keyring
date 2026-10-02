# AMGT_RESAPP task order -- `AMGT-an-2` -- FWD-37: THE TIMELINE SERVES DATED MARKERS (COVERAGE EVENTS FROM GOLD; THE EARNINGS KIND WITH ITS REASON)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-an-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~211</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; every pool or table access is a read the function already makes.
comp-adversary: RUN by the issuer at the cut -- r64_served c11 FAILS at the base: the timeline serves no markers (BA 1 event, 0 markers).
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r64-211` (branch `wk-AMGT_RESAPP-211`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r64-211`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-an-2` (round 64, decomposition s.72; FWD-37)

PRD FWD-37 (v0.34). Issuer ruling R2, s.72.
1. **`/security/{key}/timeline`** (`lib/research/harvest/timeline_api.py` `get_timeline`, about :262; dispatched from `scoped_amgt.py`
   `_timeline_split` / `_serve_timeline`) serves `markers`: a list of `{date, kind, label}`.
   - For each event in `events` (gold `chatter_event`), one marker: `date` = the event's `first_day`, `kind` = "coverage_event",
     `label` = its `lead_headline` (empty string only when the event has none).
   - No earnings date is pulled yet (a QUALIFIED WAIT on Andrew's word: the CORPUS Model-block pull carries the dates). So serve
     `marker_kinds_absent: [{"kind": "earnings_release", "reason": "no earnings dates are pulled yet"}]`.
   - When a pulled date exists later, it becomes a marker of kind `earnings_release`; build the shape so that needs no route change.
2. `events` and `series` are unchanged. The day route is unchanged.
3. Tests: an event becomes a coverage marker with its headline; no events means no coverage markers; the earnings kind is absent with
   its reason.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W211-S<k>`, `disarm_owner`
`2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no vendor or model call, no portal write.
2. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
lib/research/harvest/timeline_api.py
lib/research/harvest/tests/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-an-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -q -p no:cacheprovider lib/research/api/tests/ lib/research/harvest/tests/; echo "exit=$?"</invocation><expect>every test passes, your new tests included, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-an-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c11 --where local; echo "exit=$?"</invocation><expect>C1 PASS for BA, AMD and VLO (markers for every event, the earnings kind absent with its reason); R64 C11 SERVED: YES -- and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~211 <0.9.0_WK_AMGT_RESAPP~211@opal.agent>" -F <msgfile> -- <paths>` (message file written
with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~211/AMGT_RESAPP.TO-AMGT-an-2.timeline-markers.proof_of_spec.json`. Report once: the commit
hash, every criterion's output lines, the functions you changed, and any row. The `<status>` flip is the issuer's.

## 6. AMENDMENT 1 (issuer `2.0.0_SA_COO~Z`, 2026-10-02 ~22:0xZ) -- the round-63 analysis @8642d76ceb

**Package watch (analysis section 3):** the artifact is at 96.8% of the 262,144,000 B ceiling. In your worktree, after your commit, run `bash infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --build-only /c/tmp/r64-pkg-<slot>.zip` and report its `SIZE:` line and `CONTENT-DIFF SUMMARY`. A build past the ceiling is a STOP: report it, and do not trim to fit.

**Publisher-terms note:** the HARVST card is open at Andrew. Add NO new processing of publisher article text. Serving what gold already holds is unchanged.

Gate limb that graded this modification: none (LIMB 6 fires only on a newly-added order; GATE (viii) does not apply, `<placeholders>NONE</placeholders>`).

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** PRD v0.34 FWD-37 (earnings path a qualified wait, v0.34). Served by an-7.

<status>pending</status>
<round>64</round>
<slot>0.9.0_WK_AMGT_RESAPP~211</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-02 ~23:3xZ):** ACCEPTED. Worker ~211 `a966df15bf`/`361859ed33`, drained `f43c05b00e`. Re-graded on the shared tree: union (peers + management + api + harvest + coverage) 1012 passed exit=0 after the drain repairs `949b24cadb` (the am-1 day-route tests) and the an-3 fake; c11 YES (BA 1 event = 1 coverage marker; the earnings kind absent with its reason on 3 of 3). AC1's 7 failures were pre-existing: 4 HARVST tests already fixed on CLOUD, and 3 am-1 day-route tests repaired at `949b24cadb` (row Z-W211-S1). Package 96.8%. Served by an-7.

<status>complete</status>
