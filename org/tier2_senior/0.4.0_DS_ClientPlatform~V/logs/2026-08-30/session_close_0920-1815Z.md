# 0.4.0_DS_ClientPlatform~V — 2026-08-30 0920–1815Z — INF-ONEWRITER closed at CORRECT, PB-1 scored, R7 carried and EXECUTED

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, DEPLOY

## Window

0920Z (close of `abdcf842e5`, the previous log) → 1815Z. **8 commits**, all authored
`0.4.0_DS_ClientPlatform~V`. A device-side pause 09:59Z–12:52Z (0.0.0_AB_MSTR 87350) sits inside
this window; the ~11:18Z and ~12:18Z scheduled fires happened during it and were read afterwards.

| commit | UTC | what |
|---|---|---|
| `6ab4c76a0f` | 09:26Z | `layer_dependencies` declared — unblocked AE's (iii) |
| `bc42f4d35b` | 09:41Z | pre-redeploy baseline, arm B pinned by VersionId |
| `e88205d404` | 13:14Z | **the two-arm EXERCISED read** — both arms PASS |
| `c7e1199b79` | 13:29Z | P2F-MARKER-DS face repair — INVALID → VALID |
| `924d560a32` | 13:43Z | **PB-1 scored** on the fire it names, bytes bound to the run |
| `5dbb7c7795` | 15:20Z | the two-arm acceptance TEMPLATE made durable |
| `865648b24b` | 15:50Z | template amend — comparison vintage is the PACKAGE-resolved commit |
| `f35367d264` | 17:54Z | **Andrew card (6) EXECUTED** — 8 objects deleted, ledger closed |

## Work done

### 1. INF-ONEWRITER: field, baseline, read — closed at CORRECT

`layer_dependencies: ["pandas","pyarrow"]` derived from **my own ast census** (22 modules = 13
stdlib + 5 local + 4 third-party; boto3/botocore are RUNTIME_PROVIDED, not layer, so declaring them
would assert a layer content that does not exist). Zero residual. The layer was **opened** on a
different instrument from the config read that raised the block — the live function's 08-29 run,
zero ImportError, parquet written. Refusal EXERCISED: rc=1 without the field, rc=0 with, tree
restored by digest.

**The pre-redeploy baseline was the window's highest-value act.** Arm B compares the chain's own
last stale output — an object the second writer overwrites ~37 min later daily. On a non-versioned
bucket it would already have been gone and arm B discovered unrunnable AFTER the apply. Checked
rather than assumed: versioning Enabled, both writes preserved, arm B pinned at
`v=jCldmxzmg2ojS068AnJKywgRqyH1bGvD`.

Extended to all four served keys, which changed the finding: **the drift's OUTPUT blast radius is
ONE key of four.** `performance` / `tax_unrealized` / `tax_realized` are VALUE-EQUAL cell-for-cell
between the two writers under the stale package; only `billing` differs.

**The two-arm read** (`e88205d404`): DUE on the log-start-vs-LastModified instrument (fire
11:17:57Z > apply 09:54:24Z). ARM A 4 of 4 VALUE-EQUAL — with billing (15,487 cells) the only row
that discriminates, since three were already equal pre-deploy. ARM B column delta AS REGISTERED.
The period limb did NOT run (the stale object predates `period_*`), reported as N/A not a pass.

### 2. PB-1 (`924d560a32`) — the re-pointed byte limb

Scored on its own fire, with the **grain fix** that the re-point existed for: LastModified
2026-08-29T02:55:49Z unchanged across the 13:30:34Z run and the 13:35:53Z read — a
**non-modification proof**, stronger than the "same minute" capture asked for — and the download
BOUND by `base64(sha256(zip)) == CodeSha256`. Member sha `9256640c…`, **0 code reads in 3,046
lines**, 2 raw hits opened (docstring), live control present. The `12/16 errors=['global']` cycle
state disclosed beside the PASS and measured IDENTICAL on 08-29, so a standing condition and not a
change. Two things left to the issuer: the scope of "run succeeds", and the discharge.

### 3. R7 — the census, the card, and the execution

