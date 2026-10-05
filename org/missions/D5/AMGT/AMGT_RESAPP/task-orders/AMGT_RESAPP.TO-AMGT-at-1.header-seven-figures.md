# AMGT_RESAPP task order -- `AMGT-at-1` -- THE HEADER'S SEVEN FIGURES ON EVERY COVERED NAME, OR A PLAIN REASON PER MISSING ONE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-at-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~226</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only stores the function already reads; no write. A read of a NEW S3 path is named in your report (the redeploy cell simulates it).
comp-adversary: RUN by the issuer at the cut -- r70_served c30 FAILS at the base on deployed: 43 of 95 headers miss a figure with no reason (short interest on HK/JP names; enterprise value on some).
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only. A figure or leg that needs a NEW vendor pull is served with a plain reason and filed as a row for Andrew's act, never pulled.
</preflight>

**Your worktree:** `C:/tmp/r70-226` (branch `wk-AMGT_RESAPP-226`, cut from the issuance commit with `--portal-ref 6936e92b`). Work
and commit only there. Start every shell call with `cd /c/tmp/r70-226`: a call that starts elsewhere resolves `git rev-parse
--show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-at-1` (round 70, decomposition s.78; CTO round-69 analysis item 1; DSGN FWD-4)

The header block (`header_figures`, served on `/security/<key>/thesis` and `/overlay` from the same builder in
`lib/research/api/scoped_amgt.py`) must cover seven figures on every covered name. They are price (`PX_LAST`), market cap
(`CUR_MKT_CAP`), enterprise value (`CURR_ENTP_VAL`), net debt (`NET_DEBT`), beta (`EQY_BETA`), average volume (`VOLUME_AVG_30D`) and short
interest (`SHORT_INT_RATIO` or `SI_PERCENT_EQUITY_FLOAT`).

1. **Serve the stored value when one exists.** Use only the stores already read: the Bloomberg header object it reads today, and any
   other stored source it already reads for these fields.
2. **When no stored value exists,** serve an entry for that figure with `value: null` and a non-empty plain `reason`. Say why it is
   missing, for example "Bloomberg does not report short interest for this listing" or "not in the latest stored pull".
   - Never fabricate a figure.
   - If a figure could be filled only by a NEW vendor pull, serve the reason and file ONE row listing those names and fields for
     Andrew's act.
3. **The plant test** `lib/research/api/tests/test_header_seven.py`. A name missing some of the seven serves a reasoned null entry for
   each missing one; a name with all seven is unchanged.

Run `lib/research/api/tests/` before your commit and report its last line. **Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W226-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`. If one api test fails only because it
reads a portal function absent at this worktree's portal ref (`test_model_words.py`), name it in your report and file no row; the issuer
grades the suite on the shared tree.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. Add reasoned entries only. No served figure VALUE changes, and no existing entry is removed or renamed.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block,
   estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~226/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-at-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_header_seven.py; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-at-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round70/checks/r70_served.py" --cell c30 --where local; echo "exit=$?"</invocation><expect>population names 95 with 0 non-200; C1 PASS 0 names failing; R70 C30 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-at-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round68/checks/r68_served.py" --cell c28 --where local; echo "exit=$?"</invocation><expect>R68 C28 SERVED: YES (plain words hold); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~226 <0.9.0_WK_AMGT_RESAPP~226@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~226/AMGT_RESAPP.TO-AMGT-at-1.header-seven-figures.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the functions you changed;
- any new S3 read path;
- any row, including any vendor leg listed for Andrew.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-69 analysis @0bdf5b47ae item 1 and rulings 1-2; routed from DSGN_AMGTV1 FWD-4. Served by at-6.

<status>pending</status>
<round>70</round>
<slot>0.9.0_WK_AMGT_RESAPP~226</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
