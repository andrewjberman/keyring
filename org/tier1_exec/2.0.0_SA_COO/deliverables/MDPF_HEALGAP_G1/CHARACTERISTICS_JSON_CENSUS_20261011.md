# Census: readers and writers of `platinum/satellites/characteristics.json` -- `2.0.0_SA_COO~G1`, 2026-10-11 ~08:4xZ

Input to the characteristics-producer re-time pair (CTO ruling ADDENDUM 3 @c3cc34f2d0, msg 3655: "counts every reader of
`characteristics.json` and every writer of the key (N printed)"). Instrument: `python .tools/comp-find 'satellites/characteristics\.json|characteristics\.json'
--files --all --band <B>`, corpus `all`.

**Denominator:** 351 hit(s) across 81159 file(s) scanned (HEAD / DEF / SURFACED / CONFIG bands; the TEST band read 354 across 81183,
three files added between the runs). 6310 ephemeral-floor and 5962 binary files are NOT searched. 3 unreadable. A zero in a band is
OUT-OF-CORPUS for those, not absence.

## First-party runtime files (deliverable folders, audit logs, `.scratch` and change-management records removed)

| role | file | note |
|---|---|---|
| WRITER (code) | `data/assets/scripts/gold/build_satellites_characteristics.py` | the producer; the Lambda wrapper calls it. Also runs as a CLI with `--as-of` (a DRIVEN run). |
| WRITER (trigger + grant) | `infra/aws/terraform/cot-pipeline/satellites-characteristics-producer.tf` | role `cot-satellites-characteristics-producer-role`, rule `cot-satellites-characteristics-producer-daily` `cron(30 12 * * ? *)` |
| READER | `infra/aws/lambda-edge/shared-advisor-router/index.mjs` | the edge router that admits the leaf |
| READER | `portal/src/api/endpoints/satelliteRegistry.ts` | the portal endpoint module |
| READER | `portal/src/pages/Positioning/shared/satelliteAdapter.ts` | the Positioning page adapter |
| TEST | `infra/aws/lambda-edge/shared-advisor-router/test/satellites-registry.spec.mjs` | not a runtime reader |

**N of readers (runtime) = 3. N of writers by grant: to be PRINTED from the live role policy at the pair** (the census reads literal text;
it cannot see an operator run under another principal, and it did not read the role's `s3:PutObject` statements live).

## Not read here

- Whether the consumers compare `holdings_as_of` to `as_of`, and whether a same-day basis is something any of the three requires.
- The producer's measured run duration and the new fire time: both come from the first 13:15Z fire (CTO: "read from HG-t-9's stamp-gated
  fire plus that fire's measured duration, not guessed"), which has not happened at the time of this file.
