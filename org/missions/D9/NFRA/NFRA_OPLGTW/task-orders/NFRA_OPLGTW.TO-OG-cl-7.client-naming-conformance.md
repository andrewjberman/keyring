# NFRA_OPLGTW task order -- `OG-cl-7` -- G2 client modules: firm names resolve through `lookup()`, never hand-kept (naming conformance, CTO msg 34575, LGIC rule 30)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-cl-7</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-cl-7</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~111</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests only; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the CTO's ruling (msg 34575): "adapters resolve firms through lookup() against the registry, with no `# naming-place-override`" (LGIC rule 30, `infra/logic/02_DOCTRINE.md`).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-cl-7` (decomposition addendum R3-T.74, workstream G2-CONFORM, FWD-22)

The six merged client adapters (`app/client_adapter_*.py`: schwab, bd49f, orion, eclipse, bdcottonwood, smartx, commonwealth) and the core (`app/client_core.py`) type the canonical firm names (`49financial`, `cottonwood`, `inflection`) and a few aliases as string literals. The commit-time naming gate in ENFORCE REFUSES them: `hand-kept carrier of 'inflection' outside every permitted context: read it through lookup('inflection')`. A release commit is graded in ENFORCE, so these must conform BEFORE the release.

1. **Measure first.** Build the diff that adds every `app/client_*.py` file whole (`git diff --no-index /dev/null <file>` for each, concatenated) and run `python .tools/naming-gate.py --diff <that diff> --staged-paths <a file listing the paths plus one path under org/missions/D9/NFRA/NFRA_OPLGTW/> --enforce`. Save the output as `W/CL7_BEFORE.txt` (the REFUSE lines name each file, line and literal). A gate run that cannot reach its live read prints a `LIVE-READ-FAILED` note: the REFUSE verdict stands on the literal alone, say so.
2. **Conform.** Read `lib/opal_naming.py` `lookup(scope, registry=None)` (it returns the `scopes.json` row for a long form, a short form or an alias, else `KeyError`) and how the gateway's other modules import from `lib/` (`lib/trading_calendar.py` is the precedent: read how `app/` reaches it and how the deploy stages it). Replace EVERY hand-kept firm-name literal in the seven adapter modules and the core with a read through `lookup(<literal>)` (the argument of `lookup` is the one permitted context) taking the row's `key` or `long` field as the canonical spelling, ONCE per module into a module constant (for example `_INFLECTION = lookup("inflection")["key"]`), and use the constants everywhere. A scope the registry does not hold is a `KeyError`: that is a MISSING REGISTRY ROW, which `4.0.0_SA_CRO~Z` writes (`infra/logic/registry/`): do NOT add the row yourself and do NOT add a placement override; file a BLOCKING row naming the scope and keep the rest.
3. **The deploy fact.** The gateway artifact stages `lib/trading_calendar.py` and not `lib/opal_naming.py` or the registry JSON files. Do NOT edit `deploy-to-ec2.sh` (not yours). Make the import SAFE: the module must still import in the host-shaped check (a 4-parent path with `lib/trading_calendar.py` beside it and NO `lib/opal_naming.py`), by resolving the firm constants lazily at the first call with a clear refusal `registry_unavailable` (an enveloped refusal, zero reads) when `lookup` cannot be imported or read, and by a single fallback seam `client_core.firm_registry` that the release cell will supply (the issuer's release stages the registry copy under `app/refs/`, byte-equal). Say in your report exactly which files the release must stage.
4. **Do not change behaviour.** Every existing client test still passes; every probe line `probe <vendor>: envelope_ok True; ...` still prints for the worker probes you can re-run.
5. Run the naming gate over the same full-add diff again with `--enforce`: it must print NO REFUSE. Save it as `W/CL7_AFTER.txt`.

## 2. BOUNDS

- Code and tests only, in the eight client modules and their tests. No release, no deploy, no IAM, no registry or catalog edit, no placement override, no hand-typed firm map.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print an account number or a person's name; override a gate.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_core.py
infra/aws/ec2/opal-gateway/app/client_role.py
infra/aws/ec2/opal-gateway/app/client_adapter_schwab.py
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/app/client_adapter_orion.py
infra/aws/ec2/opal-gateway/app/client_adapter_eclipse.py
infra/aws/ec2/opal-gateway/app/client_adapter_bdcottonwood.py
infra/aws/ec2/opal-gateway/app/client_adapter_smartx.py
infra/aws/ec2/opal-gateway/app/client_adapter_commonwealth.py
infra/aws/ec2/opal-gateway/tests/test_og_cl1.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
infra/aws/ec2/opal-gateway/tests/test_og_cl3.py
infra/aws/ec2/opal-gateway/tests/test_og_cl4.py
infra/aws/ec2/opal-gateway/tests/test_og_cl5.py
infra/aws/ec2/opal-gateway/tests/test_og_cl6.py
infra/aws/ec2/opal-gateway/tests/test_og_cl7.py
lib/opal_naming.py
lib/trading_calendar.py
infra/logic/02_DOCTRINE.md
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~111/`. Rows: id `NFRA_OPLGTW-Z-W111-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-cl-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl7.AC1.sh; echo "exit=$?"</invocation><expect>(?s)client suites: pytest rc=0; passed [0-9]+ \(want at least 49\); failed 0.*host-shaped import: client modules import without lib/opal_naming True.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-cl-7"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/cl7.AC2.sh; echo "exit=$?"</invocation><expect>(?s)naming gate over the client modules in ENFORCE: rc=0; REFUSE verdicts 0 \(want 0\); hand-kept firm literals 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the existing client suites still pass (at least 49 tests) and the modules still import where `lib/opal_naming.py` is absent (the host shape). `AC2`: the naming gate in ENFORCE over every client module whole prints no REFUSE and no module holds a hand-kept firm-name literal outside a `lookup(...)` call.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-cl-7.client-naming-conformance.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G2-CONFORM (decomposition addendum R3-T.74). CTO msg 34575: conform via `lookup()`, no override, fold into the cl merges; a lookup refusal is a missing registry row, which `4.0.0_SA_CRO~Z` writes. Found by every adapter worker (rows Z-W103-S8, Z-W104, Z-W105-S?, Z-W106-S11, Z-W107-S11): the gate printed REFUSE in the WARN window of their worktrees; the ENFORCE window is the release commit's.
- Slot ~111, spawned when `OG-cl-1` (the core) and the other adapters are merged on trunk, so the files exist in one place.
- Pre-cut: cl7.AC1 base: PASS-or-FAIL read; cl7.AC2 base: FAIL as expected (the hand-kept literals are present).

<status>pending</status>
<round>37</round>
<workstream>G2-CONFORM</workstream>
<slot>~111</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
