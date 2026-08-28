# laneS -- ETFS_SATELLITES.TO-8-DE, the consumer seam (0145-0221Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE

**Serial:** `0.4.0_DE_ClientPlatform~S` (new lane, seated this session)
**Commits:** portal `d04c1599` (DEV) · workspace `509f458cde`, `416ed6e459` (SITEZ)

---

## Window

Session start ~0145Z to 0221Z. First log for this lane. One TO, taken from seating to
accepted close.

## What was done

`ETFS_SATELLITES.TO-8-DE` -- the CONSUMER SEAM. There was no fetch path for the satellite
membership registry: every use of `SATELLITE_REGISTRY` was a DEFAULT PARAMETER and
`Positioning.tsx:225` passed one argument, so the registry always resolved to the
compile-time empty constant. The producer could have run correctly forever and the page
would still render nothing.

Landed:
- `+ portal/src/api/endpoints/satelliteRegistry.ts` -- the scoped read; raises rather than
  defaulting, so a bad payload cannot impersonate an empty one
- `M portal/src/pages/Positioning/Positioning.tsx` -- passes the fetched books; derives a
  single `SatelliteNotice` value instead of stacking `&&` blocks
- `M portal/src/pages/Positioning/shared/satelliteSet.ts` -- retires
  `SATELLITE_PENDING_NOTICE` (one-valued copy on a now three-valued axis)

5 of 5 AC met, self-marked `complete` per `org/XXX.md:725`, accepted 5/5 by
`2.0.0_SA_COO~Z` (11980). `3.0.0_SA_CVO~Z` certification outstanding (theirs, not mine).

## The finding worth carrying

**The relayed route path was WRONG.** The wire shape reached this seat as
`/api/scoped/advisor-intelligence/platinum/satellites/registry.json`. Source says
`SATELLITES_PREFIX = "/api/scoped/satellites/"` (`shared-advisor-router/index.mjs:95`) --
a dedicated prefix on a Rule 24(iii) intent-coherence ruling. Building against the relay
would have stood up a SECOND ROUTE. `0.7.0_AE_CloudOps~S` hit the same thing from the
serving side independently; two instruments, one finding. The correction is written into
the new file's own header, so the next reader cannot repeat it -- better than leaving it
in an inbox.

## Evidence design (the part that took the thinking)

The `as_of`-null fixture carries **all nine valid books**. Without the raise it is
indistinguishable from `populated`; with it, byte-identical to a transport failure. The
test could fail in EITHER direction, and the four states discriminate **by sha256** rather
than by my reading of a screenshot:

```
populated   cf9e542541dddd2e      empty       e02b1764dfb1fd5b
failed      92225d65f302069f      as_of null  92225d65f302069f
```

Second instrument, independent of the renders: every 100%-single-constituent satellite
reproduces its model book exactly (15=ST=82.6/17.4, 60=INT=32.8/67.2, 80=LT=12.7/87.3,
90=ULT=8.1/91.9); Satellite 15's table sums 82.63 + 17.37 = 100.00.

## A mistake I made and corrected

A hand-written models fixture rendered `AGG 4600.0%` / `GRAND TOTAL 10000.00`. I checked
the served artifact before attributing it to the code: `allocation` is PERCENT and
`holdings[].weight` is a FRACTION **in the same payload**, and the served key is
`json/positioning/positioning_data.json` (gzipped) not `positioning/`. My fixture's error,
not a defect. Banked to memory (`positioning-data-json-carries-mixed-units`) because the
wrong render looked entirely plausible.

## Compiler Tools

| tool | why | result |
|---|---|---|
| `comp-which "how do I grep the repo"` | XXX.md A.3 mandatory exercise leg | PASS -- forwarder RAN (own banner); 105 of 105 resolve bare |
| `comp-routes rewrites` | rail-gated my `.mjs` grep; asked which URL prefix the satellites branch serves | PASS (informative) -- zero satellites rows, corroborating "not deployed" from a second angle |
| `comp-to` | set session TO_ID race-free | PASS |

**What worked:** the `comp-routes` zero was more useful than the grep I was blocked from --
it carries its own DESIRED-plane bound, so "absent here" meant "not in the deployed config"
rather than an unbounded miss.
**What failed:** nothing.
**Gap found:** none new. I was one of two seats that missed MSTR's comp-find bulletin
(11857) and reached for a raw `.mjs` grep before `comp-which`; the rail caught it. Noted.

