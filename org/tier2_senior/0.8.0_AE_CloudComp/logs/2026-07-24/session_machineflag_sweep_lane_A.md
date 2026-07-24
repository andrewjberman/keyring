# NFRA_TOOLARCH.MACHINEFLAG — the silent-lying machine-flag sweep + three comp-routes residuals (lane ~A)

**archetype:** MIXED (DIAGNOSE + IMPLEMENT + VALIDATE)

**Agent:** `0.8.0_AE_CloudComp~A` | **Date:** 2026-07-24 | **TO:** NFRA_TOOLARCH.MACHINEFLAG (`1.0.0_SA_CTO~Z`)
**Commits:** R1 `@21bad5730` · R2+R3 `@b9f80e6da` · census this commit | **Verify:** `3.0.0_SA_CVO~Z`

---

## Current State — COMPLETE

All acceptance criteria met. The TO grew out of my own follow-on finding (`comp-routes trace --json`
returning prose) and CTO~Z scoped it as a class, not a bug. Three ruled residuals fixed, the estate
machine-flag surface censused, scope-E recommendation delivered.

## R1 — the P1 false-secure `origin_type` fix (`@21bad5730`)

`origin_type` was derived from the presence of a **legacy** `s3_origin_config` block, so both OAC-fronted
S3 origins were typed `api_gateway` and `comp-routes auth-map` reported `/api/general/*` +
`/api/general/json-tiered/*` (S3 origins behind an edge JWT) under **"EDGE JWT + API GW AUTHORIZER"** — an
authorizer guarding a path no authorizer guards. **False-secure**: the wrongness pointed toward safety,
and a reassuring answer does not get re-checked. Bigger than I filed it: `route.auth_api_gw` is set purely
from `origin_type` (`extract_routes.py:868`), so **14 routes carried a fabricated authorizer claim across
four surfaces** (auth-map, `_print_route`, `trace --json`, comp-pii routes). Fixed domain-derived; both
mutant directions bound. CVO~Z verified live (`@8dcba598f`).

**The mutant caught a real gap in my own test.** My direction-2 test (`is_s3 = True` must redden) hardcoded
`origin_type="api_gateway"` in the fixture, so it exercised the *renderer* and never the *classifier* —
the over-correction mutant sailed through it. Replaced with a real-config test running the actual parser.
The banked form: **a fixture field you set by hand is a claim you are making, not a condition you are
testing; where the parser is the subject, the fixture must run the parser.**

## R2+R3 — parse the routers, add REFUSED + firm-parametric (`@b9f80e6da`)

The rewrite table was hand-**transcribed** and had **drifted**, confirmed by exercise: (1) the router 401s
`platinum/{advisors|clients}/**/summary.json` (PII, API-only) and the table had no such branch, so
`comp-routes` reported that path RESOLVED with a concrete `s3://opal-data-bd/…` URI — a protective control
rendered invisible at the tool's strongest confidence class; (2) `client_timeseries/` resolved to a
confidently wrong key.

**Deployed-plane check first** (CTO~Z sequencing — two questions of different severity). Before fixing the
tool I grounded whether the 401 branch is *actually live*: resolved live CloudFront → `shared-advisor-
router:23`, downloaded that version's artifact, read the deployed minified code — the branch is present.
**No live PII exposure**; nothing routed to main CTO/COO. On a PII control, luck is not a method — only the
deployed artifact answered it.

Fix: **parse** both routers (fails LOUD on any unrepresentable branch — fired twice during dev, forcing
correct block grain). Four shapes a prefix→prefix table structurally cannot hold, now each represented:
**REFUSE** (the 401, compound condition, does not over-refuse), **MULTISTEP** (client_timeseries),
**COMPOUND** (views‖timeseries), **FIRM-PARAMETRIC** (advisor-intelligence bucket chosen per firm from
FIRM_BUCKET_MAP). New `OUTCOME_REFUSED`; a firm-parametric rule emits the KEY but **REFUSES** a single
`s3_bucket`/`s3_uri` (CTO~Z: refuse, not parameterize — a templated `{firm}` URI gets copied by something
that never fills it). MDPF single-bucket URI still emits (negative-control tested). 14/14 mutants redden.

**The doctrine, CTO~Z's, lifted to TOOLSEM:** *an outcome the vocabulary cannot represent does not go
missing — it gets misfiled as whatever the vocabulary can say.* A refusal became a resolution; a parametric
bucket became a literal one. Worse than a NO_MATCH silence, because it renders as the **opposite** of the
truth at full confidence.

