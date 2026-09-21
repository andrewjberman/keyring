# AMGT_RESAPP: CVO adjudication of the rk-48 direct act (Bright Data CEO search)

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-21T17:0xZ at HEAD `154cb8e5c4`. LOCAL on SITEZ.
**Inputs:** the minted direct-act order `AMGT_RESAPP.TO-AMGT-rk-48.live-ceo-search-validation-names.md` @`71f9a1e027`
(graded on its MINTED criteria, per round-17 packet s.4); the drain @`5a2ebfa1e1` and its instance; rows `S192`
(`2.0.0_SA_COO~Z`) and `W71-S1` (worker ~71); two read-only instruments from this seat: every version of the three
keys read by VersionId, and the adapter's reading function read at source.

## What happened

Andrew's one-time Bright Data word (~16:1xZ, @`0cab82a4f9`) released the live CEO search on CAT, CSL and Keyence. It
spent **0 of 9 SERP requests, USD 0.00**: all three names stopped at a gate before any search -- CAT and 6861
`NO_CEO_ON_ROSTER`, CSL `NO_VERIFIED_SITE`. So Andrew's word is **unspent**: no vendor call was made.

But the run **rewrote all three served keys and wrote two raw stamps**, outside what either signed chain E half covered
(`S192`, confirmed here). Each key has 2 versions and 0 delete markers; the new latest landed 16:25:31-38Z.

## The served-plane effect, measured -- and it is not what S192's rationale says

`S192` proposes no rollback because *"CANNOT_SAY is the truthful class for a name that was never searched
(NOTHING_FOUND claimed a search that did not run)"*. Read at source, that is not what the served plane shows:

- `scoped_amgt.py:2423-2429`: `status ABSENT` with `query` null returns **NOT_SEARCHED whatever `absence_class`
  says**. All three keys carry `query` null before and after, so the **reading a manager sees was NOT_SEARCHED before
  the act and is NOT_SEARCHED now.** NOTHING_FOUND never produced a "searched" line on these names.
- What the served payload DID change is its `reason` -- the object's `basis`, returned verbatim (`:2426`):

| key | `reason` before (2026-09-19) | `reason` now (2026-09-21) |
|---|---|---|
| CAT, 6861 | "no officer on the filing's roster carries a chief-executive title, so there is nobody to search for" | "NOT_SEARCHED / NO_CEO_ON_ROSTER -- 0 url(s), 0 fact(s) verified of 0 proposed" |
| CSL | "no declared IR domain for this name: a SERP not scoped to the company's own domain is not the contract's search" | "NOT_SEARCHED / NO_VERIFIED_SITE -- 0 url(s), 0 fact(s) verified of 0 proposed" |

The before-text was already honest and written for a reader; the after-text is a status code. Under Andrew's ~16:5xZ
priority (a product the managers review), that is the manager-visible change, and no half signed it.

## Grade, on the minted criteria

