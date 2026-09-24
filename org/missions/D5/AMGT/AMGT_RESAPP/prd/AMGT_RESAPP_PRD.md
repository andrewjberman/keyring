# AMGT_RESAPP -- PRD (L4)

```json
{
  "project": "AMGT_RESAPP",
  "directive": "D5",
  "fabric": "site-z",
  "prd_version": "v0.25",
  "step": 4,
  "brief_ref": "docs/briefs/amgt-resapp-security-analysis-20260910.md@19ce7d5b4d",
  "addendum_b_brief_ref": "docs/briefs/amgt-resapp-frontend-pattern-brief-20260924.md@21dd61e392",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8",
    "FWD-9",
    "FWD-10",
    "FWD-11",
    "FWD-12",
    "FWD-13",
    "FWD-14",
    "FWD-15",
    "FWD-16",
    "FWD-17",
    "FWD-18",
    "FWD-19",
    "FWD-20",
    "FWD-21",
    "FWD-22",
    "FWD-23",
    "FWD-24",
    "FWD-25",
    "FWD-26",
    "FWD-27",
    "FWD-28",
    "FWD-29",
    "FWD-30"
  ],
  "status": "RATIFIED"
}
```


**archetype:** SCRIBE (spec) · **author** `1.0.0_SA_CTO~Z` (L4 owner: CTO, no COO, no CVO)
**status:** `LANDED` -- L3 + L4 registered 2026-09-10 ~18:3xZ

> ⭐ **THIS FILE IS NOW AT ITS HOME.** It was authored before this tree existed, staged at
> `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_PRD_STAGED_20260910.md` @`449a7c8fc2`, and
> **moved here byte-for-byte unchanged apart from this banner and the status line.** That deliverable
> is now a POINTER, not a second copy -- two carriers of one obligation drift from the minute the
> second is written, which is the exact defect that cost NFRA_REPORT a round today.

| | |
|---|---|
| **Directive** | D5 Alternative Research (placement SITEZ) |
| **Macro** | `AMGT` -- Andrew-direct @`1f89e24eac` |
| **L1 brief** | `docs/briefs/amgt-resapp-security-analysis-20260910.md` @`19ce7d5b4d` (**v2 -- see s.0**) |
| **L2 endpoint** | `.../deliverables/AMGT_RESAPP_ENDPOINT_20260910.md` @`3bc8f5f2c4` |
| **Origin** | Adam Muller (Head of Asset Management) -> Andrew, 2026-09-10, "Claude automation" |

### ENDPOINT provenance and history -- held HERE, deliberately

**This block lives in the PRD PREAMBLE, which belongs to NEITHER sign-off half** (`half_of_section`
returns `None` for the pre-heading text), so the record below is preserved without contaminating
`ENDPOINT` and without re-opening the CRO's brief half. It was moved out of `ENDPOINT` on the L4-R
refusal @`1ec5ade3f5` (review `.../AMGT_RESAPP_v04_RATIFIED_TEXT_REVIEW_20260911_Z.md`@`cfaa24b7b8`),
which held that L4-R forbids annotation, history and seat names across the whole section.

- **Outcome provenance.** The outcomes are reproduced VERBATIM from the L2 endpoint @`3bc8f5f2c4`
  and are NOT re-authored in this PRD. `FWD-1`..`FWD-12` derive from brief `O1`-`O12`; `FWD-13` and
  `FWD-14` were added at L2 and accepted without reservation by `4.0.0_SA_CRO~Z` (msg 21001) as its
  own gaps. `FWD-15` came from Andrew's frontend walkthrough (the Lead Panel), carried in
  `4.0.0_SA_CRO`'s full-stack vision Part C and this seat's synthesis, and was CONFIRMED by Andrew
  2026-09-11 ~12:1xZ ("Recs approved") as his reserved L2 confirmation.
- **Carriers, for the verbatim comparison L4-R makes** (recorded HERE, outside the ENDPOINT, at v0.8 on
  `3.0.0_SA_CVO~W`'s review @`576b1edcec`: an annotation is not a card). `FWD-1`..`FWD-14` compare against
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_ENDPOINT_20260910.md` @`3bc8f5f2c4`; `FWD-15` against
  Andrew's reserved L2 confirmation (s.3b); `FWD-16`..`FWD-19` against
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_RESAPP_ENDPOINT_ADDENDUM_20260915.md` @`2285a23678`, which
  quotes beside each card the Andrew-direct sentence it was cut from; its four cards are byte-identical to
  the four in the ENDPOINT. v0.7 had placed this paragraph inside the ENDPOINT section; v0.8 moves it.
- **The transcription omission, recorded rather than quietly fixed.** The staged copy of this PRD
  carried a POINTER to the L2 endpoint artifact instead of the outcome cards, with a note saying the
  block "is transcribed into this section when this file lands in the tree." The landing was
  byte-for-byte, so the transcription never happened, and for roughly an hour the outcomes existed
  only in a deliverable while the PRD that cites them held none -- `FWD_DEF_RE` measured **0
  outcomes defined**. This is the same TWO-CARRIER shape that cost `NFRA_REPORT` a round the same
  morning, committed again by the same seat hours after writing the correction. Found by
  `2.0.0_SA_COO~ZZZ` running the L6 gate's own functions with a positive control, not by its author.
  **The `ENDPOINT` section is the only carrier of the cards.**
- **Stale count corrected in the same amendment.** The L5 bar read "Thirteen outcomes cannot be
  closed by any build" while the section carries FOURTEEN `EXERCISED` outcomes; the reviewer caught
  it and it now reads "Fourteen".
- **And again at v0.7.** v0.6 added four `EXERCISED` outcomes and left the same sentence at "Fourteen";
  `3.0.0_SA_CVO~W` caught it (review @`01e640925c`) and it now reads "Eighteen". The version-history
  parenthetical v0.6 placed after the BAR DISTRIBUTION line is moved out of the ENDPOINT to s.9g.

### C-LIST-OWNER -- THE NAMED OWNER, RECORDED 2026-09-14 (a fact, not an amendment)

`C-LIST-OWNER` (`:947`, serves `FWD-14`) requires that each of the publisher allowlist and the
company-to-social-account map carry **a named owner** and **a rot signal**. **THE NAMED OWNER IS
`0.5.0_AE_OpalETL~Z`.**

**PROVENANCE, because an assignment with no date and no author is the thing this PRD's own s.0 warns
about.** Andrew-direct 2026-09-14 ~05:31Z, laptop terminal, relayed by `0.0.0_AB_MSTR~Z` over bus
`087b3fea-f49e-43db-856f-47fe3c791f4c`, VERBATIM:

> *"The publisher list and company-to-social map i already answered earlier, specifically saying I
> dont know why this needs an owner and following up with if theres some process architecture that
> mandates it that they can use `0.5.0_AE_OpalETL~Z`, but I dont see why that would be needed."*

⚠ **THIS IS A CONDITIONAL HE SATISFIED, NOT AN UNCONDITIONAL NAMING**, and the antecedent is met by
**THIS CONTRACT**, which predates and is independent of any CTO ruling -- `C-LIST-OWNER` mandates an
owner whether or not the CTO had ruled, and a conditional satisfied by the CTO's own act would be
this seat bootstrapping its own authority. Adjudication record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ADJUDICATION_AMGT_RESAPP_20260914T0300Z_C_LIST_OWNER.md`
@`7fb0c06c65`.

⛔ **WHAT THIS DOES NOT DO.** It does not amend `C-LIST-OWNER` -- it records WHO, not WHAT IS
REQUIRED. It **SEATS NOBODY**: an owner-of-record is not a dispatched seat and no task order is
implied. It does not touch `C-NO-CONTACT` -- an agent serial is not Adam's team. It grants no vendor
egress.

⛔ **AND `FWD-14` DOES NOT REALIZE ON THIS NOTE.** The delivered lists at
`deliverables/0.9.0_WK_AMGT_RESAPP~5/lists/` still read `"owner_status": "UNASSIGNED"`. **FWD-14
realizes when a CELL delivers the owner into the lists with correct provenance** -- a round-N cell,
the COO's to cut after a slug. The rot-signal half is already delivered and running (90-day and
30-day review intervals, `reviewed_at` stamps, a separate computed `rot_signal.json`).

⭐ **WHY IT IS RECORDED HERE AND NOT BESIDE THE CONTRACT AT `:947`.** Two reasons, both measured.
**(1)** `.tools/prd_signoff_lib.py:93-98` -- `half_of_section(None)` returns **None**: the
pre-heading preamble belongs to NEITHER L4-R half, while `## 3. CONSTRAINTS ON THE CUT` (which holds
`:947`) is the **brief** half. Writing the fact at `:947` would make a SIGNED half stale for a note
that changes no requirement. **(2)** `TREE_DELIVERABLES` is **NOBODY by enumeration** -- the gate
refused `2.0.0_SA_COO~ZZZ` on the lists themselves, and back-filling a ROUND-2 worker's artifact with
a fact Andrew supplied **two rounds later** would make that file assert a provenance it does not
have. ⚠ The cost is DISCOVERABILITY: a reader who opens `:947` alone does not see this note. That is
accepted deliberately, and it is why the note names the contract rather than the reverse.
---

### v0.9 -- WHAT CHANGED AND WHICH HALF IT MOVES (recorded HERE, in the preamble, deliberately)

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-16, at L10 of round 11. **Answers:** the round-11 CVO slug
`REMEDIATION_v11.md` @`5d3a04cab6` ("Append FWD-20") and `ROUND_ANALYSIS.round11.md` s.4 and A1.3
@`1db70c8e87`.

**THE HALVES, MEASURED BEFORE THE EDIT WAS WRITTEN AND AGAIN AFTER, not assumed:**

| half | v0.8 | v0.9 | signer owed |
|---|---|---|---|
| ratified-text | `cc038187d71c` | `88e330dea809` | **`3.0.0_SA_CVO~Z` -- MOVED, a signature IS owed** |
| brief | `0455fc3d1e95` | `0455fc3d1e95` | **`4.0.0_SA_CRO~Z` -- UNCHANGED, nothing is owed** |

⭐ **WHY THIS TABLE IS HERE RATHER THAN IN A MESSAGE.** A half binds to the HASH of its sections and
never to `prd_version`, so "what does this bump re-open" is a MEASUREMENT, and a reviewer should not
have to re-derive it. `2.0.0_SA_COO~Z` asked for exactly this read before the addendum was written
rather than after (msg 23370), and it was run that way.

⚠ **AND THIS SECTION IS A `###`, NOT A `##`, FOR A MEASURED REASON: the first draft of it used a
`##` heading, which made it a TOP-LEVEL SECTION rather than preamble and MOVED THE BRIEF HALF
(`0455fc3d1e95` -> `379799cfc644`) for a note that changes no requirement -- the exact trap described in
the next sentence, committed while writing the warning about it. Caught by re-reading the half hashes
AFTER the edit instead of trusting the intent. ⭐ MEASURE THE HALVES AFTER THE WRITE, NEVER ONLY BEFORE.**

⛔ **AND IT IS WHY THIS SECTION SITS IN THE PREAMBLE.** The pre-heading preamble belongs to NEITHER
half (`prd_signoff_lib.half_of_section`, title `None` -> `None`), so recording the change costs no
reviewer a re-read. Writing this same paragraph into a `##` section would have moved a half for a
note that changes no requirement -- the trap this PRD already records one screen above.

**WHAT MOVED THE RATIFIED-TEXT HALF, itemised so the reviewer can diff by intent:**
1. **`FWD-20` appended to the ENDPOINT** -- a filings-and-history-seeded house free-cash-flow
   forecast, seeded independently of consensus, with Divergence shown on the Model tab and ABSENT
   with a reason wherever the house forecast does not serve. Bar `EXERCISED`.
2. **The BAR DISTRIBUTION line** reads 19 of 20 `EXERCISED` (was 18 of 19), and the warning beneath
   it reads NINETEEN outcomes that no build can close (was Eighteen).
3. **Five contract rulings appended to CONTRACTS** as `C-ROUND12-*`, each carrying the call it
   settles and the row it answers.

**WHAT DID NOT CHANGE:** no existing `FWD-n` text, no existing contract, no constraint, no surface
manifest row, and nothing in the brief half. `FWD-n` ids remain permanent and never reused;
`FWD-20` takes the next unused number.


### v0.10 -- the four L4-R grounds, fixed (recorded HERE, in the preamble, deliberately)

`3.0.0_SA_CVO~Z` REFUSED the v0.9 ratified-text half at `88e330dea809` (stamp @`33621451eb`, review
@`eeddafa99f`) on four grounds, every one of them correct. All four sat inside ENDPOINT or CONTRACTS, so v0.10
re-opens the RATIFIED-TEXT half only; the brief half is untouched again and `4.0.0_SA_CRO~Z` owes nothing.

| ground | fixed by |
|---|---|
| **R1** `FWD-20`'s ACCEPT dropped two operative constraints of its own pins -- assumptions stored with their source and time, and the pre-deployment degeneracy check | two sentences added to the card in its plain register; the numeric floor moved to `C-ROUND12-DIVERGENCE-DEGENERACY` |
| **R2** `FWD-20`'s SOURCE did not cite the Divergence record that two of its three sentences rest on | `@287d2c2619` added by title and pin |
| **R3** two SEAT NAMES inside the ENDPOINT section | replaced with non-serial citations |
| **R4** `C-ROUND12-PULL-WIRED` ratified a Lambda consumer this PRD's own L10 author had already found impossible | the contract rewritten to the corrected ruling; no Lambda consumer |

⛔ **R4 IS THE ONE WORTH READING TWICE, because nothing mechanical could have caught it and the bytes were
innocent.** The contract was written at v0.9 and the ruling behind it was CORRECTED fifteen minutes later in an
addendum; the contract's bytes never moved, so every hash comparison read clean while the content had gone
wrong. ⭐ **A CONTRACT AGES SEPARATELY FROM THE RULING IT ENCODES** -- the same shape as a citation ageing
separately from the text it quotes, one level up. **When a ruling is corrected, re-read every artifact that
already encoded it**; a half-hash comparison cannot see it, and signing would have ratified a design the project
had already ruled cannot work on this box.

⚠ **R3 is a READING rule with no regex behind it** (`prd_signoff_lib.py` carries none), so nothing would have
refused it either. Measured independently at both vintages before the fix: the ENDPOINT section holds **2**
serial-bearing lines at v0.9 of 231 body lines, and **0** at v0.8 of 211. Both were introduced by this bump.


### v0.24 CHANGE NOTE -- 2026-09-23 ~04:3xZ, `1.0.0_SA_CTO~Z`: Lenovo IS an EDGAR entity, and the regulator route was already ratified

**BRIEF HALF ONLY. The ratified text is UNTOUCHED -- no ENDPOINT line and no `C-` contract moves.** New
section **12a** carries both corrections; section 12's stage-3 row is rewritten to match it.

- **Lenovo IS an EDGAR filer.** Section 12 said `(not an SEC filer)`. Measured at the regulator
  (`data.sec.gov` submissions for CIK 0000932477, HTTP 200): **LENOVO GROUP LTD, 63 filings all-time**
  (`filings.files` empty, so nothing older is unread), **0 of 10-K / 20-F / 40-F / 6-K**, and **six `ARS`
  annual-family documents whose newest is 2007** and which are paper placeholders. The entity RESOLVES at
  step (2); what fails is acceptance test (b) CURRENT, then (c) KNOWN FAMILY. The battery's recorded
  REASON is served through `rk-127`'s HELD marker, so the false sentence would reach the page.
- **The regulator route needed no amendment.** `C-FILINGS-ANALYZER` has carried international step (5),
  the national regulator, since @`4de34f0d95`. The CTO ruling @`0210Z` directed it into `C-`-space; that
  act is VOID as unnecessary and the ruling's other three limbs stand. ⛔ **The ruling measured the CODE
  and concluded about the CONTRACT** -- the true state is RATIFIED AND UNBUILT, which is a cell.

⚠ **Consequence for round 35: it needs NO ratified-text re-signature and NO new authority from Andrew.**
**Placed as a `###` in the preamble, before `## 0.`, so this note moves neither half by itself.**

### v0.23 CHANGE NOTE -- 2026-09-22 ~15:2xZ, `1.0.0_SA_CTO~Z`: the sibling project AMGT_HARVST

Andrew-direct ~14:4xZ made `AMGT_HARVST` a new project beside this one (record @`e279a48e4e`). Its v0.2 PRD
replaces the chatter axis's read path. This bump makes three changes:
- **Ratified text:** `C-ONE-STORE` names that supersession and its trigger. This is `3.0.0_SA_CVO~Z`'s R1 on
  AMGT_HARVST v0.1, and the "same bump" it asked for.
- **Brief half:** section 12's stage 9 waits on AMGT_HARVST's bronze and silver.
- **Brief half:** the Lenovo before-count is corrected from 19 to 18. The unanchored grep had matched a byte size;
  the key-anchored count is 18.

Both halves move.

### v0.22 CHANGE NOTE -- 2026-09-22 ~14:0xZ, `1.0.0_SA_CTO~Z`: the Lenovo trial

Andrew-direct ~13:5xZ (record @`cd0cca7f46`): run Lenovo through the entire pipeline as the trial. This bump makes these
changes:
- It adds section 12, which makes `992_HK_Equity` the validation scope in place of the three names in `C-VALIDATION-NAMES`.
- It re-pins the channel-formats plan in section 11 to @`1b43fd2933`.

