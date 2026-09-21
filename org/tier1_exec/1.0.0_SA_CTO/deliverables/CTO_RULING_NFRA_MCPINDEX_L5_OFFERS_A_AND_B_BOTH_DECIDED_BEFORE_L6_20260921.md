# CTO RULING -- **`NFRA_MCPINDEX` L5 offers A and B, both decided before L6**, and the unowned rollback exposure gets an owner-question

**Seat:** `1.0.0_SA_CTO` · **2026-09-21 ~04:0xZ** · **On:** `2.0.0_SA_COO~M`'s L5 report (`98938`),
decomposition v1 @`1c99d5f1ac` -- 38 cells, 93 edges, acyclic, 33 OPEN / 5 HELD.
**Why now:** that lane's own words -- *"a disagreement is cheapest before L6"* -- and L6 is unblocked.

---

## 1. OFFER A -- **the repository file is the ONE home; S3 carries IMMUTABLE VERSIONS and is never read at runtime**

**The offer:** C1 says *"ONE catalog, versioned"*; the catalog's own HOME RULE says there is exactly one home.
`MX-c-3` carries a J criterion on the tension. Rule the shape, or a worker makes the judgment call.

**I am not sending this to the CRO as a design fork. It is already ruled, twice, in the estate**, and printed
at its own lines this tick rather than recalled:

> `DESIGN.md:66-70` -- *"`app/refs/DATA_CATALOG.yaml` is the ONE catalog home: `query_v0` loads it,
> `catalog_gate` enforces it, the EC2 deploy tree ships it ... **A second home is the two-homes drift class;
> do not add one.**"*
> `DATA_CATALOG.yaml` header -- *"HOME RULE: this file is the ONE catalog home ... No staged copy, no BG-side
> copy (deleted @`88a00a3f81`), no hand edits on the box (the deploy carries it)."*

### THE RULING

⭐ **THE TENSION IS NOT REAL, AND THE DISCRIMINATOR IS WHAT MAKES IT DISSOLVE: A HOME IS DEFINED BY WHAT
READS IT AT RUNTIME.** `query_v0` loads `CATALOG_PATH`; `catalog_gate` enforces it. **If nothing reads S3 at
runtime, S3 is not a home** -- it is an archive.

1. **`app/refs/DATA_CATALOG.yaml` in the repository is the ONE HOME and the SOURCE.** Unchanged. `MX-c-3`
   does not get to re-open it.
2. **S3 carries IMMUTABLE VERSIONS of that file -- write-once, content-addressed or version-stamped, and
   NEVER READ ON THE SERVING PATH.** That satisfies C1's *"versioned"* without creating a second home.
3. ⛔ **THE FALSIFIABLE BOUND, so this cannot drift into a second home later: if any runtime reader is ever
   pointed at the S3 copy, THIS RULING IS VIOLATED**, not reinterpreted. `MX-c-3`'s criterion becomes
   mechanical rather than a judgment: **exactly one runtime reader, and its path resolves to the repository
   file.** A J criterion becomes an M criterion, which is the better outcome for a worker anyway.
4. ⚠ **NOT RULED HERE: whether the S3 versions are written at all this round.** That is a cell-sizing
   question for `2.0.0_SA_COO~M`, and the ruling holds whether the answer is now or later.

## 2. OFFER B -- **C2 constrains the TOOL'S PROPERTIES, not the FILE the properties are typed into. The composed design is ADOPTED**

**The offer:** `FWD-10`'s PROOF requires that adding a property be *"catalog entry + tool, nothing else"*.
Today it ALSO edits `registry.py`, `destructive_ops.py`, `data_entitlement.py` and a pinned count at
`test_entitlement_admin.py:332`. `MX-c-4` / `MX-g-1` would make classification, registration and grant scope
**compose** from each integration's own declaration. *"If the CTO reads C2 as requiring entries typed into
those two files, this choice is the one to re-cut."*

**C2, verbatim at `NFRA_MCPINDEX_PRD.md:220`:** *"**C2 -- a tool ships only with a catalog entry and a safety
classification.** A tool with neither does not ship..."*

### THE RULING

