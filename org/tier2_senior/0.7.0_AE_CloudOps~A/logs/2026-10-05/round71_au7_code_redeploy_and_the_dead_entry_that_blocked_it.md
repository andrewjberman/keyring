# Round 71 AMGT-au-7: one code-only redeploy, a 16-hour-dead entry that formally blocked it, and a false zero that nearly hid it -- 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY

## Objective

Execute `AMGT_RESAPP.TO-AMGT-au-7` on the GO at `b411936d8a` (msg 29754). AMENDMENT 1 reduces it to
**ONE leg, code only**: build and upload one artifact at `a53eaf74c5` carrying au-1, au-3, au-4 and au-6,
then one code-only `safe-apply` of `opal-amgt-scoped-api`. `memory_size` stays 1769. The gold leg LEAVES
this act (AMGT_HARVST is the gold mention table's one writer), so AC1 grades c34/c36 only and c35 is the
issuer's after HARVST's next build. Four CTO conditions. au-6 is Andrew's Lead Panel speed issue, and
condition 3's measured before/after is what gates his DSGN PROD promote.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| comp-find | `comp-find 'TO-AMGT-au-7' --files` | PASS. 13 hits / 119026 files scanned, HEAD band 2; located the order and the GO message. Denominator read, not just the top hit. |
| comp-find | `comp-find 'deploy_ledger' --name --limit 10` ; `comp-find 'open_deploys' --name --limit 20` | PASS. First gave `.tools/deploy_ledger.py` (230 hits, HEAD band 230 -- a name census, so the band is the whole hit set). |
| comp-read | `comp-read infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh --for "flags, build-only, upload target, content manifest"` | ADVISORY. 738 lines / 73 sections; surfaced `BUILD_ONLY` at :108-125 and the content-diff block at :723-738, with 42 qualifiers. **It named the flag but not the semantics that mattered**, so the header and the upload boundary were read at the bytes (`sed -n '105,132p'`, `'718,738p'`) before use. The shape read is the index, not the answer. |
| comp-which | `comp-which "how do I open a NEVER-2 open_deploys deploy ledger entry"` | **NO CURATED RULE MATCHED** -- the tool said so in as many words. The fuzzy top-3 (comp-schedule 0.57, comp-freshness 0.42, comp-lambdamap 0.38) were NOT taken; picking the first-ranked here is exactly what its own warning forbids. The tool was found instead in this seat's round-70 log. |
| deploy_ledger.py | `open` / `close-leg` x4 / `close` | PASS. One entry, 4 legs, opened and committed **before** the first apply, each leg closed against its own `proof_required`. |
| proof-of-spec-check.py | on the instance, then on the committed bytes | **VALID (rc=0)**, 10 of 10 controls discriminating, 0 DID-NOT-DISCRIMINATE, rollback named. First pass was INVALID with 14 violations; see Decisions. |
| comp-schedule / comp-iam / comp-adversary | declared by the issuer at the cut | Carried forward, not re-run. comp-adversary's base arm is this act's negative control: on `GS//XHnV` the same instruments that pass now all FAILED. |

## Deployment Sequence

| # | Step | Evidence |
|---|---|---|
| 1 | Base re-read **live**, not from the order | `GS//XHnVd4+bBIg1VU++r1fp9v495pi6jKFat9KbEYE=`, 1769, LastModified `2026-10-05T08:23:19Z`. Equals the declared base, so no STOP. |
| 2 | `.open_deploys` union over **every** live worktree | 47/47 trees resolved, 55 distinct entries, per-tree denominators printed. Found ONE open entry on this function. See Verification. |
| 3 | Issuer ruling on the wait clause | msg 29756: PROCEED; the CORPUS entry is measured dead. Acked. |
| 4 | NEVER-2 entry opened + committed BEFORE any apply | 4 legs, DEPLOY genre, `@d3a58f6f61` |
| 5 | Detached checkout at the pin | `git worktree add --detach /c/tmp/au7-pin-r71 a53eaf74c5`; HEAD `a53eaf74c5c59c70fa28ecb854ee2370f7bfe16d`, `status --porcelain` 0 lines |
| 6 | `--build-only` (no upload) | `CONTENT-DIFF SUMMARY: files 364, IDENTICAL 361, CHANGED 2, ADDED 1, REMOVED 0` against the deployed sha. SIZE 253,923,711 B of 262,144,000 (96.9%, 8,220,289 spare). Cold-start FATAL `[]`, request-time break `[]`, ISOLATED 3/3. |
| 7 | Real build + upload | VersionId `WG8u2w_ngxnIWFRsCrae3S4nSD2Og8ux`, ContentLength 41,214,968, `content-sha256 wbIT0PHvxKIgJvgVy+u0XhLuSXFK5dUE/wypJPDcf8o=`; CONTENT-DIFF **byte-identical to the --build-only pass** |
| 8 | Independent `head-object` re-read | Agrees with `upload_verified`'s own read-back. Two instruments, one answer. |
| 9 | TF config identity checked **by content** | `scoped-amgt-api.tf` sha256 `1ec09a06aeb1dec3` at the pin, at shared HEAD and in the worktree -- so the apply could run from the shared tree without importing a config difference. |
| 10 | Full plan, saved | `terraform plan -out=C:/tmp/au7.tfplan` |
| 11 | Plan graded from `show -json` | 49 `resource_changes` -> 48 no-op + 1 update = `module.scoped_amgt_api.aws_lambda_function.this`. destroy 0, IAM 0, route 0, gateway 0 across all 49. Only 3 of 46 attributes move: `s3_object_version`, `source_code_hash`, computed `last_modified`. `memory_size` 1769 -> 1769; role, layers, runtime, handler, architectures, timeout unchanged. |
| 12 | `safe-apply` of the **saved** plan | `.tools/safe-apply.sh apply -input=false C:/tmp/au7.tfplan` -- the graded artifact IS the applied artifact, so no re-plan drift could enter |
| 13 | Live verify + 0-diff | `CodeSha256 wbIT0PHv...`, 1769, `19:14:52Z`; re-plan `No changes` with `-detailed-exitcode 0` |
| 14 | leadpanel AFTER, **first**, 92 s after the apply | Before any other check. See Verification. |

## Verification

AC1 `c34` YES (reads 11, objects carrying score 572, non-200 0) and `c36` YES (covered 95, rows 292,
missing 0), exit=0. AC3 nine cells all SERVED YES, exit=0. AC2 `c38` YES -- all 9 Lead Panel reads warm
under the 2000 ms bar, 0 over, worst 801 ms -- and AMENDMENT 1 makes it **report-only**, so the PASS is
reported rather than relied on.

Every cell printed a **non-zero population**, so no YES is a vacuous pass over an empty set. Two cells
carry their own negative arms, which is what makes the set a regression test and not a smoke test: `c26`'s
`PASS C2 the control ZZZZ_US_Equity thesis still answers 404` shows the 200s discriminate, and `c23`'s
inverted-window arm shows the error branch still answers. `c25` cross-checks two planes -- the ledger news
stamp against the overlay's `harvested_news` last_run -- and they agree on all three names.

**Condition 2 is wider than AC3, and the gap is in the cut.** The signed CTO half requires `c14, c15 as
amended, c23-c33` = 13 cells; AC3's invocation reaches 9. The four outside it were run anyway: `c14` YES,
`c27` YES, `c28` YES, and `c15` YES with **cold 3 of 3** after a measured ~23-minute idle (1929.8 / 1931.18
/ 1934.12 ms, init 226.54 / 222.48 / 221.4), worst run 1934 ms against its 5 s rollback bar. So condition 2
reads **13 of 13** and is fully discharged. Filed as surprise row `AMGT_RESAPP-Z-S354` and kept working;
re-cutting AC3 is the issuer's call, not this seat's.

`c15`'s `AMGT_SEGMENT` per-segment limb is **MET this round** where round 70 recorded it NOT MET (0 of 6
invokes emitted any line; now 3 of 3). That is a change in the instrument's reach, not in the bar, and it
also supplies the per-segment times condition 3 asks for: identity 514-540 ms, import 759-778,
gold_chatter_daily 330-348, _list 45-50, _get 27-37, _decode 175-187.

