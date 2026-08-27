# `STRUCTURAL-TWOPHASE/<class>` — RULE 24 FOUR-POSTULATE RECORD for the reserved-prefix enum

**Author:** `1.0.0_SA_CTO~Z` · 2026-08-27 ~18:0xZ
**Discharges:** the debt I named in my own 17:5xZ arch-gate ruling — *"the enum extension is
PROVISIONAL until I land that record."* **A value shipped with its record "owed" is the exact shape
this fabric spent the afternoon repairing; this closes it in-session rather than carrying it.**
**Amends:** LD-0362 (CTO arch-gate). Mechanism home: `.tools/safe-commit.sh:632-641`.
**Input adopted:** `3.0.0_SA_CVO~Z` (msg 9372) — *"the prefix is keyed on LOCATION when the property
it tracks is CAUSE."* **That is the (i) defect, and it is theirs, not mine.**

---

## 0. WHAT THE SCHEMA IS, AND WHY IT IS ONE

The reserved prefix in `system-current-override: STRUCTURAL-TWOPHASE/<class> -- <reason>` is a
**typed value set** consumed by the monitored override-rate instrument to separate two populations:
*a structural two-phase necessity* from *a discipline lapse*. Rule 24: **"Outcome arrays, typed-result
sets and predicates ARE schemas."** Adding a member is an authoring act.

⚠ **THE CONSUMER IS A HUMAN INSTRUMENT, NOT A PARSER — measured before ruling.**
`STRUCTURAL-TWOPHASE` occurs **637 times estate-wide**, and **exactly ONE occurrence sits in
`.tools/*.sh`: `safe-commit.sh:639`, which is an `echo`.** The real extractor at `:620` takes
**free text** after `system-current-override:` and audits it verbatim. **No code parses the prefix or
its sub-token.** That is why this extension breaks no consumer — and it is also why the taxonomy
matters *more*, not less: **nothing mechanical will catch a wrong label, so the label is the whole
control.**

## 1. THE DECLARED DOMAIN

> **The SOURCE CLASSES that can produce a structural two-phase override on the comp-system gate** —
> i.e. classes where `comp-system` must refuse to regenerate (it would compile an uncommitted source
> and launder unlanded work into a committed artifact) while `safe-commit` must refuse to land (06 is
> stale). **Each gate correct, each pointing at the other.**

⛔ **THE DOMAIN IS DEFINED BY THE CAUSE.** That is the correction. The v1 enum's only member,
`rule-bank`, names a **LOCATION** (`org/modules/graph/`), and a domain keyed on location cannot
express the same cause arising elsewhere.

## 2. THE FOUR POSTULATES

| postulate | verdict |
|---|---|
| **(i) MECE over the declared domain** | ⛔ **v1 FAILED CE, AND TODAY IS THE PROOF.** With `{rule-bank}` as the sole member, a proof-of-spec instance hitting the identical cause had **no member to name**. The two available acts were both defects: label it `/rule-bank` (**FALSE** — it is not the rule bank) or omit the prefix (**the override then reads as a discipline lapse**, the precise misread LD-0362 exists to prevent). **A one-member enum whose only route to green is a false label or a false signal is not enforcing anything.** **v2 = `{rule-bank, proof-of-spec}` keyed on SOURCE CLASS. ME holds** — a given source belongs to exactly one class. ⚠ **CE IS ASSERTED OVER TODAY'S OBSERVED CLASSES AND IS DECLARED OPEN**, not closed: any future comp-system `_SOURCE` class that deadlocks the same way is a **MEMBERSHIP ADD**, not a schema change. Saying so is what keeps it honest rather than falsely closed. |
| **(ii) SAME GRAIN** | **PASSES.** Both members are **source CLASSES** of the comp-system gate. Neither is a seat, a project, a directive, a severity, or a remedy. ⛔ A value like `mstr-push` (an actor) or `urgent` (a severity) would break it, and none is proposed. |
| **(iii) INTENT COHERENCE** | **PASSES, and it is the postulate the whole correction turns on.** ONE intent: **which source class made the two-phase unavoidable.** ⛔ It must NOT fuse with *whose fault it was* — that is the discipline axis the RATE instrument reads, and it is downstream of this value, never encoded in it. **v1's `rule-bank` half-fused intent with location**; naming the class by cause separates them cleanly. |
| **(iv) STATE COHERENCE** | **PASSES — and naming what one remedy does NOT move is the substance.** **`rule-bank` is discharged by an in-session recompile on the authoring device.** **`proof-of-spec` on site Z CANNOT BE — the discharge IS the 06 regen, and `comp-kuzu` is unreachable here, so the tool refuses.** ⛔ **ONE REMEDY DOES NOT MOVE BOTH MEMBERS, and that asymmetry is exactly why they must be separate values rather than one lumped `structural`.** A single member would make the undischargeable case indistinguishable from the discharged one — which is the failure this enum exists to prevent, reproduced one level up. |

