# AMGT_RESAPP task order -- `AMGT-rq-1` -- THE EXPORT SAYS ABSENT THE WAY THE PAGE DOES, NAME BY NAME

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rq-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~159</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for writes -- the check READS one deployed function and the model-block store through the box's own credentials; it grants nothing.
comp-adversary: RUN by the issuer at the cut -- the adversarial arm is an instrument that disagrees with the served plane; the base run reproduces the served comparison at one capture (s.50b.1). Blind spot, stated: a local pass predicts the served one only for the code the deploy then ships, which rq-2 grades.
EGRESS CLASS, declared: ONE AWS READ SURFACE -- `lambda invoke` of Opal's own `opal-amgt-scoped-api` and reads of its model-block store, for the 89 snapshot keys; no S3 write, no vendor, no server.
</preflight>

## 1. THE CELL -- `AMGT-rq-1` (round 42, decomposition s.50)

Round 41 measured the served export against the page across the 89-name snapshot (`0.9.0_WK_AMGT_RESAPP~4/universe.json`, read 2026-09-10T23:18Z); the ABSENCE axis on all 89, the FIGURE axis on every name whose page carries figures and found 84 of 89 divergent
(`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~158/fwd30_population.tsv`; the analysis
`ledger/ROUND_ANALYSIS.round41.md` s.3). Every class is EXPORT-side, in `lib/research/print/render_pack.py`
`build_rich_text`. **Make the export say absent the way the page does, name by name:**

1. **Undrafted thesis.** Where the Thesis tab shows its ONE empty state -- `PanelEmpty` "No drafted prose for this name yet."
   (`portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx:288-291`, taken when `drafting_status` is ABSENT) -- the export writes
   that one line, NOT one `[MACHINE-EMPTY: ...]` marker per drafted section.
2. **Exec Management absent.** Where the Exec tab shows `Exec Management: ABSENT (<absent_because>).` with its detail
   (`ExecManagementTab.tsx:216-221`), the export writes those words, not its own "ABSENT: no M-1 management object ..." line.
3. **Posture.** The export carries the Posture tab's own absence lines verbatim -- its verdict line `ABSENT -- no call was
   made` with the reason the page prints beside it (`PostureTab.tsx:78`, `:442-444`). Round 41 found this line DROPPED on 80 names.
4. **Fiscal years.** The export's fiscal-year figures are limited to the years the Model tab shows (`ModelTab.tsx`); on 12 names it
   printed years the page does not show. And the one figure the page shows that the export drops (`9433_JP_Equity`) reaches it.

**AMENDMENT 1 (issuer, 2026-09-25 ~16:0xZ, on row `AMGT_RESAPP-Z-W159-S1`):** the 25 names still NOT_OK trace to the INSTRUMENT,
and the instrument is fixed in the instrument, never by bending the product to it. (5) **Remove `_page_absence_cap`** from
`render_pack.py`: the export writes every absence reason IN FULL, as the page shows it. (6) **Fix
`portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs`** (you are its named `POD_DE_ANY` writer for this
amendment): `pageAbsences` reads the whole reason (no 300-character cap), and the Model-sheet parser reads a value cell that
carries a nested `CheckFaceBadge` span. Portal files commit inside `portal/` on `wk-AMGT_RESAPP-159-portal`. The criteria are
unchanged: AC3's control must still read the stale body as NOT OK after the harness change.

Read each target from the page file, never from this text. **The instrument** is
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round42/checks/rq-1.local_sweep.py`: it rebuilds each name's
export IN PROCESS from your tree over the SAME served inputs the page renders from. Its page-side captures and model blocks are
cached OUTSIDE the repository at `C:/tmp/amgt-r42-cache2`, captured at one moment, so your fix is graded against a fixed page.
Run it with `--only KEY,...` while you work. Unit tests for each limb go in `lib/research/print/tests/`.

## 2. BOUNDS

1. **No server; no deploy; no write to AWS.** The sweep READS the deployed function and the model-block store. Standing: no install,
   no push, no promote, no vendor call. REFUSE, do not rescue.
2. **The export only.** You change no page file and not `build_pack` (the pdf path). If a class cannot be closed without a page
   change or new data, record it as a row and continue: a row, not a rescue.
3. **Do not refresh the cache.** `C:/tmp/amgt-r42-cache2` is the fixed page the issuer's base run read; deleting or re-capturing
   it moves the target. Python from the repo root with `PYTHONPATH="$(pwd)"`; the harness runs from `portal/` (read-only).

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/**
portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~159/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/**
</paths>

## 4. PROOF OF SPEC (literal; timeout 3600 for a population sweep, 600 otherwise)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-rq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round42/checks/rq-1.AC1.sh; echo "exit=$?"</invocation><expect>local rebuild over 89 of 89 folders: OK 89, NOT_OK 0, CAPTURE_FAILED 0 -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round42/checks/rq-1.AC2.sh; echo "exit=$?"</invocation><expect>the print package's tests pass, the cell's new ones among them (N passed, 0 failed) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rq-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round42/checks/rq-1.AC3.sh; echo "exit=$?"</invocation><expect>THE HARNESS CAN FAIL: harness on the stale body: rc=1 (the control needs 1) -- and exit=0</expect></criterion>
  <criterion id="AC4" cell_refs="AMGT-rq-1" judgment="true"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round42/checks/rq-1.AC4.sh; echo "exit=$?"</invocation><expect>the rebuilt export's thesis, exec, posture and fiscal-year sections for three names spanning the round-41 classes, for a person to judge whether each says what the page says; RECORDED, no verdict</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~159/AMGT_RESAPP.TO-AMGT-rq-1.the-export-says-absent-the-way-the-page-does.proof_of_spec.json`. Report once: what you changed and where, the verdict counts, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Amendment 1 (the instrument fix and the cap's removal, <paths> widened by the harness file) was cut on row Z-W159-S1 after the worker's first pass read 64 of 89; no criterion changed, and no gate limb grades a modification of an order without <placeholders>. s.7 items 1 and 2 in one cell because both live in render_pack.py (cells are cut by write set). SERVED: the change reaches the served body at rq-2. AC4 is the judgment criterion s.7 item 1 requires. The instrument's base runs are in round42/base-runs/ (s.50b).

<status>complete</status>
<round>42</round>
<slot>~159</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
