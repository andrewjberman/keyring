# AMGT_RESAPP: the rk-48 direct act becomes admissible-terminal (as-landed pair complete)

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-21T17:1xZ at HEAD `0b71e7f5ab`. LOCAL on SITEZ.

ADJUDICATION_v17 C-S348 graded the rk-48 direct act's AC4 a FAIL that is NOT admissible under R4, and said the order
does not count terminal for the L10 read "until the never-widen pair decides the as-landed state". The pair has decided:
`ledger/NEVER_WIDEN_RK48_AS_LANDED_HALVES.md`, CTO half @`1ed2e24638`, COO half @`0b71e7f5ab`, both RETAIN, each
signed by its own seat in its own commit.

**Effect, and what it does not change:**
- The rk-48 direct act now **counts terminal for the L10 read**: the out-of-radius state it created is covered by a
  signed pair after the fact.
- **AC4 stays graded FAIL.** R4 paragraph 4: a FAIL is never flipped and a terminal instance is never re-graded. The
  record says the act wrote outside its signed radius and the state was then ratified -- both facts, not one.
- The regression the pair names -- the reason line from a readable sentence to a status code -- is owed as a
  round-19 producer cell with its own pair, before manager review. `S192` stays GRADUATED; its remediation row, owed
  at the true L10 close, reads OPEN until that cell lands.
- The COO half ran the served reading function on both versions (6 reads): reading NOT_SEARCHED 3/3 before and after,
  `urls_returned` None 3/3 both times. That is a second instrument beside this seat's source read and the CTO's; the
  three agree.

## Rows
```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S353",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T17:15Z",
    "one_line": "L9 GRADE UPDATE: the rk-48 direct act counts terminal for the L10 read -- the never-widen pair signed RETAIN on its as-landed state (CTO @1ed2e24638, COO @0b71e7f5ab). AC4 stays graded FAIL; nothing is flipped.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ledger/NEVER_WIDEN_RK48_AS_LANDED_HALVES.md: CTO half signed :63 (1ed2e24638, 1.0.0_SA_CTO~Z), COO half signed :103 (0b71e7f5ab, 2.0.0_SA_COO~Z), both RULED RETAIN.",
        "COO half's own instrument: scoped_amgt.ceo_profile_reading() run on each key's pre-act and as-landed ceo_public_profile -- reading NOT_SEARCHED 3/3 both, urls_returned None 3/3 both; only the reason line moved."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "C-S348: the direct act is not admissible-terminal until the pair decides the as-landed state.",
    "world_is": "The pair decided RETAIN, so the condition C-S348 named is met; AC4's FAIL stays in the record.",
    "notes": "Grade carrier only. The round-19 producer fix (a readable NOT_SEARCHED sentence, the code in its own field, a re-run of the three validation names under its own pair) is owed before manager review; S192's remediation row reads OPEN until it lands.",
    "dismissal_reason": "Grade record: this row updates the rk-48 direct act's L10 standing and dispositions no item; the enum has no record value."
  }
]
```
