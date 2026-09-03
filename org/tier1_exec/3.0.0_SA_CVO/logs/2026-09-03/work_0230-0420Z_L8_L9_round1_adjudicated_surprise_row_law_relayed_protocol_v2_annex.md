# 3.0.0_SA_CVO -- 2026-09-03 02:30Z to 04:20Z -- L8/L9 on NFRA_COMPEFFICACY round 1; the surprise-row law relayed; SURPRISE_CHANNEL_PROTOCOL v2.0 as the L7-L10 annex

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, SCRIBE

Seat: 3.0.0_SA_CVO base, MAIN fabric, laptop, CLOUD, PID 14124. Continues `startup_0158-0230Z_...md`.

## Summary

1. **L8 exercised end to end, then the law caught up with it.** The round's one worker surfaced its first surprise by
   MCP only (92943, no row on either root). This seat assembled row S1 at the tree home @03eb9e3dba; the notifier fired
   on the row within one poll. A fork Andrew ran at this terminal reported that the file path was already deterministic
   and the message hop the only non-deterministic part; Andrew then ruled at this terminal (~03:06Z, verbatim in
   `deliverables/ANDREW_DIRECT_20260903_031xZ_SURPRISE_ROW_NOT_MCP_GATE_ON_PROOF_OF_SPEC_SURPRISES.md` @007481053a):
   CLAUDE.md must not route surprises over MCP, and a gate on the proof-of-spec `surprises` field lands now. Relayed to
   `1.0.0_SA_CTO` (92976; cc COO, MSTR). CTO landed both within 15 minutes (@7968221ef5 the SURPRISES limb, 6 of 6
   red-first, live probe VALID against S1 / REFUSED against a phantom; @6e8805eb90 the law: Rule 27 stub + "a broker
   message is NEVER the carrier"); COO closed the flat-lane asymmetry @bfec7d99b5; CTO's follow-up @835a7e1785. All on
   origin by 03:42Z (MSTR frames, ls-remote re-read here).
2. **Round 1 adjudicated in append-only form.** S2 arrived as the worker's own row, no MCP. CTO's T1 report 93025 and
   COO's terminal flip @fc5ec7106c met S1's closing condition. This seat's other-seat exercise of the rework
   (@2718cffc45, read on its bytes) found the forced ceiling textbook and the DEFAULT budget also expiring: 3 of 3
   `--corpus aws` pulls at 90 s, 03:53Z-03:58Z, no burst, no leftovers, DB unchanged -- S2's "self-resolved" falsified.
   A first write flipped S1/S2 in place; the row gate REFUSED it (mutation limb: corrections are new rows citing the
   old id). Redone as it should be @db508e75b4: S4 closes S1 (DISMISSED_WITH_REASON); S3 is this seat's own row for the
   recurrence (ARMED, disarm owner `0.8.0_AE_CloudComp`); S2 stays open with S3 as its carrier. L10 HELD: 4 of 4
   CVO-checked, 1 item closed, 1 open, 0 graduated, 0 routed. COO's L10 read agreed (93059) and retracted its
   "the read is this seat's" clause to the spine's allocation (93061): the CVO stamps, the route owner acts.
3. **The protocol re-keyed** (Andrew's brief @ba9add4200 s.3, MSTR 93029): `org/ref/SURPRISE_CHANNEL_PROTOCOL.md` v2.0
   @d1220c4971 -- the L7-L10 annex of the spine in constitutional form (219 lines replacing 263; body census 0 for the
   retired tokens; changelog carries dates and records). Broadcast 93076-93079. LOCAL under Andrew's push hold
   (MSTR 93072, verbatim: "you need to stop pushing until i say so, stop interrupting the fabric").

## Compiler Tools

| Tool | Target | Result | Note |
|---|---|---|---|
| `comp-find --corpus aws opal-gateway --budget 1` | the reworked comp-find @2718cffc45 | BUDGET REACHED 1 s (flag), rc 0, 2 s | the forced control; `--help` discloses the carrier |
| `comp-find --corpus aws opal-gateway` (default) x2, `... LAMBDA` x1 | same | BUDGET REACHED 90 s (default), scanned 0 of 1, rc 0, 91 s wall each | **the S3 finding**; no leftover process; DB 82,661,376 B unchanged |
| `python .tools/proof-of-spec-check.py <T1 instance>` | @6d04680f2b | VALID rc 0; surprises 2 of 2 resolve, ENFORCE; alignment 6/6, 1/1, 1/1; artifacts 4 CONTENT-resolved | same instrument, second seat |
| `comp-read <protocol> --enumerate '<retired tokens>'` | v2.0 draft, then committed bytes | 10 hits -> 2, both benign (`staged`, the changelog hash line) | the brief's form check |
| `git show <pin>:<file> | grep -c` x6 | comp-find @2718cffc45 | BUDGET REACHED 6, WITHIN BUDGET 1, --cursor 8, COMP_BUDGET_S 2, _compbudget 11, budget-s 0 | pipe-receiver counts |
| `ls -la --time-style` + `ps -ef` | kuzu_nessie_db; kuzu processes | mtime 2026-09-03T00:36:15Z (S2 wrote the LOCAL time with a Z); 0 processes | grain note on S2 |
| `git checkout -- <file>` + a python rewrite | INVESTIGATION_v1.md | removed lines = 1 (denominator), +71 | the append-only redo after the gate refusal |

**What worked:** the row gate refusing my own in-place flip -- the control fired on the certifier, which is the point;
the second write was additive only and passed. **What failed:** my first adjudication write (in place) and the first
run of the redo script (CRLF from the checkout broke the fence regex; normalized to LF). **Gap found:** the notifier's
WARN lines during a restore-and-rewrite (count fell, rows "mutated") describe worktree churn, not the record; a reader
of its stream needs the commit to tell them apart -- noted to the seats, not chased.

## MCP traffic

Inbound ~25 (all READ-acked by id; the broker's re-echo at each heartbeat is its EMITTED view). Outbound of note:
92909-92911 (record + surfaces), 92931-92932 (stand-down + L4 input), 92970-92971 (S1 assembled), 92976-92978 (Andrew's
word relayed), 93005-93006 (S2 read), 93055-93057 (adjudication), 93076-93079 (protocol v2.0 broadcast).

## Surprise channel (manned, two roots)

NFRA_COMPEFFICACY: 4 rows at HEAD (S1 by this seat for the worker; S2 by the worker; S3 this seat's own; S4 this seat's
closure of S1). Open: S2/S3, one phenomenon, mechanism ungrounded; disarm asked of `0.8.0_AE_CloudComp` (a new row citing
S3). Nothing routed. Notifier denominator 20 files / 195 rows.

## Files Modified

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/surprise-channel/investigations/INVESTIGATION_v1.md` @03eb9e3dba, @db508e75b4 ·
`deliverables/ANDREW_DIRECT_20260903_031xZ_SURPRISE_ROW_NOT_MCP_GATE_ON_PROOF_OF_SPEC_SURPRISES.md` @007481053a ·
`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` @d1220c4971 · this log.

## Blockers

None BLOCKED. Round 1's L10 is HELD on S2/S3, which is the process working, not a blocker.

## Current State

- origin/CLOUD @db508e75b4 (ls-remote 04:1xZ at this seat); LOCAL ahead: d1220c4971 (this seat) and any peer commits
  since. Pushes are held on Andrew's word; LOCAL is the expected state.
- Monitors: inbox bec32h3nh; notifier b6cli05zq. Zero crons.
- 25 PENDING estate-report days still await Andrew.

## Next Steps

- [0.8.0_AE_CloudComp] the disarm measurement for S3 (`--mode inc` vs a non-incremental read), as a new row citing S3.
- [3.0.0_SA_CVO] on that row: graduate S2/S3 to a remediation row if the mechanism grounds (then stamp the route), or
  record a third data point and keep L10 held; the INERT `_compbudget.py` docstring residual rides CloudComp's next touch.
- [1.0.0_SA_CTO] gate limb (iv); the spine's cycles 2-3; the pipeline-doc stub.
- [Andrew] lifting the push hold; the estate-report backlog, at his pace.
