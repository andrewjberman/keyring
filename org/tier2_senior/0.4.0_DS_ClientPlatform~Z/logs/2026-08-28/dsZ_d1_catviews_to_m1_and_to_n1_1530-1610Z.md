# A census I ran to validate a new schema field retired the field instead, and the defect I found in my own accepted work was invisible to every criterion that accepted it

**archetype:** BUILD
**secondary_archetypes:** DIAGNOSE, VALIDATE, COORDINATE

**Date:** 2026-08-28
**Project:** D1_CATVIEWS (Rule 27 — this instance's only project)
**Window:** 2026-08-28T15:30Z -> 16:10Z (session start to the Andrew-direct reboot order)

**Workspace commits (SITEZ, LOCAL — 0.0.0_AB_MSTR~Z is the integrator, GATE 5 denies seat pushes):**
`a5227cf161` · `c5b405f643` · `70a0828226`
**Push state: LOCAL, UNREAD** — no `ls-remote` run; the reboot order arrived mid-build and pushing is
the integrator's act under the STEP 2 sequence in 13373.

---

## Objective

Seated to `D1_CATVIEWS.TO-M1-DS` — map the L2 dollar values. Andrew-direct ~15:0xZ, verbatim:
*"It's there but no dollar values attached need that sorted."* Blocks `TO-S1-DE`.

---

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | `'D1_CATVIEWS' --files` · `'mdpf_category_registry' --files --all` · `'\baum_basis\b' --all` · `'\w+_basis\b' --all -i` | **RAN, AND THE `aum_basis` CENSUS KILLED A SCHEMA ACT.** See "Decisions". |
| `comp-pipescript io` | both edited gold scripts, `--pipeline mdpf` (flagless is rc=2 REFUSED) | WARN "READS/WRITES none detected" on both. Recorded as the **tool's blind spot**, not a finding: the consolidator builds S3 keys dynamically, the registry is pure in-process. Write path read manually at `:837` and confirmed against live `s3api`. |
| `comp-estate` | `--resource 'category-views'` | `no chain references 'category-views'` — a **true negative kept rather than dropped**. Located the artifact by direct `s3api` listing instead. |
| `.tools/commit-gate.sh` | 3 runs across 2 scripts | PASS every time; `2 of 2` and `1 of 1` files checked (denominator printed). |
| `.tools/safe-commit.sh` | 3 commits, `-F` msgfiles written by the **Write tool**, never a shell heredoc | PASS; `msg-verify MATCH` on all three. |
| `proof-of-spec-check.py` | **3-arg form** with the TO's declared set | `rc=1 INVALID`, 2 violations, both on the TO's face. The **2-arg form is the one that returns a false VALID** (`3.0.0_SA_CVO~Z`, 13332) and was not used to close anything. |
| `comp-validate` | **NOT RUN** | It is the DS minimum *before signalling AE*. No AE signal is being sent and the post-change artifact does not exist; running it against the pre-change bytes would validate the very bytes this change alters. Owed at the deploy signal. |

---

## Work Completed

**`a5227cf161` — TO-M1-DS, the producer half.** `models_member_aum` accumulated in the loop that
already held both the member id and its value; `_members()` emits `aum`. Nothing new is computed and
no new source is read — byte-for-byte the same keep-vs-discard the SMA half was corrected on 08-27.

**`c5b405f643` — the TO-M1-DS proof-of-spec instance.** AC2/AC3/AC4/AC5 PASS. **AC1 UNCOMPUTABLE, not
rounded up**, with its lifting event named *in the field*.

**`70a0828226` — TO-N1-DS, the predicate fix.** `_l0_of()`; both branches now use one form.

---

## Decisions Made

- **Refused to fold TO-N1 into TO-M1.** A one-line fix and a one-line blast radius are different
  measurements: TO-M1 maps display values, the other moves **$22.79M between two served client-facing
  categories**. `3.0.0_SA_CVO~Z` and `2.0.0_SA_COO~Z` both backed the refusal; cut as its own TO.
- **Emitted `aum: null`, not `0.0`, for an unmapped member** — and did NOT encode Andrew's
  *"a null is a 0 in this case, practically"* in the producer. His two rulings are only
  simultaneously satisfiable if the producer emits null and the **renderer** zeroes it. Encoding 0.0
  here would satisfy one by destroying the other. Routed to `0.4.0_DE_ClientPlatform~Z`.
- **Rejected `startswith("SMA")`, the repair the TO itself named as the obvious candidate.** A bare
  prefix has no delimiter, so a future `SMARTX` node folds silently INTO SMA exactly as the suffixed
  paths fell OUT of it. Same defect, longer fuse. Split on the `" > "` separator instead — **and
  applied it to the Models branch too**, removing the latent trap from the branch that never broke.
- **Did not edit the TO face to make my own proof validate.** Routed the two-backtick fix to the
  issuer with a control. Precedent is in this project's own record.
- **Took the audited `system-current-override` rather than regenerating `comp-system`** — this
  checkout is shared by ~6 live seats and regenerating would compile their unlanded work into a
  committed artifact.

---

## ⛔ THE FINDING: MY OWN ACCEPTED WORK WAS BROKEN AND ITS OWN 7/7 COULD NOT SEE IT

`TO-L2-DS` moved SMA members to `view_path="SMA > {bucket}"`. `mdpf_gold_consolidator.py:611` still
read `== "SMA"`. **The branch became unreachable by construction**, so:

```
49financial serves, VERBATIM:  "49financial has NO SMA category members (Andrew-direct
                                2026-08-25 ...) A TRUE ZERO"
reality:                       divz $18,783,379.81 + pfoe $4,011,386.44 = $22,794,766.25
Client:                        overstated by exactly that -- the netting line is gated on
                               members_present, which never fired
```

**A defect wearing a sovereign citation is worse than a bare defect: the citation is what stops the
next reader from questioning it** (`3.0.0_SA_CVO~Z`).

**Three mechanisms, each worth carrying past this incident:**

1. **All seven of TO-L2-DS's criteria sat on the PRODUCER side of the seam.** The registry emits the
   new shape correctly — true, and certified. Not one asked whether the **consumer** still recognised
   it. *A producer-side criterion set cannot fail on a consumer-side break, however many criteria it
   has.* And the estate had this written down already, for the pipeline next door
   (`etf_positioning_gold.py:266-268`): *"if DS mints one spelling and DE reads another ... BOTH
   HALVES PASS THEIR OWN CHECKS."* **Writing a hazard down does not deploy a check for it.**
2. **`D1-inv-4` held, correctly, at 1,762,750,154.52.** *A sum invariant cannot see a misattribution
   between two of its own summands.* It is not weak — it measures a different proposition, and it
   passes for the same reason the defect is invisible.
3. **`1.0.0_SA_CTO~Z`'s form:** two adjacent lines, same job, different predicate forms. *A
   restructure tests every coupling that is EXACT and silently spares every one that is TOLERANT — so
   the surviving branch teaches you nothing about the safety of the change.*

---

## ⭐ THE CENSUS THAT RETIRED ITS OWN PROPOSAL

I was about to mint `aum_basis` (`measured|absent`) as a claim field, with the Rule 24 four-postulate
record it would owe. The mandated word-boundary census returned it **already in use** in
`data/etf_dashboards/` meaning *which Bloomberg field the AUM came from* — different domain, different
intent. Minting it would have **bridged two vocabularies on one token**. Combined with the consumer
already declaring `aum?: number | null`, the answer was **no new field at all**.

**The census is normally run to justify a token. This one deleted the feature.** I had also done the
MECE uncovered-member hunt for the enum (0 of 30 by_model entries carry an empty `model_value`) —
that work was correct and is now moot, which is the cheaper direction for it to be moot in.

---

## Blockers

**None at this seat.** Four acts remain and **none is DS** — named per Rule 29:

1. **[`2.0.0_SA_COO~Z`]** two backticks in TO-M1-DS's `<decomp_ref>`. Until then the filed instance
   reads INVALID for a reason that is not in the instance.
2. **[`0.7.0_AE_CloudOps`]** ship the gold-lambda package carrying `a5227cf161` + `70a0828226`.
3. **[the next scheduled ~13:31Z fire]** the only route to TM1-AC1 and CATV-TON1-AC7. No ad-hoc run.
4. **[`0.4.0_DE_ClientPlatform~Z`]** render `null` as `$0.00`.

---

## IN FLIGHT AT THE REBOOT — stated so a successor reads it correctly

- **TO-M1-DS:** code + instance committed. AC1 outstanding on the scheduled fire.
- **TO-N1-DS:** code committed and exercised (AC1/AC3/AC4/AC5/AC6 all measured green against the
  served artifact). **NOT DONE:** AC7 (scheduled fire), AC8's estate-wide census limb — run only
  against this one file, **NOT CLAIMED** beyond it — and **no proof-of-spec instance filed**.
- **NOT STARTED:** the 4 missing ETFS_INGEST TO-6/TO-8 proof-of-spec instances, the second half of
  this session's dispatch. Untouched, not investigated.

## Postmortem

**The finding came from grounding, not from looking for it.** I was measuring per-member dollars to
build TO-M1 and printed the SMA rows beside the Models rows because the loop already had them. The
$22.79M was in that output. **Nothing in my task pointed at SMA** — the discipline that caught it was
printing the whole denominator instead of the rows I needed.

**And I nearly shipped the wrong repair twice.** `startswith("SMA")` was named by the TO, endorsed by
two senior seats as "the obvious candidate", and is wrong for the same structural reason as the bug it
fixes. `aum_basis` was mine, fully reasoned, with its Rule 24 record half-drafted. **Both were caught
by a mechanical check I nearly skipped as a formality** — one census, one delimiter question.
