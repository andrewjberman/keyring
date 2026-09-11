# L5 DISSENT -- NFRA_REPORT v0.8. NOT STAMPED.

**archetype:** VALIDATE

**Seat:** `2.0.0_SA_COO~Z` · **Date:** 2026-09-11 ~02:5xZ · **Artifact:** `org/missions/D12/NFRA/NFRA_REPORT/prd/NFRA_REPORT_PRD.md`
**Read at:** HEAD, content pin `d9c70e9b0a12` (prd-stamp's own pin) · **Read in full:** 756 lines, all nine sections
**Act:** L5 stamp WITHHELD. `python .tools/prd-stamp.py stamp <prd> --stage L5` NOT run.
**Owner of the remedy:** `1.0.0_SA_CTO~Z` (L4 is the CTO's alone, rule 27; `prd/**` is ANY_CTO and the
owned-paths gate refuses a COO commit to it, so this seat could not amend it even if that were legal).

---

## Why this document exists

Andrew-direct 2026-09-11 at the `2.0.0_SA_COO~Z` terminal, VERBATIM:

> *"what you should be doing is reading the PRD critically and either stamping or dissenting."*

`prd-stamp` has three verbs -- `stamp`, `sign`, `status` -- and no dissent verb. The COO's dissent is
therefore the ABSENCE of an L5 stamp plus a stated reason, and a reason that lives only in a broker
message is not durable. This is the carrier.

---

## The dissent, in order of decisiveness

### 1. ⛔ TWO OF TWENTY-ONE OUTCOMES ARE SERVED BY NO ENGINE ROW -- `FWD-13` and `FWD-15`

Computed by SUBTRACTION from the printed denominator, per rule 24(i), never by recall:

```
DENOMINATOR  header endpoint_outcomes            21
COVERED      outcomes named in any section 8 / 8a row   19   (19 rows: S1-S13, S21-S26)
UNCOVERED    declared MINUS covered               2 -> FWD-13, FWD-15
```

  `FWD-13` -- *the morning email a person actually receives carries the new edition's structure with
              TODAY's live numbers.* EXERCISED bar.
  `FWD-15` -- *nothing a reader relies on today disappears in the swap.* EXERCISED bar, and it is the
              regression guard for the whole recut.

**And section 8's own MECE run still prints `12 of 12 outcomes carried, 0 uncovered`.** That claim was
true when the header declared twelve. The header now declares twenty-one. The run was never re-executed
against the new denominator, so the document certifies a coverage it does not have.

⛔ **THIS IS WHY IT BLOCKS L5 SPECIFICALLY, AND IT IS NOT A TIDINESS OBJECTION.** Rule 27's L6 is ONE
ISSUANCE COVERING EVERY CELL. If this seat decomposes from sections 8 + 8a as written, it cuts 19 of 21
and `FWD-13`/`FWD-15` are cut into no cell at all -- **the exact defect this PRD's own v0.5 entry exists
to remedy**, where `FWD-4` was served by no cell and L6's id-scoped coverage limb passed 12-of-12 anyway
because it compares row IDs and cannot see content coverage. That limb would pass again here. The
document would certify the decomposition, and two of Andrew's outcomes would be silently unbuilt.

⚠ **The third recurrence of one class in this document's history**, and the PRD names the first two
itself: v0.2->v0.3 (both carriers not bumped together) and v0.5 (`FWD-4` cut into no cell). The v0.8
header fix at `@1ed4ade1bb` repaired the *header*; the *coverage* beneath it was never re-run.

### 2. ⛔ THE TWO VERSION CARRIERS DISAGREE, AND v0.8 HAS NO CHANGELOG ENTRY

```
prose  **Version:** line 12    v0.7
json   "prd_version"  line 39  v0.8
```

Every other version in this document carries a narrated entry in the `Before it, v0.X ...` chain --
v0.7, v0.6, v0.5, v0.4, v0.3, v0.2, v0.1 all do. **There is no v0.8 entry.** A reader following the
document's own changelog reads a document that stops at v0.7.

What v0.8 actually did, read from `@1ed4ade1bb`: it added **`FWD-13` .. `FWD-21` -- nine outcomes** --
to `endpoint_outcomes`. So the undocumented bump is not cosmetic; it is the single largest change to
the contract in the document's history, and **the two outcomes it left uncovered are among the nine it
added.** Finding 1 and finding 2 are the same incomplete fold seen from two sides.

⚠ This also bears on any future sign-off: sign-offs are version-bound (`prd-stamp` binds them to
`prd_version`), so a reviewer who read the prose and signed "v0.7" would not have covered the nine.

### 3. ⛔ `S1` SPECIFIES TWO AXES WHILE SECTION 6 RULES A THIRD LANDS AT L5

Section 6's ruling on msg 20592 is explicit that the third axis is adopted, and where:

> *"Adopt `state: desired | applied | exercised` VERBATIM from CLAUDE.md rule 22 -- build-ladder rung 2,
> the estate already has this vocabulary. Do not mint a synonym for it."* ... **"BOTH LAND AT L5."**

`S1` is the only surface row for the state model. It names the instrument axis (six values) and the
world axis (three) and **does not carry `state` at all.** Section 2's OWNS item (1) still reads *"the
two-axis vocabulary itself."*

**The CTO flagged this against itself and it has not been carried:**

> *"the moment a third axis lands, this PRD must stop calling it 'the two-axis model' or the record and
> the artifact diverge. **That is this seat's to carry**, not that lane's, and it is flagged here so it
> is not discovered later as a contradiction."*

Discovered later, as predicted. A worker handed `S1` builds two axes and drops `state` -- which is
**precisely the failure `S1`'s own note documents** ("v0.2 abbreviated this cell as 'CHECKED vs BLIND'
and a worker handed only the cell would have built a TWO-value axis"). The cell cannot be cut until it
says which model it specifies.

---

## Two constraints I am recording as constraints, NOT as dissent grounds

**(a) The L4-R sign-offs are absent, so LIMB 6 will refuse my issuance today.**
Measured with a positive control: `org/missions/D9/IRPT/IRPT_BCKEND/prd/signoff` EXISTS (that project
reads both reviewers SIGNED), and the identical probe against `NFRA_REPORT` returns nothing. So the
absence is real absence, not a wrong path -- my first probe used `prd/signoffs/` (plural) and was wrong;
the control caught it.

⛔ **THIS IS NOT A CRITICISM OF THE L4 DELIVERY AND MUST NOT BE READ AS ONE.** The L4-R sign-off gate
was ruled Andrew-direct 2026-09-10 ~21:2xZ; this PRD landed at v0.8 at 19:07Z, **before the gate
existed.** Grading an artifact against a rule minted after it is the error this seat made earlier
tonight against `prd-stamp` and was corrected on by Andrew; it is not repeated here. The sign-offs
matter only because they bind MY act TODAY: `.tools/to-pipeline-gate.py` LIMB 6 refuses a task order
against an unsigned PRD, so an L6 issuance cannot land regardless of when the PRD shipped.

**(b) The PRD names a different L5-L6 owner than the seat holding it.**
The header reads **L5-L6: `2.0.0_SA_COO~ZZ`**, and section 7 and section 9 address that lane by name
throughout. `2.0.0_SA_COO~ZZ` measured DARK at 02:0xZ (6 live serials, it is not among them), and
`1.0.0_SA_CTO~Z` delivered the PRD to THIS lane (msg 21040, *"step 4 done; step 5 is yours"*). This
seat will take L5-L6 on that word and is not refusing on ownership -- but a reassignment that lives
only in a broker message while the PRD's header says otherwise is worth one line in the PRD.

---

## What I am NOT claiming

- **No defect in the substance.** This is a strong PRD. The constraint set is unusually well built:
  `C-TOKEN-PARAM` names the exact footgun with the three parameter names distinguished; `C-MODEL-STRING-VERIFIED`
  refuses to downgrade Andrew's instruction on an absence of confirmation; `C-EXISTING-HOME` measured the
  bucket rather than minting one; section 9 declares its own degenerate packet rather than dressing 12
  alphabetical digests as adversarial findings. Sections 5a and 8a are a correct and honest recut.
- **No remedy proposed as binding.** Each finding has an obvious repair and all three are L4 acts. Which
  repair, and whether `FWD-13`/`FWD-15` get their own rows or extend `S21`/`S22`, is the CTO's call.
- **Nothing reopened.** Round 4's port, partition and deploy are sound and section 8a says so; this
  dissent does not touch them.
- **No gate invented.** Rule 27's L4-R gate and LIMB 6 are pre-existing mechanical gates. This seat
  added nothing.

## What unblocks the L5 stamp

One L4 edit closing findings 1-3: re-run section 8's MECE against the 21-outcome denominator and give
`FWD-13`/`FWD-15` a carrier; narrate v0.8 and align the two version carriers; state whether `S1`'s state
model is two axes or three. Sign-offs then govern L6, not L5. On that edit this seat decomposes the
same turn and stamps.

**Push state:** LOCAL at authorship; `0.0.0_AB_MSTR~Z` holds all pushes.
