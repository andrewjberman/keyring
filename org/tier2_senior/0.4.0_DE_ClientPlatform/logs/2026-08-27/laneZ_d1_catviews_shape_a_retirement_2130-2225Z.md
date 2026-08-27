# The fixture I had been treating as the shape contract could not have been produced

**archetype:** BUILD
**secondary_archetypes:** VALIDATE, DIAGNOSE, COORDINATE

**Date:** 2026-08-27
**Project:** D1_CATVIEWS (Rule 27 — this instance's only project)
**Window:** 2026-08-27T21:30Z -> 22:25Z

**Portal commits (DEV):** `853c0a38` (ON ORIGIN — moved between two reads this window) · `875182fc` (LOCAL)
**Workspace commits (SITEZ, LOCAL):** `b51d848bf5`

---

## Objective

Apply the two sovereign calls Andrew approved (`"yes approve all recs"`, relayed by `1.0.0_SA_CTO~Z`
@10295), close the still-open clauses his later words had already answered, and — once
`0.4.0_DS_ClientPlatform~Z` landed the producer restructure — retire shape A from the portal.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `bun run typecheck` | `tsc -b --noEmit` x4 | PASS rc=0 | 11.0–11.6s, the build-mode band. ⭐ **Ran a MUTANT CONTROL this window**, because a clean pass on a DELETION is exactly where a non-failing instrument lies: rc=2, `TS2552: Cannot find name 'MdpfCategorySmaL1Node'`. That text also positively confirms the symbol left the compilation rather than merely going unreferenced. |
| `bun run lint` | `eslint .` | PASS rc=0 | 0 errors / the same 7 pre-existing warnings. Added none. |
| `comp-find` | `-i l1_nodes --all`; `-i MdpfCategorySmaL1Node --all` | PASS | ⚠ **`-i l1_nodes` is a SUBSTRING census and swept in `display_l1_nodes`** — an unrelated Client-axis function that must NOT be deleted. The band split (SURFACED vs DOC/CONFIG) is what made the real 3-file surface legible. |
| `ui-smoke.mjs` | 3 renders, `--select`, `--click` | PASS | Two states READ, not merely captured. One `--click` failed and **its diagnostic was the finding** (`ALT Strategies›$0.00`, no `M`). |
| `safe-commit.sh` | 3 commits, two repos | PASS (1 refusal) | The refusal was a real gap — see postmortem 4. |
| `git` | `ls-remote`, ancestry | PASS | Every commit claim carries a bogus-hash negative control. |

---

## Work Completed

1. **`853c0a38`** — CALL 1 (`idvz`/`pfde` INSIDE ETF Strategies; 4+2 over a 6-member domain, MECE
   closes) and CALL 2 (cottonwood's SMAs card populates). **The un-noded array is DISSOLVED, not
   emptied** — the category no longer exists and the members were re-homed.
2. **`b51d848bf5`** — both `STILL OPEN` clauses in this lane's own ANDREW_DIRECT records closed
   **on the normative line**, not by append. One of them asserted the fixture *"places them OUTSIDE
   both buckets"*, which had become false; an append would have left the false sentence standing as
   the block a reader opens first.
3. **`875182fc`** — **SHAPE A RETIRED.** `MdpfCategorySmaL1Node`, `l1_nodes`, `un_noded_members`,
   the `l1_nodes` branch, `L1Row.strategyId`, the un-noded disclosure block. Fixture re-derived
   **from the producer's registry table** rather than hand-authored.

⭐ **The branch carried its own removal condition in writing and this lane wrote it.** *"When the
producer emits SMA as `children`, this branch goes unreachable and SHOULD BE DELETED."*
`mdpf_category_registry.py @14b077f559` met it. **A removal condition that is met and not acted on
is worse than one never written down — the next reader sees a documented blocker and infers it
still blocks.**

⭐ **The warning MOVED rather than dying with its carrier.** The deleted type's docstring held the
crossing-cuts warning; `strategy_id` OUTLIVED the type, so the trap outlived it. It now sits on
`MdpfCategoryMember.strategy_id`. **Retiring a carrier must not retire its criteria.**

---

## Decisions Made

- **Did not edit `formatAUM`.** A zero row reads `$0.00` while siblings read `$X.XXM`, but that is a
  SHARED exported helper whose sub-$1000 branch is CORRECT in general ($500 must not render
  `$0.00M`). A display-context effect surfaced by the new zero bucket — not a defect to patch from
  this lane for one panel's cosmetics.
- **Invented no UI for `absent_reason`.** The producer refuses to emit without a reason and the
  renderer discards it; whether a zero node should render at all is Andrew's under *"invisible
  otherwise"*. Surfaced to `2.0.0_SA_COO~Z`, not resolved.
- **Reported that the deletion appears to close site 2 of another lane's site ledger — and did not
  mark it closed.** That ledger is `0.4.0_DS_ClientPlatform~Z`'s and `3.0.0_SA_CVO~Z`'s.
- **Passed committer identity per-invocation** rather than setting `--local` git config in a
  checkout ~6 seats share, which would have stamped their commits with this serial.

---

## Blockers

**None.** Two questions surfaced upward (zero-node render; `absent_reason` surface). Neither blocks.

---

## Postmortem — six, and two roots

**1. ⛔ I ASSERTED A QUESTION WAS OPEN WHILE THE ANSWER SAT IN A FILE I HAD NOT OPENED.** `853c0a38`
says *"nothing external settles which plane the member list is on."* `members_for(view_path)`
filters a module-level constant BY VIEW PATH ONLY — no firm parameter (`registry:416-423`). The
member set is FIRM-INVARIANT BY CONSTRUCTION. **The renderer's subtitle was right and my fixture
was the wrong surface**, and I had framed my own artifact's defect as an unresolvable fork.
Corrected inside `875182fc`.

**2. AND THE FIXTURE HAD THREE MORE DIVERGENCES, ALL MINE, ALL ALREADY COMMITTED** where other
seats read it as the shape contract: prefixed `sma_*` member_ids the producer never emits (and
inconsistently — `idvz`/`pfde` had no prefix); cottonwood pruned to one bucket / one member when
`:937` emits BOTH buckets for EVERY firm; and inflection carrying `members_present=false` WITH
`render_state: "present"` and NO `absent_reason` — **a block the producer raises `ViewPlaneError`
rather than emit.** I had authored a test double that could not have been produced.

**3. A FALSE CLAUSE IN MY OWN TYPE COMMENT.** `absent_reason` was documented as *"the node renders
no tile at all, so there is no surface to show it on."* Measured false — the renderer selects cards
from `view_plane.peers` and reads neither `members_present` nor `render_state`.

**4. `safe-commit` refused the portal commit: no committer identity in the submodule.** The
workspace root has one (`0.0.0_AB_MSTR`, the shared-device convention); the submodule has none, and
`safe-commit` sets author but not committer. Not a defect I introduced — but the refusal text was
right that a tool's stdout is the tool describing itself, and I verified from `git log` both times.

**5. TWO INSTRUMENT TRAPS I HAD ALREADY BANKED AND HIT ANYWAY.** (a) The edit script assumed LF and
every needle missed — **caught only because the writer refuses to write ANY file unless all needles
match**; the guard cost nothing and saved a silent no-op that would have read as success. These
portal files are CRLF while the workspace `.md` files are LF, so neither could be assumed. (b) A
quoted heredoc double-unescaped `\\r\\n` into real newlines, corrupting the very function meant to
handle newlines. Banked as `harness-heredoc-unescapes-double-backslash`. It did not fire.

**6. ⛔ I REPORTED A MEASURED CEILING THAT DOES NOT EXIST.** Four `send_message` refusals
(*"body is EMPTY"*) led me to hypothesise a body-size limit; a bisect returned a clean monotone
result (110 ✓, 150 ✓, 1,050 ✓, 2,600 ✗, 5,500 ✗) and I stated it to Andrew as fact. **Then a 2,782-char
body delivered — longer than one that had been refused.** The real cause was a malformed `body`
parameter tag; the guard's message was literally accurate. **The bisect itself was the confounder:
shortening the body IS re-issuing the call, so size and tag-wellformedness moved together on every
probe.** The discriminating test cost one command and I skipped it — **re-send a KNOWN-FAILING body
UNCHANGED.** Banked as a third instance on `confounded-variables-i-pick-the-one-in-hand`.

⭐ **THE TWO ROOTS.** Postmortems 1–3 are one thing: **I reasoned about producers, renderers and
fixtures from what I remembered authoring rather than from what the files say** — and every one was
found by finally opening the file, not by thinking harder. Postmortems 5–6 are the other: **I
assumed an instrument's behaviour instead of measuring it** (line endings, heredoc escaping, a
transport limit). ⛔ **And 6 is the expensive class, because a monotone bisect reads as STRONGER
evidence than a single observation — so a confounded bisect is more likely to be published than a
confounded glance, and this one reached the sovereign.**
