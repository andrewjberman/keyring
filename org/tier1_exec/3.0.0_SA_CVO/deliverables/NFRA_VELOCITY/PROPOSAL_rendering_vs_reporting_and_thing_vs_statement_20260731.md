# PROPOSAL -- two laws, one family: RENDERING vs REPORTING, and THING vs STATEMENT-ABOUT-THING

**Author:** `3.0.0_SA_CVO~Z` · **Co-signed:** `1.0.0_SA_CTO~Z` (CORE owner) · **Routed via:**
`0.0.0_AB_MSTR~Z` → **main CTO** (CLAUDE.md and `docs/doctrine/` are law surfaces; `~Z` does not land
them under the exclusive regime).
**Date:** 2026-07-31. **Origin:** NFRA_VELOCITY CORE WS-C1, one session, three seats.
**Blocks nothing.** Not urgent. Submitted as a proposal, not a change.

---

## The two laws

> **(1) `git show` RENDERS. `git cat-file` REPORTS.**
> `git show <ref>:<path>` applies the smudge filter, so its output is a *rendering* of the blob, not
> the blob. Use `git cat-file -p` (or `--batch`) whenever the question is about BYTES -- line endings,
> size, byte-identity at a vintage.

> **(2) A CHECK THAT CANNOT DISTINGUISH A THING FROM A STATEMENT ABOUT THE THING WILL FORBID THE
> RECORD FROM DOCUMENTING ITSELF.**
> A string-absence check ("token X must not appear") cannot tell a token USED from a token NAMED. It
> fires on the artifact's own explanation of the rule, on the correction that records the defect, and
> on the tool's statement of its own bound.

**They are one law at two altitudes.** (1) confuses a RENDERING with the bytes; (2) confuses a MENTION
with the fact. Both are *an instrument answering a different question than the one asked, in a
well-formed way that reads as an answer.* **Splitting them loses the generality that makes either
worth landing** -- which is why this is one proposal.

## Why it is empirical, not clever: it fired FIVE times in one night, in five costumes

| # | seat | instrument | what it did |
|---|---|---|---|
| 1 | CVO~Z | F-1 token check: "SUPERSEDED/ORPHAN absent as a string in the subtree" | **FALSE FAIL** -- every hit was prose STATING the prohibition. Would have forbidden the rule bank from documenting its own rule. |
| 2 | CTO~Z | `DEAD`-verdict grep over ~C's census | one hit -- **the tool stating its own bound** |
| 3 | CTO~Z | post-edit check on the rule bank | flagged **the correction's own quoted provenance** |
| 4 | CVO~Z | `git show HEAD:<path> \| grep -c $'\r'` as a byte oracle | reported **CRLF=64 on a blob stored LF** -- inverted an EOL finding in a message already sent to two seats |
| 5 | MSTR~Z | `grep -c $'\r'` in MSYS bash | **positive control FAILED** -- reported 3 CRLF lines in a pure-LF file; every absolute number from that pass was garbage |

Instances 4 and 5 are the same question asked of two different rendering layers (git's smudge filter;
MSYS's own EOL translation). **For an EOL question the oracle must not sit downstream of an EOL
transform -- and both obvious tools are.**

## Where each piece goes (per CLAUDE.md's own "WHERE THINGS GO" table)

**This is the part I want reviewed hardest**, because the failure mode of a good finding is landing it
in the wrong place and taxing every agent's context forever.

| piece | destination | why |
|---|---|---|
| **Law (1)**, one line | **CLAUDE.md**, Git section | It is a **MECHANISM an agent cannot obey the surrounding rules without.** That section already forbids `2>/dev/null` on `git show <ref>:<path>` because the mangle prints to stderr and returns clean-empty stdout -- **so the file already knows `git show` lies in ONE direction and does not know it renders in another. Two failure modes on one command, one recorded and one not, is exactly what makes the recorded one read as complete.** |
| **Law (2)**, general form | **`docs/doctrine/CONTROLS_OVER_CARE.md`** | It is a *principle binding future behaviour*, not an imperative with a mechanism. It belongs beside "a control that cannot fail is not a control." |
| **The five instances** | **`docs/references/`** | *The scar is not the rule.* |

**Proposed CLAUDE.md text (one line, Git section):**

> - **`git show` RENDERS (smudge filter applied); `git cat-file -p` REPORTS (raw blob).** For any
>   BYTE-level question -- line endings, size, byte-identity at a vintage -- use `git cat-file`.
>   `git show HEAD:<f> | grep -c $'\r'` reported CRLF=64 on a blob stored **LF** (2026-07-31), which
>   inverted an EOL finding already relayed to two seats. Sibling of the `2>/dev/null` caveat above:
>   **same command, second failure mode.**

## On gates -- honest, because CLAUDE.md asks for one

CLAUDE.md says a new rule *ideally ships WITH a gate*. I am not going to invent a weak one to satisfy
the form.

- **Law (1) -- gate CANDIDATE, real but narrow:** lint a `git show <ref>:<path>` whose stdout is piped
  into a byte-level consumer (`grep -c $'\r'`, `od`, `wc -c`, `cmp`, `md5sum`) → warn, name
  `git cat-file -p`. Cheap, textual, low false-positive. **Routing this as a candidate, not building
  it** -- and noting that a text-matching gate is legitimate here for the same reason CLAUDE.md's F-010
  gate is: the hazard IS in the shell-parsed command text.
- **Law (2) -- NOT GATEABLE, and I will say so rather than pretend.** A gate that could detect "this
  check confuses a mention with the fact" would have to model the checker's INTENT. **It is a review
  heuristic and belongs in doctrine, not as a gate.** *The operational form that IS actionable:* when
  a check asserts a token's ABSENCE, scope it to the **structural position** (enum member, dict key,
  emitted value) and **positive-control it in both directions** -- prove the search still finds the
  tokens that SHOULD be there, and still finds the forbidden token where it legitimately appears.
  That is what turned instance 1 from a false fail into a correct PASS.

## What this proposal does NOT claim

- It does not claim these are new laws. It claims **the git half is an undocumented second failure
  mode on a command the file already caveats**, and the general half is a named shape for something
  the estate keeps rediscovering.
- **It does not claim a count of historical incidence.** Only LOUD instances leave a scar; a
  string-absence check that quietly passed is indistinguishable from one that never ran. Five is what
  ONE NIGHT surfaced with people actively looking -- **it is a floor, never a total.**
- It does not ask for a rewrite of the Git section. One line, one doctrine paragraph, one reference
  entry.

---

*Provenance: WS-C1 design attack + verify, 2026-07-31 ~0250-0445Z. Instance 1 is my own false fail
caught before reporting; instance 4 is my own error caught by `0.0.0_AB_MSTR~Z` after I had relayed
it; instance 5 is MSTR~Z's, caught by their own positive control. **Every one was caught by a control
failing, not by anyone being careful** -- which is the doctrine this belongs next to.*
