# NFRA_OPLGTW task order -- `OG-ch-1` -- G2 client core: two adapters per vendor routed by firm, the Black Diamond read role keyed by firm, the roster name map

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-ch-1</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-ch-1</to_id>
<issued_to>0.9.0_WK_NFRA_OPLGTW~111</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- code and offline tests plus one offline probe; no deploy, no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell changes no IAM; the roles belong to `OG-ap-24`. It only changes WHICH environment variable names the role the code assumes.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is the issuer's ruling A3 of `OG-ap-24` (applier msg 34612): IAM must fence the two Black Diamond firms apart, so the code keys that role by firm.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `OG-ch-1` (decomposition addendum R3-T.75, workstream G2-HOOKUP, FWD-22)

The core `app/client_core.py` and `app/client_role.py` are merged. Seven adapter modules are merged (`app/client_adapter_*.py`: schwab, bd49f, orion, eclipse, bdcottonwood, smartx, commonwealth; commonwealth may still be landing: the tests use fakes, the probe skips a module that is not on your head and says so). The issuer registers them all in one process at the hookup, and three things in the core stop that from working. Read the core and the two modules first, then fix exactly these three, and change nothing else.

1. **Two adapters, one vendor.** `bd49f` and `bdcottonwood` both declare `VENDOR = "blackdiamond"` (they differ in `FIRMS`: `("49financial",)` and `("cottonwood",)`). Today `register_adapter` raises "a different adapter is already registered for this vendor" on the second, and `_adapter(vendor)` returns one module per vendor. Change the registry to hold several modules per vendor, admitted only when their `FIRMS` are DISJOINT (an overlap, or a module without a `VENDOR`, is the existing `ValueError`; registering the same module twice stays idempotent). `registered_vendors()` still returns the sorted DISTINCT vendor names. Every route that picks an adapter (`_single`, `client_get_transactions`, `client_get_fees`, and the `holders` list in `client_resolve_account`) picks the module whose `FIRMS` holds the CANONICAL firm of the call; a firm held by no module of that vendor is the existing `firm_not_served` (zero adapter calls); a vendor nobody registered stays `vendor_not_registered`. The `account_ref` form is unchanged (`****<last4>/<vendor>/<alias>`).
2. **The Black Diamond read role is keyed by firm.** `Ctx._scope` builds the client with `client_role.client_for(vendor)`, so both Black Diamond firms would assume one `BLACKDIAMOND_READER_ROLE_ARN` and IAM could not keep them apart. Add `client_role.role_key(vendor, segment)`: for a vendor in the constant `FIRM_KEYED_VENDORS = ("blackdiamond",)` it returns the vendor plus the prefix's SECOND segment with a trailing `-live` removed, then every non-alphanumeric character removed and lower-cased (`blackdiamond/49f/...` and the live tables' `blackdiamond/49f-live/...` both give `blackdiamond49f`, `blackdiamond/cottonwood/...` gives `blackdiamondcottonwood`); for any other vendor it returns the vendor unchanged. `Ctx._scope` passes the key (so the environment variables are `BLACKDIAMOND49F_READER_ROLE_ARN` and `BLACKDIAMONDCOTTONWOOD_READER_ROLE_ARN`, `<KEY>_READER_EXTERNAL_ID` likewise). A firm-keyed vendor whose own key variable is unset gets the DEFAULT client, never another firm's role (the cache is per key). Types no bucket, prefix or key.
3. **The roster name map (ruling A2 of `OG-cl-5`, CRO msg 34577).** `Ctx.firm_roster()` today reads `doc["advisor_firms"]`, a key the real roster does not carry. It must return `{advisor_name: canonical firm id or None}` built from `data/mdpf/config/partner_roster.json` `partners[].aliases.advisor_name`: each partner's `firm_id` is the canonical firm (map it to the core's `FIRM_CANONICAL` spelling: `49financial`, `cottonwood`, `inflection`; a `firm_id` that is none of those, or a name with no firm, maps to `None`). The file the core reads stays `ROSTER_FILE` (`app/refs/partner_roster.json`, a byte-equal copy the issuer supplies at the hookup); your tests and probe point it at the repo file `data/mdpf/config/partner_roster.json` (monkeypatch the module constant). A `roster` passed to `Ctx(...)` still wins unchanged.
4. **The Black Diamond fence (A1).** `Ctx.firm_segments(vendor, firm)` returns `[]` for any vendor whose `FENCE_KIND` entry for the firm is not `"all-segments"`, and `FENCE_KIND` has no `blackdiamond` entry, so BOTH Black Diamond adapters refuse every read (`bd49f._firm` wants exactly one segment; `bdcottonwood` wants `[firm]`). Add a second fence kind to `FENCE_KIND`: `{"blackdiamond": {"49financial": ("segment", "49f"), "cottonwood": ("segment", "cottonwood")}}`, and make `firm_segments` return `[segment]` for a `("segment", name)` entry ONLY IF some catalog row's prefix starts with `<vendor>/<name>/silver` (else `[]`); the `"all-segments"` kind is unchanged. A firm with no entry stays `[]` (the existing refusal path).

