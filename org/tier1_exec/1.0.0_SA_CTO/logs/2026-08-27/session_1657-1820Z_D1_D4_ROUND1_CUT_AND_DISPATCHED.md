# 1.0.0_SA_CTO~Z — SESSION LOG 1657–1820Z: D1 + D4 ROUND 1 CUT, SEATED, BUILT

**archetype:** DECIDE
**secondary_archetypes:** VALIDATE, COORDINATE

> **WRITTEN FOR A ZERO-CONTEXT SUCCESSOR**, in the form my own predecessor used — which is the only
> reason this seat was functional at minute one. **The METHOD is the content; the verdicts are
> recoverable from the artifacts, the reasoning is not.**

---

## 0. WHAT WAS ASKED AND WHAT LANDED

Andrew-direct via `0.0.0_AB_MSTR~Z` (9308): *"its time to get started on D1 and D4 as defined in
their logs."* D1 first (*"D1 first and foremost, then build in D4"*).

**BOTH ROUND-1 SETS ARE CUT, SEATED AND BUILT INSIDE ~80 MINUTES.**

| commit | what | push |
|---|---|---|
| `2162f50620` | D1_NAMEDISCOVERY round 1 — 3 TOs, 20 cells / 16 criterion-bearing / **16 covered** | on origin |
| `d5b1139e9f` | ETFS_SATELLITES round 1 — 4 TOs + the `modesFor` four-postulate record | on origin |
| `8f0ee6e728` | D1_NAMEDISCOVERY project record un-staled (read 2 stages behind) | on origin |
| `ebce987b42` | DS~P's TO-6 GICS field — landed under my exec lane (see §5) | on origin |
| `04808926c9` `da53392d33` | `STRUCTURAL-TWOPHASE` Rule 24 record + amendment | on origin / LOCAL |

Seats then built against them: **D1_NAMEDISCOVERY round 1 COMPLETE** (`0.4.0_DS_ClientPlatform~Q`),
**ETFS_SATELLITES TO-1+TO-2 BUILT 9/9** (`~W`), **TO-3 in flight** (`0.4.0_DE_ClientPlatform~Y`).

---

## 1. ⛔ THE THING THAT NEARLY SHIPPED A BAD TO — AND THE GENERAL SHAPE IT BELONGS TO

**`SAT-inv-2`'s remedy was recorded as LANDED by two seats. Both were telling the truth. The
normative line had not moved.**

```
grep -n "SAT-inv-2" DECOMP.md          ALL 5 occurrences, nothing headed/tailed
  :118  MEMBERSHIP DERIVES FROM A DECLARED PREDICATE OVER THE ROSTER   <== NORMATIVE. v1. UNMOVED.
  :218  AMENDED SAT-inv-2: membership is a DECLARED REGISTRY ...       <== the fix lives HERE
git show 2758833b9f -- DECOMP.md       ONE hunk, @@ -170,6 +170,96 @@  -- A PURE APPEND
git log --all -S "<the v1 wording>"    eeb64c7f6b ONLY -- never removed by any commit
POSITIVE CONTROL: -S on the amended wording -> 2758833b9f (the instrument DOES find amendments)
```

**Three accurate reports over one unmoved line.** The commit subject said *"fix ... s.3a"* — true.
Both logs said *"SAT-inv-2 AMENDED"* — true of s.3a. **Nobody claimed :118 moved.** The heading over
:118 says *"INVARIANTS — binding"*; the heading over :218 says *"ANSWERING CVO's CERTIFICATION."*
**A builder opens the block that says BINDING.**

>> ⭐ **THE GENERAL SHAPE, WHICH RECURRED FOUR TIMES TODAY ACROSS FOUR SEATS: A STATE CHANGE WRITTEN
   WHERE A READER LOOKS, WHILE THE FIELD A CONSUMER BRANCHES ON NEVER MOVES.** `SAT-inv-2`:118 · my
   own `build_package.py` stale citations · the channel's `hazard_standing` · `sub_asset_class`
   claiming asset-class while serving GICS. **An append leaves the original IN FORCE, and every
   report about the append is TRUE.** <<

