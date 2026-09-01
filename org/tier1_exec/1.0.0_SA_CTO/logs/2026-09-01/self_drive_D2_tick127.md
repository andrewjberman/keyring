# /self-drive D2 — tick 127

**Seat:** `1.0.0_SA_CTO` · **State:** ARMED · **Cron:** `e106e9c8` · **UTC:** 2026-09-01 ~19:5xZ
**Ticks covered:** 127 · **Carrier:** `org/XXX.md:633` · **Paired:** `/drive` @ `2.0.0_SA_COO`

```
COMPLETION: 2 of 10 -> NOT DONE        fabric declared: 10 of 10        ledger: 40
MOVEMENT: 16 seats / 45 commits.  POSITIVE CONTROL FIRES: 1.0.0_SA_CTO = 9
register open_tos: 17 -- UNVERIFIED, see tick 125
OPEN CALLS: 0 pitched. The two long-standing cards CLOSED BY ANDREW this window.
```

⚠ **THE INVOCATION ARGUMENT IS STALE AND I AM NOT DRIVING ON IT.** It still reads *"D3 order is a
card at Andrew, unresolved."* **Andrew ruled it at ~18:2xZ: D8 SITS FIRST.** The loop order is
**D2 → D8 → D3**. A driver that kept re-reading its own invocation would have carried that card for
the rest of the session.

---

## 1. Both cards this seat carried all session are CLOSED

- **D3 vs D8 → D8 SITS FIRST.** ⭐ It survived a blanket *"All recs approved"* over a 9-card slate,
  because its rec was the explicit non-recommendation *"no recommendation with confidence."*
  **APPROVING A NON-RECOMMENDATION AUTHORIZES NOTHING**, and it took a second `/open-calls` to draw
  the real word.
- **PERFRP publish → (b)-UNNARROWED, and limb (b) PER-FAMILY.** Finding `4022ebae4a` closed on both
  limbs. ⛔ **Limb (b) had been silently treated as answered** — the ruling's *"(b)-unnarrowed"* meant
  **branch (b) of the 04:0xZ call**, not my card's limb (b). Two different `(b)`s, one paragraph.
  `3.0.0_SA_CVO` retracted its own *"no open sovereign calls remain"* and called it worse than the
  label collision I generously named it: **it dropped the limb at its own hop.**

>> **ONE LESSON, TWO MECHANISMS: a card closes silently whenever the ruling's text CAN be read as
   covering it — whether by carrying least content, or by ambiguous labelling.** <<

## 2. The loop got built, end to end, on Andrew's word

| step | artifact | state |
|---|---|---|
| 1 | `/brief-create` — **NEW SKILL** @`098a5aa28d` | built; structure LEARNED from CRO's delivered brief |
| 2 | `/endpoint --forward` Phase 0 @`3e2244fee1` | built, then refined 3× |
| 3 | `fabric` key on all ten D2 projects @`a2ff0db2e7` | **10 of 10** (estate: 349 absent, D2 was blocking) |
| 4 | `docs/architecture/_PRD_TEMPLATE.md` @`847c2ffa7c` | built |
| — | `org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md` | memorialisation, **not operational** (his word) |

**Andrew defined step 4 in conversation** — the spec named 1,2,3,5,6,7,8,9,10 and was silent on it. I
flagged the gap rather than inventing a step; he filled it: *"the PRD is the document that takes a
briefing and converts it into a project arc with a defined outcome."*

### Three refinements, each from him reading the thing and pushing back

- **`REACH` → `DONE WHEN`.** He asked what REACH meant — ⛔ **which IS the answer: the label failed
  the disputability test the skill itself mandates.** I invented it, so I owned the miss.
- **`DESIRED` is not a valid bar.** Working his question through found a design error of mine: an
  outcome delivered when someone merely *intends* it is not an outcome. The field is binary.
- **ACCEPT lines carry NO technical language**, his words. ⛔ **The reason is not style:** a line in
  system vocabulary can only be graded by someone who knows the system, **so it silently becomes a
  check the BUILDER grades** — the self-attestation this whole loop exists to prevent.

## 3. ⭐ The CVO sync, and it found a break neither of us would have hit alone

Andrew instructed it. I sent seams rather than an opening, and it returned committed bytes.

⛔ **SEAM 10→2 IS BROKEN AND IT IS MINE:** step 10 routes a SCOPE_CHANGE back to step 2, and
`/endpoint --forward` **refuses without a fresh brief and refuses to read the register** — so the
route terminates in a skill that refuses its caller.
- `3.0.0_SA_CVO` sent the exact arriving shape (`route`, `loop_target`, and the real payload
  `spec_asserts` + `world_is`) **before** I designed anything, because I asked for the shape rather
  than inventing a contract it would then have to satisfy.
- **It named the gap as MINE:** the row cannot cite which outcome was contradicted, and adding
  `outcome_ref` needs my numbering STABLE. **It was not.** Now a contract in both carriers
  @`b3584ea86a`: ids permanent, retired numbers left vacant, renumbering forbidden — because
  **a drifting id turns a grounded finding into a wrong one while it still looks grounded.**

### ⛔ And its caution is the price of Andrew's own premise

That seat shipped a gate carrying an **unratified enum value, taken from a MAP instead of the enum's
authority.** Generalised: *"the skills contain all relevant instruction"* means **every skill carries
its own COPY of a vocabulary it does not own — and copies drift while each reads as authoritative.**
**SELF-CONTAINED AND SINGLE-SOURCE-OF-TRUTH ARE IN TENSION.** Not an argument against the premise —
the price, payable if a copied value cites its authority beside it. **Debt recorded on my own three
files rather than claiming the discipline.**

⭐ **And it CHECKED where I ASSERTED:** I claimed reference docs survive only as maps; it read its own
gates and found they already carry measurement, rejected alternative, cost and non-application in
module comments. Second time today it answered an assertion of mine with a measurement.

## RESERVED cards still at Andrew

- Whether the flow-ingestion defect widens the ruled 22. **(D3-vs-D8 and the PERFRP publish card are
  both CLOSED this window.)**

## Compiler Tools

Derived cursor + FULL unbounded movement census · `directives-check.py --json` + completion and
fabric scan (denominators printed) · `comp-read` on the spec, `prd-check`, `directives-check.py` ·
full-face read over 62 TO files from 2,233 · `comp-iam reconcile` on a census I refreshed ·
`safe-commit` with post-commit STATE verification on every landing. No `head` on any census.

**PUSH STATE, MEASURED:** 9 commits LOCAL this window. `origin/CLOUD` last read `6f9bf277f1` via a
peer's `ls-remote` — **not my own read, and perishable.**

**State:** `ARMED` · next tick on the cron.
