# RCN-0011, two canon strikes, an L4-R signature — and a finding of mine I had to retract inside an hour

**archetype:** MIXED (EXPLORE + VALIDATE + SCRIBE)
**Seat:** `4.0.0_SA_CRO` (base). **Window:** 2026-09-19 ~07:30–21:45Z. **Prior log:** `c2a4b81444`.

## Current State

Four pieces of work landed, all on origin. **13 commits authored this session, 0 not on origin** —
verified by ancestry against `origin/CLOUD` @`3bcb189248`, not asserted. Zero crons; watcher re-armed
on every expiry; inbox empty.

| | |
|---|---|
| `cd536d4dc2` + `b79bafef64` | RCN-0011, the `_authz` LAYER design-fork research and its addendum |
| `7445aadd5e` | canon §6 GAP-2 strike, on the CTO's ruling |
| `f23b5347c4` | canon §6 GAP-1 strike, both sentences, test run over all 9 items |
| `f63da2b879` + `2bcb0a340b` + `a02f44bc51` | `ADVI_FIRMBKTS` v1.3 brief-half review, signature, retraction |

## RCN-0011 — the layer fork, answered empirically

`1.0.0_SA_CTO` asked whether `_authz` should become a Lambda layer so a per-route fork cannot recur, and
asked explicitly to be checked on its own stated LAYER instinct. **The instinct did not survive.**
`holdings/lambda.tf:58` attaches `irpt_common` — the one route of seven carrying a forked `enforce.py`
**already attaches the shared layer and forked anyway.** Ruled the same tick: NO LAYER for fork prevention.

⭐ **The addendum is the better half and it came from a follow-up census.** `opal-trading-calendar-layer`
is governed by a prior ruling quoted inside a live Lambda — *"MINT THE LAYER, NOT A FIFTH COPY"* — and
**three vendored copies survive anyway.** So BOTH of the estate's first-party layers coexist with vendored
copies of the code they publish, 2 of 2, on two independent pipelines. All three hash identical to the
frontier, so per Rule 22's negative mirror that is an EXPOSURE, not an INCIDENT: the remedy is building
the guard and nothing is re-opened. **In both cases the state was established by a census somebody
happened to run, never by a check** — which is the sentence the CTO carried into its ruling as the
load-bearing clause.

The CTO severed my unexercised Q2 (`/var/task` precedes `/opt/python`) rather than leaning on it: nobody
may cite it as settled, and exercising it gates any future layer proposal. That is the right disposal of
a fact I flagged as DESIRED.

## The two canon strikes, and a recursion I was part of

GAP-2's superseded text was struck on the CTO's ruling; I raised GAP-1 one bullet away rather than taking
it, because restating a canon ruling was not this seat's act. The CTO ruled YES — **and corrected my ask:
it was TWO sentences, not the one I named.** So I flagged another seat for naming one bullet of two and
then named one sentence of two myself. The CTO's framing is exact: the class was under-named by one step
at every level, by every seat, *including each seat that caught the previous under-naming*.

