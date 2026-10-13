# ADVI_FIRMBKTS task order -- `FB-h-8` -- THE FENCE-SCOPED-ROWS INSTRUMENT READS ok=True AGAIN: EXPLICIT UTF-8 AND THE OBJECT SHAPE FIXTURE (TEST-ONLY)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R5.md</decomp_doc>
<owned_cells>FB-h-8</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~FB1</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a test instrument; no cron, rule, schedule or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- the instrument's own `sts get-caller-identity` and `iam simulate-custom-policy` reads, as it already makes; no grant. A simulator denial is reported, never stubbed.
comp-adversary: RUN by the issuer -- at the base AC1 reads ok=False (and the cp1252 error without the environment variable); AC2 passes at the base only if the files are already ASCII (control). Blindness: the instrument proves the renderer on scratch copies and the simulator arms, not an applied policy.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-h-8` (round 5, enrichment item 7; row `D1-S28`; the CTO's msg 4653)

`infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py` is the instrument that proves the scoped-exemption renderer
and its fail-closed readers on scratch copies. It does not read `ok=True` at HEAD. Reproduced by `0.0.0_AB_MSTR` (msg 4652):

1. On a Windows default code page it raises `UnicodeEncodeError` (cp1252) at `out()` (line 89), because a message it prints
   carries a character the code page cannot encode.
2. With `PYTHONIOENCODING=utf-8` set, the `before_strip` step fails at init in `one(list)`: `local.lgic_managed_firm_buckets`
   is now an OBJECT in the fence file, not a list, so the single-element reader fails; the run ends `ok=False` with
   `refusals_ok=0/7`.

Fix the instrument, test-only, no served change:

### 1a. The edits (files under `infra/aws/terraform/shared-infra/tests/` only)

1. Every reader and writer of text in the check, and in the files under `tests/` it imports, passes an explicit
   `encoding="utf-8"` (open, `read_text`, `write_text`, `subprocess.run(..., text=True)` with `encoding=`), and every line the
   check PRINTS is ASCII (per the repository's non-ASCII law: `OK:`/`WARN:`/`ERROR:`; replace the offending character in the
   message, do not set an environment variable).
2. `before_strip` reads `local.lgic_managed_firm_buckets` in both shapes (the list it was and the object it is), through the
   fence file's own text, never a typed value; and the check carries a FIXTURE of the object shape under `tests/` (a scratch
   copy of the fence block) so the init shape is exercised by the run, not only by the live file.
3. Close: `FENCE-SCOPED ... refusals_ok=7/7 ... ok=True` at the HEAD of the tree you commit in, with NO environment override
   (AC1 runs with `PYTHONIOENCODING` and `PYTHONUTF8` unset).

### 1b. Rules

1. Do not weaken the instrument to reach `ok=True`: the seven refusal cases, the unknown-key refusal by BOTH the validator and the
   module, the simulator arms and the `unchanged_today` comparison keep their meaning. A change to what an arm asserts is a
   BLOCKING row to the issuer, not an edit.
2. The simulator arms call `iam simulate-custom-policy`. If that call is denied to your identity, `sim_ok` cannot read; file a
   surprise row naming the denied call and the arms it blocks, leave AC1 failing, and report: the issuer routes the simulator
   arms to the laptop lane. Do not stub the simulator.
3. No AWS write, no Terraform apply, no change to a `.tf` file or to the registry.

## 2. BOUNDS

1. One commit of the files under `infra/aws/terraform/shared-infra/tests/` and your deliverables folder; no deploy, no push beyond
   the usual integration.
2. If the check fails for a reason other than the two named, STOP before editing and file a BLOCKING row naming the failing arm.

## 3. SURFACES

<paths>
infra/aws/terraform/shared-infra/tests/
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/ADVI_FIRMBKTS.TO-FB-h-8.fence-instrument-utf8-fixture.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-h-8"><invocation>cd C:/dev/ajb_workspace &amp;&amp; env -u PYTHONIOENCODING -u PYTHONUTF8 timeout 118 python infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py 2&gt;&amp;1 | tail -1</invocation><expect>^FENCE-SCOPED rows_today=[0-9]+ unchanged_today=True scoped_rendered=[0-9]+/[0-9]+ sim_ok=[0-9]+/[0-9]+ refusals_ok=7/7 unknown_key_refused_by=validator\+module ok=True$</expect></criterion>
  <criterion id="AC2" cell_refs="FB-h-8"><invocation>cd C:/dev/ajb_workspace &amp;&amp; timeout 60 python -c "import sys,glob;bad=[p for p in glob.glob('infra/aws/terraform/shared-infra/tests/check_fence_scoped_rows.py')+glob.glob('infra/aws/terraform/shared-infra/tests/derive_fence_row_shape.py') if any(ord(c)&gt;127 for c in open(p,encoding='utf-8').read())];print('NONASCII-FILES',len(bad))"</invocation><expect>^NONASCII-FILES 0$</expect></criterion>
</proof_of_spec>

AC1 is the instrument's own last line at HEAD with no environment override; AC2 the ASCII bound on the two instrument files.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/round5/ADVI_FIRMBKTS.TO-FB-h-8.fence-instrument-utf8-fixture.proof_of_spec.json`. Commit the edits FIRST, your rows and the instance second; flip `<status>` to `complete` in the SAME commit only when AC1 and AC2 pass. Report once to `2.0.0_SA_COO~B1`: the AC1 last line, the files changed and the FULL commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO msg 4653 (round 5 item 7): MSTR msg 4652 reproduced it; the file is lane CLOUD_OPS_OR_ETL, so the CTO orders it to FB1. D1-S28 is the CVO's ROUTED row (round-4 analysis section 2: "every reader and writer becomes explicit encoding utf-8 per the non-ASCII law, and the init failure gets a scratch-root fixture; close ok=True at HEAD with no environment override"). Class WORLD by the path floor (an infrastructure path); test-only. Risk the issuer names: the simulator arms may be denied to the dell1 identity (the round-4 close recorded IAM simulate refused on dell1); the order says what to do and does not let the seat weaken the instrument.

<status>pending</status>
<round>5</round>
<workstream>FENCEINSTR</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-h-8</to_id>
<slot>~FB1</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
