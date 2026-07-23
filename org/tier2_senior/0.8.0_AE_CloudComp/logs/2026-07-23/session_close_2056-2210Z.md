# Session close: deploy_ledger gate-integrity (3 fixes, dispatched + stood down) + registry-drift finding + hub routing

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

Window ~20:56Z -> ~22:10Z, continuing `session_stage2_contract_complete_and_lane_wave.md` (@d7777dd06).
Serial `0.8.0_AE_CloudComp` (base). Tilde-lane commits in the range are THEIRS and logged by them.

## My commits this window

| Commit | What |
|---|---|
| `839ee85cc` | gate-integrity: deploy_ledger red-scan MALFORMED-IS-A-VERDICT-NOT-A-CRASH + scan denominator + 11 fixtures |
| `c2a6d5539` | deploy_ledger `--all` full-re-enumeration override (the ONLY genuinely missing piece of CTO's leg 3) |
| `9438f17fa` | deploy_ledger reader accepts EVERY markdown Status spelling (CTO's AMENDED primary fix) + 7 variant fixtures |

## The deploy_ledger arc: dispatched -> 3 fixes -> Andrew-direct STAND DOWN

Main CTO dispatched (205615Z): `check --red` crashed with KeyError 'legs'. Took it TONIGHT (his
call-which) because it is the live NEVER#6 instrument on a night with multiple open deploys.

BLAST RADIUS WAS BIGGER THAN THE DISPATCH SCOPED: the KeyError fired in the Layer-1 sentinel loop, which
runs BEFORE Layer 2 -- so the ENTIRE gate-bypass scan was unreachable, not merely "entries after the bad
one". The first COMPLETED sweep surfaced SEVEN unindexed open ledgers the crash had been masking (mostly
tonight's MDPF promote chain). I framed the provenance to COO explicitly (masked-not-new) so 7 simultaneous
REDs would not read as 7 fresh bypasses.

THREE PREMISES I TESTED BEFORE BUILDING -- two came back FALSE, which is the window's real lesson:
1. Leg-3 de-dup "missing" -> ALREADY EXISTED and works (2nd sweep delivered 0 alerts, all "RED suppressed").
   Only `--all` was absent. Did NOT rebuild de-dup.
2. Leg-1 writer "must stamp terminal Status" -> cmd_close ALREADY stamps it (`_render_entry` emits
   `**Status:** CLOSED -- ... -- closed <ts>`; `_is_terminal_status()` True). So the writer leg is
   normalization-only, NOT a missing stamp.
3. Then CTO AMENDED the whole ruling on DT's reproduce-then-kill: the backlog files were NOT missing
   Status lines -- they carried them in spellings the READER could not parse (`**Status: CLOSED - ...**`
   colon INSIDE the bold span; `## Status: CLOSED` heading). THE INSTRUMENT WAS MIS-READING, NOT THE
   RECORD MISSING. A fix built to the original cause would have duplicated Status lines into files that
   already had them.
Landed the amended PRIMARY fix: `_STATUS_LINE_PATTERNS` (strict / colon-inside / heading), order
load-bearing (the colon-inside pattern captures EMPTY from the canonical form -> strict first, with a
regression guard). Reproduce-then-kill on real files: 3 of 4 flagged read terminal with ZERO edits;
`mdpf-allfirms-serve` still reads None because it genuinely has no status -- THE DISCRIMINATING CONTROL
(a loosened reader that called everything terminal would be worse than the strict one).

MALFORMED ENTRY, determined at source: hand-authored (writer emits slug/opened_at/legs/entry_path; it had
none), a CLOSED+bytes-verified deploy sitting in the OPEN-sentinel dir. I did NOT delete or rewrite it --
no change_management record existed, so it was the SOLE record of another lane's real deploy. Routed to CTO
+ author; CTO ruled (b), and 0.6.2_AE_PartnerETL~A converted it themselves @a4e63fe2e.

STAND DOWN (Andrew-direct via CTO 213512Z): my lane is infrastructure with CTO~Z, not main-fabric ledger
tooling; CTO owned the mis-route. Executed cleanly -- stopped at a clean seam (committed the tested reader
fix rather than leave a dirty shared tree, which we paid for once today; did NOT rush the half-built writer
change), handed 0.7.0 a state note carrying BOTH premise corrections so they pick up without re-grounding.

## Registry-drift finding (my surface) -- RULED, arch-gate asked

~B's LATENCY census asked me whether tools_index enumerates SUBCOMMANDS authoritatively. I MEASURED before
answering: the `subcommands:` field is populated on 65/65 tools and gated on NONE. comp-pipescript declares
8, argparse has 13. ~B's full delta: DRIFT 16 of 24 apples-to-apples multi-subparser tools (of 65 they
resolved 29; 5 pinned wrappers / 33 enumeration-uncertain / 3 engine-unresolved -- they refused to render
16/24 as a 65-tool rate, and led with a positive control reproducing my measurement exactly).

THE FINDING THAT MATTERS MORE THAN THE COUNT, verified by me not relayed: the undeclared derivations
include ones CLAUDE.md MANDATES. comp-iam exposes 15, declares 6 -- MISSING both `simulate` (Rule 22a's
spine) AND `reconcile` (the only APPLIED-plane overlay). Also `comp-pipescript postdeps` and
`comp-registry sync`. So comp-which cannot route an agent to calls the law requires -- my own
registration-invariant reasoning one grain down. Sharpest evidence the REGISTRY is the drifted surface:
my own comp-output-contracts.yaml declares by_subcommand plane overrides for comp-iam reconcile+simulate
(authored today). Two surfaces I own disagree; the contract is the more complete one.

RULED (my surface): GATE + BACKFILL, GATE FIRST -- the mechanism decides it, not the rate (nothing gated
the field, so backfill alone re-accrues). Spec carries 3 constraints: (1) no false-positive on the 5 PINNED
wrappers; (2) a declared-side GRAMMAR (the field mixes subcommands with flags/usage-forms); (3) MINE -- the
gate binds ONLY where the surface is ESTABLISHABLE; the 36 unresolved render UNKNOWN never FAIL, because an
unexercised hard-fail across 36 tools is how a gate earns a --no-verify habit. NOT BUILT tonight: a new
blocking member across the completeness family is arch-gated to CTO~Z (the route the output-contract member
took), and a member that false-positives across 65 tools is worse than none. Arch-gate asked.

## Hub routing this window

- ~D's mdpf STITCH-REFRESH ask ROUTED to 0.7.0_AE_CloudOps, grounded not guessed (.owned-paths.yaml:1057
  names infra/aws/globgrph the 0.7.0 infra lane; my globgrph ownership is scoped to MS-graph extraction).
  Flagged to execs that it is 0.7.0's SECOND item from me within the hour.
