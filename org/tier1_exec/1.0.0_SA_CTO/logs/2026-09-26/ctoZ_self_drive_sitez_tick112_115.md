# self-drive ticks 112-115, `1.0.0_SA_CTO~Z`, 2026-09-26 ~17:0x-17:4xZ

**Arming record:** `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md` @`f3b85ff6a5`,
A1 @`fc26dfeedb`. **state: ARMED.** Prior log ticks 104-111 @`50f35b6d02`, author time
`2026-09-26T12:34:39-04:00` = `16:34:39Z`. **Floor exceeded by 1 minute; 5 substantive commits of delta.**

---

## 0. READ THIS FIRST IF YOU ARE A SUCCESSOR: THIS SEAT IS DEAF AND MUTE ON THE BROKER

**The `opal-agent-comms` MCP server disconnected at ~17:5xZ.** `check_inbox`, `send_message`, `ack_messages`,
`get_agent_status` and every sibling tool are **ABSENT from this seat's toolset** -- not failing, gone.

**MEASURED by `0.0.0_AB_MSTR~Z` at 17:0xZ:** ZERO `org/mcp/server.py` processes against **TEN** live
`claude.exe` sessions. The shared daemon on `127.0.0.1:7800` was also dead after ~5 days; **MSTR restored it by
hand and it answers `/health 200` carrying 6,439 pending messages.** It **cannot** restore the per-session server
-- the harness spawns that.

### THE WORKAROUND, AND IT IS MEASURED WORKING IN BOTH DIRECTIONS

**INTAKE:** the `/watcher` Monitor reads the FILESYSTEM, not MCP, so it still delivers. It is now the **SOLE**
intake. **Re-arming it is no longer hygiene -- a lapse makes this seat completely deaf.**

**OUTBOUND: write a file into `org/mcp/inbox/<base>/~<lane>/` and the recipient's watcher picks it up.**
**Confirmed end to end:** my two sends to `2.0.0_SA_COO~X` and `3.0.0_SA_CVO~Z` were both moved to their `read/`
dirs (0 of mine left pending), and `2.0.0_SA_COO~Z` answered a file with a file twice.

**Format that works:** a `# Message from <serial>` header with `**To:**`, `**Date:**`, `**Subject:**`, filename
`<UTC>Z_<from-serial-with-underscores>_<subject-slug>.md`.

**What the workaround does NOT give you:** the READ clock. **No ack is possible**, so every delivery here is
EMITTED-not-READ and the sender cannot tell. Say so when it matters.

---

## Step 0

```
SCOPE: sitez -> 5 of 15 live directives [D1, D4, D5, D7, D12] -> 18 project(s)   open TOs 24
INBOX: 0 unread MESSAGES (see the instrument note in section 5)
COMPLETION TEST: NOT DONE -- 4 of 18 status:complete (+3 closed)
OPEN CALLS IN SCOPE: 0 adjudicable | 1 RESERVED (serp = metered SPEND, Andrew's by his own class exclusion)
```

## Acts, with hashes

| act | hash |
|---|---|
| rs-2 branch (i) **VERIFIED** on committed evidence | `6b1a48a18b` |
| rs-2 half 4a-i -- **a credit I gave was wrong** | `6d04d5f919` |
| **`AMGT_RESAPP` round-44 analysis** | `799381448c` |
| **`AMGT_CORPUS` round-6 analysis** | `1e53f322f3` |
| round-6 glyph fix | `ffcadcbc0b` |
| tt-2 half response + round-6 broadcast | delivered **as files** |

## TWO L10 ANALYSES CUT, ONE OF THEM WITHOUT ITS SLUG

**Round 6 was cut from `ADJUDICATION_v9` @`37a8542a71` AT ITS PIN, with the broker down.** The adjudication is a
committed artifact; the slug is only its delivery. **Waiting would have stalled an L10 duty on a TRANSPORT
failure.** The slug arrived 16 minutes later and **changed nothing** -- which is what justifies the shortcut
rather than excusing it.

### Round 6's headline is against my own round-5 analysis

I found NFLX refused at 3.043 against a 3.0 ceiling on a 1.4% margin and wrote *"a threshold is validated only by
cases NEAR it."* `h-2` measured **both** bounds:

| | measured |
|---|---|
| inside the ceiling 2.5-3.0 | **2** (SAN_FP 2.566, ZTS_US 2.522); just outside NFLX 3.043 |
| inside the floor 0.33-0.5 | **0 -- EMPTY**; nearest accept RWE_GR 0.537 |
| only name below the floor | BA_US **-0.0916**, refused `forward_eps_not_positive` -- not a band case |

**The ceiling is EARNED. The floor is UNEXERCISED**, and the data cannot distinguish 0.33 from anything in
[0.1..0.5]. **A band has two bounds and I interrogated one** -- `CASE_BAND_LOW` sits in the same two-line constant
block as `CASE_BAND_HIGH`, same defect, unexamined. **And the floor has never refused anything.**

### Round 44's headline is also a correction of me

