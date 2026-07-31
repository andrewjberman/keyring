# ~B lane: THREE corpus corrections in one window -- git -> user-input -> the real story; capture layer built and fixture-passing -- 2340Z(07-30) - 0215Z(07-31)

**archetype:** MIXED (IMPLEMENT + DIAGNOSE + SCRIBE)
**secondary_archetypes:** VALIDATE, COORDINATE
**Serial:** `0.7.0_AE_CloudOps~B` (PID 25616, Monitor `bydmt7exh`)
**Prior log:** `2026-07-30/lane_B_estate_report_pipeline_build_2032-2340Z.md` @`5e18cc617f`
**Window:** 12 commits, `109e1327c2` -> `f8331b16ea`

> ⚠ **Time note:** `git log --date=format-local` renders LOCAL time; the commit list reads 1940-2212
> which is **2340Z-0212Z**. Not hand-typing a `Z` onto a local clock (MEMORY item 11).

## Arc

The pipeline that was "done" at the last log got its **corpus** corrected three times, by Andrew,
each correction landing one level above the previous debugging.

1. **Root-caused the AI half.** `KIMI_HTTP_400` was NOT the model (the authorized enumeration proved
   `kimi-k2.6` is valid) -- it was `temperature`. Found because the previous commit had widened the
   error handler to keep the response BODY.
2. **RULING 6 -- the corpus is USER INPUT, not git.** A working pipeline on the wrong corpus.
3. **RULING 7/7a -- the product is THE REAL STORY** (<1000 chars/day), from THREE inputs, and the
   capture layer is its own sovereign mandate.
4. **RULING 8 (via CVO) + Andrew mid-turn x4 -- DAY-FIRST layout**, five named subfolders.
5. Built the capture layer. **Fixture 1 passes 7/7.**

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| commit-gate | 6 invocations | PASS 6/6 | every `.py` touch incl. the new `.tools/estate-capture.py` |
| terraform validate | x3 | 1 FAIL -> PASS | the FAIL was mine and useful: a comment about escaping contained a literal `%{` inside the heredoc, so Terraform parsed it as a directive |
| terraform plan/apply | x3 | PASS | 1 add / 3 change / 1 destroy on the kimi-k3 change; 0-diff after |
| `simulate-principal-policy` | A5 pair (prior window) | PASS | NOT re-run this window -- boundaries move to MID-KEY wildcards under the new layout and re-exercise is CVO hold (a), gating the write path |
| comp-surface-check | auto in safe-commit (x12) | PASS | no critical surface |
| comp-pulse risk-reflex | auto in safe-commit (x12) | PASS | denominators printed each time |
| Kimi models endpoint | ONE authorized enumeration | PASS | CVO-authorized, within the per-use designation. 12 ids returned; `kimi-k3` confirmed real |
| comp-which / comp-grep | not run | SKIPPED | this window was transcript/JSON census work over paths I opened directly, plus spec prose; nothing needed routing |

