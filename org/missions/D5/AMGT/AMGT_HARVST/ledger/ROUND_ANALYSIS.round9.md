# AMGT_HARVST -- ROUND 9 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-28 ~06:1xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~O` (file 20260928T060323Z): `adjudications/ADJUDICATION_v17.md` and
`remediations/REMEDIATION_v3.md` @`6073975682`. Terminal 2 of 2 (`HVST-x-1`, `HVST-x-2`).

**Round 9 is CLOSED. The project is NOT closed. This analysis carries a PRD ADDENDUM** (section 3), because L9 found
an outcome the contract as written cannot serve.

## 1. WHAT ROUND 9 DID

| item (round-8 list) | outcome |
|---|---|
| 1 second repair (`x-1`) | **the suite is green: 306 passed, 1 skipped (the barrons quarantine), 0 failed** on the CVO's re-run -- Z-W21-S2's red is gone |
| 2 timeline exercise (`x-2`), the round's judgment criterion | **L9 graded it: AC4 PASS with one limit** -- the corrected rule from round 8 held, and L9 was not vacuous |
| 3 the vendor cards `w-2`, `w-4`, `w-5` | at Andrew, unchanged |
| 4 the 16 backlog rows | not re-measured on the record -- carried a THIRD time (section 5) |

## 2. FWD GRADES -- what moved

| FWD | grade | why |
|---|---|---|
| FWD-5 timeline, open a day, strongest first | **NOT REALIZED -- data half EXERCISED** | `x-2` AC2 read Lenovo's landed gold: 267 of 267 dense days, no gap, day `2026-05-22` strongest-first with 0 sort violations. **But the DONE WHEN is an analyst opening the timeline on the company's PAGE**, and `w-3` built the API (3 routes), not a page. **And "strongest first" rests on FWD-4's grade, which is not yet re-derived and matched.** |
| FWD-6 events on the timeline | **NOT REALIZED -- contract defect found** | 12 events exist (the "unsatisfiable" premise was false, corrected by `2.0.0_SA_COO~Y` @`635f79990f`); 4 of 12 are not coverage about their own security (section 3) |
| the other seven | NOT REALIZED | unchanged from round 8 |

## 3. THE ADDENDUM -- `C-HV-EVENT-SPINE` counts publishers over TIER A only

**The finding (L9, `ADJUDICATION_v17`):** 8 of 12 events are real bursts about their own security. 4 exist only
because the rule counted tier-B co-mentions: an Nvidia PC story became a Lenovo, Dell and Microsoft event with 0
tier-A articles, and a Costco day reached 2 publishers through an unrelated DOJ piece.

**The CVO offered two floors; this seat RULES (a):**
- (a) publishers counted over tier-A articles -- keeps **8 of 12**, exactly the 8 L9 graded real;
- (b) at least one tier-A article -- keeps 9, so one of the 4 spurious events survives it.

**Why (a):** FWD-6's ACCEPT, which Andrew confirmed at L2, reads *"Bursts of real coverage about the company appear
as marked events."* (b) still admits an event whose second publisher wrote about something else. **This brings the
contract into line with the outcome Andrew already ratified; it is not a new outcome and not a scope change.**

**Landed:** PRD `v0.3`, `C-HV-EVENT-SPINE` working rule amended in place with the reason beside it. **It changes
CONTRACT text, so it RE-OPENS the ratified-text half** (this is a multi-round project, so the proportionate
sign-off does not apply). `3.0.0_SA_CVO~Z` signed v0.2 and is wound down; **this seat routes the re-sign to
`3.0.0_SA_CVO~O`.** The brief half is untouched.

⛔ **THE GATE CANNOT SEE THIS RE-OPENING -- measured after the commit.** `.tools/prd_signoff_lib.py` binds both halves
to the ENDPOINT hash (spine v3.19), so `prd-signoff.py status AMGT_HARVST` still reads the ratified half **SIGNED,
current** although its section hash moved (`fa4257b65ca7` signed -> `43375644bc89` now). **So the condition is a
record, not a status line: round 10 does not cut a cell against the new rule until `3.0.0_SA_CVO~O` has stamped the
ratified half at these bytes** (`prd-signoff.py sign AMGT_HARVST --half ratified-text ...`, a new file under
`prd/signoff/`). The mismatch between CLAUDE.md's proportionate-sign-off scope (single-round or sub-week) and the
lib's universal ENDPOINT binding is noted for the lib's owner; it is not ruled here.

## 4. FINDINGS CARRIED

1. **Z-W26-S1, ARMED, and bigger than this project.** A string-targeted `patch("lib....")` silently no-ops when
   pytest imports the test under a different module name (no `lib/__init__.py`): the code under test resolves the
   name off a different module object. `test_worker.py:51` works only by coincidence; `test_verification.py:11` has
   the same shape. **The disarm is a repo-wide audit of `patch("lib.` string targets** -- not a HARVST cell. This
   seat owns routing it (section 5, item 5).
2. **Four remedy clocks still read OPEN** (Z-W21-S2, Z-W9-S1, Z-S27, Z-W11-S1) although each is remedied at HEAD.
   The flip is `3.0.0_SA_CVO`'s to write; carried to it, not re-opened.

## 5. THE ENRICHMENT LIST -- round 10, in order

| # | cell | note |
|---|---|---|
| 1 | **Re-derive the events under the amended rule** (LOCAL), after the ratified half is re-signed | criterion: 8 events, the 4 named spurious ones absent; a rebuild from the same silver reproduces identical rows (`C-HV-GOLD-REBUILDABLE`) |
| 2 | **FWD-4, the strength grade re-derived from stored text and matched** (LOCAL) | FWD-5's "strongest first" and FWD-7 both rest on it |
| 3 | **The timeline PAGE** on the company view, reading `w-3`'s API, with FWD-5's JUDGMENT criterion: an analyst opens Lenovo, picks a day, reads the articles strongest first -- are they right? | the served half of FWD-5; render and READ the screenshot (`/frontend-dev`), dev port 5174 only |
| 4 | the three vendor cards | at Andrew, unchanged |
| 5 | **Z-W26-S1 routed** as a repo-wide audit, owner to be named by this seat outside the round | not a HARVST cell |
| 6 | **the 16 backlog rows** -- carried THREE times | the round-10 issuance commit states them re-measured, or states in one line why the issuer will not |

**Judgment:** cell 3 carries the round's judgment criterion and issues without a vendor word, per the round-8 rule.
**Fan-out:** 1 waits on the sign-off; 2 is independent; 3 can build against today's API and grade after 1 and 2 land.

## 6. WHAT THIS ANALYSIS DOES NOT DO

It changes no ENDPOINT text and adds no outcome. It grants no vendor word and cuts no serp or social cell (Andrew
2026-09-27, @`a89b7619ca`).

## Compiler Tools

The CVO's L9 read with its two floors compared against FWD-6's ACCEPT text, not against the event count alone --
`w-3`'s order read to establish that it built an API, not a page, before grading FWD-5 -- `prd-signoff.py status`
read before the edit (v0.2, both halves SIGNED).
