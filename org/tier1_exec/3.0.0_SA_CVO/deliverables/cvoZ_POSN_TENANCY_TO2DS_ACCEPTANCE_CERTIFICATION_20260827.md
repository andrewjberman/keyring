# POSN_TENANCY.TO-2-DS — ACCEPTANCE CERTIFICATION

**Certifier:** `3.0.0_SA_CVO~Z` · **2026-08-27 ~21:2xZ**
**Instance (certified object):** `org/tier2_senior/0.4.0_DS_ClientPlatform~L/deliverables/POSN_TENANCY.TO-2-DS_PROOF_OF_SPEC.json` @`2be92878c0`
**Deliverer:** `0.4.0_DS_ClientPlatform~L` · **Issuer:** `2.0.0_SA_COO~Z` · **Governing TO** `POSN_TENANCY.TO-2-DS` @`f1c83161bd`
**Decomp:** `posn-tenancy/20260827T200734Z/DECOMP.md` @`07de844b12`, certified PARTIAL @`c04ee33884`

## VERDICT: **ACCEPTED.** AC1–AC4 PASS. 4 criteria, 0 violations.

---

## 1. WHAT I RE-DERIVED AT THIS SEAT, AND WHAT I DID NOT

**RE-DERIVED (my own instrument):** `proof-of-spec-check.py` run here returns
**`violations=0 … VALID`**, `acceptance rows=4`, forward alignment **4/4 criteria → cell**, **4/4
cell_refs resolve** into a 22-id decomp space, governing TO resolved via `decomp_ref.to_ref`, and
`vintage_commit 07de844b12` resolves to a commit in this repo.

**NOT re-derived, and named rather than quietly inherited:** the S3 counts. `0.4.0_DS_ClientPlatform~L`
committed `posn_probe.py` **so every count is re-derivable rather than quoted** — that is the right
artifact and re-running it at a second seat would be **repetition, not corroboration**. The counts are
accepted as measured *by a published instrument*, which is a different and better basis than trust.

## 2. THE BACKTICK: RESOLVED BY VINTAGE, NOT A DISPUTE

The delivery reports `INVALID`, 2 violations, and attributes the cause to the TO's `<decomp_ref>`
being wrapped in markdown backticks so the checker's raw-tag read fails to resolve the path. **My run
returns VALID.** Both are correct at their vintages: `2.0.0_SA_COO~Z` had already owned and repaired
it **inside the TO itself** — *"the first run came back INVALID because of a defect in THIS TO, not in
the work … `0.4.0_DS_ClientPlatform~L`'s instance was correct and my formatting failed it."*

⭐ **THE DELIVERER'S REFUSAL IS THE PART TO KEEP:** *"I did NOT make my instance match the broken
extraction — adding a backtick would satisfy the string compare and still fail resolution, i.e.
**loosen a gate that is firing correctly**."* **A gate reporting a real defect in the wrong place is
still a gate reporting a real defect**, and editing the instance to silence it would have converted a
correct refusal into a permanent blind spot.

## 3. ⭐ THE STANDOUT: A GRAIN TRAP THAT WOULD HAVE INVERTED THE CRITERION

```
token 'position'    -> 922 of 6,599 hits in Cottonwood's home
                       positions_cube.py, canonical_positions.py, 0_composition.json
                       = THE CANONICAL POSITIONS PIPELINE -- a DIFFERENT GRAIN
token 'positioning' -> 0     allocation_summary -> 0     holdings_attribution -> 0
```

**A naive census returns 922 and answers "Cottonwood Positioning is PRESENT."** The criterion's true
answer is ABSENT. **This is Rule 22 GRAIN doing exactly what it exists for**, caught by the deliverer
before it reached a verdict — and it is the single most consequential act in the delivery, because
**the wrong answer here would have been confidently and specifically wrong.** A second trap
(`firm` → 2 hits, both inside `mullin-confirmation-hearing.json`) is the substring mirror.

**And the pagination discipline is the same class, handled the same way:** auto-paginate **merges
pages and drops `IsTruncated`/`NextToken` — it removes the very field AC1 asks to see** — so each page
was fetched with `--no-paginate` and the loop terminates only on `IsTruncated == False`. **`--max-items`
and `head` appear nowhere in the probe.** This is CLAUDE.md's named retrieval hazard met head-on
rather than worked around.

## 4. CELL STATUS — AFFIRMED, INCLUDING THE ONE NOT UPGRADED

| cell | reported | certifier |
|---|---|---|
| `PT-b-3` | OBSERVED, both halves, three controls | **AFFIRMED.** Home PRESENT (6,599) *and* Positioning ABSENT (0) from one probe — the two-armed form the cell requires |
| `PT-c-2` | **PARTIALLY OBSERVED** — consumer half observed, **producer half does not exist** | **AFFIRMED, and the restraint is the point** |
| `PT-inv-1` | OBSERVED (held by construction) | **AFFIRMED** — read-only method, no render, no browser call |
| `PT-inv-4` | **MEASURED NO-OP** | **AFFIRMED** — read-only ⇒ byte-identical *by construction*, reported as a no-op and **not as a verification performed** |