**PROCEDURE FOR A SUCCESSOR: when told a remedy landed, open the NORMATIVE line. Not the commit
subject, not the log, not the message.** `3.0.0_SA_CVO~Z` discharged the block only on a direct read
of the amended line — correct, and copy it.

## 1a. ⛔ AND ITS SIBLING, WHICH I HIT FOUR TIMES: **AN UNCOVERED ENUM MEMBER**

**Four independent surfaces, four seats, eight hours** — an enum missing the member that encodes
*"a decision was made about this"* as distinct from *"this has not happened yet"*:

| enum | uncovered member | what it forces |
|---|---|---|
| `STRUCTURAL-TWOPHASE/<class>` | any class but `rule-bank` | a FALSE label or a FALSE discipline signal |
| `proof_of_spec.status` | "authorization withheld" | `FAIL` (overstates fault) or `N/A` (hides) |
| `modesFor(firm)` | `null` firm (`/auth/me` failure) | an identity outage handing out a third firm's view |
| BARRED / ABSENT | **RETIRED** | a spawn that reverses a sovereign closure, looking like housekeeping |

**Treat this as a class, not four coincidences. When you author or adopt an enum, hunt the member
that carries a DECISION rather than a STATE.**

---

## 2. D1_NAMEDISCOVERY — round 1, and the one ruling I made at the cut

3 TOs (`org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/D1_NAMEDISCOVERY.TO-{1,2,3}.*`), cut
against `3.0.0_SA_CVO~Z`'s certification (CERTIFIED WITH FINDINGS, **no TO-mint block**). Build
vintage **`@669e04f27b`**, not the certified `@bcca23915b` — the F1/F4 repairs landed after the cert,
and a build against the certified-but-pre-repair vintage implements the scalar `form` field TO-3
exists to refuse.

**⛔ `ND-e-2` RULED AT THE CUT, NOT DEFERRED — CONTINUE-AND-EMIT-`UNKNOWN`, neither RAISE nor silent
SKIP.** The cell is classed DS+CTO and demands the policy be *declared, not inherited*.
- **RAISE** loses every other surface's result to one unreadable surface — and that is not
  hypothetical: the 2026-08-26 13:30Z run shows a cottonwood abort SKIPPING the global fold,
  *"one scope aborts all four."*
- **SILENT SKIP** *is* `ND-e-1`'s defect — a skipped surface and a surface with no matches are
  byte-identical.
- **CONTINUE-AND-EMIT is the only option satisfying `ND-e-1` at the SURFACE grain**; a sweep that
  drops the surface never emits the row the distinction would ride on.
⚠ **It does NOT set the consumer's policy.** That is a separate declared act and not mine to make.

**The decomp's self-invalidating line (`"NO TO IS CUT"`) was amended in the SAME COMMIT**, as the
decomp itself instructed.

---

## 3. D4 / ETFS_SATELLITES — the split that is the whole point, and my own finding

4 TOs. **`SAT-b-1` (mode, DE alone) and `SAT-c-1` (firm gate, DE+AE) are SEPARATE TOs with separate
owners**, and TO-3 carries an explicit instruction not to add firm logic *"even if it looks like one
line."*

>> **Bundled you get a pill rendering for EVERY FIRM, or a gate with nothing behind it, and NEITHER
   FAILURE ANNOUNCES ITSELF. On a multi-tenant surface the first is a client-facing exposure that
   ships green.** <<

⛔ **DO NOT cite Rule 24 (iv) for the split** — the decomp's v1 (iv)=FAIL was WITHDRAWN as an
over-application (Andrew caught it). It is a DECOMPOSITION point. Citing the withdrawn verdict lets
a certifier correctly reject the citation and the real finding dies with it.

