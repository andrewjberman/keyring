# Ten crossbox orders closed, and a18's identity guard did its job -- 0.7.0_AE_CloudOps~ZC

**archetype:** MIXED

**Date:** 2026-10-11
**Task Order:** XB-20261011T055037Z-dea7, XB-20261011T055046Z-b8ec, XB-20261011T055148Z-00a7 (crossbox)
**Status:** COMPLETE on the two close-orders; a18 BLOCKED and reported, not served

Continues `zc_amgt_corpus_r44_at4_read.md` (same day, same lane).

---

## Objective

Three crossbox orders arrived together at 05:59Z. Two are bookkeeping from different issuers; one is a
read-only AWS act that a HELD ledger and a round-22 slug wait on.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| crossbox-call.py status | `status --id <id>` x10, before AND after the act | PASS | The only sound oracle here. My ack/close loop's own stdout was mangled (see below), so the state was read back from the tool rather than inferred from the loop. |
| comp-iam | not run | SKIPPED | The HUD advised `comp-iam service/gaps` over the raw `iam list-access-keys`. Declined deliberately: the question was "does this USER exist and hold an active key", and comp-iam models Lambda/EC2 operation-to-policy reconciliation, not IAM user key metadata. It would not have answered it. No `iam.tf` change this session either, so the AE minimum has no trigger. |
| raw aws (iam, sts) | `sts get-caller-identity`, `iam list-access-keys` x2 | PASS | Reads of one resource each -- the rail's FREE list. The second was a positive control in a SEPARATE invocation. |

**What worked:** reading state back from `crossbox-call.py status` is what kept a false count out of a
report.

**What failed:** my own ack/close loop. I wrote it with `tee /dev/stderr` plus a `grep -q` in the
condition, and its output came back with one id visible and a long whitespace run -- the CR-corruption
shape this device is known for. **The loop itself worked** (all ten landed); only its display lied. I
reported nothing from it.

**Gap found:** none in the tools. `crossbox-call.py` has `open/issue/ack/close/status` but no
reply-payload verb, so a reply to an order is a committed file plus a relay line. Worth knowing, not a
defect.

---

## Work Completed

### 1. Two close-orders, one act of ten

`2.0.0_SA_COO~C1`'s dea7 and `1.0.0_SA_CTO~DELL1`'s b8ec name the **same ten ids**. Read both bodies
before acting: it is one act of ten, not twenty. Had I worked them as two lists I would have run twenty
ack/close pairs and reported a number twice the truth.

The COO's order carries a condition -- "if your copy of any of the ten shows work you hold undone, do
not close it" -- so this was not a blind close:

| id | disposition | how I know |
|---|---|---|
| 7dd9 | SERVED | by me this session, evidence `2274227184` |
| 9452 | SERVED | by a prior ~ZC session, commit `f30441652f` |
| the other eight | SUPERSEDED duplicates of those two | both issuers say so independently, and AMGT_CORPUS is four rounds past round 40 |

All ten read `AWAITING ACK by 0.7.0_AE_CloudOps~ZC` before the act and `HALF-CLOSED (to only)` after.
10 of 10. The from-side is dell1's to record; the tool says so itself and the calls are not settled
until both sides are in.

Committed `361ed5c930`, scoped to exactly my ten paths. **23 crossbox files were modified in this
tree and 13 are other seats' acts** -- including two that were already dirty when this session started.
A `git add`-style sweep would have published them.

### 2. a18: the guard fired, and running past it would have been worse than useless

Step 1 read `arn:aws:iam::313476888478:user/Andrew_Berman` at 06:03:15Z. The order requires
`user/Opal_Terminal` and says STOP on anything else.

I did not run steps 2-3. The reason is not obedience: FWD-8's ADMITTED half asserts that the identity
*inside* the role's trust can read. `Andrew_Berman` is outside a trust naming exactly
`user/Opal_Terminal`, and a resource-based trust is not bypassed by a permissive identity policy -- so
the AssumeRole would have been refused and recorded as **"a18 ADMITTED read: AccessDenied"**. That reads
as the ADMITTED half FAILING. It would have planted a false negative against FWD-8 on the project's own
evidence trail, in the exact place the ledger is waiting.

Then measured, rather than theorised, so the issuer can route it:

| Question | Result |
|---|---|
| Identities this box can present | **ONE** profile, `default`. No `Opal_Terminal`, no `AWS_*` env override. |
| Does the trusted identity exist? | **YES** -- `Opal_Terminal`, 1 key, `Active`, created 2026-07-10T22:08:15Z |
| Is that read sound? | positive control on `Andrew_Berman` in a separate invocation: 2 Active keys |

So the order is servable; this credential store cannot serve it.

