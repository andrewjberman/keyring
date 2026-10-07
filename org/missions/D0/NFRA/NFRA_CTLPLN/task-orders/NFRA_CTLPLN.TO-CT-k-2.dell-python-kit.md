# TO NFRA_CTLPLN.TO-CT-k-2 -- workstream KIT round 1 CT-k-2: the Python kit -- what the fabric's tools import, what a Dell lacks, carried from the laptop

<to_id>NFRA_CTLPLN.TO-CT-k-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~13</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>KIT</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-k-2` (`decompositions/NFRA_CTLPLN_DECOMP.kit1.md`) | **outcome_ref:** FWD-2 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-k-2`, PRD v0.14 C-KIT-PYTHON, the CTO's cell (msg 106086): "third-party imports of .tools/ and lib/ against each Dell's installed
packages, N of N, and the missing ones carried from the laptop over the tailnet, never from PyPI. It also delivers
pandas_market_calendars and ruff, beside the calendar cell." Context: both Dells lack `pandas_market_calendars`, and the shared
trading-day module silently changes its answers without it. You BUILD the three instruments and prove them on this box and on
stand-ins. You install nothing on any box, send nothing, and fetch nothing from any network.

**The hard rule of this cell: NO PACKAGE INDEX.** No `pip install <name>`, no `pip download`, no `pip wheel <name>`, no index URL, no
network call of any kind. Everything a Dell receives is built from what is ALREADY on the laptop's disk. Every pip invocation in your
code and tests carries `--no-index`; a test asserts that the string `--no-index` is present in every pip command the pack and install
tools construct.

**Build:**

1. `org/devices/kit_python_census.py`:
   - `required`: walk every tracked `.py` under `.tools/` and `lib/` (`git ls-files`), parse each with `ast` (a file that does not
     parse is `UNPARSED`, counted, never skipped silently), collect every top-level imported module name, and classify each:
     `STDLIB` (in `sys.stdlib_module_names`), `LOCAL` (resolves to a module or package inside the repo), `THIRD-PARTY` (everything
     else). For each third-party module, the distribution that provides it on THIS box (`importlib.metadata.packages_distributions()`)
     and its installed version, or `NOT-INSTALLED-HERE`; and whether the import is `HARD` (module level, not inside `try`) or `OPTIONAL`
     (inside a `try` with an `ImportError` handler, or inside a function). Print the count of files scanned, the count per class, and
     one line per third-party module with the number of importing files. Write the result to `org/devices/kit_python_required.json`
     (module, distribution, version here, hard or optional, importer count). `ruff` is a tool, not an import: add it explicitly as a
     required distribution with the version installed here and `kind: tool`. LAST line
     `KIT-REQUIRED files=<f> unparsed=<u> modules=<m> stdlib=<s> local=<l> third_party=<t> distributions=<d> not_installed_here=<x> ok=<True|False>`,
     `ok=True` only when `u == 0`.
   - `installed [--out <json>]`: this box's name (`AGENTBUS_DEVICE`, refuse if unset), its Python version and platform tag, and for
     each REQUIRED distribution whether it is installed here and at which version. This is the read a Dell runs.
   - `compare <installed.json>`: against the required file: per distribution `PRESENT`, `MISSING`, or `VERSION-DIFFERS` (print both
     versions; a difference is reported, not failed). LAST line
     `KIT-COMPARE device=<d> python=<v> required=<n> present=<p> missing=<m> version_differs=<v2> hard_missing=<h> ok=<True|False>`,
     `ok=True` only when `m == 0`.
