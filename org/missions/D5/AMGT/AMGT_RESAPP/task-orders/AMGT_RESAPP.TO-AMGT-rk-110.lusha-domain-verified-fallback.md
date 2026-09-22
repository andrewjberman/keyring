# AMGT_RESAPP task order -- `AMGT-rk-110` -- L-0e: `enrich.domain_for` falls back to the filings battery's issuer-VERIFIED site (`verified_domain_for(source_object)`) when `domains.json` has no entry, at both call sites; never `ceo_public_profile` or a crawl seed; CODE ONLY, 0 Lusha calls

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-rk-110</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~110</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- edits two library modules and adds one test file; arms nothing.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no Lusha call, the Lusha key is never read.
comp-adversary: DECLARED-NOT-APPLICABLE -- a task-order specification, not a produced artifact.
</preflight>

**You are `0.9.0_WK_AMGT_RESAPP~110`.** Work ONLY in the worktree whose absolute path is in your spawn prompt. Your first act
prints `git rev-parse --abbrev-ref HEAD` and `git rev-parse --show-toplevel` and tests that `org/`, `.tools/` and the
existing paths in section 3 exist; if any is absent, STOP with a BLOCKING row. Every Bash call begins
`export OPAL_AGENT_SERIAL=0.9.0_WK_AMGT_RESAPP~110;`. **NEVER RUN AN INSTALL. 0 Lusha calls; the Lusha key is NEVER read.**
Never read, show, diff or check out branch `wk-amgt-14-50` or `C:/tmp/wk-amgt-14-50` -- it holds an exposed credential.

## 1. THE CELL, inlined in full -- `AMGT-rk-110` (round 28, the Lenovo trial's wave 0)

**The governing text, verbatim.**
- rk-106's finding (`deliverables/0.9.0_WK_AMGT_RESAPP~106/B4_ROSTER_DOMAIN_DIAGNOSIS.md` @`e7c45ca8b5`, Q-b): *"the one
  VERIFIED non-guessed candidate is `verified_site.host` ... already read by `enrich.verified_domain_for` (`enrich.py:166-174`)
  -- just never fed into Lusha's `domain_for`. Recommended rule: fall back to `verified_domain_for` when `domains.json` has
  no entry; never `ceo_public_profile.url` or a battery seed/attempt URL."*
- CTO round-27 analysis (msg 24239): *"the B4 roster fix (issuer-verified domain; an officer source for non-SEC names)"*.
  This cell is the DOMAIN half. The officer half is L-0f, in wave 3 (CTO Q6 ruling, msg 24261).

**THE MEASURED STATE at SITEZ `96cc4dae9d` (re-read at your branch HEAD):**
- `lib/research/management/enrich.py:140-148` `domain_for(security_key, table=None)` returns `(company_domain, ir_domain,
  reason)`. With no `domains.json` row it returns `(None, None, "no declared domain for ...")`.
- `:166-174` `verified_domain_for(source_object)` returns `verified_site.host` or None.
- Callers of `domain_for` (Grep, non-test, 2):
  - `enrich.py:643`, inside the management document build. It already HAS `source_object` (`:638`), and already computes
    `verified_domain` at `:653` for the CEO search.
  - `lib/research/harvest/lusha.py:238` in `_cli`, which loads `source_object` via `roster.load_source_object` just above.
- Suites: `lib/research/management/tests` **95 passed, 13 subtests**; `lib/research/harvest/tests` **79 passed**.

**RULED, what you build:**
1. `domain_for(security_key, table=None, source_object=None)`:
   - A `domains.json` row wins EXACTLY as today, with its return value unchanged.
   - With no row and a `source_object` whose `verified_domain_for` is non-empty, return `(host, host, None)`. The 3-tuple
     is kept for compatibility, so no module-level state is added. Instead, add a sibling pure function
     `domain_source_for(security_key, table=None, source_object=None)` that returns `"domains.json"`, `"verified_site"`
     or `None`, so a caller can say which source was used.
   - With no row and no verified host, return EXACTLY today's `(None, None, reason)`, with the reason text unchanged.
   - Never read `ceo_public_profile`, a battery seed, an attempt URL or any other URL field.
2. Both call sites pass `source_object=source_object`.
   - `enrich.py`'s `lusha_meta` gains `"domain_source": domain_source_for(...)`. It is a new key; every existing key keeps
     its value.
   - `lusha._cli`'s printed dict gains `domain_source`.
3. New test `lib/research/management/tests/test_domain_verified_fallback.py`, with arms:
   - `test_declared_row_wins_unchanged`;
   - `test_no_row_verified_host_is_used`: a stub source object with `verified_site.host = "www.example.co.jp"` returns
     that host, and `domain_source_for` returns `"verified_site"`;
   - `test_no_row_no_host_is_todays_refusal`: the reason is byte-equal to today's;
   - `test_never_reads_other_url_fields`: a source object carrying `ceo_public_profile.url` and seed URLs but NO
     `verified_site` returns the refusal;
   - `test_lusha_cli_passes_source_object`: stubbed with `lusha.harvest_company` monkeypatched to record its
     `company_domain`, no client and no key.

