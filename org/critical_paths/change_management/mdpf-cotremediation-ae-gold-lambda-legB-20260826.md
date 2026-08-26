# DEPLOY-COMPLETION LEDGER -- mdpf-gold-lambda LEG B (opal_fixed_income on the global union)

**Opened:** 2026-08-26T20:12Z by `0.6.2_AE_PartnerETL~A` (**deploy-start**; NEVER#6)
**Status:** **CLOSED 2026-08-26T20:23Z** -- applied 20:21:10Z, verified on the RUNNING bytes, no leg stranded
**Authority:** `2.0.0_SA_COO` 73390 s.1 (step (b) GO) · `1.0.0_SA_CTO` 73365 s.3 (architecture
constraint: minimal pin at FILE grain, interlock `@af92b0afa3` lift by name, nothing else rides).
**Project:** MDPF_COTREMEDIATION / D8. Leg A (`@1e73554830`) and Leg A-Prime
(`mdpf-cotremediation-ae-gold-lambda-legAprime-20260826.md`) are both CLOSED and separate.

> **WHY THIS LEG EXISTS, IN ONE LINE:** tonight's exercise was green over the CODE PATH but the
> LAMBDA still runs pre-fix bytes -- the 9-key `GLOBAL_MODEL_KEYS` tuple and the pre-fix crosswalk.
> Without this deploy the 2026-08-27 13:30Z fire re-fails at 18:24Z's exact site **on a now-correct
> slice**. `2.0.0_SA_COO` 73390 s.2: the bundle is "the only plane still on pre-fix bytes."

---

## WHAT IS BEING DEPLOYED

`0.4.0_DS_ClientPlatform~T`'s registration of `opal_fixed_income` on the global union, landed at
`2d5f8a7f74`:
- `mdpf_revamp_model_crosswalk.py` -- adds `ModelEntry("opal_fixed_income", None, "Fixed Income",
  "model", False)`; tightens the `BLEND_MODEL_KEYS` predicate to `model_id is None AND eclipse_id
  is not None` (the predicate said one thing and meant another; Fixed Income is the first entry
  that separates the two).
- `dim_mdpf_aggregate_aua_timeseries.py` -- `GLOBAL_MODEL_KEYS` 9 -> 10, adding `opal_fixed_income`.
  **This is the fixed tuple that silently dropped the key and produced the 18:24Z FATAL.**

**BUILD PIN `1b96f70ad3`** = running vintage `5043bbe8d4` + those TWO files ONLY. Isolated worktree
(`legB-globalkeys`). **Not for merge. NOT HEAD.**
Zip **726,666 B**, sha256 `e7b57a0ff64d8801922817b6524277dda7af8c70c22e3d07351a6137fffe88a8`,
22 modules, import-closure PASS. In-zip `source_vintage` =
`{"commit": "1b96f70ad358b9d3278517f43fcfb629ed16b51f", "pin": "1b96f70ad3"}`.

### THE THIRD CHANGED MEMBER I DELIBERATELY DID NOT TAKE

`build_cottonwood_mdpf_slice.py` **IS** a bundle member (`build_package.py:150`, read at my own hand,
not taken on report) and **does** differ from the running vintage. **Excluded.** All 14 of its
changed lines sit inside a docstring -- the retraction of the false "global's `by_model` key set is
EXACTLY the union of the per-firm key sets" claim. Zero computed values move. Excluding it also keeps
a **CRLF** file (1044 CRLF / 0 bare LF) out of the deployed bytes, which is the class that makes a
byte-diff read CHANGED with no semantic change.
⚠ **CONSEQUENCE, STATED SO IT IS NOT LATER DISCOVERED AS DRIFT:** the deployed slice keeps the
running vintage's docstring, so a future source-vs-deployed read of that ONE file shows a benign prose
delta. **Known and chosen, not drift.** `0.4.0_DS_ClientPlatform~T` asked me to say which I took; this
is the answer.

> **INTERLOCK RE-CHECKED AT THIS PIN.** D1_CATVIEWS remains NO-SHIP; `mdpf_category_registry` stays
> at its pre-defect bundle vintage and **UNREFERENCED** (verified: the running vintage's consolidator
> has zero `mcr` references); `mdpf_aggregate_aua.py`'s defective `:699`/`:703` sites do NOT ride --
> that file is the **one-token-apart sibling** of `dim_mdpf_aggregate_aua_timeseries.py` and is not a
> member of this pin. Changed member set is **TWO FILES**.

---

## PRE-STATE CONTROL (measured live this session, not carried over from Leg A-Prime's POST)

```
mdpf-gold-lambda  LastModified 2026-08-26T18:21:12Z  CodeSize 723,461
CodeSha256        LdShsMmFvrPHq7aW8zCI1zIN7o4YdgkRHHlpFfPO/xs=
MDPF_GOLD_COMMIT  5043bbe8d47e0a0948d6896c3092c576fa28494a
running GLOBAL_MODEL_KEYS = 9 keys, opal_fixed_income ABSENT
```
> **These are numerically identical to Leg A-Prime's POST table, and I measured them anyway.** A
> prior deploy's POST is only this deploy's PRE *if nothing applied in between* -- which is a claim
> about the world, not an inference from a record. It held; that is a measurement, not an assumption.

## PRE-APPLY ARMS (run against the BUILT ZIP and the RE-DOWNLOADED RUNNING BUNDLE)

Running bundle provenance: downloaded 723,461 B == deployed `CodeSize` 723,461, asserted in the
harness rather than eyeballed.

| # | Arm | Result |
|---|---|---|
| 1 | MEMBERS diff vs running bundle | ADDED **none** · REMOVED **none** · CHANGED **[BUILD_MANIFEST.json, dim_mdpf_aggregate_aua_timeseries.py, mdpf_revamp_model_crosswalk.py]** -- exactly the pin + manifest |
| 2 | NO `mdpf_category_registry` import, AST over ALL scopes, all 18 packaged modules | **0 import nodes** |
| A | Crosswalk self-test shape UNCHANGED | **11 models: 7 served, 5 core, 2 sma, 2 blend** -- `opal_fixed_income` in **none** of served/core/sma/blend |
| B | `GLOBAL_MODEL_KEYS` on the BUILT bytes | **10 keys, `opal_fixed_income` present** |
| B-neg | Same arm on the RUNNING bundle's bytes | **9 keys, `opal_fixed_income` ABSENT** -- the arm DISCRIMINATES |
| 5 | **NEGATIVE CONTROL** -- ARM 2's matcher re-subjected where the import IS present | **FIRES**: synthetic 1 hit; real superseded build `e9d7c37976:build_cottonwood_mdpf_pair.py:66` 1 hit |
| D | Leg A-Prime work still rides (not regressed by this pin) | pair `mcr` imports **0** · cited literal `Client - Opal Supervised` **present** · `OPAL_SMA_LEAF_KEYS` **present** · slice `Opal Fixed Income` **2 occurrences** |

> **ARM B-neg IS THE ONE THAT MAKES THIS DEPLOY MEAN ANYTHING.** ARM B alone ("the new bundle has 10
> keys") is consistent with a world where the running bundle already had them. Running the identical
> extractor against the RUNNING bytes and getting **9 without the key** is what makes the 10 a
> measured change rather than a measured state.
> ⛔ **AND ARM 5 FAILED FIRST, FOR THE RIGHT REASON, AND I AM RECORDING IT RATHER THAN ONLY ITS
> REPAIR.** I aimed it at `mdpf_gold_consolidator.py` at the superseded build; it returned **0 hits**
> and the harness correctly refused to call that a pass. The import lives in
> `build_cottonwood_mdpf_pair.py:66` -- **the arm's SUBJECT was wrong, not the arm.** A positive
> control has its own subject and it can be the wrong one; this one failed LOUD, which is the safe
> direction, but the same misaim on a green-reading control is invisible.

---

## LEGS

| # | Act | Status |
|---|---|---|
| 1 | Mint pin `1b96f70ad3` (isolated worktree `legB-globalkeys`) | **DONE** |
| 2 | Build package | **DONE** -- 726,666 B, `e7b57a0f...`, 22 modules |
| 3 | Pre-apply arms | **DONE** -- all PASS; both negative controls fire |
| 4 | Upload artifact to the Terraform source key | **DONE** -- VersionId `xU7PYhHh2jOTj.r5TK6Me2vvexo.51Fl`, 726,666 B, metadata sha matches |
| 5 | `safe-apply -target=aws_lambda_function.mdpf_gold` | **DONE** 20:21Z -- plan 0 add / 1 change / 0 destroy; apply reported the same |
| 6 | Post-apply proof on RE-DOWNLOADED running bytes | **DONE** -- see PROOF below |
| 7 | Tear down worktree (RETAIN branch -- the pin must stay reachable) | **DONE** -- branch `legB-globalkeys` RETAINED, pin `1b96f70ad3` verified still reachable |

**Target:** `aws_lambda_function.mdpf_gold` ·
`s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip` ·
`MDPF_GOLD_COMMIT` at `infra/aws/terraform/mdpf-pipeline/gold-lambda.tf:109`
`5043bbe8d4...` -> `1b96f70ad358b9d3278517f43fcfb629ed16b51f`.

## ROLLBACK (same-window, captured BEFORE any write)

Versioned bucket (`Status: Enabled`, measured). Prior version = the Leg A-Prime artifact,
**VersionId `hAFXzyqIdtpFHJDPahO6QOuRWf.fnfJF`**, 723,461 B,
`content-sha256 2dd4a1b0c985beb3c7abb696f33088d7320dee8e187609111c796915f3ceff1b`, LastModified
2026-08-26T18:13:43Z. Restore it, revert `MDPF_GOLD_COMMIT` to
`5043bbe8d47e0a0948d6896c3092c576fa28494a`, `safe-apply`.

## CLOSE-OUT

**CLOSED 2026-08-26T20:23Z by `0.6.2_AE_PartnerETL~A`. All 7 legs done. Nothing half-landed.**
HALT-GATE fired at the apply with 2 pending messages (both 5d old, MSTR + CTO on the COT_SUPERVISED
merge-deploy leg). **Read, not waved:** CTO's own line closes them -- *"COT_SUPERVISED acceptance is
UNAFFECTED, sha256 identical to 0.6.2's pin on both files."* Different subject, already adjudicated;
re-run with `HALT_ACK=1`.

### PROOF ON THE RUNNING PLANE (re-downloaded bundle; every limb moved, and the control was real)

| | PRE (control) | POST |
|---|---|---|
| `LastModified` | 2026-08-26T18:21:12Z | **2026-08-26T20:21:10Z** |
| `CodeSha256` | `LdShsMmFvrPHq7aW8zCI1zIN7o4YdgkRHHlpFfPO/xs=` | **`57V6D/ZNiAGSKBe2UkJ33aevjHDCLj0HNRphN//+iKg=`** |
| `CodeSize` | 723,461 | **726,666** (= the built zip exactly) |
| `MDPF_GOLD_COMMIT` | `5043bbe8d4...` | **`1b96f70ad358b9d3278517f43fcfb629ed16b51f`** |
| `GLOBAL_MODEL_KEYS` | **9 keys, `opal_fixed_income` ABSENT** | **10 keys, `opal_fixed_income` PRESENT** |
| crosswalk shape | 10 models | **11 models: 7 served, 5 core, 2 sma, 2 blend** -- derived sets UNMOVED |
| `opal_fixed_income` in served/core/sma/blend | n/a | **none of the four** |
| `mdpf_category_registry` import nodes | n/a | **0** |
| Leg A-Prime work (cited literal, `OPAL_SMA_LEAF_KEYS`) | present | **still present -- not regressed** |

**BYTE IDENTITY:** the re-downloaded running artifact's sha256 is
`e7b57a0ff64d8801922817b6524277dda7af8c70c22e3d07351a6137fffe88a8` -- **identical to the zip I
built**, and its base64 raw digest reproduces `CodeSha256` exactly. in-zip `source_vintage.commit`
= `1b96f70ad358...` = `MDPF_GOLD_COMMIT`. **Declaration and bytes agree.**
**BOTH of `3.0.0_SA_CVO`'s required vintage instruments moved** (72801: COULD-NOT-VERIFY unless
BOTH `LastModified` AND `CodeSha256` move off the stated baseline). They did.

> **THE 9 -> 10 ROW IS THE ONE THAT MATTERS, AND IT IS A MEASURED CHANGE RATHER THAN A MEASURED
> STATE** -- the identical extractor run against the PRE bytes returned 9 without the key. A "10 keys
> present" reading alone would have been consistent with a world where the fix was already deployed
> and tonight's work did nothing.

### WHAT I GOT WRONG IN THIS DEPLOY, AND IT WAS MINE

**ARM 5, the negative control, was aimed at the wrong FILE and reported `0 hits`** -- I pointed it at
`mdpf_gold_consolidator.py` at the superseded build `e9d7c37976`; the `mcr` import actually lives at
`build_cottonwood_mdpf_pair.py:66`, which is what my own Leg A-Prime ledger already said ("fires at
line 66"). The harness refused to score it a pass, so it failed **LOUD** and I re-aimed it.
⛔ **A positive control has its own SUBJECT and the subject can be wrong.** This one failed in the
safe direction -- **the same misaim on a control that reads GREEN is invisible, and looks like
rigour.** Recorded rather than quietly repaired, and the corrected label is in the arms table above.

## WHAT THIS ENTRY DOES **NOT** CLOSE

- **(c) THE LAMBDA-PATH RE-RUN and (d) THE RE-GRADE.** `0.4.0_DS_ClientPlatform~T` grades -- the
  grader stays the seat that pre-registered against the bar. Count **`FATAL:` lines, never the
  5-of-7 summary**; gate (ii) at the **2026-08-25 VALUE-DATE cell**, `opal_fixed_income` =
  **8,442,396.91**, identity delta **0.01**.
- **PRODUCTION ACCEPTANCE** -- the 2026-08-27 13:30Z SCHEDULED fire on `3.0.0_SA_CVO`'s absolute bar.
  **The ad-hoc TESTS; the scheduled fire remains the acceptance.**
- **THE SERVE** -- Andrew's word alone. **A green is not a release.**
- **opal-assets-daily-emitter.** Its vendored crosswalk copy is now COMMITTED (`aaf2be288f`, my lane)
  but **that lambda is NOT redeployed by this entry and still runs pre-fix crosswalk bytes.** A
  vendored copy committed and a vendored copy deployed are two states; only the first is true.
  Surfaced to `1.0.0_SA_CTO` / `2.0.0_SA_COO` rather than answered by assumption.
