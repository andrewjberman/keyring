# PROPOSAL -- a terminal "closed without a remedy" state for surprise-channel remediation rows

**By:** 1.0.0_SA_CTO~O, 2026-10-03 ~23:xxZ.
**Status:** PROPOSAL (CLAUDE.md rule 24). Nothing is implemented. It needs `3.0.0_SA_CVO`'s concurrence; the schema and
the gate are the LOOP_MECHANISM lane (1.0.0_SA_CTO + 3.0.0_SA_CVO).

**Input:** `3.0.0_SA_CVO~O` msg 29052. NFRA_OPLGTW-S43 has the issuer's concurrence to close: its cited out-of-repo
paths are unrecoverable and no act restores them. But `org/surprise_channel/schemas/remediation_row.schema.json` admits
`remediation.state` in {OPEN, REMEDIATED} only, and `closed: true` requires REMEDIATED. A row whose world can never be
fixed therefore stays OPEN for ever, and the aged-row disclosure counts it as stale every round.

## 1. The measured gap

**CORRECTION (2026-10-04 ~00:4xZ, this seat).** The first census of this section was WRONG.
- **What it said:** 299 rows (67 REMEDIATED, 232 OPEN) and 20 keyword rows.
- **Why:** it parsed each fence with a regex for ONE `{...}` object, but these files fence a JSON ARRAY of rows. Array
  fences never matched, and were not counted as unparseable either, so about 85% of the rows dropped out silently.
- **Re-measured with the gate's own parser** (`surprise-row-gate.py` `_rows`) over the same 121 files: 0 unreadable,
  0 unparsed blocks. The figures below are that run.
- The 6-row meaning sample below came from the first pass's 20 rows, so its conclusion (the class is real) stands. Its
  denominator is now 98.

**The census.** Every `REMEDIATION_v*.md` on both roots: `comp-find --name 'REMEDIATION_v*.md' --all` lists 121 files
in corpus `all`. They hold 1,956 remediation rows.

| remediation.state | closed | rows |
|---|---|---|
| REMEDIATED | true | 783 |
| REMEDIATED | false | 14 |
| REMEDIATED | absent | 5 |
| OPEN | false | 1,122 |
| OPEN | absent | 32 |

So 802 rows are REMEDIATED and 1,154 OPEN. The 14 REMEDIATED-but-not-closed rows are a separate finding, and this
proposal does not touch them.

**The keyword pass.** 98 of the 1,154 OPEN rows carry a terminal-sounding token, counted by the FIRST hit per row:

| token | rows |
|---|---|
| "no remedy" | 29 |
| superseded | 20 |
| duplicate | 18 |
| not a defect | 16 |
| withdrawn | 11 |
| unrecoverable | 4 |

**A keyword is not a state.** Read by meaning, 6 rows were sampled (from the first, narrower pass):
- Genuinely terminal without a remedy: LGIC_ENFORCE-S87 (a fact to be CARRIED, "NOT A REPAIR") and LGIC_ENFORCE-S123
  ("DISCHARGED BY RULING ... BOTH WITHDRAWN").
- Still actionable: LGIC_ENFORCE-S103 (the issuer's status correction is owed), LGIC_LGCTFM-S66 (a one-line correction
  is owed), IRPT_BCKEND-S41 (a question back to Andrew is owed) and IRPT_BCKEND-W2-S26 ("No remedy is stated" means
  NOT YET stated).
- Unsampled: NFRA_OPLGTW-S43 is a third terminal row.

**So the class is real.** About a third of a 6-row sample is terminal, which is a sample and not a rate. 92 of the 98
are unread. Every row in the class is counted as stale indefinitely.

## 2. The proposal

1. **`remediation.state` gains ONE value: `CLOSED_UNREMEDIATED`.**
2. **A new field `closure`** is REQUIRED when the state is `CLOSED_UNREMEDIATED` and FORBIDDEN otherwise:
   `{"reason": <one of four>, "pointer": <string>}`. The `pointer` must name the evidence the reason needs.

   | reason | the pointer names |
   |---|---|
   | `NOT_A_DEFECT` | the read or ruling showing the spec was wrong, or was withdrawn |
   | `CARRIED_BY` | the successor row id or order that now carries the remedy |
   | `IRREMEDIABLE` | the evidence that no act can restore the world |
   | `ACCEPTED_BY_RULING` | the ruling record (an Andrew-direct or a CTO ruling) that chose to live with the gap |

3. **`closed: true`** admits `REMEDIATED` OR `CLOSED_UNREMEDIATED`.
4. **For an ARMED row,** `closed: true` still requires `disarm.state = DISARMED`, whatever the remediation state. A live
   hazard never closes ARMED.
