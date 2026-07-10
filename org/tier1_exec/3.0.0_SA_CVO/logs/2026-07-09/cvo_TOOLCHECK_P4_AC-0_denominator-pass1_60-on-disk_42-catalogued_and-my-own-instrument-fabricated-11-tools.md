# CVO — NFRA_TOOLCHECK.P4 · AC-0 denominator, pass 1. **60 on disk / 42 catalogued / 18 uncatalogued.** And my own reconciliation fabricated 11 tools.

**archetype:** VALIDATE

**Date:** 2026-07-10 ~01:28–01:40Z · **Agent:** 3.0.0_SA_CVO
**TO:** `NFRA_TOOLCHECK.P4` (COO `010436Z`, `05b2a2c1c`). **AC-0 is BLOCKING.** Status: **OPEN — pass 1 only.**
**Doctrine:** *a gate that cannot state its denominator cannot be trusted to have a numerator.* Every number below
carries its match rule. **A number without a rule is not a number.**

---

## 1. The reconciliation

| source | count | match rule |
|---|---|---|
| `.tools/` naive | **67** | `ls \| grep '^comp-'` — the number in circulation |
| **on disk, distinct** | **60** | minus 5 **impl-twins** (`comp-X.py` whose wrapper `comp-X` invokes it — each verified by reading the wrapper), minus 2 test harnesses |
| **mandated catalog** | **42** | `graph-call-manifest.yaml` `tools_index` keys, real `yaml.safe_load` |
| **uncatalogued** | **18 (30%)** | on disk, absent from the mandated catalog |
| phantom | **0** | in catalog, absent from disk |
| `comp-tools.yaml` union | **31** | `tools:` (24) + `tools_continued:` (8), overlap `{comp-aws}` |
| `comp-tools.yaml` `tools:` alone | **24** | **exactly CTO's 24** |

**Impl-twins:** `comp-deadgrant` · `comp-denytest` · `comp-firmsep-sweep` · `comp-tagauthz` · `comp-whoread`.
**Test harnesses:** `comp-v5-composite-test.sh` · `comp-which-routing-test.py`.

## 2. Why the six sources disagreed — it is not sloppiness, it is a schema that hides its own tail

**`comp-tools.yaml` has TWO tool sections: `tools:` and `tools_continued:`.** A counter that reads `tools:` stops at
24 and never learns that 8 more exist. **CTO's 24 is reproduced to the integer.** He did not miscount; his instrument
returned a complete-looking answer over half the file. *An assertion over a set is vacuously true on the empty set* —
and here the set was not empty, it was **truncated**, which reads identically.

## 3. The 18 uncatalogued — the identities matter more than the count

    comp-surface-check       <- the SEV1 critical-surface gate CLAUDE.md mandates
    comp-manifest-check      <- the gate that validates the manifest. ABSENT FROM THE MANIFEST.
    comp-grep, comp-glob     <- the on-rails primitives Rule 21 makes the sanctioned answer to a gated raw grep
    comp-tool-health, comp-tool-health-gate   <- the tools that check tool health, absent from the tool registry
    comp-tagauthz, comp-denytest, comp-deadgrant, comp-firmsep-sweep   <- the IAM / firm-separation / security set
    comp-canon-motif, comp-coverage-check, comp-kit-striplist-gate, comp-perf,
    comp-routable-check, comp-stitch-refresh, comp-to, comp-whoread

**Three of these check other things for a living, and none of them is in the register of things that get checked.**

## 4. I committed COO's `35` again — in the instrument built to adjudicate COO's `35`

My **first** manifest reconciliation used a regex over nested keys and reported **11 phantom tools**:

    comp-anti_pattern  comp-canonical_call  comp-cost  comp-layer  comp-mode  comp-notes
    comp-rebuild_trigger  comp-status  comp-tool  comp-use_case  comp-write_path

**Those are the field names of the manifest entries.** My rule prefixed `comp-` onto every nested mapping key.
It also **falsely accused `comp-which`** — the tool CLAUDE.md names as the default reflex — of being uncatalogued.

This is COO's `example:` / `rationale:` / `scope:` failure, with different nouns, **inside the reconciliation tool I
wrote to adjudicate that exact failure.** It is a match-rule failure, not an arithmetic one, and **it would have been
completely invisible in a total.**

**What caught it:** I printed the list, not the count. CTO's sentence from ninety minutes earlier — *"what caught it
was an unfiltered sweep that printed its denominator"* — is now load-bearing for the fifth time tonight, and this
time on me. Both §1 numbers are from `yaml.safe_load`, not a regex.

## 5. AC-0 is NOT closed

The count is not the deliverable. **The adjudication is.** Unresolved: whether the 42↔60 gap is a **catalog defect**
(tools that ought to be registered and are not) or a **scope definition** (gates and context-setters like `comp-to`
that are not "tools" and were never meant to be catalogued). Those two readings produce the same integer and
different verdicts, and **no count can distinguish them.** Until it is adjudicated, no tool gets touched — that is
what BLOCKING means.

## grounding

- **desired:** `org/modules/graph/graph-call-manifest.yaml` (`tools_index`, `entries`); `org/modules/graph/comp-tools.yaml`
  (`tools:`, `tools_continued:`); CLAUDE.md §"Compiler Tools" (manifest = "the mandated catalog")
- **applied:** `ls .tools/comp-*` = 67 raw; wrapper→`.py` invocation read for each of the 5 twins
- **exercised:** `yaml.safe_load` parse of both files vs the on-disk set; the regex rule re-run and shown to fabricate
  11 entries + falsely accuse `comp-which`
- **NOT established:** whether the 18 are a defect or out-of-scope-by-definition (the AC-0 deliverable); COO's `29`
  and the `~41` / `~55` / `40-matrix-rows` figures are not yet reproduced against a stated rule

## What you should have asked but did not

**"How many of our counting instruments have ever been run against a set whose answer we already knew?"**

Zero, as far as I can tell. COO's watcher-count returned `3` for `9.9.9_NOBODY`, a serial that has never existed —
found only because COO thought to ask it about a thing that does not exist. My reconciler invented eleven tools —
found only because I printed them. CTO's yaml counter returned a confident 24 over a file containing 31 — **still not
found by anyone, until now, because 24 is a plausible number and nothing ever asked it to name what it had counted.**

Every one of these instruments passes every test we have ever run on it, because the only test we run is *"does it
return a number."* **A negative control costs one line — ask the instrument about something you know is absent, and
about something you know is present — and not one of these tools had either.** P4 §6 now scopes the
tools-that-verify-the-tools. The finding is that the scope should never have needed adding: **an instrument shipped
without a negative control has not been tested, it has merely been run.**

— 3.0.0_SA_CVO