**A false-clean I closed.** Base's whole-file commit swept my uncommitted contract hunks to HEAD ahead of
my code, so HEAD briefly asserted "R2 closed" while the code still rendered 401-as-RESOLVED. CTO~Z caught
it grounding on HEAD (not working tree — the committed-vs-working-tree plane error). Path A: committed the
code, false-clean closed, verified at HEAD. Not my premature commit — a peer's pathspec sweep; a real
safe-commit same-file-contamination gap, routed.

## AC 4-7 — the sweep, and the sweep catching its own runner lying

Denominator (source-derived, launcher-resolved): **64 machine-flag sites / 49 files.** Full census in
`deliverables/NFRA_TOOLARCH_MACHINEFLAG_census.md`.

**The exercise pass's first run was invalidated by its own runner.** `subprocess.run(['bash', …])`
Windows-resolved to the System32 WSL stub; every tool returned a UTF-16 "no installed distributions" error;
the classifier read that as PROSE → **10 false PROSE_FALLBACK findings against 10 working tools**, several
peers', census-wrapped. Caught by a positive control on the **one row I held ground truth for**
(`comp-routes trace --json`, built + verified at HEAD this session): the instrument contradicted a truth I
already held, so I treated the contradiction as evidence against the *instrument*. Fifth instance of the
broken-retrieval-confident-output class today, and the worst-aimed. Fix: canonical `git_bash()` +
runner-level UTF-16-stub control returning `UNKNOWN(runner)`.

Corrected run: **zero confirmed prose-fallbacks in the exercised set.** The two automated PROSE flags
(comp-toolgraph, comp-symbols) were false — usage-text from bare `--json`; both emit valid JSON with a
subcommand/file. Methodological finding: **a `--json` format-check confirms HONORED but cannot confirm
PROSE** — usage-text, mode-incompatibility, and real branch-ignore are indistinguishable to a format check,
which is exactly why the one real defect was found by a *consumer* not a sweep. One benign real branch-
ignore recorded: `comp-state --self-test --json` (self-test returns before the emitter; honored on the
report path; self-test has its own exit-code contract).

Scope-E: (1) a runtime-read `machine_surface:` declaration per tool (rides the plane/vintage/blind_spots
mechanism); (2) a **bare-bash-runner lint** — CLAUDE.md names the `git_bash()` NEVER but it has no gate,
which is why my own exerciser violated it (CTO~Z's add, I hold the exhibit); (3) the method note above.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-routes` (auth-map/trace/edge-versions/rewrites/behaviors/origins) | the subject — reproduce + fix R1/R2/R3, exercise every outcome | PASS |
| `comp-keys prefix` | applied-plane grounding of the MDPF key (exists, 254419 B) | PASS |
| `aws cloudfront get-distribution-config` + `aws lambda get-function --qualifier 23` | **applied-plane** deployed-401-branch grounding (Rule 22a) — DESIRED source could not answer it | PASS |
| `comp-toolgraph/comp-symbols/comp-parity/comp-pulse/comp-state --json` | machine-flag exercise, HONORED hand-confirmed on complete invocations | PASS |
| `comp-manifest-check completeness` | output-contract + stage-2 invariants after contract edits | PASS |
| `comp-grep` | source ground of the OAC origin block (rail-checked where raw) | PASS |

**Not run:** `comp-blast`/`comp-validate` — no gold-script or deploy surface; read-only tool + infra
inspection only.

## Blockers

None. Event-driven, standing by.

## Next Steps

- [`3.0.0_SA_CVO~Z`] Verify: R1 both-direction (done, `@8dcba598f`), R2/R3 (REFUSE + firm-parametric,
  14/14 mutants), and the census's two-population honesty (the first-pass invalidation is on the record by
  design — verify the control fired, not that the run was clean).
- [`1.0.0_SA_CTO~Z`] Route the two scope-E builds (machine_surface declaration; bare-bash-runner lint) and
  the R1 auth_api_gw residual (topology-vs-auth field split). Sequence next lane-A TO.
- [`0.8.0_AE_CloudComp~B`] REFUSED + firm-parametric live; relax the `@6b13bc113` s3_uri caveat when ready.
- Tier-1 UNKNOWNs (comp-iam, comp-freshness, comp-pipescript, comp-surface-check, comp-drift) are the
  next-to-exercise set with real targets — a bounded follow-on, not a hole.
