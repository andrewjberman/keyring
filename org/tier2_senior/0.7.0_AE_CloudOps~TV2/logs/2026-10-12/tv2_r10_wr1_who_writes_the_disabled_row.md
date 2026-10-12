# Who writes the disabled tooling row: its own tool, not a sign-in attempt — 0.7.0_AE_CloudOps~TV2

**archetype:** READ (investigation)

**Date:** 2026-10-12
**Task Order:** TCKT_VNEXT.TO-READ-R10-wr1.who-writes-the-disabled-tooling-row-dell2 (read at `6d4355d22d`)
**Status:** COMPLETE — AC1 `WR1-READ-OK`, verdict `A_TOOL_REWRITES_ITS_OWN_ROW`

---

## The answer the CTO is waiting on, first

**Not a sign-in attempt on a disabled identity.** Zero disabled-account refusals in all three windows,
each against a control that matched. The writes are the UI walker's own tool arming its row to **active**,
signing in successfully during the walk — *that* is what writes `updatedAt` — and disarming it again.

### The chain, in the order it decides

1. **The identity is that account.** `SKILL.md:29` names the row by key and address and states it rests at
   `status disabled` with a hash nobody knows, role admin, internal, `Dev` — matching the row as read.
2. **The tool's own three writes never touch `updatedAt`.** `arm`'s lease (`:136`, `armedBy`/`armedAt`),
   `arm`'s activation (`:151`, `passwordHash`/`status`), `disarm` (`:185`, `passwordHash`/`status`, removing
   the lease). **None sets `updatedAt`** — which rules the tool out as the *direct* writer of the witness.
3. **But `arm` makes the row active** for the length of one walk.
4. **A successful sign-in is the only writer of `updatedAt` in the sign-in source:** `db.ts:271-284`,
   `SET lastLogin = :now, updatedAt = :now`, one call site — `auth.ts:204`, inside `mintSession`.
5. **A disabled row can't reach it.** The guard at `auth.ts:106` precedes `204`, so a *refused* attempt
   cannot move `updatedAt` by this path.
6. **`lastLogin == updatedAt` exactly.** One statement sets both to a single `:now`, so the last write *was*
   that statement — a minted session — and the row must have been **active** at that moment.
7. **Zero disabled refusals**, controls 108 / 72 / 40.
8. **Exactly one wrong-password refusal per window** — the signature of `disarm`'s own proof-of-refusal
   login (`:202-206`, which escalates if the login is *not* refused).
9. **The row is at rest:** `status=disabled, armed=no, armedBy=none` — a cycle completed.
10. **Nothing schedules it.** 156 EventBridge rules, no unread page, 0 naming a walk; no crontab; 0 of 513
    `.tools` files. A **tool** runs as it, invoked by a seat, on Andrew's own direction of 2026-09-26.

**A third write the order didn't name:** `updatedAt` now reads `02:01:48.268Z`, after my own round-9
re-read had confirmed `01:03:31.142Z` unchanged. Three writes known; with no stream, only the ones my reads
straddled are visible.

---

## The honest limit

The row carries no actor field. I can show a **successful session was minted while the row was active**, and
that the walk password lives only in SSM and is read in-process by the walker — but not *which client*
authenticated. A sign-in log line naming the client, or the SSM parameter's access record, would close it.
I counted log lines and never printed them, so no actor was extracted.

---

## Two instrument faults of mine, both caught

**PITR.** I wrote `point_in_time_recovery: DISABLED` into the file *from assumption*, then read
`describe-continuous-backups` and found it **ENABLED**. The correction matters: PITR enabled means the row's
prior **states** are recoverable — the most informative read still available — though it still names no
actor. The file now carries the measured value, says I had assumed the other, and records the restore as
forbidden here and not performed.

**The EventBridge control caught itself.** `--query length(Rules)` printed **100 and then 56** — page
counts, the exact trap CLAUDE.md names for paginated `list-*`. Worse, the server-side `contains(Name,'walk')`
filter ran *per page*, so a matching rule on page 2 could have been dropped silently. Counting client-side
over the auto-paginated 156 with no `NextToken` removes both faults.

Also: my first workspace search with a head limit of 60 returned exactly 60 — a page. Unlimited: 100.

---

## Compiler Tools

| Tool | Command | Result |
|------|---------|--------|
| get-item (no projection) | the one row, consistent | 13 attribute names; the third write |
| the ui-walk skill + script | lines 25-45; every write path | **none of the three writes sets `updatedAt`** |
| comp-find | the write commands, then `updateLastLogin`, both pages | 28 hits / 13 files; one real call site |
| position computation | call site vs the three guards | 106 precedes 204 → unreachable when disabled |
| the equality test | `lastLogin == updatedAt` | **EQUAL** — identifies the writing statement |
| metric + logs ×3 | control first, then quoted patterns | 0 disabled refusals; 1 credential refusal each |
| Grep (repo root) | one search, re-run unlimited | 100 files, no schedules |
| events list-rules | auto-paginated, filtered client-side | 156 rules, 0 matches |
| describe-table / -continuous-backups | one read each, nothing changed | no stream; **PITR ENABLED** |

**What worked:** the equality test. "Who wrote it" looked unanswerable without history — but
`updateLastLogin` is the *only* statement that sets both fields, and it sets them to the same value, so the
row's own two timestamps being equal identifies the writer without any history at all.

---

## Decisions Made

1. **Reported the reassuring direction first, with the evidence that earns it** — the CTO is waiting on
   whether this was a sign-in attempt, and it was not.
2. **Did not run `arm`, `disarm` or `secret`;** ran `status` exactly once, as permitted.
3. **Did not restore,** and named PITR as an available-but-unused instrument with its limit (state, not
   actors) so the next seat isn't left to rediscover the option.
4. **Corrected the PITR value I had assumed**, and said in the file that I had assumed it.
5. **Recounted EventBridge client-side** once the control exposed page counts.
6. **Stated the actor limit plainly** rather than letting "a tool did it" imply the client was identified.
7. **Filed no surprise row.** Everything here resolves my own earlier row `S54`; the one oddity found (the
   skill's SSM-deletion wording) belongs to that skill's owner, not this project's channel, and is recorded
   as an observation.

---

## Files Modified

| File | Commit |
|------|--------|
| `deliverables/r10_wr1/WHO_WRITES_THE_DISABLED_TOOLING_ROW_20261012.json`, proof_of_spec, this log, TO status | this commit |

No AWS write, nothing invoked, nothing enabled, no ledger entry.

---

## Blockers

None owed by this seat. Row `S54` is answered by this read; its disposition stays the CTO's.

---

## Current State

The disabled tooling row moves because its own tool arms it, signs in, walks, and disarms it. The witness
field is written by the walker's **authorised** session, not by anyone's refused attempt. No schedule runs
as that identity; a seat invokes a skill. The account is at rest now: disabled, unarmed, lease returned.

---

## Next Steps

1. `1.0.0_SA_CTO~DELL2` dispositions row `S54` on this read.
2. If the authenticating client must be named, that needs a sign-in log read or the SSM access record —
   neither is in this order, and a PITR restore would not answer it.
