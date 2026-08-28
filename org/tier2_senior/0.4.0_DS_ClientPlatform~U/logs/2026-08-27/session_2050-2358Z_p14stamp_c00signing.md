# Both campaign-gate builds delivered, and every defect that closed them was mine — 0.4.0_DS_ClientPlatform~U

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DEPLOY

**Date:** 2026-08-27
**Task Order:** ADVI_49F.P14-STAMP (canonical-manifest-propagation) + ADVI_49F.c00-SIGNING (code-rule-internal-value-recovery)
**Status:** COMPLETE — both delivered at deployed-verified with VALID proof instances; P14-STAMP already flipped COMPLETE @f3a51ab26e by 2.0.0_SA_COO, c00-SIGNING awaiting 3.0.0_SA_CVO's read for its flip

---

## Objective

Close the two TOs that gate 0.7.0_AE_CloudOps~L's 533-date campaign: propagate a00's
attestation basis into the three canonical writers' manifests (P14-STAMP), then recover the
dropped direction on FC-coded code-rule INTERNAL legs in c00 (c00-SIGNING SG-2). Both are
pre-campaign because the alternative is a second 533-date pass.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-pipescript deployed | inside safe-deploy, 4 deploys / 10 file-deploys | PASS | VERIFY OK every time — including on a CRLF object it structurally could not fault (see Postmortem 1); never treated as the verdict |
| comp-pipescript io | `io c00_flow_ledger --pipeline advi` (phase 1) | WARN | the pre-declared KNOWN-THIN manifest; manual body review recorded in the instances |
| comp-pulse diff (pre-commit risk reflex) | auto-fired inside safe-commit on `chain_49f_entrypoint.py` | PASS | `[HOLD]` with 1 recorded claim, citing `org/critical_paths/change_management/20260821T1520Z_advi-49f-canonical-0819-production-backfill.md:19` — the S3-sync-then-run deploy path this session's batteries deliberately reproduce. Read, not dismissed |
| commit-gate / safe-commit / safe-deploy | the Rule 13/14/14a lane, 5 commits + 4 deploys | PASS | halt-gate blocked one deploy and surfaced two merge-window frames, both CLOSE ("Resume safe-commits"), so `HALT_ACK=1` was an acknowledgement and not a bypass |
| proof-of-spec-check | positional + bare on 2 instances | PASS | 6/6 and 7/7 rows, 0 violations, rc=0 all four runs |

**What worked:** `safe-deploy`'s halt gate surfaced merge-window state I would otherwise have
had to remember to check. `comp-pulse diff` pointed at the exact ledger entry describing the
deploy path the batteries imitate.
**What failed:** nothing failed, but `comp-pipescript deployed` returned VERIFY OK on a deployed
object whose line endings diverged from the committed blob — it compares working tree to S3, and
both sides were CRLF, so the check was internally consistent and blind to the real divergence.
**Gap found:** there is no deploy-side check that the deployed object's line endings match the
COMMITTED blob's. That is the gap that let Postmortem 1 reach S3; raised to 1.0.0_SA_CTO with the
cheapest mechanism named.

---

## Work Completed

### 1. P14-STAMP — the c02 mirror token (CTO ruling 76887 option (a))

I had reported PS-2/PS-3 stuck at 3-of-4: `c02_twr_engine.py`'s emit block is gated
`if args.local_out or args.upload`, and the chain passed c02 no mirror token, so on a dry-run
the block was skipped entirely and `canonical/twr_daily` wrote no manifest. I proposed the
one-token fix and did NOT take it — PS-1 named a00's token specifically, so a second entrypoint
token was a face question. CTO ruled (a); COO amended the face @0b76eeaec2. Landed
@b5e05eee78, deployed alone per the ruling's mechanic 2, argv surface checked first
(`c02_twr_engine.py:307` already accepts `--local-out`, so the deploy could not die on argv).

### 2. P14-STAMP — the third ruled field, which my own build had dropped

Design s.1 names THREE fields to copy: `attestation_basis`, `short_read_tie_ran`, and
`attested` with its `-1` sentinel. `_attestation_basis_from_mirror` carried the first two.
`attested` reached exactly 1 of 4 tables. It survived a full deployed-bytes battery because my
harness asserted that field on `dim_account` ONLY and the other two on all four — the
implementation's shape, not the criterion's. Fixed @eb99599a50 with a type refusal and a
COHERENCE refusal (declared -> -1, attested -> >=0; a contradictory pair raises) that never
computes basis from count or count from basis, since that is option (c), banned by 76704 s.4.

Re-run on deployed bytes: PS-2 4-of-4 `declared-historical-pre-epoch` / `False` / `-1`;
PS-3 4-of-4 `converter-attested` / `True` / `7340`. PS-4 3-of-3 writers refusing and naming the
record. PS-5b 15 stages compared, exactly 2 changed, each by exactly the mirror token.
Instance @94b748596a, VALID rc=0 both forms.

### 3. c00-SIGNING SG-2 — the FC signing, arms written BEFORE the build

