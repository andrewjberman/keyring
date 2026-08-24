# Banked cleanup items -- 0.4.0_DE_ClientPlatform

Low-priority, no-clock items noticed during scoped work and deliberately **not chased** at the time
(surprise-channel discipline: surface, take no action, keep working). Each carries what was
**measured** vs what was **inferred**, so a later seat does not have to re-derive it.

Pick these up when touching the file for another reason, or when explicitly tasked. **Nothing here
is a TO and nothing here is urgent.**

---

## 1. Stale "DEMO MODE / no auth" comment on the Positioning data read

**Andrew-direct 2026-08-21: "make a note to clean up that comment at some point."** No clock.

**Where:** `portal/src/api/portal-proxy.ts:1073-1078`, in the `getPositioningData()` doc block.

**What it says, verbatim:**
> `DEMO MODE: Using public endpoint (no auth) for demo purposes`
> `TODO: Revert to shared endpoint for production:`
> `  Path: /api/general/positioning/positioning_data.json`
> `  Auth: JWT Bearer token (tier-filtered: internal + advisor only)`
> `PUBLIC DATA (DEMO): No auth required`

**Why it needs cleaning, and it is NOT an auth defect:** the comment and the deployed route disagree.
CloudFront behavior 20 `/api/general/*` carries `viewer-request: auth-validator-edge`, and the path
the comment names as the "revert to production" target is *the path the code already uses*. So the
comment describes a state that no longer exists and prescribes a change that appears already made.

**MEASURED vs INFERRED, stated so the next reader does not over-trust this note:**
- MEASURED: the comment text (source read); CF behavior 20 carries auth-validator-edge
  (`comp-routes behaviors`).
- **NOT MEASURED:** an actual unauthenticated fetch. `comp-routes` is DESIRED plane by its own
  header, so "the route carries auth" is a declared fact, not an exercised one. **Do not upgrade
  this note into "the endpoint is authenticated" without firing the request.**

**The risk it carries while it sits:** a seat reading that block during Positioning work could
reasonably conclude the page is served from a public, unauthenticated endpoint and make a decision
on it. That is the whole reason it is worth a cleanup rather than being ignored -- the defect is a
*false belief in a reader*, not a hole in the serving path.

**Also in the same block:** a non-ASCII marker at `:1073`, against the CLAUDE.md code-quality rule
(no non-ASCII in production code). Pre-existing; fix it in the same pass if the block is touched.

**Suggested fix when someone is in there:** delete the DEMO/TODO framing, state the current
posture, and cite the behavior rather than asserting an auth claim the comment cannot verify --
e.g. "served via `/api/general/*` (CF behavior 20, viewer-request auth-validator-edge); resolve the
posture live rather than trusting this line." A comment that tells the reader where to look ages
better than one that tells them what is true.

*Origin: noticed during the ETFS_POSITIONING plane (f) pre-cell read, 2026-08-21. Banked to COO in
the same turn (msg 65652) as a surprise-channel line.*
