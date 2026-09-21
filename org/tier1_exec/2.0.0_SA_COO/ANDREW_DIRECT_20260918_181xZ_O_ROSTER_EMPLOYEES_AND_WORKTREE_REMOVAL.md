# ANDREW-DIRECT 2026-09-18 ~18:1xZ -- two cards answered at the 2.0.0_SA_COO~O terminal

**Channel:** Andrew, directly, at this terminal, replying to `/open-calls` run at this lane at ~18:10Z.
**Received by:** `2.0.0_SA_COO~O`. Recorded verbatim and relayed to `1.0.0_SA_CTO` in the same turn.

## His words, VERBATIM AND ENTIRE

> yes, all opal employees can use this. on call 2, yes thats fine.

## CALL 1: sprint roster value

**The card asked:** *"Can anyone who is NOT an Opal Capital employee sign in to the Opal tenant (contractors, guests, service accounts)? (a) no (b) yes"*

**What his word settles, read narrowly:** the AUDIENCE is all Opal employees. This restates his ~14:0xZ card-4 answer, "All signed in opal capital employees".

**What it does NOT settle:** the card's population question. A bare "yes" to a card whose options were (a) no and (b) yes literally selects (b), meaning non-employees CAN sign in. The rest of his sentence reads as an audience statement, not as a claim about the tenant's sign-in population.

**So the tenant-wide wildcard `"*"` is NOT set on this sentence.** CLAUDE.md says: *"verbatim scope; relay, never adjudicate wider OR narrower; if wider seems plausible, ASK."*

- **Asked back, in one line:** does the tenant contain any non-employee sign-ins?
- **Unaffected either way:** the correctness fix, where an empty roster means UNCONFIGURED and fails closed, proceeds regardless of the answer.

## CALL 2: removal of three worker folders. ANSWERED YES, EXECUTED

Removed at ~18:17Z with `git worktree remove --force`:

- `C:/tmp/wk-oplgtw-6r` (rc 0)
- `C:/tmp/wk-oplgtw-1i4` (rc 0)
- `C:/tmp/wk-oplgtw-2a` (rc 0)

**Checked before removal:**

- **Unmerged commits:** `git rev-list --count CLOUD..<branch>` = 0 for each.
- **Scratch contents:** commit messages, gate output and probe captures only. No re-seal salt was among them.
- **One dirty tracked file** in `-2a`: `infra/aws/ec2/opal-gateway/audit.jsonl`, 6 appended `_ratelimit_control` lines with an empty user, 08:39Z and 09:05Z. None of the 6 is present on CLOUD. These are local test-run side effects, not evidence.

**Branches kept:** `wk-nfra_oplgtw-2a`, `wk-oplgtw-6-reseal` and `wk-oplgtw-1-i4` were not deleted, because his word named the folders.

**Result:** `git worktree list` now shows one NFRA_OPLGTW worktree, `C:/tmp/wk-oplgtw-2r2`, where OG-r-2 is running.

---

# ANDREW-DIRECT 2026-09-18 ~21:1xZ -- both remaining cards closed at this terminal

**Channel:** Andrew, directly, replying to `/open-calls` run at this lane ~21:1xZ (card 1 the spend limit, card 2 the roster population).

## His words, VERBATIM AND ENTIRE

> I will handle that spend limit issue, take it off the open calls list. Call 2 does not matter for us at this time.

## What each settles

### CARD 1 -- THE SPEND LIMIT IS HIS, AND OFF THIS QUEUE

He owns the remedy. This lane does not list it again, does not propose a workaround, and does not treat a future 429 as a new call -- a worker killed by one is re-spawned on the existing pickup pattern (measured tonight: OG-r-2 killed 18:55Z, re-spawned after the reset with its uncommitted work inherited).

### CARD 2 -- THE ROSTER POPULATION QUESTION IS DEFERRED, NOT ANSWERED

"Does not matter for us at this time" sets PRIORITY, not the VALUE. So:

- The employees-vs-accounts question stays OPEN and unasked. It is not re-raised at him.
- **The tenant-wide wildcard is still NOT set.** Nothing in this sentence authorizes it, and his ~18:1xZ audience word ("all opal employees") is unchanged.
- The sprint roster stays a round-2 carry, and its correctness fix -- an empty roster means UNCONFIGURED and fails closed -- proceeds on its own merit.

⛔ A deferral is not a licence to pick the wider value while nobody is watching. The value is set when he answers, or not at all.
