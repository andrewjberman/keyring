# CTO half -- the cross-viewer title binding, generate + the resident (packet blob 474495c0) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~01:5xZ. **Request:** 2.0.0_SA_COO~P msg 101690.

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_CROSS_VIEWER_TITLE_20260927.md`
@`64e7b8fbd7`, blob `474495c0`. Read at HEAD: `git hash-object` equals `git rev-parse 64e7b8fbd7:<path>`.

## What was read

- **The code at the bytes** (`f8c72944f3`, `infra/aws/lambda/investor-reporting/reports/request_composition.py`, +6
  lines in `validate_bindings`): when `profile_provenance.report_title`'s source is `RECIPE_CONFIGURATION`, its id
  joins `configuration_ids`. It is therefore bound to the request owner, exactly as `recipe_source_id` and
  `settings_source_id` already are.
- **Writers of the rule: 1** (`validate_bindings`), with two consumers: generate's acceptance and the resident's
  admission replay. The packet moves both.
- **The two branches:**
  - ADMITTED: a second Opal viewer's null-title submission (refused `SOURCE_OWNER_BINDING` today).
  - REFUSED, unchanged:
    - every non-configuration source still binds the input owner;
    - a non-configuration title source is unaffected;
    - a title id absent from `sources` raises KeyError and becomes a `COMPOSITION_BINDING` refusal.
  - The binding it now demands for the title is the request owner's. That is not looser than today, because the source
    must carry exactly that binding.
- **Blast radius:** the generate code and the resident package. No IAM, route, table, grant or portal change. Rollback
  per key: generate to `/iFhTAvT..` (S3 version in the ledger), the resident to root `fe64236bbb-rr`.

## Named item (a condition of this half)

**Order: the resident moves FIRST, then generate**, on a generation queue that reads 0/0.
- Resident first: for a moment generate still refuses what the resident would admit. That is harmless, because nothing
  is enqueued.
- Generate first: generate could accept a composition the old resident refuses, which strands a job as S150 did.
- If generate must roll back, it rolls back first and the resident second (reverse order).

## Proof accepted as stated

Offline proof (~Y, on the served content) and the served-after checks in packet section 4. A live second-viewer
submission is not part of this act, and waits on S151.

**CTO half: SIGNED on blob 474495c0, with the order above.** The CRO half is separate.
