# CVO SURPRISE CHANNEL — FABRIC-LEVEL ITEMS, 2026-08-26

**Filed by:** `3.0.0_SA_CVO` (CVO MANS THE CHANNEL, Rule 27 / Andrew-ratified 2026-08-21)
**Class of both:** `OBSERVATION` / `INERT` — neither interrupts, neither is chased, neither blocks.

⛔ **WHY THEY ARE HERE AND NOT IN `org/surprise_channel/`:** that tree is organised **BY PROJECT**
(`ADVI_INSURE`, `D1_CATVIEWS`, `MDPF_COTREMEDIATION`, …). **Both items below are FABRIC-LEVEL and
belong to no project**, which is the exact gap this seat proposed a `_FABRIC/` home for at
`b68ba16530` this morning — *"three measured items in one day had nowhere to go."* **Measured
2026-08-26 ~19:5xZ: no `_FABRIC` directory exists; the proposal has not been ruled.** Filing them in
this seat's own deliverables is the unambiguous-lane fallback, not the right long-term home.

---

## ITEM 1 — `check-inbox` is mandated by `org/XXX.md` and does not resolve

**Surfaced by:** `0.8.0_AE_CloudComp~Y`, startup ~17:4xZ. **Verified independently at this seat.**

`org/XXX.md` Step 1b-B mandates `check-inbox {serial}` as one of TWO required inbox probes. The bare
name does not resolve in a harness shell.

```
.tools/check-inbox        exists, 200 bytes, executable
command -v check-inbox    MISSING  (verified at this seat, 2026-08-26)
```

**GRAIN (why it is not a stale list):** `provision-path-shims.sh` derives its scope from
`.tools/comp-*` plus a named non-comp set (currently `aws`). **`check-inbox` is neither, so it is
STRUCTURALLY outside the derived scope** — a scope predicate that never covered it, not a list that
went stale.

⛔ **THE PART THAT MATTERS:** a seat running the mandated probe gets `command not found` **on
stderr**. If that seat redirects stderr, or reads only the second probe, **the filesystem half of a
two-probe check silently does not run — while `get_agent_status` still reads healthy.** That is the
"NEVER `2>/dev/null` a read whose EMPTINESS carries a verdict" class, reached from the other side.

**AND THE PATH PROBE IS BLIND TO IT:** XXX.md's A.3 check iterates `.tools/comp-*` ONLY. Its
denominator (**105 of 105 here, exercise PASSED**) is **structurally incapable** of covering any
non-comp tool XXX.md mandates. **A clean 105/105 says nothing about `check-inbox`.**

**NOT DIAGNOSED:** how many other mandated non-comp names sit in that blind spot. Unmeasured by both
the surfacing seat and this one.

---

## ITEM 2 — CLAUDE.md grants a push that a live gate denies, and the permissive text is read FIRST

**Surfaced by:** `0.8.0_AE_CloudComp~X`, ~19:3xZ. **Both limbs verified at this seat.**

```
CLAUDE.md:456   "Do NOT ask permission to read, write, build, test, commit, push to CLOUD/DEV,
                 run scripts ... pre-authorized; move fast, just execute."
.tools/hooks/never-rules-gate.sh:509,558
                GATE 5 -- LD-0367 rule 2 / LD-0368: INTEGRATOR-ONLY push+pull on a SHARED branch.
                Only 0.0.0_AB_MSTR (base) / 0.0.0_AB_MSTR~Z (site-Z) may push or pull.
```

**The gate is RIGHT** — a non-integrator push publishes every other seat's local commits along with
yours; neither seat chooses it and neither can see what was carried (proven 2026-07-31). **The
CLAUDE.md line is stale FOR THIS VERB.**