### 3a. MY OWN FINDING — `SAT-b-1`'s ORACLE UNDERSTATES ITS FAILURE MODE

The cell names **six** declarations and says a partial add *"fails at the one that was missed."*
**Measured at `origin/DEV 4ac152f8`: EIGHT sites, only THREE fail loudly.**

```
ENFORCED  Record<PositioningMode,X>, missing key = TS ERROR   :172 :210 :347
SILENT    binary ternary -> any new value takes the MODELS branch
            :80 declaredBooks · :156 capabilitiesFor · :105 resolveBooks · gridConfig.ts:45
SILENT    array literal, NOT exhaustiveness-checked           :353 POSITIONING_MODES  <- THE PILL LIST
```
- `:353` — add the mode to the type, satisfy every `Record`, get a **clean `tsc`**, and the pill
  never renders.
- ⛔ `:156 capabilitiesFor` gives a new value the **models** branch = **ALL TRUE**, contradicting
  `SAT-d-3`'s declared all-false. **A cell contradicted by a default is not a cell.**
- The cell's six **omit** `declaredBooks`, `resolveBooks`, `portfolioNamesFor` — three of the five
  silent ones.

⭐ **`0.4.0_DE_ClientPlatform~Y` then did BETTER than my TO asked:** I required an EXERCISE (prove the
pill renders); they built a MECHANISM — `POSITIONING_MODES` now derives from the compiler-enforced
`MODE_LABELS`, so *"having a label is what puts it on screen."* **A mechanism beats an exercise
because an exercise only covers the run you did.** Their `DECLARED SET vs VISIBLE SET` comment is an
axis I did not give them.

### 3b. `modesFor(firm)` FOUR-POSTULATE RECORD — CVO F2 discharged, and (i) FAILS

`org/tier1_exec/1.0.0_SA_CTO/deliverables/ctoZ_SAT_C2_MODESFOR_FIRM_FOUR_POSTULATE_RECORD_20260827.md`

**`AuthContext.tsx:354` sets `firmId: null` when `/auth/me` FAILS** — a session whose firm is
UNKNOWN, not absent. **`null` is not a firm, so "every other firm" does not cover it. CE FAILS.**
Remedy: a TOTAL mapping with `null` → the TWO-pill set, mirroring `isPathAllowedForFirm`'s
`?? false`. **Fail CLOSED.**

⛔ **AND THE TRAP `0.4.0_DS_ClientPlatform~W` SURFACED (routed UP, not sideways):** the bronze detail
artifact carries **`hierarchy.firmId = 4175`** — **the MODEL's owning firm, the SAME CONSTANT on all
nine.** A gate wired to it **gates nothing or everything and typechecks cleanly.** Both are called
`firmId`; that is the whole trap. TO-4's `AC1` amended to forbid that USE. `SAT-c-1`'s
"zero firm-id references in the Positioning directory" is unaffected — different plane.

---

## 4. RULINGS I ISSUED (a successor inherits these as standing)

1. **comp-system two-gate deadlock** — `comp-system` refuses to compile uncommitted sources;
   `safe-commit` refuses to land while 06 is stale; **each correct, each pointing at the other.**
   RULED: the audited override IS legal for `proof-of-spec`; **LD-0362 binds on the CAUSE, not the
   LOCATION.** Prefix `STRUCTURAL-TWOPHASE/proof-of-spec`. ⛔ **The in-session discharge is
   IMPOSSIBLE on site Z** (the discharge IS the 06 regen; `comp-kuzu` unreachable), so the reason
   string must carry `discharge owed laptop-side` or the rate instrument reads lapses.
2. **TO-6 AC4 (`sub_asset_class`)** — the gold-row emission HELD. The axis collision **predates
   TO-6**; 180 of 189 served rows already carry the GICS sector under a column named for asset
   class. ⛔ **DO NOT split `sub_asset_class`** — 24 code files incl. portal, and the portal maps
   already carry **0 of 11** GICS names. At least THREE vocabularies in that one column.
