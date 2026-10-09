# IRPT_YCDGEN task order -- `YCD-w-6` -- ROUND 6 (THREAD): THE RESIDENT PACKAGE CARRIES THE OPAL BRAND ASSET

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6M.md</decomp_doc>
<owned_cells>YCD-w-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_IRPT_YCDGEN~7</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE a render-asset change; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the gap was measured by row IRPT_YCDGEN-D2-S3 and ruled by the CTO (msg 1717)
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT) -- the Analysis report made in house, Opal-branded, with no YCharts call. Work ONLY in the worktree
your spawn line names; every path below is relative to that root. No vendor call, no AWS call, no deploy.

**RULES THAT BIND THIS ORDER (verbatim, from the dell2 CTO and Andrew):**
- "research browsing only when necessary; no packages, no installs, no file fetched onto the box."
- Never `bun install`; no package fetch of any kind.

## 1. YOUR CELL (inlined from the round-6 addendum-M decomposition)

### `YCD-w-6` -- the resident package renders the Opal page without a git checkout (resident render hop; FWD-1)
Today the resident host refuses every Opal-path Overview with `LayoutRefused("brand asset absent ...")`: the host has no git checkout,
the unit sets no `IRPT_BRAND_SPEC` / `IRPT_OPAL_LOGO`, and `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py`
`_asset_path` (lines ~101-108) looks only at those env vars and the git roots. Both assets are gitignored under `deck_generation/`.
- The logo is ALREADY committed at `infra/aws/lambda/investor-reporting/ycharts/research/brand/Opal-Capital-Logo-Full-Color.svg` (the
  laptop's byte-exact copy of the source of record). Do NOT edit or replace it. If it is absent at your HEAD, file a row and stop.
- `infra/aws/lambda/investor-reporting/ycharts/research/brand/brand.json`: regenerate it with the logic of
  `deck_generation/scripts/03_extract_brand_spec.py` (`build_brand_spec()`), written byte-identically to what that function produces
  (import it; do not hand-copy values). ASCII only.
- `layout_overview.py`: make the asset lookup try the packaged path FIRST -- `Path(__file__).parent / "brand" / <file name>` for the spec
  (`brand.json`) and the logo (`Opal-Capital-Logo-Full-Color.svg`) -- then the env var, then the git roots, as today. A missing asset
  still raises `LayoutRefused` (no substitute logo). No other layout behaviour changes.
- One test `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_brand_packaged.py`: `load_brand()` resolves both files from the
  packaged path with no env var set and the process cwd outside any git repository.

## 2. THE CONTRACT YOU BUILD AGAINST

**R21 The resident package renders the Opal page without a git checkout.** `load_brand()` resolves the spec and logo from
`ycharts/research/brand/` beside `layout_overview.py` before any env var or git root; the resident package builder's `--research` packages
both (tracked, non-test files under `ycharts/research/`); an Opal layout renders from a package tree that sits OUTSIDE any git repository
with no brand env var set.

## 3. WHAT YOU NEED TO KNOW

- The builder: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py` (read its docstring; `--research`,
  `--opal-map`, `--base-pin`, `--files-from`, `--member`, `--state-json` for an offline build). For AC3 you may build with `--state-json`
  from a file you write under your deliverables dir, or copy the `ycharts/research/` tree of HEAD (git archive) into a temp dir outside the
  repo; say which.
- The render: `layout_overview.py` renders the Overview PDF through `render_pdf.cjs` (node + playwright-core). If no node or playwright-core
  is on this box, AC3 measures `load_brand()` plus the HTML layout step from the extracted tree and records the PDF step as not run, with the
  reason; never install anything.
- ASCII only in new text. No client figure and no secret in any committed file.

## 4. SURFACES AND BOUNDS

NEVER: a vendor call, any AWS call, a deploy, an install, a package fetch, an edit of the logo file. A check you cannot satisfy inside your
`<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (id
`IRPT_YCDGEN-D2-W7-S<k>`, next unused k; `fabric` "dell2"; `surfaced_at` the real UTC time).

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/brand/brand.json
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_brand_packaged.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~7/w6_checks.py
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~7/IRPT_YCDGEN.TO-YCD-w-6.resident-package-carries-opal-brand-asset.proof_of_spec.json
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- `load_brand()` resolves both assets from the packaged path with no env var and no git root
- **AC2** -- `brand.json` equals `build_brand_spec()` output byte for byte, and the logo is byte-equal to its commit
- **AC3** -- the Opal layout renders from a package tree extracted outside any git repository with no brand env var

`w6_checks.py` (new): one argument (`brand`, `bytes` or `render`), one RESULT line each.

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-w-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~7/w6_checks.py brand</invocation><expect>^RESULT: brand PASS</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-w-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~7/w6_checks.py bytes</invocation><expect>^RESULT: bytes PASS</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-w-6"><invocation>python org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~7/w6_checks.py render</invocation><expect>^RESULT: render PASS</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Commit, then write the instance at
`org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~7/IRPT_YCDGEN.TO-YCD-w-6.resident-package-carries-opal-brand-asset.proof_of_spec.json`
with `to_id` `IRPT_YCDGEN.TO-YCD-w-6.resident-package-carries-opal-brand-asset`, check it with `python .tools/proof-of-spec-check.py
<instance>`, and commit it. Report once: each criterion's verdict line with the output above it; files written; rows filed. Leave the
`<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~G2):** addendum M (IRPT_YCDGEN_DECOMP_R6M.md), cut on 1.0.0_SA_CTO~DELL2 ruling msg 1717 after row
IRPT_YCDGEN-D2-S3 (the F1 run, ledger irpt-ycdgen-f1-svc-20261008). Chain `~7`, fresh slot; worktree cut from box/dell2 once the laptop's logo
commit is reachable (MSTR msg 1724 ask). Risk WORLD (the gate floor for an infrastructure path): a packaged render asset changes; nothing deploys in this cell -- the release that ships
it is its own never-widen pair, after-read = one Opal-path layout rendering on the host.

<round>6</round>
<workstream>R6M_BRAND_ASSET</workstream>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
**ISSUER RULING 2026-10-08 (2.0.0_SA_COO~G2) on row IRPT_YCDGEN-D2-W7-S1:** the builder's --research filter omits .svg, so the
release build that ships this cell passes `--member ycharts/research/brand/Opal-Capital-Logo-Full-Color.svg=infra/aws/lambda/investor-reporting/ycharts/research/brand/Opal-Capital-Logo-Full-Color.svg`
and its gate listing must show the member (a release-plan condition, not a builder edit). Row D2-W7-S2 (logo formats empty in brand.json
on a box without the logo package) is accepted: the Opal page reads colors and typography only.

<status>complete</status>