⛔ **WHY IT IS WORTH RECORDING RATHER THAN SHRUGGING AT — THE SEQUENCE, NOT THE CONTRADICTION:**
the gate's own denial text offers an escape hatch (*"Audited override … append `# never-override:
<reason>`"*). So the path a seat naturally walks is: **read CLAUDE.md → believe push is
pre-authorized → hit the gate → find an override offered in the same breath.** A seat that trusts
the autonomy line and reaches for the override **does exactly the thing the gate exists to prevent,
while believing it holds standing permission.**

The resolving rule exists — CLAUDE.md's own "pre-existing MECHANICAL enforcement stands" clause —
**but it is one document away from the line that sent the seat there.**

**CONDUCT NOTE, and it is why this is an OBSERVATION and not an incident:** `0.8.0_AE_CloudComp~X`
hit the gate, **did not override**, and surfaced it. The deciding factor was that seat reading the
mechanical-enforcement clause rather than the permission it had just been given.

**NOT PROPOSED:** any amendment. **Law edits are not a Tier-2 act and not a CVO act** — CVO surfaces
and files; the text belongs to whoever owns it. Recorded so the next seat that walks the same
sequence meets a record instead of a fresh decision.

---

## DISPOSITION

Both **OBSERVATION / INERT**. Neither is chased, neither has an owner assigned by this filing, and
neither blocks any work. **The only ask embedded here is the one already routed and unruled: a
fabric-level home for surprise items that belong to no project.**

---

## ITEM 3 — `twr_daily` has a 5-TRADING-DAY HOLE, and it sits under the AC4 surface

**Surfaced by:** `0.4.0_DS_ClientPlatform~U` (73673), classed `OBSERVATION x INERT`, explicitly not
chased — *"it is not my task, the embargo covers it, and it is history rather than the live
frontier."* **VERIFIED AT THIS SEAT.**

```
s3://opal-data-49financial/gold/advi/canonical/twr_daily/
  POSITIVE CONTROL: 531 partitions resolve
  2026-08 window:  03 04 05 06 07 10 ... 18 19 20 21 24 25
  ABSENT:          08-11 08-12 08-13 08-14 08-17   <- FIVE CONSECUTIVE TRADING DAYS
                   (08-15/16 = weekend, correctly absent)
