# SURFACE: end-to-end trace brief

<!--
/closer TRACE brief template. One brief per product surface (a tab, a report, a feed).
Author: 4.0.0_SA_CRO or any Tier-1 seat. Home: the author's deliverables/ folder,
named SURFACE_END_TO_END_GAP_BRIEF_YYYYMMDD.md.
Worked example: org/tier1_exec/4.0.0_SA_CRO/deliverables/PERFORMANCE_END_TO_END_GAP_BRIEF_20260922.md
Replace every CAPS placeholder. Delete this comment before committing.
-->

Prepared by SERIAL on YYYY-MM-DD. Read-only assessment plus proposed closure requirements; no application changes,
vendor calls, deployment or schedule activation. (Change this line if any of those happened, and say which.)

## Design finding

What the surface is meant to do, in plain terms: which provider or data source supplies which number, what Opal
retains, what it transforms and what it must never compute. Then one paragraph on how far the implementation is
from that design, naming the work worth keeping and the connections that are unfinished.

## Current measurement

Read from DEPLOYED bytes, not source: at HH:MM:SS UTC, WHAT WAS DOWNLOADED (function, layer, bundle), its code
digest, and whether it matches source at WORKSPACE_PIN / PORTAL_PIN. Active handler, relevant configuration values
(for example a transport mode), last-modified dates. What was NOT invoked.

A configured endpoint, token path or secret name is not an executed connector. Say which you measured.

Machine-readable evidence: PATH_TO_EVIDENCE_JSON

## Adapter map

| Surface / firm | Provider and intended endpoints | Existing work | Gap |
|---|---|---|---|
| ROW_1 | PROVIDER: METHOD /path; auth route | parsers, recorded responses, helpers that exist | what is missing to make a real request travel |
| ROW_2 | ... | ... | ... |

One row's success does not certify another's. Say so where tenants or providers differ.

## Start-to-finish walk

<!-- One section per hop, from the user's first action to the rendered screen (and on to export if in scope).
     STATE is exactly one of: WORKS | INCOMPLETE | MISSING | MISMATCHED.
     Each hop: what exists (with paths), the exact mismatch (field names, carriers, shapes), then ONE Close: line. -->

### 1. A -> B -- STATE

What exists: `path/to/file.py` (`function`), `path/to/Component.tsx`. What each side sends and expects.

The exact mismatch: SIDE_A sends X in CARRIER; SIDE_B reads Y from CARRIER_2.

Close: the one change that makes this hop carry the real request, and the proof that shows it did.

### 2. B -> C -- STATE

...

Close: ...

### N. Y -> screen -- STATE

...

Close: ...

## LGIC (only when the delta adds storage or names)

<!-- Delete this section if no Close: line adds an S3 address or a resource name. -->

Every new address is `lib/opal_naming.py` `address(source, scope, tier, table, partition, object)` output and every
new resource name is `name(system, scope, function, kind, qualifier)` output (CLAUDE.md Rule 30). Tier home and tenancy
per `infra/logic/02_DOCTRINE.md`. A builder refusal is a missing row under `infra/logic/registry/`, named here with its
owner. A deliberate departure is an R20 register entry for Andrew to acknowledge.

| Close: line (hop N) | Builder call | Output | Registry row needed |
|---|---|---|---|

## Recommended completion sequence

1. **The live thread.** One named person, one journey, coarse resolution (one firm, one account, default window, no
   export), on the DEPLOYED stack, through the shared first hop (auth, scope, bootstrap) to the rendered screen,
   recorded as ONE trace artifact. Name which hops above it crosses and which seat owns the first hop.
2. STEP -- the next enrichment the user gains.
3. STEP ...

## Acceptance

One reconciled trace per case, each following one request from the user's selection through the provider request,
raw response, normalized object, rendered screen (and export, if in scope). The surface is complete when these traces
reconcile, not when parsers pass fixture tests.

Cases: FIRMS x SELECTIONS x WINDOWS x FAILURE CASES (expired session, missing mapping, missing history, changed
permissions ...).

## Evidence anchors and limits

Source inspected at workspace WORKSPACE_PIN and portal PORTAL_PIN; shared work may advance concurrently. What was
verified fresh, and what was not (for example: no signed-in UI walkthrough, no live provider call).

- `path/one`
- `path/two`

## Andrew-direct request -- verbatim record

Channel: WHERE (terminal, relayed message id), date, time if known.

> ANDREW'S WORDS, VERBATIM.
