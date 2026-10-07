# /self-drive laptop directives -- tick 1 (2026-10-07 ~07:1xZ)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_071xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_AS_CLUSTER_CONTROL_PLANE.md`
@22fa62cc8b. **Cadence:** 60m, cron `77f028d5` (session-only). **paired_with:** solo. **state: ARMED**

## Scope

`laptop directives` -> 10 of 15 live directives (D0, D2, D3, D7, D8, D9, D10, D11, D13, D14) -> 56 register members, 63 open task
orders by the register's own count (`directives-check --json`). D10 carries NO-MEMBERS and MEMBERS-STALE: the test for it is
UNMEASURABLE until the register names its projects (a register fix, `0.0.0_AB_MSTR`'s).

## Measurements

- Sequence (`sequence-check`, file @3ff3b79d01): 26 placed, stage enum OK, no DRIFT, no UNREADABLE, no OUT-OF-SEQUENCE. Capacity 2 of
  3 COO lanes on the laptop (`~C`, `~M`).
- Inbox: 0 unread; delivery state 9 of 9 READ since 06:00Z. Active commitments: 0 lines in the last 24 hours across 69 ledgers.
- Trunk: origin CLOUD `c869ab0e4f`, laptop 36 ahead and 72 behind at 07:0xZ; `0.0.0_AB_MSTR`'s merge window OPEN (msg 106019) on
  Andrew's "Push".
- Dells: both on the tailnet; both inbound queues depth 0; no Dell acknowledgement of the seating relay has reached this seat.

## Calls ruled this tick (the driver's own REC, each)

| # | Call | Ruling | Reason |
|---|---|---|---|
| 1 | `3.0.0_SA_CVO`'s two wording findings on NFRA_CTLPLN v0.9 (msg 106015): now or next addendum | NOW, as v0.11 | The CVO is live and a stale SOURCE line that contradicts its own headline is the kind a later reader builds on. |
| 2 | `2.0.0_SA_COO~M` is idle on the laptop with MDPF_SECCLASS's decomposition next, and its successor `~M1` is not yet seated on dell1 | `~M` runs the signed rule-B remap and the v0.12 decomposition on the laptop now; `~M1` issues and executes on dell1 | Planning is the laptop's role under C-ROLES; the remap already holds both halves; idling a live seat for a Dell acknowledgement is the wait Andrew ruled out tonight. One issuer per round holds: `~M` issues nothing. |
| 3 | The laptop's third COO slot and the dark LGIC lanes (LGIC_ENFORCE, LGIC_CANON, LGIC_LGCTFM; `~G` not live) | Not seated this tick | The Dells' real load is unread until they acknowledge; the slot is ruled at tick 2 with that read. |
| 4 | MDPF_TAXSMA's six open order faces after Andrew's close | Their terminal flips go to the first D8 COO lane seated on dell1 | The issuer lane `~T` is not live, and `~C` is NFRA_CTLPLN only on Andrew's word. |
| 5 | The manual gates on MDPF_SECHIST and IRPT_CUSTDY ("the box's fabric manager is live on its own inbound queue") | Stay UNMEASURED | A queue at depth 0 cannot tell consumed from discarded; the gate is confirmed on a Dell's own acknowledgement, not on depth. |

Earlier this session, before the arm, and on record: the CT-c-5 form, rows W4-S1 to W4-S4 with the CTO half for the create grant, the
MDPF_SECCLASS-S39 roll-back, the park-or-close first pass.

## Acts taken

- NFRA_CTLPLN PRD v0.11 (this commit): FWD-5 SOURCE and C-ROLES; the ratified-text half re-opens for `3.0.0_SA_CVO`.
- One message to `2.0.0_SA_COO~M` with ruling 2.

## Acts only Andrew can do

- Start a Claude session for dell2's fabric manager if none is running there (unconfirmed from here): his own sign-in on the box.
- The IRPT_YCDGEN report retry: his own sign-in in the browser (`2.0.0_SA_COO~Y` handoff @217963b67d, "AT ANDREW (a)").
- ADVI_BILLING and NFRA_OPSWKF inputs: each firm's billing answers, and his sitting with the operations lead (`SEQUENCE.yaml` manual
  gates; a vendor or a person only he reaches).

## Completion test

NOT DONE. Read from the register: the scope holds active projects on every directive but D7 and D10; D10 is UNMEASURABLE. No member
was classified UNREACHABLE this tick.

## Owed by this seat, carried to the next ticks

- The park-or-close second pass (`CTO_ADJUDICATION_PARK_OR_CLOSE_FIRST_PASS_20261007.md`, section "Second pass").
- Confirm the two manual gates when each Dell acknowledges.
- The L10 read for NFRA_CTLPLN round 2 when `3.0.0_SA_CVO` cuts its slug (9 rows undispositioned at 06:1xZ).

## Compiler Tools

| Tool | Purpose | Result | Note |
|---|---|---|---|
| `directives-check.py --json` | resolve the scope | PASS | `as_of` prints None |
| `sequence-check.py` | sequence against the repo | PASS | its validator refused a `why` containing "seated" earlier tonight; reworded |
| `missions-tree-index.py check` | tree and index | PASS | R6 refuses a CLOSED flip without the two completion documents |
| `prd-signoff.py status` | sign-off state | PASS | reads the ENDPOINT hash, so a contract-only addendum re-opened nothing |
| `comp-surprise --project` | channel rollup | PASS | a pipe to `tail` is refused by the rail; run it bare |
| `active-commitments.py` | fabric promises | PASS | 0 lines in 24 hours |

- **What worked:** writing each multi-file edit as a script file and running it, after a heredoc with nested quotes failed in the shell.
- **Gap found:** no committed list backs the layout record's "34 quiet or cold projects"; the population was re-derived by subtraction.