### Tests, named (fakes only; no network; an Opal stand-in principal where the admit scope needs one)

- `test_ogch1_ac01`: two fake adapter modules with the same `VENDOR` and disjoint `FIRMS` register; an overlapping third raises `ValueError`; the same module twice is idempotent; `registered_vendors()` lists the vendor once.
- `test_ogch1_ac02`: for the shared vendor, a call naming each firm reaches ONLY that firm's module (recording fakes, for `client_resolve_account` and for each of the four account tools); a canonical firm held by neither module is `firm_not_served` with zero adapter calls; an unregistered vendor is `vendor_not_registered`.
- `test_ogch1_ac03`: `role_key` for `("blackdiamond","49f")`, `("blackdiamond","Cotton-Wood")`, `("schwab","anything")`; with BOTH key variables set to two different ARNs and a recording STS factory, a `blackdiamond/49f/` prefix assumes the 49F ARN and a `blackdiamond/cottonwood/` prefix the Cottonwood ARN; `role_key("blackdiamond", "49f-live")` is `blackdiamond49f`; with only the Cottonwood variable set, a 49F read gets the default client and assumes nothing.
- `test_ogch1_ac04`: `firm_roster()` over the repo roster file returns a map in which "49 Financial Group" is `49financial` and every value is a canonical firm (A1: the repo file carries no unmapped name, so there is NO clause that a name maps to `None` over it), and a synthetic roster document with a non-canonical `firm_id` maps that name to `None`.
- `test_ogch1_ac05`: the seven real adapter modules that exist on your head import and register in ONE process without error, and `registered_vendors()` equals the sorted distinct `VENDOR` values of the modules registered.
- `test_ogch1_ac06`: the Black Diamond fence over a synthetic catalog that holds `blackdiamond/49f/silver/...` and `blackdiamond/cottonwood/silver/...` rows: `firm_segments("blackdiamond","49financial")` is `["49f"]`, `("blackdiamond","cottonwood")` is `["cottonwood"]`, a catalog without the cottonwood silver rows gives `[]` for cottonwood, `("blackdiamond","inflection")` is `[]`, and the `schwab` all-segments kind is unchanged.

**Your probe** (`W/probe_ch1.py`, a script you write and run; the issuer re-runs it as AC2): it imports the core and every `app/client_adapter_*.py` on your head, registers them all, and asserts: (a) the number of registered modules equals the number of adapter files found; (b) the two Black Diamond firms route to different modules and `firm_segments` names one segment for each (`49f` and `cottonwood`) over the repo catalog `app/refs/DATA_CATALOG.yaml` read through the core's own loader; (c) the two firm role keys differ and neither equals the other's environment variable name; (d) `firm_roster()` over the repo file maps at least one name to each of `49financial` and, if present in the file, `inflection`. It prints exactly one line `probe ch1: adapters_registered_equals_files True; bd_split True; role_keys_distinct True; roster_names_mapped True` and nothing with eight or more digits in a row.

## 2. BOUNDS