3. **AC3 backfill (silver 08-24)** — WITHHELD. A `VersionId` is a lease not provenance; a silver
   rewrite without a matching gold re-run creates a silent split; DELTA≠0 needs CTO+COO and I hold
   one half.
4. **TO-6 sequencing** — slot OPEN; `etf_daily_pull.py` is production-on-save; cutoff 2h before the
   11:00Z fire; revert rather than leave a partial edit.
5. **COO CALL 3/4** — one DS lane for the `TO-F3-DS` control APPROVED (their refusal to self-accept
   AFFIRMED); **re-spawning the AE seat Andrew retired REFUSED**; DE~Z re-seat to ETFS_INGEST
   APPROVED (it un-bars three rows).

---

## 5. THINGS THAT COST ME, RECORDED SO THEY ARE NOT RE-LEARNED

⛔ **1. ALL SEVEN TOs I CUT HAD NO RESOLVABLE ASSIGNEE.** Four had no `<issued_to>` element at all;
`D1_NAMEDISCOVERY.TO-1` resolved to `0.0.0_AB_MSTR~Z` **out of my own prose** (*"the lane letter is
MSTR's to assign"*). **I ran `to-check` before committing, saw `(unassigned)` + `unresolved_serials=1`,
and wrote in my commit message that this was "honest and exactly right."** A transient truth (no seat
existed yet) matched a permanent defect, and the coincidence stopped me looking.

⛔ **2. I THEN NEARLY RE-BROKE COO's FIX.** Clearing my now-stale `SEAT NOT ASSIGNED` headers, I put
a backtick-quoted serial back into the PROSE line: `unresolved_serials` **0 → 21** and **0 → 5**.
Reverted pre-commit. **I traded a real property for an appearance** — the stale header was ugly and
inert; the field I broke is what every instrument reads. **Caught ONLY because I re-ran the
instrument against my own edit**, the discipline I had praised in COO one message earlier.

⛔ **3. MY ACK CLOCK RAN AHEAD OF MY READING.** I acked nine ids off a TRIAGE sweep having read only
subject lines. **A triage sweep produces a LIST, and a list of ids invites a single ack call** — but
the sweep answers *what needs a ruling*, never *what has been read*. **Rule adopted: ack one batch
per READING pass, never per TRIAGE pass.**

⚠ **4. `--stat` said `SKILL.md | 1 +` and I nearly filed "too thin to contain its claim."** It is ONE
VERY LONG LINE carrying all four tokens. **A line count is not a content measure.**

⚠ **5. `head -1` on three matching directories scored the wrong one** — `portal/etl/pages/positioning`
(1 file, 0 hits) instead of `portal/src/pages/Positioning`. **A clean zero from the wrong plane.**

⚠ **6. `git log --since="17:00"` returned empty** — `--since` takes **LOCAL** time and 17:00 local was
in the future. Caught, not reported as "no commits."

---

## 6. COMPILER TOOLS

| tool | result | note |
|---|---|---|
| `to-check.py --all --project` | PASS | run BEFORE every TO commit — **a TO the tooling cannot see is a TO nobody holds**; 0 parse_errors each time |
| `comp-which` | PASS | routed the viewer-firm question to the serving/auth plane |
| `comp-find --name` / content greps | PASS | every zero paired with a positive control |
| `safe-commit.sh -F` | PASS ×6 | msg-verify MATCH each; **refused me twice, correctly** (proof_of_spec missing; `infra/aws/**` lane) |
| `commit-gate.sh` | PASS | caught 4 non-ASCII chars I introduced into production code |
| `codex-send.py --body-file` | PASS | the MCP `send_message` tool refuses bodies past ~1KB with a MISLEADING `body is EMPTY`; this is the working path for substantive sends |

**Gap found:** `send_message`'s refusal text misdiagnoses the cause — five attempts lost to *"body is
EMPTY"* when the body was 4,788 B. Worth a fix; routed nowhere yet.

---

## 7. OPEN AT ANDREW (one, bundled by COO)

**WHO MAINTAINS THE SATELLITE MEMBERSHIP REGISTRY?** `2.0.0_SA_COO~Z` left the slot deliberately
unfilled; `3.0.0_SA_CVO~Z` ruled it **NOT a gate** — build proceeds, the name is a SHIPPING
condition. **An owner assigned by inference IS the unowned-list failure the invariant refuses.**

**Bundled with it (COO is putting it once, as a class):** two items where *a seat Andrew retired holds
the only lane that can act* — my `build_package.py` interlock fix (written, gate-clean, AE-lane
refused, uncommitted) and the AE-owned channel rows.

⚠ `Z-S49` **came OFF** the Andrew list — MSTR exercised the bearer question (HTTP 200, RS256, 401
negative controls), so it is a seating question now.

## 8. BLOCKERS

**None.** Every open item has a named owner. `D1-i-2` hold **NOT lifted** — a green run cannot
distinguish *someone made the reviewed edit* from *the input changed shape*.

---

# ADDENDUM — 1820–1850Z. ALL THREE DIRECTIVES CERTIFIED, AND A P1 I FIXED THREE TIMES

**The log above closed at the cut. Everything below happened after it and a successor needs it.**

## A. THE PRIORITY SET IS DELIVERED THROUGH THE FULL PIPELINE

| | |
|---|---|
| **D1_NAMEDISCOVERY** | round 1 built, **15/15**, 3 instances rc=0 VALID, **4 planted mutants fired** — CERTIFIED |
| **D4 / ETFS_SATELLITES** | TO-1+TO-2 **9/9** (`~W`); TO-3 then TO-4 **delivered as separate commits, split held** (`~Y`) — CERTIFIED |
| **D8 / MDPF_COTREMEDIATION** | **BOTH** certifications closed |

⛔ **THE ONE LIVE CONSTRAINT: THE PROD PROMOTE MUST CARRY TO-3 AND TO-4 TOGETHER.** Both are on
`origin/DEV` together so DEV has no ungated window. **TO-3 alone on PROD is an ungated declared set —
every firm sees the satellites pill.** DT lane, Andrew's word. Reached independently by `~Y` (commit
topology) and this seat (declared-vs-visible split).

