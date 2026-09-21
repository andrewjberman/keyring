# AMGT_RESAPP: CVO adjudication of the Keyence CEO and roster-reason rows (S195, S197)

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-21T19:5xZ at HEAD after the v0.16 stamp. LOCAL on SITEZ.
**Inputs:** rows `S195`, `S196`, `S197`; PRD v0.16 @`2d0da569e7` (ratified-text signed by this seat, review @`4e83003847`;
PRD ADMITTED); `1.0.0_SA_CTO~Z` msg 24034 naming round 20 as ONE cell, R20-A, on ONE key.

Both rows describe `6861_JP_Equity` (Keyence), a validation name, and both are remedied by the same cell:
- `S195`: Keyence reads NO_CEO_ON_ROSTER although its one officer is the President; the rule now sits in
  C-EXEC-MANAGEMENT (v0.16): a Japanese-listed President is the chief executive when no CEO title exists.
- `S197`: Keyence's served roster reason prints a literal `None` and an internal id ("the persisted None filing
  doc-..."), because `roster.py:944-947` formats a missing `form` with `%s`; manager-visible since rk-77. v0.16 binds a
  served reason to a readable sentence with no literal missing value.

R20-A carries both: the reason wording, the JP-President rule, and ONE re-projection of Keyence's management object,
under one never-widen pair. `S197` is the anchor because it is live on the served page today; it stays GRADUATED, not
dismissed, until R20-A lands and the served reason reads as a sentence.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S356",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T19:55Z",
    "one_line": "GRADUATED: Keyence's served roster reason prints a literal None and an internal id to a manager; the readable-reason rule is now contract (C-EXEC-MANAGEMENT, PRD v0.16) and its remedy is round-20 cell R20-A.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S197: served roster_reason 'the persisted None filing doc-1defdb68a7ffd3b7 carries an EMPTY officer section ...'; roster.py:944-947 formats source_object.get('form') with %s and a non-EDGAR doc- object carries form None.",
        "PRD v0.16 @2d0da569e7 C-EXEC-MANAGEMENT: 'A served reason is always a readable sentence; a missing value is never printed into it as a literal.' Signed by this seat, review @4e83003847."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "C-EXEC-MANAGEMENT (v0.16): every served reason is a readable sentence.",
    "world_is": "Keyence's served reason carries a literal None and an internal document id.",
    "notes": "Remedy: R20-A (holder 2.0.0_SA_COO~Z), one cell on one key under one never-widen pair: the reason wording, the JP-President rule, and one re-projection of 6861_JP_Equity. Its remediation row reads OPEN until the served reason is read back as a sentence. The CEO line will then say the CEO is identified and the search not run, since the Bright Data word for Keyence is still Andrew's.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S197"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S357",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T19:55Z",
    "one_line": "DISMISSED onto S197: Keyence's President not recognised as CEO -- the ruling is now contract (C-EXEC-MANAGEMENT, PRD v0.16) and its code lands in the same R20-A cell S197 carries.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S195: Keyence's one stored officer, Tetsuya Nakano, role 'President' (source bloomberg), reads NO_CEO_ON_ROSTER.",
        "S196 (2.0.0_SA_COO~Z) disarmed S195 against the CTO's ruling; PRD v0.16 C-EXEC-MANAGEMENT carries it: a JP-listed President is the chief executive when no chief-executive title exists, not extended elsewhere without evidence."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "The CEO rule requires a chief-executive title.",
    "world_is": "For a Japanese issuer the President is the chief executive; the contract now says so, scoped to that jurisdiction.",
    "notes": "One cell, one key, one pair: R20-A carries this and S197 together.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S195"
    ],
    "dismissal_reason": "Ruled into contract at PRD v0.16; implemented by R20-A, the cell S197 (C-S356) carries."
  }
]
```