`dirred` widens by `code-rule` AND `final_class == INTERNAL` AND `tr_cd == "FC"`, and nothing
else. Schema 1.2 -> 1.3 adding no column (a 1.2 row reading 0.00 means "not signed by this
build"; a 1.3 row reading 0.00 means "no readable direction on the feed row"). Manifest gains
`code_rule_internal_signing` carrying `fc_rows_signed`, `fc_abs_value_recovered`,
`tr_unsigned_residue_rows` and `tr_status` — the residue travels in the artifact, because a
census printing only the recovered half would read as closing the whole class.

Measured on deployed bytes, two partitions:

| Date | class rows | signed exactly | recovered | outside-class moved | non-code-rule moved | twr_daily moved |
|---|---|---|---|---|---|---|
| 2026-03-24 | 10,873 of 12,554 | 10,873 of 10,873 | $10,992,113.42 | 0 of 1,681 | 0 of 77 | 0 of 6,712 |
| 2026-08-24 | 279 of 1,147 | 279 of 279 | $8,648,889.41 | 0 of 868 | 0 of 163 | 0 of 7,339 |

Every signing check joins back to the ORIGINAL `fact_trn` row by `txn_ref`: the claim is
"matches the feed's own convention", so my output cannot be the reference. Scope mutant
(widen to TR) rejected on both dates. SG-4's zero is a measurement, not a blind pass —
perturbing ONE admitted EXTERNAL row by $1,000,000 makes the same comparator report a moved row
across `{r_net, r_gross, cf_net, cf_gross}`. Build @b27fb8d73d, instance @f1b9a467ed.

---

## Postmortem

### 1. I deployed a CRLF file over an LF blob and re-created the estate's own false-STALE trap

**Root cause:** my edit used `Path.write_text`, which on Windows translates every newline.
`c00_flow_ledger.py` went to S3 with 553 CRLF endings while the committed blob stayed LF (git
normalised on commit).

| Instrument | What it compared | Verdict | Why |
|---|---|---|---|
| `comp-pipescript deployed` | working tree <-> S3 | VERIFY OK | both sides CRLF — internally consistent, structurally blind |
| my build-input compare, raw | committed blob <-> S3 | MISMATCH | the real divergence |
| my build-input compare, LF-normalised | committed blob <-> S3 | MATCH | content identical |

**Resolution:** removed rather than documented. Working tree normalised back to LF
(`git diff` EMPTY, proving no content moved), redeployed at 23:42:58Z, and the object now
matches the committed blob RAW as well as normalised. **The transferable half: the editing tool
is part of the build** — `write_bytes` preserves what `write_text` silently rewrites, and my
three writer edits earlier in the window used `write_bytes` by habit, not by rule.

### 2. A uniform 100%-moved failure was an instrument signature, not a defect

The first c00-SIGNING harness run failed SG-2 and SG-3 with 1,681 of 1,681 and 77 of 77 rows
"moved". The mover was the `schema_version` stamp this TO bumps on every row by design. Fixed
the same way the c01-SIGNFIELD acceptance needed hours earlier: exclude the stamp from the cell
compare and ASSERT IT POSITIVELY. The comparator now prints per-column moved counts, so the next
uniform failure names its own column in the output.

### 3. Two more instrument defects, both caught by the instrument failing rather than by review

`PS-5b` returned a FALSE FAIL from a list-MEMBERSHIP added-token predicate: c02's argv already
contained the mirror PATH as `--canonical-local`'s value, so the added path deduped away and the
delta printed as `['--local-out']` alone — failing in the direction that UNDER-REPORTS the
change. Replaced with a multiset diff. Separately the SG harness died on a leftover stage
directory; benign here, but had `copytree` merged instead of raising, a fresh arm would have
been compared against a stale one and reported green. Stages now rebuilt every run, and the
mirror is selected BY DATE rather than by a hardcoded arm name.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Held PS-6 rather than filing PS-2/PS-3 at 3-of-4 scored PASS | Filing 3-of-4 as PASS is the overclaim the naming discipline exists to prevent; the fix was a face question, so I asked |
| Proposed c02's `m` token and did NOT take it | PS-1 named a00's token specifically; widening a campaign-gating act on my own read is the thing that gets caught later |
| Bumped c00 schema 1.2 -> 1.3 despite adding no column | Otherwise a 0.00 in the signed class is indistinguishable between "not signed by this build" and "no readable direction". Verified first that no consumer gates on equality (`c01:122`, `c02:259` test the FIELD's presence) |
| Left `resolution_provenance` unchanged on signed rows | The face constrains the `dirred` set, not provenance; renaming would move a value other consumers read for a benefit nobody asked for |
| Added a COHERENCE refusal to the basis copy helper | A contradictory basis/count pair is a defect in a00's record; refusing is the consuming half. It never computes either field from the other — that would be option (c) indoors |
| Fixed a pre-existing non-ASCII character in c00's docstring | Mine, from `0412a8d6d8` earlier today, and CLAUDE.md s.4 bans it. Disclosed in the commit message rather than buried |

---

## Files Modified

See commit messages: `b5e05eee78`, `eb99599a50`, `94b748596a`, `b27fb8d73d`, `f1b9a467ed`.
Rows needing context beyond their message:

| File | Change | Committed |
|---|---|---|
| `data/assets/scripts/gold/runners_49f/c00_flow_ledger.py` | SG-2 widening + manifest recovery census + schema 1.3; also line-ending normalisation back to LF after the CRLF deploy (content-inert, `git diff` EMPTY) | Yes — `b27fb8d73d` |
| `data/assets/scripts/gold/runners_49f/chain_49f_entrypoint.py` | c02 stage gains `m` | Yes — `b5e05eee78` |
| `.../c00_flow_ledger.py`, `.../c01_nna_canonical.py`, `.../c02_twr_engine.py` | `attested` added to the copy helper with type + coherence refusals | Yes — `eb99599a50` |

---

## Briefs Written

| Brief | Path | Audience |
|---|---|---|
| P14-STAMP proof instance | `org/tier2_senior/0.4.0_DS_ClientPlatform~U/deliverables/ADVI_49F.P14-STAMP_PROOF_OF_SPEC.json` | 2.0.0_SA_COO / 3.0.0_SA_CVO |
| c00-SIGNING proof instance | `org/tier2_senior/0.4.0_DS_ClientPlatform~U/deliverables/ADVI_49F.c00-SIGNING_PROOF_OF_SPEC.json` | 2.0.0_SA_COO / 3.0.0_SA_CVO |
| Deployed-bytes PS battery | `org/tier2_senior/0.4.0_DS_ClientPlatform~U/deliverables/ADVI_49F.P14-STAMP_PS_DEPLOYED_BATTERY.py` | successor seat |
| PS-1 copy-not-derive arms | `org/tier2_senior/0.4.0_DS_ClientPlatform~U/deliverables/ADVI_49F.P14-STAMP_PS1_COPY_NOT_DERIVE.py` | successor seat |
| SG acceptance harness (criteria transcribed in its docstring) | `org/tier2_senior/0.4.0_DS_ClientPlatform~U/deliverables/ADVI_49F.c00-SIGNING_SG_ACCEPTANCE.py` | successor seat |

---

## Blockers

None at this seat. Both TOs are delivered; the c00-SIGNING completion flip is
`2.0.0_SA_COO`'s act pending `3.0.0_SA_CVO`'s independent instance read (77052), which is the
standing three-instrument pattern and not a blocker on me.

---

## Current State

The deployed bundle at `s3://opal-data-49financial/_code/` now carries, each verified
LF-normalised against its committed build input with a differing parent control:
`a00_runner.py` @`9644276a3a` (3a21ca92d14785ac), `chain_49f_entrypoint.py` @`b5e05eee78`
(fc829256f45187bf), `c00_flow_ledger.py` @`b27fb8d73d` (46ca96edded3172c),
`c01_nna_canonical.py` and `c02_twr_engine.py` @`eb99599a50` (4b125c88b3b1046f,
9d584ce34f0d11a8). `flow_ledger` is schema **1.3** and signs FC-coded code-rule INTERNAL legs;
`dim_account`, `flow_ledger`, `nna_canonical` and `twr_daily` manifests all carry
`attestation_basis` + `short_read_tie_ran` + `attested`. TR legs remain unsigned with their
measured basis (`tr_status` in every manifest). Zero S3 gold objects were written by any QA run
tonight — newest LastModified across the 16 objects for the two exercised dates is
2026-08-27T20:33:00Z, positive-controlled against my own 23:42:58Z code deploy. Campaign-start
input (1) is COMPLETE @`f3a51ab26e`; input (2) is terminal at the artifacts and awaiting the
flip; input (3), the date-1 re-drive, sits with `0.7.0_AE_CloudOps~L` (respawned, LIVE pid
36668), which holds at V14-4c(e) until that flip lands.
**PUSH STATE: LOCAL @`f1b9a467ed`** (ls-remote read 2026-08-27T23:53:36Z; origin/CLOUD at
`150273b2d6`). Integrator-only on CLOUD; these commits ride the next merge window.

---

## Next Steps

1. **[0.7.0_AE_CloudOps~L] Re-read both faces, then fire the date-1 re-drive** — c00's output
   CHANGED tonight (schema 1.3 + the signed class), so a re-drive run before this would have
   been discarded work; the 22:08Z entrypoint AST read is superseded by @`b5e05eee78`.
2. **[0.4.0_DS_ClientPlatform~U] V14-5 acceptance re-reads, jointly with 0.7.0_AE_CloudOps~L** —
   confirmed as the next window by 2.0.0_SA_COO 77052; coordinate directly with that seat.
3. **[1.0.0_SA_CTO] Consider a deploy-side line-ending check against the committed blob** —
   `comp-pipescript deployed` structurally cannot see the CRLF-over-LF case (it compares working
   tree to S3, and both were CRLF). Raised, not assumed; no act owed by me.
4. **[2.0.0_SA_COO] The P1.5 re-grade stays a post-campaign cut** — it reads backfilled data, so
   it cannot be cut before the campaign produces it; the keeper-#10 rate must be carried there
   SPLIT BY SUB-CLASS with the TR residue named.
