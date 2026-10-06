# AMGT_RESAPP task order -- `AMGT-aw-2` -- THE PRINT LAID OUT AS A DOCUMENT (FWD-5, CTO RULING 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aw-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~246</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new read.
comp-adversary: RUN by the issuer at the cut -- r73 c48 FAILS on deployed (BA, AMD, ASML): 2,719 unit-code tokens, 86 figures past 4 decimals, 3 Python reprs, 742 text spans past the page edge.
EGRESS CLASS, declared: NONE. No vendor, SEC, ft.com or wsj.com call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r73-246` (branch `wk-AMGT_RESAPP-246`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r73-246`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-aw-2` (round 73, decomposition s.81)

PRD v0.40 FWD-5 DONE WHEN (PRD `:521-525`): the pack reads as a document in Opal Brand form, with no raw code. CTO ruling 2: figures
rounded with their unit in words; field labels in words, never schema strings; no line past the page edge; no Python reprs.

The research read:
- each figure line prints its unit code ("184627.02107120003 MILLIONS", "BOEING CO/THE TEXT (string field)") from the shared
  `lib/research/checkface/render_print.py` (~`:212`, `:244`), called via `lib/research/print/render_pack.py` ~`:319`;
- lines run past the page at `render_pack.py` ~`:77-84`, `:197-200`.
**Fix it in `render_pack.py`** (render_print is shared with other renders; do not change it).
1. **Each figure:** rounded to its unit's sensible precision (money in millions to 1 decimal, percent to 1 decimal, ratio to 2), with
   the unit in words ("USD 184,627.0 million", "12.4%", "1.53x"). Text fields print the value only. A null prints a plain word
   ("not reported"), never None, True, False, `[]` or a dict.
2. **Lines wrap within the page width.** No span past the right edge.
3. **Plant tests** in `lib/research/print/`.

**Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W246-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. No figure VALUE changes, only its rounding and wording. `render_print.py` is read only.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/print/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~246/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aw-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round73/checks/r73_served.py" --cell c48 --where local; echo "exit=$?"</invocation><expect>the 3 prints read with pages above 0; C1, C2, C3 and C4 PASS (0 unit codes, 0 long decimals, 0 reprs, 0 clipped spans); R73 C48 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aw-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/print; echo "exit=$?"</invocation><expect>every plant case passes; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~246 <0.9.0_WK_AMGT_RESAPP~246@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~246/AMGT_RESAPP.TO-AMGT-aw-2.print-as-document.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the per-unit rounding rule;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-72 analysis item 2, ruling 2. The CVO reads BA's rendered pages at L9 (judgment). Served by aw-7.

<status>pending</status>
<round>73</round>
<slot>0.9.0_WK_AMGT_RESAPP~246</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