**The speed answer (condition 3).** Warm chatter 9.2-12.3 s -> 0.56-0.65 s, about 17x. Warm price rankings
3.9-5.2 s -> 0.06-0.24 s, about 30x. Cold chatter 14.4-19.2 s -> 7.3-7.8 s, about 2.4x. All 9 routes faster
on both columns, all still 200. **What remains slow is the cold start**, 7.3-7.8 s, and `served_cache.py`
cannot reach it by construction: a per-container memo is empty on a cold container. Reported, not fixed,
not a rollback trigger. Raw output saved as `LEADPANEL_AFTER_au7.txt @76063becb8` with its provenance and
the caveat that these are two single runs against live data, not a controlled benchmark.

## The dead entry that formally blocked this act

Section 1 says to wait if another entry on this function is open. One was: `amgt-corpus-r36-al5.json`
(AMGT_CORPUS r36 CRPS-al-5, `2.0.0_SA_COO~X`, status OPEN, all 4 legs `proof: null`). It lives **only** on
branch `wk-NFRA_OPLGTW-15-r16 @d5899bf32b` and is absent from shared HEAD -- the producer-on-a-branch
shape NEVER-2's union exists to catch.

Measured dead three independent ways rather than reasoned dead: its 4.0h window expired `02:34Z`, 16.3
hours earlier; its named base `aoQ+WrefJ` is not the live sha; and the function was redeployed after that
window closed, by at-6 under its own closed entry. Its own base re-read would therefore STOP it, so it
cannot fire without being re-cut.

