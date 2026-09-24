# AMGT_RESAPP task order -- `AMGT-rk-124` -- the SERVER half of the overlay check-face wire: `read_security_overlay` emits `check_face` for its own header figures, so a REFUSED figure stops rendering as a bare number in the page's most prominent slot. CODE ONLY, `lib/**`, no deploy, no served bytes moved

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-124</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~124</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell arms no cron, alarm, monitor or cadence and runs no producer.
  It adds one key to a function's return value.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy, trust or grant is edited. The cell reads S3 through the
  adapter's existing read path under the seat's existing credentials and writes nothing to AWS.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~124`.** Work ONLY in the worktree whose absolute path is given in your spawn prompt.
Your first act prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that
`lib/research/api/scoped_amgt.py` and `lib/research/checkface/run_checks.py` exist; if either is absent, STOP with a
BLOCKING row. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~124;`. **NEVER RUN AN INSTALL.**
Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

⛔ **EVERY PYTHON SCRIPT YOU RUN FROM `.scratch/` MUST BE INVOKED AS `PYTHONPATH="$(pwd)" python .scratch/...`.**
A bare `python .scratch/x.py` sets `sys.path[0]` to the SCRIPT's own directory, not the repo root, and
`from lib.research...` raises `ModuleNotFoundError` no matter what you `cd` to first. **This is measured, it is row
`AMGT_RESAPP-Z-W117-S1`/`S3` from round 30, and the issuer exercised BOTH forms at this cut** -- bare form:
`ModuleNotFoundError: No module named 'lib.research'`; `PYTHONPATH` form: `IMPORT OK True`, rc=0. Every invocation
below already carries it.

## 1. THE CELL -- `AMGT-rk-124` (round 31, decomposition s.39b)