2. `org/devices/kit_python_pack.py --for <installed.json> --out <dir>`: for each MISSING distribution and each of ITS dependencies the
   target also lacks (read `Requires-Dist` from the laptop's installed metadata, recursively; a dependency the laptop itself lacks is
   `UNPACKABLE` and counted), produce an installable artifact from the laptop's disk, in this order of preference: (a) a wheel already
   in pip's local cache or wheelhouse that matches the target's Python version and platform (find them without the network); (b) a
   wheel rebuilt from the INSTALLED files via the distribution's `RECORD` (pure-Python distributions only: a rebuilt wheel of a
   compiled distribution is refused unless the target's Python version and platform tag equal the laptop's, and you say so);
   (c) `UNPACKABLE <name> <reason>`. It refuses outright when the target's Python minor version or platform differs from the laptop's
   and any missing distribution is compiled. It writes `MANIFEST.json` (file name, SHA-256, size, distribution, version, how it was
   obtained) beside the artifacts. LAST line
   `KIT-PACK target=<d> missing=<m> packed=<p> dependencies=<k> unpackable=<u> bytes=<b> ok=<True|False>`.
3. `org/devices/kit_python_install.py --from <dir> [--dry-run]`: the Dell's half. Verifies every file against `MANIFEST.json` (a
   mismatch refuses the whole install), then runs ONE `python -m pip install --no-index --find-links <dir> --user <names>`
   (`--dry-run` prints the command and runs pip with `--dry-run`). It then re-runs the census's `installed` and `compare`. LAST line
   `KIT-INSTALL device=<d> verified=<v>/<n> installed=<i> missing_after=<m> ok=<True|False>`.
4. `org/devices/test_kit_python.py` -- on this box and stand-ins, no network: (1) `required` runs on the real tree and its JSON lists
   `pandas_market_calendars` (as OPTIONAL: it is imported in a `try`) and `ruff` (tool); (2) `installed` then `compare` on THIS box
   reads `missing=0` unless `required` reported `not_installed_here` > 0, in which case the two counts agree; (3) a synthetic
   `installed.json` for a box lacking two pure-Python distributions that this box has -> `compare` reads `missing=2`; (4) `pack` for
   that synthetic target produces artifacts and a manifest, into a temporary directory; (5) `install --dry-run` from that directory in
   a fresh virtual environment created with `python -m venv --without-pip` is NOT attempted (it would need the network for pip): the
   test instead verifies the manifest, flips one byte of one artifact and asserts the install refuses; (6) every pip command string the
   pack and install tools construct contains `--no-index`; (7) a synthetic target with a different Python minor version and a missing
   compiled distribution -> `pack` refuses. LAST line `KIT-TEST cases=<k>/7 ok=<True|False>`.

### ACCEPTANCE

<criterion id="CTk2-AC1" cell_refs="CT-k-2"><invocation>python org/devices/kit_python_census.py required</invocation><expect>unparsed=0</expect></criterion>
`CTk2-AC1` -- every tracked Python file under `.tools/` and `lib/` was parsed and its imports classified, with the denominators
printed. The same line must read `ok=True`, stated in the proof row.

<criterion id="CTk2-AC2" cell_refs="CT-k-2"><invocation>python org/devices/test_kit_python.py</invocation><expect>KIT-TEST cases=7/7 ok=True</expect></criterion>
`CTk2-AC2` -- the read, the comparison, the pack and the install's verification behave on this box and on stand-ins; the tampered
artifact, the missing-two and the version-mismatch arms are the controls.

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No network, no package index, no install on this box, no send to any box, no AWS call.** If `required` reports a third-party
  module `NOT-INSTALLED-HERE`, that is a finding for your report (the laptop itself lacks something its tools import), not something
  to install.
