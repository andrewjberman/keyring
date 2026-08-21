# 0.5.0_AE_OpalETL~Z — Session Log — 2026-08-20 2200–2225Z

**archetype:** DIAGNOSE
**Project:** D7 TICKET LIFECYCLE v2 — W-B (stream/notifier accelerator) pre-write

## Summary

**W-B's AWS half is HELD, and the hold came out of the pre-write checks rather than a test-time
discovery.** I ran the mandated comp-tools *before* writing this time — the W-A lesson taken
rather than acknowledged — and they produced two findings, the second of which stopped the build.

**Nothing was written.** No TF, no notifier, no config.

## Finding 1 — W-B would be the estate's first DynamoDB stream

`comp-find "stream_view_type"` → **0 hits across 26,848 files** (with the tool's own disclosure
that 1 in-scope file was unreadable and my zero doesn't cover it); `stream_enabled`'s 10 hits are
all pyarrow library noise. DESIRED agrees with APPLIED: `describe-table` on `opal-tickets` returns
`StreamSpecification: null`. The event-source-mapping + consumer *shape* does exist 4× in
first-party TF — all SQS sources — so rung 2 is **partially** satisfied, which is the honest
classification and harder to write than either extreme. `comp-blast` on the table: no downstream
consumers (lower bound, per the tool's caveat), 10 upstream callers all via the ticket API.

Four config decisions named and ratified: `NEW_AND_OLD_IMAGES` (the old image is the only way to
know what *changed*), `LATEST` (TRIM_HORIZON would replay every existing ticket into a
client-facing channel on first enable), small batch with explicit failure config — **with CTO~Z's
added condition that the wedge must be LOUD, not merely bounded** — and the notifier writes the
nudge and nothing else.

## Finding 2 — the last arrow has no mechanism, and it stopped the build

Stream → notifier Lambda → *"BG's nudge"*. **A Lambda cannot write a local filesystem inbox**, and
by my own earlier confirmed finding it can never hold a gateway credential either, since refresh
is an interactive OAuth challenge. The estate's only live AWS→local path is the agentbus FIFO
pairs — device-scoped, MSTR-scoped, coordination-only by standing rule. So something local must
consume it, and the only thing running locally on a schedule is my 5-minute runner.

> **An event-driven accelerator whose last hop is a five-minute poll is not an accelerator; it is
> a second detector feeding the same delivery clock.** WB-1 asks me to measure and quote the stream
> path's latency — as cut, that number would have been the backstop's.

CTO~Z held the AWS half and named two of the reasons as theirs (a "zero new infrastructure" cost
claim that rested on a queue's *existence* without checking its *charter*, and clearing past their
own measure-the-wake-hop-first sequencing).

## Finding 3 — the wake hop was already measured, 48 minutes before the ruling that called it unmeasured

BG measured it at 21:32Z on real traffic: **12.48s detect + 14.13s wake-and-act = 26.61s**.
Applying CTO~Z's own test (arithmetic labelled as arithmetic; uniform arrival is *my* assumption):
5-min backstop ≈ 164s expected → 30s schedule ≈ 29s → stream ≈ 16s. **The first step buys ~135s;
the second buys ~13s** — ten times the improvement for no new infrastructure. The stream's marginal
benefit is roughly equal to the wake hop it cannot touch. And BG's stated bound runs *toward* that
conclusion: 14.13s is a warm-schema floor, so the true wake cost is that or more.

## Finding 4 — the water-test buzz mutated after posting

The composer deterministically produces `1.0.0_SA_CTO~Z`; the channel now reads `1.0.0_SA~Z`, and
contentType flipped text→html between my 20:25 and 22:16 readbacks. Not a query artifact — BG's
header in the same response is unchanged. **Mechanism UNDETERMINED and deliberately not supplied**:
the discriminating field (`lastModifiedDateTime`) is not in the gateway tool's `$select`, so the
edit hypothesis is untestable from this seat. The generalizable part: **a readback proves what was
there when you looked**, and our channel-side TAC-2' evidence is all readbacks — the producer-side
receipt and runner log are the durable half and still read exactly as recorded.

## Operational

Runner exited 2 at 22:09 and 22:14 (credential expired ~22:06, as predicted). Restored by one
legitimate gateway read at 22:16; expiry now 23:15:55Z, runner re-exercised `INTAKE PASS OK` rc=0.
**Stated so nobody reads it as self-healing: an agent warmed it by hand.** Third occurrence, same
period; the prop is not the fix and the fork is already with Andrew.

## Compiler Tools

| Run | Observed | Verdict |
|---|---|---|
| `comp-find "stream_view_type"` / `"stream_enabled"` / `"aws_lambda_event_source_mapping"` | 0 / 10-all-noise / 18 with bands — the rung-2 finding | PASS |
| `comp-blast opal-tickets` | no downstream consumers (lower bound), 10 upstream | PASS |
| `describe-table` + `sqs list-queues` | stream null; only agentbus FIFOs as AWS→local | PASS |
| `comp-find` regex warning | it caught my escaped-pipe error and told me python re treats `\|` literally — the tool correcting my input | PASS (tool earned it) |
| My own rail-marker self-review | 1 of 4 markers FAILS (a true claim about the wrong tool); tested by running `comp-find` on the search I had overridden | CONTROL FIRED ON MYSELF |
| `grep -rwci "withdrawn"` re-run | 4 = 4 case-insensitive — my census holds, but the method shared CTO~Z's blind spot and the corpus happened not to punish it | PASS (verified, not assumed) |

## Blockers

W-B's AWS half HELD at CTO~Z's word (a spec fact, not a gate) pending the rung-1 question and the
cost/benefit call, which is now carded to Andrew with numbers. Nothing else held: W-A's apply is
the laptop's, A1 waits on a real channel post, W-C/W-D/W-E/W-F are others' or design-gated.
