# AMGT_RESAPP round 27: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-22T13:1xZ at HEAD after `2aa734b2d6`, LOCAL on SITEZ.
**Inputs:**
- The COO's packet `ledger/ROUND27_L8_PACKET_20260922.md` @`2aa734b2d6`, and the two orders.
- CTO msg 24221, read from the COO lane's inbox file, as the amendment's source.
- This seat's own instruments, all local: the suites on the merged tree, a git diff of rk-105's order from issuance
  to completion, and an in-process probe of the outcome projection.

## Round state

**2 of 2 terminal:**
- `rk-105`, filing_attempt SKIP-HELD / CHANGED-HELD, @`5726f647e1`.
- `rk-106`, B4 roster/domain diagnosis, read-only, @`e7c45ca8b5`.

The sweep reads PASS 9 / FAIL 0 / UNVERIFIABLE 0 of 9 over 2 orders. **Judgment census: 0.** Suites on the merged
tree: harvest **79** (72 + 7) and filings 100.

## rk-105's mid-flight amendment: checked, not just accepted

The order was modified after issuance (ISSUER AMENDMENT 1, CTO msg 24221). Rule 27 names this case: the pipeline
gate does not grade a modification, so it is a human discipline. Checked here on the diff from the issuance commit
`40f01c2b08` to the worker's completion commit `c97befa9f5`, order file only: +23/-6. It contains exactly:
- the new subclass in item 1;
- the CHANGED-HELD catch, summary and exit 2 in item 3;
- one added test;
- AC1 changed from 6 to 7, and AC2 from H0 + 6 to H0 + 7;
- the status flip.

The quoted CTO words in the amendment ("never blocks another name", "exits NON-ZERO at the end of the run") are
present in msg 24221 (1 hit each). No other criterion moved, and no `<paths>` grant moved.

**Recorded, not faulted:** the amendment's text lives in a commit authored by the WORKER, the graded party. From git
alone, an issuer edit and a self-edit of one's own criteria cannot be told apart. The chain holds here only because
the text matches the CTO's message. A future mid-flight amendment should land in an issuer-authored commit before
the worker builds.

## rk-105: the outcome projection, probed

- **Only volatile fields differ** (`retrieved_at`, `parser_version`, top-level and per-attempt `reason`, `seconds`):
  EQUAL, so SKIP-HELD.
- **One attempt's `http_status` differs:** NOT equal. It names `battery.attempts[0].http_status: 200 -> 404`, which
  is correct.
- **One extra attempt:** NOT equal, so it is refused correctly. **But the printed label is wrong:** it reads
  `battery.attempts length: 14 -> 21`. Those are counts of FLATTENED OUTCOME FIELDS (7 top-level plus 7 per attempt),
  not attempt counts (1 -> 2). This is `filings.py` `_first_differing_outcome_field`, the length branch, which uses
  `len(old_fields)` where it needs the attempts length. The line is operator-facing: `CHANGED-HELD: <key> <field>`
  prints it during the B2 run. So an operator would read "14 -> 21 attempts". **Graduated at C-S386.** The fix is
  one line, owned by the COO's next code cell. The refusal is correct; only its wording is wrong.

## rk-106 and the keying check

rk-106 changed 0 code files, and its census read 1,780 objects before and after with 0 changed. The COO re-read both
load-bearing citations. W106-S1, a cell-text defect (the "model block" is not an S3 object), is dispositioned below.

**Andrew's keying rule (msg 24223):** rk-105 adds no new key or lookup. It keys the existing write-once object by the
existing `security_key` partition. rk-106's recommendation is not built, and it reuses an existing `security_key`
lookup, which is correctly FLAGGED for the composite-FIGI design. No violation.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S385",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T13:15Z",
    "one_line": "L9 GRADE RECORD for round 27: 2 of 2 terminal, sweep 9/0/0, judgment 0; harvest 79 / filings 100 on the merged tree; rk-105's mid-flight amendment matches CTO msg 24221 exactly on the issuance-to-completion diff; no new ticker-key dependency.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_RESAPP --round 27: PASS 9 / FAIL 0 / UNVERIFIABLE 0 of 9 over 2 orders.",
        "pytest merged tree: harvest 79 passed, filings 100 passed.",
        "git diff 40f01c2b08 c97befa9f5 -- rk-105 order: +23/-6, only the subclass, CHANGED-HELD catch/summary/exit 2, one test, AC1 6->7, AC2 H0+6->H0+7, status; 'never blocks another name' and 'exits NON-ZERO at the end of the run' each found once in msg 24221.",
        "In-process: volatile-only differences project EQUAL; http_status difference names battery.attempts[0].http_status: 200 -> 404."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it; Rule 27: a mid-flight modification is a human discipline, not a gate.",
    "world_is": "Both cells meet their orders; the amendment is faithful to its source, and it was committed by the graded worker rather than the issuer.",
    "notes": "Grade carrier. For future amendments: land the amended order in an issuer-authored commit before the worker builds.",
    "dismissal_reason": "Grade record: this row carries the round-27 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S386",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T13:15Z",
    "one_line": "_first_differing_outcome_field's length branch prints the count of FLATTENED OUTCOME FIELDS under the label 'battery.attempts length' (a 1->2 attempt change reads '14 -> 21'); the refusal is correct, the operator-facing CHANGED-HELD text is wrong.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "lib/research/harvest/filings.py _first_differing_outcome_field: 'return \"battery.attempts length: %d -> %d\" % (len(old_fields), len(new_fields))' where old_fields is _filing_attempt_outcome_fields(existing), 7 top-level + 7 per attempt.",
        "Probe: one attempt vs two attempts, otherwise equal -> 'battery.attempts length: 14 -> 21'."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "rk-105 item 3: CHANGED-HELD prints the differing field from the message.",
    "world_is": "For an attempt-count change, the printed field misstates the attempt counts.",
    "notes": "A defect in operator-facing text. One-line fix: report len(battery.attempts) on each side. Target: 2.0.0_SA_COO~Z's next code cell on lib/research/harvest/filings.py. Remediation row owed at L10."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S387",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-22T13:15Z",
    "one_line": "DISMISSED onto the cell-text class: W106-S1, rk-106's text named 'the model block' as an S3 object that does not exist as such; answered via the crosswalk record, answer unaffected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "COO packet round 27 s.2 item 3; the worker answered via the crosswalk record and the diagnosis stands on battery.py:1182 and enrich.py:166-174."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "rk-106 cell text: read the model block object.",
    "world_is": "No such standalone object; the equivalent read is the crosswalk record.",
    "notes": "Issuer-text defect of 2.0.0_SA_COO~Z's, not the worker's.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W106-S1"
    ],
    "dismissal_reason": "Instance of the bar-authored-without-measuring class (C-S335); the diagnosis is unaffected."
  }
]
```
