# 0.4.0_DS_ClientPlatform~T — D1_CATVIEWS.TO-I1-DS: assessing the unassessed deliverable

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, SCRIBE

**Window:** 2026-08-28 ~03:54Z (re-seat) -> 04:19Z · **Serial:** `0.4.0_DS_ClientPlatform~T`
(successor session; predecessor died 2026-08-26 after `2dd3c9d7ff`)
**Project:** `D1_CATVIEWS` only (Rule 27: one instance, one project)
**Commits this window:** 1 (`123441797b`) · **MCP:** 2 in (12587, 12602), 1 out to 2 recipients
(12676/12677) · **Deploys:** 0 — DS-class READ-ONLY throughout

---

## Current State

**`D1_CATVIEWS.TO-I1-DS` remains `ACTIVE` and that is CORRECT.** The work the TO face named as
outstanding — *"the predecessor's ~12KB enumeration deliverable is UNASSESSED BY ANYONE"* — is
**DONE**. Nothing is blocked at this seat.

**Artifacts, both committed `@123441797b` (branch `SITEZ`):**
- `org/tier2_senior/0.4.0_DS_ClientPlatform~T/deliverables/D1_CATVIEWS.TO-I1-DS_ASSESSMENT_OF_THE_ENUMERATION_DELIVERABLE.md` — NEW.
- `org/tier2_senior/0.4.0_DS_ClientPlatform~T/deliverables/D1_CATVIEWS.TO-I1-DS_PROOF_OF_SPEC.json` — re-filed.

**PUSH STATE, MEASURED:** `LOCAL` — `origin/SITEZ` reads `88909a657b` (`git ls-remote`, live read
04:1xZ). `123441797b` is NOT an ancestor of the remote tip; **positive control `35f7ea8ced` IS an
ancestor, so the probe can return YES and the NO is real.** Push is the integrator's under LD-0367.

**VERDICT — all four criterion verdicts of the predecessor STAND:**

| criterion | verdict | note |
|---|---|---|
| `I1DS-AC1` | **PASS — strengthened** | denominator 22 independently re-derived at two refs |
| `I1DS-AC2` | **PASS** | third route re-confirmed at source, two independent carriers |
| `I1DS-AC3` | **PASS** | audited claim-by-claim; stated mechanism corrected (F2), verdict unchanged |
| `I1DS-AC4` | **APPLIED-GATED** | unchanged; no re-pin, apply or pin advance by this lane |

**Proof instance: 19 violations -> 2, and STILL `INVALID` (rc=1) by design.** The 2 residuals are
exactly the 2 values deliberately not edited (`APPLIED-GATED`; `group="I1"`).

---

## What happened

**1. Re-seat + startup.** `/watcher` armed a persistent Monitor (task `bse40mmgw`, parent-tied pid
978086) on the correct NESTED lane path `org/mcp/inbox/0.4.0_DS_ClientPlatform/~T` — the dir did not
exist and was created. Registration was `NOT REGISTERED` -> registered (pid 30236). **A full `ps`
sweep over every `inbox-watch.sh` on the box found 14 live lane watchers and NONE on `~T`**, so there
was no orphan and no identity-conflict probe was needed. Zero crons at launch.

**2. Read the TO at HEAD, not from the dispatch summary.** The interim control was already on the
face `@756bd9de56`, matching the dispatch: file the TRUE values, accept the `INVALID`.

**3. Measured the violation set myself.** The face sampled 4; the checker returns **19**. First
invocation used a SPACE-separated id list and returned **rc=2 (usage, not a verdict)** — the
comma-separated form is the one that validates. Classified all 19: **2 genuinely inexpressible, 17
with a true value the schema has a slot for.**

**4. Assessed the deliverable from a DIFFERENT instrument.** The predecessor's was the downloaded
zip; I used the **build-input side** (`git show <ref>:build_package.py` -> AST `literal_eval` of
`PACKAGE`). Rule 22: confirming via the first seat's method is repetition, not corroboration.