CONTRACTS and ENDPOINT are untouched, so **only the brief half moves.** The working key (composite FIGI, "for the
purposes of research", @`6f1a72e4be`) is recorded as a trial output, not a contract.

### v0.21 CHANGE NOTE -- 2026-09-22 ~11:1xZ, `1.0.0_SA_CTO~Z`: the CVO's v0.20 residuals and carry items

This bump applies the v0.20 review @`45cc68b8ac` exactly.
- (a) The round-5/v0.6 history is stripped from C-PAGE-LAYOUT. Its operative sentence stands alone.
- (b) The dated ticker measurement is stripped from C-UNION-UNIVERSE.
- (c) C-ETF-PLANE-READ names the role, not the lane.
- (d) The closed row id is stripped from C-HARVEST-HOME, and C-PAGE-LAYOUT's S13 is named as the open social-feed surface.
- Carry 1: the preamble now says where owners are recorded.
- Carry 2: the POSN_ASTTAX PRD pointer carries its path.

Only the ratified-text half moves.

### v0.20 CHANGE NOTE -- 2026-09-22 ~11:0xZ, `1.0.0_SA_CTO~Z`: the CONTRACTS provenance cleanup, per the CVO's ruling

This bump executes the ruling at `org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_RULING_AMGT_RESAPP_CONTRACTS_PROVENANCE_20260922.md`
@`8420ba2ddc`. Each contract keeps ONE owner and ONE `path@commit` pointer to its immutable record.
- Time-only Andrew-direct citations are pinned to the record carrying them.
- Removed: incidental history (measurement narratives, lane suffixes, version tags, settled row ids, intermediate commit trails).
- No operative sentence changes.

Only the ratified-text half moves.

### v0.19 CHANGE NOTE -- 2026-09-22 ~10:5xZ, `1.0.0_SA_CTO~Z`: where Bloomberg's received form is recorded, and its non-finite rule

`C-BRONZE-AS-RECEIVED` takes the CVO's three wording items.
- A non-finite number is serialised as null, and the serialiser refuses any other value JSON cannot carry. This is
  rk-96's rule, now in the contract.
- The received form is recorded in S3 object METADATA, never in the body. A body field would alter the very
  serialisation the clause defines.
- The key is named as stored: `received-form`.

The contract edit moves the ratified-text half; this change note moves the brief half. The broader CONTRACTS
provenance cleanup is NOT in this bump: the section's own
preamble requires each contract to name "its owner and the record it comes from", so a pure deletion would contradict
it. That question is put to the CVO as a governance fork.

### v0.18 CHANGE NOTE -- 2026-09-22 ~08:0xZ, `1.0.0_SA_CTO~Z`: Bloomberg's received form, and what stays on its served path

The two contract clauses record the rulings the round-21/22 cuts ran under.
- **`C-BRONZE-AS-RECEIVED`** names Bloomberg's received form. The Terminal client hands the producer a parsed object,
  and the wire bytes are unreachable, so its deterministic JSON serialisation is the received form, marked as such
  (msg 24106).
- **`C-FORMAT-SEQUENCE`** states that a served object whose reader cannot read silver's format keeps its one served
  path until the gold chain builds a served JSON projection: `model_block`, and the publication bodies and links
  (msgs 24123 and 24125).

Section 11 records the moves as done and the registry items as closed. BOTH halves move. The CONTRACTS
provenance cleanup (the CVO's v0.17 carry-item) is still owed, as its own bump.

### v0.17 CHANGE NOTE -- 2026-09-21 ~21:3xZ, `1.0.0_SA_CTO~Z`: platinum's home, Lusha's exception, and what "retire" means

The format contracts take five changes.
- **Platinum.** `C-HARVEST-HOME` puts platinum where the builder prints it, not at R6. The landed GENERAL tenancy homes
  every tier by scope, which is Andrew's "whole pipeline in harvest", and its only remaining condition is the duplicate
  `harvest` scope row (row Z-S203).
- **Lusha.** It takes Andrew's R20 exception (~19:5xZ, *"Yes on Exception"*): silver only, contact fields dropped, no
  bronze.
- **Retire.** `C-FORMAT-SEQUENCE` defines "retire" (readers switched, writers stopped and read grant removed in one
  window; deletion is a separate human word).
- **Re-serialisation.** It counts a lossless re-serialisation as a copy.
- **filings/v1.** Its DERIVED records go to silver.

These answer the COO's four calls (msg 24087). Section 11 records that the tenancy and the five vendor rows have landed
on SITEZ. BOTH halves move.

### v0.16 CHANGE NOTE -- 2026-09-21 ~19:3xZ, `1.0.0_SA_CTO~Z`: who the CEO is, and readable reasons

`C-EXEC-MANAGEMENT` gains two rules. (1) Who the CEO is, ruled on rows Z-S195/S196: a Japanese-listed "President" is
the chief executive when no officer carries a CEO title. (2) A served reason is always a readable sentence, prompted by
row Z-S197, where a missing value printed as "None" into Keyence's roster reason. Section 11 re-pins the format plan at
`1a9f1c4469`; its correction drops a dual-write move order that the same-window contract forbids. BOTH halves move.

### v0.15 CHANGE NOTE -- 2026-09-21 ~17:5xZ, `1.0.0_SA_CTO~Z`: the six format contracts move to CONTRACTS

v0.14 put the six format contracts in section 11, which the sign-off hashes as the brief half, so the ratified-text
reviewer never saw them; `3.0.0_SA_CVO~Z` caught it (msg 23999). They now sit in the CONTRACTS section. The same
edit takes the reviews' conditions: bronze takes three forms (the brief reviewer's refusal, msg 24001); one writer
per fetch key; a moved path retires in the same window; the home is conditional in its own sentence; platinum at R6's
home, as the drafted tenancy lands it (msg 24000); never-kept bronze filled by a first fetch. BOTH halves move.

### v0.14 CHANGE NOTE -- 2026-09-21 ~17:4xZ, `1.0.0_SA_CTO~Z`: the harvest storage format (section 11)

Andrew-direct ~17:2xZ (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_172xZ_AMGT_RESAPP_PROMOTE_IF_FEATURES_NO_WATER_IN_PIPES_BACKFILL_HELD_FOR_BRONZE_SILVER_SHAPE.md`
@`e70b949ba0`): the coordinated backfill is held until the bronze/silver format of `opal-data-harvest` per ingestion
channel is settled. `4.0.0_SA_CRO~Z`'s plan (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md`
@`bc8c18a28f`) is adopted as the channel-by-channel specification, and section 11 carries the contracts. The ENDPOINT
and the CONTRACTS section do not move. Only the brief half re-opens.

### v0.13 CHANGE NOTE -- 2026-09-18 ~20:1xZ, `1.0.0_SA_CTO~Z`: ratified-text hygiene, and Andrew clears SA's terms

(1) **`3.0.0_SA_CVO~Z` REFUSED v0.12's ratified-text half on criterion (d) alone** -- annotation, history and seat names inside
the section; substance passed (review `org/tier1_exec/3.0.0_SA_CVO/deliverables/AMGT_RESAPP_V011_RATIFIED_TEXT_REVIEW_20260918_Z.md`
@`969755b2f2`, stamp @`075227f4c0`). Every RULE is kept. Moved OUT of `C-FILINGS-ANALYZER`, `C-FILINGS-TRANSLATION`,
`C-EXEC-MANAGEMENT` and `C-PEERS-V-FLOORS` into section 10's closing evidence list: seat serials, present-tense defect
descriptions with file:line, the Keyence measurements and the supersession narrative. (2) **Andrew-direct ~20:0xZ,
VERBATIM:** *"I have already clarified SA ToS, we are good, if I had an issue with the design i wouldnt have designed it this
way."* (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_20xxZ_AMGT_RESAPP_SA_TERMS_CLEARED.md`). `C-SA-TERMS-BEFORE-SCHEDULE` is SATISFIED for the two Seeking Alpha paths lifted at v0.12, and the terms-reading
task is withdrawn. Both halves move.

### v0.12 CHANGE NOTE -- 2026-09-18 ~19:4xZ, `1.0.0_SA_CTO~Z`: Andrew answered the six round-13 cards

Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md`. His words, VERBATIM: *"1.) Yes use SA thats fine. 2.) Yes full egress. 3.) Yes. 4.) Agreed, yes. 5.) Base. I
think the upside and downside cases can be discussed on methodology. 6.) Yes"*. Landed before either v0.11 half was signed,
so the signers review v0.12's bytes. **Ratified-text half:** `C-PEER-SET-SA` (SA production use LIFTED for this path by
name); `C-FILINGS-ANALYZER` (international battery order RATIFIED). **Brief half:** `C-MODEL-FORECASTS` (SA fallback
LIFTED by name); `C-MODEL-WINDOW-AND-ROWS` (Base case adopted; Upside/Downside ABSENT pending methodology); `C-VERBATIM-GATE`
(a sentence with no span is HELD); the `C-SA-VENDOR-WORD` table (the two named lifts); `C-VALIDATION-NAMES` (Lusha and SA
authorized inside the validation); and, on `4.0.0_SA_CRO~Z`'s review (msg 23744), `C-DESCRIPTION-LINE`'s order corrected
(Bloomberg's field first; a drafted sentence only past a describes-the-business test) and card 4's figure re-stated over the
served population (179 of 389). Card 6 (headless capture, estate-wide) is outside this PRD and routed to
`0.0.0_AB_MSTR~Z`. **Not changed:** a RECURRING or SCHEDULED Seeking Alpha read still waits on `C-SA-TERMS-BEFORE-SCHEDULE`.

### v0.11 CHANGE NOTE -- 2026-09-18, `1.0.0_SA_CTO~Z`, the answer to round 13's slug (`ledger/ROUND_ANALYSIS.round13.md`)

**Source:** round 13's slug (97 of 97 orders terminal) and the six current-to-desired panel briefs `4.0.0_SA_CRO~Z` brought
forward with Andrew (Lead Panel, Thesis, Exec Management, Peers, Model, and the three-name instantiation validation
@`b527b93214`), read into `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTOZ_AMGT_RESAPP_PANEL_BRIEFS_INTAKE_20260918.md`. The
Posture brief is NOT integrated here (Andrew: *"no need to wait for Posture brief"*); FWD-19 is untouched. **BOTH HALVES
RE-OPEN.**

**Ratified-text half (ENDPOINT + CONTRACTS):** `C-FILINGS-ANALYZER` replaced (the source is the per-security battery's
winning document; Bloomberg supplies keys, never text); `C-FILINGS-TRANSLATION` added (analyze the original, translate the
output); `C-EXEC-MANAGEMENT` replaced (Andrew's cards 1 and 2 and the CEO search; `roster_source`; a zero-officer roster is
not SERVED); `C-SIMILARITY-RANKER` narrowed to FWD-19's comparable, and FWD-8's peer set moved to the new `C-PEER-SET-SA`
with `C-PEERS-V-FLOORS`; the ENDPOINT's stale "Eighteen outcomes" corrected to Nineteen (the v0.9 note said it was fixed;
the bytes were not).

**Brief half:** `C-UNIT-MAP-MEASURED` amended (built for every name); `C-MODEL-FORECASTS` and `C-MODEL-WINDOW-AND-ROWS`
added; `C-VERBATIM-GATE` replaced (every pass count prints its split; a sentence with no span is served LABELLED, and whether
it is instead HELD is Andrew's card) -- ⛔ **THAT LAST CLAUSE IS SUPERSEDED: Andrew answered the card
(*"Agreed, yes."*, ~19:4xZ) and **v0.12 makes a no-span sentence HELD, never served** -- read
`C-VERBATIM-GATE` at `:1107-1114`, not this note. Measured blast radius of the HELD rule: **179 of 389
sentences (46%) across 12 served documents.** ⚠ **This note is TRUE AT ITS OWN VINTAGE (v0.11) and a
reader scanning change notes for this contract finds it FIRST; `3.0.0_SA_CVO~Z` came one sentence from
ruling the figure branch already admissible on it, 2026-09-23.** ⭐ **A change note ages past the clause
it describes, and nothing in a preamble announces which entry is newest for a given contract** --; `C-SERVER-SIDE-RANKING` amended (no rank without signal; `empty_reason`);
`C-PRICE-BREAKOUT-FLOOR`, `C-PRICE-DAILY-LEG` (Andrew's Lead Panel cards B and A) and `C-DESCRIPTION-LINE` added; the
section-9 condition *"measure one Bloomberg-pulled filing"* marked superseded; and a new **section 10, THE INSTANTIATION
STAGES**, with `C-INSTANTIATION-ENTRY`, `C-PRODUCTION-HOME` and `C-VALIDATION-NAMES`. In this preamble, the five stale `:353`
citations of `C-LIST-OWNER` (on four lines) are repointed to its definition, now `:947`.

**Not changed:** every FWD line; FWD-19 and `C-POSTURE`; `C-SA-VENDOR-WORD`, `C-SA-TERMS-BEFORE-SCHEDULE` and
`C-VENDOR-EGRESS`, which bind the new Seeking Alpha paths as written; any cadence, which stays Andrew's. **Placed as a `###`
in the preamble, before `## 0.`, so this note moves neither half by itself.**

---

## 0. THE VERSION HAZARD -- BINDING ON EVERY READER OF THIS PRD

⛔ **THE BRIEF EXISTS IN TWO STATES AND ONE OF THEM IS ON THE SHARED BRANCH.** Measured with a
positive control: v1 @`046337e2df` **is** an ancestor of `origin/SITEZ` (15,429 bytes); v2
@`19ce7d5b4d` is **working-tree only** (22,244 bytes). Token counts one variable apart --
`O10`/`O11`/`O12`/`F12`/`F13`/`StockTwits` appear **0 times in v1**, 4/2/3/2/1/1 in v2.

**A cell that resolves the brief from origin loses the entire validation territory and the whole
social limb, and the result looks complete.** Until `0.0.0_AB_MSTR~Z` pushes, **every worker face
citing the brief cites `@19ce7d5b4d` explicitly** and reads from the working tree.

---

## ENDPOINT (step 2, /endpoint --forward)

⛔ **`FWD-n` IDS ARE PERMANENT AND NEVER REUSED.** A new outcome takes the next unused number; a
retired one leaves its number vacant forever. The round-N analysis and any addendum cite them back.

*Phase 0 output. `FWD-n` ids are PERMANENT and never reused; a retired outcome leaves its number
vacant. `DONE WHEN` is the BAR, not the current state. ACCEPT lines are plain English and
disputable, by rule, and carry no technical language.*

```

  FWD-1  An analyst gets a first-draft pack for a covered name without opening
         a spreadsheet or a data terminal
         DONE WHEN  EXERCISED -- an analyst has actually done it, not merely could
         ACCEPT     An analyst opens a company the firm already covers and the
                    model numbers, the business description and the segment
                    breakdown are already on screen. They did not open a
                    spreadsheet or a data terminal to get them.
         SOURCE     brief O1; III-B bar 1

  FWD-2  An analyst gets the same pack for a company the firm has never covered,
         by typing its ticker
         DONE WHEN  EXERCISED -- a real uncovered name has been pulled and read
         ACCEPT     An analyst types the ticker of a company the firm has never
                    covered and gets the same assembled page -- and the page says
                    plainly that it is being fetched now rather than shown from
                    an earlier save.
         SOURCE     brief O2

  FWD-3  An analyst can defend every number on the page in a meeting
         DONE WHEN  EXERCISED -- a figure has actually been challenged and
                    answered from the page
         ACCEPT     Someone asks where a figure came from, on what basis, and as
                    of when. The analyst answers by pointing at the screen --
                    not from a spreadsheet and not from memory.
         SOURCE     brief O3; III-B bar 2; F3 (state the basis beside the number)

  FWD-4  An analyst reads what has recently been said about the company without
         leaving the page
         DONE WHEN  EXERCISED -- an analyst has read one and followed it out
         ACCEPT     Recent commentary about the company is on the same page --
                    news, analyst writing, and mentions from the company's own
                    investor channel -- ordered by how recent and how often it
                    came up, each item clickable through to the original.
         SOURCE     brief O4

  FWD-5  Adam forwards a printed pack without reformatting it
         DONE WHEN  EXERCISED -- Adam has actually forwarded one
         ACCEPT     Adam prints a pack and sends it on unchanged. It replaces the
                    document he circulates today, rather than looking like a
                    screenshot of a dashboard.
         SOURCE     brief O5; III-B bar 3 (the displacement test)

  FWD-6  An analyst returning to a company can say what changed
         DONE WHEN  EXERCISED -- someone has actually compared two versions
         ACCEPT     An analyst returns to a company researched before and can say
                    what moved, naming the earlier version that shows it.
                    Refreshing adds a version; it does not overwrite the old one.
         SOURCE     brief O6; III-B bar 5

  FWD-7  Adam can see which covered companies have gone stale
         DONE WHEN  EXERCISED -- Adam has used it to find a stale name
         ACCEPT     Adam looks in one place, sees every company the team covers
                    with the date its research was last refreshed, and finds one
                    that has gone stale without opening any folders.
         SOURCE     brief O7

  FWD-8  The comparison block is about the company on the page
         DONE WHEN  EXERCISED -- an analyst who distrusted it has stopped
         ACCEPT     The list of comparable companies is genuinely about the
                    company being shown. Where a sensible comparison cannot be
                    worked out, the page says so rather than showing another
                    company's list.
         SOURCE     brief O8; III-B bar 4; F6 (48 of 54 measured wrong today)

  FWD-9  Machine-written prose is never mistaken for a firm view
         DONE WHEN  APPLIED -- the marking is in place and sits beside the
                    evidence the sentence was drawn from
         ACCEPT     An analyst can tell at a glance which sentences a machine
                    wrote and which the firm owns, and the machine-written ones
                    sit next to the evidence behind them. They are a starting
                    point someone edits, not a finished claim.
         SOURCE     brief O9; III-B bar 6

  FWD-10 A figure that failed its check is visible as failed
         DONE WHEN  EXERCISED -- a check has actually refused something and the
                    refusal was seen on the page
         ACCEPT     A figure that failed or skipped its check looks different
                    from one that passed, and the analyst can tell which. A
                    failure shows as a marked value -- never as a blank, a zero,
                    or a row that quietly disappeared.
         SOURCE     brief O10; III-B ("a check that cannot FAIL is not a check")

  FWD-11 An analyst sees social discussion admitted by a written rule
         DONE WHEN  EXERCISED -- an analyst has read the feed and can point at
                    why an item was admitted
         ACCEPT     Recent social discussion about the company is on the page --
                    its own official accounts and the wider conversation -- and
                    each item is there because it met a written rule the analyst
                    can read, not because it contained the ticker letters.
         SOURCE     brief O11; F12 (the surface is reachable); F13 (the
                    cashtag-native venue is absent, so the feed's own limits
                    are part of what the rule must state)

  FWD-12 An analyst can see where each input came from and re-run any one alone
         DONE WHEN  EXERCISED -- one input has actually been re-run by itself
                    while the others stayed where they were
         ACCEPT     For each kind of input -- market data, filings, news, social,
                    web -- the page shows where it came from, when it last ran,
                    and whether that run worked; and any one can be re-run on its
                    own. A single button that refreshes everything under one
                    timestamp does not count.
         SOURCE     brief O12

  FWD-13 Everything on one page is about the same company
         DONE WHEN  EXERCISED -- checked on a name that more than one business
                    uses, and found not mixed
         ACCEPT     The numbers, the recent commentary, the comparison list and
                    the social posts on a page are all about the same company.
                    Where the page cannot confirm that two sources describe the
                    same company, it says so rather than showing them together.
         SOURCE     brief III-B ("An identity" as its own class); PART V (the
                    ticker, the symbol and the investor-page identity are three
                    different keys; the social layer has no shared identifier);
                    F6 (the measured instance of exactly this failure)

  FWD-14 The lists the page depends on do not rot in silence
         DONE WHEN  EXERCISED -- a list has actually gone out of date and
                    somebody was told by the system rather than by a wrong page
         ACCEPT     The list of publishers the page will quote, and the map of
                    companies to their official social accounts, each have a
                    named person responsible; and when one goes out of date
                    somebody is told.
         SOURCE     brief PART V ("an enumerated list with no owner lapses
                    silently ... the same failure that left two keys dead")

  FWD-15 A PM can see which covered names are worth looking at right now,
         without opening each one -- ranked by how much they are moving or
         being talked about, and can jump straight to any name
         DONE WHEN  EXERCISED -- a PM has actually opened the page, read the
                    ranked list, and clicked through to a name it surfaced
         ACCEPT     Adam or Lauren opens the page cold, sees a short ranked
                    list of names that are moving in price or spiking in
                    discussion, and follows one into its full page -- a
                    decision about WHERE TO LOOK that they would otherwise
                    have made by gut or by scrolling a spreadsheet.
         SOURCE     Andrew's frontend walkthrough (the Lead Panel); his
                    reserved L2 confirmation

  FWD-16 The top of the page tells an analyst what the company is and what
         is being said about it today, before any tab is opened
         DONE WHEN  EXERCISED -- an analyst has read the day's items at the
                    top of a page and followed one out
         ACCEPT     Above the tabs, beside the ranked list, the page shows a
                    one-line description of the company and the day's news
                    and social items about it, newest and most-discussed
                    first, each one clickable through to its source. An
                    analyst reads it without opening a tab.
         SOURCE     Andrew-direct 2026-09-15 ~05:1xZ (the header panel word)

  FWD-17 An analyst sees who runs the company, and how long they have run it
         DONE WHEN  EXERCISED -- an analyst has used the profile to answer a
                    question about a management team
         ACCEPT     One tab lists the company's senior executives, each with
                    their role, a profile link and how long they have held
                    the role, and states how the team's average tenure
                    compares with the average across every company the page
                    covers. Where a person cannot be confirmed from the
                    company's own filings, the page says so.
         SOURCE     Andrew-direct 2026-09-15 ~05:04Z (executive managers),
                    ~05:1xZ (the Exec Management tab), ~05:4xZ (the whole
                    C-suite, tenure against the pool), the voice memo of
                    ~05:5xZ (part two)

  FWD-18 The company's own filings are read for the analyst, and the one
         chart that matters is drawn from them
         DONE WHEN  EXERCISED -- an analyst has clicked a filing-derived
                    figure through to the passage it came from
         ACCEPT     The Thesis tab says, in the company's own words and with
                    each sentence linked to the passage in the filing it came
                    from, what the company is doing now, its biggest
                    challenges and its biggest bets; and it shows one chart,
                    chosen for that company, of the thing it lives or dies
                    on. The Model tab's figures are the plain financial
                    model, built the same way for every company.
         SOURCE     Andrew-direct 2026-09-15 ~05:1xZ (four tabs; a filings
                    analyzer), the voice memo of ~05:5xZ (parts one and four)

  FWD-19 An analyst sees what this company means for Opal
         DONE WHEN  EXERCISED -- a PM has read a posture and acted on it, or
                    declined it, on the page
         ACCEPT     The last tab, and a line in the header, say whether this
                    company looks like a better or a worse pick than the
                    most similar name on the other side -- an Opal holding
                    when the company is not held, a non-Opal name when it is
                    -- names that comparable, and gives the reasons with each
                    one linked to what it rests on. It is marked as a
                    machine's view for a person to accept or reject; it is
                    never an instruction, and nothing is traded from it.
         SOURCE     Andrew-direct 2026-09-15 ~05:1x-05:2xZ (Posture, the
                    union universe, the symmetric comparable), the voice
                    memo of ~05:5xZ (part five)

  FWD-20 The house has its own forward view, and the page can say where it
         differs from the street
         DONE WHEN  EXERCISED -- an analyst has read a Divergence figure on
                    the page and traced it to the house forecast behind it
         ACCEPT     A forward free-cash-flow forecast is produced for a
                    covered name from the company's own filings and its
                    history, seeded independently of consensus. Every driver
                    assumption behind the forecast is kept with the filing it
                    came from and that filing's date. The Model tab shows
                    Divergence -- how far the house view sits from the
                    street's, scaled by how much the street disagrees with
                    itself -- and states ABSENT, with the reason, for every
                    name where the house forecast does not yet serve. Before
                    any Divergence is shown, the spread of Divergence across
                    the covered universe is checked for the sign that the
                    drivers were seeded from consensus after all, and
                    Divergence stays ABSENT, with that reason, until the
                    check passes. Model upside and the raw percentage
                    disagreement are REPORTED beside it and are never ranked
                    on.
         SOURCE     CVO round-11 slug REMEDIATION_v11.md @5d3a04cab6 ("Append
                    FWD-20 for a filings/history-seeded house FCF forecast
                    independent of consensus");
                    ANDREW_DIRECT_20260915_183xZ_MODEL_TAB_SCORE_IS_DIVERGENCE_FROM_CONSENSUS_FCF_AND_PEERS_RESENT.md
                    @287d2c2619 (the Divergence definition, the companion
                    figures, and the pre-deployment degeneracy check); the CTO
                    adjudication of 2026-09-15 ~19:5xZ, call 4 @1685652d6e
                    (the forecast seeded from filings and history, never
                    consensus, with every assumption stored with its source
                    and time); ROUND_ANALYSIS.round11.md s.4 item 3
                    @c708914c50

  ===== ADDENDUM B, v0.25, 2026-09-24 -- FWD-21..FWD-30 ========================
  Cut from docs/briefs/amgt-resapp-frontend-pattern-brief-20260924.md@21dd61e392
  (4.0.0_SA_CRO~Z, F1 resolved by Andrew) plus Andrew-direct ~05:0xZ. Rationale
  and the contracts are in ADDENDUM B below; THIS FENCE IS THE ONLY CARRIER of
  the definitions. Acceptance for FWD-21..FWD-29 is ONE instrument:
  portal/scripts/ui-smoke.mjs -- a PNG at 1440 plus the DOM measurement JSON for
  each of the six states -- and A JSON PASS WITHOUT THE PNG READ BY A PERSON IS
  CARE, NOT A CONTROL (C-RENDER-IS-THE-ORACLE).

  FWD-21 A PM opens BA_US_Equity and reads the Thesis ON ONE SCREEN under ONE
         dark band
         DONE WHEN  EXERCISED -- the rendered state reads
                    bandContainersTopLevel == 1, the identity header is that
                    band, the tab panels are white hairline panels, and the
                    Thesis renders as a recommendation line, a summary paragraph
                    and headed sections with evidence FOLDED
         ACCEPT     A PM reads the thesis without scrolling past three more dark
                    bands. TODAY: four stacked bands, 6,548 px of 12-px text.
         SOURCE     brief O1; F1 resolved by Andrew ~04:5xZ
  FWD-22 The name's headline figures read as LABELLED TILES, not a mnemonic list
         DONE WHEN  EXERCISED -- price, market cap, net debt, enterprise value,
                    beta and short interest render as Stat tiles with units and
                    tabular numerals, and each tile's tooltip carries the
                    mnemonic and full-precision value verbatim
         ACCEPT     A PM never has to parse a float, and can still dispute any
                    tile. TODAY: 14 rows of 161867780096.00003 ABSOLUTE
                    CUR_MKT_CAP.
         SOURCE     brief O2
  FWD-23 Every drafted sentence keeps its evidence, folded until asked for
         DONE WHEN  EXERCISED -- a sentence shows its PASS face and a "cites N
                    passages" affordance; opening it reveals the passage and
                    accession line FROM THE DOM; and a census prints ZERO
                    passages carried in a native title= tooltip
         ACCEPT     The verbatim gate (AMGT-rj-2) is preserved BY CONSTRUCTION,
                    and a reader no longer scrolls 48 blockquotes to reach Risks.
         SOURCE     brief O3
  FWD-24 The Model sheet reads as a table and a refusal as ONE line per row
         DONE WHEN  EXERCISED -- the fiscal table renders as a white heatmap
                    panel with tabular numerals; a REFUSED row renders one status
                    icon and one navy sentence spanning the row; ABSENT rows fold
                    into a single footnote naming them
         ACCEPT     A refusal is readable once, not ten times. TODAY: the DPS row
                    repeats a 60-char refusal in ten red chips.
         SOURCE     brief O4
  FWD-25 The comparable set shows the columns that EXIST, and the absent ones
         are openable
         DONE WHEN  EXERCISED -- the table renders the PRESENT columns only; an
                    "Absent columns (N)" disclosure lists each with its registry
                    reason; the basis is a status chip with the test statement
                    one hover away
         ACCEPT     A PM reads five real columns instead of scanning twelve that
                    say ABSENT. TODAY: 17 columns, 12 ABSENT in all 18 rows,
                    under a 696-char paragraph.
         SOURCE     brief O5
  FWD-26 The Posture verdict reads as a headline and its reasons as cards
         DONE WHEN  EXERCISED -- the verdict renders as a Stat with the
                    comparable beside it; each reason is a numbered card with
                    cites folded; an UNRESOLVED cite renders a status.warning
                    ICON beside navy text and NOT amber text
         ACCEPT     Status colour never carries meaning as text on a light
                    ground (C6).
         SOURCE     brief O6
  FWD-27 The Lead Panel's controls read as the Dashboard's controls do
         DONE WHEN  EXERCISED -- Movement and Subject render as segmented
                    controls whose active state is WEIGHT AND RULE, the
                    generation and resolution lines sit in a "Source:" footer,
                    and the rendered state reads purpleFills == 0 in Universe
                    mode and == 1 (Refresh) in Security mode
         ACCEPT     One purple action per view (C8). TODAY: a filled purple view
                    chip plus two 10-px caption lines above the rows.
         SOURCE     brief O7
  FWD-28 Every panel renders one of the four DESIGNED states when empty
         DONE WHEN  EXERCISED -- PanelEmpty, PanelLoading, PanelError and
                    PanelNoPermission from src/ui/components/states each captured
                    at least once across the six states
         ACCEPT     An empty panel looks designed, as /market's already does.
                    TODAY: the empty Thesis is a centered sentence in a dark band.
         SOURCE     brief O8; C12
  FWD-29 The contract's render check PASSES, and CAN FAIL
         DONE WHEN  EXERCISED -- for each of the six states the JSON reads
                    bandContainersTopLevel == 1, fonts == {Lato}, weights within
                    {400,700}, no size below 11, radii within {2,3,4,pill},
                    shadows == 0 outside the focus ring, lowContrastChars == 0,
                    purpleFills per FWD-27, the four states present; the
                    drafting, tabs and posture harnesses green; AND THE SIX PNGs
                    READ BY A PERSON, a rejection citing its clause
         ACCEPT     ⭐ THE SAME INSTRUMENT READS TODAY'S PAGE AS FAILING EACH OF
                    THESE, WHICH IS WHAT MAKES IT A CONTROL AND NOT A CHECKLIST.
         SOURCE     brief O9; C-CLAUSE-CITED-REJECTION, C-RENDER-IS-THE-ORACLE
  FWD-30 A PM exports the name they are reading and gets a usable artifact
         DONE WHEN  EXERCISED -- the export produces EITHER (a) a presentation in
                    Opal Brand Guidelines form (deck_generation/DESIGN_BIBLE.md),
                    shaped like the Asset Management team's own earnings updates,
                    AT MOST TWO PAGES, OR (b) a machine-readable rich-text
                    output; AND a field-by-field comparison against the page
                    shows the SAME figures, the SAME cites and the SAME absences,
                    with NOTHING in the export that is not on the page
         ACCEPT     Adam forwards the output without reformatting it, and nothing
                    in it is unsourceable back to the page.
         SOURCE     Andrew-direct ~05:0xZ, VERBATIM "export option functional
                    with presentation in Opal Brand Guidelines form mimicking
                    Asset Mgmt team's earnings reports 2pg max or machine
                    readable rich text output".
                    ⛔ IN NEITHER L1 BRIEF -- found by subtraction (B.1).
                    THE "OR" IS HIS AND IS NOT COLLAPSED: either branch
                    satisfies; the 2-page cap binds branch (a) only; "functional"
                    means an artifact a person opens, not a button that resolves.
                    ⚠ If branch (a) needs a field no route serves, that is a
                    ROUTE change and returns to 1.0.0_SA_CTO~Z before it is
                    built (C-PRESENTATION-ONLY names this exception).
```

**BAR DISTRIBUTION: 19 of 20 are `EXERCISED`; only `FWD-9` is `APPLIED`.**

⚠ **THIS IS THE MOST IMPORTANT SINGLE FACT FOR L5. Nineteen outcomes cannot be closed by any
build.** **No cell may claim an `EXERCISED` outcome REALIZED on the strength of its own artifact.**
**Grade the `DONE WHEN` state line, never the `ACCEPT` paragraph beside it.**

---

## CONTRACTS -- v0.7 (ratified text; the reviewer is `3.0.0_SA_CVO`, always)

*Contracts are the shapes every cell must respect. Each one names the record it comes from. A contract that names an
owner assigns that part to that seat; every other contract is owned by this PRD's L4 author, and the cell that executes
it is assigned by the decomposition.
None of them is an outcome and none of them is graded; they are what a cell may not silently change.*

**C-PAGE-LAYOUT.** The Security Analysis page is ONE HEADER and FIVE TABS. The header is the discovery
surface: the Lead Panel's ranking cross (movement Trending | Breakout x subject Price | Chatter, List |
Chart), the company-level feed (publisher items from the harvest and, once the social-feed surface (S13, `FWD-11`) has measured a source,
social items), a one-line description, and the Posture line. The tabs, in order: **Thesis** (prose over
cited evidence + the one "big thing" chart), **Exec Management**, **Peers**, **Model**, **Posture**. Print
is a header export action, never a tab. The Coverage TAB is retired: its content is the header feed. The
Model tab is RESTORED as its own tab. The Model tab carries the model block in the shape of Adam's `Model` sheet,
the same way for every company.
Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_051xZ_SECURITY_ANALYSIS_HEADER_PANEL_FOUR_TABS_FILINGS_ANALYZER.md@a5c6a066de`; the voice memo `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_055xZ_TRANSCRIPT_SECURITY_ANALYSIS_PANELS_DRILL_DOWN.md@2285a23678`; measured shape: Adam's Boeing one-pager workbook
(`SUBSTRATE_CARDS.md` card 3).

**C-ONE-STORE.** The pool `s3://opal-data-harvest` is THE article store. The chatter
axis producer and the coverage reader READ the pool through ONE shared adapter: the association at
`publication-links/v1/{security_key}/{publisher}/{digest}.json` (its `security_key`, `publisher`, `article_key`),
the body at `publications/v1/{publisher}/{digest}.json`, where `article_key = publisher + ':' + article_id` is
the stable identity and `digest = sha256(article_key)`; the publication time is the body's **`published`** field
(the canonical schema `lib/opal_data_harvest/article.schema.json` has no `published_at` and forbids additional
properties; the consumer maps `published` to its own `published_at` at its
boundary and never substitutes `fetched_at`, the retrieval vintage, or the link's `first_discovered_at`); one
article counts ONCE per associated security however many links or retries carry it; a missing body, a
malformed record, an access denial and a partial read stay DISTINGUISHABLE from a quiet day and from an empty
feed; the DynamoDB articles table is RETIRED as a source once both readers are repointed, and nothing writes
it after that. The field-level source contract and the acceptance examples are the connection
brief `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_POOL_READERS_20260915_W.md@0e7de170e3`, including the package seam: the deployed archives must carry
the reader, its schema files and `jsonschema`, exercised in an isolated runtime. Inflow to the pool is TRACEABLE: every body carries its publisher, canonical URL,
stable identity and retrieval receipt. Andrew's word (`org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/ANDREW_DIRECT_20260915_0504Z_EXECUTIVE_MANAGERS_LUSHA_AND_THE_HARVEST_POOL.md@7cf62a165f`) names the pool as the system of record;
this contract makes it the only one. Owner of the readers: `2.0.0_SA_COO`; owner of the
writer: the harvest lane, whose mechanism and cadence stay reserved to Andrew by name. **The read path is superseded,
at a stated point, by `AMGT_HARVST`'s `C-HV-AXIS-PROJECTION`** (`org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md`
v0.2). When that project's gold `article_security_mention` and `chatter_daily` tables land, the chatter-axis producer
and the coverage reader read THOSE tables through this same single adapter; `publication-links/v1/` and
`publications/v1/` retire under `C-FORMAT-SEQUENCE` in one window with that move's never-widen pair. Until then this
contract binds as written.