- Packed artifacts are written only to temporary directories or to the `--out` the caller names; none is committed.
- No non-ASCII in any file you write. The commit gate runs ruff: avoid ambiguous single-letter names such as `l`.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W13-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
org/devices/kit_python_census.py
org/devices/kit_python_pack.py
org/devices/kit_python_install.py
org/devices/test_kit_python.py
org/devices/kit_python_required.json
org/devices/kit_terraform_providers.py
org/devices/test_kit_terraform_providers.py
org/devices/kit_terraform_required.json
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: every file under `.tools/` and `lib/`, `org/devices/DEVICES.json`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.kit1.md</decomp_doc> (workstream KIT, round 1), cell `CT-k-2`.
<owned_cells>CT-k-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CTk2-AC1, CTk2-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~13/NFRA_CTLPLN.TO-CT-k-2.dell-python-kit.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CTk2-AC1,CTk2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines; the third-party list (module, distribution, version here, hard or optional, importer count); anything
`NOT-INSTALLED-HERE`; which distributions are compiled; how each of `pandas_market_calendars` and `ruff` would be packed (cache wheel,
rebuilt wheel, or unpackable) and their dependency closures; the exact three commands a Dell and the laptop run in order; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a silent fetch from a package index (--no-index on every pip command, asserted by a test; no pip download or wheel-by-name anywhere); a tampered or truncated pack (SHA-256 manifest verified before any install; the one-byte arm); a compiled wheel installed on a mismatched interpreter (pack refuses on a Python or platform difference); an optional import read as a hard requirement or the reverse (HARD and OPTIONAL classified and printed); a census that skips a file it cannot parse (UNPARSED counted, fails ok); BLIND: each Dell's real interpreter and site-packages -- read only when the Dell runs its half after the drain.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.14 ADDENDUM v0.14 C-KIT-PYTHON; CTO msg 106086; CLAUDE.md "Agent Autonomy" (all egress off Opal infrastructure is
excluded); decomposition KIT round 1. Base dry-run at the cut: CTk2-AC1 and CTk2-AC2 base FAIL as expected (neither file exists).

## AMENDMENT 1 (2.0.0_SA_COO~C, 2026-10-07 ~09:4xZ) -- REOPENED: the Terraform provider cache joins the kit; ruff is already sent

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated and commit 5e1482a22a is inherited state (merged
to the trunk @2479031e22). Authority: `1.0.0_SA_CTO` msg 106117, verbatim: "dell1 cannot terraform init a root because the providers
are not on the box and fetching them is egress ... Provider cache: add it to the same cell -- the provider versions the Dell-placed
projects' roots lock, carried from the laptop's plugin cache over the tailnet, so a Dell's terraform init needs no registry." And:
"ruff: sent by this seat to both Dells by Taildrop ... take it off the kit cell's missing list once each Dell reports the version."
Gate limb: none graded this modification. The Python kit above is done and stays; THE WORK below is the whole of this amendment.

**THE HARD RULE STANDS: NO NETWORK.** No `terraform init` that reaches a registry, no `terraform providers mirror` (it downloads), no
download of any kind. Everything comes from provider binaries ALREADY on the laptop's disk.

1. `org/devices/kit_terraform_providers.py required`: the Terraform roots of the Dell-placed projects, derived exactly as
   `infra/aws/terraform/nfra-ctlpln-identity/tests/derive_resource_kinds.py` derives them (import that function; do not write the
   method twice), plus this project's own two roots (`nfra-ctlpln-identity`, `nfra-ctlpln-agentbus`). For each root, read its
   `.terraform.lock.hcl` (a root with no lock file is `NO-LOCK`, counted) and list each provider's source address, locked version
   and the lock's `h1:` / `zh:` hashes. Print the distinct (provider, version) set with the roots that lock each. Write
   `org/devices/kit_terraform_required.json`. LAST line
   `TF-REQUIRED roots=<r> locked=<k> no_lock=<n> providers=<p> distinct_versions=<v> ok=<True|False>` (`ok=True` when every root was read).
