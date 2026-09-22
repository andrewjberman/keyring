# AMGT_RESAPP task order -- `AMGT-rk-112` -- L-0d: every money figure in the derived model block states its currency -- the REPORTING currency (`EQY_FUND_CRNCY`) against the QUOTE currency (`CRNCY`) -- and NOTHING is converted; CODE ONLY, stub reads, CHAINED after rk-109

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-112</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~112</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- edits one producer module and adds one test file; arms nothing; runs no pull.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS or Bloomberg call; every S3 read in the tests is a STUB.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~112`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. That worktree
is based on rk-109's DRAIN, so re-read `stage_derive` as rk-109 left it. Your first act prints
`git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel`, and tests that `org/`, `.tools/`,
`integrations/bloomberg/research/model_block_pull.py` and `integrations/bloomberg/research/tests/test_stage_derive_fye.py`
(rk-109's) exist. If any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~112;`. **NEVER RUN AN INSTALL. NEVER CALL BLOOMBERG OR S3.** Never read,
show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50`.

## 1. THE CELL, inlined in full -- `AMGT-rk-112` (round 28, the Lenovo trial's wave 0, chained after rk-109)

**The governing text, verbatim.**
- PRD v0.22 s.12 @`d0597e7e0a`, Preconditions: *"**Currency.** The model block states Lenovo's reporting currency (USD)
  against its listing currency (HKD) on every per-share and valuation figure, and never mixes the two silently."*
- CTO ruling, msg 24261 (2026-09-22 14:06Z): *"Q2 (currency): AS RECOMMENDED. Label the reporting currency (USD) against
  the quote currency (HKD) on every figure, and convert NOTHING in the trial. L-0d may join round 28 now, since this
  ruling lands inside the round."*

**THE MEASURED STATE at SITEZ `96cc4dae9d`, before rk-109 (re-read at YOUR base, which carries rk-109's drain):**
- `integrations/bloomberg/research/model_block_pull.py:89-107` `HEADER_FIELDS` carries `CRNCY`, the QUOTE/trading currency
  (`FIELD_BASIS` `:198`). There is NO reporting-currency field: `EQY_FUND_CRNCY` is not requested.
- `:595-599` `_CURRENCY_SENSITIVE_FIELDS` has 13 money fields, among them `SALES_REV_TURN`, `IS_EPS`,
  `BOOK_VAL_PER_SH`, `IS_DIV_PER_SHR`, `NET_DEBT`, `CURR_ENTP_VAL` and `CUR_MKT_CAP`. `PX_LAST` and the ratios are
  deliberately outside it.
- `:602-616` `_currency_caveat(mnemonic, security)` attaches a free-text FINDING only when the field map's cross-check
  flagged the security. Otherwise it is None, so a money figure carries NO currency statement at all.
- The trial baseline (`.scratch/r28_lenovo/BASELINES_992.json`, read-only) found Lenovo's refdata mixing the two scales:
  quote HKD, reporting USD.

**RULED, what you build** (in `model_block_pull.py` only):
1. `HEADER_FIELDS` gains `EQY_FUND_CRNCY`, appended at the END, with a `FIELD_BASIS` line reading "ISO currency code of the
   issuer's financial-statement (reporting) currency."
2. `stage_derive` reads `quote_ccy = header CRNCY` and `reporting_ccy = header EQY_FUND_CRNCY`, each None when absent or
   errored. Every figure dict gains TWO keys:
   - `"currency"`: the currency THIS figure is in, as returned by Bloomberg. A `_CURRENCY_SENSITIVE_FIELDS` member (a
     statement/per-share money figure) gets `reporting_ccy`. `PX_LAST` gets `quote_ccy`. A ratio or percent gets `None`
     (currency-invariant).
   - `"currency_basis"`: one of `"reporting (EQY_FUND_CRNCY)"`, `"quote (CRNCY)"`, `"invariant"`, or
     `"UNSTATED: <reason>"` when the needed header field is absent. An unstated currency is NEVER silently filled in.
3. The block gains top-level `"currencies": {"quote": quote_ccy, "reporting": reporting_ccy, "mixed": quote_ccy != reporting_ccy,
   "converted": False}`.
4. NOTHING is converted, no FX field is requested, and `_currency_caveat` and its value are unchanged.
5. **Non-regression:** every served block is re-derived by a later pull, never by this cell, and this cell's change is
   ADDITIVE keys only. Existing keys keep their values: rk-109's December byte-identity arm must still pass, compared
   after dropping ONLY the new keys `currency`, `currency_basis`, `currencies` and the header figure `EQY_FUND_CRNCY`.
   Amend nothing in rk-109's test file. Put that comparison in THIS cell's test.
6. New test `integrations/bloomberg/research/tests/test_currency_labels.py`, with stubbed reads, with arms:
   - `test_lenovo_shape_labels_usd_vs_hkd`: header CRNCY "HKD" and EQY_FUND_CRNCY "USD". Every money figure is `currency`
     "USD" with the reporting basis, PX_LAST is "HKD" with the quote basis, and `currencies.mixed` is True with
     `converted` False.
   - `test_ratio_is_invariant`: PE_RATIO has `currency` None and basis "invariant".
   - `test_missing_reporting_ccy_is_unstated`: EQY_FUND_CRNCY errored gives every money figure `"UNSTATED: ..."`, and no
     value is invented.
   - `test_no_value_changes`: every figure's `value` is byte-equal to the same derive without this cell's labelling (the
     rk-109 base module loaded from its drain commit, which you name).
   - `test_december_block_equal_modulo_new_keys`: the rk-109 December fixture's block, minus the four new key families,
     equals the pinned block at `96cc4dae9d`, compared the same way rk-109's test does.

**What this cell does NOT change:**
- `fye_join.py`;
- rk-109's test file;
- the field map, the unit map and `_currency_caveat`;
- the pull (beyond one more refdata field NAME, which a later pull requests);
- any S3 object or served block.

## 2. WHERE THIS CAME FROM

**ROUND 28**, decomposition s.36: the Lenovo trial's wave 0. CHAINED after rk-109 on the same module (disjointness).

## 3. SURFACES -- what you may read and write

<paths>
integrations/bloomberg/research/model_block_pull.py
integrations/bloomberg/research/tests/test_currency_labels.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~112/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-112.currency-labels.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL**, including rk-109's `test_stage_derive_fye.py`. Scratch is
  `<your worktree>/.scratch/r112/`.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~112 <0.9.0_WK_AMGT_RESAPP~112@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **CODE ONLY.** **Test FILES are run one pytest call each** (the directory does not collect).
- **A script that carries a backslash is a FILE.**
- **Pins:** `96cc4dae9d` (pre-trial), and rk-109's drain commit (your base; name it in AC0).
- **THE REFUSAL CLAUSE** applies. Pre-existing failures must not GROW.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W112-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Z`.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