**What this cell does NOT change:**
- `domains.json`;
- the officer roster;
- `battery.py`;
- any served object;
- any Lusha call.

## 2. WHERE THIS CAME FROM

**ROUND 28**, decomposition s.36: the Lenovo trial's wave 0, ahead of L-MGMT (the ONE Lusha pass, CTO Q3 ruling msg 24261).

## 3. SURFACES -- what you may read and write

<paths>
lib/research/management/enrich.py
lib/research/harvest/lusha.py
lib/research/management/tests/test_domain_verified_fallback.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~110/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D5/AMGT/AMGT_RESAPP/task-orders/AMGT_RESAPP.TO-AMGT-rk-110.lusha-domain-verified-fallback.md
</paths>

- **A SURFACE NOT NAMED IN `<paths>` IS A WALL.** Scratch is `<your worktree>/.scratch/r110/`.
- **COMMITTING:** `bash .tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~110 <0.9.0_WK_AMGT_RESAPP~110@opal.agent>" -F <msgfile> -- <paths>`.

## 4. BOUNDS

- **CODE ONLY**: no AWS, Lusha or vendor call; the key is never read.
- **Qualified imports in tests** (W85-S1). **Run each test directory in its own pytest call.**
- **A script that carries a backslash is a FILE.**
- **The pin is `96cc4dae9d`.**
- **THE REFUSAL CLAUSE** applies.
- **SURPRISE ROWS:** `AMGT_RESAPP-Z-W110-S<k>`, with `disarm_owner` `2.0.0_SA_COO~Z`. Never print a contact field.

## 5. PROOF OF SPEC (each invocation LITERAL; timeout 600)

`.scratch/r110/ac4.py`:
```
import subprocess
out = subprocess.run(["git", "diff", "--name-only", "96cc4dae9d", "HEAD", "--", "lib", "integrations", "infra", ".tools", "portal"], capture_output=True, text=True).stdout.split()
print("changed_code_files", sorted(out))
for f in sorted(out):
    b = open(f, "rb").read()
    compile(b.decode("utf-8"), f, "exec")
    print(f, "compiles True crlf", b.count(bytes([13, 10])), "non_ascii_chars", sum(1 for ch in b.decode("utf-8") if ord(ch) > 127))
```

<proof_of_spec>
  <criterion id="AC0" cell_refs="AMGT-rk-110"><invocation>cd "$(git rev-parse --show-toplevel)" && sed -n '140,148p' lib/research/management/enrich.py && sed -n '236,240p' lib/research/harvest/lusha.py && python -m pytest lib/research/management/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>BEFORE any edit: domain_for with no source_object parameter; lusha._cli calling enrich.domain_for(args.security_key); then M0 (95, 13 subtests) and H0 (79). Record both</expect></criterion>
  <criterion id="AC1" cell_refs="AMGT-rk-110"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/management/tests/test_domain_verified_fallback.py -v -p no:cacheprovider 2>&1 | tail -8</invocation><expect>"5 passed" and 0 failed, with the five named arms PASSED</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-rk-110"><invocation>cd "$(git rev-parse --show-toplevel)" && python -m pytest lib/research/management/tests -q -p no:cacheprovider 2>&1 | tail -1 && python -m pytest lib/research/harvest/tests -q -p no:cacheprovider 2>&1 | tail -1</invocation><expect>management "N passed" with N = M0 + 5 (subtests unchanged) and harvest "H0 passed", 0 failed in both</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-rk-110"><invocation>cd "$(git rev-parse --show-toplevel)" && python .scratch/r110/ac4.py</invocation><expect>"changed_code_files" lists EXACTLY lib/research/harvest/lusha.py, lib/research/management/enrich.py and lib/research/management/tests/test_domain_verified_fallback.py; each "compiles True crlf 0 non_ascii_chars 0"</expect></criterion>
</proof_of_spec>

**Record each criterion's ACTUAL OUTPUT and its DENOMINATOR.** No judgment criterion.

## 6. WHEN YOU ARE DONE

Write the instance to
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~110/AMGT_RESAPP.TO-AMGT-rk-110.lusha-domain-verified-fallback.proof_of_spec.json`.
Grade it with `python .tools/proof-of-spec-check.py <instance> AC0,AC1,AC2,AC3` (rc 0), flip to `complete` only if every
criterion passes, commit with `--only`, and report once.

**MUTATION DISCIPLINE:** snapshot first. Never `git checkout --`, `stash` or `git show :path`.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5):**
1. **Behavioural consequence, recorded:** after this cell, a management build for a name with NO `domains.json` row but a
   verified site WILL call Lusha (billable) where today it SKIPS. Nothing runs here. Every live run is a later, worded
   cell (L-MGMT for Lenovo only, cap 10 credits).
2. **Keying rule** (Andrew-direct @`5c20841dd1`): the domain comes from the issuer-verified site, NOT the ticker-derived
   key. The existing lookup of the source object by `security_key` is unchanged, pre-existing coupling, flagged in the
   round-27 packet s.3.
3. The 3-tuple is kept to avoid touching every caller and test; `domain_source_for` carries the provenance.

<status>complete</status>
<round>28</round>
<slot>~110</slot>
<fabric>site-z</fabric>
