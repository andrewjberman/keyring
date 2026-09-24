# AMGT_RESAPP round 19: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-21T20:2xZ at HEAD `7e5612369e`. LOCAL on SITEZ.
**Inputs:** the COO's packet `ledger/ROUND19_L8_PACKET_20260921.md` @`7e5612369e`; the four orders; the channel census
(34 carriers, 7 UNDER_INVESTIGATION before this document).

## Round state

**4 of 4 terminal** (`rk-76` @`e37f29cc16`, `rk-75` @`f33b359869`, `rk-77` @`03af0dd7a9`, `rk-78` workspace
@`a6ada7dc1a`, portal branch `wk-amgt-19-78-portal` @`95d96edb` UNPUSHED). Acceptance **PASS 26 / FAIL 0 /
UNVERIFIABLE 0 of 26 over 4 orders**; the order files carry 26 criterion ids (8 + 6 + 6 + 6); **judgment census 0 of 4.**

## The page is not yet ready for the judgment the managers' review will close

`rk-43` AC5 ("the rendered Exec Management tab tells the reader the truth about each served name") stays NOT_EVALUATED:
its instrument is a headed session on the real page. The COO's `/frontend-dev` screenshots are a local render of an
UNPUSHED branch against live `/thesis` bodies -- real evidence, not the named instrument, and not converted into a
verdict (C-S273 precedent). But they show that **the bar would FAIL on today's page for reasons R20-A does not touch:**
- **`S202` (ARMED):** CAT, a validation name, serves ONE officer (its Chief Legal Officer) as its whole RESOLVED roster,
  because its 10-K Item 10 says the officers "appear in Item 1D" and the parser does not follow the reference. The page
  shows no CEO and presents a one-line roster as complete -- a claim that is not true.
- **`S201`:** a "from the filing" subtitle sits over a Bloomberg-fallback table -- a false source claim on a reader line
  -- and every not-searched CEO line ends in a doubled full stop.

So the Exec Management capture should follow R20-A AND the `S201`/`S202` fixes; the Model and Security Analysis tabs
(`rk-2` AC6, `rk-8` AC4) are unaffected and can be captured at any time.

