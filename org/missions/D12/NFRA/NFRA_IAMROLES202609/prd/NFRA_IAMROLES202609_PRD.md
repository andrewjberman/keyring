# NFRA_IAMROLES202609 -- least privilege across every IAM role, and how we would know

*Registered 2026-09-09 under `D12` on Andrew-direct at the `1.0.0_SA_CTO~Z` terminal, VERBATIM:
**"Ok we will make a project NFRA_IAMROLES202609 underneath D12"**, and sequenced by him in the same
session: **"that is a D12 project as well but it comes behind the others."** That sequencing has now
arrived -- `NFRA_REPORT` is in round 1 and `NFRA_OPSEC202609` holds its own COO lane.*

**Directive:** D12 Platform Operations - **Fabric:** site-z - **dep_stage:** PRD
**L1 owner:** `4.0.0_SA_CRO~Z` - **L2-L4 owner + author:** `1.0.0_SA_CTO~Z` - **L5-L6:** UNSEATED - **L8-L10:** `3.0.0_SA_CVO~Z` - **Integrator:** `0.0.0_AB_MSTR~Z`
**Brief (L1):** `docs/briefs/nfra-iamroles202609-least-privilege-brief-20260909.md` @`1a90986047`
**Endpoint (L2):** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_NFRA_IAMROLES202609_20260909.md`
**Version:** v0.1, 2026-09-09 ~22:5xZ -- **L4 MINT. THE ENDPOINT BELOW IS RATIFIED IN FULL.** All
eight `DONE WHEN` bars confirmed by Andrew 2026-09-09 ~22:3xZ, VERBATIM: **"Confirm on
IAMROLES202609."** Given in answer to `/open-calls` CALL 3 of 3, whose card put exactly these eight
bars to him and recommended confirming now so L3/L4 could run.
**archetype:** SCRIBE (spec)

```json
{
  "project": "NFRA_IAMROLES202609",
  "directive": "D12",
  "fabric": "site-z",
  "prd_version": "v0.1",
  "step": 4,
  "brief_ref": "docs/briefs/nfra-iamroles202609-least-privilege-brief-20260909.md@1a90986047",
  "endpoint_outcomes": [
    "FWD-1",
    "FWD-2",
    "FWD-3",
    "FWD-4",
    "FWD-5",
    "FWD-6",
    "FWD-7",
    "FWD-8"
  ],
  "status": "RATIFIED"
}
```
*PRD_HEADER block (`org/standards/PRD_HEADER.schema.json`; limb 5 of `.tools/to-pipeline-gate.py`).
`status: RATIFIED` because every outcome's `DONE WHEN` was confirmed by Andrew in one word. L5 may
begin on this header.*

**Commissioning (Andrew-direct 2026-09-09, VERBATIM):** *"Also in NFRA_OPSEC202609, is there anything
there for assessing all IAM roles and making sure we are properly adhering to least privilege?"* --
answered NO on measurement (brief F1), which is what produced this project rather than an amendment
to that one.

---

## ENDPOINT (step 2, /endpoint --forward)

*Phase 0 output, pasted VERBATIM from the L2 deliverable. `FWD-n` ids are PERMANENT and never reused;
a retired outcome leaves its number vacant. `DONE WHEN` is the BAR, not the current state. ACCEPT
lines are plain English and disputable, by rule, and carry no technical language.*

```
  FWD-1  Someone can state our least-privilege posture with a number, what it is
         out of, and when it was taken
         DONE WHEN  EXERCISED -- a reviewer has actually answered the question with
                    that evidence attached, rather than an opinion
         ACCEPT     Asked "are we following least privilege?", someone answers with
                    how many things were checked, out of how many exist, and as of
                    when. "Nobody has measured it" stops being the honest answer.
         SOURCE     brief Part I, O1; Part II Owns (the over-grant question, its
                    census and its coverage). Today the coverage is zero of 208

  FWD-2  For any role, a reviewer can see which of its permissions it has never used
         DONE WHEN  EXERCISED -- real roles have been read and their unused
                    permissions named, over a stated lookback
         ACCEPT     Pick any role. A reviewer can see which of the things it is
                    allowed to do it has never actually done, and over what period
                    that was judged.
         SOURCE     brief Part I, O2. ⚠ This is the PERMISSION grain, and F5
                    (corrected) establishes it is the half that is NOT built -- the
                    role-level half already is

  FWD-3  For any policy, a reviewer can see what it REQUIRES of the caller, not only
         what it lets them touch
         DONE WHEN  EXERCISED -- at least one real policy has been surfaced as
                    perfectly scoped and yet requiring nothing of whoever calls it
         ACCEPT     A rule that is careful about WHAT someone can touch but asks
                    NOTHING about who they are or how they proved it is visible as
                    such. Being tightly scoped stops being able to hide asking for
                    no second factor.
         SOURCE     brief Part I, O3; the exhibit is F8. ⚠ Part VII item 5 bounds it:
                    that the estate is broadly silent on this axis is an INFERENCE
                    from ONE policy, never a measured population claim

  FWD-4  Every role we run is either written down in our code or is a recorded,
         owned exception
         DONE WHEN  APPLIED -- each one is either in code or carries a named owner
                    and a reason
         ACCEPT     There is no role running that nobody wrote down and nobody
                    decided to leave out. Something deliberately kept outside the
                    normal way of doing things says who decided that and why.
         SOURCE     brief Part I, O4; Part II Owns. F2/F3: 16 of 208 are governable
                    and undeclared, and are therefore invisible to every check that
                    reads our code
         BOUND BY   brief Part II -- these are TWO remedies, not one. Whether a role
                    should be in code at all is a different question from whether it
                    is over-granted, and a single cell doing both will do one badly

  FWD-5  An engineer can narrow a permission and know beforehand what it would break
         DONE WHEN  EXERCISED -- a real narrowing has been checked in advance and
                    the check was believed
         ACCEPT     Before anyone takes a permission away, they can find out what
                    would stop working -- and be right. Nothing breaks because we
                    tidied up.
         SOURCE     brief Part I, O5; the named failure mode at
                    docs/doctrine/CONTROLS_OVER_CARE.md:512. F11: the live-plane
                    instrument for this already exists

  FWD-6  Anyone can tell whether a past clean-up actually happened
         DONE WHEN  EXERCISED -- each of the known past plans has been established
                    as done or not done, on evidence
         ACCEPT     For work someone planned months ago, a reader learns whether it
                    was finished -- and does not have to guess from which folder the
                    document is filed in.
         SOURCE     brief Part I, O6; F10 -- three such plans exist with unknown
                    status, one of them untouched since February

  FWD-7  A reviewer can tell "this is unused" apart from "we cannot see whether it
         is used"
         DONE WHEN  APPLIED -- the assessment reports the two differently, at
                    permission grain
         ACCEPT     Something nobody has looked at never reads as something that was
                    looked at and found clean.
         SOURCE     brief Part I, O7 (AMENDED at @39b106d036)
         ⛔ DO NOT CUT AS GREENFIELD -- HALF OF THIS IS ALREADY BUILT. The existing
                    tool's own self-test already asserts that never-used is not the
                    same as cold, and it carries an explicit UNKNOWN band, on the
                    ROLE axis. A cell written as new work would re-buy passing,
                    self-testing code. What is missing is the same discipline at
                    PERMISSION grain

  FWD-8  The assessment can be re-run without doing it by hand again
         DONE WHEN  EXERCISED -- it has actually been re-run and produced a
                    comparable answer
         ACCEPT     Someone can ask the same question next quarter and get an answer
                    they can put beside this one. It does not quietly stop happening
                    because only one person knew how to do it.
         SOURCE     brief Part I, O8; F4 -- the closest existing thing is explicitly
                    marked as not schedulable
