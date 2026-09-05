# PROPOSAL -- an allocator coordinate in the surprise-channel row id (`<CODE>-(Z-)?(W<n>-)?S<k>`)

**Author:** `3.0.0_SA_CVO` (owner of the row schemas and the annex). **Status:** PROPOSAL, not implemented -- proposing
is legal, implementing waits for the owners' word (the gate and checker regexes are `1.0.0_SA_CTO`'s; whether this
falls inside Andrew's "the mechanisms right now" is his scope call, relayed by `4.0.0_SA_CRO` 94015 and not widened
here). **Rule 24 record:** the four postulates and the token census are below; without them this is not a proposal.

## The defect this removes

Spine v3 gives every worker its own worktree. The row gate is the id allocator and allocates against the index it
grades, so two indexes -- the main tree and a worker's worktree -- each mint "the next" id from one sequence, and the
drain merge does not re-run the allocator. Measured 2026-09-04: `NFRA_COMPEFFICACY-S34` names two rows (the CVO's
adjudication of S29 @b50a124783 at 01:46Z; worker `0.9.0_WK_NFRA_COMPEFFICACY~2`'s observation @e7dda3d93c at 03:46Z,
merged by the drain @46ff7f8c8a). The rollup resolved the worker's row to the CVO's dismissal; the gate kept it open.
Record: `NFRA_COMPEFFICACY-S37` @f357b84197.

Two remedies detect the collision after it exists (a cross-document uniqueness limb in the gate, `1.0.0_SA_CTO`; the
drain running the gate on the merged index before the merge lands, `2.0.0_SA_COO`, landed @e6351512fe). This one
removes the race: rows minted by different allocators cannot share a sequence, so no merge can collide two of them.

## The grammar

```
<CODE>-S<k>            a row minted in the main index by a seat (unchanged)
<CODE>-Z-S<k>          a row minted on site Z (unchanged -- the fabric coordinate, annex section 9)
<CODE>-W<n>-S<k>       a row minted in worker <n>'s worktree (NEW -- the allocator coordinate)
<CODE>-Z-W<n>-S<k>     site Z's worker <n> (composition; the coordinates nest fabric-then-allocator)
```

`<n>` is the worker's own suffix (`0.9.0_WK_<CODE>~<n>` -> `W<n>`); `<k>` restarts at 1 per coordinate. The pattern:
`^[A-Z0-9_]+-(Z-)?(W[0-9]+-)?S[0-9]+$`. The seat form is a strict subset of today's, so every existing id is valid
under it and nothing is renumbered -- including both S34s, which stay as they are and are cited by vintage.

## The four postulates (Rule 24)

1. **MECE over a declared domain.** The domain is *the allocator of a row*: the main index (seats), site Z's index,
   a worker worktree's index. Each row has exactly one allocator; the coordinate names it; a fourth allocator (a second
   site, a second worker fabric) extends the grammar by one coordinate and never overloads one. The uncovered member
   hunted for: a row a seat appends *inside* a worker's worktree -- ruled out by the gate's authorship check (the
   committer's serial must match `surfaced_by`; a seat does not commit under a worker serial), so a worktree's rows
   are the worker's by construction.
2. **Same grain.** One coordinate per row, minted once at the row's commit, never derived later and never changed.
3. **Intent coherence.** One axis, one intent: *who allocated this id*. It carries no class, no hazard, no disposition,
   no vintage (the vintage stays in the citation form `<id>@<commit>`); it is not a routing token and not an owner.
4. **State coherence.** No remedy moves an id. A disarm, a remediation, a correction and a dismissal are all NEW rows
   citing the old id, as today; the coordinate is inert to every state machine on the row.

## Token census -- every consumer of the id grammar (denominators printed)

Instrument: `comp-find` over `corpus=all` (148,424 files scanned) for the fabric-coordinate regex fragments, then
`comp-read --enumerate` on each hit for the exact line. Consumers that PARSE or VALIDATE the id:

| consumer | line | what it does | owner |
|---|---|---|---|
| `org/surprise_channel/schemas/investigation_item.schema.json` | `:18` `pattern` | validates `id` | `3.0.0_SA_CVO` |
| `org/surprise_channel/schemas/remediation_row.schema.json` | `:20` `pattern` | validates `id` (must equal the graduated item's) | `3.0.0_SA_CVO` |
| `.tools/surprise-row-gate.py` | `:78 ID_RE`, used `:533`, `:786` | identity check (project/fabric against the id); the allocator | `1.0.0_SA_CTO` |
| `.tools/proof-of-spec-check.py` | `:946 SURPRISE_ID_RE`, used `:1019`; comment `:943` "the id grammar is surprise-row-gate.py's ID_RE" | the `surprises` limb: an entry must open with a row id | `1.0.0_SA_CTO` |
| `org/surprise_channel/surprise-watch.sh` | `:80 ID_RE`, counted `:248` | the intake's row count and NEW ROW lines | the channel intake (`3.0.0_SA_CVO` uses it; authored on Andrew's word) |
| `.tools/comp-surprise.py` | no regex (`_project_of` by path `:48`; ids as strings) | the rollup resolves by id string -- unaffected by the grammar, affected only by uniqueness | `1.0.0_SA_CTO` |

Five files carry the grammar; three regexes and two schema patterns change in ONE commit (the gate reads the schema
from the staged index, and the checker's comment pins its regex to the gate's). Prose mentions (this seat's
`PROPOSAL_SURPRISE_CHANNEL_FABRIC_HOME_20260826.md`, the CTO's `CANONICAL_LOOP_REMEDIATION_DESIGN_20260902.md`, one
site-Z channel file, message archives) describe and do not consume.

## What the gate adds beside the grammar (the CTO's half, stated so the proposal is whole)

- A row committed under a worker serial `0.9.0_WK_<CODE>~<n>` must carry `W<n>` equal to the committer's suffix; a
  seat's row must carry no `W`. This is the same authorship discipline the foreign-row sweep already enforces.
- Cross-document uniqueness still applies WITHIN a coordinate (a worker cannot mint its own `W2-S1` twice); the
  detection limb and the prevention grammar are complementary, not alternatives.
- The annex (section 4's id row and section 9's "one investigation file per fabric") gains the coordinate in the same
  window, by this seat, as annex v3.2.

## What this proposal does not decide

Whether to adopt it at all (a lane grant for workers, item 3's open limb, is the larger act and may change how
workers commit); whether `<n>` should be the worker's slot number or a per-issuance sequence; whether the CVO's own
rows in `adjudications/` want a coordinate (`C-`) so an adjudication id can never collide with a worker's -- this
seat's inclination is yes, for the same reason, and it is stated as an inclination.

— 3.0.0_SA_CVO
