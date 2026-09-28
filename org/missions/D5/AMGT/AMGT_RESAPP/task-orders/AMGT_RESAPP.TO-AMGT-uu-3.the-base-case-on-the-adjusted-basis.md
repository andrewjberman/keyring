# AMGT_RESAPP task order -- `AMGT-uu-3` -- THE BASE CASE ON THE ADJUSTED BASIS, EACH INPUT CARRYING ITS BASIS, THE VALUE PRINTED AS A VALUE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-uu-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~166</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for writes -- the checks read committed fixtures; AC1/AC2 make no AWS call. The served change reaches the Lambda at uu-4.
comp-adversary: RUN by the issuer at the cut -- AC1 was fed a GREEN arm (a scratch reference implementation of the ruled rule, monkeypatched in: 3 of 3) and reads 0 of 3 at base, so it discriminates both ways; AC2 compares the PAGE against the EXPORT, so a change on one side only fails it. Blind spot, stated: the pinned blocks are three names; the served census over every name is uu-4 AC3.
EGRESS CLASS, declared: NONE. No server, no fetch, no network, no Bloomberg call.
</preflight>

## 1. THE CELL -- `AMGT-uu-3` (round 46, decomposition s.54)

**Andrew ruled (2026-09-28 ~21:3xZ): the Base case is ADJUSTED EPS x ADJUSTED P/E, rebuilt from the served data with no new
vendor pull.** Today the Base case = `BEST_EPS` (FY1, which Bloomberg defines on the adjusted basis) x the median of `PE_RATIO`
(which tracks GAAP) over the closed fiscal years: a mismatched pair. AMD's served base reads 1.035 of its price only because of
that mismatch. Three limbs, one cell:

1. **The adjusted P/E.** For each closed fiscal year y (`fiscal_year <= history_window.latest_closed_fiscal_year` and
   `< consensus_eps.fiscal_year`) where the block carries BOTH a `PX_LAST` and an `IS_COMP_EPS_ADJUSTED`
   `fiscal_year_line_item` with EPS > 0, JOINED ON `fiscal_year` (never on a date string): `pe_y = (PX_LAST_y / f) /
   IS_COMP_EPS_ADJUSTED_y`, where f is the block's minor-unit factor (`model_block_pull._is_minor_unit_quote` /
   `_MINOR_UNIT_FACTOR`: 100 for a GBp quote over GBP reporting, else 1) so the multiple is dimensionless. `trailing_median_pe`
   = the median over exactly those years; its `window` lists them, `n` counts them, and it carries a `basis` object naming
   both mnemonics (shape as the figure rows' `basis`: `{"mnemonic", "definition"}`). Base value = `consensus_eps.value x
   trailing_median_pe.value x f`, with every existing refusal (EPS not positive, no price, currency mismatch, the
   `[0.33, 3.0]` band) kept as it is; the formula text says "adjusted" for both inputs.
2. **`consensus_eps` carries its `basis`**: the `basis` object of the block's own `BEST_EPS` `forecast` figure for the same
   fiscal year, copied, never re-worded.
3. **Served values print as values.** A SERVED case value prints with exactly two decimals ("537.70 USD", "5941.78 GBp") in
   BOTH `lib/research/print/render_pack.py` `_model_case_line` (`:741-760`, today `str(value)`) and
   `portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx` (`:212`, today `` `${String(value)} ${currency}` ``), identically:
   Python `"%.2f" % value`, JS `value.toFixed(2)`. FWD-30 compares these two lines byte for byte.

**ONE implementation of the rule.** It is computed today by the producer, `integrations/bloomberg/research/model_block_pull.py`
`_compute_cases` (`:1140-1300`), and served AS LANDED by `lib/research/api/scoped_amgt.py` `_model_cases` (`:2971-2998`).
Stored blocks carry the old construction, and re-landing them is out of scope (no S3 write), so the served adapter must
compute the Base case from the stored block's own figures by the SAME function the producer calls. Where that function lives
is yours, provided the Lambda's import closure carries it (the build is `infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh`;
you may RUN `--build-only <a temp dir>` to prove it, which uploads nothing; you edit nothing under `infra/`). Upside and
Downside stay the ruled ABSENT object, reason unchanged ("methodology to be discussed with Andrew" -- it is still true of them).

## 2. BOUNDS

1. **No S3 write, no Bloomberg call, no deploy, no server.** Standing: no install, no push, no promote, no vendor call.
   REFUSE, do not rescue.
2. **Nothing but the Base case's construction, its inputs' `basis`, and the two print sites moves.** The pdf path (`build_pack`),
   the posture path, every other served key: byte-unchanged. The upside/downside objects: byte-unchanged.
3. Portal files commit inside `portal/` on your portal branch, then the outer commit. Do not commit the portal gitlink.
   Python from the repo root with `PYTHONPATH="$(pwd)"`. Update the existing tests that assert the old formula; add the tests
   that pin the new one.

## 3. SURFACES

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/**
lib/research/api/scoped_amgt.py
lib/research/api/*.py
lib/research/api/tests/**
lib/research/print/render_pack.py
lib/research/print/tests/**
portal/src/pages/SecurityAnalysis/tabs/ModelTab.tsx
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~166/**
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; the fixtures under `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/fixtures/`.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-uu-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-3.AC1.py; echo "exit=$?"</invocation><expect>ADJUSTED BASE CASE, BASIS CARRIED, VALUE PRINTED: 3 of 3 names -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-uu-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-3.AC2.py; echo "exit=$?"</invocation><expect>PAGE AND EXPORT PRINT THE SAME CASES: 2 of 2 names (each: harness rc=0; CASES page=3 rich=3 same=3 missing=0 extra=0) -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-uu-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round46/checks/uu-3.AC3.sh; echo "exit=$?"</invocation><expect>all passed (no failed, no error) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 is the rule over three pinned stored blocks (AMD USD, GOOGL the raw-float name, RKT the GBp minor-unit name); AC2 the page
and the export moving together; AC3 the bound (the case, export and producer-guard suites).

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~166/AMGT_RESAPP.TO-AMGT-uu-3.the-base-case-on-the-adjusted-basis.proof_of_spec.json`. Report once: what you changed and where (name the module that holds the one rule and whether `--build-only` shows it in the closure), the three names' new base values and ratios, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-45 analysis s.4 items 3 + 4, with s.2 item 2 answered by Andrew (record @c027b4726f, CTO msg 26218).
Base: AC1 FAIL (0 of 3), AC2 PASS (2 of 2, both sides unchanged -- run on the published tree, since the shared tree's harness
crashes, Z-S292), AC3 PASS (66 passed). GREEN arm for AC1 (scratch reference): 3 of 3 -- AMD 415.64 USD (ratio ~0.66), GOOGL
511.61 USD, RKT 5941.78 GBp. Issuer's choice, stated: compute at SERVE time from the stored figures (one Lambda redeploy, no S3
write over ~95 keys) rather than re-land the blocks. SERVED; reaches the served body at uu-4 under a never-widen pair.

<status>pending</status>
<round>46</round>
<slot>~166</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
