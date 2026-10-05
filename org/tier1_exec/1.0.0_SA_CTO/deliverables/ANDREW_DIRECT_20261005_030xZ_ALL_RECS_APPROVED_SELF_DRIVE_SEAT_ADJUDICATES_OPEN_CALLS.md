# Andrew-direct 2026-10-05 ~03:0xZ -- "all recs approved" on three cards; the self-driving seat adjudicates its own open calls

At the `1.0.0_SA_CTO` terminal, answering this seat's `/open-calls` frame (3 cards, ~03:0xZ). VERBATIM:

> "all recs approved. Also please note, your /self-drive skill must handle open calls at this seat. please note the skill
> details; you are the adjudicator when that skill is running. As a result, I should never see available open calls at this
> seat unless open calls have arisen post-selfdrive tick and pre-the next selfdrive tick."

## The three cards, as approved

| card | the REC he approved | executor |
|---|---|---|
| 1 | YES: delete `s3://opal-data-portal-v2/platinum/advi/49financial/perfrp_performance_account.json` (one key; versioned; ETag/VersionId stop; rollback by the delete marker). CTO half @4a63c9b600, COO half @48fa2860ab | `2.0.0_SA_COO~P`, then both after-reads, then W121-S1 disarms |
| 2 | YES: restart EC2 `i-02448edb624a7a7cf` (mdpf-daily-runner; stopped "User initiated (2026-10-04 16:41:18 GMT)"). This lifts his 2026-10-03 ~17:3xZ data-engineering hold for this one start only | `2.0.0_SA_COO~P` under a change ledger; `2.0.0_SA_COO~M` informed (the runner carries the MDPF daily chain and stage 6d) |
| 3 | NOT YET: PROD `/investor-reporting` stays admin and Dev only (his 2026-09-22 gate). After the directory refresh runs, one named test advisor | none; the gate stands |

## The standing instruction (scope, verbatim reading)

While `/self-drive` is armed at this seat, the seat is the adjudicator of every open call in its scope (`/self-drive` Step 1).
His `/open-calls` at this seat shows a call only if it arose after the last tick and before the next. Applied as:
- `.claude/skills/open-calls/SKILL.md`: section "At a seat running /self-drive";
- `.claude/skills/self-drive/SKILL.md` is unchanged: it is over its byte budget, may only shrink, and its Step 1 already makes the driver rule every call.

This binds this seat's `/self-drive` and `/open-calls`. It sets no gate on any other seat.

**Self-correction on record:** card 3 ("not yet") was a decision this seat should have ruled at its tick. Cards 1 and 2 are acts
only he can perform (CLAUDE.md Agent Autonomy "S3 deletes"; lifting a hold he set by name). Under the amended skill they print as a
cited act list, never as cards.

-- 1.0.0_SA_CTO
