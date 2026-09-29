# CUTOVER REVIEW -- AMGT scoped-api no-span HOLD repair -- **PRE-PAIR VERIFICATION. ACCEPTANCE WITHHELD.**

- **Reviewer:** `3.0.0_SA_CVO~Z`
- **Act under review:** deploy the runtime no-span HOLD repair to the `opal-amgt-scoped-api` Lambda.
- **Date:** 2026-09-23.
- **Verdict:** **NOT ACCEPTED -- and NOT REFUSED.** This seat's cutover review sits **AFTER** the
  CTO+COO never-widen pair by its own narrowing, and the pair is **INCOMPLETE**. What follows grades
  the **CTO half only**, so that when the COO half lands this review is one read away rather than a
  cold start.

---

## 1. WHY THIS IS NOT AN ACCEPTANCE, STATED BEFORE THE GRADES

`2.0.0_SA_COO~Z` **DECLINED** to sign the pair half (and found the rollback defect while declining --
recorded in the CTO half's amendment 2). Andrew has approved that seat signing, but that approval is
**AUTHORIZED, NOT ACTIVATED**: it must reach `2.0.0_SA_COO~Z` as a **direct operator instruction in
that seat's own Codex session**, and **a broker relay cannot close a session-level restriction.**

**So the blocking act is Andrew's, not this seat's and not the CTO's.** Until the COO half is on
file, this seat's acceptance is **WITHHELD**, and withheld is **`NOT_EVALUATED` on the act** -- never
an implied pass. This seat's review is **IN ADDITION** to the pair and never in place of it.

---

## 2. THIS SEAT'S FOUR-ITEM CHECKLIST, GRADED AGAINST THE CTO HALF AT HEAD

Object: `org/critical_paths/change_management/20260923T1735Z_amgt_scoped_api_nospan_hold_repair_NEVERWIDEN_CTO_HALF.md`,
read at HEAD `1b1244cecf` (body + amendment 1 + amendment 2 @ `3b4083a685`).

| # | item | grade |
|---|---|---|
| 1 | **rollback does not restore the incident** | **MET** |
| 2 | **both branches covered, FAIL CLOSED as default** | **MET** |
| 3 | **writer count PRINTED** | **MET** |
| 4 | **blast radius at the ARTIFACT grain** | **MET** |

**Item 1.** Amendment 2 **WITHDRAWS** section 4's unconditional "ONE key, single redeploy". The
revert branch is explicitly **NOT pre-authorised**, because the old package *is* the defective one
and restoring it re-serves the 179 held sentences. The availability-versus-contract trade is
deferred to **Andrew's contemporaneous call**. That is the correct disposition: a rollback that
re-deploys the defect is a second deployment of the defect.

**Item 2.** Section 3 covers both producer branches read from the producer's own rule -- span
present -> **serves, 210**; no span -> **HELD, 179**, zero no-span output; `210 + 179 = 389`
reconciles to the historical census. Amendment 2 adds the default this seat required:
**FAIL CLOSED, NEVER FAIL OPEN** on any observed failure, with the fail-closed response being
disable-or-error the affected route, not a revert.

**Item 3.** Section 1 prints N **per writer class** with its denominators (126 deployed Python files,
3 matching; 3900 candidate lib/infra files, 16 matching) **and a ZERO-PARSE-FAILURES coverage
control** -- which is the load-bearing half, since an unparsed file is invisible to an AST census and
a census with unparsed files cannot support an N at all. N resolves to **ONE enforcement point that
both production consumers cross**, so the repair sits on all emitting paths.

**Item 4.** Amendment 1 binds the half to an **artifact identity, not a description**: candidate ZIP
sha256 `0c44108821fe52850c77b119490039453b082c3639fae6dbf58de054b1397a55` at packet pin
`dd91fd3126`, with "any other bytes are OUT OF SCOPE". The half says so itself, and its own
`225`-versus-`227` test-count drift is the demonstration: a description ages, a content hash does
not.

---

## 3. AND ONE CHECK ON A **DIFFERENT INSTRUMENT**, BECAUSE A RE-READ OF THE SAME DOCUMENT IS REPETITION

Rule 22: *a second seat's confirmation via the FIRST seat's method is REPETITION, not corroboration.*
Sections 2's grades are all reads of the CTO's own record. So the load-bearing figure was
**re-derived from the artifact**, not from any seat's report of it:

| artifact (`C:/tmp/amgt-r-no-span-package-20260923/`) | this seat's own sha256 | record's value | verdict |
|---|---|---|---|
| `candidate.zip` (807,904 bytes, **197 members**) | `0c44108821fe52850c77b119490039453b082c3639fae6dbf58de054b1397a55` | identical | **MATCH** |
| `rollback.zip` (807,553 bytes, 197 members) | b64 `r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w=` | = `before_code_sha256_base64` | **MATCH** |

**Two things follow that the document alone could not establish:**

1. **The artifact the signature covers still exists AT THOSE BYTES and has not been rebuilt.** This
   is the check amendment 1 exists to make possible, and it is the one that would catch a
   same-description, different-artifact substitution.
2. **`rollback.zip` IS the defective deployed package** -- its sha256 equals the recorded
   `before_code_sha256_base64`. **So amendment 2's defect claim is corroborated on evidence the CTO
   did not produce**, rather than accepted on its author's word.

**Also cross-checked, cheaply:** the record's base64 and hex forms of the candidate hash decode to
each other (`REPAIR_PACKAGE.json` carries both; they agree). A pair of encodings that disagreed
would have made every downstream citation ambiguous.

### SCOPE LIMITS OF THAT CHECK, STATED

- **Both ZIPs are DEVICE-LOCAL** (`C:/tmp/...`, outside the repo). This confirms the **candidate**
  artifact, not the **deployed** one. **Nothing here reads the live Lambda**, so `before` is a
  repo-record claim at this moment, not an EXERCISED one.
- `197 members` and `changed_members: ["lib/research/api/scoped_amgt.py"]` are read from
  `REPAIR_PACKAGE.json`; this seat verified the **member count** independently and did **not**
  re-run the per-member AST comparison.
- **DESIRED / APPLIED, never EXERCISED:** the repair is **NOT DEPLOYED**
  (`"deployment": "NOT EXECUTED"`). Every 210/179/0 figure is a **REPLAY** against retained S3
  versions, not served behaviour. No claim here reaches the served plane.

---

## 4. WHAT THIS SEAT WILL DO WHEN THE PAIR COMPLETES, AND WHAT IT WILL NOT

**On the COO half landing**, this seat re-reads the pair at its then-bytes and issues the cutover
verdict. **It will re-read the candidate ZIP's sha256 at that moment** -- the check in section 3 is
perishable, and a rebuild between now and the deploy voids this signature by amendment 1's own terms.

**NOT_EVALUATED here, and not silently:** the COO half (not on file); the deploy itself (not
executed); the 12 retained drafting objects, which the CTO half **explicitly excludes** as a separate
act needing its own pair; **raw-D1 evidence-input posture**, carried forward and expressly not
claimed repaired; and **human viewing of the served sentences**, which remains UNMEASURED and which
no artifact read can settle.

-- `3.0.0_SA_CVO~Z`, 2026-09-23.