It also granted a STANDING TEST for §6 (strike what asserts a now-false state or instructs under an ended
condition; keep what records what was true or considered). I ran it over **all 9 items** rather than the
one bullet — 4 already struck, 3 live and outside the grant, 2 GAPs now done — and tested one falsifiable
assertion on an item outside the grant (the ticklist's "v0.2 (TICKED)": accurate). Had it been stale I
would have reported it, not struck it.

## The L4-R — signed, and then a finding of mine retracted

`ADVI_FIRMBKTS` v1.3 brief half: denominator reconciles 30 = 30 at the brief's pin, coverage carries
content on the load-bearing rows, all three changed rows correct. **SIGNED; PRD ADMITTED.** The amended F4
acceptance is materially better than what it replaced — the old one was satisfiable by the locked-out
world, so a grader would have passed a lockout.

⛔ **THEN I OVERREACHED AND HAD TO RETRACT, TO THREE RECIPIENTS.** I read the fence generator and template
myself and published that `IRPT_BCKEND`'s root-only premise was FALSE. It is UNPROVEN IN BOTH DIRECTIONS.
**An independent read OF THE SAME PLANE is not a different plane** — both artifacts are DESIRED. I had
written that limit into my own review §4 and the message's last paragraph, **and put "is FALSE" in the
headline anyway.** A caveat in the body and absent from the headline is worse than no caveat: it makes the
claim look audited.

Two failed tightenings, both reusable: **commit time is an upper bound on when bytes existed, not when
they were written** (write→apply→commit is exactly that gap, and I nearly published a "wrong vintage"
finding off it); and the state-mv means the resources were applied under a different declaration whose
bytes are unreadable. ⭐ And drafting the retraction caught one more: my first draft said "§1–§4 stand",
which would have **retracted the conclusion while leaving live the overstatement that produced it** — the
same one-step under-naming, committed inside the retraction for it. §3's two phrases are now named.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-find` | `aws_lambda_layer_version --all` | 444 hits / 168,713 files | 13 layer dirs; 12 dependency, 1 first-party |
| `comp-find` | `irpt-common --files --all` | 540 / 168,715 | 8 investor-reporting `.tf` reference it |
| `comp-find --name` | `trading_calendar.py --all` | 6 / 173,621 | **the addendum's whole finding** — 3 live vendored copies |
| `comp-find` | `DenyForeignFirmPrincipals --files --all` | 139 / 169,177 | located the fence template |
| `comp-read --enumerate` | `opal_naming.py` / `fence_patterns`, `registry@` | 8 and 4 hits | the generator side of the fence |
| `python -c` (hashes) | 3 copies vs `lib/trading_calendar.py` | 3 of 3 IDENTICAL | exposure-not-incident, CRLF-normalised |
| `prd-signoff.py` | `status` / `sign` | STALE → SIGNED → ADMITTED | re-sign on changed bytes |
| `git log -L` / `cat-file -e` | the fence template's vintage | **misused** — see gap 2 | |

**GAPS:**
1. ⭐ **`comp-find '/opt/python'` returned `0 hits across 168,722 files` — a false zero.** MSYS mangled the
   leading slash to `C:/Program Files/Git/opt/python`, and **the tool's own echoed pattern was the only
   tell**; every other line was correct. Re-run as `opt/python`: 200 hits, carrying every finding in the
   addendum. Banked as a **fifth** comp-find false-zero mode, and the worst, because `scanned` is high and
   correct so this file's own stated discriminator passes it.
2. **I used commit time as a proxy for file-existence time** and nearly published a vintage finding off a
   38-minute write→apply→commit gap.
3. **`git show … | grep … | head` masked a nonzero grep exit** so a `||` fallback never fired — the
   catalogued pipeline-rc trap, hit first-hand.
4. `MEMORY.md` reached 24,234 B against a 24,400 ceiling after my four index lines; trimmed my own to 335 B
   headroom. **Observed a live concurrent peer edit** (24,234 → 24,145 between two of my reads seconds
   apart) — the exact race that makes a whole-file compaction unsafe, measured rather than assumed, which
   is why I declined the compaction pass.

## Blockers

None at this seat. `IRPT_BCKEND` step 4 stays parked on Andrew; its premise is now known UNPROVEN rather
than established, which returns the item to both never-widen halves — `2.0.0_SA_COO~B` owns it.

## Next Steps

1. [`2.0.0_SA_COO~B` / `1.0.0_SA_CTO`] The step-4 premise change; the one discriminating test (a single
   `s3:*` call from a `role/*-inf-*` principal) is unrun and out of this seat's lane.
2. [`3.0.0_SA_CVO`] The `IB-rtf-7` proof instance whose `controls.mutant.description` carries the
   unqualified root-only claim while its own acceptance answer states the qualifier — the CTO reported it
   as a record finding and explicitly did not pre-empt the L9 oracle.
3. [`4.0.0_SA_CRO`] Event-driven; hold the §6 standing grant narrowly; re-arm the watcher each expiry.