That measurement is **not the same as authority to clear the clause**. The entry belongs to another lane
and my order says wait, so the question went to the issuer with the three measurements attached while I
did the build and CONTENT-DIFF, which did not depend on the answer. Ruling msg 29756 came back PROCEED in
under two minutes. Closing the entry remains `2.0.0_SA_COO~X`'s act and was not done here.

## A false zero that nearly hid it

The **first** union read parsed `git worktree list --porcelain` with `awk '{print $2}'`. This device's
workspace path is `C:/Users/Opal Bloomberg/Desktop/ajb_workspace`, so awk split it at the space and 12
trees collapsed to the bare string `C:/Users/Opal` -- each then reading **0 entries**.

Zero read exactly like absence. It passed shape: 47 rows printed, counts printed, a union printed. Had I
taken it, the al-5 entry would have stayed invisible and I would have deployed into what I believed was a
clear field, with a printed denominator "proving" it. Re-read with `sed -n 's/^worktree //p'`, which keeps
the whole line: 47/47 resolved, 0 unresolvable, 5-29 entries per tree, and al-5 surfaced. No conclusion in
this round rests on the first pass. This is the banked path-with-a-space lesson arriving in a new costume;
the tell was that 12 of 47 rows were the *same truncated string*, which no real worktree list produces.

## Decisions Made

| Decision | Why |
|---|---|
| Ask the issuer about al-5 rather than clear it myself | The entry is another lane's and my order says wait. Measuring it dead is evidence, not authority; CLAUDE.md forbids adjudicating another seat's scope wider or narrower. |
| Do the build while the question was open | The build and CONTENT-DIFF are read-only and do not depend on the answer. `--build-only` exists precisely so the whole gate can run with no upload and no activation. |
| Apply the **saved** plan, not a fresh one | A re-plan at apply time can differ from the plan that was graded. Applying the saved file makes the graded artifact and the applied artifact the same object. |
| Run `leadpanel --label after` first, before AC1/AC2/AC3 | The cold column is perishable. Two cold-dependent reads competed for one un-warmed container and only one could be protected; condition 3's measurement is the one Andrew is waiting on. `c15`, the other, was taken last after a measured idle and still got cold 3 of 3. |
| Run the four cells outside AC3 | The signed CTO half names them. Cheap, read-only, in-lane, and it turned a partially-discharged condition into a fully-discharged one. |
| Read the CONTENT-DIFF at the lines, never from rc | The script's own comment says the diff is "a report, not a gate: CHANGED/ADDED/REMOVED lines exit 0". An rc-only reading would pass a fourth file silently. |
| Not flip the order's `<status>` | The order's `<paths>` does not grant `task-orders/`, and `git log` on the at-6 order shows every flip committed by the issuer. Measured, not assumed. |
| Not cite the HALTGT pass | cloud-ops: the checkpoint cannot see a `~lane` serial's mail and a live Monitor moves the message first, so its pass is uninformative here. Nobody cites a HALTGT pass. |
| Fix the proof instance against the checker rather than argue with it | First pass INVALID with 14 violations -- enum-illegal `status` strings carrying nuance, `kind`/`deployed_state` outside their enums, a root key the schema does not allow, an object where `surprises` wants a row-id string, `artifact_covered_by` citing criterion ids that did not exist, and an AC3 invocation I had abbreviated with `...`. The last one matters most: **a recorded invocation that is not the criterion's leaves the record ungoverned**, so it was restored verbatim. Nuance moved into `observed` / `output_evidence`, where it belongs. |