```

---

## 1. Purpose -- what DONE means

**A reviewer can state, with a number and a vintage, how close this estate is to least privilege --
and for any single role can see which of its permissions have never been used, what its policies
REQUIRE of a caller, whether anyone wrote it down, and what would break if it were narrowed.**

The brief's own framing (F4) is the thing to hold onto: **the tooling is pointed the other way.**
The estate can answer *what is this role allowed to do* from documents all day. It cannot answer
*what does this role actually use*, and least privilege is a question about the gap between those
two. This project closes the gap and leaves behind an assessment that can be re-run.

---

## 2. Territory -- what this owns, and what it only relies on

**OWNS, ENUMERATED (the DECLARED DOMAIN for rule 24(i); the brief's Part II Owns cell, split into
its four clauses and numbered so a MECE check can be RUN against it rather than asserted):**

1. **The over-grant question across the IAM estate** -- the INSTRUMENT.
2. **The over-grant question's CENSUS** -- the population and the number.
3. **The over-grant question's COVERAGE** -- what the number counted out of, and what it could not see.
4. **The CONDITION AXIS** -- what a policy REQUIRES of a caller, not only what it scopes.
5. **DECLARED-vs-LIVE role reconciliation.**
6. **The GOVERNANCE DISPOSITION of undeclared roles** -- a separate remedy from (5), per `D6`.
7. **COMPLETION EVIDENCE for historical least-privilege remediations.**

*Items 1-3 are the brief's single clause "the instrument, the census, and its coverage" split into
three, because they are three different engines with three different failure modes and the brief's
own F-numbers separate them.*

STOP: **AND THE DOMAIN AS THE BRIEF STATES IT DOES NOT COVER TWO RATIFIED OUTCOMES. This is a real
uncovered-member finding and it is recorded rather than smoothed over.** Running rule 24(i) forward
from the Part II Owns cell:

| Outcome | Rides an OWNS item? |
|---|---|
| `FWD-1` posture number | YES -- (2) + (3) |
| `FWD-2` unused permissions per role | YES -- (1) |
| `FWD-3` condition axis | YES -- (4) |
| `FWD-4` every role in code or exempt | YES -- (5) + (6) |
| **`FWD-5` narrow-and-know-what-breaks** | **NO -- Part II Owns names no such item** |
| `FWD-6` did a past clean-up land | YES -- (7) |
| `FWD-7` unused vs unobservable | YES -- (3), the coverage clause |
| **`FWD-8` re-runnable assessment** | **NO -- Part II Owns names no such item** |

**`FWD-5` and `FWD-8` are ratified outcomes with no OWNS clause behind them.** Both are genuinely
in-scope capabilities Andrew confirmed; the brief's boundary section simply did not enumerate them.
**THE DECLARED DOMAIN FOR THIS PRD IS THEREFORE THE UNION: the seven OWNS items above PLUS `FWD-5`
and `FWD-8` as items (8) and (9).** Surfaced to `4.0.0_SA_CRO~Z` so Part II can be amended at its
next touch if wanted; nothing waits on that, and the manifest below is MECE against the union.

8. **PRE-FLIGHT BLAST RADIUS for a narrowing** -- what breaks, known BEFORE the change (`FWD-5`).
9. **RE-RUNNABILITY of the whole assessment** (`FWD-8`).

**RELIES ON, DOES NOT OWN** (brief Part II, carried unchanged): request-path front doors, WAF, the
sentinel and the auto-block framework (`NFRA_OPSEC202609`); portal MFA enforcement
(`D12_PLATFORM_OPS`); `comp-iam`'s existing DESIRED-plane surfaces and its `simulate` mode (the
comp-tool build lane); the website IAM identity and its Terraform (`NFRA_WEBSITE`).

---

## 3. Acceptance properties

1. **EVERY NUMBER CARRIES ITS DENOMINATOR AND ITS VINTAGE.** A posture figure without what it counted
   out of, and when, is not an answer to `FWD-1`.
2. **UNUSED AND UNOBSERVABLE ARE NEVER THE SAME VALUE** (`FWD-7`). A grant nobody has looked at must
   not render as a grant shown to be clean.
3. **A SCOPE CLAIM IS DESIRED UNTIL EXERCISED** (`D3`). Everything read from a policy document is
   DESIRED; only a `simulate-principal-policy` battery moves it.
4. **A NARROWING IS PREDICTED BEFORE IT IS MADE** (`FWD-5`, `D5`). The project must not cause the
   `AccessDenied` it exists to prevent.
5. **THE ASSESSMENT IS RE-RUNNABLE BY SOMEONE WHO DID NOT BUILD IT** (`FWD-8`).

---

## 4. Out of scope

- **`NFRA_OPSEC202609`'s nineteen outcomes.** Consumed, never amended; its four narrow
  least-privilege cells stand as done and are **inputs, not coverage** (`D7`).
- **Minting any alert, alarm, monitor or notification.** The standing moratorium is armed. This
  project ASSESSES and REMEDIATES; findings land as gates or owned blocking items.
- **Retiring or narrowing anything serving live production without the estate's normal sign-off.**
- **Portal MFA enforcement**, the website IAM identity, and the request-path surfaces above.

---

## 5. Constraints that BIND the decomposition

- **`C-EXTEND-NOT-BUILD` (`D2`/`D4`, Andrew ruling 20).** `comp-iam-usage` is BUILT, tracked,
  executable and self-testing. The instrument direction is **EXTEND to permission grain**, never
  greenfield. **A cell written as a build re-buys working code.**
- **`C-ANALYZER-PRICED-FIRST` (`D4`).** AWS Access Analyzer is the FALLBACK, not the plan. **No
  per-role price has been read by anyone.** If it is ever taken off the shelf, pricing it is the
  first act -- and that is a VENDOR call requiring Andrew's explicit word, never an inherited
  assumption.
- **`C-TWO-REMEDIES` (`D6`).** The 16 undeclared roles are a GOVERNANCE question and a PERMISSIONS
  question. **They do not move together, and one cell doing both will do one of them badly.**
- **`C-NO-ACCESSDENIED` (`D5`).** `CONTROLS_OVER_CARE.md:512` names the failure mode. This constrains
  HOW grants are narrowed and is a design input, not a sequencing note.
- **`C-DESIRED-UNTIL-EXERCISED` (`D3`).** Every scope claim in the brief is read from a document.
- **`C-COVERAGE-OVER-COUNT`.** `FWD-7` outranks `FWD-1`'s tidiness: a smaller number that states what
  it could not see beats a larger one that does not.

---

## 6. Rulings that BIND

- **2026-09-09, Andrew-direct:** the project exists and sits in D12 -- *"Ok we will make a project
  NFRA_IAMROLES202609 underneath D12"*.
- **2026-09-09, Andrew-direct (ruling 19):** *"process the infra report brief first"* -- ordering,
  discharged at L2.
- **2026-09-09, Andrew-direct (ruling 20, discharging ruling 18):** EXTEND `comp-iam-usage` to
  permission grain; Access Analyzer is the fallback. **Instrument direction only -- it authorises no
  build and cuts no cell.**
- **2026-09-09, Andrew-direct:** *"that is a D12 project as well but it comes behind the others"* --
  the sequencing, now satisfied.
- **2026-09-09 ~22:3xZ, Andrew-direct:** **"Confirm on IAMROLES202609."** All eight `DONE WHEN` bars
  RATIFIED. This is the gate that released L3 and L4.

---

## 7. Sequencing input for the L5 lane (not a dispatch)

**`FWD-2` IS THE ROOT.** The permission-grain instrument is what every other number leans on:
`FWD-1`'s posture figure is a rollup of it, and `FWD-7`'s unused-vs-unobservable distinction is a
property of its coverage. **Nothing that quotes a permission-level number can be graded before it.**

**`FWD-4` AND `FWD-6` ARE INDEPENDENT ROOTS and should not idle behind `FWD-2`.** Declared-vs-live
reconciliation runs off `comp-find --corpus aws`, which is REPAIRED and re-exercised (`D1`), and the
three historical remediation plans (`F10`) can be established as landed-or-not with no instrument
work at all. **Reading `FWD-2`-first as "nothing else may start" would idle two lanes for a round.**

STOP: **`FWD-5` IS THE ONE WHERE THE BAR IS DOING REAL WORK.** Its `DONE WHEN` is EXERCISED for a
stated reason: a pre-flight check never run against a real narrowing is indistinguishable from one
that always answers *"nothing breaks"* -- and the failure it exists to prevent is an outage this
project would have caused itself. **`APPLIED` would let the project ship the exact thing it was
commissioned not to do.**

**The 16 undeclared roles are a SETTLED SET, not just a settled count** (`F2a`): 16 of 208, corroborated
across two substrates and re-measured at the merged head (`216 hit(s) / 216 aws node(s)`,
`DECLARED=200 LIVE-no-DECLARED=16`). `C-TWO-REMEDIES` governs how they are cut.

---

## 8. SURFACE MANIFEST (step 4 -> step 5) -- one row per ENGINE

**Contract** (as adopted @`ecaa7c7dcb`, ETFS_GUARDRAIL s.7, and used by `NFRA_OPSEC202609` s.8 and
`NFRA_REPORT` s.8): `claim` is about the SURFACE ADDRESS and takes the five-value basis vocabulary
`absent | unmeasured | held | inferred | measured` (`.tools/substrate-card-check.py` `BASIS_RANK`;
every legal transition is a rank increase, and `verify` is the act that moves `absent`/`unmeasured`);
`verb` is the contract enum `port | classify | wire | align | retire | verify`; `outcome` = `FWD-n`;
`accept` = the section 3 acceptance-property number; `depends_on` = row ids; `bound` = the constraint
the cell may not cross.

**Provenance, read before citing any cell.** Every `measured` evidence cell is the L1 BRIEF's
measurement at `@1a90986047` (`4.0.0_SA_CRO~Z`, 2026-09-09) unless it names another seat. **Nothing
in this table was re-measured at L4**; the brief's `F<n>` ids are cited so the L5 battery re-grounds
each cell at its own vintage. `absent` rows are outcomes with nothing built.

**Domain (postulate i):** the section 2 **OWNS** cell, NINE enumerated items -- the brief's four
clauses split into seven, PLUS items (8) and (9) for the two ratified outcomes Part II Owns does not
enumerate. **MECE is RUN below, not asserted.**

| id | outcome | surface (engine) | claim | MEASURED-BY / evidence | lane | verb | depends_on | accept | bound |
|---|---|---|---|---|---|---|---|---|---|
| S1 | FWD-2 | The PERMISSION-GRAIN usage instrument -- for a given role, which granted permissions have never been used | measured | brief F5 (CORRECTED): `.tools/comp-iam-usage` is BUILT, tracked, executable, self-test passing -- and answers the ROLE axis (`role-cold`), not the PERMISSION axis. F4: the estate's tooling is pointed at what a role MAY do, never what it DOES | iam lane | port | -- | 1, 3 | `C-EXTEND-NOT-BUILD` (ruling 20) -- EXTEND the working tool; **a cell written as greenfield re-buys working code**. `C-ANALYZER-PRICED-FIRST`: Access Analyzer is the FALLBACK and pricing it is a VENDOR call at Andrew |
| S2 | FWD-1 | The POSTURE NUMBER -- one figure for the estate's least-privilege standing, carrying its denominator and its vintage | absent | brief F2: 208 roles is the population and the limit on the number; brief Part I O1 requires a PRINTED denominator and a vintage | iam lane | wire | S1, S3 | 1 | a rollup of S1 and NOTHING ELSE; `C-COVERAGE-OVER-COUNT` -- a smaller number that states what it could not see beats a larger one that does not |
| S3 | FWD-7 | The COVERAGE vocabulary -- `unused` rendered distinctly from `unobservable`, at the grain the claim is made | absent | brief F7: AWS's native unused-access finder is STILL not enabled, measured the same day; F5's `UNKNOWN` band is the existing seed | iam lane | wire | S1 | 2, 5 | **a grant nobody looked at must NEVER render as a grant shown clean.** This outranks `FWD-1`'s tidiness |
| S4 | FWD-3 | The CONDITION AXIS reader -- what a policy REQUIRES of a caller (MFA, source, tags), not only what it scopes | absent | brief F8: least privilege has TWO axes and the estate measures ONE. The exhibit is F8's own worked policy | iam lane | wire | -- | 3 | bounded by brief Part VII item 5; `C-DESIRED-UNTIL-EXERCISED` -- read from a DOCUMENT, so DESIRED until a simulate battery runs |
| S5 | FWD-4 | The DECLARED-vs-LIVE RECONCILER -- which live roles exist in code and which do not | measured | brief F2a: **16 of 208 undeclared is a SETTLED COUNT AND A SETTLED SET**, corroborated across two substrates and re-measured at the merged head (`216 hit(s) / 216 aws node(s)`, `DECLARED=200 LIVE-no-DECLARED=16`); F3: the 16 are invisible to the estate's own analysis | iam lane | verify | -- | 1 | `D1` is RESOLVED -- `comp-find --corpus aws` works and carries its VINTAGE. **`C-TWO-REMEDIES`: this row RECONCILES only; it does not dispose** |
| S6 | FWD-4 | The GOVERNANCE DISPOSITION of undeclared roles -- for each, in-code or a recorded, owned exemption | absent | brief Part II Owns (the disposition clause); F9: the instance is discharged and the CLASS re-arms on onboarding | iam lane | classify | S5 | 1 | ⛔ **`C-TWO-REMEDIES` (`D6`) -- governance and permissions DO NOT MOVE TOGETHER. This row is SEPARATE from S1 by contract, and one cell doing both will do one of them badly** |
| S7 | FWD-6 | The HISTORICAL REMEDIATION completion evidence -- did a past least-privilege clean-up actually land | absent | brief F10: **THREE prior remediation plans exist with UNKNOWN status** | iam lane | verify | -- | 1 | landed-or-not on the ARTIFACT, never on the plan document's own say-so; `C-CLOSED-RECORD` -- a closed record is a snapshot, not an oracle |
| S8 | FWD-5 | The PRE-FLIGHT BLAST RADIUS -- what a narrowing would break, known BEFORE the change | absent | brief F11: **the APPLIED-plane instrument already exists**; `D3`: no `simulate-principal-policy` battery has been run | iam lane | wire | S1, S4 | 4 | ⛔ `C-NO-ACCESSDENIED` (`D5`, `CONTROLS_OVER_CARE.md:512`) -- **the project must not cause the outage it exists to prevent.** `FWD-5`'s bar is EXERCISED for this reason and APPLIED would defeat it |
| S9 | FWD-8 | The RE-RUN HARNESS -- the whole assessment repeatable by someone who did not build it | absent | brief F4: the closest existing thing is explicitly not this; Part I O8 | iam lane | wire | S2, S3 | 5 | reruns must produce a COMPARABLE answer, so the denominator and vintage of S2 travel with it; build-ladder rung 2 -- compose the existing comp-tools, do not mint a runner |

**MECE, BOTH DIRECTIONS, RUN RATHER THAN ASSERTED (at this edit):**
- **FORWARD -- every OWNS item has at least one row:** (1)->S1 - (2)->S2 - (3)->S3 - (4)->S4 -
  (5)->S5 - (6)->S6 - (7)->S7 - (8)->S8 - (9)->S9. **9 of 9 covered, 0 uncovered.**
- **BACKWARD -- every row maps to an OWNS item and to exactly one outcome:** 9 rows, 0 orphans.
- **OUTCOME COVERAGE:** `FWD-4` is served by **S5 and S6** (two rows, one outcome -- mandated by
  `C-TWO-REMEDIES`); every other outcome by exactly one row. **8 of 8 outcomes carried, 0 uncovered.**

⭐ **AND NO ROW SERVES MORE THAN ONE OUTCOME. THAT IS DELIBERATE AND IT IS THIS SESSION'S LESSON
APPLIED.** `NFRA_REPORT`'s row `S1` named two outcomes (`FWD-2`, `FWD-4`); its cell mirrored the row
BY ID, cut only one half, and **L6's coverage limb passed "12 of 12" because it compares row IDS**
(ARMED row `NFRA_REPORT-Z-S1`, `2.0.0_SA_COO~ZZ`). **A coverage check scoped to the KEYS cannot see
a defect in the VALUES.** A one-outcome-per-row manifest makes that partial cut impossible to hide,
so the id-scoped check the fabric already runs becomes sufficient here.
⚠ **The reverse -- TWO rows serving ONE outcome (S5/S6 on `FWD-4`) -- is the SAFE direction** and is
required by `D6`: each row is independently cuttable and neither can be silently half-served.

⚠ **THE 9-AND-8 IS A MEASUREMENT AT THIS EDIT, NOT AN INVARIANT.** `NFRA_OPSEC202609` asserted a
bijection in a heading and it went FALSE with nothing able to fail -- prose cannot fail. A surface
needing two acts across rounds is normal. **What L5 must preserve is COVERAGE IN BOTH DIRECTIONS and
the ONE-OUTCOME-PER-ROW property**, never the counts.

**What this manifest does NOT assert:** that every row is buildable as written -- `S8` depends on a
simulate battery nobody has run (`D3`); that the `lane` column is a seat assignment (it is a lane;
no COO is seated on this project yet); or that `absent` means unexamined -- every `absent` row names
what was measured about the CURRENT state's failure to serve it.