**C-ONE-IDENTITY (sharpens `C-IDENTITY-RESOLVED`).** ONE canonical security
identity per economic security, resolved ONCE at the route boundary and carried unchanged through overlay,
thesis, peers, model, coverage, ranking and Posture. A VERSIONED, EXPLICIT crosswalk (`crosswalk/v1` in the
pool) maps that identity to its Bloomberg identifier (`BA US`), display ticker, model/pack key (`BA_US_Equity`)
and every publication-association key already persisted (`BA`, `security-<16 hex>`), carrying the source
universe row and the identifier's provenance. It preserves exchange and share-class distinctions; an unresolved
vendor identifier stays UNRESOLVED and is never guessed as US, never made by appending `US Equity` or stripping a
suffix; a folder rename is not a new security; the five pilots and the other 84 names sit in the same declared
system; the full universe reports 89 input names and ONE disposition per name; re-running the mapper or
changing a display label mints no second record. Article bodies need no migration (they are keyed
`publisher:article_id`); the read adapter learns the legacy association aliases or a separately verified link
migration runs, and in either case an old and a new link for the same article count ONCE; old links are
preserved until the transition is verified; no deletes. Source:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_IDENTITY_20260915_W.md@b90bfdd20d`.
Owner of the crosswalk and the route-boundary resolution: `2.0.0_SA_COO` (the round-11 cut
chooses the home); `Z-S95`'s remedy and disarm stay with their named owner.

**C-RANKING-GENERATION (the write rule for every ranking partition; sharpens s.3b's `C-SERVER-SIDE-RANKING`).**
A ranking run for one axis and one date publishes a COMPLETE GENERATION, and the reader selects that committed
generation: either an immutable generation plus a current pointer, or a bounded replacement of the whole
same-axis/date membership -- the cut names which, and an upsert that leaves prior rows in place is neither.
Zero winners, a changed winner and a failed or interrupted write are three DISTINGUISHABLE states: a
successful empty product clears the earlier membership; a producer or read failure leaves the prior generation
current and says so; no mixed generation is ever readable. Every generation carries its run id, its source
coverage vintage and its payload hash, and `Z-S72`'s exact-input exercise carries that identity, because a date
alone cannot tell two computations on one day apart. A reader Limit is NOT a repair: a stale row can itself
carry rank 1 and displace a current winner. Source:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_RANKING_RETRIES_20260915_W.md@5ae6dd04b5`.
Owner: `2.0.0_SA_COO`.

**C-ETF-PLANE-READ.** AMGT_RESAPP READS the ETF holdings plane `s3://opal-data-etfs` (`config/etf_universe.json`,
`gold/book/`, `gold/holding/`, `snapshots/snapshot_<date>.json` written daily at 22:00Z) and NEVER writes it.
That plane, its producers and its vintages belong to the `~Z` fabric's POSN_ASTTAX / ETFS_* projects. Every
Posture output and every membership claim carries the snapshot date it read. Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_051xZ_SECURITY_ANALYSIS_HEADER_PANEL_FOUR_TABS_FILINGS_ANALYZER.md@a5c6a066de`
(Posture) and `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_035xZ_W_FABRIC_IS_AMGT_RESAPP_ONLY_Z_FABRIC_IS_POSN_ASTTAX.md@9dfee40ce0` (the fabric split). ⚠ **The producer's side of this read is NOT yet a
contract:** the POSN_ASTTAX PRD `org/missions/D4/POSN/POSN_ASTTAX/prd/POSN_ASTTAX_PRD.md@ab2ee8052a` carries no CONTRACTS section and names none of these paths or the
22:00Z schedule; until the CTO pins a producer contract this
read is ONE-SIDED, every consumer carries the snapshot date AND the object's own schema version, and a layout
change on that plane is a cell in this project, never a silent repair. No POSN signature is implied or asked for.

**C-UNION-UNIVERSE.** The harvest universe is the UNION of the coverage list (`universe.json`, 89 name
folders) and the current holdings of the four Opal ETFs
at the snapshot vintage, so every comparable Posture names carries the same model block, feed, filings
and peers evidence as the target. Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_051xZ_SECURITY_ANALYSIS_HEADER_PANEL_FOUR_TABS_FILINGS_ANALYZER.md@a5c6a066de` (the third Posture word).

**C-SIMILARITY-RANKER (the rule for FWD-19's comparable; Rule 24 schema. FWD-8's peer set moved to `C-PEER-SET-SA` below).**
The comparable set of a subject is computed, never copied from a workbook (the F6 defect), by ONE ranker
over ONE database:
- the database = the Security Scanner's universe data (`UniverseDataRow`: ticker, name, mktVal, country,
  sector, industryGroup, universe weight for sp500 / r1000 / r1000v / acwx / eafe / eafev) UNION the
  harvest universe's model-block header scalars (classification, market cap, country);
- the rungs, lexicographic, in Andrew's order: same SECTOR, then a SIZE BAND (the existing engine's
  0.2x-5x market-cap band, `lib/research/peers/engine.py`), then same COUNTRY, then same SUBSECTOR
  (industry group); a numeric similarity within the last rung breaks ties (log market-cap distance);
- the four postulates: (i) MECE over the database -- every candidate is in exactly one rung or excluded,
  written as the database MINUS the excluded, with the denominator printed; (ii) same grain -- one
  security per row, one classification field named in every emitted set's `test` string; (iii) one
  intent -- similarity of business and scale, never valuation; (iv) state coherence -- the set carries
  `basis` = analyst | derived | absent as the engine already does, and a Seeking Alpha comparables list, if
  its API exposes one, is an INPUT candidate measured first, never the rule.
Source: the voice memo `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_055xZ_TRANSCRIPT_SECURITY_ANALYSIS_PANELS_DRILL_DOWN.md@2285a23678` (part three); card 3.

**C-PEER-SET-SA (FWD-8's peer set and comparison table; supersedes C-SIMILARITY-RANKER for FWD-8 only).**
- SET: a subject's peers are Seeking Alpha's suggested peers, 5 per subject (`/api/v3/symbols/{slug}/suggested`,
  `source_type=peers_similarities`), fetched through the EXISTING `integrations/seekingalpha/rest_fetch.py`
  (`load_config` / `build_session` / `_do_get`), GET only. No new fetcher, and never the crawler. `basis` = sa | absent;
  an absent set names its reason (no SA slug; entity test failed; no suggested peers; REHARVEST).
- IDENTITY FIRST: a subject's SA slug passes an ENTITY test (SA's company name shares a distinctive token with ours) before
  any peer call; a slug that fails it is UNRESOLVED with its reason, never the first hit. `ROG` -> Rogers Corporation, not
  Roche, is the standing positive control and must be refused. **Each PEER ticker's Bloomberg join passes the same
  name-agreement check** before its values are used -- the same trap one hop further out.