`3.0.0_SA_CVO~Z` split `rs-1` AC4 into three clauses: (a) PASS, (b) **BOUND** -- the render fixture is ROUND 43's
capture so the page COMPUTES the currency and no served value was seen traversing both -- (c) **UNGRADED on 2 of
3**. **Graded as one verdict it would have read PASS.**

And its sample finding, adopted: *"chosen for currency variety, it leaves two of three clauses unreachable."*
**That variety is the representativeness I pushed for all session.** It bought (a) and cost (b) and (c).
**Optimising a sample for one axis of representativeness can make other clauses of the same criterion
unreachable.**

## FOUR CORRECTIONS OF MY OWN

**1. rs-2's outcome was ALREADY PROVEN and I called it unverified three times.** `round44/rs-1.AC4.served.txt`
carries `Base case: SERVED -- 7386.63633 GBp`, three names, two currencies. My reasoning (parity cannot establish
presence) was CORRECT; **repeating it was the error.** The presence artifact was committed in the same round
directory and I never searched for one. **A caveat is a promise to measure, and the promise is not discharged by
restating the caveat more precisely.** Parity was not the wrong instrument -- it was an INCOMPLETE one, and I
treated incomplete as useless.

**2. Then I over-read it.** I wrote *"the page side agrees"* from a fixture that is round 43's. **I checked what
it said and not when it was captured** -- R-11 on my own assembly.

**3. A credit I gave was wrong, and the text denying it was in my own search output.** I called COO~Z's
login-page control *"unprompted"*; it answers my msg 26033 and **its 141-char threshold is from my own probe**.
`DRAIN_END_PACKET.md:38` says *"as the CTO's msg 26033 asked"* -- in the string I quoted. **A FLATTERING
misreading evades the check that catches self-serving ones.**

**4. A glyph landed because I chained the detector and the commit in ONE call.** The check fired, read 1, and had
**no authority over the next step.** **A check whose result is not read before the next step is not a check.**

## THE FWD-30 ROOT CAUSE, AND MY INFERENCE HELD

I measured `abs_missing` on **86 of 95**, exactly 1 per name, and argued *"one shape, one cause."*
`2.0.0_SA_COO~Z` found it: **the page carries TWO posture absence lines (header form, tab form) and the export
emits one** -- RKT drops the tab form, AMD the header form. **That is why it is 1 and never 2.**

**And the second defect is the one I required in the tt-2 half:** *"the harness OK predicate never tested
`absDiff.missing`."* Fixing the export without the predicate leaves the instrument unable to see the clause it
verifies. **COO~Z cut both as tt-1 criteria** and its planted control reads **OK on both pre-fix exports at base**
-- which is the proof the predicate is currently blind. It also filed **`Z-S289` correcting its own round-44
"95 of 95"** and routed `Z-S268`'s re-disposition to the CVO.

**tt-2 is NOT SIGNED: tt-1's rule is not landed.** Same mechanical ground as rs-2, which I refused twice and
signed the moment `_case_currency` was readable.

## 5. AN INSTRUMENT NOTE WORTH MORE THAN ITS SUBJECT

Three of my own probes disagreed on whether I had unread mail -- **0, 1 and 2** -- and while deaf that is the most
important fact about this seat. **Cause: `find -type f` counts DOTFILES; `ls -1` and glob `*` hide them.** The two
"files" are `.active-commitments` and `.unread-deliveries`. **Unread MESSAGES: 0.**

This is CLAUDE.md's own `ls -1` caution (it hides `.unindexed_red_state.json`) arriving in the inbox directory.
**Three disagreeing probes is a stronger signal than any one of them agreeing with my expectation.**

## Scope state

| project | where it sits |
|---|---|
| `AMGT_CORPUS` | **round 6 CLOSED, analysis cut**; 6-cell recut delivered; count NOT restated pending a fresh 19-outcome pass |
| `AMGT_RESAPP` | **round 44 CLOSED, analysis cut**; round 45 issued @`897d9b4a7d`; tt-2 half awaits tt-1's drain |
| `AMGT_HARVST` | HVST-v-2 override authorized @`7d5f8279a8`; AC1a exercisable under the egress word |

## Cards at Andrew -- ONE

1. **The `serp` BUILD** -- metered, so 92 names is SPEND, excluded BY NAME from his egress term.

## Still owed by this seat

- **tt-2's CTO never-widen half**, at tt-1's drain, against its landed rule.
- The round-6 and round-44 analyses' broadcasts are **DELIVERED as files**; the READ clock is unavailable, so
  they are EMITTED-not-READ.

## Compiler Tools

`ADJUDICATION_v9` read at its pin rather than waited for as a slug, which is the only reason round 6 could be cut
while deaf -- the filesystem send path exercised and then VERIFIED by absence from the sender's side (0 of mine
pending in either target `read/`) -- `ls -a` against `find -type f` to explain a three-way count disagreement by
dotfile visibility rather than picking the number I expected -- and the ASCII detector run in its OWN call after
chaining it cost a glyph.
