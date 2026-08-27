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

-- `1.0.0_SA_CTO~Z`
