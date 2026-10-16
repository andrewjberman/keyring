# What the intake tools demand of the approval file and the signed file

Read from the CODE at this commit; each rule names its function and line. Each example block is graded by
`.tools/tests/test_round28_intake_page.py` through the gate named above its fence. Names are synthetic.

## 1. The approval-file line

A line must pass BOTH readers.

- **fetch** (`intake_fetch.py` `Fetch.approval` 355-357, `approval_gate` 630-641): CASE-SENSITIVE search for `name==version`,
  not preceded by a letter, digit, `.`, `_` or `-`, not followed by a letter, digit, `.`, `_`, `+` or `!`. A trailing comment
  passes; a hash suffix passes.
- **check 2** (`intake_check.py` `check_2` 385-402, `norm_name` 202): cuts at `#`, strips, splits at the first `==`, folds the
  name (case, `-`, `_`, `.`), compares the version exactly. It is laxer on case and spaces; it refuses a hash suffix.

Write the bare lowercase form `examplepkg==1.2.3`, optionally followed by `  # comment`.

<!-- gate: intake_fetch.approval_gate -->
```text accepted
examplepkg==1.2.3
examplepkg==1.2.3  # the one line the CTO approved
```

<!-- gate: intake_fetch.approval_gate -->
```text refused
ExamplePkg==1.2.3
examplepkg == 1.2.3
examplepkg[socks]==1.2.3
examplepkg==1.2.4
examplepkg==1.2.3.post1
examplepkg-1.2.3-py3-none-any.whl
```

<!-- gate: intake_check.check_2 -->
```text refused
examplepkg==1.2.3 --hash=sha256:0000000000000000000000000000000000000000000000000000000000000000
examplepkg[socks]==1.2.3
examplepkg==1.2.4
examplepkg==1.2.3.post1
examplepkg-1.2.3-py3-none-any.whl
```

Dry run of one line: NONE. `intake_fetch.py resolve` checks the file before any socket, then requests release documents.

## 2. The signed check-8 file

- **Where:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/` or below (`DEFAULT_SIGNER_REL` 52, `check_8` 831-841). Never the
  approval file, by path or content (845-855).
- **Names:** the text must contain the batch id AND the full wheel file name (`check_8` 856-859). The project name alone fails.
- **Marker:** a line starting with `CHECK 8 SIGNED` or `SIGNED, check 8` after markdown is stripped (`has_sign_marker` 784-794).
  Without it no WAIVE line is read (860-862). Dry run of a signed file: NONE.

<!-- gate: intake_check.check_8 -->
```text accepted
# CTO check 8 -- batch intake-20261016-example
CHECK 8 SIGNED -- release may proceed for this file.
examplepkg-1.2.3-py3-none-any.whl
```

<!-- gate: intake_check.check_8 -->
```text refused
# CTO check 8 -- batch intake-20261016-example
CHECK 8 SIGNED -- release may proceed.
---
# CTO check 8 -- batch intake-20261016-example
examplepkg-1.2.3-py3-none-any.whl is NOT check 8 SIGNED yet.
---
# CTO check 8
CHECK 8 SIGNED -- examplepkg-1.2.3-py3-none-any.whl
```

## 3. The `WAIVE` line

Form: `WAIVE <file name> check <N>: <reason>`, one file and one check per line (`WAIVE_RE` 798, `parse_waivers` 801-823).

- Checks 3 to 7 only (`WAIVABLE_CHECKS` 797). A WAIVE for check 1 or 2 fails check 8 for the whole file (818-819, 864-867).
  Check 8 and numbers outside 1 to 7 are ignored (820-822). No wildcard, no batch form (810). The reason is non-empty (814).
- Verdict: `_derive` (908-924) carries a failed check 3 to 7 with a matching waiver; the verdict becomes
  `released-with-waiver`, naming the checks. The record keeps the failure.

<!-- gate: intake_check.parse_waivers -->
```text accepted
WAIVE examplepkg-1.2.3-py3-none-any.whl check 6: compared across platforms; the differing file is build metadata
- WAIVE examplepkg-1.2.3-py3-none-any.whl check 3: the version already runs on this machine
```

<!-- gate: intake_check.parse_waivers -->
```text refused
WAIVE examplepkg-1.2.3-py3-none-any.whl check 1: the digest differs
WAIVE examplepkg-1.2.3-py3-none-any.whl check 8: the signature
WAIVE examplepkg-1.2.3-py3-none-any.whl check 6:
WAIVE examplepkg-1.2.3-py3-none-any.whl check 6
WAIVE * check 6: any file
WAIVE examplepkg check 6: the project name only
WAIVE examplepkg-1.2.3-py3-none-any.whl check 9: out of range
```

## 4. The order of the batch route

1. request: `intake_request.py file --name N --version V --needed-by T --why-no-approved T --by SEAT`
2. approval: the CTO writes the approval file (section 1); `intake_request.py decide --id REQ --verdict APPROVED --by SEAT --reason T --evidence <file>`
3. fetch: `intake_fetch.py fetch --batch B --name N --version V --python-tag T --abi-tag T --platform-tag P --approved-by <file>`
4. checks 1-7: `intake_check.py check --batch B --file <file name> --approved-by <file>` (check 8 reads unsigned)
5. signed check 8: the CTO writes the signed file (sections 2-3); `intake_check.py check` again with `--signed-by <file>`
6. release: `intake_check.py release --batch B --file <file name>`
7. pack: `intake_check.py pack --batch B --out <dir> [--released-only]`
8. verify: `intake_receive.py verify --from <pack>`
9. send: no tool verb; the pack goes to the receiving box, where `intake_receive.py prove` then `install --target <new dir>`

## 5. The dry-run commands

| tool | verb | reads | writes |
|---|---|---|---|
| `intake_check.py` | `selftest-unsigned` | a synthetic wheel in a temporary folder | nothing |
| `intake_check.py` | `selftest-av` | the Security Center antivirus list | nothing |
| `intake_receive.py` | `selftest-unchecked` | a synthetic pack in a temporary folder | nothing |
| `intake_receive.py` | `install --from <pack> --target <new dir> --dry-run` | a verified pack | nothing |
| `intake_request.py` | `status --name N --version V` | request records, `requirements.txt` | nothing |
| `intake_fetch.py` | `list --batch B` | records and the holding folder | nothing |
