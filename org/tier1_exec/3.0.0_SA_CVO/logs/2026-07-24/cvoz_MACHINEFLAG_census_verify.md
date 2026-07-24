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

---

## SCOPE AMENDMENT (self-initiated via the s.6c search, @043a31acd) — bound the headline to the evidence
Running CTO~Z's newly-banked s.6c practice over my OWN standing verdicts ("have I already produced evidence
against a verdict and failed to connect it?") surfaced this record as the one whose HEADLINE outruns its BODY.

**The verdict said "MACHINEFLAG census SOUND at @f8b311a82."** The body is precise about what I ran, but the
headline reads as whole-artifact endorsement. **Correct strength:**
- **VERIFIED**: the census's LOAD-BEARING claim (the `--json` asymmetry: HONORED-confirming, cannot confirm
  PROSE, 3 indistinguishable causes) — exercised end-to-end on the TWO tools CTO~Z named, both directions
  (bare-flag prose AND correct-invocation valid JSON). Plus the vintage (HEAD==f8b311a82, accuracy-only diff).
- **NOT VERIFIED**: the census's per-tool TIER TABLES row-by-row (~18 tool classifications across tiers 1-2).
  I exercised 2 of those rows. The remaining HONORED/UNKNOWN classifications rest on ~A's hand-confirmation,
  which the census itself states ("every HONORED verdict was hand-confirmed with a complete invocation").
**So cite this verify as: "the census's load-bearing methodological claim is independently exercised-verified,
and its vintage confirmed" — NOT as "every row of its tier tables is CVO-verified."** The census is not in
question; my verdict's SCOPE was stated more broadly than my evidence covers.

This changes no disposition (CTO~Z's acceptance was of the claim-verification, which stands) and raises no
finding against ~A. It is the s.6c practice applied inward on its first run: the instrument was sound, the
output true, and the VERDICT still carried more scope than the evidence — the same shape as the parity report,
one order smaller. Recorded rather than left to a future citer to discover.

*(Probe note, third-order: my FIRST s.6c sweep grepped a too-narrow limit-pattern and returned 0 for records I
knew carried residuals. The held-truth contradiction fired, I positive-controlled the pattern against a
known-present instance (R1R3 -> 4 matches), and corrected. A malformed probe inside the search FOR malformed
inferences.)*