- `app/client_core.py`, `app/client_role.py`, `tests/test_og_ch1.py` and your probe only. Do NOT edit any adapter module, `app/tools.py`, `app/data_entitlement.py`, `app/destructive_ops.py`, any pinned-count test, any IAM or Terraform file, `deploy-to-ec2.sh` or the catalog. The existing client suites (`tests/test_og_cl1.py` to `cl6.py`) must still pass unchanged.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; print a person's name, an account number or an amount; override a gate. Tool names must not end in `_group`, `_role` or `_profile` (you add none).
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/client_core.py
infra/aws/ec2/opal-gateway/app/client_role.py
infra/aws/ec2/opal-gateway/tests/test_og_ch1.py
infra/aws/ec2/opal-gateway/tests/test_og_cl1.py
infra/aws/ec2/opal-gateway/tests/test_og_cl2.py
infra/aws/ec2/opal-gateway/tests/test_og_cl3.py
infra/aws/ec2/opal-gateway/tests/test_og_cl4.py
infra/aws/ec2/opal-gateway/tests/test_og_cl5.py
infra/aws/ec2/opal-gateway/tests/test_og_cl6.py
infra/aws/ec2/opal-gateway/app/typed_scope.py
infra/aws/ec2/opal-gateway/app/harvest_typed.py
infra/aws/ec2/opal-gateway/app/client_adapter_schwab.py
infra/aws/ec2/opal-gateway/app/client_adapter_bd49f.py
infra/aws/ec2/opal-gateway/app/client_adapter_orion.py
infra/aws/ec2/opal-gateway/app/client_adapter_eclipse.py
infra/aws/ec2/opal-gateway/app/client_adapter_bdcottonwood.py
infra/aws/ec2/opal-gateway/app/client_adapter_smartx.py
infra/aws/ec2/opal-gateway/app/client_adapter_commonwealth.py
data/mdpf/config/partner_roster.json
lib/trading_calendar.py
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/G2_ADAPTER_PROTOCOL.md
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The adapter modules are listed to be READ and imported, not edited (bound above). `W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~111/`. Rows: id `NFRA_OPLGTW-Z-W111-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-ch-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ch1.AC1.sh; echo "exit=$?"</invocation><expect>(?s)pytest rc=0; named tests passed 6 of 6; failed/error lines 0.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-ch-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/ch1.AC2.sh; echo "exit=$?"</invocation><expect>(?s)probe ch1: adapters_registered_equals_files True; bd_split True; role_keys_distinct True; roster_names_mapped True.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the six named tests pass. `AC2`: the probe, re-run here, registers every adapter on your head in one process and proves the Black Diamond split, the distinct firm role keys and the roster name map.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-ch-1.client-core-hookup-fix.proof_of_spec.json` (also a byte-identical copy at the hyphen stem the status flip reads, as the earlier workers did). Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once. Your report names the exact environment variable names the host needs.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream G2-HOOKUP (decomposition addendum R3-T.75). Found at the hookup: both Black Diamond adapters declare `VENDOR = "blackdiamond"`, so `register_adapter` raises on the second; and the applier (`OG-ap-24` Phase A, msg 34612) found the role key is the vendor, which would put both firms behind one role. `Ctx.firm_roster` reads a key (`advisor_firms`) the real roster does not carry (the `OG-cl-5` A2 ruling).
- Slot ~111; `OG-cl-7` (naming conformance of the same files) follows in this slot's queue AFTER this order is merged: one chain, never two workers on `client_core.py`.
- Pre-cut: ch1.AC1 base: FAIL as expected (tests absent); ch1.AC2 base: FAIL as expected (probe absent).

- A1 (issuer, 2026-10-16 ~00:5xZ, worker rows Z-W111-S1 to S3): (1) THE AC04 CLAUSE IS WITHDRAWN: the repo roster maps every name to a canonical firm, so "at least one name is None" was an issuer error; the None arm is the synthetic non-canonical document only. (2) `role_key` strips a trailing `-live` (the live Black Diamond tables sit at `blackdiamond/49f-live/`). (3) The Black Diamond fence is added to the core (item 4, `FENCE_KIND` second kind): without it every Black Diamond read refuses at the hookup. New test `ac06`; AC1 reads 6 of 6. Your inherited commits are `b19745d35b` and `c6beffe883`. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>G2-HOOKUP</workstream>
<slot>~111</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