2. `... located`: for each distinct (provider, version), where the laptop holds its binary for `windows_amd64`: the Terraform plugin
   cache directory if one is configured (`TF_PLUGIN_CACHE_DIR`, the CLI config file's `plugin_cache_dir`), else any root's
   `.terraform/providers/` tree. Print the path and size, or `NOT-ON-THIS-BOX` (counted). Verify each found binary against the lock
   file's hashes where the hash scheme can be computed offline (`zh:` is the SHA-256 of the provider's release zip, which you do not
   have; `h1:` is a directory hash of the unpacked provider and CAN be computed from the unpacked files: read how Terraform computes
   `h1` -- the `dirhash` "h1" scheme over the sorted file list -- implement it, and say plainly if you could not match it and why).
   LAST line `TF-LOCATED distinct_versions=<v> found=<f> not_on_this_box=<x> h1_verified=<h>/<f> bytes=<b> ok=<True|False>`.
3. `... pack --out <dir>`: lay the found providers out as a Terraform FILESYSTEM MIRROR
   (`<dir>/registry.terraform.io/<namespace>/<type>/<version>/windows_amd64/<binary>`), the unpacked layout Terraform reads with
   `provider_installation { filesystem_mirror { path = ... } }`, and write a `MANIFEST.json` (path, SHA-256, size, provider,
   version) plus the exact CLI-config snippet a Dell puts in its Terraform CLI config file so `terraform init` uses the mirror and
   never the registry (`direct { exclude = ["registry.terraform.io/*/*"] }`). Hard links or copies, never symlinks.
4. `... verify --from <dir>`: the Dell's half: every file against the manifest; a mismatch refuses.
5. `org/devices/test_kit_terraform_providers.py`: (1) `required` on the real tree lists the `hashicorp/aws` provider and at least the
   two versions this project's two roots lock (the identity root and the agentbus root lock different major versions); (2) `located`
   on this box; (3) `pack` into a temporary directory for ONE small provider if one is present, else for a stand-in directory tree
   the test builds, and `verify` passes; (4) one byte flipped -> `verify` refuses; (5) THE SEAM PROBE: with the mirror the test packed
   and a CLI config pointing only at it (`TF_CLI_CONFIG_FILE` set for that one command), `terraform init -backend=false -input=false`
   in a temporary copy of the smallest locked root succeeds WITHOUT network -- prove "without network" by the config's `direct`
   exclusion and by the init output naming the filesystem mirror; if the needed provider is not on this box, the case records
   `SKIPPED-NOT-ON-BOX` and the last line says so; (6) no command the tool constructs contains `providers mirror` or a URL. LAST line
   `TF-KIT-TEST cases=<k>/6 skipped=<s> ok=<True|False>`.

**ACCEPTANCE, two criteria ADDED to the two above (which are unchanged and must still pass):**

<criterion id="CTk2-AC3" cell_refs="CT-k-2"><invocation>python org/devices/kit_terraform_providers.py required</invocation><expect>TF-REQUIRED roots=</expect></criterion>
`CTk2-AC3` -- every Dell-placed root's provider lock was read; the same line must read `ok=True`, stated in the proof row, with the
`no_lock` count reported.

<criterion id="CTk2-AC4" cell_refs="CT-k-2"><invocation>python org/devices/test_kit_terraform_providers.py</invocation><expect>TF-KIT-TEST cases=6/6</expect></criterion>
`CTk2-AC4` -- the mirror packs, verifies, refuses a tampered file and feeds a real `terraform init` with the registry excluded. The
line must read `ok=True`; a `skipped` count above 0 is reported with the provider that was not on the box.

<expected_criteria>CTk2-AC1,CTk2-AC2,CTk2-AC3,CTk2-AC4</expected_criteria>

(The `<expected_criteria>` line above replaces the earlier one.) Write a NEW proof instance over the old one covering all four ids,
validate it with `python .tools/proof-of-spec-check.py <instance> CTk2-AC1,CTk2-AC2,CTk2-AC3,CTk2-AC4`, and flip `<status>` back to
`complete` only when all four pass. In your report: the distinct provider versions and which roots lock each, which are on this box
and how large, whether `h1` verification matched, and the exact commands a Dell and the laptop run for one delivery.