## Files Modified

| Path | Commit |
|---|---|
| `.open_deploys/amgt-resapp-r71-au7.json` | opened `d3a58f6f61`, removed at close `ba5f7871ed` |
| `change_management/20261005T1901Z_amgt-resapp-r71-au7_deploy_completion.md` | `d3a58f6f61` -> CLOSED 4/4 `ba5f7871ed` |
| `deliverables/0.7.0_AE_CloudOps~A/AMGT_RESAPP.TO-AMGT-au-7.the-code-redeploy.proof_of_spec.json` | `ba5f7871ed`, VALID on the committed bytes |
| `surprise-channel/investigations/INVESTIGATION_v1.md` | `ba5f7871ed`, row `Z-S354`; appended in the SHARED tree per CLAUDE.md 14b's inversion for an append-only channel; re-parsed after the write to 765 rows, 0 duplicate ids |
| `deliverables/0.7.0_AE_CloudOps~A/LEADPANEL_AFTER_au7.txt` | `76063becb8` |

No `.tf` edit, no IAM change, no gold or store write, no S3 delete, no vendor call, no shared-branch push,
no portal promote.

## Blockers

**None.** Nothing is owed by this seat on au-7.

## Current State

`opal-amgt-scoped-api` runs `wbIT0PHvxKIgJvgVy+u0XhLuSXFK5dUE/wypJPDcf8o=` at memory 1769, carrying au-1,
au-3, au-4 and au-6. Every criterion in the order passes and so does the wider condition-2 set, 13 of 13.
The NEVER-2 entry is CLOSED with all four legs proven and the sentinel removed. The named rollback, prior
artifact version `.Sj7rblal1sHPyETvJW_ZKXvOzeGVds3`, is retained and untouched.

**Push state: LOCAL @76063becb8**; `origin/CLOUD` reads `01a47ac2e7` (`git ls-remote`). Pushing `CLOUD` is
`0.0.0_AB_MSTR`'s on Andrew's word, not this seat's.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** `c35`, after AMGT_HARVST's next hand-run gold build -- that build is what carries
   au-3's `url` column.
2. **[`2.0.0_SA_COO~Z`]** Condition 3's second half: the plain-words speed note for Andrew, through
   `0.0.0_AB_MSTR~Z`. The measurement it needs is `LEADPANEL_AFTER_au7.txt @76063becb8`, including what
   remains slow.
3. **[`2.0.0_SA_COO~Z`]** Surprise row `Z-S354`: whether AC3 should be re-cut to match the half it was
   signed under.
4. **[`2.0.0_SA_COO~X`]** Close `amgt-corpus-r36-al5` SUPERSEDED. Measured dead; `2.0.0_SA_COO~Z` said it
   is asking.
5. **Open design question, nobody's task order yet.** If the warm numbers do not settle Andrew's speed
   issue, the remaining item is the 7.3-7.8 s cold start, which no redeploy of this shape can fix -- a
   per-container memo is empty on a cold container. That is a design call, not a deploy.
