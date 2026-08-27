# DEPLOY-COMPLETION LEDGER -- mdpf-gold-lambda minimal-pin rebuild (MDPF_COTREMEDIATION LEG A)

**Opened:** 2026-08-26T15:17:15Z by `0.6.2_AE_PartnerETL~A` (**deploy-start**; NEVER#6)
**Status:** **CLOSED 2026-08-26T15:34:36Z** -- applied, verified on the RUNNING bytes, no leg stranded
**Authority:** `2.0.0_SA_COO` 72361 -- RULED minimal pin, amending 72320 s.2's "build from source".
Leg A (lambda rebuild + apply) ruled AE at 72320 s.2; Leg B (S3 script sync) is a separate DS lane.
**Project:** MDPF_COTREMEDIATION / D8 · **Fix commit:** `@ae106b1124` · **Handover:** `@041969c39a`

---

## WHAT IS BEING DEPLOYED, AND WHY THIS PIN

Repairs the 2026-08-26 13:30Z scheduled gold run, which lost `cottonwood` and `global` to
`ValueError: no canonical by_model key for Cottonwood model 'Opal Fixed Income'`
(`build_cottonwood_mdpf_slice.py:990` via `mdpf_gold_consolidator.py:718`). **Neither guard is
touched** -- both refused correctly.

**BUILD PIN `48c473caa1`** = the DEPLOYED vintage `530ba66971` + `@ae106b1124`'s 3 files ONLY.
Ephemeral, built in an isolated worktree on branch `legA-minimal-pin`. **Not for merge.**

> ⛔ **NOT HEAD, AND THAT IS THE RULING.** Between `530ba66971` and HEAD: **43 commits, 31 files,
> 4,620 insertions** -- including `mdpf_category_registry.py` **+814** (D1_CATVIEWS, **NO-SHIP**),
> `mdpf_gold_consolidator.py` +294, and ~2,000 lines of unrelated 49F perfrp work. **The fix is 58 of
> those 4,620 lines.** At HEAD, `mdpf_category_registry.py:992` is still exact float equality with no
> `RECON_TOLERANCE`, and `mdpf_gold_consolidator.py:84` imports it at module level -- so the
> `ViewPlaneError: REFUSING EMIT` predicate is loaded by the consolidator that runs the fire, and a
> HEAD build could convert a **2-scope outage into a 4-scope one**.

**Why this pin is safe, verified in git before building:**
- consolidator @`530ba66971` = 55,629 B, **0** occurrences of `mdpf_category_registry` --
  **byte-identical to the running consolidator pulled from the live bundle.** The deployed artifact
  IS that pin; not inferred.
- `mdpf_category_registry.py` @`530ba66971` = 12,602 B, **0** occurrences of `ViewPlaneError` --
  **the fatal predicate does not exist at this pin.** It arrived with the +814.
- All 3 files are **UNCHANGED** between `530ba66971` and `ae106b1124^`, so the carry is exact.
- **22 of 22** PACKAGE members resolve at the pin (pre-checked; no build-time refusal).
- Worktree delta vs the deployed pin: **3 files, 58 insertions, 0 deletions.**

---

## LEGS

| # | Act | Mechanism | Evidence | Status |
|---|---|---|---|---|
| 1 | Mint ephemeral build pin | isolated worktree `legA-minimal-pin` @`530ba66971` + 3 files | pin `48c473caa1`; delta 3 files / +58 / -0 | **DONE** 15:17Z |
| 2 | Build the package | `build_package.py --pin 48c473caa1` | 701,490 B, sha256 `dfff3ded...`, 22 modules, import-closure gate PASS | **DONE** 15:2xZ |
| 3 | Pre-apply bundle proof | vs deployed bundle: ADDED `mdpf_category_registry.py` (12,602 B, **no `ViewPlaneError`**, **no packaged module imports it -> INERT**); CHANGED only my 2 modules (+28/-0, +15/-0, non-comment = my 3 lines); REMOVED none | **DONE** |
| 4 | Apply | `safe-apply apply -target=aws_lambda_function.mdpf_gold` (HALT-GATE reviewed + acked: 2 msgs, 5d old, COT_SUPERVISED, unrelated) | plan **0 add / 1 change / 0 destroy**; `Apply complete! Resources: 0 added, 1 changed, 0 destroyed` | **DONE** 15:29Z |
| 5 | **Post-apply proof on the RUNNING plane** | re-downloaded the live bundle | see PROOF below -- **TRUE/TRUE against a FALSE/FALSE control** | **DONE** 15:3xZ |
| 6 | Tear down worktree | removed; **branch `legA-minimal-pin` RETAINED** so pin `48c473caa1` stays reachable (the vintage stamp + in-zip manifest both cite it) | | **DONE** 15:34Z |

**PRE-STATE CONTROL (measured 2026-08-26, and it is a real control because it reads FALSE):**
```
mdpf-gold-lambda  LastModified 2026-08-25T19:38:55Z  CodeSize 684,807
CodeSha256 UVT5XRX3R2O3zsr+g2QTPrD2DDYlQilSP+IfmjD2mIc=
  build_cottonwood_mdpf_slice.py  56,697 B  carries 'opal_fixed_income': FALSE
  mdpf_revamp_model_crosswalk.py  17,874 B  carries 'opal_fixed_income': FALSE
```

---

## WHAT THIS ENTRY DOES **NOT** CLOSE

- **LEG B** -- the S3 script-prefix sync to `opal-data-mdpf/code/scripts/{assets_gold,gold}/`. DS lane,
  separate seat, separate ledger. Both keys read STALE. Not covered here.
- **ACCEPTANCE.** This ledger closes the DEPLOY. Acceptance is the **2026-08-27 13:30Z SCHEDULED**
  fire advancing `as_of_last` **and** `_provenance.written_at` for global **and** cottonwood on the
  served plane, verified by `3.0.0_SA_CVO`. ⛔ **NO AD-HOC INVOKE** -- time-of-day is the only
  discriminator the read has.
- **ANDREW'S SENTENCE.** The measurement establishes STRUCTURE, not INTENT. Deploy puts correct code
  in place; his word governs whether the row PUBLISHES.
- **THE ~$36.2M BOOK MOVE** (OBSERVATION/ARMED, disarm carried in `@041969c39a`): cottonwood's dim
  grew 146,879,940.09 -> 191,504,659.67 on 2026-08-26; **$8,442,396.91 is the new row and IS
  explained; the remaining ~$36.2M is NOT explained by this repair.** Unowned, not chased.

---

## CLOSE-OUT

**CLOSED 2026-08-26T15:34:36Z by `0.6.2_AE_PartnerETL~A`. All 6 legs done. Nothing half-landed.**

### PROOF ON THE RUNNING PLANE (the control is real -- it read FALSE before)

| | PRE (control) | POST |
|---|---|---|
| `CodeSha256` | `UVT5XRX3R2O3zsr+g2QTPrD2DDYlQilSP+IfmjD2mIc=` | `3/897ecG2Xzal+0Xl+Ygoshsqccd6smAcMwygv8KjZQ=` |
| `LastModified` | 2026-08-25T19:38:55Z | **2026-08-26T15:29:34Z** |
| `CodeSize` | 684,807 | **701,490** (= the built zip, exactly) |
| `MDPF_GOLD_COMMIT` | `1daf1913dd...` | **`48c473caa1...`** |
| `build_cottonwood_mdpf_slice.py` carries `opal_fixed_income` | **FALSE** | **TRUE** (58,961 B) |
| `mdpf_revamp_model_crosswalk.py` carries `opal_fixed_income` | **FALSE** | **TRUE** (18,988 B) |

in-zip `source_vintage` = `{"commit": "48c473caa1aebd2c9b40d9f6ef81fe692adc830d", "pin": "48c473caa1"}`
-- **matches `MDPF_GOLD_COMMIT` on the applied plane.** The declaration and the bytes now agree.

⚠ **A DRIFT FIXED IN PASSING, worth recording because the tf comment predicted it.** `MDPF_GOLD_COMMIT`
read `1daf1913dd...` while the DEPLOYED zip's own manifest said `530ba66971...` -- the stamp had
drifted AGAIN, the exact defect `gold-lambda.tf:98-108` warns about ("never carry the prior value
forward"). It is now set from the pin actually built with and confirmed against the built zip.

### ROLLBACK (same-window, if the 08-27 fire regresses)
The artifact bucket is versioned. Prior artifact: VersionId `r819XZni2appiJCYjDj4ack.BzFrBnJq`,
684,807 B, `content-sha256=5154f95d15f74763b7cecafe8364133eb0f60c36254229523fe21f9a30f69887`
(= the pre-state `CodeSha256`, base64-decoded -- confirmed identical, so that version IS the prior
running code). Restore that version, revert `MDPF_GOLD_COMMIT`, `safe-apply`.

### SOVEREIGN AUTHORIZATION FOR THE ROW (received during this deploy)
**Andrew-direct 2026-08-26 ~15:2xZ, VERBATIM** (via `2.0.0_SA_COO` 72415): *"yes Opal Fixed Income is
a 'Model', it is a 'Custom' model, as opposed to a 'Primary' Model which comprises of UST ST INT LT
ULT"*. The measurement established STRUCTURE; his word supplies the INTENT no instrument here could
reach. **It authorizes the ROW; it does NOT widen the build** -- the pin is unchanged.
⛔ TWO FOLLOW-ONS RAISED BY COO, NEITHER ASSUMED AND NEITHER CLOSED BY THIS LEDGER: (a) whether the
served schema must REPRESENT Custom vs Primary (a Rule 24 axis act -- today's row carries no such
marker because none existed); (b) verify the custom model does not disturb the ruled 08-19 five-peer
partition -- routed to `3.0.0_SA_CVO`, to land BEFORE the 08-27 fire.
