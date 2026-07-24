# CVO~Z verify — NFRA_TOOLARCH.MACHINEFLAG census @f8b311a82 (~A)

**archetype:** VALIDATE · `3.0.0_SA_CVO~Z` · branch CLOUD · GO: CTO~Z 045927Z (vintage-pinned)
**Verdict: SOUND at the pinned vintage. Load-bearing claim CONFIRMED BY EXERCISE (per CTO~Z's method).** No finding.

## Vintage (CTO~Z pinned it -- a verify on the wrong commit is the stale-vintage class)
- HEAD == `f8b311a82` (confirmed). NOT the superseded `@a4f7bb892` CTO~Z accepted at.
- `a4f7bb892 -> f8b311a82` diff = +64/-4 across the census .md + NFRA_TOOLSEM_PRD.md; **accuracy-only**: the
  "64 sites / 49 files" denominator appears only in unchanged contextual lines, no finding removed/altered, the
  ruled "runner-failure lead" ("the first automated exercise pass was invalidated by its own runner") intact.
  Both corrections (@ddb8e5393 tier-1-mis-derived-from-rail; @f8b311a82 ~B's own over-statement walk-back) are
  scope/accuracy fixes from ~B's review, not finding changes. CTO~Z's "accuracy-only" holds.

## THE LOAD-BEARING CLAIM -- verified BY EXERCISE, not by re-reading (CTO~Z's instruction)
Claim (census :64-70, :130-132): an automated `--json` format-check is **HONORED-confirming ONLY**. A non-JSON
result cannot be called PROSE, because three states print non-JSON and are indistinguishable to a format check:
(a) a real flag-ignored-on-a-branch defect, (b) usage/help text from an INCOMPLETE invocation (missing
subcommand/arg), (c) an incompatible mode combo. So the sweep's honest output is HONORED-or-UNKNOWN; a PROSE
verdict needs a per-tool valid invocation by hand. ~A's two false-positives: comp-toolgraph, comp-symbols.

**EXERCISED (I hold the ground truth -- ran them myself, correct invocation, not the sweep's subprocess-bash):**
| invocation | result | proves |
|---|---|---|
| `comp-toolgraph --json` (bare) | **usage text** (`usage: comp_toolgraph.py ... {census,edges,...}`) | cause (b): incomplete-invocation prose |
| `comp-toolgraph census --json` | **VALID JSON** (dict, keys artifact/author/..., 24,876 chars) | it HONORS --json behind the subcommand |
| `comp-symbols --json` (bare) | **usage text** (`usage: comp_symbols.py ...`) | cause (b) |
| `comp-symbols <file> --json` | **VALID JSON** (dict, functions/classes/constants/imports/path, 3,559 chars) | HONORS --json behind the file arg |

So both tools DO honor --json; a bare `--json` yields usage text that a format-check reads as PROSE. **The census's
sweep would false-flag both as PROSE, and the census CORRECTLY identifies them as false-positives.** The method
note ("HONORED-confirming only; a PROSE verdict requires a per-tool valid invocation") is verified: cause (b)
reproduced directly, and the HONORED direction confirmed on the correct invocation. The claim is sound.

This is the s.2e generalization exercised: an instrument that can confirm ONE direction (honored) but whose
"failures" conflate 3 causes -- the same shape as the runner incident that motivated the census (subprocess-bash
-> WSL stub -> UTF-16 error read as PROSE -> 10 false findings). The census's own honesty about this is the point.

## PROBE HONESTY (the firing condition, tick-44 doctrine, twice this turn -- and thematically exact)
Verifying a claim ABOUT instruments that misread valid content as prose, my OWN probe hit the same class TWICE:
`head -c 300 | json.loads` TRUNCATED the valid JSON mid-object, so my parser reported "NOT JSON" on output that
visibly began `{"artifact": ...}` / `{"functions": [...]}`. **The held-truth contradiction (it LOOKS like JSON,
my parser says no) fired the tick-44 firing condition at my own apparatus -- I checked my probe first, found the
truncation, re-ran on full output -> both VALID.** A truncation making valid JSON look invalid is cause (b) of the
very list I was verifying, committed by the verifier. Caught pre-report; recorded because the coincidence is the
lesson: the probe-is-an-instrument doctrine is not about other people's tools.

## Verdict
MACHINEFLAG census SOUND at @f8b311a82: vintage clean (accuracy-only corrections), denominator 64/49 intact,
runner-failure lead intact, and the load-bearing --json-asymmetry claim CONFIRMED BY EXERCISE (both named
false-positives independently reproduced -- bare-flag prose AND correct-invocation valid JSON). No finding.

## Compiler Tools
`comp-toolgraph {--json, census --json}` + `comp-symbols {--json, <file> --json}` (LIVE exercise of the claim,
both directions) · `git rev-parse`/`git diff --stat a4f7bb892 f8b311a82` (vintage + accuracy-only confirmation) ·
`comp-glob` located the census. Gap found: none in the census; 2 truncation-probe errors of my own, self-caught.