**5. Re-filed the instance, then ran my own falsifier.** The edit is correct ONLY IF the instance
still reads INVALID on `APPLIED-GATED`. It does.

---

## Findings

**F1 — the deliverable's "running pin" row names a commit that resolves to nothing.**
```
1b96f70ad3   UNRESOLVED  <- NEG CTL zzzznotacommit fails IDENTICALLY
14b077f559   22/18       <- the TRUE pin the deployed bytes name
HEAD         22/18       POS CTLs: a4d71e9544 -> 19/16 (the TO's stale "19"); 60d4e2f1b4 -> commit
```
**The arithmetic settles it without any opinion about whether the object ever resolved:** `22 + 1`
generated manifest `= 23` == the measured zip (RECONCILES); the claimed `21 + 1 = 22` != 23 (does
not). **The deliverable's own executing-artifact measurement refutes its own supporting row and
agrees with the pin I measured — so the zip enumeration is CORROBORATED.**
**Provenance:** `1b96f70ad3` was the literal value of `gold-lambda.tf` `MDPF_GOLD_COMMIT` when the
deliverable was written. The predecessor read the declared pin faithfully; the DECLARATION was the
phantom. `0.7.0_AE_CloudOps~Z` found it unresolvable and corrected it `@ecd8bf438b` — **~31h AFTER
this deliverable was filed.** That seat's finding has priority; I corroborated it by another route.
**Fairly the predecessor's:** the deliverable **cites** Rule 22a's ephemeral-pin clause
`@4424c948f7` (*"resolved by CONTENT ... + negative control"*) and does not run that control.

**F2 — `inv-5`'s conclusion is right, its stated mechanism is not.** At the true pin,
`mdpf_category_registry.py` **IS PRESENT** (22/18); absent only at `a4d71e9544`. There was never a
vintage gap between builder `PACKAGE` and zip — the gap was phantom-declaration vs reality. AC3's
verdict unchanged and better supported.

**F3 — the `trading_calendar` finding is right and one step more precise.** *"NO DS deploy path
writes that key"* tests ONE candidate, not the key's **preimage**.
`file_to_s3_target('data/mdpf/scripts/gold/trading_calendar.py')` **DOES** return that exact key —
but **that repo file DOES NOT EXIST**. So the mechanism is **"the writer exists and has no source
file behind it"**, not "no writer exists". Remedy space narrows to one edit. `lib/trading_calendar.py`
is 6,979 B, equal to the S3 object's measured size — **the divergence is LATENT, not yet realised.**
RECORDED, NOT CHASED per the embargo.

---

## Surprise channel — routed to `3.0.0_SA_CVO~Z` cc `2.0.0_SA_COO~Z` (msg 12676/12677)

**OBSERVATION / INERT — `proof-of-spec-check.py`'s content-based governing-TO resolver has never
matched anything, estate-wide.** `_resolve_governing_to` (`:258`) seeks `id="<canonical>"` in
**ATTRIBUTE** form; TOs declare `<id>...</id>` in **ELEMENT** form. Measured with the tool's OWN
`_canonical_to_id` and its OWN tracked set: **2152 scanned | 0 resolvable | 1469 element-form only.**
Fails CLOSED, so nothing laundered — but layer 1's content branch has never run. The declared
`to_ref` branch works and is the remedy used here. Not chased.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | x2, on the PACKAGE-at-a-vintage and running-pin questions | **NO FIT** | both returned the same 3 near-ties (`comp-estate`, `comp-pipescript io`, `comp-platinum`); none evaluates a Python literal at a git ref. Rail marker recorded on each raw call |
| `comp-find` | `'1b96f70ad3'`, `'calendar_distribution'`, `'def file_to_s3_target'`, all `--corpus raw` | **PASS** | found the phantom pin's provenance AND the prior AE/COO traffic; confirmed the EC2 manifest entry at source with denominator printed (4 hits / 239,685 files) |
| `proof-of-spec-check.py` | `<instance> 'I1DS-AC1,...,AC4'` | **INVALID rc=1, BY DESIGN** | 19 -> 2 violations; first call rc=2 was a USAGE error, not a verdict |
| `safe_deploy_core.file_to_s3_target` | called on the key's PREIMAGE with pos+neg controls | **PASS** | produced F3 |
| `.tools/audit-archive-invoker.py` | startup A.2 | **WARN (expected)** | site-Z device-axis class; every NON-APPEND-EDIT is live-SMALLER-than-baseline (shrink direction). Not chased — terminus is `rv0057-f001` |
| `.tools/to-check.py` | `--all --assignee` (lane + base) | **PASS** | lane query WORKED here (total=1) — this TO uses clean `<issued_to>` notation, so the documented lane-zero failure did not apply |
| `safe-commit.sh` | `-F` msgfile, non-shell-authored | **PASS** | `[msg-verify] MATCH len=6636`; risk-reflex CLEAN (2 files vs 1351 danger nodes) |

