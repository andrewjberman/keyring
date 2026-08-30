# A green result is only as wide as the arms that existed when it was read — the criterion-5 rework, and a gate whose blocking limb turned out to be superseded law rather than missing work — 0.4.0_DS_ClientPlatform~E

**Date:** 2026-08-30
**Task Order:** D3_MODELOVERLAY.TO-D3.1b (closeout) + 2.0.0_SA_COO 85818 acts (a) and (b)
**Status:** COMPLETE
**Window:** 03:20–05:30Z (delta since the 02:09–03:20Z log)

---

## Objective

Close TO-D3.1b against the grader's verdict, and execute the issuer's two bounded acts: (a) the
criterion-5 rework, (b) a measuring-only pre-read of TO-D3.2's gate. No build, no enum, no
contract edit in either.

---

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `proof-of-spec-check.py` | `<instance> D3.1b-1..D3.1b-5`, unpiped, three times | **rc=1 INVALID (reproducing the grader's FAIL on the committed bytes) → repair → rc=0 VALID with `artifact-resolution: 1 resolved at pin`.** The third run is the one that matters: the arm now *exercises* rather than being absent. |
| `git show <pin>:<path>` + `grep -c` | `artifact-resolution` at `e4a4f3cbee` vs `HEAD` | **0 vs 4.** This is the whole mechanism finding — the checker grew an arm between my run and the grade. Content-resolved at two pins, not inferred from a filename or a date. |
| `comp-find` | `'arm-(a)' --all --files` | 150 hits / 133,234 files scanned. Used to locate the sovereign record rather than trust its name; the deciding read was then `git show 7a843d25da:<deliverable>`. |
| `git merge-base --is-ancestor` | 3 commits vs `FETCH_HEAD`, **plus a negative control** | 3 ON ORIGIN; control (origin head vs my commit) correctly returns false, so the test discriminates rather than answering YES to everything. |
| `comp-system` | regen of `06_current_state.{md,json}` | PASS — discharged the second two-phase override in-session. |

**`comp-pipescript` / `comp-validate` NOT run, same reason as the prior log:** both acts were
read-only. No gold script was touched, deployed or run, so the DS role minimums do not attach.

---

## Work Completed

### 1. The grade, and reproducing the FAIL before explaining it

`3.0.0_SA_CVO` 85812 graded D3.1b-1..4 PASS and **D3.1b-5 FAIL**: the committed instance carried
`commit_or_etag: "PENDING-COMMIT"` on the investigation-file row. I reproduced it at this seat on
the committed bytes (`git diff e4a4f3cbee -- <instance>` empty; checker rc=1, one violation)
**before touching anything**. The FAIL was correct and I said so first.

### 2. The mechanism — neither candidate the issuer offered

`2.0.0_SA_COO` 85818 asked for the mechanism, not the apology, and named two candidates: a
pre-edit draft, or an rc read through a pipe. **Both wrong.** The `artifact-resolution` arm did
not exist in the checker bytes I ran; it was added by `1.0.0_SA_CTO~X` `@3948c766a7` and reached
this shared worktree in a later window push.

Both runs were honest against the instrument each ran. **The instance was wrong the whole time** —
`PENDING-COMMIT` was never legal, merely unchecked. The arm did not create the defect, it revealed
it, and that distinction is the reason this is a banked class rather than an excuse.

### 3. The rework

`PENDING-COMMIT` → `e4a4f3cbee`. **A hash and deliberately not `PENDING-THIS-COMMIT`**: the `.md`
rides `e4a4f3cbee` and does *not* ride the rework commit, so the sentinel would have been false.
CVO confirmed that as the right choice between the two forms it offered. Re-graded **PASS**;
TO-D3.1b **CLOSED, 5 of 5**.

### 4. Act (b) — the D3.2 gate pre-read

**Verdict: still gated, one limb met.**

- **Limb (i) TO-D3.1 — MET, but not by the route its face names.** D3.1-6 ("register the axis in
  `SYSTEM_DEFINITIONS`") is *superseded* by Andrew's 2026-08-20 naming-law act; the sole occurrence
  on origin is the changelog line recording the axis's **removal**. The carry-over that relocation
  created was voided by the CRO itself as "a phantom against finished work." **I verified the
  destination rather than citing that message** — `stability_frame:` `:120`, `sibling_axes:`/
  `identity_source` `:204-205`, both present on origin — which is precisely the error the CRO's own
  message records itself making. **Nothing owed; no CRO re-spawn**, which was the question asked.
- **Limb (ii) the D2 flip — NOT MET on both terms.** P1 green = P1.5 re-grade, unreached (C02-g-6
  at 200 of 535, tick 10 `@80fa8d9ab8`); P3 is downstream of it by the brief's own sequence.

---

## Decisions Made

- **Framed the sovereign scope question rather than answering it.** Opening `@7a843d25da` showed
  Andrew's arm-(a) word is already given and *conditional* ("serve what grades green"), not
  pending — which invited the tidy conclusion that P3 is blocked only on green. But that record is
  scoped to the 08-27 fire and names cottonwood/partner/global, **not 49F**, while the register
  carries a separate 49F-flip hold with its source-gap half unmet. Concluding either way would have
  adjudicated his word wider or narrower. Named it instead; the CTO cut it as reserved call **R5**
  with a recommendation, and both CTO and COO recorded the framing-not-answering as the right act.
- **Reported the C02-g-6 discrepancy without adjudicating it.** The issuer said ~350 of 535; the
  tick-10 commit says 200. A fresher read at the issuer is the likely explanation, the verdict is
  identical at either value, and picking one silently would have been the wrong kind of tidy.
- **Took the reserved two-phase override a second time** rather than inventing a way around a gate
  that was working correctly — and discharged it in-session, as before.

---

## Files Modified

| File | Commit |
|---|---|
| `deliverables/D3_MODELOVERLAY.TO-D3.1b_PROOF_OF_SPEC.json` (criterion-5 rework) | `c393a1e986` |
| `infra/system/06_current_state.{md,json}` (override discharge) | `3cd788b` |
| this log | (this commit) |

**PUSH STATE: LOCAL** — `origin/CLOUD` was `c723b323cf` at my last `ls-remote` read (04:49Z frame).
The three earlier commits (`e4a4f3cbee`, `383b122b87`, `714f985347`) are **ON ORIGIN @5a0e1df70b**,
verified by my own is-ancestor read with a negative control. The rework rides the next window.

---

## Blockers

**None.** TO-D3.1b is closed 5 of 5 and both issuer acts are delivered. TO-D3.2 remains gated on
D2's own remediation round, which is executing normally — **that is a condition, not a stall, and
no D3-side act can accelerate it.**

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| (none this window — both acts reported by message) | 85889/85890 (act a), 85970/85971 (act b) | CVO, COO, CTO |

---

## Current State

TO-D3.1b **COMPLETE, 5 of 5**. TO-D3.1 **CLOSED by the issuer** on limb (i)'s evidence. TO-D3.2
**stays GATED**; nothing seatable on D3 before the flip. The arm-(a) scope question is live as
reserved call **R5** at Andrew. Two two-phase overrides taken this session, both discharged in it.
Delivery ledger clean under LD-0480's `by`-field predicate — every row READ by this serial, no
foreign stamps.

---

## Next Steps

1. **[2.0.0_SA_COO]** Release this seat on capacity, per 85989 — the unit is done and a released
   seat is not a dark one. Re-spawn at the D2 flip for D3.2's seating.
2. **[Andrew, via 1.0.0_SA_CTO's R5 card]** Does the standing arm-(a) word cover the 49F
   PERFRP/INSURE serve, or does the 49F-flip hold need a fresh word? **Settle it before P1.5 goes
   green, not at the moment of serve.**
3. **[1.0.0_SA_CTO]** The tool-shape note CVO routed: have the checker print its own commit-ish
   beside the verdict, so a re-grade under a grown checker reads as a *checker change* rather than
   an author's false claim. This session cost a seat a false attribution for ten minutes.
4. **[whichever D3 face is next]** Re-read `0042708566` against **Monday 2026-08-31**'s partition —
   08-30 is a Sunday, so it is the first business-day read that can settle the one-day absence.
