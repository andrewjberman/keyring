# 0.4.0_DT_ClientPlatform — 2026-08-12 — pillar editability + lane narrowing

**archetype:** IMPLEMENT
**secondary_archetypes:** EXPLORE, COORDINATE

Window: since `6ace037246` (the PROD-promote log) through now. Third log of this session; the
first two cover the OPAL_INVPHL build and the v2.1.161 promote.

## Current State

**Pillar editability is BUILT, EXERCISED, and both halves are landed** — the producer by the
lane that owns it, the consumer by me.

| Piece | Where | State |
|---|---|---|
| Producer — `yang-generate-cma` optional Philosophy sheet | workspace `@b894ac431e` | **LANDED by `0.7.0_AE_CloudOps`** (YANG_PIPELINE_DEPLOY lane), not by me |
| Consumer — served-copy overlay + per-field repo fallback | portal DEV `@684e67de` | LANDED (mine) |
| `README_CMA_PIPELINE.md` stale-architecture warning | working tree, POD2 lane | authored, **unstaged**, awaiting the lane |
| Deploy (Terraform apply) | — | **NOT DONE**, deliberately separate |
| `prompt.md` yang authority narrowed | `@9df2b3e739` | LANDED |
| Deploy-completion ledger (v2.1.161) | `@b7d4681325` | CLOSED |

**Net effect:** Yang/Manav can reword a `/philosophy` pillar by editing the CMA workbook and
re-uploading it on the portal's existing Data Refresh page. No code change, no PR, no PROD
promote. **Zero new artifacts** — the sheet rides an existing workbook, the parse an existing
Lambda, the output the served key the page already fetched.

⚠ **The feature is INERT until a workbook carries the sheet.** The consumer renders exactly
today's copy; the producer emits no key. That is the designed resting state, not an unfinished one.

## What the session actually turned on

**Rung 2 of the build ladder, climbed rather than skipped.** Andrew ruled the text editable with
a hard ceiling — *"extremely light… do not want overwrought process architecture."* The scope
question was where content could live without minting anything. The answer was already in the
estate: **`GenerateCMA` is already a step in the portal's Data Refresh upload pipeline**, so a
production path that touches no code already existed. Nothing needed inventing.

**Reading the source changed the design, and the change was the whole value.** The existing
parse is `pd.read_excel(BytesIO(excel_data))` with **no `sheet_name`**. A named-sheet read
**raises** when the sheet is absent — and every workbook uploaded to date lacks it. The naive
implementation would have taken CMA generation **down on the normal case**, from an *optional,
additive* feature, on the serving path for a page promoted to PROD two hours earlier — while
passing every test in which the sheet exists.

**MUTATION-PROVEN, not argued:** swapping the guard for the naive read produces
`ValueError: Worksheet named 'Philosophy' not found` on the no-sheet limb. Reverted; 8/8 green.

**Two fallbacks, failing in the same safe direction** — producer: no/bad sheet → key absent,
`assumptions.json` byte-identical to today; consumer: key absent → repo copy. Editability cannot
introduce a blank pillar on a client-facing page.

## The lane refusal — the finding I raised against myself

`owned-paths` refused my producer commit: `yang-generate-cma` is lane `YANG_PIPELINE_DEPLOY`
(AE set + `0.2.0_DT`/`0.2.0_DS_PortfolioAnalytics`), and the README is POD2. **I did not
override** — no `--force`, no `GIT_COMMIT_AUTHOR_OVERRIDE`.

But my own `prompt.md` claimed *"yang-pipeline — Full DT Authority"*, which reads as authority
over the pipeline. **A role doc that reads broader than the gate is exactly how a seat talks
itself into an override**, so I surfaced it against my own interest. CTO ruled: **narrow the
prompt, not the gate** — the gate was behaving correctly.

⚡ **Then the same class caught the ruling seat within sixty seconds.** CTO went to land the
narrowing themselves and `safe-commit` refused them — `prompt.md` is POD4. Their *"role docs are
mine"* was itself a claim broader than the enforced lane. They declined the audited override on
the grounds they had just written the opposite instruction into my file, and it landed in my
lane instead (`@9df2b3e739`). **That provenance is in the commit message deliberately**: a rule
whose author was bound by it within the minute is much harder to talk past than my finding alone.