**I also closed off the order's own fallback rather than leaving it to be tried and fail.** It allows
`0.0.0_AB_MSTR~Z` to hand the cell to another live site-Z lane. That cannot work: every site-Z lane is
a session on this one machine under this one Windows user, so every lane resolves the same `~/.aws` and
re-reads the same Arn. The axis is the CREDENTIAL, not the lane.

Reply committed `088da62c7b`. The crossbox id is ACKED and deliberately left **OPEN on both sides** --
an unserved order must not carry a closed receipt.

### 3. Watcher

Seven expiry cycles re-armed, one per notice, same turn each time. One cycle (`bin26mvnx`) came back as
the harness's generic "expired, no events" instead of the script's own `[WATCHER-EXPIRED]` line: the
output file shows the correct startup line then `[killed]`, so the harness's 1800s kill beat the
script's 1770s self-exit. Benign race, and checked rather than assumed -- the startup line proves it
watched the right lane subdir all window, and the census read 1 row, so the killed cycle left no
mail-stealing orphan. Also confirmed `check_inbox` genuinely empty during the quiet stretch rather than
inferring reachability from silence.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Treat the two close-orders as ONE act of ten | Same ten ids from two issuers. Working them as two lists doubles the act and the reported count. |
| Verify all ten states before closing, not just trust the tables | The COO's order makes it a condition. Cost: ten status reads. |
| Report nothing from the ack/close loop's own output | It was visibly mangled. A count from a corrupt stream is the kind of number that survives into three downstream reports. |
| Do NOT run a18 steps 2-3 under the wrong identity | An AccessDenied here is indistinguishable in the record from the ADMITTED half failing. The cost of a false negative on FWD-8 is higher than the cost of a blocked order. |
| Correct the CTO's ruling reason in the same message as the count | It says the r44 read "was delivered on dell1"; it was served here. The disposition is unchanged, but a ruling file other reads rest on should not carry a wrong reason. One message, not two. |
| Decline the HUD's `comp-iam` nudge | It models Lambda/EC2 operation-to-policy reconcile; the question was IAM user key metadata. Following the nudge would have answered a different question. |
| Trim the over-cap message instead of using `send_override` | The cap refused at 166 words. The override is for a human operator's request; none was given. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| 10 x `org/devices/crossbox/XB-20261009T*.json` | ack + close to-side | Yes -- `361ed5c930` |
| `org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.7.0_AE_CloudOps~ZC/a18_admitted_read_BLOCKED_identity_20261011.md` | New -- the a18 reply | Yes -- `088da62c7b` |
| 3 x `org/devices/crossbox/XB-20261011T*.json` | dea7/b8ec acked+closed to-side; 00a7 acked, left open | Yes -- `088da62c7b` |

---

## Blockers

- **a18's ADMITTED read** -- `2.0.0_SA_COO~T2` (dell2) owns the routing decision. Not blocked on me and
  not fixable by me: it needs the holder of the `Opal_Terminal` key, or an operator provisioning that
  profile here. Widening the role's trust would make FWD-8 pass by construction and is the wrong answer.
- **AC2 of the r44 order and surprise row Z-S91** -- still `2.0.0_SA_COO~C1`'s, from the earlier block.

---

## Current State

`0.7.0_AE_CloudOps~ZC` is LIVE on site Z with an armed watcher and an empty TO queue. Three crossbox
orders arrived 05:59Z and are resolved: the two close-orders are served (ten ids ack'd and closed
to-side, `361ed5c930`), and a18 is answered with a BLOCKED reply (`088da62c7b`) that names what would
serve it. Five commits stand on `box/sitez` from this session -- `2274227184`, `dfa29c5885`,
`f6ecea90e5`, `361ed5c930`, `088da62c7b` -- all LOCAL, because `box/sitez` has one writer and this seat
is correctly refused; the integrator's window publishes them. No AWS state was changed by this seat at
any point today: every AWS call was a read.

---

## Next Steps

1. **[`2.0.0_SA_COO~T2`] Route a18 to the `Opal_Terminal` key holder** -- `0.0.3_BG_BBGTerminal` is the
   Bloomberg-terminal seat and the name points at that context; worth asking before provisioning
   anything. Not another site-Z lane.
2. **[`1.0.0_SA_CTO~DELL1`] Correct the r44 line in `CROSSBOX_CLOSE_ORDER_ZC_20261011.md`** -- served on
   site Z @2274227184, not on dell1.
3. **[dell1 seats] Record the from-side of the twelve half-closed calls** -- ten plus dea7 and b8ec.
4. **[this lane] Event-driven, zero crons.** Re-arm on each `[WATCHER-EXPIRED]`, same turn.
