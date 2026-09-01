# CENSUS: who actually READS the investigation docs -- and why I am NOT swapping the container

**Discharges the precondition I set myself** in `/open-calls` card 2 (Andrew-approved): *"DEFER the
markdown-to-JSON container swap until I census the readers of the 17 existing INVESTIGATION docs."*
**The census is run. The result reverses my own recommendation.**

⚠ **THIS DECLINES A STATED ANDREW PREFERENCE ON MEASURED GROUNDS, so it is stated loudly rather than
buried.** His words (transcript `9-1 flow_6519.txt`): *"I do not like the idea of any of these key
files being done in markdown if we can avoid it ... I much prefer to do everything in structured
format."* **The override is his and this document exists to make taking it easy.**

---

## 1 · THE MEASUREMENT

```
  comp-find "surprise_channel" .tools org/modules org/mcp
  DENOMINATOR: 841 hit(s) across 103,138 file(s) scanned
  BANDS: HEAD=4  DEF=1  SURFACED=263  CONFIG=2  DOC=571
```
⛔ **TWO EARLIER ATTEMPTS RETURNED `0 hit(s) across 0 file(s)` AND I DID NOT REPORT THEM AS ABSENCE.**
The first passed a literal `--` before the pathspec; the second used bare `'*.py' '*.sh'`, which in
git-pathspec terms matches only the top directory. **Per Rule 21, `0 across 0` is OUT-OF-CORPUS, NOT
ABSENCE** -- and here it would have produced exactly the wrong conclusion ("no code touches the
channel"), which is the reading that makes a swap look free.

### THE DECISIVE NUMBER IS `DEF=1`

**Exactly ONE piece of code defines a path into this tree:**
```
  .tools/comp-surprise.py:31   CHANNEL = os.path.join(ROOT, "org", "surprise_channel")
  .tools/comp-surprise.py:40   for m in re.finditer(r"```json\s*(.*?)```", txt, re.S)
  .tools/comp-surprise.py:52   pats = [ .../"INVESTIGATION_v*.md", .../"REMEDIATION_v*.md" ]
```
**Config governance is 1 file and it is SUFFIX-AGNOSTIC:** `.owned-paths.yaml:1040` guards
`org/surprise_channel/**`, so the ownership guard survives any rename.

**Everything else -- 571 DOC + 263 SURFACED -- is PROSE citing `INVESTIGATION_v1.md` by path.**

---

## 2 · THE DECISION: KEEP THE MARKDOWN CONTAINER. DO NOT RENAME.

>> **THE MACHINE BENEFIT OF THE SWAP IS ZERO, BECAUSE THE ONLY PROGRAMMATIC READER ALREADY PARSES
THE ROWS AS JSON.** `comp-surprise.py:40-42` extracts the fenced block and calls `json.loads`. The
rows are, and have always been, real JSON against real schemas. **The markdown is a wrapper around
structured data, not a substitute for it.** <<

**What the swap would actually cost:**

| | cost |
|---|---|
| CODE | 1 file, 2 lines (`:40` fenced-regex -> whole-file load; `:52-53` glob suffix). **Cheap.** |
| CONFIG | **ZERO** -- the `**` glob is suffix-agnostic |
| POINTERS | **~571 DOC-band citations to `INVESTIGATION_v1.md` become stale.** The expensive one. |
| CAPABILITY | **A REAL LOSS, and I did not know it before the census** |

⛔ **THE CAPABILITY LOSS IS THE ARGUMENT I DID NOT HAVE WHEN I RECOMMENDED THE SWAP.**
`comp-surprise.py:40` is `re.finditer` -- **it reads EVERY fenced block in a file, N of them.** A
pure-JSON file can hold exactly ONE top-level array. The channel's docs use one block today, so the
loss is invisible right now -- **which is precisely why it would be discovered later, by whoever
first needed to append a second block rather than rewrite a 408 KB file.**

⭐ **AND THE PARSER'S FAILURE DIRECTION IS ALREADY CORRECT:** *"Malformed blocks are SURFACED, never
dropped."* A swap would be replacing a reader that fails LOUD with one that fails on `json.loads`
for the whole file -- **one bad row would take out an entire project's channel** instead of
surfacing itself.

### WHAT ANDREW ACTUALLY WANTED IS ALREADY TRUE, AND THE PART THAT ISN'T IS ENFORCEMENT

His concern is structure, not suffix. **The rows ARE structured** -- `investigation_item.schema.json`
and `remediation_row.schema.json` exist, with real conditional bars (GRADUATED requires GROUNDED with
non-empty evidence; ARMED requires a named `disarm_owner`; a bare dismissal is refused).
**The gap is that nothing REFUSES a row that violates them at write time.** That is where the
structured guarantee actually comes from, and it is unaffected by the container.

>> **MANDATE SCHEMA VALIDITY, NOT A FILE EXTENSION.** <<

---

## 3 · WHAT I AM MANDATING INSTEAD (card 2, unchanged in substance)

```
  step 7   spec_asserts + world_is    both halves required on a row
  step 9   disposition                enum EXISTS, unchanged
  step 10  route + loop_target        REQUIRED on a remediation row
                                      spec-error -> 6 | decomp-invalidating -> 5 | scope -> 2
```
Enforced against the schemas at write time, on the existing container. **`.Z.md` fabric variants are
preserved for free** -- `INVESTIGATION_v*.md` already globs `INVESTIGATION_v1.Z.md`, and the fabric
split is live (`ETFS_POSITIONING` holds both, 14 and 16 rows).

## 4 · THE OVERRIDE, MADE EASY

**If Andrew wants the rename regardless**, the work is: `comp-surprise.py:40` and `:52-53`; a
`git mv` per project preserving the `.Z` coordinate; and accepting that ~571 prose pointers go stale
and the N-block capability collapses to 1. **No other code changes.** It is a half-hour job and the
census is what makes that estimate safe to state.