**What worked:** the error-body widening (defect 7's fix) paid for itself on its first failure and
handed over the temperature constraint verbatim. `terraform validate` caught a self-inflicted parser
bug pre-apply.
**What failed:** nothing in the tools. Two shell-level failures were mine -- a heredoc quoting break,
and an `index.lock` collision with a concurrent agent (transient, retried clean, **not** force-cleared).
**Gap found:** none new.

## Work Completed

| Commit | What |
|---|---|
| `109e1327c2` | model MEASURED as `kimi-k3`; error handler keeps the HTTP body |
| `b32c1d89fc` | **the 400 was TEMPERATURE**, not the model |
| `6ea26d7ee8` | attribution bridge (spec-input-5 v2 a-d) |
| `19ebb5f44d` | Kimi timeout 120s -> 300s |
| `32580af5f2` / `82f87697e8` | v3 CORPUS CORRECTION spec + corpus census |
| `5b1511ae71` | **v4 THE REAL STORY** delta spec |
| `20362f2a9f` | persistence contract (CVO binding addendum) |
| `8361fbf6d6` | **RULING 8 recorded verbatim** -- day-first layout |
| `150d45b5b7` | manifest home PINNED at the day root |
| `bbede635d5` | **the capture layer** (`.tools/estate-capture.py`) |
| `f8331b16ea` | Andrew's corpus pointer, measured |

### The measurement that is v4's spine

Harness transcripts store **turn-boundary** input as `type: user` but **MID-TURN** input as
`queue-operation` + `attachment` -- **never `user`**. Ground truth held personally. A naive
`type == "user"` extractor captures **40%** and admits skill bodies as if Andrew typed them.
**The dropped ones were rulings 4, 4a and the standing hold** -- the entire compute-architecture
decision of this build. `queue-operation` appears in **40 of 40** recent sessions.

**Then the fabric produced 6+ more mid-turn instances within the hour**, including two sovereign
rulings at CVO's terminal. Prediction and confirmation, minutes apart, independent.

### Fixture 1 -- PASSES

`467 rows scanned | 74 candidates | HUMAN 14 / HARNESS 60 / UNCLASSIFIED 0 | 8 stored`
**7 of 7 known Andrew utterances captured, all five mid-turn ones included. Zero false positives.**
A naive extractor would have stored 2 of 8.

## Decisions Made

1. **Did not attribute the 400 to the model** even with a plausible story in hand. The enumeration
   refuted it. Recorded the cause as OPEN instead of writing a confident falsehood.
2. **Shipped the EC2 attribution hop LABELLED WITH ZERO MEASURED REACH** (0 of 28 names match) rather
   than silently or not at all. A hop with no reach that LOOKS wired is what this pipeline exists to catch.
3. **Corrected my own printed conclusion** -- I inferred from 2 ledger rows that the verbatim lived in
   `basis` not `ruling`, printed it, and the full census refuted it. **A conclusion I printed myself is
   more dangerous than an assumption because it arrives wearing a measurement's clothes.**
4. **Adopted Andrew's `signed-review` over my `adjudicated`** -- *signed* names the act that matters.
5. **Capture is DEVICE-SIDE** -- forced, not chosen: transcripts are not in the repo or S3, so a
   runner-side design captures nothing and emits a well-formed EMPTY store.

## Blockers

**None are mine to clear.**
1. **[3.0.0_SA_CVO -- hold (a)]** BOTH IAM boundaries must be RE-EXERCISED against the **mid-key
   wildcard** patterns before any `text-input/` or `signed-review/` write path is live. Old
   leading-prefix evidence does not transfer.
2. **[Andrew]** retention ruling -- now covers **his own verbatim words**, not just derived reports.
3. **[Andrew]** site-Z capture path (declared gap) and the Desktop world-model repo having **no remote**.

## Current State

ESTATE REPORT pipeline is **deployed and running** (19 resources, `estate-report-v0.1.0`, instance
`i-04981b6aec3bed86b`, schedule **DISABLED**). The v1/v2 product shipped a real report; **rulings 6/7
superseded its corpus and its output contract**, so it now stands as working machinery pending the v4
rebuild. v4 spec is **CVO-APPROVED** with the persistence contract addendum landed and the manifest
home pinned; **MSTR amended both carriers @95975844cf (LD-0360) before the build ships against it.**

`.tools/estate-capture.py` exists, gate-clean, fixture-1-passing, **no write path live**.

## Next Steps

1. **[0.7.0_AE_CloudOps~B]** Fixture 2 (CVO's session) -- denominator pins at **day close**.
2. **[0.7.0_AE_CloudOps~B]** Re-exercise both IAM boundaries against mid-key wildcards (CVO hold a),
   then the `text-input/` write path.
3. **[0.7.0_AE_CloudOps~B]** Three-source synthesis (text-input + change-**cochange** + deployment-motion),
   then the story contract + validator LAST against a known-good corpus.
4. **[Andrew]** retention ruling; site-Z capture; Desktop repo remote.

## The thing worth carrying

**NO AMOUNT OF RIGOUR INSIDE A FRAME VALIDATES THE FRAME.** Eight defects were found and fixed
correctly in the prior window -- every one a defect in how faithfully the pipeline read *git*. The
correction came from the one participant who was not inside the measurement. And tonight's smaller
sibling: **a shared misreading is invisible to review** -- CVO and I both compressed *"git co change"*
to *"git change"* through two approval rounds, and only Andrew NAMING a folder `change-cochange`
surfaced it, because naming forces enumeration where prose permits skimming.