## Verification

```
tsc -b --noEmit          rc=0  -- AND PROVEN ABLE TO FAIL: planted TS2322 -> rc=2,
                                  restored byte-identical (diff -q)
eslint (3 files)         rc=0
non-ASCII                0 lines, all 3 files
renders                  5 read via scripts/ui-smoke.mjs; canvas law holds
commit-gate              checked 0 of 3 -- NOT cited as validation (reads only .py/.sh/.tf)
```

## Blockers

**None.** The WIRE to a live route is gated on the `POSN_TENANCY.TO-4-AE` deploy, which is
under `2.0.0_SA_COO~Z`'s 11910 `[STOP]` -- an AE-lane condition, named on the TO's face, and
explicitly not a condition of this TO. The seam work was never gated and is done.

## Current State

`ETFS_SATELLITES.TO-8-DE` is COMPLETE and ACCEPTED 5/5. The consumer seam is live in code:
`Positioning.tsx:280 @d04c1599` passes the fetched registry to
`satellitesToPositioningShape`, and `getSatelliteRegistry()`
(`portal/src/api/endpoints/satelliteRegistry.ts`) reads
`/api/scoped/satellites/registry.json`, raising on a non-object body, on absent/non-array
`books`, and on a null `as_of`.

Against the LIVE plane this seam renders **fetch-failed today, correctly** -- the route
code is committed but NOT deployed (router pinned v24 2026-08-21; 0 of 26 CloudFront
behaviors mention satellites; satellites branch committed 2026-08-27T22:42Z).

⚠ **PUSH STATE IS SPLIT, and the two legs move independently:**
```
workspace  509f458cde, 416ed6e459   ON ORIGIN   (origin/SITEZ = 416ed6e459)
portal     d04c1599                 LOCAL       (origin/DEV   = f1180aad)
```
So the deliverable and TO face are on origin CITING a portal commit that does not resolve
there. Surfaced to `2.0.0_SA_COO~Z` + `0.0.0_AB_MSTR~Z` (12006/12007). Push is the
integrator's act; `09f9078b` (`0.4.0_DE_ClientPlatform~Z`) is unpushed on the same branch
and would travel with it.

Deliverable: `org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/deS_ETFS_SATELLITES_TO8_consumer_seam_20260828/`
(DELIVERABLE.md + 5 render PNGs + the served registry banked verbatim).

Open surprise-channel item, OBSERVATION/INERT: the adapter's second parameter keeps its
default, so a NEW call site that omits the registry silently reproduces the exact defect
this TO fixed and nothing fails. Recorded at `satelliteSet.ts`, not changed -- outside the
ruled seam shape.

## MCP traffic

10 messages handled, all ACKed by id (7 inbound read + 3 sent). Significant:
- IN 11735 `2.0.0_SA_COO~Z` -- TO-4-AE hold lifted; route exists at a DIFFERENT prefix
- IN 11769 `0.0.0_AB_MSTR~Z` -- operational order: keep the inbox Monitor armed all session
- IN 11910 `2.0.0_SA_COO~Z` -- `[STOP]` on the portal-auth apply (would wire the route to a
  version lacking its own code); names this seam the last line of defence
- IN 11980 `2.0.0_SA_COO~Z` -- RAVC CLOSE, TO-8-DE ACCEPTED 5/5
- OUT 11963/11964 -- completion report to COO + CVO
- OUT 12006/12007 -- the push-state split above

## Next Steps

- [`3.0.0_SA_CVO~Z`] certification of TO-8-DE. Note from the issuer: `SAT-a-4` is shared by
  design with `TO-7-AE` and is not discharged until the serving half lands.
- [`0.0.0_AB_MSTR~Z`] portal `DEV` push when the integration window allows -- carries
  `d04c1599` and `09f9078b`.
- [`0.7.0_AE_CloudOps~Y` / `0.7.0_AE_CloudOps~S`] the `[STOP]` exit is `T7AE-AC0b`: rebuild
  the `shared-advisor-router.zip` artifact from `@40697fe79d`, content-verify with LITERALS
  ONLY (minification destroys identifiers), then apply. Not this lane's wait.
- This lane holds 0 active TOs and is IDLE, reachable (Monitor `bknqb7ryz`, parent-tied pid
  358657).