⛔ **`PT-c-2` NOT UPGRADED DESPITE FOUR PASSING CRITERIA, AND THAT IS CORRECT.** Criterion verdicts and
cell states are different objects; **a cell is upgraded by observation, not by its criteria passing.**
The deliverer states cell status *"from states OBSERVED only, never synthesized from criterion
verdicts"* — **that is the discipline my F2 finding was about**, arriving unprompted from the lane.

⭐ **AND `PT-inv-1` IS HELD BY METHOD RATHER THAN BY TESTIMONY.** A read-only substrate probe **cannot**
discharge anything by a render. **This is the first POSN_TENANCY evidence produced after F2, and it
does not contain the failure F2 named.**

## 5. ⛔ A FINDING ABOUT MY OWN CERTIFICATION, SURFACED BY THE CHECKER

The alignment pass reports:

> *"UNDELIMITED — 3 harvested id(s) `['PT-b-2','PT-b-4','PT-inv-7']` are not reached by any criterion,
> but this `<decomp_ref>` has no `<owned_cells>` delimiter, so a READ-DEPENDENCY or an EXPLICIT
> EXCLUSION CLAUSE reads here as a claim."*

**Those three ids are in the TO because they are MY SCOPE FENCE** — the TO quotes *"Certified PARTIAL
by `3.0.0_SA_CVO~Z` — 18 of 19 cells…"* and names what is excluded.

>> **MY FENCE, QUOTED INTO A TO, IS HARVESTED BY THE ALIGNMENT CHECKER AS DECLARED CELLS.** I found
   this shape three hours ago with a grep and wrote *"the better-written the fence, the more a census
   reads it as a violation."* **It is not a property of my grep. It is a property of the estate's
   alignment instrument**, and it will recur in every TO that cites this certification. <<

**The tool handles it correctly** — reports it, declines to assert a violation, and names the remedy.
**REMEDY, and it is an issuer-side act I am asking for rather than making:** TOs citing this
certification should carry `<owned_cells>id, id</owned_cells>` inside `<decomp_ref>`. **The exclusion
list is the certifier's contribution and the delimiter is the issuer's; neither works alone.**

## 6. SURPRISE CHANNEL — DISPOSITIONS

- **(a) served key referenced by client code does not exist** — `portal-proxy.ts:1381` fetches
  `positioning/model.json`; head-object 404 against a 200 control. **OBSERVATION / INERT.** *Demoted by
  the deliverer's own caller check*: `getModelData` has **zero call sites** (2 occurrences in 1,069
  tracked files, both in `portal-proxy.ts`), and the portal's docs record the call being removed for
  performance. ⭐ **They excluded the benign rival (`X-User-Tier`) via `comp-routes` rather than
  assuming it away** — *"it becomes a defect the moment anything calls the export."*
- **(b) the TO mandates a field the schema forbids** — **VERIFIED at this seat:** `cell_status` is
  **absent** from `org/standards/PROOF_OF_SPEC.schema.json`, root is `additionalProperties: false`
  (positive control: `criterion_id` present). **Putting it in the instance makes the instance INVALID.**
  Placing it in the deliverable was correct. **OBSERVATION / ARMED — owner `2.0.0_SA_COO~Z`** as TO
  author, and it will recur for every TO asking for cell status.
- **(c) the shared checkout moved twice mid-task** — portal advanced `8b8a2cc775 → 4a52439cbe` between
  reading a file and citing it; every `file:line` was re-derived at the current commit. **OBSERVATION /
  INERT**, and the sentence is the estate's: *"a citation whose vintage moved is not a citation, and on
  a ~12-seat shared tree the vintage moves with no signal to the reader."*
- **(d) `PT-b-4`'s two prefixes traversed by the AC2-b sweep** — **reported seen, not acted on**, per
  the TO's standing block. **Correct**: `PT-b-4` is uncertified and no criterion may rest on it.

## 7. BOUNDS

- **I did not exercise the AWS reads.** The probe is committed and re-derivable; that is the basis.
- **AC3's `:1099-1100` 401-vs-404 point is RELAYED, not re-derived** — the deliverer says so, and
  re-running it needs a live bearer, outside a read-only TO. **The relay carries its qualifier.**
- **This certifies TO-2-DS's acceptance only.** `PT-b-3` and `PT-c-2` remain **PRE-CHANGE
  MEASUREMENT**; **no cell is discharged**, because every one carries a post-change exercise arm and
  **no change has been made.**
