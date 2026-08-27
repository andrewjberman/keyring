# DEPLOY-COMPLETION LEDGER -- mdpf-gold-lambda LEG A-PRIME (cottonwood pair decomposition fix)

**Opened:** 2026-08-26T18:13:38Z by `0.6.2_AE_PartnerETL~A` (**deploy-start**; NEVER#6)
**Status:** **CLOSED 2026-08-26T18:23:44Z** -- applied, verified on the RUNNING bytes, no leg stranded
**Authority:** `1.0.0_SA_CTO` 72684 (Leg A-Prime is AE) · `2.0.0_SA_COO` 72878 operative sequencing,
GO on `bae0a826d3`. Leg A's ledger (`@1e73554830`) is CLOSED and separate; this is its own deploy.
**Project:** MDPF_COTREMEDIATION / D8

> ⚠ **THIS FILE WAS REWRITTEN AT 18:1xZ AFTER I CORRUPTED IT MYSELF.** I edited it with an UNQUOTED
> heredoc (`<<PYEOF` rather than `<<'PYEOF'`), so bash command-substituted every backticked term in my
> replacement strings and **silently deleted them** -- leaving grammatical rows with their values gone
> (`"DIVZ PLACEMENT | -> ; NOT in /sidecar"`), plus a duplicate row 6. Nothing executed harmfully; the
> terms were not commands. **Recorded here rather than quietly fixed**, because a ledger that was
> briefly wrong about its own evidence is exactly the thing a reader must be able to see. The estate's
> banked class: content crossing a shell-parsed region is evaluated by that shell.

---

## WHAT IS BEING DEPLOYED

Carries `0.4.0_DS_ClientPlatform~T`'s cottonwood pair decomposition fix into the running bundle: the
`:133` pre-filter is removed so accounts assigned to a non-Opal container holding Opal children
descend; the residual classifies as `Client - Opal Supervised` via a cited literal; and the Opal SMA
sleeve routes to `meta.sma_l0.by_key` per Andrew's 17:42/17:45Z ruling.

**BUILD PIN `5043bbe8d4`** = running vintage `48c473caa1` + `bae0a826d3`'s
`build_cottonwood_mdpf_pair.py` ONLY. Isolated worktree (`legA-prime3`). **Not for merge. NOT HEAD.**
Zip 723,461 B, sha256 `2dd4a1b0c985beb3c7abb696f33088d7320dee8e187609111c796915f3ceff1b`,
22 modules, import-closure PASS.

> **STILL NOT HEAD, AND THE INTERLOCK STILL BINDS.** D1_CATVIEWS remains NO-SHIP;
> `mdpf_category_registry` stays at its pre-defect bundle vintage and UNREFERENCED;
> `mdpf_aggregate_aua`'s defective `:699`/`:703` sites do NOT ride. Changed member set is ONE FILE.

---

## PRE-STATE CONTROL (captured before deploy-start; all three must move)

```
mdpf-gold-lambda  LastModified 2026-08-26T15:29:34Z  CodeSize 701,490
CodeSha256  3/897ecG2Xzal+0Xl+Ygoshsqccd6smAcMwygv8KjZQ=
MDPF_GOLD_COMMIT 48c473caa1aebd2c9b40d9f6ef81fe692adc830d
running build_cottonwood_mdpf_pair.py CARRIES the :133 pre-filter as LIVE CODE
```

## PRE-APPLY ARMS (all run against the DEPLOYED bundle before the apply)

| # | Arm | Result |
|---|---|---|
| 1 | MEMBERS diff vs running bundle | ADDED none · REMOVED none · CHANGED [BUILD_MANIFEST, the pair file] |
| 2 | NO `mdpf_category_registry` import, AST over ALL scopes | zero import nodes (catches aliased + function-local) |
| 3 | SYMBOL CLOSURE vs bundle-vintage members | 17 refs checked, **0 ABSENT** |
| 4 | Cited literal present; live `display_label` call sites | literal TRUE; **0 live calls** (2 textual hits are comments at :85/:93) |
| 5 | **NEGATIVE CONTROL** — ARM 2 re-subjected at the superseded build `e9d7c37976` | **FIRES at line 66** |
| 6 | DIVZ PLACEMENT (CTO 72856 constraint 4) | `OPAL_SMA_LEAF_KEYS = {"DIVZ SMA": "opal_div_sma"}` -> `meta.sma_l0`; **NOT** in `by_model` or the sidecar, so `GLOBAL_ACCOUNT_DIST_DISPLAY` is never consulted and no crosswalk edit is needed |
| 7 | `sys.modules` behavioural arm (COO 72774 s.2) | post-apply, on the rebuilt bundle's own copy |

> **ARM 5 IS WHAT MAKES THE REST MEAN ANYTHING.** It was first pointed at the RUNNING copy, which
> predates the `mcr` import entirely and therefore could never have shown the arm firing. Re-pointed at
> the superseded build it fires at line 66. **An arm that cannot fail is not a control.**

---

## LEGS

| # | Act | Status |
|---|---|---|
| 1 | Mint pin `5043bbe8d4` (isolated worktree) | **DONE** |
| 2 | Build package | **DONE** — 723,461 B, `2dd4a1b0...` |
| 3 | Pre-apply arms 1-6 | **DONE** — all clean; negative control fires |
| 4 | Upload artifact to the Terraform source key | **DONE** — VersionId `hAFXzyqIdtpFHJDPahO6QOuRWf.fnfJF`, 723,461 B, metadata sha matches |
| 5 | safe-apply -target=aws_lambda_function.mdpf_gold | **DONE** 18:21Z -- plan 0 add / 1 change / 0 destroy; apply reported the same |
| 6 | Post-apply proof on RE-DOWNLOADED running bytes | **DONE** -- see PROOF below |
| 7 | Tear down worktree (RETAIN branch — the pin must stay reachable) | **DONE** 18:23Z -- branch legA-prime3 RETAINED so pin 5043bbe8d4 stays reachable |

---

## WHAT THIS ENTRY DOES **NOT** CLOSE

- **A9 GRADING.** `0.4.0_DS_ClientPlatform~T` re-fires the `qa_local` ad-hoc and grades — the grader
  stays the seat that pre-registered against the bar. PRIMARY arm is the DELTA (`0.0100` present,
  `43676557.1200` absent), not the count: a 12/12 is consistent with two worlds.
- **A5a / A5b.** Both are IN this deploy and both were pre-registered MET by
  `0.4.0_DS_ClientPlatform~T` **in-process** (A5a 2,256,694.98 full-segment / 1,476,313.07 at COO's
  grain; A5b 1,393,065.98, denominator ONE account). That seat re-grades them off the LAMBDA run —
  in-process evidence is not evidence about the lambda's output.
- **PRODUCTION ACCEPTANCE** — tomorrow's 2026-08-27 13:30Z SCHEDULED fire on CVO's absolute bar.
- **THE SERVE DECISION.** Andrew ruled **conditional-YES** at 18:10Z (@666fe25b0c): green grade ->
  the 08-27 fire serves the corrected split; not green -> nothing serves and the fork returns to him.
  **A green grade tonight is the DAY's acceptance, not a release.**

## ROLLBACK (same-window)

Versioned artifact bucket. Prior version = the Leg A artifact, VersionId
`uGLKSxGv0WkvTRNfQQznjaOOzFvsCm8m`, 701,490 B,
`content-sha256 dfff3dede706d97cda97ed1797e620a2c86ca9c71deac98070cc3282ff0a8d94` — which decodes to
the pre-state `CodeSha256`, so that version IS the prior running code. Restore it, revert
`MDPF_GOLD_COMMIT` to `48c473caa1aebd2c9b40d9f6ef81fe692adc830d`, `safe-apply`.

---

## CLOSE-OUT

**CLOSED 2026-08-26T18:23:44Z by `0.6.2_AE_PartnerETL~A`. All 7 legs done. Nothing half-landed.**

### PROOF ON THE RUNNING PLANE (re-downloaded bundle; every limb moved, and the control was real)

| | PRE (control) | POST |
|---|---|---|
| `LastModified` | 2026-08-26T15:29:34Z | **2026-08-26T18:21:12Z** |
| `CodeSha256` | `3/897ecG2Xzal+0Xl+Ygoshsqccd6smAcMwygv8KjZQ=` | **`LdShsMmFvrPHq7aW8zCI1zIN7o4YdgkRHHlpFfPO/xs=`** |
| `CodeSize` | 701,490 | **723,461** (= the built zip exactly) |
| `MDPF_GOLD_COMMIT` | `48c473caa1...` | **`5043bbe8d47e0a0948d6896c3092c576fa28494a`** |
| `:133` pre-filter as LIVE CODE (AST) | **True** | **False** |
| cited literal `Client - Opal Supervised` | absent | **present** |
| live `display_label` call sites | n/a | **0** |
| `mdpf_category_registry` import nodes | n/a | **NONE** |
| `OPAL_SMA_LEAF_KEYS` (DIVZ -> `meta.sma_l0`) | absent | **present** |

in-zip `source_vintage` = `{"commit": "5043bbe8d47e0a0948d6896c3092c576fa28494a", "pin": "5043bbe8d4"}`
— matches `MDPF_GOLD_COMMIT` on the applied plane. **Declaration and bytes agree.**

**BOTH of `3.0.0_SA_CVO`'s required vintage instruments moved** (72801: COULD-NOT-VERIFY unless both
`LastModified` AND `CodeSha256` move off the stated baseline). They did.

