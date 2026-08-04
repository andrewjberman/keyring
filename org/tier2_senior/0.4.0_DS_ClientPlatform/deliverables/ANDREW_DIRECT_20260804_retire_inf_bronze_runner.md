# ANDREW-DIRECT RULING: retire the inf-bronze-runner EC2 leg (R-1 arbitration resolved)

**Channel:** Andrew direct at the 0.4.0_DS_ClientPlatform terminal
**Time:** 2026-08-04 ~01:4xZ
**Recorded by:** 0.4.0_DS_ClientPlatform (same turn, verbatim, per org/XXX.md Andrew-direct law)

## VERBATIM

Context: after walking the R-1 dual-writer lineage (six inf dim feeds written by BOTH the
per-dim Lambdas AND the EC2 orchestrator), the Orion auth chain (JWT minted on the
inf-exporter box, consumed at run time by the Lambdas), Andrew said:

> "The lambda pattern is lighter/better, and surely the way this should be done, just
> need to clarify how they authenticate"

then, after the auth clarification and the exporter-device walkthrough:

> "ok great, so that means we can get rid of the EC2 run, whichever one this is
> i-083ad9ae297f88e9f"

## SCOPE (surfaced, not adjudicated -- the receiving agent does not adjudicate)

- The instance named is **inf-bronze-runner (i-083ad9ae297f88e9f)** -- Writer B of the
  registry's R-1 named risk. NOT the auth capture box (inf-exporter i-081ae6aafb394fb1a).
- Read as: the R-1 arbitration question ("single writer, or distinct keys per producer")
  is RESOLVED in the retire-Writer-B direction -- the Lambda leg becomes the sole writer
  of the six dual feeds. This is the exact decision OPAL_VENDORPROVENANCE.BR1
  (@eb8e263397, staged) was chartered to brief; the ruling arrives ahead of the brief.
- Engineering reality surfaced to Andrew in the same exchange (not pushback -- the safe
  execution path): the box carries TWO non-duplicated loads that must be rehomed BEFORE
  retirement: (1) the Eclipse pull (pull_eclipse_portfolios.py, boot-dispatch only;
  permanent-gap vendor class -- any cutover miss is unrecoverable), (2) the
  _BRONZE_COMPLETE.json sentinel (the silver chain + inf-assets-trigger/gold-runner fire
  on it; the dim Lambdas do not emit it).
- Execution shape (sequencing, gates, who builds the Eclipse rehome, sentinel re-source
  vs trigger re-point, the final stop/teardown) routes through COO/CTO per normal law;
  a begun cutover finishes or rolls back (NEVER#7 discipline).