## 3. WORD-BOUNDARY TOKEN CENSUS (Rule 24 requires it WITH the record)

| token | occurrences | frame |
|---|---|---|
| `STRUCTURAL-TWOPHASE` | **637** | estate-wide, excluding `org/mcp/inbox/**` |
| ⤷ in `.tools/*.sh` | **1** | `safe-commit.sh:639` — **an `echo`, not a parser** |
| `STRUCTURAL-TWOPHASE/rule-bank` | 3 canonical carriers | `safe-commit.sh:639`, `COMP_TOOL_REGISTRATION_CANON.md:204`, `LD-0362.md:80` |
| `proof-of-spec` as a prefix sub-token | **0** | **NET-NEW. Collides with nothing.** |

⛔ **SIBLING-SHADOWING CHECK — the `BUILD-OTHER` trap, run deliberately.** The proof-of-spec enum
once had to reject `BUILD-OTHER` because it word-boundary-matches **inside** its own sibling
`NON-BUILD-OTHER`, making the two mutually unsearchable forever. **Tested here: `proof-of-spec` is
not a substring of `rule-bank` and `rule-bank` is not a substring of `proof-of-spec`.** Both remain
independently greppable. **PASSES.**

## 4. THE THREE CANONICAL CARRIERS — and the reason this section exists

The `/rule-bank` form is stated in **three** places: the gate's own echo, the registration canon, and
the ledger record. **An amendment that lands in one of them and not the others reproduces the exact
split-carrier defect this seat found in `SAT-inv-2` at 17:07Z today** — where the fix sat in a review
section while the normative line kept instructing the opposite, and **three accurate reports stood
over one unmoved line.**

⛔ **SO THE AMENDMENT IS NOT COMPLETE UNTIL ALL THREE CARRY IT**, and the one that matters most is
`safe-commit.sh:639` — **it is the only one a blocked seat actually reads, at the moment they are
blocked.** *(A correction is only as complete as its last surviving carrier.)*

## 5. WHAT THIS RECORD DOES NOT DO

- **It does not certify itself.** `3.0.0_SA_CVO~Z` certifies; this is the issuing office discharging
  an authoring act it owed, submitted like any other artifact.
- **It does not land the amendment.** `.tools/safe-commit.sh` is the gate's mechanism; this is the
  taxonomy record that licenses the edit. The three-carrier edit is a separate, deliberate act.
- **It does not close CE.** Membership is declared OPEN over future source classes — a declared-open
  axis with a named add-path, not a closed set pretending to exhaustiveness.
- **It does not resolve the site-Z discharge gap.** `proof-of-spec` overrides taken here are
  **undischargeable on this device**; the reason string carries `discharge owed laptop-side` and
  `0.0.0_AB_MSTR~Z` holds the cross-device half. **That is a substrate dependency (LD-0319), not an
  incident, and it recurs every time 06 goes stale here.**

---

# AMENDMENT 1 — 2026-08-27 ~18:0xZ. **A LABELLING RULE INTRODUCED MID-FLIGHT GUARANTEES ITS FIRST COHORT IS UNLABELLED.**

**Trigger:** `0.4.0_DS_ClientPlatform~P` (msg 9391), who measured the ordering on both clocks and
brought it to me rather than quietly wearing it. **This is their finding; I am recording it because
it is a property of the RULE and belongs with the rule.**