`.scratch/r112/ac4.py`:
```
import subprocess
out = subprocess.run(["git", "diff", "--name-only", "96cc4dae9d", "HEAD", "--", "lib", "integrations", "infra", ".tools", "portal"], capture_output=True, text=True).stdout.split()
print("changed_code_files_since_pretrial_pin", sorted(out))
for f in sorted(out):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for ch in b.decode("utf-8") if ord(ch) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-112"><invocation>cd "$(git rev-parse --show-toplevel)" && git log --oneline -3 && sed -n '89,108p' integrations/bloomberg/research/model_block_pull.py && for t in test_stage_derive_fye test_fye_join test_vintage_derivation_identity test_latest_stamp_raw_pair test_forecast_fallback; do echo "$t $(python -m pytest integrations/bloomberg/research/tests/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>BEFORE any edit: the log shows rk-109's drain as the base (record its hash); HEADER_FIELDS has no EQY_FUND_CRNCY; five per-file baselines recorded (test_stage_derive_fye 4 passed if rk-109 landed as ordered)</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-112"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest integrations/bloomberg/research/tests/test_currency_labels.py -v --color=no -p no:cacheprovider 2>&1 | tail -8</invocation><expect>"5 passed" and 0 failed, with the five named arms PASSED</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-112"><invocation>cd "$(git rev-parse --show-toplevel)" && for t in test_stage_derive_fye test_fye_join test_vintage_derivation_identity test_latest_stamp_raw_pair test_forecast_fallback; do echo "$t $(python -m pytest integrations/bloomberg/research/tests/$t.py -q --color=no -p no:cacheprovider 2>&1 | tail -1)"; done</invocation><expect>each line EQUALS its AC0 line -- rk-109's four arms still pass, and no pre-existing failure grows</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-112"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r112/ac4.py</invocation><expect>the changed code files since the pre-trial pin are EXACTLY rk-109's two plus integrations/bloomberg/research/tests/test_currency_labels.py (model_block_pull.py appears once, carrying both cells); each "compiles True crlf 0" and non_ascii_chars equal to the pin's value for model_block_pull.py</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~112/AMGT_RESAPP.TO-AMGT-rk-112.currency-labels.proof_of_spec.json`.
Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3` (rc 0), flip to `complete` only if every
criterion passes, commit with `--only`, and report once.

**MUTATION DISCIPLINE:** snapshot first. Never `git checkout --`, `stash` or `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5):**
1. **CHAINED after rk-109** (same file). Spawn this worker only after rk-109 DRAINS, in a worktree based on the drain.
2. `EQY_FUND_CRNCY`'s entitlement on this Terminal is unmeasured. That is why an absent value gives "UNSTATED", and the
   L-MB pull reads the real reply.
3. The "11 unmapped unit fields" in the plan's L-0d line are NOT in this cell: the ruling covers currency labelling. The
   unit gaps are carried to the trial report.
4. **December non-regression is ADDITIVE-keys-only, NOT byte-identity.** Once L-MB re-derives, every block gains the new
   keys. That is a served change, and it rides L-MB's pair.
5. No new security_key dependency.

<status>pending</status>
<round>28</round>
<slot>~112</slot>
<fabric>site-z</fabric>
