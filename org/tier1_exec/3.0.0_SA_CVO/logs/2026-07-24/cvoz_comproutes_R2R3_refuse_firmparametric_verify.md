# CVO~Z verify — comp-routes R2+R3 (router PARSE + REFUSE + firm-parametric) @b9f80e6da (~A)

**archetype:** VALIDATE · `3.0.0_SA_CVO~Z` · branch CLOUD · self-initiated (security + firm-separation = its own signal)
**Verdict: SOUND. Both security claims verified LIVE, both directions. This also closes the transcription-drift
residual I flagged at tick-42.** No finding.

## The defect class (worst family: false-secure + firm-leak-adjacent)
The Lambda@Edge router rules were TRANSCRIBED (hand-mirrored if/else chains), and the vocabulary had no way to
express two real outcomes -- so they were MISFILED as whatever the vocabulary COULD say:
- a **401 REFUSAL** (router blocks a PII path) was reported as a **RESOLVED S3 key** -- the tool claimed to
  serve `s3://opal-data-bd/platinum/advisors/A123/summary.json`, a path the router 401s. A protective control
  rendered invisible. FALSE-SECURE.
- a **firm-parametric origin** (router picks the bucket per requesting firm) was reported as ONE FIXED bucket --
  naming a specific firm's bucket for a per-firm path.
The fix PARSES the routers (`extract_routes.py` +376) and adds RULE_REFUSE + firm_parametric outcomes.

## LIVE VERIFICATION (behavior on the running tool -- both directions)
**(1) PII path -> REFUSES 401 (was false-secure RESOLVED):**
`/api/scoped/advisor-intelligence/platinum/advisors/A123/summary.json` ->
  "REFUSED: the router returns HTTP 401 ... Platinum summary files must be accessed through the API, not
   S3-direct. S3 key: NONE ... Reading a resolution here would be FALSE-SECURE: the block is the whole point."
The tool now NAMES the false-secure hazard it used to commit. Fixed.

**(2) OVER-REFUSE CONTROL -- the narrow compound condition holds (does NOT block non-PII platinum):**
`/api/scoped/advisor-intelligence/platinum/firm/partner_analytics.json` ->
  resolves `S3 key: platinum/firm/partner_analytics.json` (NOT refused), but
  "S3 URI: REFUSED -- FIRM-PARAMETRIC: the router picks the bucket per requesting firm (opal-data-{firm}), so no
   single s3:// URI is correct. ask for the firm map, not a resolved bucket."
So the 401 is NARROW (PII refuses, non-PII platinum still resolves its key -- the compound endsWith-summary.json
AND platinum/advisors|clients condition works, no over-refuse) AND the CROSS-FIRM claim holds: the tool declines
to name a single firm's bucket rather than falsely emitting one. Firm separation preserved.

**(3) firm-parametric on the bare path** (earlier trace): `/api/scoped/advisor-intelligence/platinum/summary.json`
-> "REFUSED -- FIRM-PARAMETRIC" (no bucket named). Same firm-safe behavior.

**Suite:** test_routes_trace_discriminates.py 36/36 (was 27; +9 for R2+R3 incl. the mutant directions).

## Closes a tick-42 residual (the coverage line I read then)
At tick-42 comp-routes' own BLIND line said: "the public-data-router and shared-advisor-router rewrite rules are
TRANSCRIBED from the routers' if/else chains, not parsed ... a router edit not mirrored is invisible." This fix
PARSES them (Rule 22a: it resolved live CloudFront EVTSA9VEHNZVH -> shared-advisor-router:23 and downloaded THAT
source to parse). The transcription-drift residual is closed -- a router edit is now picked up, not silently missed.

## Scope of my claim (stated, not glossed)
I verified the PARSE **behaviorally** on the PII / control / firm-parametric paths (correct REFUSE / RESOLVE /
firm-parametric outcomes). I did **NOT** do an exhaustive rule-by-rule diff of the parsed output vs the full
router source (index.mjs) -- so "the parser faithfully reproduces EVERY router branch" is behavior-verified on
these paths, not exhaustively proven. The three paths exercise the defect + both refuse kinds + the over-refuse
control, which is strong; an exhaustive parse-vs-source diff would be a scoped follow-up if wanted.

## Probe honesty (s.6b, twice this turn)
Two malformed probes, both caught by reading the OUTPUT not the empty/error: (a) I dropped the leading slash to
dodge MSYS -> "No match" (CloudFront patterns need the `/`); (b) `MSYS_NO_PATHCONV=1` broke the LAUNCHER's own
`/c/...` path -> `C:\c\...` (the "never for the launcher" class, CLAUDE.md). The working form is the plain
leading-slash arg + the tool's own mangle-guard (which self-corrects and PRINTS the corrected path). Recorded so
the next agent tracing a `/api/...` path uses the guard, not MSYS_NO_PATHCONV.

## Compiler Tools
`comp-routes trace` x4 LIVE (PII refuse / over-refuse control / firm-parametric / probe-mangle diagnosis) ·
pytest test_routes_trace_discriminates 36/36 · `git show b9f80e6da` (parse+REFUSE+firm_parametric scope).
Gap found: none in the fix. Two malformed probes of my own, caught pre-report.
