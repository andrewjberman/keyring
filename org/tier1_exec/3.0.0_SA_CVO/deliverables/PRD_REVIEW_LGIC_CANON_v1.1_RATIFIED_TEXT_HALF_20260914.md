# PRD REVIEW -- LGIC_CANON v1.1 @56608aadd4 -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** the L4 notifier, msg 96536.

**Prior:** v1.0 SIGNED -- sign-off `447e20385b`, review @`c2357a9e3b`. v1.1 landed four minutes after that stamp, to
answer `4.0.0_SA_CRO`'s two refusals of the brief half, so the v1.0 signature is correctly STALE.

**Read, UTC 2026-09-14 ~07:4xZ:**
- The PRD @`56608aadd4`. The working copy is identical to HEAD.
- A section-by-section diff against v1.0 @`4d65f28d36`, run through `.tools/prd_signoff_lib.py`'s own `top_sections` parser.
- The two changed CONTRACTS lines, read in full.
- The brief-half lines that define the new generated section (DEC-1(b), C1, PATHS, SURFACE MANIFEST), read for context and not graded.
- `LGIC_ENFORCE` v1.1's generated-views row and DEC-5, @`78128f29ea`.

**Half hash reviewed:** ratified-text `43fa46d2a86f5474d6600060010bdf51a99d449299cb0a0415008df3faa1620b`. It matches the
notifier's `43fa46d2a86f`.

## VERDICT: SIGN -- one new non-blocking note (N4); v1.0's three notes carry

## THE DIFF OF THIS HALF, v1.0 -> v1.1

**ENDPOINT is byte-unchanged,** so v1.0's finding carries: TITLE, DONE WHEN and ACCEPT are verbatim for 6 of 6 outcomes,
and no ruled constraint lives outside the outcome block.

**CONTRACTS changed on two lines, and only those:**

| row | v1.0 | v1.1 |
|---|---|---|
| `infra/logic/02_DOCTRINE.md` | its naming axis CITES `NAMING_SCHEMA.json` and restates none of it | its naming axis PRESENTS the schema's content as a GENERATED section, rendered from `NAMING_SCHEMA.json` and stamped with that file's version and content hash; never hand-edited; *"its bytes equal a fresh render of the stamped schema"* |
| `NAMING_SCHEMA.json`, consumed | the canon cites it and restates none of it | the canon presents it as a generated, version-stamped section and owns none of it: *"a change to an enumeration is a change to this file, re-rendered into the canon, never an edit to the canon"* |

**The change is coherent.**
- **One owner.** The schema stays the only owner of every enumeration; the canon owns none of it. That agrees with `LGIC_NAMING` v1.2's row 1.
- **One renderer, and it is this project's.** The section is written by `infra/logic/render_naming_section.py` (C1), which reads the schema and never writes it. `LGIC_ENFORCE`'s generator does not write it, and its generated-views row and DEC-5 correctly do not list it. So there is no counterpart gap.
- **The reason is recorded.** It answers `4.0.0_SA_CRO`'s brief-half R2: a reader judges the naming axis from the one document alone, as FWD-1 requires.

### N4 (non-blocking) -- a stale generated section is detectable, but nothing refreshes or refuses it

**What the rows bind.** The doctrine row binds the section to *"a fresh render of the STAMPED schema"*. That keeps
the section equal to the schema version it names. It does not keep it equal to the schema that is current.

**What happens on a schema bump.** When `NAMING_SCHEMA.json` bumps, the section stays internally consistent and
falls out of date. The stamp makes that visible to a reader who compares it with the live file. But:
- *"re-rendered into the canon"* is stated as a fact, with no mechanism named;
- no row names what refreshes the section, or what refuses a stamp that is behind the live schema.

**Why it matters.** A seat judging a tree from the canon (FWD-1) would then judge against the old enumerations.

**Why it does not block.** Staleness is detectable from the stamp itself, and the section cannot drift from the
version it names.

**Fix, at the next bump of this half, or at L5 for cell C1:** name the trigger, for example:
- the renderer runs in the same change as any schema bump; or
- a check refuses a section whose stamped content hash differs from `NAMING_SCHEMA.json`'s current hash.

## CARRIED FROM v1.0, UNCHANGED

- **N1:** neither counterpart lists the canon as a consumer. `LGIC_NAMING`'s schema row names `LGIC_ENFORCE` and "every seat minting a name", and now the canon renders the schema too.
- **N2:** parity of the four produced rows is NOT EVALUATED, because `ADVI_FIRMBKTS` and `MDPF_CANON` have no PRDs.
- **N3:** row 8's "once this file exists" is already true after `89b9afd9d1`.
- **Every consumed anchor still resolves.**

## NOT CLAIMED

- **The brief half** -- DEC-1 onward, including the slot-aware naming check (the CRO's R1), the cells, paths, coverage and surface manifest. That half is `4.0.0_SA_CRO`'s.
- **That the renderer exists.** `infra/logic/render_naming_section.py` is new in C1, and its correctness is graded at L9.
