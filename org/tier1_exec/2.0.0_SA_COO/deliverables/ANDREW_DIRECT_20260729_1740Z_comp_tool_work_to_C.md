# ANDREW-DIRECT 2026-07-29 ~1740Z — all comp-tool work routes to `1.0.0_SA_CTO~C`

**Recorded by:** 2.0.0_SA_COO (COO terminal, direct from Andrew — not relayed)
**Channel:** COO terminal · **Time:** ~2026-07-29T17:40Z · **Broadcast:** CTO + MSTR + ~C, same turn

## VERBATIM

> "Yeah all comp-tool work should be going to ~C"

Context: I had just reported that WS1 (`comp-opalbizsem`) was unowned after Andrew's ~1712Z scoped
`1.0.0_SA_CTO~B` to SQS-only, and that its dependency sits in an AE-only path.

## WHAT IT SETTLES

**Ownership of the comp-tool package is `1.0.0_SA_CTO~C`, entire.** This closes the WS1 orphan —
`comp-opalbizsem` joins WS2 (`comp-legacywriter`) and WS3/WS4 (registry census, `comp-pipescript`
hardening), which ~C already held. Three re-assignments in 35 minutes resolve to one owner.

Supersedes for routing purposes: base CTO's 170957Z assignment of WS1 to `~B` (already superseded by
Andrew's ~1712Z), and `~C`'s own 171101Z retraction of its WS1 claim.

## WHAT IT DOES *NOT* SETTLE — SURFACED, NOT ADJUDICATED

**Ownership is not capability.** WS1 steps 2-3 (`extract_s3_served.py` + the `SERVED_FROM` key-grain
derive edge) live under `infra/aws/globgrph/**`. Measured at source, 2026-07-29T17:38Z:

- **No `globgrph` longest-match rule exists** in `.owned-paths.yaml` (grep: zero path rules). It falls
  through to `infra/aws/**` = **`ANY_AE`**. No CTO serial — base, `~B`, or `~C` — can commit there.
- **The directory is MIXED, not pure graph code:** `_canonical.py`, `code_heat_emit.py`,
  `comp_cluster_cli.py`, `derive_runner.py` **alongside `Dockerfile`, `buildspec.yml`,
  `build-derive-image.sh`** — container and build machinery.
- **The documented precedent deliberately stopped short of this path.** The 2026-06-16 same-tool
  decompose-time grant (`.owned-paths.yaml:1091`, landed by 2.0.0_SA_COO, CTO-routed) granted
  `org/modules/graph/contract_engine*.py` and explicitly noted *"derive_runner.py is
  infra/aws/globgrph/ (0.7.0 infra lane)"* — i.e. a prior COO decision on this exact boundary chose
  to leave globgrph in the AE lane.

**MY READING, offered as a reading and not as a ruling:** these two steps were never comp-tool work.
CVO's reroute doc already assigned them to an AE (`0.8.0_AE_CloudComp` **or** `0.7.0_AE_CloudOps`),
with the reason written in its own owner column — *"`infra/aws/globgrph/**` is not my lane; I do not
commit producers."* They are graph-PRODUCER infra that `comp-opalbizsem` consumes. On that reading
Andrew's instruction is fully satisfied with **no grant change and no scope adjudication**: ~C owns
every comp-tool, an AE builds the two producer steps beneath them, exactly as the doc specified
before the dispatch layer overrode it.

**If Andrew or CTO reads `infra/aws/globgrph/**` as inside "comp-tool work," that is a scope call
they make, not me** (XXX.md: the receiving agent surfaces, does not adjudicate). It would need a
narrow longest-match grant, grantor-landed per SoD — and it should be narrow, because the path
carries deploy machinery and `infra/aws/**` is AE-only for reasons unrelated to graph tooling.

## STATE CORRECTION THIS RECORD MAKES

I told CTO at 172238Z that this dependency was *"unowned."* **That was wrong and I am correcting it
here:** CVO's doc named a correct AE owner. The defect was never an absent assignment — **the
dispatch layer overrode a correct assignment with a serial that structurally could not commit the
path.** The remedy is therefore *restore the named owner*, not *find someone*.

## OPEN AT ANDREW (one line, no action implied)

`1.0.0_SA_CTO~B` stood down for the day and left bar item (f) deliberately open: both agentbus queues
are LIVE and OUTSIDE Terraform (TO `OPAL_SQSCHAT.T1`, `0.7.0_AE_CloudOps`, post-freeze). Its ~1735Z
ruling closed FUNCTIONALITY expansion; ~B explicitly did **not** read that as cancelling or as
confirming T1, and declined to close it by inference. It needs Andrew's word either way.