### THE ONE DEFECT I CAUSED IN THIS DEPLOY, AND IT WAS MINE

At 18:13Z I edited this ledger with an **UNQUOTED heredoc** (`<<PYEOF`, not `<<'PYEOF'`). Bash
command-substituted every backticked term in my replacement strings and **silently deleted them**,
leaving grammatical rows with their values gone — `"DIVZ PLACEMENT | -> ; NOT in /sidecar"` — plus a
duplicate row 6. The shell printed `command not found` for `opal_div_sma`, `by_model`,
`OPAL_SMA_LEAF_KEYS` and others, which is what surfaced it.

**Nothing executed harmfully** (the terms were not real commands) and **no deployed artifact was
touched** — the corruption was confined to this file, between 18:13Z and the rewrite minutes later.
The file was rewritten in full with a non-shell writer, which is the estate's prescribed remedy.

⛔ **This is a banked class and I was carrying it in memory when I did it.** The recorded form:
*content crossing a shell-parsed region is evaluated by that shell; backticks EXECUTE.* CLAUDE.md
Git §F-010 says the same about commit messages built by a shell, and its stated remedy — *write the
message with a non-shell writer, THEN feed it* — is exactly what I failed to do here and then had to
do afterwards. **A LOUD failure this time; the same mistake with a real command name is silent.**

### WHAT THIS ENTRY DOES NOT CLOSE

- **A9 GRADING** — `0.4.0_DS_ClientPlatform~T` re-fires the `qa_local` ad-hoc and grades. PRIMARY arm
  is the DELTA (`0.0100` present, `43676557.1200` absent), not the count.
- **A5a / A5b off the LAMBDA run** — that seat's in-process values are not evidence about the
  lambda's output, as it said itself.
- **PRODUCTION ACCEPTANCE** — the 2026-08-27 13:30Z SCHEDULED fire, CVO's absolute bar.
- **THE SERVE** — Andrew's conditional-YES (18:10Z, @666fe25b0c) turns on tonight's grade. **A green
  grade is the DAY's acceptance, not a release.**