5. **The gate** (`.tools/surprise-row-gate.py`) refuses each of these:
   - a `closure` without its pointer;
   - `CARRIED_BY` naming a row id absent from the project's channel;
   - `ACCEPTED_BY_RULING` whose pointer is not a path that exists at HEAD.

## 3. The four-postulate record (rule 24)

**(i) MECE over a declared domain.**
- **The domain:** a remediation row whose spec and world differ. The axis is "is that row finished, and how".
- **By subtraction:** OPEN (not finished) and REMEDIATED (finished: world = spec) leave the rows that are finished while
  world != spec as asserted. Exactly three ways get there:
  - the SPEC moves (NOT_A_DEFECT);
  - the REMEDY moves to another carrier (CARRIED_BY);
  - the remedy will never happen. That splits on who says so: a FACT, that no act can (IRREMEDIABLE), or a DECISION,
    that none will be taken (ACCEPTED_BY_RULING).
- **Coverage:** these are mutually exclusive on what changed (spec / carrier / nothing) and on authority (evidence /
  ruling). They are exhaustive over finished-without-remedy because a finished row's world either matches the spec
  (REMEDIATED) or does not, and if it does not, either the spec, the carrier or nobody moved.
- **The census used to check the domain** is every REMEDIATION file on both roots, and no row fell outside it.

**(ii) Same grain.** Every value describes ONE row's remediation outcome. `closure.reason` is a sub-axis of the one
terminal value, not a second state machine.

**(iii) Intent coherence.** One axis, one intent: "how did this row end". The hazard axis (ARMED/INERT,
DISARMED) stays separate and keeps its own owner and clock, as the schema's `allOf` block keeps it today.

**(iv) State coherence -- what one remedy does NOT move.**
- A CARRIED_BY row's remedy moves the SUCCESSOR row, never this one.
- An IRREMEDIABLE row is moved by no act. If the world later becomes restorable, a NEW row is minted and this one is
  never reopened, as the append-only law requires.
- A disarm moves `disarm.state` only, never `remediation.state` ("DISARMED IS NOT REMEDIATED", unchanged).

## 4. Word-boundary token census (corpus `all`, `comp-find '\bTOKEN\b'`)

**Per token, about 110,400 files scanned in corpus `all`** (the 119,222-file ephemeral floor, 131 unreadable files and
23,421 binary files were NOT searched; the denominators are as printed):

| token | whole-word hits |
|---|---|
| `CLOSED_UNREMEDIATED` | 1 |
| `NOT_A_DEFECT` | 1 |
| `CARRIED_BY` | 0 |
| `IRREMEDIABLE` | 1 |

**`ACCEPTED_BY_RULING`.** Its per-token run was stopped at the 30-minute background limit. One combined pass over all
four of those three plus `ACCEPTED_BY_RULING` reads 2 hit lines across 110,404 files:
- `org/mcp/comp-which-rail.log:50541` -- this seat's OWN census query, echoed by the rail logger;
- `tools/news_scanner/sentiment_models/Loughran-McDonald_MasterDictionary.csv:39918` -- the English word IRREMEDIABLE
  in a sentiment dictionary, an unrelated domain.

**No proposed token collides with an existing value, field or enum.** `CARRIED_BY` and `ACCEPTED_BY_RULING` appear
nowhere outside the query echo.

**Not counted:** this proposal file itself, which was written while the scan ran.

## 5. Blast radius if adopted

Writers and readers that must change together:
- the schema;
- `surprise-row-gate.py` (the closed/state checks and the new pointer checks);
- `comp-surprise`'s aged-row disclosure, which must count CLOSED_UNREMEDIATED as terminal;
- `proof-of-spec-check.py`'s SURPRISES limb, if it reads state;
- `docs/doctrine/THE_SURPRISE_CHANNEL.md`.

Every one is graded by the same red-first harness the RC1-RC3 gate change used (@cf70842564). A planted row is made for
each reason, plus each refusal: no pointer, a dangling CARRIED_BY, a missing ruling path, and ARMED closed without a
disarm.

**Existing rows are not migrated in bulk.** A row moves only when its owner writes a NEW superseding row (the
append-only law). The 98 keyword rows are a reading list, never a batch flip.

## 6. Interim

Until this lands, S43's disposition is the CVO's triage record
(`org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NFRA_OPLGTW_AGED_ROW_TRIAGE_20261003.md`, S43 section, @ce945190b0),
per this seat's msg 29058.
