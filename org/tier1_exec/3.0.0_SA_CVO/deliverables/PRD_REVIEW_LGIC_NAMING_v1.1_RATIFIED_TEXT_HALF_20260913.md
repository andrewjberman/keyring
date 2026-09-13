# PRD REVIEW -- LGIC_NAMING v1.1 @b75a62552d -- the RATIFIED-TEXT half (ENDPOINT + CONTRACTS; L4-R, spine v3.15) -- 3.0.0_SA_CVO

**Archetype:** VALIDATE.
**Reviewer:** `3.0.0_SA_CVO`.
**Requested by:** `1.0.0_SA_CTO`, msg 96427. The notifier's 96415 and 96421 never landed as inbox files; `LGIC_NAMING-S1` records that.

**Read, every item at a pin, UTC 2026-09-13 ~23:1xZ:**
- The PRD `org/missions/D14/LGIC/LGIC_NAMING/prd/LGIC_NAMING_PRD.md` @`b75a62552d`. The working copy is identical: `git diff` is empty and `git status` is clean.
- The endpoint `org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FWD_D14_NAMING_SCHEMA_20260913.md` @`e2210bf34c`, unchanged at HEAD.
- The executable-layer endpoint `ENDPOINT_FWD_D14_EXECUTABLE_LAYER_20260913.md`, for the carried machine-run bar.
- `org/standards/NAMING_SCHEMA.json` @`b75a62552d`, parsed.
- The ~03:2xZ and ~03:5xZ ruling records (@`998b3f0105`, @`38f2268d48`).
- `infra/logic/02_DOCTRINE.md` R1.
- The naming brief @`1b42dbe758`, IV.2.

**Half hash reviewed:** ratified-text `d15cd6217ef5dd6ecadcf1f6463d9a0e630ac8de40a4468960d1ed627e3a071e`, computed by
`.tools/prd_signoff_lib.py` `half_hashes` over the bytes above. The stamp is pinned to it with `--expect-half-hash`, so it
refuses if the half has moved.

## VERDICT: SIGN -- with two corrections returned by pinned line, neither blocking

## ENDPOINT -- 6 of 6 outcomes carried verbatim

**Instrument:** a parser over both documents' FWD blocks, compared field by field -- not a visual read.

| FWD | title | DONE WHEN | ACCEPT | SOURCE |
|---|---|---|---|---|
| FWD-1 | EQUAL | EQUAL | EQUAL | EQUAL |
| FWD-2 | EQUAL | EQUAL | EQUAL | EQUAL |
| FWD-3 | EQUAL | EQUAL | EQUAL | qualifier dropped (correction 1) |
| FWD-4 | EQUAL | EQUAL | EQUAL | qualifier dropped (correction 1) |
| FWD-5 | EQUAL | EQUAL | EQUAL | qualifier dropped (correction 1) |
| FWD-6 | EQUAL | EQUAL | EQUAL | qualifier dropped (correction 1) |

- **FWD-6 at APPLIED is Andrew's ruling** (~18:4xZ card 5, stamped on the endpoint @`e2210bf34c`).
- **The two AT RISK notes are dropped, and the reason holds.** FWD-1 and FWD-3 lost their AT RISK notes because both named the per-slot form question, which S4 closes (brief half, signed by `4.0.0_SA_CRO~D`). S4 does state one spelling per slot. The endpoint's other FWD-1 risk -- no kind for a Lambda -- is closed by the data file: `lambda` is in `kind.values` (20 values), so FWD-1's own example derives.
- **FWD-5's machine-run bar is CARRIED, not dropped.** The executable-layer endpoint's s.6, *"THE NAMING ENDPOINT'S MACHINE-RUN BAR LANDS HERE, AS PROMISED"*, makes it that endpoint's FWD-5.

### CORRECTION 1 (non-blocking) -- four SOURCE lines drop the endpoint's deviation qualifiers

| PRD line | FWD | PRD reads | endpoint reads |
|---|---|---|---|
| 64 | FWD-3 | `brief Part I O3; bar Part III O3` | `brief Part I O3 (as CORRECTED by the ruling -- s.2); bar Part III O3` |
| 75 | FWD-4 | `brief Part I O4` | `brief Part I O4 -- NO Part III bar; cut from Part I alone (s.4)` |
| 89 | FWD-5 | `brief Part I O5; bar Part III O5` | `brief Part I O5; bar Part III O5 RE-CUT to what this brief owns (s.3)` |
| 99 | FWD-6 | `brief Part I O6; bar Part III O6` | `brief Part I O6; bar Part III O6 LOWERED, stated (s.5)` |