## Dispositions (7 open -> 1 open, `W37-S1`)

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S358",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T20:25Z",
    "one_line": "L9 GRADE RECORD for round 19: 4 of 4 terminal, acceptance 26/0/0 of 26, no judgment criterion; rk-43 AC5 stays NOT_EVALUATED, and the available screenshots show two defects R20-A does not fix that would fail its bar today.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Order files at 7e5612369e: rk-75 8, rk-76 6, rk-77 6, rk-78 6 criterion ids; parser reads the same; judgment=\"true\" in 0 of 4; --acceptance --round 19: PASS 26 / FAIL 0 / UNVERIFIABLE 0 of 26 over 4 order(s).",
        "Round-19 packet s.1: /frontend-dev screenshots of wk-amgt-19-78-portal @95d96edb against live /thesis bodies; S201 and S202 were filed from them."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "All 26 criteria pass; the page they build is not yet truthful on CAT (S202) or on the fallback table's source line (S201).",
    "notes": "Grade carrier only. The Exec Management capture for rk-43 AC5 waits for R20-A and the S201/S202 fixes.",
    "dismissal_reason": "Grade record: this row carries the round-19 L9 grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S359",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T20:25Z",
    "one_line": "GRADUATED: CAT, a validation name, serves a one-officer roster (its Chief Legal Officer) as complete and RESOLVED, because the parser does not follow its 10-K Item 10 cross-reference to Item 1D -- no CEO on the page.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S202 (2.0.0_SA_COO~Z, from its own screenshots and the live thesis leaf): CAT_US_Equity serves 1 officer, Derek Owens, Chief Legal Officer, roster_source FILING, RESOLVED; reads NO_CEO_ON_ROSTER.",
        "Round-19 packet s.3: the filing's Item 10 says the executive officers appear in Item 1D; the parser does not follow the reference."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "C-EXEC-MANAGEMENT: the Exec Management tab tells the reader the truth about each served name; only a zero-officer roster is withheld.",
    "world_is": "A partial roster is served as complete for a validation name, and it hides the CEO.",
    "notes": "Remedy, holder 2.0.0_SA_COO~Z: the roster parser follows an Item 10 cross-reference to the section it names (Item 1D here), or, where it cannot, marks the roster INCOMPLETE rather than RESOLVED. The most manager-visible open defect on the validation names; it gates the managers' review of the Exec Management tab.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S202"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S360",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T20:25Z",
    "one_line": "GRADUATED: the Exec Management tab puts a 'from the filing' subtitle over a Bloomberg-fallback table -- a false source claim -- and ends every not-searched CEO line with a doubled full stop.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S201 (2.0.0_SA_COO~Z, from its /frontend-dev screenshots of wk-amgt-19-78-portal @95d96edb): '... so the CEO web search was not run..' on every NOT_SEARCHED name; the 'from the filing' subtitle renders over CSL's BLOOMBERG_FALLBACK table.",
        "rk-78 renders roster_source on each row ('per Bloomberg, not the filing'), so the subtitle contradicts the rows beneath it."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "C-EXEC-MANAGEMENT: a fallback roster is labelled with its roster_source; a served line is a readable sentence.",
    "world_is": "The table's own rows say Bloomberg while its subtitle says the filing; the sentence ends '..'.",
    "notes": "Remedy, holder 2.0.0_SA_COO~Z: a portal fix -- the subtitle reads from roster_source, and the CEO line's terminal punctuation is not doubled. The cheapest manager-visible fix open.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S201"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S361",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T20:25Z",
    "one_line": "GRADUATED: two of three validation names served no management under a false ZERO_OFFICERS label; the adapter half is live (rk-77), the page half lands only with rk-78's portal push and the PROD promote.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Round-19 packet s.1: live CodeSha256 hP+6OO5P...; thesis leaf for CSL SERVED BLOOMBERG_FALLBACK 14 officers, 6861 1 officer, ASML ABSENT ZERO_OFFICERS 0.",
        "Portal branch wk-amgt-19-78-portal @95d96edb is UNPUSHED; the DEV push is 0.0.0_AB_MSTR~Z's (LD-0522), the PROD promote standing under the CTO adjudication @c7bbb53f2a item 1."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "C-EXEC-MANAGEMENT: the Bloomberg fallback fills the table labelled with roster_source; only a zero-officer roster is withheld.",
    "world_is": "The adapter now serves the fallback rosters; the page that renders them is on an unpushed branch.",
    "notes": "Remedy remaining: rk-78's portal DEV push (0.0.0_AB_MSTR~Z) and the PROD promote (the DT owner). Its remediation row reads REMEDIATED once the served page is read back with the fallback line.",
    "adjudicates": [
      "AMGT_RESAPP-Z-S194"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S362",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T20:25Z",
    "one_line": "DISMISSED onto S197: CSL's served roster reason is its raw attempt log, not a readable sentence -- remedied by R20-A's second write, the cell S197 (C-S356) carries.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S200: CSL's served roster_reason is stale and technical under PRD v0.16's readable-reasons rule.",
        "1.0.0_SA_CTO~Z msg 24050 item 5: R20-A widens to a second write, CSL's roster_reason only, re-derived as a sentence from the current filings object; no search, Bloomberg call or pool write on CSL."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "C-EXEC-MANAGEMENT (v0.16): a served reason is a readable sentence.",
    "world_is": "CSL's reason is an attempt log until R20-A rewrites it.",
    "notes": "Same cell, one pair, two keys (6861 and CSL).",
    "adjudicates": [
      "AMGT_RESAPP-Z-S200"
    ],
    "dismissal_reason": "Remedied by R20-A's second write, carried under S197 (C-S356)."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S363",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T20:25Z",
    "one_line": "DISMISSED: two worker rows with no grade impact -- a heading count in a criterion's prose (1 stated, 2 measured) that no refusal rule used, and a CRLF checkout fixed on disk with LF committed.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W75-S1: both never-widen halves carry two headings naming rk-75 (an H1 and an H2); AC1's refusal rule never fired (packet s.2 item 2).",
        "W78-S1: the worktree's core.autocrlf=true checked out CRLF; every committed blob is CRLF 0 and non-ASCII 0 (packet s.1, s.2 item 3)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Each criterion's literal expect.",
    "world_is": "Each diverged in a way that moves no grade.",
    "notes": "W75-S1 is another instance of the bar-from-memory class (C-S335).",
    "adjudicates": [
      "AMGT_RESAPP-Z-W75-S1",
      "AMGT_RESAPP-Z-W78-S1"
    ],
    "dismissal_reason": "No grade impact; the committed state is correct."
  }
]
```