**CTO's addition to the staging trap** (which I then hit myself, twice): `safe-commit` stages
*before* the hook fires, so a refused write is left **in the index** — and `git checkout --`
restores *from the index*, silently bringing the edit back. `git reset HEAD` first. I found the
README still staged at log time and unstaged it.

## Verification

- **Producer, 8 cases on the real function** (no mocks of the unit under test): no sheet → None ·
  well-formed → extracted + content verified · missing column → None · empty sheet → None · blank
  load-bearing fields → None · corrupt bytes → None · empty bytes → None · mixed rows → only the
  usable row. Never raises.
- **Consumer, both limbs in a browser:** without the served block, five repo pillars with repo
  body text; with it, overridden pillars show served copy, the other three keep repo copy, a
  planted **unknown id renders nowhere**, strip still exactly five in repo order.
- **What AE landed, verified against HEAD rather than their receipt:** guarded read present,
  `PHILOSOPHY_SHEET` present, future-import present, `numpy` removed — with a positive control
  (a line I knew was in the file) so an empty read could not read as agreement.
- `tsc -b` + `eslint` clean; `commit-gate.sh` clean on the Lambda.

## Blockers

None. The producer landed in its own lane; the README rides POD2's routing; the deploy is
deliberately a separate act.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | `capital-markets`, `DataRefresh` (content), `generate_cma*` / `*cma*` (name), `yang-generate-cma*` | **The session's decisive instrument.** Found the served path, the Data Refresh surface, and — critically — a **measured zero**: `generate_cma*` = 0 hits over 25,559 files, which is what exposed the README as documenting a dead architecture. A `--name` search first returned 0 for DataRefresh; re-running by **content** found 66 hits across 409 files. Wrong axis, not absence. |
| `commit-gate.sh` | on the CMA Lambda, mine and HEAD's | **Gap found:** HEAD's version ALREADY failed with 3 errors before my change (F401 unused `numpy`; 2 pre-existing PEP-604 unions). Cleared all four to make it committable, verifying numpy had 0 uses rather than trusting ruff. Reported rather than folded in silently. |
| `safe-commit.sh` / owned-paths | producer half, prompt.md | **PASS as designed** — correctly refused a cross-lane write; no override reached for. |
| never-rules-gate (F-010) | ledger-close commit | **Fired on me correctly**: `-m` with backticks would have executed a substitution before git saw it. Redone with `-F`. |
| comp-rail (Rule 21) | an `infra/` grep during log prep | **Fired correctly** — routed me off a blind `.tf`-adjacent grep. Re-ran without it. |
| `tsc -b --listFiles` / `eslint` | portal | PASS, 1931 files examined. |

**What worked:** `comp-find`'s denominator line is what made a *measured zero* usable as
evidence rather than an absence of luck. **What failed:** nothing this window. **Gap found:** the
HEAD-already-fails-the-universal-gate class (census authorized bounded/post-P1 at COO's
sequencing, classify-don't-fix — not started).

## Next Steps

1. `[2.0.0_SA_COO]` — route the `README_CMA_PIPELINE.md` stale-architecture warning to a POD2
   seat; it is authored and parked in my tree.
2. `[2.0.0_SA_COO]` / `[0.7.0_AE_CloudOps]` — the `yang-generate-cma` **Terraform deploy** is
   still outstanding and is deliberately a separate act; the feature is inert until then.
3. `[2.0.0_SA_COO]` — the CI zero-file typecheck TO (`ci.yml:56` should call package.json's
   `typecheck`). **Must be MUTATION-verified, not accepted on a green run.**
4. `[1.0.0_SA_CTO]` / `[2.0.0_SA_COO]` — the `/prod-deploy`-vs-GATE-5 collision stands: three of
   seven legs push shared branches.
5. `[0.4.0_DT_ClientPlatform]` — a live-PROD visual pass of `/philosophy` + the model modals at
   Andrew's convenience. Nothing else outstanding.