**Why it matters.** As written, FWD-5 and FWD-6 name the brief's Part III bar as their source, and those are NOT the bars
this PRD carries:
- The brief's O5 bar is a running check over all 1,912 names, which moved to the executable layer.
- Its O6 bar can only be met by a remediation project; the PRD carries it lowered to APPLIED, as Andrew ruled.

A reader who follows SOURCE instead of ACCEPT grades against the wrong bar.

**Why it does not block.** The ACCEPT lines, which are the bars, are verbatim, and every PIN line resolves to the endpoint
that carries the qualifiers.

`1.0.0_SA_CTO`'s 96427 describes each block as ADDING a SOURCE line. In fact the blocks carry the endpoint's own SOURCE
lines, shortened.

**Fix:** restore the four qualifiers verbatim.

## CONTRACTS -- four rows, each checked against its source

| row | checked against | result |
|---|---|---|
| 1 `NAMING_SCHEMA.json`, produced | the file, parsed at `b75a62552d` (9,275 bytes) -- see the list below | every enumeration the row names is present |
| 2 the grading rule, produced | not yet written (cell N2), and the row says so | NOT EVALUATED -- nothing to read yet. The shape the row states (three verdicts, RAISE, no fourth) matches the data file's `grade` block |
| 3 the registry's rows, consumed | seed `infra/logic/05_IDENTITY_SPINE.md` @`b75a62552d` (9,311 bytes); rows produced by `LGIC_ENFORCE` under ruling (a) | holds |
| 4 the key string, consumed (ruled) | ruling @`998b3f0105` card 1; doctrine R1 | the substance holds; the labelling is correction 2 |

**What row 1 was checked against.** The data file at `b75a62552d` carries:
- `key`: the grammar, 6 tiers and 4 scope classes;
- `bucket`;
- `resource`: the grammar and the last-slot rule;
- `kind`: 20 values, and `by_type` with 18 types;
- `types_not_graded_by_kind` with 15 types. That makes 18 + 15 = 33, disjoint, which equals `node_type_vocabulary.denominator`;
- `cadence`, `secret`, `log_group` and `iam_policy`;
- `firm_forms`, 4 rows;
- `refused_tokens`: `bd` and `mockadv`;
- `system`;
- `grade`: the signature, three verdicts (CONFORMANT, ALIAS, OUT-OF-PATTERN), and RAISE on a name it cannot place.

**Firm forms.** The data file's `49financial`/`49f`, `inflection`/`inf` and `cottonwood`/`cot` match the ~03:5xZ ruling
(@`38f2268d48` card 2). `demo` uses one token for both forms, so no new short form is added. `bd` is refused.

**The counterpart is NOT EVALUATED, not passed.** `LGIC_ENFORCE`'s PRD does not exist, so there is no counterpart text
to compare. The section binds `LGIC_ENFORCE` to state the same four rows from its side. This seat reads the two against
each other at `LGIC_ENFORCE`'s L4-R.

### CORRECTION 2 (non-blocking) -- row 4 labels the RENDERED key string as the RULED one

**What was ruled.** Andrew ruled `{source}/{scope}/{tier}/{table}/{partition}`, *"the same string in every bucket"*
(@`998b3f0105`, card 1). Doctrine R1 writes the same string with a trailing `...`.

**What the PRD carries.** Row 4, S1 and the data file's `key.grammar` carry
`{bucket}/{source}/{scope}/{tier}/{table}/{partition}/{object}`. That is the ruled string with its container and its
leaf, and the naming brief's IV.2 already renders it that way (@`1b42dbe758`, line 104).

**Why the substance holds.** The segment order is the ruled order.

**Why it still matters.**
- Row 4 calls the seven-segment form "ruled".
- `key.grammar` sits beside `same_string_in_every_bucket: true` with `{bucket}` inside the grammar.

So `LGIC_ENFORCE`'s `key()` builder could read `{bucket}` as a KEY segment and write a bucket name into every key.

**Fix.**
- Row 4 quotes the ruled five-segment string verbatim, and names `{bucket}` as the container and `{object}` as the leaf.
- The data file says the same in a field `key()` can read -- for example, the ruled segments listed apart from the container and the leaf.

## NOT CLAIMED

- **Anything in the brief half** -- S1-S13, the cells, paths, coverage and surface manifest. That half is `4.0.0_SA_CRO~D`'s, signed @`98ff34e45f`.
- **That S4, the per-slot split, is Andrew's.** It is ratified at L4 by `1.0.0_SA_CTO` and is revertible on his word, as the PRD says.
- **A disposition of `LGIC_NAMING-S1`**, the notifier's undelivered requests. It is L8 input for this project's first round.
