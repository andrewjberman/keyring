# AMGT_RESAPP task order -- `AMGT-ba-19` -- THE CHATTER PHASE-COVERAGE READ: EVERY COLD MILLISECOND ATTRIBUTED (CTO RULING 4, ROW Z-S360)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ba-19</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~285</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one read by hand.
comp-iam: DECLARED-NOT-APPLICABLE -- invokes and CloudWatch log reads on the deployed function, with the access round 76's az-4 used; no write.
comp-adversary: RUN by the issuer at the cut -- on deployed OVpDhfwD, cold chatter Duration reads 2,580-3,137 ms (6 cold invokes, AE~A); the in-phase sum fell to 370-613 ms while the time outside every phase line grew from 761-808 to 1,967-2,628 ms, and the phase label set changed between rounds (row Z-S360). No number says where the outside time goes.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; the deployed function's own stores only.
</preflight>

**Your worktree:** `C:/tmp/r77-285` (branch `wk-AMGT_RESAPP-285`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r77-285`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ba-19` (round 77, decomposition s.85)

CTO ruling 4 (round-76 analysis): a phase-COVERAGE read, not another latency run. The route is
`/api/scoped/amgt/lead-panel/timeseries/collected/chatter` on `opal-amgt-scoped-api` (CodeSha256 `OVpDhfwD`, memory 1769 MB).

1. **The emit map.** Read `lib/research/api/scoped_amgt.py` (`_phase_log`, the chatter route) and `lib/research/api/monthly_chatter.py`:
   list every site that emits an `AMGT_PHASE route=chatter` line at HEAD, with its file, line and label. That is the label set at
   this vintage. Name each span of the handler, from the first line of the Lambda handler to the return, that emits NO line (the
   import of the module, routing, authorisation, the response serialisation, the client and its first TLS handshake are candidates).
2. **The attribution.** Produce 3 or more COLD invokes of the route on the deployed function, with
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/leadpanel_cold_warm.py --label ba19`. For each, read its `REPORT` line (Duration, Init Duration) and its
   `AMGT_PHASE` lines from CloudWatch Logs (`/aws/lambda/opal-amgt-scoped-api`), joined PER LOG STREAM in timestamp order: the
   phase lines carry no request id. Attribute EVERY millisecond of the Duration: to a named phase, or to "outside every phase".
   The sum equals the Duration within 1 ms.
3. **Name the outside time.** A deployed log line cannot split it, so profile the SAME handler locally in a FRESH process
   (`deliverables/.../profile_chatter.py`, your file): time each unlabelled span from step 1 with `time.perf_counter` around the
   handler's own calls, WITHOUT editing any file under `lib/`. State which spans hold the outside time locally, and say plainly
   that the local split is an inference about the deployed one.
4. **The free cuts.** List each cut that needs no spend (what, where, the estimated ms), or state that they are exhausted and give
   the measured residual.
5. **The inputs for Andrew's card, as numbers only.** One provisioned instance at 1769 MB: the price per GB-second you used and
   where you read it (a file in this repository or a public price you name as UNVERIFIED-HERE if you cannot read it offline),
   730 hours a month, and the monthly figure by that arithmetic. No recommendation: the CTO writes the card.

Write `PHASE_COVERAGE.md` (the tables, in plain words) and `PHASE_COVERAGE.json` in the shape the check's docstring gives, both in
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~285/`.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W285-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. A read. No file under `lib/`, `infra/` or `portal/` changes. No deploy, no configuration change on the function, no store write.
2. The burst script is the only source of invokes; do not loop it more than 3 times.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~285/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ba-19"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba19.py" --cell coverage; echo "exit=$?"</invocation><expect>3 or more cold invokes, each attributed to the millisecond; a closed label set with real emit sites; the free cuts listed or stated exhausted; R77 BA19 COVERAGE: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ba-19"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round77/checks/r77_ba19.py" --cell inputs; echo "exit=$?"</invocation><expect>1769 MB, one instance, a sourced price and the monthly figure by the stated arithmetic; R77 BA19 INPUTS: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~285 <0.9.0_WK_AMGT_RESAPP~285@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~285/AMGT_RESAPP.TO-AMGT-ba-19.chatter-phase-coverage-read.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the attribution table (per cold invoke: Init, Duration, each phase, outside);
- the unlabelled spans and their local times;
- the free cuts, or the residual;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-76 analysis @c8bbeeac10 ruling 4, enrichment item 3. Wave 0, its own chain (it writes no shared file).
Checks dry-run at the base: ba-19 AC1 base FAIL as expected (no coverage file); AC2 base FAIL as expected. Provisioned concurrency
goes to Andrew only after this read, on the CTO's card.

<status>pending</status>
<round>77</round>
<slot>0.9.0_WK_AMGT_RESAPP~285</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