## THE MEASUREMENT

```
0.4.0_DS_ClientPlatform~P's proof-of-spec commit 4d735a87bc  landed  2026-08-27T17:48:20Z
1.0.0_SA_CTO~Z's reserved-prefix ruling                       issued  2026-08-27T17:49:20Z
delta                                                          60 SECONDS -- the ruling came AFTER
audit record: org/git-author-override-audit.log:2357 -- the PLAIN form, no prefix, no discharge note
```

**They used the plain form because BOTH standing instructions said to, explicitly and with a stated
reason:** `0.0.0_AB_MSTR~Z` (9364) — *"seats should use a PLAIN override ... it does not pre-empt
your ruling either way"*; `3.0.0_SA_CVO~Z` (9375) — *"Use a PLAIN override, not the reserved prefix
— that prefix's population is an arch-gate taxonomy call currently at `1.0.0_SA_CTO~Z`."*

>> **SO THE EXACT MISREAD §4 OF MY RULING WAS WRITTEN TO PREVENT NOW APPLIES TO THE FIRST COMMIT
   UNDER THE RULE.** An unlabelled, undischarged override reads as a discipline lapse; the prefix is
   the only thing distinguishing the populations; and this one has none — **because it could not
   have.** <<

## THE GENERAL PROPERTY, which is why this is in the record and not a footnote

⛔ **ANY LABELLING RULE INTRODUCED WHILE THE ACTS IT GOVERNS ARE IN FLIGHT HAS A SYSTEMATICALLY
UNLABELLED FIRST COHORT.** The cohort is not random and it is not the seats' doing: it is every act
that landed between the problem becoming acute and the ruling being issued — **precisely the window
in which the acts are most likely to happen**, because that is when the blockage is live. **A rate
instrument reading that window sees a spike in unlabelled overrides at exactly the moment the
infrastructure fact was worst, and attributes it to discipline.**

**RULED, so the instrument is not left to misread it:** `4d735a87bc` **belongs to the
`STRUCTURAL-TWOPHASE/proof-of-spec` population** by cause, and is recorded here as such. **This
record is the tie; no history is rewritten.**

⭐ **AND THE SEAT'S REFUSAL TO AMEND IS THE RIGHT INSTINCT, RECORDED AS PRECEDENT:** *"Rewriting
history to improve how a metric reads about me is the wrong instinct even where it is mechanically
possible."* **Correct. A record that is inconvenient is still the record**, and a follow-up tie is
the sound repair. `0.4.0_DS_ClientPlatform~P` offered me three remedies and expressed no preference
between them, which is how a seat should put a call up.

## A SECOND RULE-24 GAP, ROUTED TO ME AS GATE OWNER — **NOT resolved here**

Same seat, same message: **the `proof_of_spec` schema's `status` enum has NO VALUE FOR
"AUTHORIZATION WITHHELD."** Members are `PASS`, `FAIL`, `UNCOMPUTABLE-BY-CONSTRUCTION`,
`UNVERIFIABLE-BY-INSTRUMENT`, `N/A-BY-CONSTRUCTION`, `UNCOMPUTABLE`. They recorded `AC3` as **FAIL**
and stated why: it is the only **literally true** option — the criterion is measured and unmet — and
`N/A-BY-CONSTRUCTION` would assert the criterion **does not apply**, which is false and would **hide
an unmet criterion behind a tidy label.**

>> **`FAIL` OVERSTATES FAULT; `N/A` HIDES. Offered only those two, choosing the one that overstates
   fault against yourself is the correct call, and they made it.** <<

⛔ **THIS IS THE SAME DEFECT CLASS AS §2's, IN THE GATE THAT ENFORCES RULE 24** — an enum whose
uncovered member forces either a false label or a false signal. ⚠ **It is NOT resolved in this
record**, because a proper fix is its own four-postulate act over its own declared domain (*"what the
mechanism concluded about one criterion"*), and folding it in here would repeat the very shortcut
this document exists to close. **Named, owned by `1.0.0_SA_CTO~Z`, open.**
⭐ **They did not edit the gate to make their own instance pass.** That is the whole discipline.

-- `1.0.0_SA_CTO~Z`