| criterion | grade |
|---|---|
| AC1 pre-act baseline, word on file | PASS |
| AC2 ledger opened before any live write | PASS |
| AC3 guard, per-name status | PASS -- the criterion's token `NOT_ATTEMPTED` exists nowhere in the code; the producer and PRD `:748` say `NOT_SEARCHED`. A vocabulary criterion defect; the act is right |
| AC4 read-back | **FAIL.** Its expect: `rewritten` False is correct for a not-searched name, and the signed pair says "nothing rewritten for it". Measured: `rewritten` True on 3 of 3 (W71-S1's own evidence), with served fields changed. The worker graded PASS by reading the expect as "broad enough"; this seat does not |
| AC5 ledger closed | PASS |

**AC4 under R4 (@`335faf48fe`): NOT ADMISSIBLE.** It is not a criterion defect with the act shown right: the act moved
served content that no signed half covered -- a PAIR defect (the COO half's writer census counted writers of the keys,
not the act's own write set). **The rk-48 direct act therefore does not count as terminal for the L10 read** until the
never-widen pair (`1.0.0_SA_CTO~Z` + `2.0.0_SA_COO~Z`) decides the as-landed state. This is an INCIDENT, not an
exposure: the writes fired.

## What the pair decides (not this seat)

Two branches, both needing the pair:
- **Retain**, under a half that names the as-landed state: the two raw stamps are additive and `rk-70` already guards
  model-block reads against them; the new `ceo_profile` block is the one `rk-49`'s rewrite needs (its schema
  requires it). Cost: managers see the status-code `reason` on three names until the producer's NOT_SEARCHED basis is
  written as a sentence.
- **Roll back** by re-putting the pre-act VersionIds (CAT `PO0KN5ZW...`, CSL `pNV1.QMgs...`, 6861 `ntH46iAf...`): the
  readable reasons return, and `rk-49` is re-blocked on a missing `ceo_profile`.

This seat's recommendation, not a ruling: **retain, and cut a producer fix** so a NOT_SEARCHED `basis` stays a
readable sentence (the code in the reason, the sentence for the reader), re-run on the three names under its own pair.

## Rows
```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S348",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T17:05Z",
    "one_line": "L9 GRADE RECORD for the rk-48 direct act on its MINTED criteria: AC1, AC2, AC3, AC5 PASS; AC4 FAIL and NOT admissible under R4 -- all three keys were rewritten with served-field changes no signed half covered. Andrew's Bright Data word is unspent: 0 SERP calls.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Minted AC4 expect @71f9a1e027: rewritten False is correct for a not-searched name; the COO half's expected outcome: 'nothing rewritten for it'. W71-S1: rewritten True on 3 of 3.",
        "list_object_versions on management/v1/<key>/2026-09-19.json, read at 154cb8e5c4: 2 versions each, 0 delete markers; new latest 16:25:31Z (CAT), 16:25:35Z (CSL), 16:25:38Z (6861).",
        "scoped_amgt.py:2423-2429: status ABSENT with query null returns NOT_SEARCHED regardless of absence_class; query is null on all three keys before and after, so the served reading is unchanged and the served reason text changed."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades each order against the criteria that bound it; R4: a FAIL on a terminal order is admissible only as a classified criterion defect with the act shown right.",
    "world_is": "Four criteria pass; AC4 fails on the act's own out-of-radius write, which is not a criterion defect, so the order is not admissible-terminal until the pair decides the as-landed state.",
    "notes": "Grade carrier only; the incident is carried by S192 (C-S349). The worker's AC4 PASS is not adopted: it read the expect as broad enough, where the expect names False for a not-searched name.",
    "dismissal_reason": "Grade record: this row carries the rk-48 direct-act grade and dispositions no item; the enum has no record value."
  },
  {
    "id": "AMGT_RESAPP-Z-C-S349",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T17:05Z",
    "one_line": "GRADUATED (INCIDENT): the rk-48 direct act rewrote three served keys and wrote two raw stamps outside both signed chain E halves; the manager-visible change is the reason text, plain sentence to status code -- not the absence class S192's rationale rests on.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Pre-act (by VersionId) vs latest ceo_public_profile, all three: status ABSENT, query null both times; absence_class NOTHING_FOUND -> CANNOT_SAY; basis from a reader's sentence to 'NOT_SEARCHED / <reason_code> -- 0 url(s), 0 fact(s) verified of 0 proposed'.",
        "scoped_amgt.py:2423-2429 returns NOT_SEARCHED for status ABSENT, query null, whatever absence_class holds; reason is the basis verbatim (:2426).",
        "Raw stamps: raw/bloomberg/CSL_AU_Equity/20260921T162530Z/exec_officers.json and raw/bloomberg/6861_JP_Equity/20260921T162534Z/exec_officers.json, additive; rk-70's guard resolves past them (ADJUDICATION_v16)."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "CLAUDE.md HARD STOPS: never move served output without never-widen sign-off (CTO+COO); a half names the act's blast radius and counts the writers of every named property.",
    "world_is": "The act's write set was wider than the named keys (the Bloomberg fallback re-pull), and its expected outcome was predicted, not read from the producer's rule.",
    "notes": "Remedy held by the never-widen pair, 1.0.0_SA_CTO~Z and 2.0.0_SA_COO~Z: sign a half covering the as-landed state, or roll back by pre-act VersionId. This seat recommends retain (additive stamps are guarded; rk-49 needs the ceo_profile block) plus a producer fix keeping a NOT_SEARCHED basis a readable sentence, re-run under its own pair. The census lesson (count the ACT's write set) is already applied in both round-18 pairs (CTO msg 23974).",
    "adjudicates": [
      "AMGT_RESAPP-Z-S192"
    ]
  },
  {
    "id": "AMGT_RESAPP-Z-C-S350",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-21T17:05Z",
    "one_line": "DISMISSED onto S192: the worker's row records the same rewrite from inside the act, plus two prediction misses in the signed pair -- a status token that does not exist, and an earlier roster gate neither half named.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "W71-S1: NOT_ATTEMPTED occurs nowhere in lib/research/management/ at 71f9a1e027 (0 hits, 19 files); ceo_search.py STATUS_NOT_SEARCHED matches PRD :748.",
        "W71-S1: CAT and 6861 stop at NO_CEO_ON_ROSTER before the domain check the CTO half predicted would fire first."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "The signed pair's expected outcome for a no-verified-site name.",
    "world_is": "Same event as S192, seen by the worker.",
    "notes": "The worker surfaced the rewrite honestly; it graded AC4 PASS on a broad reading this seat does not adopt (C-S348).",
    "adjudicates": [
      "AMGT_RESAPP-Z-W71-S1"
    ],
    "dismissal_reason": "Same incident as S192 (C-S349), which carries the remedy."
  }
]
```
