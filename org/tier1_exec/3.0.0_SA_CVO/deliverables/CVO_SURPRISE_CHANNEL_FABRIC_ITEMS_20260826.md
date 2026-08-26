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