- TABLE: SA's shape, 17 of 17 CSC columns. Preferred + Minority is ONE column, `other_cap_struct`.
- SOURCE RULE (Andrew's, general for this pipeline): a column SA carries comes from SA; a column SA lacks comes from
  Bloomberg (the SA ticker queried as `<TICKER> US Equity`); where Bloomberg has no value, SA's nearest measure is used,
  LABELLED as that measure and never under the Bloomberg column's name. Every cell carries `source` = `SA` | `BBG` |
  `SA_FALLBACK:<field>`. One source per measure across a set wherever the data allows; every Average / Median / Min / Max
  row prints its source mix.
- NOT MEANINGFUL: an SA value flagged `meaningful: false`, or an absent SA value, is shown as such (ABSENT with SA's reason)
  and never zero-filled or filled from another source. The Bloomberg fill applies only to the columns SA lacks.
- SESSION: a 403 that `detectors.classify` reads as REHARVEST STOPS the run and says so. The Peers path never signs in,
  never retries around the challenge and never launches the harvester. Raw bytes land before derivation, at an address
  built by `lib/opal_naming.py` (Rule 30).
- PRODUCTION USE AUTHORIZED BY ANDREW, BY NAME (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md@4de34f0d95`):
  `C-SA-VENDOR-WORD` is lifted for THIS path -- one Peers read per security at instantiation and in validation, and its
  refresh. `C-SA-TERMS-BEFORE-SCHEDULE` is SATISFIED BY ANDREW for this path
  (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_20xxZ_AMGT_RESAPP_SA_TERMS_CLEARED.md@1699960261`).
- NOT CHANGED BY THIS CLAUSE: FWD-19's comparable (C-SIMILARITY-RANKER, C-POSTURE); C-VENDOR-EGRESS;
  C-IDENTITY-RESOLVED; C-ETF-PLANE-READ.
Source: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_17xxZ_PEERS_SEEKING_ALPHA.md@f48864fce6`.

**C-PEERS-V-FLOORS (amends the floors in `lib/research/scores/peers_v.py`).** MIN_PEERS_FOR_V 8 -> 5 and
MIN_PEERS_PER_MEASURE 6 -> 5; MIN_MEASURES_FOR_V (|M| >= 3) unchanged. Source: `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_17xxZ_PEERS_SEEKING_ALPHA.md@f48864fce6`, *"It's now 5 instead
of 8, we'll fit to the SA shape"*; the per-measure floor follows from his *"Agree with everything"*, which confirmed the
CRO's stated consequence (at 6, no measure computes over five peers). The asserts carry this citation in place of the
earlier ruling; they are floors, never loosened below 5 / 5 / 3. Peers V's `absent_reason` is never empty.
⚠ L4 READING, NOT ANDREW'S WORD: Peers V runs AS WRITTEN on its own Bloomberg `FIELDS`, pulled for the SA peer tickers
as `<TICKER> US Equity`. SA chooses WHO; the measure's own fields say WHAT. Feeding it SA's metrics would be a translation layer
and is not done.

**C-POSTURE (FWD-19's shape).** Posture = (1) MEMBERSHIP at the snapshot vintage (held / not held, book,
weight); (2) the COMPARABLE = the most similar name on the OTHER side by C-SIMILARITY-RANKER (an Opal
holding for a non-held subject; a non-held name for a held one); (3) the JUDGMENT over the two
evidence packs (each = Thesis, Exec Management, Peers, Model, all four for both names), producing
`{verdict: better | worse | hold | steer_clear, comparable: <security_key>, basis: [cited claims],
as_of: <snapshot date>, marked: machine}`, stored versioned in the pool under `posture/v1/{security_key}/
{as_of}.json`. A name's factor profile scored under the Opal ETF presets (DIVZ 13 factors, PFOE 16;
`SecurityScanner/constants.ts`) is the FIT input to (3). Posture is a recommendation surface: nothing in
the trade pipeline reads it. "The final execution" is a person's act on the page. Source: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_051xZ_SECURITY_ANALYSIS_HEADER_PANEL_FOUR_TABS_FILINGS_ANALYZER.md@a5c6a066de`
and the voice memo `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_055xZ_TRANSCRIPT_SECURITY_ANALYSIS_PANELS_DRILL_DOWN.md@2285a23678` (part five); card 3.

**C-FILINGS-ANALYZER (FWD-18's shape).** ⛔ **BLOOMBERG SUPPLIES KEYS, NEVER TEXT.** Bloomberg returns no filing text.
The analyzer reads the WINNING DOCUMENT of
the security's FILINGS BATTERY. Bloomberg supplies the keys that battery searches with: the CIK (`CENTRAL_INDEX_KEY_NUMBER`),
the LEI and the legal name. Its web address is a HINT, never a key.
**The battery -- ordered; the first document passing the acceptance test wins:**
- **US (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_16xxZ_THESIS_NO_RERUN_AND_FILINGS_BATTERY.md@96c22cdc72`):** (1) EDGAR; (2) EDGAR by the Bloomberg-resolved CIK; (3) web search, surfaced
  through the issuer's IR page.
- **International (RATIFIED by Andrew, `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md@4de34f0d95`; proposed at CRO brief s.8.2):** (1) EDGAR
  by ticker; (2) EDGAR by Bloomberg CIK; (3) ESEF / UKSEF by LEI; (4) the company's own site; (5) the national regulator,
  one adapter per jurisdiction, built only for a name that step 4 fails.
- **Terminal:** UNRESOLVED-SOURCE, persisted with every step's attempt, key and failure reason. Never a silent skip.
**One acceptance test, every step:** (a) **RIGHT ENTITY** -- the document names the listed issuer, checked against
Bloomberg's legal name and the LEI where the document carries one, otherwise the legal name plus a national registry
identifier. A subsidiary's report on the parent's domain FAILS.
(b) **CURRENT** -- an annual report for a fiscal year ended within the last 18 months. (c) **KNOWN FAMILY** -- a document
family the section cutter and the roster can parse; a cut from a family the cutter does not know FAILS (c) and never passes
as a section. Language is RECORDED, not tested (`C-FILINGS-TRANSLATION`). A failing document is recorded with its
reason, and the next step runs. The source object carries the winning step, the key it used, the family, the language and
the entity evidence; the family is recorded because cutting and roster parsing are BY FAMILY.
⛔ **Step 1 reads the LIVE SEC tables** -- the ticker table AND the submissions index -- never a cached subset, and applies the
name guard to EVERY listing, US included. A miss is reported against the table actually read, with that table's row count.
The analyzer calls the Claude API with document citations and writes TYPED rows to the pool
(`filings/v1/{security_key}/{accession}.analysis.json`): guidance changes, segment revenue, top risks, management commentary,
big bets, big challenges, and a THESIS DRIVER field naming the series the one chart is drawn from. With a JSON answer
requested, citations arrive INLINE and structured output cannot be combined with citations, so the cell is TWO PASSES or a
TAG PARSER, and the cut names which. Every sentence the Thesis tab shows is MARKED machine prose beside its cited passage
(FWD-9). The analysis carries an ANALYZER VERSION that MOVES whenever its output contract moves; a skip-on-unchanged rule is
built only after that, never before.
**Kept from the connection brief `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_FILING_EVIDENCE_20260915_W.md@a65fe406c2`:** every cited claim RESOLVES to an exact passage. The analysis
persists the source document and the exact submitted excerpt with content hashes, the canonical identity, the accession or
document id, the retrieval time, the parser version and an index-to-passage map. A claim whose tag resolves to nothing is
HELD uncited: never rendered as evidence and never a chart input. The drafting reader validates each evidence id's existence,
association and source version before `C-VERBATIM-GATE`, and runs that gate against the passage. The THESIS DRIVER series and
the officer role-start field are EXERCISED on a real filing before either is claimed to exist.
⛔ **NO FLEET RUN AND NO RE-RUN until the process is validated end to end** (`org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_16xxZ_THESIS_NO_RERUN_AND_FILINGS_BATTERY.md@96c22cdc72`). Stale analyses stay
stale. A validation run needs his per-use word; the three-name run is the precedent, not a standing grant. Building
any battery step that calls outside Opal needs his per-use word. The scheduled batch stays disabled until he activates it.
**NOT CHANGED:** the typed row set, the pool path, FWD-9 marking, the two-pass-or-parser choice, batch activation as
Andrew's call, and the roster authority (`C-EXEC-MANAGEMENT`).

**C-FILINGS-TRANSLATION (translation is a stage; `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_16xxZ_THESIS_NO_RERUN_AND_FILINGS_BATTERY.md@96c22cdc72`, *"a translation functionality will be required"*).**
⛔ **ANALYZE THE ORIGINAL; TRANSLATE THE OUTPUT.** A battery winner in any language is analyzed in its ORIGINAL language. Only
the analyzer's OUTPUT is translated. Every cited span re-locates VERBATIM in the ORIGINAL filing. ⛔ **Translating the passages
first is REFUSED:** the check would then verify against the model's own translation, and a mistranslation would be invisible.
**Where it sits:** after the cutter and the passage map, before analysis. Language is detected there and recorded on every
document, so the stage runs exactly when needed and a wrong detection is visible.
**Preconditions:** (i) **Unicode passages** -- no ASCII folding of evidence text; (ii) **citation blocks pre-cut to the passage
map** -- a plain-text document yields whole-document citations on a script without spaces; (iii) **a CHARACTER-LEVEL verbatim
rule** for scripts written without spaces.
**Contract for translated text (a value carries its claim):** each translated line carries `translated: true`, the source
language, the translator (model and prompt version) and the time, with the original sentence and its passage id beside it.
The page labels it a translation, never the filing's words. A chart point is verified in the original and parsed with the
document's locale and unit. Roster names keep the original script and take an English rendering only from the issuer's own
document.
**English edition:** an issuer's English document is used instead of translation only when it is the SAME fiscal year AND the
SAME document family and it passes test (c). A thinner document in English is a different document.
**NOT CHANGED:** `C-VERBATIM-GATE`'s object stays the original filing; the battery's acceptance test does not test language;
this clause authorizes no model call, producer or run.

**C-EXEC-MANAGEMENT (FWD-17's shape; `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20260918_17xxZ_EXEC_MANAGEMENT_CARDS.md@b0ff057a68` cards 1 and 2).**
The FILING's executive-officer section is the roster authority, and each officer's role start comes from it. When the
filing yields no RESOLVED roster, Bloomberg's `COMPANY_EXEC_OFFICERS` (name and title only, names kept verbatim) fills
the officer TABLE and is labelled on the page as a Bloomberg fallback. Role start, tenure and the pool comparison stay
ABSENT, with the reason that Bloomberg carries no role start. A RESOLVED filing roster replaces the fallback on the next
build. Every management object carries `roster_source` = FILING | BLOOMBERG_FALLBACK. ⛔ **The fallback never hides why
the filing failed:** when a filing roster failed (an empty officer-section cut, or a section no declared shape reads),
its own `roster_status` and `roster_reason` stay on the object beside the Bloomberg officers, and the page shows them.
Two further rules apply to every roster:
- A roster with ZERO officers is NOT SERVED. It is ABSENT with its reason. Every census and report prints the content
  count (names with at least one officer) beside the status count, and counts FILING and BLOOMBERG_FALLBACK separately.
- A roster row must be a PERSON. A title alone ("Executive Vice", "Senior Vice") is never accepted as a name. A roster
  whose rows all fail this test is not RESOLVED, so the fallback applies to it.
**Enrichment** (Lusha profile link and title) is a step of instantiating a new security. It attaches to an officer that
the roster's own source confirmed; Bloomberg-fallback officers are enrichable, and the label says which source applies.
The company domain comes ONLY from the site the filings battery VERIFIED as the right entity -- never a hand list, never
Bloomberg's raw web address. A name with no verified domain records Lusha as NOT ATTEMPTED, with that reason. Lusha is
never the roster. Each Lusha call is billed and runs only under Andrew's per-use word.
**The CEO profile** comes from a Bright Data SERP on the CEO's NAME, followed by an agent that reads the results and pulls
and organizes the relevant ones. The CEO is the only officer searched. **Who the CEO is:** the officer carrying a
chief-executive title; for a Japanese-listed issuer with no such officer, a "President" or "Representative Director and
President" is the chief executive. The rule is not extended to another jurisdiction without evidence for that
jurisdiction. A served reason is always a readable sentence; a missing value is never printed into it as a literal. The rules:
- A FAILED search (a request error or an unparseable body) is recorded as FAILED, with its cause -- never as an EMPTY
  search.
- Each organic result keeps its title and snippet, not the url alone.
- An identity test (this person, at this company, in this role) comes before any result is kept; a namesake is refused.
- Every organized fact carries its url and a quote that re-locates VERBATIM in the fetched page. A fact with no quote is
  HELD and never shown. The agent adds nothing from its own knowledge.
- The page renders the object's own `absence_class`, never a reason it infers, in FIVE states: CONFIRMED; NOT SEARCHED,
  with the reason; SEARCHED, NOTHING FOUND; SEARCHED, NOTHING KEPT (results read, none passed the identity test or carried
  a verbatim quote); SEARCH FAILED, with its cause.
- Bright Data calls, like Lusha calls, run only under Andrew's per-use word.
**The pool:** the average tenure is the mean over OFFICERS across EVERY current FILING roster -- the newest object per name
across all dates, within the union universe -- never over one run's objects. The denominator prints beside the value. No contact data point (email, phone, mobile) is stored at any level,
including in anything the CEO agent pulls.
This clause does NOT change: the filing as the authority, the role-start source, the pool's mean over officers, the
collection lane's owner (the harvest estate), or Andrew's standing "no fleet run until validated end to end". It
authorizes no run and no vendor call. Open at L4, not decided here: whether a Bloomberg-fallback CEO is searched.

---

**C-ROUND12-COMPARABLE-COVERAGE.** A Posture verdict STATES what its
comparable lacks and is STILL ISSUED; the verdict carries the comparable's evidence coverage beside it. A
comparable with no pack is NAMED as such. ⛔ Ordering is NOT restricted to complete packs and the comparable is
NOT drafted: restricting the ordering silently changes WHICH comparable is chosen, and drafting one manufactures
evidence. A stated gap is honest; a narrowed universe is a hidden decision nobody can see afterwards. Ruled
`1.0.0_SA_CTO`, `org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round11.md@4055200e2f` s.4 item 1.

**C-ROUND12-THESIS-ASOF.** The thesis bundle CARRIES ITS OWN `as_of_date`, sourced from the
FILING the drafting derives from, and ABSENT-explicit where no filing date resolves. ⛔ NOT `generated_at`, which
is the serve time, and NOT `identity.crosswalk_vintage`, which is an identity vintage. A reader asking "as of when
is this thesis true" is asking about the EVIDENCE, not about the request. Ruled `1.0.0_SA_CTO`,
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round11.md@4055200e2f` s.4 item 2.

**C-ROUND12-PRINT-SERVER-SIDE (settles the print route's 500; `FWD-5`'s producer).** The print pack is rendered
SERVER-SIDE: matplotlib, pypdf and numpy ship in the deployed archive or a layer, the template lives in the pool
rather than on a OneDrive path, and the renderer reads no worker-local deliverables folder and imports no plotting
library at module level. ⛔ NOT ruled a browser act: `FWD-5`'s displacement test is that a person forwards the
output AS PRODUCED, and a browser-rendered print is the analyst's own reformatting under another name.
Ruled `1.0.0_SA_CTO`, `org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round11.md@4055200e2f` A1.3 R2.

**C-ROUND12-PULL-WIRED (settles the 501 on refresh; `FWD-2`'s carrier).** The on-demand pull is WIRED, not
retired: the page calls the enqueue route, and the adapter DECLARES its queue carrier so the refresh route stops
answering 501. ⛔ **THE CONSUMER STAYS BOX-SIDE AND IS NOT A LAMBDA.** The reason is a dependency, not a
preference: the consumer reaches the Bloomberg desktop interface on the local loopback of the terminal box, so a
Lambda consumer would drain the queue and fail every message at the health check. The seam is box-side by its
own design. ⛔ **NO LAMBDA CONSUMER IS BUILT**, and the consumer's CADENCE is RESERVED to Andrew by name, on the
same standing as the harvest cadence -- a card, never a cell. ⛔ No alarm, monitor, freshness checker or
notification rides along: the standing moratorium binds, and a wired queue is not a monitor. Ruled at L10,
`org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round11.md@4055200e2f` A1.3 R3 as CORRECTED by ADDENDUM 2 C1.

**C-ROUND12-SURFACED-OUTCOMES (settles the three no-surface outcomes).** `FWD-7`, `FWD-12` and `FWD-14` each get a
SERVED ROUTE and a PAGE SURFACE. ⛔ An outcome whose only
implementation is a hand-run module is NOT REALIZED, whatever its rows say. If a round's fan-out cannot carry
them, they move to the NEXT round as data stated in the issuance -- never by omission. ⛔ **AND A CONTROL THAT
CANNOT ACT SAYS WHY.** A re-run control is bound to a stage that exists, or it REFUSES with a named reason; it
never records a silent skip and it is never a button that does nothing. A decoration does not satisfy this
contract. Ruled at L10, `org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round11.md@4055200e2f` A1.3 R4 as
extended by ADDENDUM 2 C2.


**C-ROUND12-DIVERGENCE-DEGENERACY (carries `FWD-20`'s pre-deployment gate; the numeric form the card states in
plain words).** Before Divergence is shown for any name, the producer measures the standard deviation of
Divergence ACROSS THE COVERED UNIVERSE. **A value below 0.25 is the documented sign that the drivers were seeded
from consensus after all, and that the factor is therefore not measuring disagreement.** Below that floor
Divergence is ABSENT for every name with that reason recorded, and the gate is checked BEFORE deployment. ⛔ **It
binds the MODEL-BLOCK PRODUCER, not only the page** -- a page-side guard would let a degenerate factor land in
the store and be read by anything else. Verbatim source:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_183xZ_MODEL_TAB_SCORE_IS_DIVERGENCE_FROM_CONSENSUS_FCF_AND_PEERS_RESENT.md@287d2c2619`
("sd(D) across universe < 0.25 -- drivers likely seeded from consensus; factor is not measuring disagreement").


**C-HARVEST-HOME (the storage home; CONDITIONAL until the registry resolves `harvest` to ONE scope row).** AMGT_RESAPP's
bronze, silver, gold, platinum, state and code live exactly where the builder prints them. Under scope `harvest` and
its GENERAL tenancy, that is `opal-data-harvest` for every tier, which is Andrew's (`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260918_2145Z_AMGT_RESAPP_OPAL_DATA_ASSETS_IS_CLIENT_DATA_ONLY_WHOLE_PIPELINE_IN_HARVEST.md@97341c3df2`) "the whole pipeline lives in
opal-data-harvest". The vendor is `{source}` for bronze and silver; `amgt` is `{source}` for gold, platinum, state and
code. Every address is `lib/opal_naming.py address()` output and every resource name is `name()` output; a builder
refusal is a missing registry row, never a hand-typed key. `opal-data-assets` holds client/partner custodial
information only. ⛔ **This contract is NOT MET while the registry carries more than one `harvest` scope row:** the
builder takes the first, a PRODUCT-tenancy row, and prints `opal-data-assets` for bronze and silver. No harvest writer
is cut against this contract until only the GENERAL row remains.

**C-BRONZE-AS-RECEIVED.** Bronze is the response bytes exactly as received -- no parsing, trimming or
re-serialising -- one object per fetch, never overwritten, with the channel's FETCH key in the partition, in one of
three forms: (a) an entity fetched repeatedly: `{vendor}/harvest/bronze/{request}/{entity}={id}/{YYYYMMDDTHHMMSSZ}.{ext}`;
(b) an immutable document: `{vendor}/harvest/bronze/{request}/{entity}={id}/{document id}/{vendor file name}`;
(c) a request: `{vendor}/harvest/bronze/{request}/date=YYYY-MM-DD/{request hash or file}.{ext}`. Every bronze
address a writer uses is one the builder printed; the measured outputs are listed in section 11. Where a vendor's
client hands the producer a parsed object and the wire bytes are unreachable (the Bloomberg Terminal client), the
received form is that object's deterministic JSON serialisation (sorted keys, fixed separators, UTF-8), so an
unchanged fetch yields identical bytes. A non-finite number (NaN, Infinity) is serialised as null, and the serialiser
refuses any other value JSON cannot carry. Each such object records the form in its S3 OBJECT METADATA, never in the
body, under the key `received-form` with the value `bbg-client-json`.

**C-SILVER-PARQUET.** Silver is parquet with every vendor field kept and typed, partitioned `date=` by fetch date,
one part file per run. Every row carries `bronze_key`, `fetched_at` and `record_hash` (sha256 of the row's vendor
fields).

**C-LUSHA-EXCEPTION (a declared departure, Rule 30 R20; `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260921_195xZ_AMGT_RESAPP_KEYENCE_SEARCH_YES_LUSHA_R20_YES.md@6e09c649aa`, *"Yes on Exception"*).**
Lusha keeps NO bronze, and its silver DROPS every contact field: emails, phone numbers, postal addresses, and any
personal messaging or social handle. It keeps the officer match, the title, and ONE public professional-profile URL.
That URL is the "profile link" `C-EXEC-MANAGEMENT` enriches with and the page shows; it is kept because it is that
served field, not as a channel for reaching the person. Nothing else a person could be reached through is kept. This departs from
`C-BRONZE-AS-RECEIVED` and `C-SILVER-PARQUET` for Lusha only. Its silver rows carry `fetched_at` and `record_hash`, and
`bronze_key` is null by rule. The R20 register entry is the registry lane's to write, citing Andrew's record.

**C-DEDUPE-BY-KEY (one writer per fetch key).** Each channel names a FETCH key and a RECORD key. Before any vendor
call, the writer checks the bucket for the fetch key. ⛔ **Exactly one writer holds a channel's fetch keys at a
time**, so no two writers can both read "absent" and both pay; a fan-out assigns a channel to one worker, never
splits it. A silver writer skips an unchanged `(record key, record_hash)` and writes a changed row as a new row,
never an update; a reader takes the newest `fetched_at` per record key. The bucket is the authority for what has
been fetched, never a file on one desktop.

**C-SLASH-SAFE-KEY.** One slash-safe security key is minted in the crosswalk module and used everywhere downstream.
An entity id sits in a partition, never in the builder's free-form `object` argument.

**C-FORMAT-SEQUENCE.** The backfill's gate is bronze and silver only: the tenancy act, the vendor registry rows, the
bronze writers, the silver writers with their record keys, and the fetch-key check. Gold (parquet) and platinum (a
JSON publisher the API reads) are rebuilt from silver after the backfill. Existing objects move by COPY with their
vintage, never by re-fetch or re-derivation; bronze that was never kept is filled by the backfill's FIRST fetch
under its fetch key, which is a first fetch, not a re-fetch. ⛔ **Each move of served objects carries its own never-widen pair, and
the source path's readers switch and the source path retires in the SAME window** -- a copy that leaves the old
path serving beside the new one is a standing duplicate output path, which the shadow-pipeline veto forbids. The
move is its own chain, not a rider on another cell.
- **"Retire" means** that in the move's window the old path's readers are switched, its writers are stopped, and its
  read grant is removed. It does NOT mean deletion. No move performs an S3 delete; deleting retired prefixes is ONE
  batched act on a human's word.
- **A lossless re-serialisation is a copy.** An existing JSON object re-written as parquet silver, with every field
  kept, counts as a copy under this contract, not a re-derivation. Each object is graded by a round-trip equality check.
- **Derived records split by what they are.** The `filings/v1` `.source.json` objects (the filing's own sections,
  cut from a document the pipeline never stored) move to SILVER. The `.analysis.json` objects (the model's reading)
  are what Opal cares about, so they are GOLD under R10 and follow the gold chain after the backfill. The document's
  bronze is filled only by the backfill's first fetch of it.
- **A served object whose reader cannot read silver's format keeps its one served path until the gold chain.** The
  served adapter reads JSON and carries no parquet reader. So `model_block` and the publication bodies and links stay
  on their current single served path. They move when the gold chain builds a served JSON projection: silver parquet
  is the system of record, the projection is what the reader reads, and the reader is switched and the old path
  retired in one window. No second served path exists meanwhile.


## 2. THE BOUNDARY

**THIS PROJECT OWNS:** the Security Analysis portal page and its design spec; the versioned pack
object and its store; the assembly path that fills it; and the print renderer that emits Adam's
artifact.

**IT RELIES ON AND DOES NOT OWN:** the Bloomberg terminal and its desktop API; the Bright Data
account; the residential-proxy + vision-authenticator pattern; the portal shell, auth and panel
primitives; and **the research corpus in SharePoint, which is READ-ONLY to us.**

⛔ **THE PROJECT BOUNDARY IS UNCHANGED BY THE MACRO RULING, AND THIS IS A NAMED TRAP.** Andrew ruled
that **`AMGT` (the macro) holds all of D5's research and analysis**, including the alt-research
corpus -- the research-call transcripts and the 63-name materiality queue. **That is a statement
about what the MACRO covers. It is NOT a statement about what THIS PROJECT consumes.**

Brief PART II stands verbatim: the corpus is *"the same directive, a DIFFERENT function"* and
**"AMGT_RESAPP does not consume or replace it."** ⛔ **If any later cell or seat proposes that
`AMGT_RESAPP` absorb the transcript corpus or the materiality queue, that is a NEW SCOPE QUESTION
REQUIRING ANDREW'S WORD.** It is not implied by the macro ruling and must not be inferred from it.
(Distinction drawn by `4.0.0_SA_CRO~Z`, msg 21007, and adopted.)

**EXPLICITLY NOT OWNED:** the missing Terraform declarations on the seven Seeking Alpha Lambdas (an
`AE_CloudOps` estate defect); the FactSet and CapIQ subscriptions; and **Adam's editorial judgment
-- the analyst-specific sections are the value of a pack and this project drafts toward them, it
does not replace them.**

---

## 3. CONSTRAINTS ON THE CUT

Each is binding on L5 and L7. Cite the constraint id, never this section.

### Data correctness -- these three are the measured landmines

**`C-UNIT-MAP-MEASURED`** -- ⛔ **A MNEMONIC-ONLY FIELD MAP IS SILENTLY WRONG BY 100x IN SOME CELLS
AND 1e6 IN OTHERS.** Measured (brief F4): market cap is absolute while net debt and enterprise value
are millions; shares outstanding is absolute while diluted-EPS share count is millions; margins are
percents where the source holds decimals; capital expenditure's sign is inverted. **Every mapped
field carries a MEASURED unit and sign, never an inferred one, and the measurement is per field.**

⚠ **v0.11 (Model brief @`f48864fce6`, M1).** The map is built for EVERY name at instantiation, not the three pilots. Its home is
version control beside the producer that reads it (`C-PRODUCTION-HOME`); today it sits in a worker's deliverables folder
(`integrations/bloomberg/research/model_block_pull.py:286-288`, worker `~1`), and for every other name `_resolved_unit`
(`:300-316`) falls back to "not yet built" and the check face refuses. **All 348 measured refusals are this one missing entry,
not bad data.** Building the map needs NO new pull: the `derive` stage re-reads the raw block from the pool. A field whose unit
is not measured stays REFUSED; it is never inferred to clear a refusal.

**`C-MODEL-FORECASTS` (v0.11; Andrew-direct ~18:4xZ 2026-09-18, *"I'd use Bloomberg as primary, seeking alpha as a fall
back"*).** The Model carries forecast years FY1-FY3 beside the history. **Bloomberg is primary**: the `BEST_` consensus
fields (`BEST_EPS`, `BEST_SALES`, `BEST_EBITDA`, `BEST_PE_RATIO`, `BEST_DPS`), each pulled with an EXPLICIT
`BEST_FPERIOD_OVERRIDE` per year -- without the override a `BEST_` field returns the next QUARTER, which reads as a plausible
annual value (measured). Coverage measured with the override: `BEST_EPS` 33/33/33, `BEST_SALES` 33/33/32, `BEST_EBITDA`
31/31/31, `BEST_PE_RATIO` 31/32/32, `BEST_DPS` 33/33/33; control BA FY2026-28 EPS -0.83 / 3.95 / 8.05. **Seeking Alpha fills
a cell only where Bloomberg has none.** Every cell carries its fiscal year and `source` = `BBG` | `SA_FALLBACK`. Column headers
come from `BEST_PERIOD_END_DATE`, never from a counted offset. The page labels the columns CONSENSUS, never reported. **The
SA fallback is a Seeking Alpha production read, AUTHORIZED for this path by name** (v0.12, Andrew-direct ~19:4xZ, *"Yes use SA
thats fine"*); `C-SA-TERMS-BEFORE-SCHEDULE` is satisfied for it (v0.13, *"I have already clarified SA ToS, we are good"*). The refresh cadence is Andrew's (his Bloomberg-cadence reservation stands).

**`C-MODEL-WINDOW-AND-ROWS` (v0.11).** (1) **The window rolls:** the history ends at each issuer's LATEST CLOSED fiscal year --
a year that has ENDED and been REPORTED -- never a fixed date (today `HIST_END = "2025-12-31"`, `model_block_pull.py:101`).
(2) **Five sheet rows have no field today** (Revenue per share, FCF yield, FCF margin, return on total assets, earnings
margin). The Bloomberg fields that carry them join the producer's field list; the page never computes them, and keeps refusing
until the field exists. (3) **The model block is an instantiation stage** (section 10): pulled when a security is added, then
refreshed after each fiscal close on a cadence Andrew sets; today every block is one hand run dated 2026-09-16. (4) **The
yellow key:** every Bloomberg call names the security as `<RESOLVED bloomberg id> Equity` or reads the block's own security
string. The crosswalk's `bloomberg` field carries no yellow key, and a call without one returned 33 of 33 security errors --
a failed instrument reading as zero coverage. **Appending the yellow key to an id `C-ONE-IDENTITY` has already RESOLVED is not
the guess it forbids** (making an id by appending `US Equity` to an unresolved one). (5) **The Base case is consensus EPS x
the security's own trailing-median P/E** (v0.12, Andrew-direct ~19:4xZ, *"Base."*), each input carrying its source and
window. **Upside and Downside stay ABSENT** with the reason "methodology to be discussed with Andrew" (*"I think the upside
and downside cases can be discussed on methodology"*); no seat chooses a spread. (6) The robustness
inputs (quarterly TTM over the ruled 8-quarter window) are an open L4 question at `1.0.0_SA_CTO~Z`, not a round-14 cell.

**`C-FISCAL-YEAR-JOIN`** -- ⛔ **NEVER JOIN PRICE TO FUNDAMENTALS ON THE DATE STRING.** Measured
(F5): 4 of 10 years land split, 14 rows for 10 fiscal years, and a date-string join **silently drops
40% of that name's price history**. **Fiscal year is the join key.**

**`C-BLOOMBERG-BASIS`** -- Andrew-ruled (F3): **adopt Bloomberg's definitions and STATE THE BASIS
BESIDE THE NUMBER.** No Bloomberg mnemonic reproduces FactSet's recurring EPS across 8 tested --
that normalization is proprietary and **must not be reverse-engineered into a lookalike figure.**
⚠ The field map was measured on **ONE security**; a US name, an ADR or a financial is the most
likely place F4's conventions differ, and **nothing establishes they generalise.**

### Pipeline shape -- constraints, not a design; sequencing is L5's

**`C-RAW-BEFORE-DERIVED`** -- raw vendor bytes land before anything derives from them. ⛔ **This is a
CORRECTNESS requirement and not an optimisation:** Bloomberg's derived fields have **no backfill**,
so a rule change that cannot be re-derived from stored raw bytes is a permanent data loss.

**`C-STAGE-PERSISTS`** -- every stage persists its own output and is **independently re-runnable**.
Serves `FWD-12` directly. **A single refresh that moves everything under one timestamp is a
violation, not a shortcut.**

**`C-VERBATIM-GATE` (v0.11)** -- wherever output quotes a source, the quoted text must be an exact substring of the ORIGINAL
fetched text, inside the passage the sentence cites; normalisation is limited to whitespace and Unicode canonical equivalence,
and a fold that changes characters (ASCII folding, symbol substitution) is not verbatim; non-verbatim is **rejected and
regenerated**. ⛔ **EVERY PASS COUNT PRINTS ITS SPLIT:** passed on a span / passed with NO span / held. A count that omits the
split is not evidence of verbatim coverage (measured D18: a sentence with no quoted span passes today -- 17 of 39 for CAT, 16
of 40 for CSL -- so the "389 of 389 PASS" figure did not mean what it read as). ⛔ **A drafted sentence with no verbatim span is
HELD: never served, and counted in the split** (v0.12, Andrew-direct ~19:4xZ, *"Agreed, yes."*). Over today's 12 served documents
this withholds **179 of 389 sentences (46%, measured 2026-09-18 by `4.0.0_SA_CRO~Z`, msg 23744)**; the validation names ran
17 of 39 (CAT) and 16 of 40 (CSL). It reverses the v0.7 choice to keep passage support and exact quotation as separate outcomes; both
consequences were on the card he answered. The minimum run length is word-based for spaced
scripts and CHARACTER-based for scripts without spaces (`C-FILINGS-TRANSLATION`); the cut states each threshold. The rule binds
BOTH writers of `drafting/v1/<key>.json` (`batch.py:150`, `analyze.py:1215`). ⭐ **This is a GATE, not trust-the-model**: it is
machine-checkable and has discriminating controls -- a span pointed at the neighbouring passage, and a one-character mutation of
a passing span, must both be REFUSED.

**`C-MARK-NOT-DEGRADE`** -- ⛔ **a failed stage MARKS the pack; it never silently produces a thinner
one.** A thin pack that looks whole is the exact failure `FWD-10` exists to prevent.

### Validation -- the six classes, and what L4 does and does not fix

Brief III-B names six classes that must each carry a stated qualification rule: **a figure, a peer,
an identity, a news or social item, a source, a generated sentence.**

**`C-RULE-MUST-EXIST`** -- **an input class with no stated rule is NOT SHIPPED DARK.** It is either
ruled on or held back from the page. There is no third option.

**`C-CHECK-MUST-REFUSE`** -- ⛔ **A CHECK THAT CANNOT FAIL IS NOT A CHECK.** Every rule **names the
input that makes it refuse**, and that input is exercised. A rule whose refusal case was reasoned
rather than run has not been tested.

**`C-SHARED-DEFECT`** -- ⛔ **A CHECK SCOPED TO EACH ITEM CANNOT SEE A DEFECT THE ITEMS SHARE.**
Measured on this very project: the stale peer set passed every per-name look for months because
nothing asked what the 54 workbooks had in COMMON. **Every class carries a per-item check AND one
unscoped pass over the population.**

⛔ **NO THRESHOLD IS SET IN THIS PRD, AND THE OMISSION IS DELIBERATE AND BOUNDED.** L1 refused to set
one because a number invented early is treated as ratified by every later stage. **L4 does not
invent one either, for a different reason: the estate has not measured the distributions any
threshold would have to be drawn against.** ⛔ **An unmeasured exact constant fails closed while
looking principled**, which is worse than an absent one.

>> **WHAT L4 FIXES INSTEAD, AND THIS IS THE INSTRUCTION TO L5:** each class's cell must **produce the
>> measurement from which its threshold is drawn, and state the threshold in its own deliverable**.
>> The cell that maps figures measures the field population; the cell that admits news measures the
>> ratio of about-the-security to merely-contains-the-string. **A threshold arrives WITH the
>> distribution it was drawn from, or it is not a threshold.** <<

**`C-IDENTITY-RESOLVED`** -- serves `FWD-13`. The Bloomberg ticker, the Seeking Alpha symbol, the
investor-relations domain and the social account are **four different keys, and the social one has
no shared identifier at all.** ⛔ **Two sources may not be displayed together on one page until their
identity is confirmed resolved; where it cannot be, the page SAYS SO rather than showing them side
by side.** The measured instance is F6 -- 48 of 54 packs carrying another company's peer set.

**`C-LIST-OWNER`** -- serves `FWD-14`. The publisher allowlist and the company-to-social-account map
are **living lists that rot**. Each carries a **named owner** and a **rot signal**. ⛔ **An enumerated
list with no owner lapses silently** -- the same failure that left two vendor keys dead.

### Standing law -- inherited, not minted here

**`C-VENDOR-EGRESS`** -- ⛔ **NEVER call an external vendor API without Andrew's explicit per-use
word. Availability is not authorization.** This binds every Bright Data dataset call, every Seeking
Alpha fetch and every proxy request. **A cell may not spend that word and may not assume it.**

**`C-LISTING-NOT-CAPABILITY`** -- ⛔ **NOTHING ABOUT THE SOCIAL DATASETS HAS BEEN EXERCISED.** F12
measured they are LISTED and reachable: 1,763 datasets, HTTP 200. **No dataset was triggered, no
record returned, no cost, field schema, latency or freshness observed**, and whether the post-level
sources can be queried by cashtag at all is unknown. ⛔ **A LISTING IS A CATALOGUE ENTRY, NOT A
CAPABILITY** -- `FWD-11` must not be cut as though social data is in hand. **The first social cell's
job is to find out, and its acceptance criterion is allowed to be a measurement rather than a
feature.** ⚠ And F13: the cashtag-native venue carries **0 datasets** on this account, so the feed
is general-social plus finance-adjacent. **That limit is a required disclosure of the feed itself**
(`FWD-11`'s own source line), not a footnote.

**`C-ZONE-IN-CALLER`** -- one account credential, three zone archetypes, selection lives in the
caller. ⚠ **F12's dataset API is a FOURTH SURFACE, not a fourth zone** -- same credential, different
API. A reader who assumes everything is one of three zones will hunt for a zone that does not exist.

**`C-DESIGN-SPEC-FIRST`** -- **no `.tsx` is written until the design spec is approved.** The estate's
own precedent gates it in exactly these terms.

**`C-NO-CONTACT`** -- ⛔ **NO SEAT CONTACTS ADAM MULLER.** Andrew-ruled. Requirements reach him
through Andrew and no other route.

---

### 3a. SEEKING ALPHA -- ANDREW-DIRECT 2026-09-10 ~18:4xZ

**His words, verbatim and complete**, typed at the `2.0.0_SA_COO~ZZZ` terminal and relayed
(record `ANDREW_DIRECT_20260910_184xZ_COOZZZ_SEEKING_ALPHA_IN_THE_TOS_...md` @`ee0eacab07`):

> *"Something I want to fold in to your TOs, there should be a section somewhere in there on Seeking
> Alpha, pulling info from it and testing SA etl. I want to note that this is a good page to scrape a
> modal popup `https://seekingalpha.com/symbol/{TICKER}/virtual_analyst_report`. I also want to
> explore actually hitting their REST API with an authenticated bundle versus doing all this scraping
> bullshit, hence why we have my user info in AWS Secrets Manager."*

⛔ **THIS ADDS NO OUTCOME AND THE id LIST IS UNCHANGED.** Analyst commentary on the page is already
`FWD-4`; the Seeking Alpha symbol is already one of the four keys `C-IDENTITY-RESOLVED` names. **What
his word adds is a NAMED SOURCE, a REQUIRED COMPARISON, and the closing of one open precondition** --
those are constraints and surfaces, not a new capability. Inflating the outcome list for a source
would make the endpoint a list of implementations.

> ⛔ **SUPERSEDED BY MEASUREMENT 2026-09-10 ~19:5xZ.** `4.0.0_SA_CRO~Z` investigated the route on
> Andrew's word and the finding CONTRADICTS the source he named, on evidence:
> `org/tier1_exec/4.0.0_SA_CRO/deliverables/AMGT_RESAPP_SEEKING_ALPHA_AUTH_INVESTIGATION_20260910.md`
> @`b1656bbebc` -- **the vintage matters and this citation was written without one.** At this
> seat's read the file was STAGED AND UNCOMMITTED, so the only reference available was a
> working-tree path, which is not a citation. `4.0.0_SA_CRO~Z` landed it minutes later and the
> hash is verified here with a negative control (a bogus path in the same tree returns empty).
>
> **THE MODAL PAGE IS THE WRONG INSTRUMENT.** `seekingalpha.com/symbol/{TICKER}/virtual_analyst_report`
> is JS-rendered and **its HTML carries none of the content** -- a plain fetch returns *"Javascript is
> Disabled"*. The content the page displays lives ONLY at the endpoint the page itself calls once.
> **Scraping that page could never have worked, and no amount of care in a cell would have found that
> before building it.**

**`C-SA-NAMED-SOURCE` (AMENDED)** -- the named source for `FWD-4` is the **API artifact, not the page**:
`GET /api/v3/symbols/{ticker}` returns the internal `sa_id`, and `GET /api/v3/virtual_analysts/{sa_id}`
returns the report as JSON (markdown `responseContent` plus a ratings block, each bullet citing an
article id). Analysis and news reach full bodies via `GET /api/v3/symbols/{t}/analysis|news` ->
`GET /api/v3/articles/{id}`. ⭐ **NO HTML PARSING ANYWHERE ON THIS PATH.** The report re-generates every
few days and carries its own `createdAt` and `previousReportDate`, so `FWD-6`'s what-changed axis is
served by the source itself rather than reconstructed.

**`C-SA-ROUTE-COMPARISON` -- DISCHARGED, NOT PENDING.** Andrew asked to *"explore ... versus"* and
the comparison HAS BEEN RUN by `4.0.0_SA_CRO~Z` under his own per-use word. ⛔ **NO CELL RE-RUNS IT.**
The result, measured:

| route | verdict |
|---|---|
| authenticated REST with a browser-harvested session | **WORKS** -- 200 on every ticker and every article tried |
| scraping the modal page | **CANNOT WORK** -- the page is JS-rendered and its HTML holds no content |
| cookieless unlocker | **CANNOT WORK** -- empty body; an unlocker cannot ride an authenticated session |

**`C-SA-SESSION-SHAPE`** -- the production shape is **harvest in a real browser, park the session, ride
by REST through the residential proxy, re-harvest on the challenge signal.** Two conditions are
load-bearing and both were measured one variable apart:
- **the jar must carry the browser-minted bot-protection cookies AND the request a per-ticker `Referer`.**
  Identity cookies alone return 403. The full jar with no `Referer` returns **200 with a 2-byte body** --
  ⚠ **a success status over an empty payload, which is the shape that cost that investigation a round
  and would silently produce empty rows in production.**
- **the fetch must egress through the residential proxy.** This device's native IP served ~10 calls and
  was then blocked for every call including ones that had just worked.
A short-lived challenge cookie expires; **the re-harvest signal is a small challenge body on a 403, and
it is NOT an auth failure** -- a cell that treats it as one will re-authenticate instead of re-harvesting.

**`C-SA-NO-POST-THROUGH-PROXY`** -- ⛔ the residential zone **refuses every POST** (`policy_20130`,
no-KYC access mode). A login is a POST, so **login can never complete through the proxy** and the
harvest must run somewhere with real browser egress. Andrew is completing the KYC; until it lands the
proxy carries **reads only**, which is the whole production path anyway.

⚠ **THE CREDENTIAL AND THE SESSION ARE BOTH IN SECRETS MANAGER AND NEITHER NAME IS WRITTEN INTO A
CELL BY THIS PRD.** They are located at run time. The parked session artifact was created 2026-09-10
19:29Z by that seat.

**`C-SA-PAYWALL-PRECONDITION-PARTLY-CLOSED`** -- §5's open precondition read *"A decision on
paywalled sources ... Nobody has decided."* **Somebody now has, in part:** authenticated access is
IN SCOPE TO EVALUATE. ⚠ **It is NOT thereby ratified for production**, and whether the login is
captcha-gated remains unmeasured, so the vision-authenticator question stays open.

**`C-SA-UNMEASURED`** -- ⛔ **FIVE THINGS THE INVESTIGATION EXPLICITLY DID NOT ESTABLISH, AND A CELL
MAY NOT ASSUME ANY OF THEM.** Named by `4.0.0_SA_CRO~Z` against its own work, which is why they are
usable:

| unmeasured | why it bites |
|---|---|
| **session lifetime** | observed ~30 minutes; the TTL is unknown. The re-harvest cadence is a GUESS until measured |
| **headless / Linux** | every green run was a HEADED real browser on this Windows device. A box deployment must exercise headless FIRST -- it is the likeliest thing to fail |
| **MFA** | the account showed no OTP step. Whether the vendor forces one on a new device or geography is unknown, and the harvester has no adapter wired |
| **rate limits** | paced at roughly one call every 1-3 seconds; nothing faster was tried |
| ⛔ **the vendor's terms on programmatic access** | **NOT READ.** This is the one on the list that is not an engineering question |

⛔ **THE TERMS QUESTION IS ANDREW'S AND IT IS NOT A CELL'S TO SETTLE.** A scheduled consumer reading a
paid account's content programmatically is a commercial and contractual posture, not a build detail.
**It is surfaced to him and NOT built around.** Nothing in this PRD authorises a cell to read those
terms and rule on them.

> ⭐ **RULED 2026-09-10 ~21:1xZ. ANDREW-DIRECT, VERBATIM: "all recs approved but call 3, dont need
> alarm."** -- approving this seat's recommendation on the terms card. **THE RULING: the vendor's
> terms are READ BEFORE ANY SCHEDULED CONSUMER SHIPS. The exploration and comparison he already
> authorised do NOT need them.**
>
> **`C-SA-TERMS-BEFORE-SCHEDULE` (new, binding):** no cell may stand up a RECURRING or SCHEDULED
> read of this vendor until the terms on programmatic access have been read and the finding
> recorded. ⛔ **A one-off exploratory fetch is NOT a scheduled consumer and is not gated by this.**
> ⛔ **AND NO CELL READS THE TERMS AND RULES ON THEM** -- the reading is a task, the ruling is
> Andrew's, and a cell that does both has taken a commercial decision it does not hold.
> **v0.13: SATISFIED for `C-PEER-SET-SA` and `C-MODEL-FORECASTS`'s SA fallback** -- Andrew-direct ~20:0xZ, *"I have already
> clarified SA ToS, we are good"* (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260918_20xxZ_AMGT_RESAPP_SA_TERMS_CLEARED.md`).


⛔ **`C-SA-VENDOR-WORD` -- THE PER-USE EGRESS READING, RULED HERE BECAUSE IT IS L4's AND
`2.0.0_SA_COO~ZZZ` CORRECTLY DECLINED TO RULE IT.** `C-VENDOR-EGRESS` requires Andrew's explicit
per-use word and says a cell may neither spend nor assume it. His sentence names **the vendor, the
route, the authentication and the credential's location, in the imperative**, which is far past
"availability".

| | |
|---|---|
| **AUTHORIZED** | the EXPLORATION and the COMPARISON -- calling the route to establish whether it works, and how it compares to the scrape |
| **NOT AUTHORIZED** | recurring or production use of that route. **A word for an evaluation is not a standing right**, and `C-VENDOR-EGRESS` is per-use by construction |
| **LIFTED BY NAME (v0.12)** | Andrew-direct ~19:4xZ, *"Yes use SA thats fine"*: production use at instantiation and in validation for exactly two paths -- `C-PEER-SET-SA` and the `SA_FALLBACK` cells of `C-MODEL-FORECASTS`. Every other route stays NOT AUTHORIZED |
| **TERMS CLEARED (v0.13)** | Andrew-direct ~20:0xZ, *"I have already clarified SA ToS, we are good, if I had an issue with the design i wouldnt have designed it this way."* `C-SA-TERMS-BEFORE-SCHEDULE` is SATISFIED for the two paths above: his ruling on the terms is recorded, so their scheduled refresh is not gated by it. No terms-reading task is owed |

⚠ **THIS READING IS THIS SEAT'S AND ANDREW MAY CORRECT IT.** It is recorded so a cell does not have
to guess, and so that if it is wrong it is wrong in ONE place with a name on it rather than in every
cell that touches the vendor.

---

### 3b. THE APPROVED SURFACE -- ANDREW-DIRECT 2026-09-11 ~12:1xZ ("Recs approved")

Record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_121xZ_OPEN_CALLS_ALL_FOUR_RECS_APPROVED.md`.

**⛔ `C-DESIGN-SPEC-FIRST` IS LIFTED FOR THIS PROJECT.** Andrew approved the amended page shape: three
tabs (Thesis / Peers / Coverage) beneath a persistent **Lead Panel**; Print as a header export action;
the Model tab CUT with its figures rehomed into Thesis and the Security overlay. `.tsx` is authorized
in the SURFACE round (a later issuance, after round 4 drains). `FWD-15` is his confirmed outcome.
⭐ **SUPERSEDED AT v0.6/v0.7 as to the SHAPE (s.9f):** `C-PAGE-LAYOUT` -- one header and FIVE tabs (Thesis, Exec
Management, Peers, Model, Posture); the Coverage tab's content becomes the header feed and the Model tab is
RESTORED. The lifting of `C-DESIGN-SPEC-FIRST`, the `.tsx` authorization and `FWD-15` stand unchanged.

**`C-AMGT-ARTICLES-STORE`** -- per-ticker article content lands in a NEW DynamoDB table
`opal-harvest-articles` (RENAMED from `opal-amgt-articles` 2026-09-11; env knob
`HARVEST_ARTICLES_TABLE`), shaped like `opal-news-articles` (title/source/url/published_at/sentiment) plus
`ticker`/`security_key` (via S12) and `platform`. GENUINELY SEPARATE from the general-market
`opal-news-articles` (not that table with a filter) and from `opal-data-harvest` (which stays S1's
model-block + S5's print-snapshot home; RENAMED from `opal-data-research` 2026-09-11, env knob
`HARVEST_BUCKET`). Serves S4 (`FWD-4`) + S13 (`FWD-11`). ⛔ S12 must resolve each
platform's OWN identifier before dispatch (SA symbol-slug, Bloomberg `"TICKER US Equity"`, FT id).
⭐ **SUPERSEDED AT v0.6/v0.7 (s.9f) by `C-ONE-STORE`:** the pool `s3://opal-data-harvest` is THE article store
and this table is not; TRANSITION: the table stays readable until BOTH readers (chatter axis, coverage) are
repointed at the pool and exercised, then it is retired as a source and nothing writes it. S12's per-platform
identifier clause stands and is sharpened by `C-ONE-IDENTITY`.

**`C-SERVER-SIDE-RANKING`** -- Trending/Breakout/Price/Chatter are computed SERVER-SIDE by daily jobs
and written as pre-computed per-ticker rows into a SEPARATE metrics table
`opal-harvest-security-metrics` (RENAMED from `opal-amgt-security-metrics` 2026-09-11, MIGRATED with
42 live rows on full item equality; env knob `HARVEST_METRICS_TABLE`)
(mirroring the proven `opal-news-articles` / `opal-news-trending-daily` split). The Lead Panel READS
them and never re-derives a ranking at render time. Chatter axis = the committed chatter gate (30-day,
0-100 normalized, TOP_N=10); Price axis = the new engine (S16).

⚠ **v0.11 (Lead Panel brief @`9136ff9e73`, L2 and L5) -- NO RANK WITHOUT SIGNAL.** A ranking never lists a member with no
signal. Today Trending x Chatter ranks ten names that all have zero articles and score 0, in alphabetical order, and the list
looks finished. **Signal, per subject:** CHATTER -- at least one article for the name in the window (score above zero);
PRICE -- at least two observations in the window, the movement gate's own `INSUFFICIENT_OBSERVATIONS` test. A SUCCESSFUL run
whose every member lacks signal, or fails its breakout test, publishes an EMPTY generation carrying `empty_reason`: the
dominant exclusion reason and its count over the printed denominator (today Breakout x Chatter computes
`BELOW_MIN_ABSOLUTE_JUMP` for 191 of 191 and discards it). **A FAILED run is not EMPTY**: it stays a failure and the prior
generation stays current, as `C-RANKING-GENERATION` already requires. `empty_reason` is part of the pointer contract: BOTH
generation writers (`lib/research/metrics/chatter_axis.py`, `lib/research/price/generation.py`) write it through ONE shared
pointer builder in place of today's two copies, it is covered by the generation's `payload_hash`, and the adapter carries it
to the panel, which shows it in place of an empty list.

**`C-PRICE-RANKING-BOXSIDE`** -- the price axis reads Bloomberg historical/intraday and therefore runs
in the BOX-SIDE puller shape (the ETF-daily-pull shape), NOT a Lambda calling Bloomberg. 30-day window,
matching chatter (Andrew unified both to 30).

**`C-PRICE-BREAKOUT-FLOOR` (v0.11; Andrew's Lead Panel card B, sequenced msg 23684).** A price BREAKOUT is a POSITIVE move of
at least **+5% over the trailing 30-day mean close**, measured UNSMOOTHED: `(close - mean) / mean >= 0.05`, with `mean > 0`.
⛔ **It is NOT a `MIN_ABSOLUTE_JUMP` entry:** that table holds a jump in the subject's own units, and the chatter smoothing
(`BASELINE_SMOOTHING = 1.0` in `breakout_pct`'s denominator, `lib/research/metrics/movement_gate.py:386-398`) is a
count-scale device that would shade a percentage on a price. The price rule is its own test, and the chatter floor is never
transplanted onto price. Measured before it: 23 of 32 listed price "breakouts" were FALLING names (the gate returns
`NO_RATIFIED_ABSOLUTE_FLOOR`, `:413-428`). The count under the new rule is RE-MEASURED by the cell, never asserted from this
figure. Card B is a direct act with card A, B first, under a never-widen pair.

**`C-PRICE-DAILY-LEG` (v0.11; Andrew's Lead Panel card A, sequenced msg 23684).** Prior-day prices are pulled on the EXISTING
daily job (`scheduled_daily_pull.cmd`) as their own leg with their own exit codes (80-83), a change record opened first and a
never-widen pair signed; the price lists were 3 trading days stale without it. Staleness is counted in TRADING days
(`lib/trading_calendar.py`), never calendar days.

**`C-DESCRIPTION-LINE` (v0.11; Lead Panel L8; order corrected at v0.12 on `4.0.0_SA_CRO~Z`'s L4-R review, msg 23744).** The
one-line description has three sources, in this order: (1) Bloomberg's description field -- `CIE_DES`, else `CIE_DES_BULK` --
added to the model-block pull's header list and labelled as Bloomberg's (today the pull never requests `CIE_DES`, and
`CIE_DES_BULK` is populated for the 21 names with no filing identity); (2) else the first sentence of a VALIDATED drafted
`company_description` section, marked machine, with its evidence ids, **ONLY if it passes a stated describes-the-business
test** -- the test's wording is the cut's; (3) else ABSENT, naming every probe. ⛔ **"VALIDATED" means schema-valid, not
descriptive:** measured 2026-09-18 over the 12 served names with the adapter's own reads, sentence 1 of `company_description`
describes the business on 0 of 12 (Boeing: *"Commercial Airplanes revenue was $41,494 million in 2025..."*; Home Depot:
*"Consolidated net sales were $164.7 billion in fiscal 2025."*), and validation D23 found the same on CAT. Today's reader
(`lib/research/api/scoped_amgt.py:2538` `read_description`) tries a header scalar first and then that sentence unconditionally;
the cell adds the field and the test. The adapter reads the field by the exact name the pull writes, and the long-text field's
shape is measured on a real block before the reader is built against it.

**`C-HARVESTER-COMPUTE`** -- ⭐ **AMENDED AT v0.5 (addendum s.8). The compute moves OUT of this
project's build and INTO the HARVEST ESTATE**, which Andrew assigned to `4.0.0_SA_CRO~Z` to oversee and
execute (Andrew-direct 2026-09-11 ~17:3xZ) and whose architecture he APPROVED ~18:3xZ.
**ONE box and ONE lambda**, harvest-named, declared in the ONE harvester terraform module -- **not the
four harvesters on a shared box this constraint previously specified, and not
`infra/aws/terraform/amgt-resapp/`.** It keeps AMGT_RESAPP's OWN IAM role and write access to the
article store, and the ASTN_WSJFT box is still explicitly NOT reused.
⛔ **THE BOX IS AN EC2 INSTANCE. IT IS NOT SITE-Z.** Andrew-direct ~18:3xZ, VERBATIM: *"this box is
sitez. it is a local server at Opal, not an aws cloud box. accordingly it is not terraformed nor
included in the aws resource cloud."* A local server cannot sit inside a canonical, self-contained,
terraformed estate, so site-Z is ruled OUT as the box -- while remaining fine for the one-shot
BACKFILL, which is an operator PROCESS and never was a provisioned resource.
⛔ Refresh must still WAKE the stopped box (SSM / inf-jwt-trigger shape) or it silently no-ops.
**EXECUTION ORDER, Andrew-approved:** module consolidation + renames FIRST, THEN the backfill, THEN
the box and lambda. **THE RENAMES ARE DONE** (`4.0.0_SA_CRO~Z`, 2026-09-11, under Andrew's
~19:5xZ full-authority word): bucket migrated with all 53 objects verified and the source deleted;
both tables migrated and the old ones deleted.
BLOCKED: **ITS STATED PREMISE -- "while both stores are empty (0 items, measured)" -- WAS FALSE, AND
THE WORD "measured" WAS THIS SEAT'S.** It rested on DynamoDB `ItemCount`, which is a ~6-HOURLY CACHE,
not a measurement. Measured properly on 2026-09-11, same table, two instruments:
`describe-table ItemCount` -> **0**; `scan --select COUNT` -> **42**. Both come from the live API and
only one is live. The 42 reconcile exactly to this project's own output (rd-6: 32 PRICE + 10 CHATTER).
A DynamoDB rename is a DESTROY/RECREATE, so on this sentence's premise the rename would have SILENTLY
DROPPED 42 live rows belonging to two round-5 cells. Caught by `4.0.0_SA_CRO~Z` distrusting a number
this seat had repeated, and the migration preserved all 42 on full item equality.

⭐ **SUPERSEDED AT v0.7 (s.9f) AS TO THE BOX, by a LATER Andrew word this clause never saw.** Andrew-direct
2026-09-14 (Eastern) at `4.0.0_SA_CRO~W`'s terminal, recorded at
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260914_DOWJONES_HARVEST_W.md` @`187f003998`, VERBATIM:
*"The architecture should be the same self-healing cookie secural run from a stable server and then lambda rest
api pulls, the only difference is that the stable server is this box, and the lambda api calls are also this
box. i think this whole operation needs to be handled local on this device with some kind of local cron job that
cycles through the various platforms for the various securities in a polite manner so no rate limiting."* So the
DIRECTED architecture is LOCAL on site-Z: the session harvesting AND the HTTP/API worker on this box, ONE canonical
library inside `opal-data-harvest` carrying each platform's tokens, API contract and code; the EC2 box and
cloud lambda of the ~18:3xZ ruling are HISTORY and available infrastructure, not a binding production target.
What is NOT yet decided is the RECURRING ACTIVATION: the collection MECHANISM and CADENCE stay RESERVED to Andrew
by name pending validation (his ~04:3xZ remediation word, `ANDREW_DIRECT_20260915_HARVEST_REMEDIATION_LOOP_W.md`
@`cdc3576436`; `org/XXX.md` Step 1b-F @`9db2a36cdc`); the local commissioning runs to date are bounded samples on
the pilot keys with no schedule (`HARVEST_COMMISSIONING_20260915_W.md` @`e07048dc32`). Carried on `4.0.0_SA_CRO~W`'s
read of the v0.7 draft (06:41Z), which named the source this seat had missed.

**`C-STARRED-PER-FIRM`** -- the starred watchlist is SHARED ACROSS THE FIRM (both PMs see the same
starred names), keyed per-firm, not per-user. Andrew-ruled 2026-09-11; reversible to per-user on his
word. ⛔ Starring is a PURE MARKER -- it triggers no refresh and queues no harvester; Refresh is its own
explicit action.

**`C-VENDOR-WORD-HARVESTERS` (TIME-SCOPED)** -- Andrew gave the per-use word for **Seeking Alpha, FT,
Bloomberg and WSJ** for THIS project's harvesters, **effective when the harvester box is stood up and
ready to run -- NOT before**. ⚠ NOT a blanket grant: `C-VENDOR-EGRESS` continues to bind every other
vendor and every other use, and the standing "availability is not authorization" law is unchanged.
⭐ **RE-HOMED AT v0.5, AND THIS IS THE AMENDMENT THAT MATTERS MOST.** Until v0.5 this bound had no cell
of its own -- decomposition s.13d carried it as a TIME-SCOPED BOUND ON `rd-4`, deliberately, so the
subtraction balanced visibly. **Superseding `rd-4` therefore removes this constraint's only carrier.**
It is re-homed HERE, onto the HARVEST ESTATE's acquisition surface, **with all three limits intact:
the four named platforms, THIS project's harvesters only, and not before the box stands.**
⛔ **AND IT IS NOT WIDENED BY THE HARVEST HANDOVER.** Andrew's ~17:3xZ grant of "full egress and
override authority" to `4.0.0_SA_CRO~Z` is authority to REALIZE THE ESTATE; it is **not** a widening of
`C-VENDOR-EGRESS`. Recorded in writing rather than left to assumption, because a narrow time-scoped
grant losing its carrier at the same moment broad-sounding egress language arrives is exactly how a
bound quietly becomes blanket with nobody seeing it happen.
⛔ **A PROXY VENDOR IS A SEPARATE, UNANSWERED QUESTION.** This constraint authorises egress TO the four
platforms. It does **not** authorise a new PROXY VENDOR for platforms that did not use one -- extending
Bright Data Web Unlocker from WSJ to the three SESSION harvesters is a NEW per-use vendor call for
Andrew, never an inference from an EC2 IP proving unworkable against PerimeterX.

---

## 4. SURFACE MANIFEST (step 4 -> step 5) -- one row per ENGINE

| id | outcome | surface | claim | measured-by | verb | depends on | bound |
|---|---|---|---|---|---|---|---|
| S1 | `FWD-1` | THE MODEL BLOCK -- the mechanical one-pager figures for a covered name | absent | F2: ~20 line items x 10 years + ~25 header scalars; 180 points / ~3.4 KB / one call for one security | build | -- | `C-UNIT-MAP-MEASURED`, `C-FISCAL-YEAR-JOIN`, `C-BLOOMBERG-BASIS` |
| S2 | `FWD-2` | THE ON-DEMAND PULL -- a name outside coverage, by ticker | absent | F2: the binding constraint is UNIQUE SECURITIES TOUCHED, not volume | build | S1 | the page states it is fetching now; `C-VENDOR-EGRESS` |
| S3 | `FWD-3` | THE PROVENANCE FACE -- source, basis and vintage beside every figure | absent | F3 (basis stated beside the number, Andrew-ruled) | wire | S1 | `C-BLOOMBERG-BASIS` |
| S4 | `FWD-4` | THE COVERAGE READER -- recent commentary, ranked by recency and frequency | absent | F7 (the landed corpus is an ARCHIVE, not a feed: dates stop at 2026-04, 0 of 200 sampled carry a ticker); F11 (the SERP path works; the obvious link field is an obfuscated redirect) | build | S12 | `C-VENDOR-EGRESS`, `C-RULE-MUST-EXIST` |
| S5 | `FWD-5` | THE PRINT RENDERER -- Adam's artifact | absent | F1 (template and packs are consistent, provenance confirmed by a shared misspelling) | build | S1, S3 | `C-DESIGN-SPEC-FIRST` |
| S6 | `FWD-6` | THE VERSION STORE -- snapshots that accumulate rather than overwrite | **STORE EXISTS; surface absent** | brief O6; `opal-data-harvest` (RENAMED from `opal-data-research` 2026-09-11, 53 objects migrated and verified, source deleted) was created by THIS project's own `AMGT-s-6` (CLOSED deploy-completion @2026-09-10T20:59Z; declared at `infra/aws/terraform/harvest/s3.tf` -- **the former citation `infra/aws/terraform/research/s3.tf:11` is DEAD, that module was retired 2026-09-11**); **versioning `Enabled`, so FWD-6's accumulate-never-overwrite bar is met BY CONFIG, not by convention**; no lifecycle, so accumulation is not silently truncated; read/list access MEASURED. Row `AMGT_RESAPP-Z-S8` | **INTEGRATE -- no create cell** | -- | `C-RAW-BEFORE-DERIVED` |
| S7 | `FWD-7` | THE COVERAGE-FRESHNESS VIEW -- Adam's one place | absent | brief O7 | wire | S6 | -- |
| S8 | `FWD-8` | THE PEER SET -- comparable to THIS company, or absent with a reason | **BROKEN TODAY** | F6: 48 of 54 (88.9%) carry a stale set copied from one workbook; 4 (7.4%) are genuine and hand-chosen | build | S12 | `C-IDENTITY-RESOLVED`, `C-SHARED-DEFECT` |
| S9 | `FWD-9` | THE DRAFTING FACE -- generated prose marked, beside its evidence | absent | brief O9; Andrew's ruling on limb order | wire | S1, S4 | `C-VERBATIM-GATE` |
| S10 | `FWD-10` | THE CHECK FACE -- pass, fail or provisional, per figure | absent | brief III-B | wire | S11 | `C-MARK-NOT-DEGRADE`, `C-CHECK-MUST-REFUSE` |
| S11 | `FWD-10`, `FWD-3` | THE QUALIFICATION RULES -- one per class, each naming its refusal input | absent | brief III-B, six classes | build | -- | `C-RULE-MUST-EXIST`, `C-CHECK-MUST-REFUSE`, `C-SHARED-DEFECT` |
| S12 | `FWD-13` | THE IDENTITY LAYER -- ticker, symbol, IR domain, social account | absent | PART V (three keys + a social layer with no shared identifier); F6 as the measured failure | build | -- | `C-IDENTITY-RESOLVED` |
| S13 | `FWD-11` | THE SOCIAL FEED -- admitted by a stated rule | absent | F12 (1,763 datasets LISTED, none exercised); F13 (0 cashtag-native) | **measure, then build** | S11, S12 | ⛔ `C-LISTING-NOT-CAPABILITY`, `C-VENDOR-EGRESS` |
| S14 | `FWD-12` | THE INPUT LEDGER -- per class: source, last run, outcome, re-run | absent | brief O12 | wire | S6 | `C-STAGE-PERSISTS` |
| S15 | `FWD-14` | THE LIST REGISTER -- allowlist + social map, each owned, each with a rot signal | absent | PART V (both rot; an unowned list lapses silently) | build | S12 | `C-LIST-OWNER` |
| S16 | `FWD-15` | THE LEAD PANEL + ITS RANKINGS -- universe discovery: Trending/Breakout x Price/Chatter, List/Chart, Security overlay, Starred | absent | Andrew's frontend walkthrough; CRO full-stack vision Part C; CONFIRMED 2026-09-11 | build | S4, S8, S12, S13 | `C-SERVER-SIDE-RANKING`, `C-PRICE-RANKING-BOXSIDE`, `C-STARRED-PER-FIRM`, `C-AMGT-ARTICLES-STORE` (superseded by `C-ONE-STORE`, s.9f) |

⭐ **S12 IS THE ROOT AND IT IS NOT IN THE BRIEF'S OWN SURFACE LIST.** Four surfaces depend on it
(S4, S8, S13, S15) and it is the direct remedy for the one defect this project has actually measured
in production. **Cutting S4, S8 or S13 before S12 rebuilds F6 on a new axis.**

⚠ **S13 IS THE ONLY ROW WHOSE VERB IS `measure, then build`**, and that is deliberate: its substrate
is a catalogue nobody has exercised. **Its first cell may honestly deliver a measurement rather than
a feature**, and an acceptance criterion that demands a working feed from an unexercised catalogue
is a criterion a correct build cannot satisfy.

---

## 5. WHAT MUST BE TRUE, AND IS NOT YET

Carried from brief PART V. **These are preconditions, not outcomes -- no `FWD-n` is graded on them.**

- **The desktop/cloud seam is crossed somehow.** The portal runs in AWS; the Bloomberg interface is
  local to one device. **Any design must say how a browser request reaches it.**
- **The Bloomberg session's state is visible to the user.** Sign-out is the most common failure and
  costs a budgeted repair; a page that fails silently against it reads as broken.
- ~~**`opal-data-research` exists** -- measured ABSENT on the live plane.~~ **RESOLVED 2026-09-11
  -- THE BUCKET EXISTS.** Measured on the live plane at `2026-09-11T15:55Z`: `s3api head-bucket`
  returns rc=0, `arn:aws:s3:::opal-data-research`, region `us-east-1`; the negative control
  `opal-data-research-nope-xyz` returns 404, so this distinguishes an existing bucket from a
  resolvable-looking name. Measured by `3.0.0_SA_CVO~Z` at 15:44Z (round-4 row
  `AMGT_RESAPP-Z-S5`) and re-read at 15:55Z by `1.0.0_SA_CTO~Z`.
  ⛔ **THE RE-READ IS A REPETITION, NOT A CORROBORATION, AND AN EARLIER DRAFT OF THIS BULLET CALLED
  IT "a second instrument" -- WITHDRAWN.** Both reads are `s3api head-bucket`: the same method run
  twice, which Rule 22 names as repetition. The one genuinely different instrument on this fact is
  the CVO's `comp-find --corpus aws` (1 hit across 2445 nodes, `S3_BUCKET`, drift `DECLARED`).
  ⚠ And the NEGATIVE control proves less than it appears to: `head-bucket` renders **403 as 404**,
  so a 404 means absent **OR unauthorised**. The POSITIVE read is unaffected and carries this
  bullet on its own -- rc=0 with a real ARN and region proves the bucket EXISTS, whatever the
  control does.
  ⭐ **THE HISTORY QUESTION IS ANSWERED, AND THE ANSWER IS "GENUINELY ABSENT THEN."** An earlier
  draft of this bullet asserted the ABSENT reading "was correct when taken"; that was WITHDRAWN as
  unmeasured, and **the withdrawal was correct ON THE EVIDENCE THEN.** Round-4 row
  `AMGT_RESAPP-Z-S8` since supplied evidence that settles it, so the fact is carried on MEASUREMENT
  rather than on courtesy: **`opal-data-research` was measured ABSENT TWICE and was then CREATED BY
  THIS PROJECT'S OWN CELL.** `comp-find --corpus aws` read 0 of 2382 nodes at 2026-09-10T12:24:50Z,
  and a live `head-bucket` re-measured it absent at **2026-09-10T20:56:33Z as cell `AMGT-s-6`'s own
  AC1, three minutes before that cell created it**. Creation is recorded in a CLOSED
  deploy-completion entry (`org/critical_paths/change_management/
  20260910T2059Z_amgt-resapp-opal-data-research-bucket_deploy_completion.md`) and the resource was
  DECLARED at `infra/aws/terraform/research/s3.tf:11` AT THAT TIME; it is now
  `infra/aws/terraform/harvest/s3.tf` (the research module was retired 2026-09-11 and that path NO
  LONGER EXISTS -- a citation left in the present tense would send a reader to nothing).
  **Brief PART V is SUPERSEDED, never
  falsified** -- and that is now a measured statement rather than a generous one.
  ⭐ **ACCESS IS MEASURED TOO, not just existence** -- the gap an earlier draft of this bullet
  correctly flagged as open. `list-objects-v2` SUCCEEDS and returns this project's own round-1
  output under `derived/model_block/`, so the principal holds read/list rather than mere name
  resolution. Configuration measured with it: **versioning `Enabled`** (re-read independently by
  this seat), **no lifecycle configuration**, **no bucket policy** (access is IAM-only).
  ⚠ What is still NOT claimed: write access was not exercised, and nothing here grants it.
  `C-RAW-BEFORE-DERIVED` is no longer blocked on the bucket's existence.
- **A decision on paywalled sources.** If analysis behind a login is in scope, the vision-
  authenticator pattern is the route; if public pages suffice, neither it nor the credential is
  needed. **Nobody has decided, and whether the login is captcha-gated is unknown.**

---

## 6. WHAT THIS PRD DOES NOT CLAIM

- **No qualification threshold exists anywhere in this document.** Anyone reading a number into s.3
  is reading something that is not there.
- **The field map was measured on ONE security.** F4's unit conventions are the most likely thing to
  differ on a US name, an ADR or a financial.
- **Whether the stale peer set reaches the PRINTED packs is UNVERIFIED.** The document pastes
  spreadsheet output as an image and which image is the comparison was never traced. ⛔ **Nobody
  should conclude packs shipped wrong on the strength of this PRD.**
- **The IR scan was proven on one name, not at scale**, and the ex-US names are the risk.
- **Nothing about the social datasets has been exercised** (`C-LISTING-NOT-CAPABILITY`).
- **No decomposition, no sequencing, no task orders.** That is L5 and it is not this seat's.

---

## 7. PROVENANCE

```
GROUNDED ON:  L1 brief @19ce7d5b4d read IN FULL from the working tree (330 lines, 22,244 bytes)
              L2 endpoint @3bc8f5f2c4 -- the fourteen outcomes, unmodified
              4.0.0_SA_CRO~Z msg 21001 (both additions accepted) and msg 21007 (the macro-scope
                vs project-boundary distinction adopted at s.2)
              Andrew-direct @1f89e24eac -- the macro and its scope
NOT READ:     the task-order register; any sibling project's code or decomposition; the D5
              directive PRD (reading the parent would import outcomes nobody wrote for this project)
UNVERIFIED:   every F-numbered measurement is the CRO's, re-derived by nobody. This PRD carries
              them as CITED, not as CONFIRMED, and a cell relying on one re-measures it first.
```

**Push state:** LOCAL at write time; ancestry rather than a tip hash. `0.0.0_AB_MSTR~Z` pushes.

---

## 8. ADDENDUM v0.5 -- THE HARVEST ESTATE (Andrew-direct 2026-09-11 ~17:3xZ and ~18:3xZ)

**Author** `1.0.0_SA_CTO~Z` (L4). **Trigger:** two Andrew-directs relayed VERBATIM by `4.0.0_SA_CRO~Z`
and recorded @`bb1800ec4d` (the five directives) and @`135aa5b0d0` (the approved draw).

⛔ **THIS ADDENDUM CHANGES THE BRIEF HALF ONLY. The ENDPOINT is untouched** -- `FWD-1`..`FWD-15` are
unchanged and the ratified-text half's hash is unmoved, so `3.0.0_SA_CVO~Z`'s signature stands. The
brief half re-opens and is owed to `4.0.0_SA_CRO~Z`. **No outcome changed; only HOW and BY WHOM two of
them are served.**

### 8a. What Andrew ruled

One box and one lambda under harvest naming, `opal-data-harvest` buckets, all worker terraform in ONE
harvester module, and `4.0.0_SA_CRO~Z` to **oversee and execute** it with full egress and override
authority -- behind his own gate, *"just /draw me your intended architecture and i can approve/revise."*
The draw was APPROVED ~18:3xZ with ONE correction: **the box is an EC2 instance, NOT site-Z**, because
a local server "is not terraformed nor included in the aws resource cloud."
⭐ **v0.7: SUPERSEDED as to the box by Andrew's LATER word of 2026-09-14 (@`187f003998`, quoted at
`C-HARVESTER-COMPUTE`'s v0.7 marker in s.3b; the map in s.9f):** the whole operation is directed LOCAL on this
box with a local cron job; its recurring activation (mechanism, cadence) stays reserved to Andrew pending
validation. The EC2 estate this section drew is history and available infrastructure.

### 8b. What changes in round 5, and what does NOT

**`rd-3` (harvester box + own IAM role) and `rd-4` (four harvesters) are SUPERSEDED** by the harvest
estate. ⛔ **The SUPERSEDE IS THE ISSUER'S ACT, NOT THIS SEAT'S** -- `2.0.0_SA_COO~ZZZ` sets the status,
and it correctly declined to do so before this addendum existed because coverage is graded at L10.
⛔ **AND THE DECOMPOSITION IS NOT EDITED HERE.** `decompositions/**` is lane `TREE_COO` (checked at
`.owned-paths.yaml`, not assumed). **Decomp s.13c's subtraction becomes FALSE the moment rd-3/rd-4 go**
-- it reads "REMAINDER ZERO" over PRD s.3b's six constraints with `C-HARVESTER-COMPUTE -> rd-3 + rd-4`,
and that constraint would then map to no cell in this round. **Repairing s.13c is the COO's act in its
recut, and it must land in the SAME act as the supersede.** A subtraction record that is quietly
falsified is worse than none, because it still prints a clean remainder.

**UNCHANGED and still round 5's:** `rd-1`/`rd-2` (terminal, tables live), `rd-5`/`rd-6` (running --
neither is the box or the lambda), `rd-7`, `rd-8`. Round 5's coverage drops from EIGHT cells to SIX.

### 8c. Bounds that survive the handover -- stated because a handover is where bounds die

- **`C-VENDOR-WORD-HARVESTERS` re-homed** onto the harvest estate's acquisition surface, three limits
  intact (s.3b). It had no carrier but `rd-4`.
- **A PROXY VENDOR IS NOT AUTHORISED.** Extending Bright Data Web Unlocker from WSJ to the three
  SESSION harvesters is a NEW per-use vendor call for Andrew.
- ⛔ **THE PORTAL HOLD STANDS.** `/api/private/research/pull` keeps its path and the route rename is
  DEFERRED; nothing portal promotes, PROD or DEV, until Andrew names it. `rd-8` stays commit-yes,
  promote-no.
- ⭐ **SUPERSEDED 2026-09-11 ~18:5xZ -- ANDREW NAMED THE RETROACTIVE CASE AND RULED RENAME.** Verbatim:
  *"call 2 no it should actuall be a rename there is no data in there anyway, better to have all of
  this stuff grouped by name right from the start."* This clause previously read NO RETROACTIVE RENAME
  absent his word; **his word has arrived.** `opal-data-research` IS renamed into harvest naming.
  ⛔ **BUT HIS PREMISE IS FALSE AND THE ACT IS BIGGER THAN HIS SENTENCE DESCRIBES.** Measured
  `2026-09-11T18:55:29Z` before anything moved: **53 objects, 60 versions** -- `derived/model_block/`
  (BABA x4, BA x4, NVDA x2, SAP_GY x4), `derived/model_block_fye/` (3 tickers), `packs/*/input_ledger.json`.
  S3 has no rename primitive. **This is a DATA MIGRATION OF 53 OBJECTS, executed as copy -> VERIFY
  count and key grammar -> only then delete the source.** Surfaced to him; the ruling stands meanwhile.
  ⛔ **AND THIS PRD'S EARLIER CLAIM IS WITHDRAWN AS OVERSTATED:** it said the rename "would destroy the
  two-snapshot evidence that `FWD-6`'s accumulate bar was followed." **It would not.** That evidence
  lives in the KEY GRAMMAR -- distinct timestamped paths -- which a copy PRESERVES. What is lost is the
  S3 VERSION HISTORY (60 -> 53, the ~7 versions of overwritten keys), and `FWD-6` does not read those.
  **The rename is more expensive than his sentence assumes and much cheaper than this PRD claimed.**
  ⛔ **THE CLAIM THAT ONCE STOOD HERE -- that the two DynamoDB tables were "genuinely empty (0 items
  measured)" -- IS WITHDRAWN AS FALSE.** It read `ItemCount`, a ~6-hourly CACHE, and called it a
  measurement. `opal-amgt-articles` was genuinely empty; `opal-amgt-security-metrics` held **42 live
  rows** (`scan --select COUNT`), which a destroy/recreate rename would have dropped. Both were
  MIGRATED rather than recreated, on full item equality, and both old tables are deleted.
- **Terraform commits ride an audited `GIT_COMMIT_AUTHOR_OVERRIDE`** naming Andrew's grant, one per
  lane. **No `.owned-paths.yaml` edit** -- the AE-only lane rule is overridden per-commit with an audit
  line, not amended.

### 8d. What this addendum does NOT claim

It does not grade any `FWD` outcome, does not authorise an apply, and does not settle whether the
harvest consolidation absorbs the orphaned S9/S10 module reconcile -- `4.0.0_SA_CRO~Z` has since
confirmed it does, and verified the module is genuinely broken first (`terraform validate` -> three
duplicate-block errors), which is that seat's to carry rather than this PRD's.

---

## 9. ADDENDUM v0.6 / v0.7 -- THE PAGE AS ANDREW DEFINED IT ON 2026-09-15 (the round-10 L10 addendum, and the L4-R answer)

**Author:** `1.0.0_SA_CTO~W` (the L4 owner on Andrew's word @`ce7371d0b3`). **Trigger:** the round-10 slug
`surprise-channel/remediations/REMEDIATION_v10.md` @`e28f0b546c` and this seat's
`ledger/ROUND_ANALYSIS.round10.md` @`8d5fe78265`. **What v0.6 changed:** the ENDPOINT gained FWD-16..FWD-19; a
CONTRACTS section was added (eight contracts, not the "seven" v0.6 wrote here); this section. **What v0.7
changes (s.9g has the itemised list):** both L4-R halves of v0.6 were REFUSED (`3.0.0_SA_CVO~W` @`01e640925c`;
`4.0.0_SA_CRO~W` @`d8bee9fd68`) and v0.7 answers each named correction, adds TWO contracts (`C-ONE-IDENTITY`,
`C-RANKING-GENERATION`; ten contracts now) and sharpens two (`C-ONE-STORE`, `C-FILINGS-ANALYZER`) on the five connection briefs
`4.0.0_SA_CRO~W` sent under Andrew's sixty-minute review word (@`76ab87a06e`). **What neither bump changes:**
the fifteen v0.5 outcomes and their bars; the surface manifest of s.4 as a set of engines (round 11's
decomposition extends the rectangle; this PRD does not pre-cut it). ⚠ **s.2-s.8 DO change, by supersession,
and v0.6 said otherwise:** the clauses v0.6's contracts overtake are named one by one in s.9f with the
replacing contract and the transition condition, and each carries an in-place marker at its own line.

### 9a. Provenance -- exact paths and pins

Paths are under `org/tier1_exec/` unless written from the tree root. A pin is the last commit touching the file
at this bump (`git log -1 --format=%h -- <path>`), read 2026-09-15 ~06:3xZ.

| record (path @ pin) | what it carries |
|---|---|
| `1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_232xZ_W_LANES_FOR_AMGT_RESAPP_CANONICAL_FLOW_AND_COMP_STATE_SPAWN_VIA_MSTRZ.md` @`dc36f73ac0` | the `~W` lanes take the project; the L2/L4 owner from here |
| `1.0.0_SA_CTO/deliverables/AMGT_RESAPP_W_LANES_HANDOVER_20260914.md` @`9dfee40ce0` | the hand-over: seating, scope, round-10 substance, residue |
| `1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_035xZ_W_FABRIC_IS_AMGT_RESAPP_ONLY_Z_FABRIC_IS_POSN_ASTTAX.md` @`9dfee40ce0` | `~W` = AMGT_RESAPP only; `~Z` = POSN_ASTTAX |
| `2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/ANDREW_DIRECT_20260915_0504Z_EXECUTIVE_MANAGERS_LUSHA_AND_THE_HARVEST_POOL.md` @`7cf62a165f` | executive managers; Lusha; the pool as the system of record |
| `1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_051xZ_SECURITY_ANALYSIS_HEADER_PANEL_FOUR_TABS_FILINGS_ANALYZER.md` @`a5c6a066de` | six words: the header, four tabs, a filings analyzer; Posture; the union universe; the symmetric comparable; Adam's packs and the Scanner; the whole C-suite and tenure |
| `1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_052xZ_EGRESS_GRANTED_TO_CTO_W_FOR_THE_SESSION.md` @`5007337353` | egress for the session, seat-scoped; `comp-secrets` as the instrument |
| `2.0.0_SA_COO/deliverables/AMGT_RESAPP_W/ANDREW_DIRECT_20260915_0542Z_WHOLE_SITEZ_FABRIC_FREE_EGRESS_THIS_SESSION.md` @`dfa63b6d92` | the egress word widened to the whole site-Z fabric for the session |
| `1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_055xZ_TRANSCRIPT_SECURITY_ANALYSIS_PANELS_DRILL_DOWN.md` @`2285a23678` (the record @`fbd5d91431`; the correction of its line-80 pointer @`2285a23678`) and `1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260915_055xZ_TRANSCRIPT_New_Recording_34_9677.json` @`fbd5d91431` | the voice memo, verbatim with timestamps: parts one to five, the ranker, "the RAG is just the four tabs plus comparing with the opal position" |
| `1.0.0_SA_CTO/deliverables/AMGT_RESAPP_ENDPOINT_ADDENDUM_20260915.md` @`2285a23678` | the pinned ratified carrier for FWD-16..FWD-19: each card beside the Andrew-direct sentence it was cut from (s.9g) |
| `1.0.0_SA_CTO/deliverables/AMGT_RESAPP_PAGE_V2_DESIGN_20260915_W.md` (created @`2285a23678`; its price-partition label corrected to `TRENDING_PRICE#<d>` / `BREAKOUT_PRICE#<d>` in the v0.7 commit on `4.0.0_SA_CRO~W`'s read) | the v2 page drawn from the contracts; the as-built page of the round-10 drain as its appendix |
| `1.0.0_SA_CTO/deliverables/AMGT_RESAPP_SUBSTRATE_MEASUREMENTS_20260915_W/SUBSTRATE_CARDS.md` @`5007337353`, with `BA_10K_2026-01-30_measurement.json`, `boeing_csuite_prospecting.json`, `measure_filings_analyzer.py`, `measure_lusha_csuite.py` beside it at the same pin | card 1 the filings analyzer; card 2 the Lusha C-suite; card 3 Adam's workbook, the Scanner registry and presets |
| `4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260914_DOWJONES_HARVEST_W.md` @`187f003998` | Andrew's 2026-09-14 harvest words at `4.0.0_SA_CRO~W`'s terminal: the Dow Jones credential in Secrets Manager; ONE canonical library in `opal-data-harvest`; "the stable server is this box, and the lambda api calls are also this box ... local on this device with some kind of local cron job"; JSON first, HTTP extraction a last resort |
| `org/XXX.md` Step 1b-F @`9db2a36cdc`; `4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260915_HARVEST_REMEDIATION_LOOP_W.md` @`cdc3576436`; `4.0.0_SA_CRO/deliverables/HARVEST_COMMISSIONING_20260915_W.md` @`e07048dc32` | the harvest remediation loop Andrew directed at `4.0.0_SA_CRO~W`; mechanism and cadence reserved to him by name; the local commissioning evidence |
| `4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260915_RESAPP_60M_PROGRESS_LOOP_W.md` @`76ab87a06e` | Andrew's sixty-minute progress and gap review word to `4.0.0_SA_CRO~W`: "Look for gaps, if you find any, write a brief on connecting them and send that brief to CTO~W" |
| `4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_POOL_READERS_20260915_W.md` @`0e7de170e3` | the pool's `published` field, the join key, dedupe, distinguishable failure states, the package seam |
| `4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_IDENTITY_20260915_W.md` @`b90bfdd20d` | three key conventions on one name; the crosswalk |
| `4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_SOCIAL_SERP_20260915_W.md` @`36a08d3d1a` | S13's supported input methods (profile-array and keyword discovery, asynchronous jobs), typed social items, two separate judgments |
| `4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_FILING_EVIDENCE_20260915_W.md` @`a65fe406c2` | citation resolution before drafting; the drafting gate's three probes |
| `4.0.0_SA_CRO/deliverables/RESAPP_CONNECTION_BRIEF_RANKING_RETRIES_20260915_W.md` @`5ae6dd04b5` | a ranking rerun retains stale winners (three rows, two rank-1s, locally reproduced); complete-generation semantics |
| `3.0.0_SA_CVO/deliverables/AMGT_RESAPP_V06_RATIFIED_TEXT_REVIEW_20260915_W.md` @`01e640925c` | the ratified-text refusal of v0.6: R1, R2, R3, the count, the counterpart, the missing file |
| `4.0.0_SA_CRO/deliverables/AMGT_RESAPP_v06_BRIEF_REVIEW_20260915_W.md` @`d8bee9fd68` | the brief refusal of v0.6: R1 the supersession map, R2 exact pins and the coverage map |
| `org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round10.md` @`8d5fe78265`; `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/remediations/REMEDIATION_v10.md` @`e28f0b546c` | the L10 read and the slug it answers |

### 9a-2. Coverage map -- each source requirement, the contract that carries it, the engine surface it lands on

| source (row of 9a) | substantive requirement | contract | engine surface (existing or proposed) |
|---|---|---|---|
| ~05:1xZ, first word | the header = the ranking cross + the company feed (publisher + social) + a one-line description | `C-PAGE-LAYOUT`, `C-ONE-STORE` | S16 Lead Panel (built; mounted at ri-4); the header feed = S4's reader repointed at the pool; the description = a model-block header scalar |
| ~05:1xZ first word (tab 2); ~05:04Z; the sixth word; memo part two | Exec Management: the whole C-suite, Lusha, a targeted web search, tenure against the pool | `C-EXEC-MANAGEMENT` | a new lane: the filing's officer section (authority) -> Lusha `contacts_prospecting` -> an IR-domain search for the CEO; pool-average tenure over the union universe |
| ~05:1xZ first word (tab 3); the fifth word; memo part three | Peers = comparable multiples in Adam's `CSC` shape; the ranker sector -> size -> country -> subsector; the Scanner's ranking material | `C-SIMILARITY-RANKER` | `lib/research/peers/engine.py` (rungs 1-2 exist; no candidate universe loaded) + the Scanner `UniverseDataRow` + `factor_metadata_registry.json` |
| ~05:1xZ first word (tab 4); memo part four | Model = the plain financial model from Bloomberg, the same every time | `C-PAGE-LAYOUT` (Model restored) | the model block AMGT-s-1 already produces, rendered in Adam's `Model` sheet shape |
| ~05:1xZ first word (tab 4); memo part one; Yang Liu's Teams pointer | a filings analyzer; the one "big thing" chart chosen from the filings by the thesis | `C-FILINGS-ANALYZER` | a new scheduled cell over the union universe: the Claude API with document citations (card 1); the index-to-passage map; the drafting reader (brief @`a65fe406c2`) |
| ~05:1xZ second, third and fourth words; memo part five | Posture; the union universe; the symmetric comparable; "the RAG is just the four tabs plus comparing with the opal position" | `C-POSTURE`, `C-UNION-UNIVERSE`, `C-ETF-PLANE-READ` | a new cell, last in order: membership from the ETF snapshots (read-only), the comparable by the ranker, the judgment over two packs, `posture/v1` |
| ~05:04Z | the pool is the system of record every frontend runs off | `C-ONE-STORE` | the chatter axis + the coverage reader repointed at `publication-links/v1` / `publications/v1` through one adapter |
| brief @`b90bfdd20d`; `Z-S95` | one canonical identity; three conventions crosswalked | `C-ONE-IDENTITY` | `crosswalk/v1`; the route boundary in `lib/research/api/scoped_amgt.py` |
| brief @`36a08d3d1a`; S13 | a supported social input method before any cashtag claim | `C-LISTING-NOT-CAPABILITY`, `C-VENDOR-EGRESS` (standing) | S13 "measure, then build": one security, one declared method, a cap, a window |
| brief @`5ae6dd04b5`; `Z-S72` | a ranking rerun publishes a complete generation; zero winners / changed winner / failure distinguishable; run identity in the exact-input exercise | `C-RANKING-GENERATION` | `lib/research/metrics/chatter_axis.py` writer + `scoped_amgt.py` date-partition reader (the chatter recut) |

**Measurement limits carried into round 11, each with the check the cut runs before building on it:**

| limit (card / brief) | what it means | required check |
|---|---|---|
| ONE company's filing (Boeing 10-K, an Item 1A + Item 7 excerpt), a public filing standing in for the Bloomberg pull (card 1) | nothing is known about a second filer, a 10-Q, a foreign filer or a whole document | run the analyzer on at least three filings across two filers including one non-US name; print items / cited / uncited per filing; measure one Bloomberg-pulled filing before the public stand-in is retired (SUPERSEDED at v0.11 by `C-FILINGS-ANALYZER`: Bloomberg carries no filing text, so this condition is retired) |
| 5 of 76 outputs uncited (card 1); the saved parsed object shows `citations_total=0` because citations arrived INLINE and no passage map was persisted | uncited rows exist, and the measurement cannot locate the passages it cites | hold uncited rows; persist the index-to-passage map; a resolvability check over every cited id (brief @`a65fe406c2`, first acceptance line) |
| the Lusha `c-suite` filter is LOOSE, 50 of 50 rows returned, NO tenure field (card 2) | Lusha can be neither the roster's authority nor the tenure source | the filing's officer section is the authority; Lusha enriches CONFIRMED officers only; tenure from the filing field; print confirmed / unconfirmed per company |
| the peers engine has NO candidate universe loaded (9b) | the ranker's rungs exist but rank over nothing | load the Scanner universe data UNION the model-block headers; print the denominator; run the four-postulate MECE check (the database MINUS the excluded = the ranked) |
| the coverage list: 32 of 89 tickers MEASURED, 57 UNRESOLVED (2026-09-10); the ranker input 34 eligible (06:02Z audit) | the union universe is not yet one identity space | `C-ONE-IDENTITY`'s 89-name disposition table before the union is computed |
| the ETF plane's producer contract is unpinned (`C-ETF-PLANE-READ`) | a layout change there would break Posture silently | every consumer carries the snapshot date + the schema version; a schema-shape assertion at read time that fails loudly |
| social: 0 cashtag-native datasets; profile-array and keyword discovery are documented, none exercised (brief @`36a08d3d1a`) | no social item can be admitted yet | S13's bounded first measurement (one security, one method, a cap, a window) before any header social item |
| the Bloomberg licence terms for filings and financials: an OPEN question (card 1) | the production input may be constrained | Andrew's word before a scheduled batch reads a Bloomberg-pulled filing |
| the ranking writer upserts and never clears (brief @`5ae6dd04b5`; a local probe, no live write; the live partitions UNMEASURED for mixed generations) | any same-day rerun since ri-2 may have left stale winners in a served partition | before round 11 serves a ranking: count rows and distinct ranks per axis/date partition on the live table, print the denominator; the three-run acceptance (2, 2, 0 visible winners) on the recut writer |

### 9b. Compiler and substrate evidence (what changed this PRD)

| instrument | result | changed the PRD? |
|---|---|---|
| Claude API over Boeing's 10-K, citations + schema (card 1) | 76 items, 71 cited inline, USD 1.06, 114.5 s; citations INLINE with JSON, no citation blocks | yes: C-FILINGS-ANALYZER's two-pass-or-parser clause |
| Lusha prospecting, boeing.com, c-suite (card 2) | 50 of 50 rows, 9 fields, no tenure field, loose filter | yes: C-EXEC-MANAGEMENT puts the filing first, Lusha second |
| Adam's Boeing workbook (card 3) | `Model` and `CSC` sheets measured; stale telecom set present | yes: C-PAGE-LAYOUT (Model restored), C-SIMILARITY-RANKER's rendered shape |
| Security Scanner registry + presets (card 3) | 289 factors / 18 categories; DIVZ 13, PFOE 16 | yes: the ranker's database and Posture's fit input |
| `lib/research/peers/engine.py` at HEAD | sector + 0.2x-5x band, basis analyst/derived/absent, no candidate universe loaded | yes: the ranker's first two rungs are the existing engine |
| Grep census of `opal-harvest-articles` writers / `publications/v1` readers (row `Z-S96`) | 0 writers of the table; 0 readers of the pool keys outside the harvester | yes: C-ONE-STORE |
| `s3://opal-data-etfs` layout on the live plane | config (4 tickers), gold/book, gold/holding, 95 daily snapshots | yes: C-ETF-PLANE-READ |
| receiving-check on the round-10 analysis | UNCHECKED (no checker for a round analysis) | stated, not hidden |

### 9c. What this bump does NOT authorise

No cell, no vendor call by any cell (the session egress word is Andrew's and is recorded where it was
given), no read of the ETF plane by any AMGT cell before the COO's cut names it, no trade-pipeline
consumer of Posture, no promote (PORTAL FROZEN: COMMIT YES / PROMOTE NO), no push, no change to the
harvest collection mechanism or cadence (reserved to Andrew by name @9db2a36cdc), and no grade of any
outcome. FWD-16..FWD-19 are UNREALIZED at this bump, as every outcome has been at every bump.

### 9d. The round-11 shape the L4 owner RECOMMENDS (the COO cuts)

In dependency order: `C-ONE-IDENTITY`'s crosswalk and the route-boundary resolution (which subsumes `Z-S95`'s
ranked-click recut); the other two AC6 limbs as recuts of existing seams (`C-S196` drafting paired with
evidence -- now through the citation-resolution adapter of brief @`a65fe406c2`; `Z-S72` the exact-input
exercise); `C-ONE-STORE` (the two readers repointed at the pool through one adapter, `published` mapped at
the boundary, the package seam exercised in an isolated runtime -- brief @`0e7de170e3`; the chatter writer under
`C-RANKING-GENERATION` with the three-run acceptance -- brief @`5ae6dd04b5`); the filings analyzer
as one scheduled cell with its passage map; the ranker over the Scanner universe data and the Peers tab in
the `CSC` shape; the exec-management lane; the header (feed + description) and the Model tab; S13's bounded
first social measurement (brief @`36a08d3d1a`: one security, one documented method, a cap and a window; the
cadence stays Andrew's); Posture last, since it consumes everything above for two names. The issuer criteria
the slug names (`W17-S4`, `W17-S5`) are amended at the cut and are not cells.

### 9e. L4-R on this bump

v0.6's two halves were REFUSED at their stamps (ratified-text `ebe1dab5a5`; brief `7c0a757ab5`), each with a
pinned review. v0.7 re-delivers BOTH halves at new bytes: the ENDPOINT (R1, R2, the carriers line) and CONTRACTS
(the count, `C-ONE-STORE`'s field, `C-ETF-PLANE-READ`'s counterpart note, `C-ONE-IDENTITY`, `C-RANKING-GENERATION`,
`C-FILINGS-ANALYZER`'s v0.7 clause) re-open the ratified-text half for `3.0.0_SA_CVO~W`; the s.3b / s.4 / s.8a markers and this s.9
re-open the brief half for `4.0.0_SA_CRO~W` (or a live COO not holding the round in its stead); the preamble
note belongs to neither half. `python .tools/prd-signoff.py status AMGT_RESAPP` is the one read of what is
owed; `to-pipeline-gate.py` LIMB 6 refuses a newly-added round-11 order until both halves are SIGNED at these
bytes.

### 9f. SUPERSESSION MAP -- the v0.5 clauses v0.6's contracts overtake (the brief review's R1)

| clause at v0.5 (its lines at v0.6 @`2f3b65d8b8`) | superseded / qualified by | transition condition | what stands |
|---|---|---|---|
| s.3b "three tabs (Thesis / Peers / Coverage) ... the Model tab CUT with its figures rehomed" (698-701) | SUPERSEDED by `C-PAGE-LAYOUT`: one header, five tabs, Model restored, Coverage's content = the header feed | the round-11 SURFACE cell lands the five-tab shell; until then the served page is the three-tab as-built (design file, appendix) | `C-DESIGN-SPEC-FIRST` lifted; `.tsx` authorized; `FWD-15` |
| s.3b `C-AMGT-ARTICLES-STORE` -- article content in DynamoDB `opal-harvest-articles` (703-709) | SUPERSEDED by `C-ONE-STORE`: the pool is the store | the table stays readable until BOTH readers are repointed at the pool and exercised; then it is retired as a source and nothing writes it | the bucket and table renames of 2026-09-11; S12's per-platform identifier rule (sharpened by `C-ONE-IDENTITY`) |
| s.4 row S16's constraint list naming `C-AMGT-ARTICLES-STORE` (795) | the same supersession, marked in the row | as above | every other constraint on the row |
| s.3b `C-HARVESTER-COMPUTE` -- the EC2 box + lambda in the harvest estate, "IT IS NOT SITE-Z" (724-738), and s.8a (903-906) | SUPERSEDED as to the box by Andrew's LATER word of 2026-09-14 (@`187f003998`): "the stable server is this box, and the lambda api calls are also this box ... handled local on this device with some kind of local cron job"; the session harvesting and the HTTP/API worker run on site-Z from one canonical library in `opal-data-harvest` | the RECURRING ACTIVATION (mechanism, cadence) is Andrew's decision pending validation (@`cdc3576436`, @`9db2a36cdc`); until he gives it, only bounded commissioning runs on the pilot keys (@`e07048dc32`) | the harvest naming; the pool; `4.0.0_SA_CRO~Z`'s renames of 2026-09-11; JSON-first collection with HTTP extraction as a recorded last resort (same record) |
| s.3b `C-SERVER-SIDE-RANKING` -- the chatter axis as "the committed chatter gate" over the articles table (711-718) | SHARPENED by `C-ONE-STORE` (the axis reads the pool), `C-ONE-IDENTITY` (rows carry the canonical key) and `C-RANKING-GENERATION` (a rerun replaces the whole generation; the upsert-and-never-clear writer is the measured defect) | the producer's repoint is a round-11 cell (ri-2 moved it to the harvest TABLES; the pool is the next hop) | the metrics table, the daily partitions, TOP_N=10, the 30-day window |
| s.6 `C-IDENTITY-RESOLVED` -- four keys (535-539) | SHARPENED by `C-ONE-IDENTITY` (a fifth and a sixth key measured: the local association keys) | the crosswalk lands | the display rule ("the page SAYS SO") |

Nothing else in s.2-s.8 is touched by v0.6 or v0.7. A reader at any of the lines above finds the marker in place.

### 9g. What changed v0.6 -> v0.7, itemised (so each reviewer can diff by intent)

Ratified-text half: (1) the version-history parenthetical after the BAR DISTRIBUTION line is removed from the
ENDPOINT and lives here instead: *v0.6 added FWD-16..FWD-19, every one `EXERCISED`; the fifteen v0.5 ids and
their bars are byte-for-byte unchanged -- an addendum never lowers a bar*; (2) "Fourteen outcomes cannot be
closed by any build" -> "Eighteen"; (3) the ENDPOINT preamble names the carriers -- FWD-1..14 @`3bc8f5f2c4`,
FWD-15 s.3b, FWD-16..19 `AMGT_RESAPP_ENDPOINT_ADDENDUM_20260915.md` @`2285a23678`, whose four cards were
extracted and compared byte-for-byte against the ENDPOINT's before that commit (703 / 899 / 921 / 971 chars,
identical); (4) `C-ONE-STORE`: `published_at` -> `published`, the join key, dedupe, distinguishable failure
states, the package seam; (5) `C-ETF-PLANE-READ`: the producer counterpart is NOT established, the read is
one-sided, the schema version is carried; (6) NEW `C-ONE-IDENTITY` and NEW `C-RANKING-GENERATION`; (7) `C-FILINGS-ANALYZER`: the v0.7
citation-resolution clause. Preamble (neither half): (8) the stale-count note gains the v0.7 bullet. Brief
half: (9) in-place markers at s.3b (three clauses -- the `C-HARVESTER-COMPUTE` one carrying Andrew's LATER local-box
word @`187f003998`, which this seat had missed and `4.0.0_SA_CRO~W` named on the draft at 06:41Z), s.4 row S16, s.8a; (10) s.9's opening corrected ("seven" ->
eight at v0.6, ten at v0.7; s.2-s.8 DO change by supersession); (11) 9a rewritten with exact paths and pins;
9a-2 added (the coverage map, the measurement limits, the required checks); (12) 9d gains the five briefs in
dependency order; (13) 9e, 9f, 9g. Outside the PRD, at @`2285a23678`: the carrier, the design file, and the
correction on the transcript record whose line 80 named a file that did not exist.

---

## 10. ADDENDUM v0.11 -- INSTANTIATING A NEW SECURITY: THE STAGES (Andrew-direct 2026-09-18 ~16:3xZ)

**The frame, verbatim:** *"we will be adding things over time and the more important thing than establishing a pipeline
itself is the process behind full 'security analysis' backend instantiation for a new security."* **So the product is the
PROCESS that stands up every stage for a security that is not covered today**, and each panel's constraints above are the
rules of one or more of these stages.

**Every stage takes the BATTERY'S SHAPE:** ordered attempts; ONE acceptance test per attempt; an explicit terminal state --
SERVED, or UNRESOLVED with its reason -- never a silent skip and never an empty success; and the route that won recorded on
the object. **A stage's population is the crosswalk's MEASURED records (`crosswalk/v1/<date>.json`), never a store listing,
a hand list or a worker's folder** (`C-PRODUCTION-HOME`).

| stage | what must exist for the security | what triggers it for a NEW security -- today, measured (validation @b527b93214) |
|---|---|---|
| identity | a MEASURED crosswalk record in the POOL | **none** -- the entry point that is missing. `C-INSTANTIATION-ENTRY` below |
| universe row + filing identity | a `universe/v1` row with its filing identity | none (manual; newest vintage 16 Sep) |
| model block | a Bloomberg model block, every unit measured | none (a hard-coded pilot list) |
| filings | a source object from the battery (`C-FILINGS-ANALYZER`) | only battery step 1 exists in code, and it reads a stale subset |
| translation | translated OUTPUT over the original passages | none -- not built |
| analysis and drafting | an analysis and a drafted document, every sentence on a verbatim span | the disabled batch; no run until validated |
| management | a roster (`C-EXEC-MANAGEMENT`), enriched | the disabled weekly task |
| peers | a peer set and comparison table (`C-PEER-SET-SA`) | none |
| posture | a posture object (`C-POSTURE`) | none; reads model blocks from a repo folder, not the pool |
| scores | the three scores, each SERVED or ABSENT with its reason | none; reads the pool crosswalk directly |
| description | a drafted section or the Bloomberg description field | read time |
| chatter and news | article links for the name | **the chatter Lambda -- the ONLY scheduled stage**; its source covers 3 names |
| price | a daily price pull (Lead Panel card A) | none (manual) |
| movement lists | computed from chatter and price | automatic once both inputs exist |

**`C-INSTANTIATION-ENTRY` (new, v0.11).** ONE "add a security" step lands a new security's identity in the POOL crosswalk --
name, exchange, LEI, SEC id and CIK, from ONE Bloomberg call with the yellow key appended -- and every downstream stage runs
from that record in dependency order. **Every reader behind the page keys on the pool crosswalk, so a security produced end
to end elsewhere renders nothing until this step has run** (measured on CAT, CSL and Keyence). A security whose identity
cannot be resolved is UNRESOLVED with its reason, and no downstream stage runs for it.

**`C-PRODUCTION-HOME` (new, v0.11).** A production code path never reads or writes a WORKER'S deliverables folder -- that
folder is the proof artifact of one task order and covers only the names that worker handled. **Configuration** (for
example the unit map) lives under version control beside the producer that reads it; **cached data** (for example the SEC
ticker table and the peer candidate universe) lives in the pool at an address built by `lib/opal_naming.py` (Rule 30). **A
dry run writes nothing, anywhere.** Measured instances this clause retires: the unit map
(`integrations/bloomberg/research/model_block_pull.py:286-288`, worker `~1`), the SEC ticker cache
(`lib/research/identity/build_universe.py:503-507`, worker `~19`, whose miss is reported as absence from the full table),
and the peer candidate universe (`lib/research/peers/universe.py`, worker `~21`, rewritten even under `--dry-run`).

**`C-VALIDATION-NAMES` (new, v0.11).** Every round-14 cell is proven on the three validation names -- Caterpillar (US,
10-K), CSL (English, company site only), Keyence (Japanese) -- or on a dry run. A run on those three names IS the
end-to-end validation Andrew set as the bar; **no cell is a fleet run or a re-run of the covered population** before it
passes (Andrew-direct ~16:3xZ, *"I dont care about rerunning until the process is completely validated end to end"*).
**Vendor calls inside the validation (v0.12, Andrew-direct ~19:4xZ):** Lusha, *"Yes full egress"* -- no credit ceiling
within the validation, read as scoped to it and not as a standing grant across the covered population; Seeking Alpha on the
two paths `C-SA-VENDOR-WORD` names as lifted.

**What this section does NOT change:** any stage's own contract above; the Posture stage, whose brief is not yet
integrated; the chatter schedule; any cadence, which stays Andrew's.

**Evidence behind the v0.11 CONTRACTS -- moved here at v0.13 so the ratified text carries rules and provenance only** (the
ratified-text reviewer's criterion (d): a defect said to exist "today" inside ratified text becomes false the moment it is
fixed, and a cited line ages separately from the text quoting it). Each item is a measurement as of 2026-09-18 and a pointer
for the round-14 cell, not a rule.
- `C-FILINGS-ANALYZER`: Bloomberg returns no filing text -- docsvc and news refuse, BQL refuses on entitlement (Thesis brief
  s.3). Bloomberg's web address names a subsidiary or branch site for 3 of 22 names measured. Subsidiary reports that fail
  the entity test: Roche Holdings Inc, RWE Finance Europe BV, Zurich Life. D1: `lib/research/identity/build_universe.py:503-508`
  reads a 33-ticker cache in a worker folder and reports a miss as absence from the 10,422-row table, so it misses
  Caterpillar; `:518-520` reads the submissions from the same cache; the guard at `:510` fires only for non-US listings. D9: an
  unknown document family must fail (c). The stale analyses all claim the current analyzer version.
- `C-FILINGS-ANALYZER` supersedes the v0.7 premise that the analyzer reads "the filing Bloomberg pulls", and retires the
  section-9 condition *"measure one Bloomberg-pulled filing before the public stand-in is retired"* (Bloomberg carries no
  filing text, so it can never be met). v0.7's resolve-every-claim rule was measured by the CRO at brief @`a65fe406c2`.
- `C-FILINGS-TRANSLATION`: all three preconditions are absent; `lib/research/filings/passages.py:67-79` keeps 6.8% of Japanese
  characters. Keyence (the Yuho, Japanese): 70 of 71 findings carried a verbatim run of 12+ characters inside their one cited
  passage; the neighbour-passage and one-character-mutation controls refused 70/70 and 68/68; 0 of 71 translations re-locate
  in the original. Keyence's English Annual Report is not the Yuho.
- `C-EXEC-MANAGEMENT`: the SERP primitive breaks silently and returns a list (`data/find/dualbiz/scripts/serp.py:264-272`),
  and the caller records 0 urls as NOTHING_FOUND (`lib/research/management/enrich.py:434-439`); the pool keeps only one
  `as_of` (`enrich.py:582-594`).
- `C-PEERS-V-FLOORS`: the floors sit at `lib/research/scores/peers_v.py:62-70`, the measure's `FIELDS` at `:74-82`; SA peer
  tickers were measured to resolve as `<TICKER> US Equity` with no mapping step. The L4 reading in that clause is
  `1.0.0_SA_CTO~Z`'s.

## 11. ADDENDUM v0.14 / v0.15 -- THE HARVEST STORAGE FORMAT: evidence and open items (Andrew-direct 2026-09-21 ~17:2xZ)

The coordinated backfill is held until the harvest storage format is settled. The six format contracts --
`C-HARVEST-HOME`, `C-BRONZE-AS-RECEIVED`, `C-SILVER-PARQUET`, `C-DEDUPE-BY-KEY`, `C-SLASH-SAFE-KEY`, `C-FORMAT-SEQUENCE` --
sit in the CONTRACTS section, where the ratified-text reviewer reads them. This section holds only their evidence and
what they leave open.

**Specification.** `org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md`
@`1b43fd2933` (re-pinned at v0.22: the SA article hash is `sha256("sa:"+id)`; the plan as corrected: bronze takes three forms, never-kept bronze is filled by a first fetch, and its move order no longer dual-writes). It
gives each channel's fetch key, record key, readers and freshness. Where it and the contracts disagree, the contracts
bind.

**Builder output the contracts cite (measured in the plan, one per bronze form, plus silver):**
- (a) entity: `s3://opal-data-harvest/bloomberg/harvest/bronze/refdata/security_key=CSL_AU_Equity/20260921T162530Z.json`
- (b) document: `s3://opal-data-harvest/sec/harvest/bronze/filing/cik=0000012927/000162828026004357/ba-20251231.htm`
- (c) request: `s3://opal-data-harvest/sec/harvest/bronze/company_tickers/date=2026-09-21/sec_ticker_cik_cache.json`
- silver: `s3://opal-data-harvest/bloomberg/harvest/silver/model_block/date=2026-09-21/part-20260921T162530Z.parquet`
When the plan was measured, each printed `opal-data-harvest` only under the simulated tenancy (plan s.3.2; 59 of 60
addresses, controls unmoved). Since v0.18 the live builder prints the same (below).

**Landed on SITEZ at v0.17 (measured at HEAD `39731fbda7`):** `tiers.json` carries the GENERAL tenancy (every tier
home:scope), and `systems.json` carries the five vendor rows (`barrons`, `wsj`, `ft`, `filings-xbrl`,
`issuer-site`). Both arrived through the CLOUD merge. The builder still prints `opal-data-assets` for bronze and silver
(and `opal-data-portal-v2` for platinum), for one reason: `scopes.json` holds TWO `harvest` rows, and `lookup()` takes
the PRODUCT one (row Z-S203). With that row alone removed, on a scratch registry, every tier prints
`opal-data-harvest`, validate returns 0 refusals, and the controls for other pipelines are unmoved (`1.0.0_SA_CTO~Z`,
and `4.0.0_SA_CRO~Z` msg 24080). S3 census 21:19Z (`2.0.0_SA_COO~Z` msg 24087): 1,461 objects in `opal-data-harvest`
and 0 AMGT objects in the vetoed buckets, so the migration renames keys inside one bucket.

**Closed at v0.17:** Lusha's bronze and contact fields, now `C-LUSHA-EXCEPTION`, on Andrew's word.

**Closed at v0.18:**
- The duplicate `harvest` scope row was deleted by the registry lane (`10bace8916`). `validate()` now refuses a
  repeated scope key (measured with a planted duplicate: 1 refusal; live: 0). The builder prints `opal-data-harvest`
  for every AMGT tier (row Z-S205). `C-HARVEST-HOME` is MET.
- The moves M1 (`raw/bloomberg/`), M2 (`filings/v1/*.source.json`) and M3 (`raw/seekingalpha/`) are done. Each retired
  its old path on S3, IAM and code in one window, with the old objects kept as inert data (round-22 adjudication
  `d8a57a5b82`).
- The harvest writers H0-H6 are built and idle. Their new-grammar prefixes reach the served adapter as build-time
  generated constants from `address()`.

**Open, and not decided by this PRD:**
- The R20 register entry for `C-LUSHA-EXCEPTION`, by the registry lane.
- The backfill runs, at validation scope first, on Andrew's per-use vendor words.
- The gold chain: the `model_block` and publications re-homing, the producer's forecast fiscal-year type, and the
  Terraform IAM prefix list generated from `address()`.
- One batched deletion of the retired old prefixes, on a human's word.
- Retiring the empty `opal-harvest-articles` table is a table deletion and needs a human's word when executed; the
  contracts record the intent, not the authority.

## 12. ADDENDUM v0.22 -- THE LENOVO TRIAL: one security through every stage (Andrew-direct 2026-09-22 ~13:5xZ)

**The word, verbatim:** *"Let's try one sample first, let's run Lenovo through the entire pipeline. Let's do every single
thing for Lenovo and use that as the trial."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260922_135xZ_AMGT_LENOVO_SINGLE_SAMPLE_FULL_PIPELINE_TRIAL.md`
@`cd0cca7f46`. It rests on:
- @`78106b9cea`: Andrew delivers the starting list, and the structure is built on it.
- @`6f1a72e4be`: composite FIGI is the working key for research, and the data quota binds.
- The field-level channel map @`3a0b3cadaa` (`prd/FIELDMAP_20260922.md`).

**Scope.** The validation scope for the next round is ONE security: **Lenovo Group, `992_HK_Equity`.** It is listed in
Hong Kong, reports in USD and has a fiscal year ending 31 March. It **replaces the three names of `C-VALIDATION-NAMES`**
for every cell until the trial is graded. Every other clause of section 10 stands: no fleet run, and no re-run of the
covered population. **Posture is out of scope** (@`78106b9cea`).

**What "every single thing" is.** Every stage of section 10's table except posture, run for Lenovo in dependency order.
Each stage ends SERVED or UNRESOLVED with its reason, never a silent skip. Every channel of the field map is exercised at
each layer it has: identity -> bronze -> silver -> the served object -> the page.

| # | stage | channels | Lenovo today (measured: 18 of 1,780 harvest objects, key-anchored `992_HK`) |
|---|---|---|---|
| 1 | identity | Bloomberg add-security, with the FIGI family, ISIN, SEDOL and LEI appended to its identity fields | no identity record, no FIGI |
| 2 | model block | Bloomberg refdata, histdata and bestdata; bronze then silver `model_block`; served block | refdata and histdata 09-16; 3 served blocks; no forecasts; silver not wired |
| 3 | filings | ⛔ **the battery IN ITS RATIFIED ORDER, EDGAR STEPS INCLUDED -- see s.12a, Lenovo IS an EDGAR entity.** Steps 1-2 run and are expected to RESOLVE the entity and then FAIL acceptance test (b); step 4 is the issuer's own site; step 5 is HKEX, the first instance of the ratified national-regulator route. ESEF does not apply (HK) | `filing_attempt` UNRESOLVED-SOURCE -- the state is right and **its recorded REASON is wrong** (s.12a) |
| 4 | translation | only for a document the detector reads as non-English | none |
| 5 | analysis and drafting | the analyzer and the drafter (model calls) | none |
| 6 | management | the filing's officer section, Bloomberg `COMPANY_EXEC_OFFICERS`, Lusha, the CEO SERP | no `management/v1` object at all |
| 7 | peers | the SA peer set via the ADR line, where `C-PEER-SET-SA` can be met; otherwise the ranker, recorded as the fallback | `peers/v1` (5 versions, ranker) |
| 8 | scores | the three scores | `scores/v1` present |
| 9 | chatter and news | the publications harvester (one run for Lenovo), EXECUTED by `AMGT_HARVST` once its `C-HV-BRONZE-AS-RECEIVED` and `C-HV-SILVER-FROM-BRONZE` land (`C-HV-BOUNDARY`: one pass, not two; this stage waits on them); SA news on the ADR line | none |
| 10 | social | one Bright Data dataset job | none |
| 11 | price | the daily price pull | none |
| 12 | the page | Lead Panel, Thesis, Exec Mgmt, Peers and Model on DEV, read from the pool | renders from partial objects |

**Preconditions -- each lands before the stage it guards, not after:**
- **Identity first.** Stage 1 runs before every other stage. The working key (composite FIGI) is RECORDED on the crosswalk
  record as an attribute. `security_key` stays the partition and page key until the key design is ruled.
- **Fiscal-year pairing.** The model block for a 31 March year-end is graded only with the fiscal-year join wired
  (field map s.3 item 2, `fye_join.py`).
- **Language (Z-S221).** No filing is analysed until the detector distinguishes Latin-alphabet languages. This is the CVO's
  ordering ruling, `ADJUDICATION_v30` @`921cc430c1`.
- **Currency.** The model block states Lenovo's reporting currency (USD) against its listing currency (HKD) on every
  per-share and valuation figure, and never mixes the two silently.

**Vendor words, for Lenovo only, one pass per channel.** The caps are the L4 owner's, stated in the record:

| channel | cap |
|---|---|
| Bloomberg | 1 unique security |
| issuer crawl | at most 40 pages |
| Seeking Alpha | at most 10 calls |
| Lusha | at most 10 credits |
| SERP | at most 3 queries |
| social | at most 1 dataset job of the smallest size |
| publications | 1 run |

A channel whose cost cannot be stated in advance prints it before the call.

**Served objects.** The trial writes Lenovo's served keys (`derived/model_block`, `management/v1`, `peers/v1`, and so on).
**Each such write takes its never-widen pair** (CTO and COO halves, blast radius = Lenovo's keys only, with rollback per key).

**Done when:**
- (a) every stage 1-11 ends SERVED or UNRESOLVED with its reason for `992_HK_Equity`;
- (b) the DEV page renders all five in-scope tabs for Lenovo from the pool;
- (c) ONE trial report lists, per channel, the fields that landed at each layer and which tab shows them. It names every
  breakpoint Lenovo hit.

That report is the design input for the key, fiscal-year, currency and language structure and the per-component
contracts, before any second security.

**What this section does NOT authorise:**
- any security other than Lenovo;
- any schedule or cadence;
- any deletion;
- posture;
- a contract change -- the ratified text is untouched.

### 12a. ADDENDUM v0.24 -- LENOVO **IS** AN EDGAR ENTITY, AND THE REGULATOR ROUTE WAS ALREADY RATIFIED

⛔ **TWO CORRECTIONS, BOTH OF CLAIMS THIS SEAT ITSELF WROTE. Neither changes a contract; both change what a
cell is told to do.**

#### (1) `(not an SEC filer)` WAS FALSE -- measured at the regulator, not inferred

`GET https://data.sec.gov/submissions/CIK0000932477.json`, 2026-09-23, HTTP 200, 12,943 bytes:

| field | value |
|---|---|
| `name` | **LENOVO GROUP LTD** |
| `cik` | `0000932477` |
| business address country | **Hong Kong** |
| `formerNames` | LEGEND GROUP LTD /FI; LEGEND HOLDINGS LTD /FI |
| `tickers` / `exchanges` | `[]` / `[]` |
| **filings, all-time denominator** | **63** (`filings.files` is EMPTY, so `recent` IS the whole history -- no older shard unread) |
| form histogram | `SUPPL` 44, `ARS` 6, `SC 13D/A` 5, `F-6EF` 2, `4` 2, `SC 13D` 1, `3` 1, `12G32BR` 1, `424B3` 1 |
| **10-K / 20-F / 40-F / 6-K** | **0 / 0 / 0 / 0** |

**So the entity RESOLVES at battery step (2) EDGAR-by-Bloomberg-CIK.** What is absent is not the filer --
it is a CURRENT annual report. ⭐ **And the sharpest part is that EDGAR DOES hold six annual-family
documents for Lenovo (`ARS`), and they fail anyway:** every one is an `AUTO-GENERATED PAPER DOCUMENT`
under a `9999999997-*` placeholder accession, newest **2007-08-07**. So they fail acceptance test **(b)
CURRENT** (19 years, against an 18-month bar) and test **(c) KNOWN FAMILY** (a paper placeholder has no
document for the cutter to parse).

⛔ **WHY A WRONG REASON IS NOT COSMETIC HERE.** `C-FILINGS-ANALYZER` already requires UNRESOLVED-SOURCE to
persist *"every step's attempt, key and failure reason"*, and `rk-127`'s HELD marker puts that reason on
the **served page**. A battery that records *"not an SEC filer"* writes a **false sentence onto Andrew's
screen** and tells the next reader the EDGAR steps are inapplicable to Lenovo, when in fact they resolve
the entity and are the cheapest available identity evidence. The correct recorded reason names the
resolved entity, the step that resolved it, and the acceptance test the document failed.

⚠ **One live hazard this measurement surfaces, stated not fixed:** five of Lenovo's EDGAR filings are
`SC 13D`/`SC 13D/A` in which **Lenovo is the FILER about another issuer.** Acceptance test (a) RIGHT
ENTITY matches on the issuer's name and would PASS such a document; only test **(c) KNOWN FAMILY** rejects
it. **The guard holds, but on its third leg, not its first** -- so (c) is load-bearing for every non-US
name and must not be relaxed into a warning.

#### (2) THE REGULATOR ROUTE NEEDED NO `C-` AMENDMENT -- IT WAS RATIFIED ON 2026-09-18

The CTO ruling `CTO_RULING_AMGT_RESAPP_REGULATOR_ROUTE_20260923T0210Z.md` directed that *"a PRD amendment
carries the route into `C-`-space."* ⛔ **That act is VOID as unnecessary: `C-FILINGS-ANALYZER` has carried
*"(5) the national regulator, one adapter per jurisdiction, built only for a name that step 4 fails"*
since Andrew ratified the international battery** (`ANDREW_DIRECT_20260918_194xZ_AMGT_RESAPP_SIX_CARDS_ANSWERED.md@4de34f0d95`),
and that clause sits INSIDE the CONTRACTS section (ratified-text half).

⭐ **THE ERROR WAS A GRAIN ERROR AND IT IS WORTH NAMING: the ruling MEASURED THE CODE
(`battery.py:597`/`:639`, `fetch.py:242` -- no regulator abstraction, true) AND CONCLUDED ABOUT THE
CONTRACT.** Those are different objects with different owners. The true state is **RATIFIED AND UNBUILT**,
which is a CELL, not a scope change -- so nothing re-opens the ratified-text half and HKEX needs no new
authority beyond what Andrew already gave. The ruling's OTHER three limbs stand unchanged: the route is
additive and ordered LAST, EDGAR and issuer-site precedence is untouched, and `filing_attempt` stays
write-once and overwrite-refusing.

⚠ **Rule 30 still binds the build and is NOT restated as a contract here** -- it is law, and a PRD that
repeated it would create a second carrier of one obligation. The cell's own AC0 is the registry row;
`infra/logic/registry/` carries six files and none mentions `hkex` or `regulator`.

**Which half this moves:** the BRIEF half only. No ENDPOINT line and no `C-` contract changes.

---
---

# ADDENDUM B -- THE FRONTEND IN PATTERN, AND THE EXPORT (v0.25, L4, 2026-09-24)

**Author** `1.0.0_SA_CTO~Z`. **Driver** `2.0.0_SA_COO~Z`, named by Andrew. **Cut for a fresh CANONICAL ROUND** --
`AMGT_RESAPP` handed back out of closer mode at `ad5c7a75c6` (R-26).

**L1 basis** -- `4.0.0_SA_CRO~Z`, `docs/briefs/amgt-resapp-frontend-pattern-brief-20260924.md`, cut at
**@`21dd61e392`**, the bytes that carry F1 RESOLVED (walk delivered @`eeaec8707b`; F1 note added additively).

**THE GOVERNING WORD IS THE GOAL, NOT THE BRIEF.** Andrew-direct ~05:0xZ, recorded verbatim at
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_050xZ_AMGT_GOAL_AND_COMPLETION_TEST.md`:

> *"Visually polished "Security Analysis" application with all Asset Management research companies folded in,
> export option functional with presentation in Opal Brand Guidelines form mimicking Asset Mgmt team's earnings
> reports 2pg max or machine readable rich text output ... Only when all of this is done for every single security
> in the Asset Management research folder is the goal complete. Finish AMGT_RESAPP, AMGT_CORPUS and close them out
> and their addendums."*

## B.1 -- ⛔ THE EXPORT IS IN NEITHER BRIEF, AND ONLY A SUBTRACTION FINDS THAT

The frontend brief's nine outcomes (`O1`-`O9`) are **all render outcomes**, and its own Part VII lists *"the print
action"* among what it did **not** capture. The CORPUS brief never mentions an export. ⛔ **SO BOTH ADDENDA COULD
HAVE BEEN CUT, SIGNED, DRIVEN AND GRADED COMPLETE WITH ANDREW'S THIRD CLAUSE UNSERVED, AND EVERY ARTIFACT WOULD
HAVE READ DONE.** It is found here because his goal was decomposed as *his clauses MINUS what is covered* rather
than read for the parts that matched work already in flight. **`FWD-30` exists because of the subtraction.**

## B.2 -- THE NEW OUTCOMES: `FWD-21`..`FWD-30`

Highest existing id is `FWD-20`, so these take the next unused numbers; nothing is renumbered or reused.
`FWD-21`..`FWD-29` are the brief's `O1`..`O9` in its own order; `FWD-30` is B.1's.

⛔ **THE DEFINITIONS LIVE IN THE ENDPOINT SECTION ABOVE, NOT HERE -- ONE CARRIER.** ⚠ **That is a correction: the
first cut defined them here and in the header and left the ENDPOINT section empty of them, and the step-4 PRD
surface-manifest gate REFUSED the commit, naming all ten** -- *"the R3 monitor reads the header and step 5 reads the
section, so this drift is invisible to a reader and total to a consumer."* ⭐ **Third instance tonight of this seat
amending a decision and leaving a coordinate, and the only one a gate caught rather than a reading.**


⚠ **`FWD-30`'s "OR" IS ANDREW'S AND IS NOT THIS SEAT'S TO COLLAPSE.** He wrote *"2pg max **or** machine readable
rich text output"*, so **either branch satisfies the outcome** and a cell may serve one. ⛔ **A cell that serves
NEITHER, or that serves a two-page layout which is not in Opal Brand Guidelines form, does not realize it** -- and
the brand form is `deck_generation/DESIGN_BIBLE.md`, a ratified carrier, not a judgment. **The 2-page cap binds
branch (a) only**; branch (b) has no page count because rich text has no pages.

## B.3 -- F1 IS RESOLVED BY ANDREW, SO THIS ADDENDUM CARRIES NO FORK

`4.0.0_SA_CRO~Z` raised ONE fork and routed it to Andrew rather than taking it silently. He answered ~04:5xZ,
VERBATIM: *"Go with your recommendation on the band, and your recommendations on whatever else, if you need to do
more research first go ahead but otherwise hand off to CTO!Z"* (record @`21dd61e392`).

**RESOLVED: in Security mode the identity header is the page's ONE band; in Universe mode the Lead Panel is the ONE
band; every other container is a white hairline panel.** ⚠ That seat read his sentence NARROWLY -- the recs it had
in front of him and nothing wider -- and this seat adopts that reading without widening it.

⭐ **AND THE ARCHITECTURE TENSION IS CLOSED BY MEASUREMENT RATHER THAN BY PICKING A SIDE.** His 02:47Z word
*"i wouldnt change AMGT_RESAPP page layout architecturally"* and his ~04:3xZ word *"completely upgrade the
frontend"* are both honoured by the NARROW reading, and **the walk's own conclusion is that nothing requires the
architecture to change**: one header, five tabs in the ratified order, no tab moved, no route added, no re-split.
`C-PAGE-LAYOUT` is UNTOUCHED.

## B.4 -- NEW CONTRACTS

**`C-CLAUSE-CITED-REJECTION`.** A rejection of any `FWD-21`..`FWD-29` candidate **cites a `DESIGN.md` clause
number**. A rejection on taste is not a rejection. The clauses in scope are C1, C3, C5, C6, C8, C9, C10, C11, C12.

**`C-RENDER-IS-THE-ORACLE`.** ⛔ **A SOURCE READ NEVER GRADES A RENDER OUTCOME.** *"Walls of text and overlapping
chaos"* is a RENDERED property; acceptance is a PNG at 1440 plus the DOM measurement JSON from
`portal/scripts/ui-smoke.mjs`, for each of the six states. ⭐ **AND A PASS ON THE JSON WITHOUT THE PNG READ BY A
PERSON IS CARE, NOT A CONTROL** -- the brief's own words, adopted verbatim as contract.

**`C-EXPORT-ADDS-NOTHING`.** The export serves only what the page serves: same figures, same cites, same absences.
An ABSENT field is ABSENT in the export with its reason. **No figure is computed for the export**, and the
"value must carry its claim" law binds the export exactly as it binds the page.

**`C-PRESENTATION-ONLY`.** ADDENDUM B changes **presentation** and not the four routes, their payload shapes, or
any served DTO. ⛔ **A field a tile or tooltip needs that the payload does not carry is a SERVED-RUNTIME ASK, never
a page-side computation** -- `C-SERVER-SIDE-RANKING` and the value-must-carry-its-claim law both bind. ⚠ **`FWD-30`
IS THE ONE OUTCOME THIS CONTRACT MAY NOT COVER**: if the two-page form needs a field no route serves, that is a
route change and it comes back to this seat before it is built, not after.

## B.5 -- WHAT ADDENDUM B DOES NOT DO

No page-architecture change (B.3). No route or DTO change (`C-PRESENTATION-ONLY`). No PROD promote -- portal is
commit-yes/promote-no and that is unchanged. No vendor call. No notifier. No change to the verbatim gate, the
PASS/REFUSE face, the three-state reads, the generation caption's facts, the crossed-controls model, the
Peers/Posture symmetry or the "machine, never an instruction" marking -- **the spec changes how these are shown,
never whether** (the brief's IV.9, adopted).

⚠ **AND THE CLOSER ITEMS ARE NOT SWEPT INTO THIS ROUND.** Under Rule 27 work in flight at hand-back completes under
its own spec: the Peers consumer-2 grading, the three Peers failure cases, `BP/_LN_Equity`, the `DE_US_Equity`
third-source fork and the `1ec5446c` portal deploy finish as closer items and their OUTCOMES feed the round-N
enrichment list. **They are named here so the round does not double-own them and so nobody reads their absence from
`FWD-21`..`FWD-30` as their cancellation.**

## B.6 -- L4-R

ADDENDUM B adds ENDPOINT lines and CONTRACTS, so the RATIFIED half re-opens to `3.0.0_SA_CVO~Z`; it rests on a new
L1 brief, so the BRIEF half re-opens to `4.0.0_SA_CRO~Z`, its author. ⚠ **Per R-10 Andrew suspended the L4-R
signature as a BAR for AMGT -- the review is kept, the ritual is not** -- so both halves are routed and the round is
not held on a stamp. `FWD-1`..`FWD-20` and every existing contract are unchanged.