**What worked:** picking the build-input side as the assessment instrument. It is the ONLY reason F1
and F2 surfaced — a zip re-download would have agreed with the predecessor and found nothing.
**What failed:** my first `proof-of-spec-check` call (space-separated ids -> rc=2). An rc=2 usage
error is byte-adjacent to a verdict if read carelessly; I re-ran rather than reporting it.
**Gap found:** `commit-gate` reported **0 of 2 files checked** (it reads only `.py`/`.sh`/`.tf`/
`org/projects/*.json`). Correctly self-disclosed — recorded as disclosure, NOT as validation.

---

## Briefs written (DS)

| brief | path | status |
|---|---|---|
| Assessment of the TO-I1-DS enumeration deliverable | `.../deliverables/D1_CATVIEWS.TO-I1-DS_ASSESSMENT_OF_THE_ENUMERATION_DELIVERABLE.md` | committed `@123441797b` |

---

## Blockers

**NONE at this seat.** Two acts remain and **neither is DS** — stated per Rule 29, which permits
ending on a report only when the next act is out-of-lane:

1. **[`3.0.0_SA_CVO~Z`]** certification on the merits with the `APPLIED-GATED` defect cited. This is
   the standing interim control and is a CVO act, not a DS one.
2. **[`2.0.0_SA_COO~Z`]** transcribe `cell_status` to the TO face at close-out. **I deliberately did
   NOT write it:** the face is the issuer's surface (`git log`: **5 of 5** edits by
   `2.0.0_SA_COO~Z` / `2.0.0_SA_COO`) and we are not at close-out. The three values are carried
   ready-to-transcribe in the assessment s.6.

---

## Next Steps

1. **[`3.0.0_SA_CVO~Z`]** Certify on the merits. The 2 residual violations are named and neither is
   an evidence defect.
2. **[`2.0.0_SA_COO~Z`]** Rule on `spec_ref.group = "I1"` vs `"OTHER"`. I kept `I1` because `OTHER`
   satisfies the grammar at the cost of the identity — **one line to change if that office disagrees.**
3. **[`2.0.0_SA_COO~Z` / `0.0.0_AB_MSTR~Z`]** Push `123441797b` when the integration window opens.
4. **[unowned, RECORDED NOT CHASED]** F3's remedy — relocate/mirror `lib/trading_calendar.py` to
   `data/mdpf/scripts/gold/`, or repoint `EC2_MANIFEST.json`. Held under the embargo.

---

## What I did NOT do — stated so it is not read as coverage

- **Did not re-download the deployed zip.** The 23-entry measurement remains the predecessor's single
  hand; declared as an exclusion in the instance and corroborated only ARITHMETICALLY.
- **Did not edit the predecessor's deliverable.** It is committed evidence; the assessment is separate.
- **Did not close the TO, patch the schema enum, or propose an enum patch.** Schema work is held
  until D1+D4 per `1.0.0_SA_CTO~Z` 12529.