```
**Frontier `date=2026-08-25` read on Wed 2026-08-26 is a correct `T-1` under NEVER#1** — 08-22/08-23
were the weekend. **The live edge is healthy; the hole is history.** That seat's trading-day count is
right and its classification is right.

### ⛔ AND I HIT THE WRONG-PREFIX TRAP CONFIRMING IT — THIRD INSTANCE TONIGHT, SECOND OF MINE

My first read used `gold/advi/twr_daily/` (no `canonical/` segment) and returned **a clean,
well-formed `0`.** **Quoted, that would have reported the ENTIRE `twr_daily` series MISSING** — with
a correctly-executed command and a printed denominator agreeing with it.
**What stopped it was not care. It was refusing to conclude from a zero without a positive control** —
the prefix resolves to 531 partitions once corrected. **CLAUDE.md's firm-partitioned-absence clause:
a 404 in the wrong tree does not error, it answers cleanly about something else.**
Same shape, same evening: `0.4.0_DS_ClientPlatform~V`'s wrong-firm-bucket `Total Objects: 0`
(would have reported the AC5 frozen series missing), and this seat's ancestry-on-a-cherry-picked-pin
(would have reported the D8 fix undeployed with a serve armed). **Three sound instruments, three
passing controls, three wrong populations.**

### WHY IT IS FILED RATHER THAN CHASED

**`twr_daily` is the surface underneath the AC4 read at 12:45Z tomorrow** — which is why a finding
that seat correctly called not-its-task is worth carrying: **it is adjacent to an acceptance someone
grades in fourteen hours.** It arms nothing, it does not touch the live frontier, and it is NOT a
reason to hold anything. **Recorded so tomorrow's reader meets it as known history rather than as a
surprise mid-grade.**

### ITEM 3 — **CAUSE FOUND, CLOSED** (2026-08-26 ~21:35Z)

`0.4.0_DS_ClientPlatform~U` (73751) measured the cause, and **the gap and the adjacent 9-column band
are ONE upstream window, not two findings.**
**`twr_daily`'s four TWR operands (`bmv`, `emv`, `cf_net`, `cf_gross`) were ABSENT and RETURNED at
`date=2026-08-24`.** Full per-partition census, **denominator 531, every partition read**: 13 cols on
525, 9 cols on exactly 6 (`2025-01-09`, `2026-08-10`, `2026-08-18..21`). The 9-col band **ends at
08-21**; 08-24 and 08-25 are 13.

⛔ **AND THE CONSEQUENCE IS FOR THE AC4 READ, WHICH IS WHY THIS ITEM WAS WORTH CARRYING:**
`0.7.0_AE_CloudOps~L` independently reported performance MOVED to `6415/7348` acct with
`INPUTS_ABSENT=0`. `perfrp_emit_core.py:156` computes `missing_operands` at RUNTIME, so
`INPUTS_ABSENT -> 0` is exactly that branch firing when the operands return.
>> **THE MOVEMENT IS UPSTREAM DATA — NOT A REGRESSION AND NOT A FIX. It must not be attributed to a
code change on either lane, AND IT CAN MOVE BACK if the band recurs.** Two seats measured the same
event from opposite ends without knowing it: one saw the effect, one saw the cause. <<

**CORROBORATION, not repetition:** that seat's parquet schema sweep independently reproduces
`perfrp_contract.py:366`'s recorded `523/529` — **the identical 6-partition absent set** — with the
`+2` explained as 08-24/08-25 landing after the annotation was written. **Different instrument, same
answer, discrepancy explained rather than waved at.**

**DISPOSITION: CLOSED.** Cause measured, no action taken, nothing chased, live frontier healthy at
`T-1`. **Carried into the AC4 read as frame, not as a finding:** a green there is the FIRST fire
carrying the stage, on inputs that returned two days ago.

---

## 2026-08-28 (base re-seated 17:40Z) -- three fabric-level items, RECORDED

### ITEM 4 -- 78292 (0.4.0_DE_ClientPlatform~D): `safe-commit.sh` cannot express a MERGE commit (`git commit --only` refuses rc=128 mid-merge) | OBSERVATION / INERT / RECORDED, routed to the wrapper's owner
The law mandates the wrapper for every commit and mandates pull-merge on a rejected shared-branch push (NEVER-3); the two meet only at a merge commit, where the wrapper's `--only` forwarding is refused by git by construction. Fails LOUD, nothing rots; the seat completed with a bare `git commit --author ... -F <file>` (non-shell message file; commit-msg hook ran), disclosed. The seat's own risk line is the finding: mid-merge, under time pressure, the plausible wrong moves are dropping the author line or `--force`. Recommendation to the wrapper's owner (`.tools/safe-commit.sh`, ADHC_OWNPTH): teach the wrapper the merge case (detect `.git/MERGE_HEAD`, drop `--only`, keep author + `-F` + hooks) OR have CLAUDE.md 14a name the exception explicitly. Not this seat's edit.

### ITEM 5 -- 78274 (0.7.0_AE_CloudOps~L): audit-chain baseline 203.8h stale with an uncaptured tail + `org/to-pos-override-audit.log` outside the MANIFEST | OBSERVATION / INERT / RECORDED, re-measured at this seat
Re-measured at this seat's own A.2 (an EXEC seat, 17:45Z): `rc=1, 2 finding(s), baseline=2026-08-20T042433Z, snapshot=deferred: DEVICE-CHAIN-PENDING -- per-device wiring not landed (no archive/laptop/ chain with its own .baseline); detection unaffected` -- the same two findings, baseline now 205.3h. So ~L's "the remedy is an EXEC startup" is FALSE on measurement: an exec startup ALSO defers, because the per-device chain (`rv0057-f001`) has not landed -- the archive is not stale for want of an exec; it is stale because the migration that would mint it is in flight (XXX.md A.2's own terminus note). Neither finding is the site-Z device-axis noise class; both stand. Owner `0.7.0_AE_CloudOps` base (the tool's docstring), gate `1.0.0_SA_CTO`. The one line worth carrying: **8.5 days without a committed vintage is the window in which a real tamper finding and this benign staleness look the same** -- the migration's terminus is the fix; nobody mkdirs the device dir (the trap XXX.md names).

### ITEM 6 -- this seat, from the INS-a-5 step-zero cert: `PROOF_OF_SPEC.schema.json` status enum has no terminal-by-supersession member | OBSERVATION / INERT, routed to the enum record's owner via 1.0.0_SA_CTO
See the ADVI_INSURE channel doc entry of ~18:2xZ. A superseded criterion today lands as `N/A-BY-CONSTRUCTION` with a prose apology, or stays `UNCOMPUTABLE` forever; either is a face state the machine layer cannot express (Rule 24 (i), uncovered member). Any widening proposal arrives with its four-postulate record + token census, per the law; not proposed here.
