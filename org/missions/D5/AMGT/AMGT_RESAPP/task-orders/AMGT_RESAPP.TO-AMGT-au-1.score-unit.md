# AMGT_RESAPP task order -- `AMGT-au-1` -- EVERY SERVED PRICE-MOVEMENT `score` CARRIES ITS UNIT (FWD-34)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-au-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~231</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- adds a constant field; reads no new store.
comp-adversary: RUN by the issuer at the cut -- r71_served c34 FAILS at the base, deployed and local: 572 of 572 objects carrying `score` carry no `score_unit`.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/r71-231` (branch `wk-AMGT_RESAPP-231`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r71-231`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-au-1` (round 71, decomposition s.79)

PRD v0.38 FWD-34 DONE WHEN (PRD `:950-961`): every price-movement figure in a served ranking or per-name response carries its unit in its
field name's `_pct` suffix; where the payload also carries a unit field (e.g. `score_unit`), it reads percent and never contradicts the
suffix; no served field leaves the unit to the page.

The price rankings already serve `score_pct` beside an unsuffixed `score` (`_serve_percent`, `lib/research/api/scoped_amgt.py` ~`:1222-1256`).
**The portal reads `row.score`** (`portal/src/.../RankedList.tsx:156-157`), so `score` is NOT renamed or removed.

1. **Add `score_unit: "percent"`** to every object that carries a price-movement `score`:
   - the rows of `/lead-panel/rankings/{trending,breakout}/price` (default window, `?days=90`, `?days=365`);
   - the points of `/lead-panel/timeseries/{trending,breakout}/price` (built ~`:1693-1704`);
   - the overlay's `price` and `breakout_price` blocks (`/security/<key>/overlay`).
   No value changes.
2. **The plant test** `lib/research/api/tests/test_score_unit.py`: a ranking row, a timeseries point and an overlay block each carry
   `score_unit == "percent"`, and `score` equals `score_pct`'s source value unchanged.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W231-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Add the field only. No served value changes; no field is removed or renamed.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~231/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-au-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_score_unit.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-au-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_served.py" --cell c34 --where local; echo "exit=$?"</invocation><expect>population reads 11 with non-200 0; C1 PASS objects failing 0; R71 C34 SERVED: YES; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~231 <0.9.0_WK_AMGT_RESAPP~231@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~231/AMGT_RESAPP.TO-AMGT-au-1.score-unit.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the functions you changed;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-70 analysis @21e6a2dc1c item 1, ruling 3; the CVO accepts either form (ADJUDICATION_v85 :74). Served by au-7.

<status>pending</status>
<round>71</round>
<slot>0.9.0_WK_AMGT_RESAPP~231</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
