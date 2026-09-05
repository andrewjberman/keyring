# COO~Z session log 00:00-05:10Z -- eleven of eighteen served, and five criteria I wrote could not have been satisfied

**archetype:** COORDINATE
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Seat:** `2.0.0_SA_COO~Z` - **Project:** `NFRA_OPSEC202609` (D12, site-z) - **Limbs:** L5 decomposition + L6 task orders - **Lanes held:** 7 (`~S ~T ~U ~V ~W ~X ~Z`) - **Push state: LOCAL at close, not read against origin** (integration window is the integrator's).

---

## 1. WHERE THE PROJECT STANDS

**ELEVEN OF EIGHTEEN ENDPOINT OUTCOMES SERVED**, computed from the decomposition's own cell states rather than recalled: **FWD-1, 2, 3, 5, 6, 7, 8, 9, 11, 16, 18.**

**PARTIAL (3):** FWD-14, 15, 17 -- the sentinel chain. **NOT YET (4):** FWD-4, 10, 12, 13.

**Cell census: 35 cells -- 19 COMPLETE, 8 HELD, 5 OPEN, 3 CLOSED. Zero cells out of step with their face** (reconciliation re-run at 04:1xZ; the one drift it found, `OP-s-28`, is described in §3).

**BLOCKED ON ANDREW, four items, all of which I put to him as cards and he approved the recommendations on ("Recs approved", ~03:4xZ, recorded verbatim @`097481d310`):**
1. **The SNS confirmation click.** The alarm subscription exists but AWS creates it `PendingConfirmation` -- **until he clicks, the alarm still reaches nobody**, which is the exact state `OP-s-6` was held for.
2. **One GoDaddy validation CNAME**, then ACM issues and the certificate half of FWD-13 unblocks.
3. **Which `/wp-admin` address.** The lane derived candidates and did NOT apply them -- his approval authorised *derive and bring back*, not *apply*.
4. **The apex decision** (migrate the zone to Route53 vs serve on `www` with a redirect). **I gave no recommendation, so his approval selected nothing here.**

**AT L4 (`1.0.0_SA_CTO~Z`), not blocking:** C-4's premise (the partner allow list is unbuildable -- see §2), and C-2's wording (see §3).

---

## 2. THE MEASUREMENT THAT MOST CHANGED THE PROJECT

**The partner allow list cannot be built, and the reason is us.** `0.7.0_AE_CloudOps~U` measured the only window of sign-in traffic that exists: 695 events on `/auth/login` from exactly 3 addresses over 15.06 hours, `recordsScanned == recordsMatched == 2771`.

⛔ **680 of 695 -- 97.8% -- carry this project's own probes in the User-Agent.** A second independent axis agrees: 679 of 695 fall in the two 30-minute bins containing `TO-OP-S-7`'s own ledger burst. **Two axes, same answer -- corroboration, not a re-run.**

**So a list built from that window would have entered the fabric's own egress address as a partner firm** -- a permanent edge allow rule admitting our own infrastructure under a partner's name, justified by a census correct at every step. **Nothing was built.**

⭐ **THE REUSABLE SHAPE: A PROJECT THAT INSTRUMENTS A SURFACE CONTAMINATES THE TRAFFIC IT LATER NEEDS TO MEASURE THERE.** 695 events over 15 hours on a live auth path looks entirely reasonable; nothing would have prompted the check.

**Consequence: `OP-s-14`'s BLOCK arm is HELD on a CHAIN, not a queue** -- no clean window -> no allow list -> no C-4 -> no BLOCK arm. Written into the cell so nobody reads WATCH-only as work someone forgot.

---

## 3. THE DEFECT CLASS THAT DOMINATED THE NIGHT: A CHECK SCOPED TO ONE PLANE CERTIFIES THE OTHER CLEAN

**`Z-S136` is the sharpest instance and it is the finding of the session.** `addresses = []` on the WAF IP sets **does not mean "Terraform does not manage addresses" -- it means Terraform DECLARES them empty and enforces that on every apply.** An unscoped plan was measured **queued to delete a live entry**, on any apply of `portal-auth` or `opal-gateway`, by any operator, for any unrelated reason, silently.

⛔ **AND NO PRINCIPAL CENSUS COULD EVER HAVE FOUND IT.** `TO-OP-S-22` simulated **231 principals** and proved only the reconciler holds `wafv2:UpdateIPSet`. **That verdict is true and was worthless here: Terraform writes through principals already counted, and the second writer is the DECLARATION, not an identity.** C-2 was verified on the principal plane and broken on the declaration plane. Repaired @`3758b14afc`, 4 of 4 sets, verified at HEAD; **`S15-AC5` is not discharged until the guard is exercised against a POPULATED set.**

**Related instances the same night:** the third live grant on `opal-users` (two roots, not one); the IP sets being **four, not two**; `OP-s-28` complete in its face and `OPEN` in its cell with **nothing in the fabric comparing the two**.

---

## 4. FIVE CRITERIA I WROTE THAT COULD NOT HAVE BEEN SATISFIED

Recorded together because the pattern is mine, not the lanes':

| criterion | why it could not pass | found by |
|---|---|---|
| `TO-OP-S-15-19` GO condition | demanded `TO-OP-S-22`'s verdict, which verdicts roles only that face creates -- **the two faces named each other** | `~W`, stopped before starting |
| `S15-AC3` | "only the reconciler's role" over a population that necessarily includes account administrators | `~T`, 231 principals |
| `S13-AC2`'s condition | a status-code test on XML-RPC, which **returns 200 on failed auth** | `~U` |
| `S9C-AC4` as I amended it | "observe on each function's own trigger cadence" for functions with **no cadence** | `~X`, stopped before acting |
| `S23-AC3` | iterates over an allow list that does not exist; its own *"zero is a fine answer"* clause **pre-blesses the vacuous pass** | `~U`'s commissioned sweep |

⭐ **The sweep that found the last one read 62 of 62 criteria across 11 of 11 open faces and returned ONE new finding.** Its generalisation is the one I want carried: **a cell going HELD silently makes every downstream criterion vacuously satisfiable, and nothing checks for that.**

**Three further errors of mine, all self-disclosed at the time:** citing row `Z-S111` before minting it (it was another seat's); a commit message asserting it contained a row my script had failed to write; and **taking `Z-S124`'s POSITIVE CONTROL for its SUBJECT**, which put two wrong instrument traps into a face -- a wrong-object join from two adjacent sentences in one summary.

---

## 5. WHAT THE LANES DID THAT I WANT REPEATED

- **`~W`** enumerated permission pairs **before any role existed** -- catching that the IP sets were four, not two, at zero cost. Then found `Z-S136` while taking an unrelated baseline, **and volunteered that its own IAM verdict could not have caught it.**
- **`~T`** simulated **all 231 principals** rather than filtering policy documents for `wafv2`. ⭐ **The cheap census would have returned exactly ONE holder and CONFIRMED the criterion** -- the three admins' grant is an inherited wildcard no document scan matches.
- **`~X`** filed `Z-S130` **before acting**, owning that "seven LIVE lambdas" was its own attachment census wearing a liveness adjective. Later showed a **control table still present** beside a deleted one, so `ResourceNotFoundException` proved a deletion rather than a broken read.
- **`~U`** returned a **measured negative** twice and refused to substitute the fabric's own egress either time.
- **`~S`** confirmed a defect **in its own completed cell**, on a plane the finder could not reach, and neither committed nor reverted another lane's in-flight edit.
- **`~Z`** corrected my bar: an EC2 code deploy is not a `terraform apply`, verified at source. ⭐ *"There is no plan to read, because there is no apply -- that is the strongest possible form of 'it does not remove the block list'."*
- **`~V`** measured `Invocations` reading **ZERO on a Lambda@Edge function under 141,685 invocations**, which is the instrument a seat following my own ruling would have reached for.

---

## 6. COMPILER TOOLS

| tool | invocation | result |
|---|---|---|
| `proof-of-spec-check.py` | 6 instances validated at this seat with their expected id sets | PASS -- all VALID rc=0; never accepted a reported rc |
| `to-pipeline-gate.py` | `TO-OP-S-9D`, `TO-OP-S-10C` | PASS rc=0 |
| `surprise-row-gate.py` | every channel append | PASS after 3 schema corrections (`class`/`disposition` are closed enums; `grounding` is an object) |
| `channel-commit-guard.py` (mine) | every channel commit | **FIRED rc=3 once** -- caught a foreign row AND an id collision; the only reason a lost write was seen at all |
| `comp-find --corpus aws` | IP-set census | **MEASURED ZERO over 2103 nodes -- and WAFv2 IP sets are not a modeled class.** Taking it at face value would have left the faces asserting two sets with a census appearing to agree. Live plane used with a `# rail-checked:` marker. |
| `comp-find --files` | `aws_wafv2_ip_set` across roots | **4 roots, not the 2 reported** -- and `website/` has ZERO `addresses =` hits, so the bar did not spread past the defect |
| `comp-read --enumerate` | `addresses =` / `ignore_changes` per root | attribute-level confirmation the fix was present and **uncommitted** |

**Gap found:** `comp-find --corpus aws` cannot distinguish an unmodeled resource class from an absent one except by its own warning line. It states this honestly; a reader in a hurry will still take the zero.

---

## 7. CURRENT STATE AND NEXT STEPS

**In flight:** `~T` reconciler deploy + `S15-AC1/AC2/AC5` and the `S19` exercises - `~V` `TO-OP-S-10B` ledgered deploys - `~W` `TO-OP-S-10C` `AC3/AC4/AC5` (adoption landed **INERT**, live function byte-for-byte untouched) - `~Z` `TO-OP-S-12` gateway deploy, then the two-slot rotation exercise and a **5-caller observation window that is multi-session by construction** - `~X` sizing `Z-S127`.

**Owed by me:** route `Z-S127` to L4 **once sized** (does anything still validate against that cleartext `JWT_SECRET`, and who can read it) -- **I will not route a severity I have not sized.**

**Not startable by anyone:** `TO-OP-S-23`, gated on a month of accumulated WATCH rows, **before 2026-10-04**.

**[ANDREW]** the four items in §1. **[`1.0.0_SA_CTO~Z`]** C-4's premise and C-2's wording, both routed with measurements attached, neither blocking.
