# ANDREW-DIRECT 2026-10-09 ~02:4xZ -- at the `0.0.0_AB_MSTR~Z` terminal (site Z): the CLAUDE.md egress law edit

## The question put to him (verbatim, as asked)

> **Change CLAUDE.md's egress rules to match your ~01:5x word? yes/no**
> CRO~Z recorded you saying: "infinite egress on all channels now (aside from BBG which goes through its queue logic)".
> CLAUDE.md still says "Excluded: all egress off Opal infrastructure" and "NEVER call an external vendor API without
> Andrew's explicit per-use word". CLAUDE.md's lock rule needs your express order before anyone edits it.
> REC: yes. I'd replace those two lines with: egress is open on every channel except Bloomberg, which runs only through its
> queue; per-user entitlement scoping waits until another MCP user connects. I'd cite your record, commit, and broadcast it
> to every box.

## His word, verbatim and entire

> yes

## The substance it adopts

His ~01:5xZ words at the `4.0.0_SA_CRO~Z` terminal, recorded verbatim in
`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261009_015xZ_OPAL_STAFF_MAY_READ_BLACK_DIAMOND_THROUGH_GATEWAY.md`
@0035550443:

> "and by the way infinite egress on all channels now (aside from BBG which goes through its queue logic).
> the point is that we can always work on per user entitlements later, nobody uses mcp right now aside from alyssa and
> she's fine.
> do not hold up progress or work about theoretical users that arent even connected and we'd apply entitlement scoping
> at that time, not now"

## The edit this record orders (CLAUDE.md "Agent Autonomy", nothing else)

- "**Excluded: all egress off Opal infrastructure.**" becomes: egress is open on every channel; the one exception is Bloomberg,
  which runs only through its queue logic.
- "**NEVER call an external vendor API without Andrew's explicit per-use word** -- availability is not authorization." and its
  box-memory pointer become: a Bloomberg pull goes only through its queue; any other vendor API needs no per-use word;
  per-user entitlement scoping waits until a further MCP user connects. Pointer: this record and the CRO~Z record above.
- No other rule changes. The "Human confirmation ONLY for" list (recursive deletion, destructive git, dropping tables/S3
  deletes, stopping EC2, anything unrecoverable) is unchanged.

## Exact text (CLAUDE.md, Agent Autonomy, lines 268-271 at box/sitez HEAD)

Replace:

```
**Excluded: all egress off Opal infrastructure.** Human confirmation ONLY for: recursive deletion, destructive git,
dropping tables/S3 deletes, stopping EC2, anything unrecoverable.
- **NEVER call an external vendor API without Andrew's explicit per-use word** -- availability is not authorization.
  Record: box memory `feedback_availability_is_not_authorization_vendor_egress` (per-device, not in the repo).
```

with:

```
**Egress is open on every channel, except Bloomberg.** Human confirmation ONLY for: recursive deletion, destructive git,
dropping tables/S3 deletes, stopping EC2, anything unrecoverable.
- **A Bloomberg pull goes only through its queue logic, never ad hoc; any other vendor API needs no per-use word.** Per-user
  entitlement scoping waits until a further MCP user connects. Order:
  `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261009_024xZ_LAW_EDIT_CLAUDE_MD_EGRESS_OPEN_EXCEPT_BBG.md`.
```

## Who commits it

CLAUDE.md sits in owned-paths lane BASE_EXEC (CTO, COO, CVO); `0.0.0_AB_MSTR~Z` is refused there (safe-commit, 02:5xZ) and
does not take the audited author override. The edit is committed by a permitted seat, `1.0.0_SA_CTO~Z`, with this file as
`ANDREW_LAW_EDIT_ORDER`. The broadcast to site Z's live seats and to the laptop, dell1 and dell2 managers follows its commit,
by `0.0.0_AB_MSTR~Z` as relay, with the push state stated.