**THE DEFECT.** `SecurityOverlayBundle` carries `header_figures` and **no `check_face` field at all**
(`portal/src/pages/SecurityAnalysis/types.ts:1002-1017`, against `ThesisBundle`'s `check_face` at `:962`), because
`read_security_overlay` never builds one (`lib/research/api/scoped_amgt.py:1936-1951`). The overlay's renderer
therefore calls `displayValue(figure.value, undefined, undefined)`, `isRefusal(undefined)` is `false`, and
`refusalPresentation.ts:41-43` takes the else arm and prints `String(value)`. **So a REFUSED figure renders as a
bare number in the page's most prominent slot, while the SAME figure renders as a refusal on the Model tab**, which
does the wire correctly (`ModelTab.tsx:45-55`, fed by `data.check_face` at `:149`).

⭐ **IT IS A WIRE GAP, NOT A PROP OMISSION, AND THE SERVER IS THE LONG POLE.** Nothing downstream can render a
refusal it was never sent. This cell is the SERVER half only.

**MEASURED BY THE ISSUER AT THE CUT, on live data, and these are your AC0 numbers:**

| | `BA_US_Equity` | `992_HK_Equity` |
|---|---|---|
| overlay bundle keys | **11**, `check_face` ABSENT | **11**, `check_face` ABSENT |
| overlay `header_figures` | **14** | **16** |
| thesis `check_face` entries | 179 | 228 |
| thesis check-face entries matching an overlay header figure | **14 of 14** | **16 of 16** |
| verdicts on those | **PASS 14** | ⛔ **PASS 10, PROVISIONAL 3, REFUSE 3** |

⛔ **SO THE DEFECT IS INVISIBLE ON `BA_US_Equity` AND REAL ON LENOVO: six of Lenovo's sixteen header figures are
NOT PASS and every one of them currently renders as a bare number.** The three REFUSE are `header:CIE_DES`,
`header:CIE_DES_BULK`, `header:EQY_FUND_CRNCY` (*"unit/sign convention is 'NOT-YET-BUILT', not MEASURED"*); the
three PROVISIONAL are `header:CUR_MKT_CAP`, `header:NET_DEBT`, `header:CURR_ENTP_VAL` (*"not yet checked
(status='PENDING')"*). **Use Lenovo as your discriminating case; BA cannot show you this defect at all.**

⚠ **THE JOIN KEY IS `figure_id`, NOT `mnemonic`.** A check-face entry is
`{figure_id, value, verdict, reason, marker}` and `figure_id` is `"<scope>:<mnemonic>"` (e.g. `"header:NAME"`).
**The issuer's first probe matched on `mnemonic`, got `0 of 14`, and would have written a false finding into this
order had it not been re-checked against the actual object shapes.** Match on `figure_id` or you will measure a
zero that is not there.

**THE ACT.** In `read_security_overlay` (`scoped_amgt.py:1870`, returning at `:1936-1951`):
1. Hoist `_figures(model_block, SCOPE_HEADER)` (currently inline at `:1939`) into a local, so it is computed once.
2. Build the check face for **exactly those header figures and nothing else** -- mirror the thesis bundle's shape at
   `:2012-2016`: import `check_block` from `lib.research.checkface.run_checks` **inside the `if model_block:` branch,
   exactly as `:2014` does** (keep the local import; it is deliberate), and call it on the header figures ALONE.
   ⛔ **Do NOT add `fiscal_year_figures` or `forecast_figures` to the overlay's check face.** The thesis bundle
   includes them because the Model tab renders them; the overlay renders only its header figures, and widening the
   call would ship a payload carrying checks for figures the overlay never draws.
3. Add `"check_face": <that list>` to the returned dict. **`[]` when `model_block` is falsy**, exactly as
   `:2012` initialises it -- never `None`, never a missing key.
4. Add tests in the adapter's existing test home.

## 2. WHERE THIS CAME FROM

`1.0.0_SA_CTO~Z`'s round-30 analysis @`28ab7ce9fd` (msg 24424), ranked item 5, first of the four layout defects, in
its stated value order. The inventory that found it is @`13eeb3e447`.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/**
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~124/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
.scratch/r124/**
</paths>

⚠ **`portal/**` IS DELIBERATELY ABSENT AND YOU MAY NOT WRITE IT.** It is lane `POD_DE_ANY`
(`.owned-paths.yaml:1944-1946`), which the ISSUING seat does not hold, so naming it here would admit you to it
through the `worker_grant` with **no lane consulted** -- the delegation CVO ruling R5 forbids. The client half is
carded to the CTO. If your work seems to need a portal edit, **STOP and file a row**; do not reach for it.

## 4. BOUNDS

- **CODE ONLY. No deploy, no `terraform`, no Lambda update, no S3 write, no AWS mutation of any kind.** The adapter
  file changes on disk; **nothing served moves**, because this cell does not deploy it. That is why it carries no
  never-widen pair.
- Reads of live S3 through the adapter are fine and expected (AC0/AC3 do exactly that).
- **No vendor call. No Bloomberg call. Zero egress.** Every figure you need is already in the stored model block.
- Do not change `read_thesis_bundle`, `check_block`, `_figures`, or anything the Model tab reads.

## 5. PROOF OF SPEC (literal; timeout 600)

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-124"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r124/ac0.py</invocation><expect>BEFORE any edit, on live data, printed with denominators: for BA_US_Equity the overlay bundle has 11 keys and "check_face_present False" with 14 header_figures; for 992_HK_Equity the overlay bundle has 11 keys and "check_face_present False" with 16 header_figures. Joining on figure_id (NOT mnemonic), the thesis check face covers 14 of 14 BA header figures (PASS 14) and 16 of 16 Lenovo header figures (PASS 10, PROVISIONAL 3, REFUSE 3), and the six non-PASS Lenovo figure_ids are printed by name. Record every value</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-124"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -3</invocation><expect>the adapter suite BASELINE before your edit -- record the passed/failed counts as A0. This is a measurement, not a bar; whatever it reads is the number AC4 must beat by exactly your new arms</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-124"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r124/ac2.py</invocation><expect>AFTER the edit, on the SAME two live names: both overlay bundles now have 12 keys with "check_face_present True". BA's overlay check_face has 14 entries, all verdict PASS. Lenovo's has 16 entries with PASS 10, PROVISIONAL 3, REFUSE 3, and the three REFUSE figure_ids are exactly header:CIE_DES, header:CIE_DES_BULK, header:EQY_FUND_CRNCY. Every entry carries figure_id, value, verdict, reason and marker. NO entry has a scope other than header -- print the distinct scopes as proof the call was not widened to fiscal_year or forecast figures</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-124"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python .scratch/r124/ac3.py</invocation><expect>THE NO-REGRESSION ARM, printed as an explicit comparison: for both names the thesis bundle's check_face length is UNCHANGED from AC0 (179 for BA, 228 for Lenovo) and its header_figures are unchanged; and the overlay's other 11 keys are byte-equal to AC0's values under json.dumps(sort_keys=True) with check_face removed. "others_byte_equal True" for both names, and the empty-model-block path returns check_face == [] (a list, never None) -- assert it on a name with no model block, or construct the falsy-model_block call directly and say which you did</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rk-124"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest lib/research/api/tests -q -p no:cacheprovider 2&gt;&amp;1 | tail -3</invocation><expect>passed = A0.passed + (the number of arms you added) and failed = 0. If A0 carried pre-existing failures, they must be the SAME failures by name -- print them and say so rather than reporting a clean number</expect></criterion>
  <criterion id="AC5" cell_refs="AMGT-rk-124"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; git diff --name-only $(git rev-parse HEAD) -- lib integrations infra .tools portal &amp;&amp; git diff --name-only --diff-filter=A $(git rev-parse HEAD) -- lib</invocation><expect>the first list is EXACTLY lib/research/api/scoped_amgt.py plus your new test file, and NOTHING under portal/, infra/ or .tools/ appears in either list. ⛔ This criterion deliberately does NOT use HEAD~1..HEAD: row AMGT_RESAPP-Z-W117-S4 measured that form failing on any cell whose execution spans an amendment or a second session. Pin against the commit your branch started from, printed by your AC0 run. ⚠ THE ISSUER EXERCISED THIS EXACT FORM IN THE SHARED TREE AT THE CUT AND IT RETURNED infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-constituents.py -- a PRE-EXISTING uncommitted modification belonging to no cell. YOUR worktree is cut fresh from HEAD and must NOT carry it. If this list contains ANY file you did not write, that is a BLOCKING row naming the file, never a silent pass and never a criterion you relax</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write your instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~124/AMGT_RESAPP.TO-AMGT-rk-124.overlay-check-face-server.proof_of_spec.json`
per `org/standards/PROOF_OF_SPEC.schema.json`, graded by **YOUR WORKTREE'S OWN**
`PYTHONPATH="$(pwd)" python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3,AC4,AC5` run from inside that
worktree (rc 0 is the verdict), then flip the order's `<status>` on the record face to `complete` only if every
criterion PASSES. Report once, naming: AC0's two key-counts, AC2's verdict split for Lenovo, AC3's
`others_byte_equal`, and AC5's exact file list.

**MUTATION DISCIPLINE:** snapshot `scoped_amgt.py`'s working-tree bytes to `.scratch/r124/` before editing. Never
`git checkout --`, never `git stash`, never `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES -- the L5 choices:**

1. **CODE ONLY, deploy deliberately excluded.** Emitting `check_face` changes what the adapter RETURNS, but only
   once deployed. Splitting emit-from-deploy keeps this cell inside `lib/**` (lane `BASE_EXEC`, which this seat
   holds), moves no served bytes, and needs no never-widen pair. The deploy is a routed act on the rk-122/rk-123
   pattern, and is not cut until the client half exists -- shipping the server half alone changes nothing a viewer
   sees.
2. **THE CELL IS HALF A FIX AND THE RECORD SAYS SO.** The client half is in `portal/**`, which this seat's lane does
   not admit (s.39a). Nobody should grade a half-wired overlay as a fixed one.
3. **The join-key trap is in the worker face because the issuer fell into it**, measured `0 of 14`, and caught it
   only by printing the two object shapes instead of trusting the zero. That is a `Z-S235`-class near miss at the
   cut rather than at execution, and the order carries the correction rather than the mistake.
4. **The `PYTHONPATH` form was exercised at this cut, both arms**, per the remedy adopted in `Z-S235`.

<status>complete</status>
<round>31</round>
<slot>~124</slot>
<fabric>site-z</fabric>