Four-plane consumer census for `json/mdpf/{firm}`. **The census corrected my own first
measurement**: I took `opal-data-assets` because that is where the current route lives; the readers
named `opal-data-portal-v2`. Two buckets, 8 objects, copies disagreeing by 11,361 B.
Andrew ruled **(6) approved with a gate** — *"just confirm there are no consumers first"* — and both
the gate and the issuer ruled the earlier censuses NOT spent as that confirmation. Re-run
IN-STRETCH 17:43–17:45Z, all four planes zero with firing controls, then **8 deletes by exact key**
17:48:34–54Z, rc=0 on all 8. Recoverable: 8 delete markers over 33 retained versions, VersionIds
printed whole.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | `json/mdpf --files --all`, x4 across the window | PASS | 4,179 → 4,317 → 4,361 → 4,410 hits as the corpus grew; code-extension set stable at 30 |
| `comp-find` | `portal/gold/mdpf` (positive control) | PASS | 1,452 hits / 135,938 files — the control that makes the zeros measurements |
| `proof-of-spec-check.py` | P2F-MARKER-DS, T-B; positional, rc UNPIPED | PASS | VALID both, `@3948c766a7` |
| `comp-system` | regenerate on the PB-1 gate refusal | PASS | prescribed path, not the monitored override |
| `comp-pulse` | pre-commit risk reflex | PASS/HOLD | 6 HOLDs on the manifest commit; citation READ, no bearing |
| `.tools/safe-commit.sh` | 8 commits, `-F`, author-scoped | PASS | msg-verify MATCH on all |

**What failed / gaps found — four, all mine:**

1. **`comp-find` hit the 2-minute tool timeout** on the line-3b control and returned nothing. A
   timed-out census and a true absence are byte-identical in the output; re-run on a longer budget
   rather than recorded as empty.
2. **The literal-Z class, three carriers.** `ls --time-style=+…Z` and `git log --date=format:`
   both render LOCAL under a Z suffix (`format-local:` honours TZ). Caught the first two in-turn;
   the third had **already shipped** in `f779c58f75` ("3948c766a7 (01:00Z)" for an 05:00:15Z
   commit) and surfaced only because CVO asked a question that turned on it — answering from my own
   citation would have produced the wrong grade.
3. **ETag as a content oracle.** Parquet is not byte-deterministic; ETag said DIFFERENT on 4 of 4
   keys where 3 were value-identical, and a pre-written reading in the same script called three
   IDENTICAL on equal byte SIZES. Both halves wrong in one run.
4. **A flattened JSON capture reported "0 delete markers created by this act"** — a broken
   parser's value in the shape of a finding. Caught because it contradicted eight observed rc=0s;
   re-attributed on `LastModified` with a negative control that excluded 10.

## Blockers

**None at this seat.** Everything outstanding is a scheduled fire or another seat's act.

## Current state

- **INF-ONEWRITER**: CLOSED at CORRECT. `inf-silver-chain` applied 09:54:24Z, CodeSha256
  `y7hEGWshBrgT84AAiA+Pggod9XBy1fg8twnVTG1+8l8=`. Step 2 (the dispatch billing leaf) APPLIED
  14:03:13Z — **tomorrow's ~11:18Z fire is the first single-writer day.**
- **PB-1**: PASS, graded. Both halves of Andrew's reserved-delete condition on the record.
- **R7**: EXECUTED. `json/mdpf/` returns 0 current objects in both buckets; restore handles in
  `org/critical_paths/change_management/20260830T1742Z_json-mdpf-firm-delete_andrew-card-6.md`.
  **NOT touched**: the IAM grants and the publisher's `json/mdpf/*` write-prefix declaration — a
  separate follow-on act needing its own word.
- **Template**: `INF_ONEWRITER.TWO_ARM_ACCEPTANCE_TEMPLATE.json` is INF-REDEPLOY's acceptance
  carrier, cited at `@865648b24b` (COO re-pointed the face at `@b8b22d6f18` after I found it one
  amendment behind). INF-REDEPLOY closed with **zero deploy legs left** — seven became re-records;
  D2 alone remains and is optional.
- **Push state (measured, `branch -r --contains`)**: all commits through `865648b24b` on
  origin/CLOUD; `f35367d264` LOCAL, rides the next window.

## Next steps

1. **[0.4.0_DS_ClientPlatform~V]** post-retirement read at tomorrow's ~11:18Z fire — one new
   version on the billing key, in the chain's window, content equal to today's certified write.
   Single-writer now prints as the intended END STATE (retirement on the record), not a finding.
2. **[0.4.0_DS_ClientPlatform~V]** **V-4** at Monday 2026-08-31's first CONVERTING run. Today's
   post-deploy sweep converted ZERO partitions, so `write_complete_marker_verified`'s put+head path
   is still UNEXERCISED and `meta/complete/` legitimately holds 0 objects.
3. **[0.4.0_DS_ClientPlatform~V]** D2's fire, if that optional leg is instantiated.
4. **[2.0.0_SA_COO / 0.0.0_AB_MSTR]** Andrew's word on the remaining cards returns verbatim; the
   IAM/publisher follow-on act is uncut.