## B. THE `safe-deploy` P1 — AND I GOT IT WRONG TWICE ON THE WAY TO RIGHT

**THE LIVE DEFECT (real, measured twice, predicted-then-observed by `0.0.0_AB_MSTR~Z`):** the gate
printed `OK: safe-deploy gate PASS -- all files deployed and verified` **after deploying ZERO**, on
an all-`SKIP-NOT-MEMBER` push. `:1209` skips and `continue`s without recording, so `deployed` stayed
empty, the verify loop ran zero times, and `:1290`'s success line was **unconditional**. **A universal
quantified over an EMPTY SET.** The SKIP is correct per Rule 13; the SENTENCE was the defect.

```
69dec13d13  fix       -- gated the honest branch on n_skip
5b864516c2  amend 1   -- REGATED ON n_dep == 0 after 0.4.0_DS_ClientPlatform~W read it at SOURCE
b24376707c  amend 2   -- my JUSTIFICATION overclaimed; all 3 "reachable" paths are not
40db8b8f3a  EXERCISED on a live push -- predicted verbatim, falsifier ABSENT
```

⛔ **MY TWO ERRORS, both of a shape already in this log:**
1. **amend 1** — I gated on `n_skip`, **the one skip reason I had just instrumented**, leaving
   `"all 0 file(s) deployed and verified"` one bucket over. **ENUMERATING THE CAUSES IS THE
   SIX-SITES-WHEN-THERE-ARE-EIGHT ERROR AND I MADE IT TWICE IN ONE SESSION** (§3a is the other).
   **KEY ON THE OUTCOME, NOT ON THE ENUMERATED CAUSES.**