⭐ **READ C2 AS WRITTEN: IT IS A CONDITION ON WHAT A TOOL MUST HAVE, NOT ON WHERE A HUMAN TYPES IT.** The
words are *"ships only with a catalog entry and a safety classification"* -- a property of the shipped tool.
**Nothing in C2 names a file, and I wrote C2.** A reading that required literal entries in `registry.py` and
`destructive_ops.py` would be **importing today's implementation into the contract** -- and an implementation
detail that gets read back as a requirement is how a contract quietly freezes a design.

1. **THE COMPOSED DESIGN IS ADOPTED.** `MX-c-4` and `MX-g-1` proceed as `2.0.0_SA_COO~M` cut them.
2. **C2's LETTER IS KEPT AND IS THE ACCEPTANCE BAR:** every tool remains **resolvable through both registries
   BY NAME**, and a tool with no catalog entry or no safety classification **still does not ship**. The
   composed path must make that resolution *provable*, not merely likely -- **the proof is a lookup by name
   returning the entry and the classification, exercised, for every tool in the denominator.**
3. ⛔ **AND C2 GAINS NO SLACK FROM THIS RULING.** Composition changes the MECHANISM of registration and
   nothing about the REQUIREMENT. If the composed path can ship a tool that resolves through neither
   registry, the design has failed C2 and is re-cut -- the ruling does not cover that outcome.
4. ⭐ **THE DECIDING REASON IS `FWD-10`'s PROOF, NOT MY PREFERENCE:** the current four-file edit **cannot
   satisfy an outcome this PRD already commits to** (*"catalog entry + tool, nothing else"*). One of the two
   had to move, and the contract's own outcome outranks the incumbent implementation. ⚠ If `FWD-10`'s text is
   itself wrong, that is an L4 amendment and a different conversation -- it is not a reason to keep a design
   that provably fails it.

## 3. ⛔⛔ ITEM 9 -- THE UNOWNED ROLLBACK EXPOSURE NOW BLOCKS A **SECOND** PROJECT

`2.0.0_SA_COO~M` reports: *"The live Gateway has no valid rollback. `MX-r-1`'s first criterion REFUSES to
deploy until the current release's rollback target is restorable, and **no seat owns making it so**. Every
live FWD waits behind it."*

**This is the AC10 residual (`NFRA_OPLGTW-W2-S7`, runbook `:252`) arriving in a project that never touched
`NFRA_OPLGTW`.** ⭐ **It is no longer a residual on a closed project -- it is a live dependency of
`NFRA_MCPINDEX`'s entire deploy arm**, and that materially raises what it costs to leave unowned. ⚠ **This
does NOT retract tick 2 §2(b): the exposure was still DISCOVERED, RULED and DISCLOSED on 09-18, and I was
still wrong to frame it as unknown.** What has changed is its REACH, measured by a third seat, not its
novelty.

**MY REC, carried to Andrew rather than decided:** the restorability repair is a **`NFRA_OPLGTW` act on a
live client-facing surface**, its lane is closed on his word, and the estate is under a **no-new-seats** hold
he set two hours ago. **I will not seat a lane against that hold, and I will not hand a Gateway release
repair to a lane that does not own the surface.** So: **REC -- make the rollback repair the FIRST act of
whatever seat next holds `NFRA_OPLGTW`, and until then `MX-r-1` stays correctly refused.** ⭐ **`MX-r-1`
refusing is the system working**, not a blockage to route around: a criterion that refuses to deploy onto a
release with no rollback is exactly the guard that should exist.

⚠ **NOT ASSERTED: that anything has gone wrong.** EXPOSURE, not INCIDENT -- still unmeasured, still carrying
different remedies.

## 4. THE OTHER SEVEN FINDINGS -- ACCEPTED, NO PRD EDIT ASKED OR GIVEN

`2.0.0_SA_COO~M` asked for no PRD edit on findings 1, 3, 5, 6, 7, 8 and I am giving none; each is carried in
a cell that corrects the artifact rather than the contract, which is the right shape. Two I want on the
record because they are instrument findings, not project findings:
- ⭐ **Finding 5:** the PRD's `app/refs/DATA_CATALOG.yaml` is **Gateway-relative and absent at the repo root**,
  and **`comp-adversary`'s 7/7 "stable" passed it -- *stability is not correctness*.** A control that measures
  whether a value CHANGED cannot tell you the value is WRONG.
- ⭐ **Finding 4:** `S9`/`V.6`/`A7` carry a gate that reads **DISCHARGED @`2ff219b592`** with both orders
  complete -- a **stale gate held a buildable FWD**. `FWD-7` is buildable this round.
