# PROPOSAL — a home for FABRIC-LEVEL surprise items

**Author:** `3.0.0_SA_CVO` (channel owner) · **Date:** 2026-08-26 · **Status:** PROPOSAL, not landed
**Object:** one value added to the surprise channel's DIRECTORY-HOME axis.
**Ratifiers:** `1.0.0_SA_CTO` (architecture) · `2.0.0_SA_COO` (routing). The protocol is
Andrew-ratified (Rule 27, 2026-08-21), so this is an amendment proposal and not a CVO unilateral edit.

---

## 1. THE DEFECT, MEASURED

`org/surprise_channel/`'s layout grammar is `{PROJECT_CODE}/INVESTIGATION_v{N}.md`, named as the
ratified home in `SURPRISE_CHANNEL_PROTOCOL.md` §0 and again in §8.

**Over the declared domain — *items surfaced by any seat* — that grammar is not collectively
exhaustive.** An item whose subject is the fabric itself, not a project, has nowhere to go.

**Three such items arose in one day, 2026-08-26, all measured, none filable:**

| item | measurement | surfaced by |
|---|---|---|
| seat `prompt.md` files mandate the `/c/` watcher path that kills the Monitor arm | **16 of 40** files; 0 carried the working form; all 16 Tier-2 | `0.4.0_DS_ClientPlatform~R` |
| CLAUDE.md's non-ASCII ban has no instrument over the population it names | **125 of 417** gold `.py`; 19 distinct chars; the census script itself crashed on U+2192 | `0.4.0_DS_ClientPlatform~R`, harm reproduced at CVO |
| this grammar gap | 3 homeless items and counting | `3.0.0_SA_CVO` |

Each lived in a message instead of the channel — **and a message scrolls while the channel persists,**
which is the precise reason the channel exists. A successor looking for "what did we find about the
watcher path" looks in `org/surprise_channel/` and finds nothing.

## 2. THE PROPOSAL

Add ONE value to the directory-home axis:

```
org/surprise_channel/
  _FABRIC/
    INVESTIGATION_v{N}.md      # same document form, same single fenced json block
    REMEDIATION_v{N}.md
```

Item ids take the existing grammar with `_FABRIC` as the project token: `_FABRIC-S{n}` (laptop),
`_FABRIC-Z-S{n}` (site Z). **The `id` pattern in `investigation_item.schema.json` is
`^[A-Z0-9_]+-(Z-)?S[0-9]+$` and `_FABRIC` already satisfies it — no schema regex change is required.**

**Nothing else changes.** Same schema, same one-block assertion, same validation, same
CVO-files-it rule.

## 3. TOKEN HYGIENE — measured over the canon, denominator 7 files

Canon: `CLAUDE.md`, `SURPRISE_CHANNEL_PROTOCOL.md`, `DIRECTIVE_EXECUTION_PIPELINE.md`,
`surprise_channel/README.md`, both schemas, `docs/doctrine/THE_SURPRISE_CHANNEL.md`.

| candidate token | word-boundary occurrences | verdict |
|---|---|---|
| `_FABRIC` | **0** | clean |
| `FABRIC` | **20** | ⛔ **REJECTED** — a heavily-used common noun in the canon; a bare `FABRIC/` directory would read as a project code |
| `ESTATE` | 17 | rejected, same reason |
| `CROSS_CUTTING` | 0 | clean but coins new vocabulary for no gain |
| `GLOBAL` | 0 | ⛔ **REJECTED** — `global` is a live MDPF **scope name**; collision with real data |

**The leading underscore is not decoration — it is this estate's existing non-project marker,**
observed in live keys today: `blackdiamond/49f/_ops/probe/`, `portal/gold/mdpf/_manifests/`,
`portal/gold/mdpf/_code/`. It is also already used inside this very directory: `schemas/` sits beside
the project codes as a non-project sibling.

## 4. RULE 24 FOUR-POSTULATE RECORD

**Declared domain:** the HOME directory of one surprise-channel item.
**Axis:** *where does a reader look for this item.*

**(i) MECE.**
*Exclusivity* — an item has a project subject or it does not; the two values cannot both apply.
*Coverage* — `{PROJECT_CODE}` covers project-subject items, `_FABRIC` covers the remainder. **The
uncovered member hunt found the gap this proposal closes; hunting again against the amended axis:**
an item spanning TWO projects still has no expressible home. ⛔ **That is PRE-EXISTING, is NOT closed
by this proposal, and is named here rather than passed over** — today the filer picks one and the
grammar cannot record that a choice was made.

**(ii) SAME GRAIN.** Both values are directories at the same level holding the same two document
kinds. `_FABRIC` is not a coarser or finer grain than a project code; it is a sibling.

**(iii) INTENT COHERENCE.** One intent: *where a reader looks.* The axis carries no severity, no
ownership, no disposition — `class`, `hazard_standing`, `disarm_owner` and `disposition` remain the
item's own fields and are untouched.

**(iv) STATE COHERENCE.** One remedy moves every value: the filer re-files the document. **Which
values do not move under the obvious instrument:** none — there is no derivation here, a home is
asserted by the filer, so no value is stranded by an instrument that cannot reach it. *(This is the
postulate that usually bites; it does not bite here precisely because the axis is not derived.)*

## 5. WHAT THIS DOES NOT DO

- **It does not authorize back-filling.** The three items above are filed going forward; nothing is
  swept.
- **It creates no gate, no approval step and no owner obligation.** Filing remains CVO's act.
- **It does not touch `investigation_item.schema.json` or `remediation_row.schema.json`.**
- **It does not resolve the two-project item**, which is named in §4(i) as an open residual.

## 6. WHY THIS IS A PROPOSAL AND NOT AN EDIT

Adding a value to a ratified schema is an authoring act, and **adoption is authoring** (Rule 24).
This seat applied that bar to two other seats' proposals today — a TO `<lifecycle>`/`<delivery>`
split, and a reconciliation predicate — and returned both for rework. **Minting a value into its own
document on its own authority, while holding peers to a four-postulate record, is the asymmetry this
record exists to avoid.**

*Grounded: all counts re-derived at this seat; the U+2192 crash is a live traceback at this seat, not
a citation.*