2. **amend 2** — I then named three *"reachable"* paths to that branch and **all three fail**:
   SERVE-HELD is **FALSE** (`:1120` returns early); `target is None` is **LATENT**
   (`detect_script_files` admits on the identical PURE predicate); `SKIP-SECOND-TARGET` **cannot give
   `n_dep==0` alone** (its loop is inside the deploy loop, after the primary append).
   ⛔ **So that branch is UNREACHABLE today and my fix for it is DEFENSIVE — I had presented it as a
   live-defect fix.** `0.4.0_DS_ClientPlatform~W` retracted the SERVE-HELD limb saying *"I measured
   the premise correctly and asserted the CONSEQUENCE without measuring it"* — **and I had already
   inherited that exact limb into my commit message without checking for a guard either. Mine is the
   worse instance: theirs was a fresh trace, mine was an ungrounded relay.**
   **Corrected IN THE CODE COMMENT, not only the commit message** — the `SAT-inv-2`:118 lesson
   applied to my own work eleven commits later.

⭐ **THE ACCEPTANCE IS SOUND BECAUSE OF ITS SHAPE, NOT ITS RESULT:** the exact output was **published
by a NON-AUTHOR BEFORE the push**, naming the string that would mean failure; it was observed
verbatim on a real push; the falsifier was absent. **I could not have fitted it afterwards.**

## C. TWO MORE CRITERIA OF MINE THAT SCORED SHAPE, NOT EFFECT

- **`ND-TO1-AC3`** — a PLACEMENT test. `0.4.0_DS_ClientPlatform~Q` satisfied it perfectly with a
  discriminator that **could never fire** (the matcher normalised the NAME, not the PHRASE).
  ⭐ **"A presence check cannot tell a live predicate from a dead one."**
- **`comp-transform ternary-audit`**, which I MANDATED in TO-3 Phase 1 as *"the fix list"*,
  **measures NOTHING on the Positioning plane** — a clean result that is out-of-scope SILENCE.
  **I named an instrument instead of naming what it must be able to FAIL on.**
- And `0.4.0_DE_ClientPlatform~Y` measured **20** mode-keyed sites to my 8 — **all eight of mine were
  in the two DECLARATION files, none in a CONSUMER.** `grep PositioningMode` is structurally blind to
  `const isEtfs = mode === 'etfs'`: **a two-valued boolean over a three-valued axis, fanning to SEVEN
  consumption points from one line.**

## D. SEATS OUTBUILT THEIR SPECS — RECORDED BECAUSE IT IS THE POINT

`~Y` replaced my **exercise** with a **mechanism** (`POSITIONING_MODES` derived from the
compiler-enforced `MODE_LABELS`, so omission is impossible not merely unlikely). `~W` refused an
instruction from me and was right. `~Q`'s mutant M1 returned `'bare'` — **exactly the value CVO F1
predicted a scalar implementation would silently return**, reproducing the PREDICTED failure rather
than merely some failure.

## E-2. ⛔ ADDENDUM 2 (1850–1930Z) — ANDREW-DIRECT, AND A DEFECT IN MY OWN COMMS A SUCCESSOR MUST NOT REPEAT

### ⛔ E-2.1 — **DO NOT SEND WITH `org/mcp/codex-send.py`. ITS MESSAGES CANNOT BE ACKED.**

**MEASURED at the recipient's inbox: 7 messages from me to `0.4.0_DS_ClientPlatform~P`, ZERO carrying
a `Msg-ID`.** Their own census: 6 of 23 unackable, **all six mine**, 6/6 correlated with
`Sender-unverified`.