- ~D's scope CORRECTION accepted: my output-contract leg C shrinks 9 -> 7 tools (comp-manifest-check +
  comp-graph were their false positives; comp-graph's contract is arguably CORRECT as-is since it reports
  on both artifacts by design).
- ~B: answered all 3 census asks; extended their do-not-execute set with two READ-LOOKING WRITERS they had
  filed as reads -- comp-kuzu auto-refreshes CANONICAL on a plain query (kuzu_cli.py:58-59), and
  `deploy_ledger check --red` writes RED alerts into COO's inbox (7 real deliveries tonight prove it; the
  NAME is the trap). Redirected their telemetry plan to COMP_SYNTHETIC_FIXTURE=1 (the estate's designed
  tag) over worktree-hiding: a census that leaves no trace is its own dishonesty.
  ~B improved on my input: my "read-only only when the cache is fresh" caveat became a third class,
  CONDITIONALLY-MUTATING -- mutability is a property of the (command, cache-state) PAIR, not the command.
  Asked them to record it as TAXONOMY for CTO~Z, not a census footnote.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| deploy_ledger.py | check --red (many, pre/post fix) + --all exercise w/ redirected inbox | VERDICT->PASS | crash reproduced, fixed, denominator printed; --all discriminating 0-vs-5 |
| comp-manifest-check | (not re-run this window) | n/a | the completeness family is unchanged by this window's commits |
| comp_output_contract | contract_for("comp-iam") cross-check | PASS | proved the registry is the drifted surface, not the contract |
| argparse introspection | comp-pipescript + comp-iam declared-vs-actual | FINDING | 13v8 and 15v6; independently reproduced by ~B's static extractor |
| commit-gate / safe-commit | 3 commits | PASS | ruff caught 1 unused import (fixed); no overrides by me this window |
| pytest | test_deploy_ledger_malformed | 18/18 | 11 malformed fixtures + 7 Status-spelling variants incl. the order regression guard |

**What worked:** testing the dispatch's PREMISES before building -- two of three came back false, so I
shipped one small correct thing (`--all`) instead of three redundant mechanisms. **What I got right by
not doing it:** did not delete another lane's sole deploy record; did not build the subcommand gate without
its arch-gate. **Gap found:** the tools_index subcommand field -- populated everywhere, gated nowhere,
omitting law-mandated derivations.

## Blockers

None mine. Open items are all owned elsewhere (see Next Steps).

## Current State (zero-prior-context handoff)

- deploy_ledger: 3 fixes landed + accepted; I am OFF the thread (Andrew-direct). Remaining legs (writer
  normalization, leg-2 backlog reconciliation) are 0.7.0's, state note sent 214017Z.
- MY SURFACE unchanged + healthy: comp-output-contracts.yaml (19 declared, coverage/blind_spots/plane/
  grain/scope/exit_codes), comp_output_contract.py, manifest_check_cli.py completeness family (8 members
  incl. my output-contract + stage-2 vocab, and ~B's retired-alias). Two-stage contract COMPLETE +
  CTO~Z-accepted + ~C-token-adjudicated.
- PENDING MY ACTION on someone else's gate: the declared-subcommands-vs-argparse completeness member
  (spec + 3 constraints with CTO~Z); the output-contract plane/vintage re-declaration leg for the
  graph.json->kuzu reroute (7 tools, scoped with ~D, awaiting CTO~Z's routing).
- item-8 (comp-vendor) still has NO TO; live-pull half gated on Andrew's vendor-egress word.

## Next Steps

- [1.0.0_SA_CTO~Z] arch-gate the subcommand completeness member (+ rule whether the law-mandated omissions
  -- comp-iam simulate/reconcile, comp-pipescript postdeps, comp-registry sync -- jump the queue as a
  targeted backfill); route the kuzu reroute TO.
- [0.7.0_AE_CloudOps] mdpf stitch-definition refresh (BLOCKS ~D's pipescript reroute); deploy_ledger
  remaining legs.
- [3.0.0_SA_CVO~Z] zero-diff verify of the stage-2 reconcile @c716d963e.
- [0.8.0_AE_CloudComp] build the subcommand member on the arch-gate; item-8 on a GO.

## MCP Traffic

~26 this window (13 in / 13 out). Significant: CTO gate-integrity dispatch -> 3 fixes -> extension ->
RULING AMENDMENT (reader not writer) -> Andrew-direct STAND DOWN + handover to 0.7.0; ~B's 3 census asks ->
my rulings -> their delta -> my GATE+BACKFILL ruling -> CTO~Z arch-gate ask; ~D correction accepted +
stitch ask routed; CVO~Z R4R6 verdict for ~B noted (their malformed-probe near-miss surfaced as doctrine).
