# MDPF Atomic Window — Crash Recovery + Full Close (0245–0345Z)

**archetype:** COORDINATE

## What happened

Predecessor COO session crashed mid-window (~0226–0231Z, after opening ledger 20260811T0150Z and
firing the L-A/L-B GOs). This session: /watcher armed (task b66sfv4cf, no orphan, clean re-register
PID 5820), startup protocol run, then the window coordinated from recovery to CLOSE @d45823dea5
(final record @14d4bcad51).

## The arc, by ledger commit

- @90822a5e76 — recovery ruling: crash = coordination interruption, NOT a leg failure; fail-both
  does not fire; FORWARD-COMPLETE ratified (CTO rec, COO concur).
- @13a4cecce8 — L-A + L-B CLOSED on applied-truth evidence (DS 3-layer verify; CTO+AE convergent
  live schedule reads, 0-drift, applies completed pre-crash).
- @4c10918958 — L-C first cycle 6/12: cottonwood differing-dollars guard refusal classified
  pre-existing/decoupled; 13:30Z interpretation table PRE-REGISTERED before evidence.
- @6dc47fc83a — WINDOW-EXISTENTIAL (DS, 3 derivations): the floor fires mdpf-gold-lambda pinned
  @0bc739e7d5 (pre-fix) — two code channels, fix on the one the floor does not read;
  comp-pipescript deployed structurally blind to the lambda zip channel (instrument gap → CTO).
  COO ruling: spec gap, not leg failure; L-D added.
- @22aae247ef — L-C verdicts: item-2 SPLIT (emitted FAIL / landed code PASS), item-3 PASS closed.
- @7067556768 — ANDREW-DIRECT supersedes L-D shape (canonical bucket, colocate opal-data-assets);
  COO 031158Z GO superseded at AE same turn (instruction conflict removed explicitly).
- @9b083a39a1 — crossed-in-flight: the GO'd apply had COMPLETED ~0318Z pre-hold; correct content
  EXECUTING; COO input relocate-over.
- @31cf67ee39 — CTO RULED relocate-over (converged); canonical path routed; discriminators refined
  (sha-unchanged expected-not-discriminating; canonical key + new s3_object_version + GetObject
  fails-loud are the oracles).
- @588bb50018 — L-D-canonical DONE; re-fire GREEN 12/12, cottonwood BUILT (point-in-time impl);
  provenance validation opened at CTO; DS named rekey-report reader.
- @d45823dea5 — WINDOW CLOSED: 12/12 = build+label correctness per the 08-10 ruling, NOT
  value-settledness (CTO guardrail verbatim); residuals carried with owners.
- @b2290412cf — (a) RATIFIED cite @e82326bdb2 (Andrew verbatim "Point-in-time, history does not
  restate"; ruled table = tonight's exact collision) → 13:30Z publishes face 12/12 on a ratified
  basis; DS deep rekey read zero-discrepancy at source grain; tags cut.
- @14d4bcad51 — push attribution corrected: COO push attempt correctly BLOCKED by LD-0367 r2 /
  LD-0368 (MSTR is the sole shared-branch integrator); integration push + 3 tags routed to MSTR
  (request 034417Z). The fix is LIVE regardless — the push publishes the record.

## Live state at log time

- Executing code: mdpf-gold-lambda sha t0w3vTNV… = @bf74d031c1, env MDPF_GOLD_COMMIT full-hash,
  artifact at canonical s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip.
- Cadence live 0-drift: pulls 13:02Z · floor 13:30Z · bridge 14:10Z · publisher 14:20Z ·
  mirror-inf 15:05Z · cot 18:30 ET unchanged; W4 selectors {"firm":"inf"}/{"firm":"cot"}.
- Tags cut (unpushed until MSTR window): mdpf-pipeline-v2.1.0 · opal-assets-v0.40.0 ·
  smartx-pipeline-v1.9.0.

## Open at this seat

1. **13:30Z bar adjudication (COO, ~10h)** — face 12/12 on the ratified basis; executing-code
   precondition satisfiable as written (sha-claim split recorded for the reader); ledger ADDENDUM
   after the cycle. Non-cottonwood degradation = failure, loud.
2. **MSTR push confirmation** — verify remote CLOUD + tags visible when MSTR reports.
3. **C-2/C-3 producer-fix routing to DS/AE post-bar** (banked 032240Z with MSTR nudge backstop).

Open elsewhere, correctly: C-1 revaluation asymmetry (CTO→Andrew, de-escalated by CTO's own
correction) · estate-wide point-in-time extension census (CTO, diagnostic) · two-live-code-channels
residue + 17b grammar observation (CTO, DS-flagged) · comp-pipescript lambda-channel blindness
(CTO, instrument gap).

## Compiler Tools

| Tool | Result |
|---|---|
| comp-which (A.3 exercise probe) | Forwarder RAN (banner produced) — rail healthy, 96/97 resolve bare |

Coordination seat this session: the leg evidence I validated carried the seats' own comp-tool runs
(DS's comp-pipescript deployed MATCH on L-A; the graph tools were not the right instrument for any
COO-side question tonight — every verification was routed to the owning seat's live primitives).
Instrument GAP surfaced instead: comp-pipescript deployed is structurally blind to the Lambda zip
code channel (returned MATCH while executing code was 4 days stale) — routed to CTO as a defect per
Rule 22.

## Notes for the record

- Two of my own written oracles were corrected by peers mid-window (sha-unchanged as re-home oracle;
  COO-as-integrator push attribution). Both corrections adopted verbatim, both now in the ledger —
  the gate catching the second one live is the control working.
- The pre-register-before-evidence discipline earned its keep twice: the 6/12 table (written before
  CTO's converging input arrived) and the executing-code precondition (which made the first L-C
  cycle's green un-adjudicable as a pass — correctly).