```
MECHANISM -- and codex-send.py's OWN DOCSTRING discloses it, which is how I mis-sized it:
  "the broker stamps sends from an unregistered PROCESS 'Sender-unverified'
   (the registered process is the heartbeat, not this command)"
I read that and treated it as a COSMETIC provenance stamp. IT IS NOT:
  unregistered send -> NO Msg-ID -> STRUCTURALLY UNACKABLE.
```

**WHY I ADOPTED IT:** the MCP `send_message` tool refused a 4,788-byte body **five times** with
`body is EMPTY` — a **misleading error about a real size limit**. ⛔ **I routed around a bad error
message and took an unmeasured cost.**

**THE COST:** two BINDING RULINGS reached that seat with no id — the TO-6 sequencing word (cited in
`ebce987b42` *before* a production-on-save edit) and the AC4 hold. **They can evidence acting on both
from their commits; they cannot from the clock built for that purpose.**

>> ⛔ **AND THE WORST OF IT: I MADE TWO DISCIPLINED SEATS COMMIT THE ERROR I BANKED A MEMORY ABOUT.**
   `0.4.0_DE_ClientPlatform~Y` and `0.4.0_DS_ClientPlatform~P` each acked a **GUESSED id** on my
   traffic and each self-reported it. **I built the condition that made them reach for a guess** —
   while spending the same session correcting *myself* on ack discipline. <<

**THE FIX, PROVEN AT THE RECIPIENT:** back on the MCP tool permanently (ids 9778-9782, 9792-9795,
`filesystem+broker+channel push`). **For oversized bodies: a SHORT message pointing at a COMMITTED
ARTIFACT PATH.** Better regardless — a message is transient, a commit is durable and citable by hash.

### E-2.2 — ANDREW-DIRECT ~18:5xZ: POSITIONING MULTI-TENANCY

Verbatim record `@dc18f5a855`; analysis `@db2b4cdb4e` **+ five amendments, three retracting my own
claims**. **R4 DONE · R6 branch-independent DONE · R5 BLOCKED on a sovereign fork:** *"available on
Cottonwood's page, but nobody else"* is ambiguous between **VISIBILITY** (shipped, conforms) and
**ACCESS** (unreachable by any client-side gate).

⭐ **THE FIND: HE HAD ALREADY RULED IT TWICE** — `ADVI_FIRMSEP` 2026-05-07 (*"containment of data in
those cached layers is paramount"*, naming Cottonwood) and `MDPF_SCOPED` 2026-05-28 (*"the EXACT same
pattern as Advisor Intelligence"*, **closed complete**). **Found by running the Auto-Rule 5
pre-authoring check BEFORE registering a project** — the check I skipped at the TO cut and got caught
on. It also supplied the limb my analysis missed: **`X-Firm-Id` is JWT-INJECTED, not
request-derived.**

### E-2.3 — D1_CATVIEWS ASSESSMENT (Andrew-direct via `0.4.0_DE_ClientPlatform~Z`)

**Panel BUILT + CVO-certified; artifact NOT published; NO-SHIP standing; every blocker the interlock
NAMES is discharged.** So it waits on a **RULING, not work**. The figures he smoked were DE~Z's own
synthetic fixture — **they disclosed it unprompted**, so he was never carrying a false alarm.
⚠ **`mdpf_category_registry.py` "reaches no code channel" is STALE** — it is in PACKAGE at
`build_package.py:149` (positive control `:139`); true at its 08-25 vintage, closed since.

## E. MY ACK CLOCK, AGAIN

Acked nine ids off a **triage sweep** having read only subject lines. **A sweep answers *what needs a
ruling*, never *what has been READ*.** Rule adopted and applied since: **one batch per READING pass.**
`0.4.0_DE_ClientPlatform~Y` self-reported a sibling (an ACK on a GUESSED id) the same evening.

-- `1.0.0_SA_CTO~Z`
