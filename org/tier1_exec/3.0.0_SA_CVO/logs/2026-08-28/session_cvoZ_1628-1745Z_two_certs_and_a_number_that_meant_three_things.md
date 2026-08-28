# CVO~Z 1628-1745Z — two certificates, and one number that meant three different things

**archetype:** VALIDATE · **secondary:** DIAGNOSE, COORDINATE
Seat `3.0.0_SA_CVO~Z`, PID 4296. Spawned ~16:28Z on Andrew-direct *"let's get the tier 1 ~Z agents
back online and they can pick up where they left off"* after the 16:0xZ device reboot.

---

## Objective
Man the surprise channel; resume the certification queue. Andrew re-scoped mid-session (~16:5xZ):
*"If CVO~Z needs to do some final certifications and etc. on ETFS or D4 work, that is fine, i can
handle that with them directly."*

---

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-system --check` | LD-0319 load control | **rc=2 STALE** | 06 source drift; `file_count` **247→248** (predecessor read it UNCHANGED at 247 — the drift ADVANCED). Cause closed to ONE file. NOT regenerated from site Z. |
| `proof-of-spec-check.py` | the declared-no-decomp instance | **rc=0 VALID** | Run to FALSIFY my own hypothesis, and it did. |
| `proof-of-spec-check.py` regexes | reused verbatim in my census | PASS | Measured what the checker DOES, not a paraphrase — the predecessor probe was mine and was wrong. |
| `safe-commit.sh` | 5 commits | PASS | risk-reflex CLEAN each; msg-verify MATCH each. |
| raw `aws` cloudfront / lambda | APPLIED-plane behaviour + origin reads | PASS | rail-marked; the comp plane is DESIRED-only and cannot answer "does the edge serve this". |
| `curl` + `/auth/login` | served-plane reads, 3-arm control | PASS | real bearer 200 / bogus scope 403 / bogus bearer 401. |
| `git show <ref>:<path>` | citation checks at vintage | PASS | Positive control on every ABSENT verdict. |

**What worked:** positive controls, again — three near-false-findings caught by one, none by care.
**What failed:** my own path and grain assumptions, four times (below).

---

## Work Completed

### Startup
`/watcher` armed — Monitor `bgilqjgz4`, **parent-tied pid 20483** (banner read: ARMED, not
orphan-capable). Registered. **CRONS: ZERO** — both readings of the LD-0318 fork still converge on
arm-nothing. **11 reboot-window messages had been drained to `read/` after my predecessor's log cut
and never read by an agent** — read in full and ACKed; 15 ACKs total across the session.

### The `<decomp_ref>` census — CLOSED, and it found a live survivor
My predecessor left it explicitly unfinished (74 faces / 8 / 42 / **24 UNACCOUNTED**, marked
DO-NOT-QUOTE). Re-run with the checker's own regexes: **2165 faces, 77 carry `<decomp_ref>`, 77 of 77
accounted** — 75 CLEAN, 1 WRAPPED, 1 NO-PATH. The wrapped one was `D1_CATVIEWS.TO-S1-DE`: **same
issuer, same batch, same decomp run as the face that had just cost TO-M1-DS forty minutes**, and the
next face an executor would pick up. Issuer fixed it; the class is now zero. The NO-PATH row I
**exercised and falsified as a defect** rather than filing it.

### Two certifications
- **`ETFS_POSITIONING.TO-12-DE` — 5/5 CERTIFIED** @`6bac8e6cdb`. I read both filed PNGs myself. AC2
  passed on a SUBSTITUTED method (the executor captured one fetch and said so rather than presenting
  one read as two) — I tested their by-construction argument instead of accepting it: 18 references,
  **zero write verbs**. AC3's *"NO OTHER ELEMENT MOVED"* is **unsatisfiable-as-written** for any
  correct AC1 — an ISSUANCE defect, accepted by the issuer.
- **`D1_CATVIEWS.TO-M1-DS` — PARTIAL 4/5** @`d28d8b6918`. AC1 correctly UNCOMPUTABLE. **Finding:
  AC4's claim is TRUE and its citations resolve to NOTHING at any ref** — `:585/:588` matches no
  commit and not the working tree, with non-constant offsets, so they point at a transient mid-edit
  tree stamped with a real vintage. *A citation whose LINE comes from one plane and whose VINTAGE
  comes from another is unverifiable by construction.*

### The pre-deploy baseline @`bc9d11dd8e` (amended `4c4f245316`, `f8f1162560`)
Captured the four served `category-views` objects **before ACT 1**, sha256-pinned, with a runnable
whole-object leaf diff. **The capture window closes at the deploy** — the producer rewrites these
every fire, so the "before" stops existing. It covers the gap the acceptance predicate structurally
could not: that predicate checks fields we PREDICTED would move, and **the residual Andrew approved on
is a field nobody predicted.**

### Surprise channel
- **S1 (BLOCKING) — portal submodule had NO committer identity** while the workspace did; every portal
  commit died rc=128. Verified the discriminator, declined to fix (shared-config mutation, out of
  lane), routed it. `2.0.0_SA_COO~Z` took it. **I then verified REMEDIATION on the axis their own test
  did not cover** — config in `portal/.git/config`, **0 hits in any diff**, and the `M portal` gitlink
  moved because a DE commit advanced the submodule, not because of the fix.
- **S2 (INERT)** — a hash cited as content that was a container. Confirmed with a negative control.

---

## ⛔ THE SECTION A SUCCESSOR SHOULD READ FIRST: ONE NUMBER, THREE MEANINGS

`global.Client` = $290,426,813.47, identical to 49financial's **to the cent**. Across ~40 minutes it
was characterised three ways, and **the arithmetic never changed — only what it was evidence OF**:

| framing | verdict |
|---|---|
| "global aggregates Client over ONE FIRM of three, understating by $359,773,356.74" | **FALSE** |
| "a RESIDUAL on a HELD node that should be `null`" | **also wrong** — nulling it would delete a correctly-computed L0 total |
| **"global's upstream `non_model_aua` carries 49financial's SERIES, not an aggregate"** | **MEASURED** |

**HOW THE FIRST ONE SURVIVED FOUR SEATS:** it predicted a TRUE arithmetic relation (the gap really is
cottonwood+inflection). Peers corroborated the ARITHMETIC — correctly, on genuinely different
instruments — and **nobody re-derived the MECHANISM.**
⛔ **AND MY SHARE IS NOT SMALL: I PRINTED `predicate: "unavailable"` IN MY OWN OUTPUT AND FILED A
"SELF-CONTRADICTION" ANYWAY** — quoting half of `predicate_reason` as contradicting the value while
the other half of the same sentence explained it. I had the disconfirming field in hand.
⭐ **`0.4.0_DE_ClientPlatform~Z` named the failure best:** *a residual on a held node predicts that
exact equality just as well as an aggregation bug does — so the number never discriminated between
the two.* Consistent with both hypotheses is the one thing evidence must not be. **I hold a banked
rule for exactly this and did not apply it.**
**THE RESOLUTION, measured:** `global.non_model_aua` == `49financial.non_model_aua`, and
`1.0.0_SA_CTO~Z` then showed it holds **455 of 455 date-aligned shared dates over 22 months**. The
discriminator is INTERNAL: **`global.Models` sums all three correctly in the SAME object.** One field
aggregates, the other does not. **Located to the ARTIFACT, not to the expression — I did not read the
upstream producer and did not name a mechanism.**

## My own errors this session, all four the same family

| what I did | caught by |
|---|---|
| Routed business logic to MSTR because that seat was carrying a card | **Andrew, directly** |
| Reported provenance read from `C:\tmp` — native python resolves a literal `/tmp/x` there, and it **silently read a DIFFERENT file** rather than failing | two reads disagreeing on one field |
| Said "4 files changed" — pathed both cottonwood builders under `data/mdpf/` when they live under `data/assets/`; `git diff -- <nonexistent>` contributes **silently** | a path-existence control |
| Wrote *"blank above = the fix entered no tracked file"* over output that was **not blank** | re-reading my own output |

**The family: an instrument that returns a plausible answer instead of an error.** A crash would have
been safe every time.

---

## Decisions Made
1. **Did not regenerate 06** from site Z — device axis, independent of dirtiness (0 of 248 sources dirty).
2. **Did not edit an issuer's face** on the backtick finding — kept the 13369 precedent.
3. **Did not set the portal committer identity** — shared-config mutation is a lane call, not a verifier's.
4. **Did not re-commit a certificate to sharpen an already-true sentence** — churn on a live-cited
   artifact is the hazard; three hash citations went stale in twenty minutes, one inside a message
   whose purpose was to correct a stale citation.
5. **Certified AC3/AC5 on the executor's denominator, CITED and NOT independently confirmed** — and
   said so, with the two-registry lead recorded for whoever needs it.

## Blockers
**NONE at this seat.** Both open items are gated elsewhere and named.

---

## Current State
`3.0.0_SA_CVO~Z` PID 4296 · watcher Monitor `bgilqjgz4`, parent-tied pid 20483 · **CRONS: ZERO**.
```
6bac8e6cdb  cert ETFS_POSITIONING.TO-12-DE 5/5        ON ORIGIN
d28d8b6918  cert D1_CATVIEWS.TO-M1-DS PARTIAL 4/5     ON ORIGIN
bc9d11dd8e  pre-deploy baseline, 4 scopes             ON ORIGIN
4c4f245316  baseline amend (global out of controls)   ON ORIGIN
f8f1162560  RETRACTION across cert + baseline         LOCAL
```
(ls-remote read; negative control: portal PROD `d4a048fd` NOT an ancestor, so the verdicts discriminate.)
Push is the integrator's leg under `0.0.0_AB_MSTR~Z`'s declared hold for laptop leg 2.

## Next Steps
1. **[3.0.0_SA_CVO~Z]** Close `TO-M1-DS` when ACT 1 lands — AC1 lifts on the **REBUILT PACKAGE**, not
   on tomorrow's fire alone.
2. **[Andrew]** The **D4 register close**. `ETFS_POSITIONING` / `ETFS_INGEST` still read `active`; per
   his 16:5xZ word the register act is his and this seat's, not a driver's. **Not stamped.**
3. **[whoever closes the ACT 1 ledger]** Run the baseline diff from the README **at HEAD**. `global`
   goes in NEITHER column — record it, unscored. Controls are cottonwood + inflection ONLY.
4. **[open, unowned]** The upstream `non_model_aua` defect — located to the artifact, expression unread.

— `3.0.0_SA_CVO~Z`
