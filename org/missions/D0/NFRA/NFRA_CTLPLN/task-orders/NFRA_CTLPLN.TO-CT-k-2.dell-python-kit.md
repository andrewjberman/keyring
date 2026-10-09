# TO NFRA_CTLPLN.TO-CT-k-2 -- workstream KIT round 1 CT-k-2: the Python kit -- what the fabric's tools import, what a Dell lacks, carried from the laptop

<to_id>NFRA_CTLPLN.TO-CT-k-2</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~13</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>in_progress</status>
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
org/devices/kit_portal_tree.py
org/devices/test_kit_portal_tree.py
org/devices/kit_bun_no_egress.py
org/devices/kit_python_wheels.py
org/devices/test_kit_python_wheels.py
org/devices/kit_python_wheels_cp314.json
org/devices/kit_python_repack.py
org/devices/test_kit_python_repack.py
org/devices/intake/closure_cp312_win_amd64.json
org/devices/intake/intake_closure.py
requirements.txt
org/devices/test_kit_bun_no_egress.py
.tools/wk-provision.sh
.tools/tests/test_wk_provision_no_registry.py
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

<criterion id="CTk2-AC4" cell_refs="CT-k-2"><invocation>python org/devices/test_kit_terraform_providers.py</invocation><expect>TF-KIT-TEST cases=10/10</expect></criterion>
`CTk2-AC4` -- the mirror packs, verifies, refuses a tampered file and feeds a real `terraform init` with the registry excluded. The
line must read `ok=True`; a `skipped` count above 0 is reported with the provider that was not on the box.

<expected_criteria>CTk2-AC1,CTk2-AC2,CTk2-AC3,CTk2-AC4,CTk2-AC5,CTk2-AC6,CTk2-AC7,CTk2-AC8,CTk2-AC9,CTk2-AC10,CTk2-AC11,CTk2-AC12</expected_criteria>

(The `<expected_criteria>` line above replaces the earlier one.) Write a NEW proof instance over the old one covering all four ids,
validate it with `python .tools/proof-of-spec-check.py <instance> CTk2-AC1,CTk2-AC2,CTk2-AC3,CTk2-AC4`, and flip `<status>` back to
`complete` only when all four pass. In your report: the distinct provider versions and which roots lock each, which are on this box
and how large, whether `h1` verification matched, and the exact commands a Dell and the laptop run for one delivery.

## AMENDMENT 2 (2.0.0_SA_COO~C, 2026-10-07 ~10:1xZ) -- REOPENED: the portal dependency tree joins the kit

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated and commits 5e1482a22a, 8170113d42 and
c46c682f7d are inherited state (merged to the trunk @16b9fd1ba8). Authority: `1.0.0_SA_CTO` msg 106138 and
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULINGS_FOR_THE_DELLS_20261007_1000Z.md` section 4, verbatim: "The bring-up kit carries
the laptop's portal dependency tree at the DEV lockfile, over the tailnet, read back by one typecheck run on each Dell; nothing is
fetched from the npm registry by a Dell. `2.0.0_SA_COO~C` adds it to the kit cell beside the Python packages and the Terraform
providers. All four boxes run Windows, so one tree serves; the cell states the Node or bun version it was built under and refuses a
box whose version differs." Gate limb: none graded this modification. The Python and Terraform kits above are done and stay; THE WORK
below is the whole of this amendment.

**THE HARD RULE STANDS: NO NETWORK.** No `bun install`, `bun add`, `npm install`, `npm ci`, `npx` of an uninstalled package, or any
command that may contact a registry. You read a dependency tree that is ALREADY on the laptop's disk.

**Where the portal is.** `portal/` is a nested git repository (a submodule of the workspace). Your own worktree's `portal/` directory
may be empty. THE READ-ONLY EXCEPTION for this amendment: you may READ (never write, never run an install in) the base checkout's
portal tree: its path is `<base>/portal`, where `<base>` is the first entry of `git worktree list --porcelain`. Derive it; do not
hardcode it. Its `node_modules` is the tree to carry.

1. `org/devices/kit_portal_tree.py describe [--portal <dir>]`: the portal repository's HEAD commit and branch; the lockfile it holds
   (`bun.lock` or `bun.lockb`, and `package-lock.json` if present: name which exists) with its SHA-256; whether that lockfile equals
   the one at the portal's `origin/DEV` (compare the blob of `git -C <portal> show origin/DEV:<lockfile>` with the working file; do
   NOT fetch: if `origin/DEV` is not present locally, print `DEV-REF-ABSENT` and say so); the `bun --version` and `node --version` on
   this box (`NOT-INSTALLED` is a value); the platform; and the tree's size: top-level package count, total files, total bytes.
   Whether the tree on disk matches the lockfile: count the packages the lockfile names and the top-level and nested package
   directories present, and report `lock_packages=<n> present=<p> absent=<a>` by reading each `node_modules/**/package.json` name and
   version against the lockfile where the lockfile is text (`bun.lock`); for a binary `bun.lockb`, use `bun pm ls --all` ONLY if it
   runs offline (it reads the lockfile and the tree; if it tries the network, do not use it) and say which method you used. LAST line
   `PORTAL-TREE head=<commit> lockfile=<name> lock_sha256=<12 hex> equals_dev=<True|False|DEV-REF-ABSENT> bun=<v> node=<v> packages=<n> present=<p> absent=<a> files=<f> bytes=<b> ok=<True|False>`,
   `ok=True` only when `absent == 0` and the lockfile was read.
2. `... pack --out <dir>`: one archive of `node_modules` (a tar written by Python's `tarfile`, uncompressed or gzip level 1: state
   which, and why; preserve relative symlinks and junctions as links where `tarfile` can, and LIST any it could not represent) plus
   `MANIFEST.json`: the archive's SHA-256 and size, the lockfile name and SHA-256, the portal HEAD, the bun and node versions, the
   platform, file count and byte count, and the list of binary or platform-specific packages found (a package with a `.node` file, a
   `bin` shipping an `.exe`, or an `os` / `cpu` field in its `package.json`). The pack REFUSES when `describe` is not `ok`.
3. `... verify --from <dir> --portal <dir> [--extract]`: the Dell's half. Refuses unless: the archive matches the manifest; the Dell's
   portal lockfile SHA-256 equals the manifest's; the Dell's `bun --version` (and `node --version` when the manifest holds one) equals
   the manifest's; the platform equals. With `--extract` it then extracts into `<portal>/node_modules` (refusing if that directory
   already exists and is non-empty unless `--replace` is given) and prints the file count extracted. LAST line
   `PORTAL-VERIFY archive=<ok|mismatch> lockfile=<ok|differs> bun=<ok|differs> node=<ok|differs|absent> platform=<ok|differs> extracted=<n|-> ok=<True|False>`.
4. `... typecheck --portal <dir>`: the read-back: runs the portal's own typecheck script as its `package.json` names it (read the
   `scripts` block; do not guess the command), bounded by a timeout argument, with no network, and prints its exit code and its last
   line. This is what each Dell runs after the extract.
5. `org/devices/test_kit_portal_tree.py`, on stand-ins and this box, no network: (1) `describe` on a small synthetic portal the test
   builds (a `package.json`, a text lockfile naming three packages, a `node_modules` holding them) reads `absent=0 ok=True`;
   (2) remove one package directory -> `absent=1 ok=False` and `pack` refuses; (3) `pack` then `verify` on the synthetic tree passes;
   (4) one byte of the archive flipped -> `archive=mismatch`; (5) the lockfile changed on the target -> `lockfile=differs`; (6) a
   manifest with another bun version -> `bun=differs`; (7) `--extract` into an empty target reproduces the file count; (8) THE REAL
   READ: `describe` on the base checkout's real portal, read-only, bounded to 100 seconds -- the case passes when the command
   completes and prints its last line, whatever `ok` reads, and the test prints that line; if it cannot finish inside the bound, the
   case records `REAL-READ-TIMEOUT` and you say so. No test packs the real tree (it is large) and no command contains a registry URL
   or the words `install`, `add` or `ci` as a package-manager verb (a test asserts it). LAST line
   `PORTAL-KIT-TEST cases=<k>/8 ok=<True|False>`.

**ACCEPTANCE, one criterion ADDED to the four above (which are unchanged and must still pass):**

<criterion id="CTk2-AC5" cell_refs="CT-k-2"><invocation>python org/devices/test_kit_portal_tree.py</invocation><expect>PORTAL-KIT-TEST cases=8/8 ok=True</expect></criterion>
`CTk2-AC5` -- the tree's description, pack, verification and extract behave on stand-ins, each refusal arm fires, and the real tree
was read. Report the real tree's `PORTAL-TREE` line in full: whether the laptop's tree matches the DEV lockfile is a FINDING, and if
it does not (`absent > 0` or `equals_dev=False`), say so plainly -- then the laptop's tree is not yet the thing to carry.

Write a NEW proof instance over the old one covering all five ids, validate it with
`python .tools/proof-of-spec-check.py <instance> CTk2-AC1,CTk2-AC2,CTk2-AC3,CTk2-AC4,CTk2-AC5`, and flip `<status>` back to `complete`
only when all five pass. In your report: the real tree's line, the bun and node versions here, the lockfile kind, the count of
platform-specific packages, the estimated archive size, the portal's typecheck command as its `package.json` names it, and the exact
commands a Dell and the laptop run for one delivery.

## AMENDMENT 3 (2.0.0_SA_COO~C, 2026-10-07 ~10:5xZ) -- REOPENED: bring the laptop's portal tree to the DEV lockfile, then cut the pack

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree and the earlier commits
are inherited state (merged to the trunk @e0a3cb15fc). Authority: `1.0.0_SA_CTO` msg 106162, verbatim: "the seat is the kit cell's
worker, under 2.0.0_SA_COO~C. `bun install` in portal/ on the laptop is the workspace's own documented portal command (CLAUDE.md,
Portal: \"bun install && bun run dev --port 5174\"); run with the frozen lockfile it changes no lockfile and brings six packages to the
versions DEV already locks. It is the laptop doing what the laptop already does, not a Dell reaching the registry. Two reads first,
each a stop if it fails: nothing is listening on port 5174 (a dev server reading that tree mid-install), and git -C portal status
shows no lockfile change afterwards. Then describe must read ok=True before the pack is cut. The Dells still fetch nothing: they
receive the pack over the tailnet." Gate limb: none graded this modification.

**THIS AMENDMENT LIFTS, FOR ONE COMMAND ONLY, two rules of the amendments above:** you MAY run exactly one install,
`bun install --frozen-lockfile`, and you MAY write to the base checkout's `portal/node_modules` through that command. Nothing else in
the base checkout is written by you; no other install, add or update command is run; no dev server is started.

**THE WORK, in this order; each numbered read is a STOP if it fails (report, file a row, leave the order `in_progress`):**

1. `<base>` is the first entry of `git worktree list --porcelain`; `<portal>` is `<base>/portal`. Record BEFORE: the portal's HEAD and
   branch; `git -C <portal> status --porcelain` in full (other seats' uncommitted portal work may be present: record it, do not touch
   it); the SHA-256 of `<portal>/bun.lock` and of `<portal>/package.json`; `bun --version`; and the `describe` last line (expected:
   `absent=6 ok=False`).
2. READ 1, a stop: nothing is listening on TCP port 5174 on this box. Measure it two independent ways (for example a Python socket
   connect to 127.0.0.1:5174 that is refused, and the operating system's listener table read for `:5174`) and print both. If
   anything listens, STOP: do not kill it.
3. Also a stop: no process is running from the portal tree that would hold its files open mid-install (look for a `bun` or `node`
   process whose command line names `<portal>`; print what you find). If one is found, STOP and report it.
4. Run ONCE, in `<portal>`: `bun install --frozen-lockfile`. Bound it (`timeout 600`), capture all output and its exit code. If it
   exits non-zero, or reports that the lockfile would change, STOP and report the output; do not retry with another flag.
5. READ 2, a stop: `git -C <portal> status --porcelain` AFTER equals the BEFORE listing for every tracked file (in particular
   `bun.lock` and `package.json` are not modified: compare their SHA-256 to step 1's), and the portal's HEAD is unchanged.
6. `python org/devices/kit_portal_tree.py describe` must read `absent=0 ok=True`. If it does not, STOP and report the differing
   packages.
7. Cut the pack: `python org/devices/kit_portal_tree.py pack --out <dir>` where `<dir>` is a NEW directory OUTSIDE every git tree,
   `C:/tmp/kit-portal-pack-<UTC date>` (derive the drive prefix; do not put it under the workspace). Then run
   `python org/devices/kit_portal_tree.py verify --from <dir> --portal <portal>` WITHOUT `--extract` on this same box as the
   self-check (the lockfile, bun, node and platform must all read ok). Record the archive's SHA-256, size and file count from the
   manifest. Do NOT send it anywhere and do NOT commit it.
8. Do NOT run the portal's typecheck in the base checkout (other seats work there); the read-back typecheck is each Dell's.
9. Write `KIT_PORTAL_PACK_RECORD.md` in your deliverables folder: the BEFORE and AFTER lines, both port reads, the install's exit
   code and last lines, the six packages and their versions before and after, the pack's path, SHA-256, size, file count, the bun
   and node versions, and the exact commands a Dell runs to verify, extract and typecheck.

**ACCEPTANCE, one criterion ADDED to the five above (which are unchanged and must still pass):**

<criterion id="CTk2-AC6" cell_refs="CT-k-2"><invocation>python org/devices/kit_portal_tree.py describe</invocation><expect>absent=0</expect></criterion>
`CTk2-AC6` -- after the frozen-lockfile install the laptop's tree is the DEV lockfile's tree. The same line must read `equals_dev=True`
and `ok=True`, stated in the proof row. (Run it with `AGENTBUS_DEVICE=laptop` exported if the tool asks for a device.)

Write a NEW proof instance over the old one covering all six ids, validate it with
`python .tools/proof-of-spec-check.py <instance> CTk2-AC1,CTk2-AC2,CTk2-AC3,CTk2-AC4,CTk2-AC5,CTk2-AC6`, and flip `<status>` back to
`complete` only when all six pass. If you stopped at a read, do NOT flip.

## AMENDMENT 4 (2.0.0_SA_COO~C, 2026-10-07 ~11:5xZ) -- REOPENED: the kit carries the Terraform binary beside the provider cache

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated and the earlier commits are inherited state
(merged to the trunk @786ca6d8e4). Authority: `1.0.0_SA_CTO` msg 106172, verbatim: "Kit: dell2 has no terraform binary (row
IRPT_BCKEND-S364). The kit cell carries the laptop's binary beside the provider cache, to both Dells, read back by terraform
version and one no-op plan." Gate limb: none graded this modification. The three kits above are done and stay; THE WORK below is
the whole of this amendment. THE NO-NETWORK RULE STANDS: nothing is downloaded; the binary carried is the one already on this box.

1. `org/devices/kit_terraform_providers.py` gains the binary:
   - `binary`: locates the Terraform binary this box's `safe-apply.sh` would run -- read `.tools/safe-apply.sh` for its resolution
     order (the `SAFE_APPLY_TERRAFORM` override, the sibling `.tools/terraform.exe`, then PATH) and resolve it the SAME way; print the
     path, the size, the SHA-256, and `terraform version -json` parsed (version, platform). If the three sources disagree (a sibling
     and a PATH binary of different versions), print both and say which the wrapper would run. LAST line
     `TF-BINARY found=<True|False> version=<v> platform=<os_arch> sha256=<12 hex> bytes=<b> source=<override|sibling|path> ok=<True|False>`.
   - `pack --out <dir>` now ALSO places the binary at `<dir>/bin/terraform.exe` (a copy, or a hard link on the same volume) and
     records it in `MANIFEST.json` (path, SHA-256, size, version, platform) beside the providers. `--no-binary` omits it.
   - `verify --from <dir>` checks the binary against the manifest like every other file, and with `--run-binary` executes
     `<dir>/bin/terraform.exe version -json` and compares the reported version and platform to the manifest's (a mismatch refuses).
     On success it prints, besides the CLI-config snippet, the one line that tells a Dell where to put the binary so that
     `.tools/safe-apply.sh` finds it WITHOUT a baked path: by the wrapper's own resolution order (the sibling location or PATH; say
     which the wrapper prefers on a box that has neither today) -- and a `--install-binary <target>` flag that copies it there and
     re-verifies the copy's SHA-256.
   - `readback --root <dir>`: the Dell's read-back, in two parts, each printed: (a) `terraform version` through the SAME resolution
     the wrapper uses; (b) "one no-op plan": `terraform -chdir=<root> init -input=false` with the mirror config, then
     `terraform -chdir=<root> plan -input=false -lock=false -detailed-exitcode`, reporting the exit code (0 = no changes; 2 = changes,
     which is NOT a failure of the kit but is reported loudly; 1 = error). It needs the Dell's own AWS identity and the state backend,
     so YOU DO NOT RUN PART (b) against a real root: the test runs it against a root with a LOCAL backend and no provider resources.
     LAST line `TF-READBACK version=<v> init=<ok|fail> plan_exit=<0|1|2> ok=<True|False>`.
2. `org/devices/test_kit_terraform_providers.py` gains four cases (ten in all): the binary is located by the wrapper's own order;
   `pack` includes it and `verify --run-binary` passes; one byte of the packed binary flipped -> `verify` refuses BEFORE running it
   (the test asserts the tampered file was never executed); `readback` on a temporary root with a local backend and only locals and
   outputs reads `init=ok plan_exit=0`. LAST line `TF-KIT-TEST cases=<k>/10 skipped=<s> ok=<True|False>`.
3. Cut the REAL provider-and-binary pack once, outside every git tree, to `C:/tmp/kit-terraform-pack-<UTC date>` (derive the drive
   prefix), with `--include-unlocked` as the earlier pass built it, run `verify --from <dir> --run-binary` on it as the self-check,
   and record the manifest's totals. Do not send it anywhere and do not commit it. Add its record to your deliverables folder as
   `KIT_TERRAFORM_PACK_RECORD.md`: path, total bytes, each provider and version, the binary's version and SHA-256, and the exact
   commands a Dell runs (verify, install the binary, write the CLI config, read back).

**ACCEPTANCE.** CTk2-AC4's expectation becomes `TF-KIT-TEST cases=10/10` (same invocation; the line must read `ok=True`). One
criterion is ADDED; the other five are unchanged and must still pass:

<criterion id="CTk2-AC7" cell_refs="CT-k-2"><invocation>python org/devices/kit_terraform_providers.py binary</invocation><expect>TF-BINARY found=True</expect></criterion>
`CTk2-AC7` -- the binary this box's apply wrapper runs is located, hashed and versioned. The same line must read `ok=True`.

Write a NEW proof instance over the old one covering all seven ids, validate it with
`python .tools/proof-of-spec-check.py <instance> CTk2-AC1,CTk2-AC2,CTk2-AC3,CTk2-AC4,CTk2-AC5,CTk2-AC6,CTk2-AC7`, and flip `<status>`
back to `complete` only when all seven pass.

## AMENDMENT 5 (2.0.0_SA_COO~C, 2026-10-07 ~12:3xZ) -- REOPENED: the bun egress disarm, measured against a loopback listener

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree and every earlier commit is
inherited state on the trunk. Row `NFRA_CTLPLN-S13` (ARMED, disarm owner the issuer). Authority: `1.0.0_SA_CTO` msg 106214, verbatim:
"cut one cell. Its control: point bun's registry at a loopback listener that logs requests. Positive arm, no disarm: the listener
logs a request. Each candidate (--no-install, a project bunfig, an environment variable): zero requests. Measure bun 1.3.9 on the
laptop and 1.4.2 on a Dell. The kit carries the form that passes." And msg 106220, verbatim: "(1) The script: on a box with no
registry redirect, the install mode refuses with a line naming link or none; the default becomes link. Its control: the same
loopback listener, zero requests from a provision. (2) The interim rule now also forbids bun install on all three boxes."
Gate limb: none graded this modification. The kits above are done and stay; THE WORK below is the whole of this amendment.

**THE HAZARD.** bun, run on a file whose import does not resolve from a `node_modules` tree, fetches the package from the public
registry without asking. Two such fetches happened on another machine; a user-level `bunfig.toml` with `[install] auto = "disable"`
was measured NOT to stop it there (bun 1.4.2). A fetch failure and a disabled install print the same error, so only a listener
that counts requests can tell them apart.

**THE ONE RULE THAT GOVERNS EVERYTHING YOU RUN: NO REQUEST MAY LEAVE THIS MACHINE.** The test that proves the disarm must not itself
be the egress. So EVERY bun process this amendment starts runs inside a harness with TWO independent redirects to loopback, and you
prove both BEFORE any arm that could fetch:
- **Redirect A, the registry:** bun's registry set to `http://127.0.0.1:<port>/` (a listener you start in Python's standard library
  on an ephemeral port, which logs method and path of every request and answers 404).
- **Redirect B, the proxy:** `HTTP_PROXY`, `HTTPS_PROXY`, `http_proxy`, `https_proxy` all set to a SECOND loopback listener that logs
  every request line (including `CONNECT host:443`) and answers 502, with `NO_PROXY`/`no_proxy` set to empty so even loopback goes
  through it if bun chooses. Whatever host bun tries, the request lands on one of your two listeners.
- **The package name** every probe imports is one that cannot exist: a scoped name with a random suffix generated per run
  (for example `@opal-no-such-scope-<16 hex>/probe`), so that even a leak would retrieve nothing.
- **Isolation:** each run uses a fresh temporary directory OUTSIDE every git tree and every `node_modules` ancestor, a temporary
  `BUN_INSTALL_CACHE_DIR`, and a temporary `HOME`/`USERPROFILE`/`XDG_CONFIG_HOME` so no user-level bunfig is read or written. You
  never write `~/.bunfig.toml`.
- **ORDER OF PROOF, and you stop at the first failure with a BLOCKING row and no further bun run:**
  (0) `bun --version` only (no script) -- with both listeners up; record any request (a version check that phones home is a finding).
  (1) THE PROXY PROOF: with Redirect B alone set and the registry left at its default, run the probe WITH the strongest disarm you
      have (`bun --no-install run probe.js`). Expect zero requests. This arm cannot prove the proxy works; it is only the safest
      first run.
  (2) THE REGISTRY-REDIRECT PROOF, the positive arm: Redirect A AND Redirect B both set, no disarm, the nonexistent package.
      Expect one or more requests ON A LOOPBACK LISTENER. If ZERO requests arrive on both listeners and bun reports anything other
      than a resolution error that names the loopback registry, you CANNOT tell where it went: STOP, file the BLOCKING row, run
      nothing further. If requests arrive only on the proxy listener naming the public registry host, Redirect A is ineffective in
      the form you set it: record that, and try the next form of Redirect A (an environment variable such as
      `BUN_CONFIG_REGISTRY` or `NPM_CONFIG_REGISTRY`; a project `bunfig.toml` `[install] registry = ...` beside the probe) -- the
      proxy is what kept it on the machine.
  Only after (2) shows the positive arm landing on loopback do you run the candidates.

1. `org/devices/kit_bun_no_egress.py`:
   - `measure`: runs the harness above, then each CANDIDATE disarm as its own arm, each from a fresh directory, each reported with
     the number of requests each listener logged and bun's exit code and first error line: (a) the command-line flag `--no-install`;
     (b) a PROJECT `bunfig.toml` beside the probe with `[install] auto = "disable"`; (c) the same setting in a user-level bunfig
     inside the temporary home (to reproduce the other machine's reading on this version); (d) each environment variable bun
     documents or its binary names for this (search the binary's strings and `bun --help` output for `auto`, `install` and
     `BUN_CONFIG_`; list what you found and tried); (e) the structural form: the probe file placed inside a directory that HAS a
     `node_modules` folder (empty) and a `package.json`. A candidate PASSES only with zero requests on both listeners AND the
     positive arm of the same run non-zero. Print one line per arm and LAST
     `BUN-NO-EGRESS bun=<version> positive_requests=<n> candidates=<k> passing=<p> leaked_public=<0|n> form=<the passing form the kit carries, or NONE> ok=<True|False>`
     (`ok=True` needs `positive_requests>0`, `leaked_public=0`, and at least one passing candidate). It writes its full result as
     JSON to a path given by `--out` (default: none). It is the SAME script a Dell runs for bun 1.4.2; it bakes no path and no
     version.
   - `wrap -- <bun args>`: runs bun with the passing form applied (and refuses, naming the reason, a bare `bun install`, `bun add`,
     `bun x`/`bunx`, `bun create` or `bun update` unless `--allow-registry <reason>` is given, which it prints loudly). This is the
     form the kit carries.
2. `org/devices/test_kit_bun_no_egress.py`: the listener logs a request made by Python itself (the listener works); `measure` on
   this machine reads `ok=True`; `wrap` refuses `install` and passes `--version`; a planted regression (the harness told to treat a
   candidate that DID make a request as passing) is caught. LAST line `BUN-KIT-TEST cases=<k>/<n> ok=<True|False>`.
3. `.tools/wk-provision.sh`, the CTO's addition: read it whole first. Its `--node-modules install` mode runs
   `bun install --frozen-lockfile` (near line 151), which is a registry path. Change: the DEFAULT mode becomes `link`; the `install`
   mode REFUSES, before running bun, unless a registry redirect is present in the environment the script can verify (a registry
   variable or project bunfig pointing at a non-public host), with one line naming `link` and `none` as the modes to use. Change
   nothing else in the script. `.tools/tests/test_wk_provision_no_registry.py`: with both listeners up and the harness environment,
   a provision in `install` mode on a scratch repository makes ZERO requests and exits non-zero with the refusal line; `link` and
   `none` are unaffected (or, where a full provision cannot run in a scratch repository, the test exercises the mode-selection
   function directly and says so). LAST line `WK-PROVISION-REGISTRY install_refused=<True|False> requests=<n> default=<mode> ok=<True|False>`.
   You do NOT run a real provision with `install`.
4. A record in your deliverables folder, `BUN_NO_EGRESS_RECORD.md`: every arm's line for this machine's bun version, the passing
   form, the exact commands another machine runs to measure its own version, and what stays unproven. State also, for row
   `NFRA_CTLPLN-S13`, what the earlier pass of this order fetched: the frozen-lockfile install run on this machine at about 10:55Z
   (ruled at the time; the same registry path) -- read `KIT_PORTAL_PACK_RECORD.md` in this folder on the trunk for the package count
   and say it. Do not re-run it.

**YOU RUN NO `bun install`, `bun add`, `bunx` OR `bun create` AT ALL**, in any directory, redirected or not. The interim rule forbids
it on this machine until this cell lands.

**ACCEPTANCE.** Two criteria are ADDED; the other seven are unchanged and must still pass:

<criterion id="CTk2-AC8" cell_refs="CT-k-2"><invocation>python org/devices/test_kit_bun_no_egress.py</invocation><expect>BUN-KIT-TEST cases=</expect></criterion>
<criterion id="CTk2-AC9" cell_refs="CT-k-2"><invocation>python .tools/tests/test_wk_provision_no_registry.py</invocation><expect>WK-PROVISION-REGISTRY install_refused=True requests=0</expect></criterion>
`CTk2-AC8` -- the same line must read `ok=True` with every case passing. `CTk2-AC9` -- the same line must read `ok=True`.

If `measure` finds NO passing candidate, that is a result, not a failure to hide: `wrap` then carries only the structural refusal,
AC8's line reads `ok=False`, you file a BLOCKING row with the arms, leave the order `in_progress`, and report.

Write a NEW proof instance over the old one covering all nine ids, validate it with
`python .tools/proof-of-spec-check.py <instance> CTk2-AC1,CTk2-AC2,CTk2-AC3,CTk2-AC4,CTk2-AC5,CTk2-AC6,CTk2-AC7,CTk2-AC8,CTk2-AC9`, and
flip `<status>` back to `complete` only when all nine pass.

## AMENDMENT 6 (2.0.0_SA_COO~C, 2026-10-07 ~14:0xZ) -- REOPENED: the Python kit against the regenerated requirements.txt, and which packages have a wheel for the Dells' Python

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree; every earlier commit is
inherited state on the trunk. Authority: `1.0.0_SA_CTO` msg 106278, verbatim: "that file is now the list the Python kit is built
against, in place of whatever list the cell derived itself. The Dells run Python 3.14 and the laptop 3.12, so a wheel set built
here does not fit there (the PyMuPDF case); the cell states per package whether a 3.14 win_amd64 wheel exists on the laptop
without a fetch, and lists the ones that do not as a file for me." The file: the repository root `requirements.txt` @bc10584676
(67 installable lines, regenerated from an import census on Andrew's word; record
`org/tier1_exec/3.0.0_SA_CVO/deliverables/ANDREW_DIRECT_20261007_133xZ_REQUIREMENTS_TXT_ALL_ACTUAL_DEPENDENCIES.md`; its own
caveat: a clean-start resolve is NOT verified). Gate limb: none graded this modification. `requirements.txt` is in the grant to be
READ; YOU DO NOT EDIT IT. THE NO-NETWORK RULE STANDS: no `pip install`, no `pip download`, no `pip index`, no `pip wheel` of a
remote package, no request to any package index. Every pip call you make carries `--no-index` or is one of `pip --version`,
`pip list`, `pip show`, `pip cache dir`, `pip cache list`, `pip inspect`, `pip config list` (which make no request).

1. `org/devices/kit_python_wheels.py`, three verbs:
   - `required`: parse the root `requirements.txt` (names, specifiers, markers, extras; a line it cannot parse is printed and
     counted, never skipped silently) and compare it with the list this cell derived itself (`org/devices/kit_python_required.json`,
     20 distributions): print the names only in one, only in the other, and in both. LAST line
     `PY-REQ lines=<n> parsed=<p> unparsed=<u> in_both=<b> only_requirements=<r> only_census=<c> ok=<True|False>`.
   - `wheels --python-tag cp314 --platform win_amd64`: for EACH requirement, state whether a wheel that Python 3.14 on 64-bit
     Windows can install exists ON THIS MACHINE WITHOUT A FETCH, and where. Sources to read, each counted: the pip HTTP and wheel
     caches (`pip cache dir`; the wheel cache holds locally built wheels by name; the HTTP cache holds downloaded files under
     hashed names whose bodies are zip archives with a `*.dist-info/WHEEL` member: identify a cached wheel by reading that member
     and `METADATA`, never by a file name alone); any wheel files already on disk in the kit's own earlier pack output, in
     `C:/tmp/kit-*`, in the user's Downloads folder and under the repository (search for `*.whl`; derive every path, bake none);
     and the installed distributions of every Python interpreter on this machine (`py -0p` lists them: an installed pure-Python
     distribution whose `WHEEL` file reads `Root-Is-Purelib: true` and tag `py3-none-any` (or `py2.py3-none-any`) can be re-packed
     into a wheel offline and fits 3.14; an installed distribution tagged `cp312-cp312-win_amd64` does NOT fit, and one tagged
     `cp3X-abi3-win_amd64` with X <= 14 does fit).
     Classify each requirement as exactly one of: `WHEEL-ON-DISK` (a file that fits, with its path and tags), `PURE-INSTALLED` (no
     file, but an installed pure-Python copy that can be re-packed offline; say at which version and whether that version
     satisfies the specifier), `ABI3-INSTALLED` (an installed stable-ABI build that fits), `NEEDS-FETCH` (compiled for another
     Python only, or absent), `UNPARSED`. A requirement whose marker excludes Python 3.14 or Windows is `NOT-APPLICABLE` with the
     marker printed. Compatibility is decided by the `packaging` library's tag logic if it is installed here
     (`packaging.tags`), computed for the TARGET (3.14, win_amd64), not for the running interpreter; if `packaging` is not
     installed, implement the three rules above and say so.
     It does NOT follow dependencies of the listed packages (the file is stated to be the full list; its caveat is a clean-start
     resolve is unverified): say that in the output, and, for each `WHEEL-ON-DISK` or installed copy, print the `Requires-Dist`
     names that are NOT themselves lines of `requirements.txt`, as a count and a list, so the gap is visible.
     Writes `org/devices/kit_python_wheels_cp314.json` (per requirement: name, specifier, class, evidence path or installed
     version, tags) and LAST line
     `PY-WHEELS target=cp314-win_amd64 requirements=<n> wheel_on_disk=<a> pure_installed=<b> abi3_installed=<c> needs_fetch=<d> not_applicable=<e> unparsed=<u> undeclared_deps=<k> ok=<True|False>`
     (`ok=True` when every requirement got exactly one class and `unparsed=0`).
   - `--from-file <json>` re-prints the last line from the saved file (the criterion's bounded form).
2. `org/devices/test_kit_python_wheels.py`: on synthetic fixtures in a temporary directory (tiny hand-made wheel archives and
   `dist-info` folders, no real package): a `py3-none-any` wheel fits; a `cp312-cp312-win_amd64` wheel does not; a
   `cp39-abi3-win_amd64` wheel fits; a `cp314-cp314-win_amd64` wheel fits; a `cp314-cp314-manylinux` wheel does not; a
   requirement with a marker excluding Windows is NOT-APPLICABLE; an unparseable line is counted. LAST line
   `PY-WHEELS-TEST cases=<k>/7 ok=<True|False>`.
3. THE FILE FOR THE CTO, in your deliverables folder: `PYTHON_WHEELS_NEEDING_A_FETCH_FOR_CP314.md` -- the `NEEDS-FETCH` list (name,
   specifier, why: compiled for 3.12 only, or absent), the `PURE-INSTALLED` list with any version that does not satisfy its
   specifier, the undeclared dependencies, PyMuPDF's line by name (it is the case that prompted this), which Python
   interpreters this machine holds, and what stays unread. Standard technical English; it is a decision document.

**ACCEPTANCE.** One criterion is ADDED; the other nine are unchanged and must still pass:

<criterion id="CTk2-AC10" cell_refs="CT-k-2"><invocation>python org/devices/kit_python_wheels.py wheels --from-file org/devices/kit_python_wheels_cp314.json</invocation><expect>PY-WHEELS target=cp314-win_amd64 requirements=</expect></criterion>
`CTk2-AC10` -- every requirement classified; the same line must read `ok=True`.

Write a NEW proof instance over the old one covering all ten ids, validate it with `python .tools/proof-of-spec-check.py <instance>
CTk2-AC1,CTk2-AC2,CTk2-AC3,CTk2-AC4,CTk2-AC5,CTk2-AC6,CTk2-AC7,CTk2-AC8,CTk2-AC9,CTk2-AC10`, and flip `<status>` back to `complete`
only when all ten pass.

## AMENDMENT 7 (2.0.0_SA_COO~C, 2026-10-07 ~15:1xZ) -- REOPENED: re-pack the 49 packages that fit Python 3.14 into wheels, offline, as the Python kit

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree; every earlier commit is
inherited state on the trunk (the classification merged @bd489b912b). Authority: `1.0.0_SA_CTO` msg 106317, verbatim: "(1) The 41
pure packages and the 8 that already fit, PyMuPDF among them, are re-packed offline and carried as the Python kit now. The Dell
proves them: pip install with no index from the kit folder, then one import each, read back; a package that fails there joins the
list below. (2) The 18 cp312-only requirements and the 12 unlisted compiled dependencies are NOT fetched today." Gate limb: none
graded this modification. THE NO-NETWORK RULE STANDS, as in AMENDMENT 6: no request to any index; allowed pip calls are the
read-only ones named there. YOU DO NOT `pip install` ANYTHING ON THIS MACHINE and you fetch nothing.

1. `org/devices/kit_python_repack.py`:
   - `repack --out <dir>`: for each requirement classed `PURE-INSTALLED` or `ABI3-INSTALLED` in
     `org/devices/kit_python_wheels_cp314.json` (49 expected: 41 + 8; re-derive the set from the file, do not type the names),
     rebuild a wheel from the INSTALLED copy with the standard library only: the files listed in that distribution's `RECORD`
     (paths under site-packages; a file outside it, such as a script in `Scripts/` or a `.data` entry, is placed under the
     wheel's `<name>-<version>.data/scripts/` or reported and the package marked `PARTIAL`), the `dist-info` directory as
     installed MINUS `INSTALLER`, `REQUESTED`, `direct_url.json` and `RECORD`, a regenerated `RECORD` (sha256, urlsafe-base64, no
     padding, sizes; the RECORD line for itself empty), and the wheel file named from the `WHEEL` file's own tags
     (`{name}-{version}-{python tag}-{abi tag}-{platform tag}.whl`, name and version normalised as the wheel specification
     states). Never include a `__pycache__` or `.pyc` file. A file listed in `RECORD` but missing on disk, or present with a
     different hash than `RECORD` states (a locally modified install), is REPORTED and the package marked `MODIFIED` and left OUT
     of the kit: a kit must not carry bytes no index ever published. Verify each built wheel by re-opening it: every `RECORD`
     hash matches, `WHEEL` and `METADATA` parse, and the tags fit the target (cp314, win_amd64) by the same tag logic the
     classifier uses.
     Writes `<dir>/MANIFEST.json` (per wheel: name, version, file name, sha256, bytes, tags, class, source interpreter version;
     the lists of packages left out and why; the target; the requirements file's commit) and `<dir>/requirements-kit.txt` (the
     exact `name==version` lines the kit satisfies, in the requirements file's order).
     LAST line `PY-REPACK target=cp314-win_amd64 selected=<n> built=<b> verified=<v> partial=<p> modified=<m> failed=<f> bytes=<total> ok=<True|False>`
     (`ok=True` when `built == verified` and `failed == 0`; `partial` and `modified` are reported, not hidden).
   - `verify --from <dir>`: checks every wheel against the manifest (sha256, size) and that the folder holds nothing the manifest
     does not list. It then prints the EXACT commands a Dell runs, which the tool also offers as verb `install-check`:
     `python -m pip install --no-index --no-deps --find-links <dir> -r <dir>/requirements-kit.txt --target <scratch>` into a
     scratch target directory first (so a failure changes nothing in the Dell's real environment), then one `import` of each
     distribution's top-level module (taken from the wheel's `top_level.txt` where present, otherwise from the first package
     directory in `RECORD`; import names differ from distribution names), run with that scratch directory first on the path, each
     import in its own subprocess with a 60-second bound, reporting per package `installed`, `imported` or the first error line.
     `--no-deps` is deliberate: the 73 unlisted dependencies are NOT in the kit, so an import that fails for a missing dependency
     is the expected finding for that package and is reported as `import_failed: missing <module>`, distinct from a wheel that
     will not install. LAST line of `install-check`
     `PY-KIT-INSTALL python=<version> wheels=<n> installed=<i> imported=<m> import_missing_dep=<d> failed=<f> ok=<True|False>`
     (`ok=True` when `installed == wheels`; the import counts are the finding).
     YOU DO NOT RUN `install-check` AGAINST A REAL TARGET HERE: this machine has no Python 3.14. The test runs it on synthetic
     wheels with this machine's interpreter.
2. `org/devices/test_kit_python_repack.py`, on synthetic distributions in a temporary site-packages (hand-made, tiny): a pure
   package re-packs and its wheel verifies; a file whose bytes differ from `RECORD` marks the package MODIFIED and leaves it out;
   a `.pyc` is never packed; the regenerated `RECORD` hashes match; `verify` refuses a wheel with one byte flipped and a stray
   file in the folder; `install-check` on two synthetic wheels with THIS interpreter (`--no-index`, a temporary target) installs
   both and imports both, and reports a third whose import needs an absent module as `import_missing_dep`. LAST line
   `PY-REPACK-TEST cases=<k>/<n> ok=<True|False>`.
3. Cut the REAL kit once, outside every git tree, to `C:/tmp/kit-python-pack-<UTC date as YYYYMMDD>` (derive the drive prefix),
   run `verify --from` on it as the self-check, and write `KIT_PYTHON_WHEELS_PACK_RECORD.md` in your deliverables folder: path,
   total bytes, the wheels built by class, every package left out and why (PARTIAL, MODIFIED, failed), PyMuPDF's wheel by name
   with its tags and size, the commands a Dell runs in order (verify, install-check into a scratch target, then the real install
   on the Dell's own decision), and what stays unproven (nothing was installed on a 3.14 interpreter here). Do not send the kit
   anywhere and do not commit it.

**ACCEPTANCE.** One criterion is ADDED; the other ten are unchanged and must still pass:

<criterion id="CTk2-AC11" cell_refs="CT-k-2"><invocation>python org/devices/test_kit_python_repack.py</invocation><expect>PY-REPACK-TEST cases=</expect></criterion>
`CTk2-AC11` -- the same line must read `ok=True` with every case passing. The real kit's `PY-REPACK` and `verify` lines go in the
proof row's evidence and in the record.

Write a NEW proof instance over the old one covering all eleven ids, validate it, and flip `<status>` back to `complete` only
when all eleven pass.

## AMENDMENT 8 (2.0.0_SA_COO~C, 2026-10-07 ~20:0xZ) -- REOPENED: the Python 3.12 kit -- the WHOLE dependency closure re-packed offline for the Dells' new Python

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree; every earlier commit is
inherited state on the trunk. What changed: Andrew admitted the Python 3.12 installer for the Dells (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_183xZ_TWELVE_ITEMS_ANSWERED_INSTALLER_PUSH_VENDOR_EGRESS_STORE_OUTLOOK_LAW_LINE_D2_HOLD_LIFTED.md`
item 2), and the CTO ruled (msgs 106375, 106537, 106549) that the Dells move to Python 3.12 so that "the kit re-pack[s] every
compiled package offline" and one version of everything runs on every box; "With 3.12 the batch is click plus site Z's Windows
file." The 3.14 kit (49 wheels, AMENDMENT 7) stays as built. Measured by the issuer on the trunk with cell CT-e-1's tool, no index
asked: `INTAKE-CLOSURE target=cp312-win_amd64 lines=67 closure=162 dependencies_added=95 pure=114 fits=47 needs_fetch=1 unknown_not_installed=0 specifier_conflicts=2 fixed_point=True ok=True`
(the one that needs a file is `click`, an editable install here with no wheel metadata; the two conflicts are `botocore` 1.43.0
against `awscli`'s and `boto3`'s specifiers). Gate limb: none graded this modification. THE NO-NETWORK RULE STANDS exactly as in
AMENDMENTS 6 and 7: no request to any index; you install nothing on this machine outside the test's synthetic wheels.

1. Save the closure for the new target: `python org/devices/intake/intake_closure.py closure --target cp312-win_amd64 --out org/devices/intake/closure_cp312_win_amd64.json`
   and confirm its last line equals the issuer's above (report any difference). `intake_closure.py` is in the grant ONLY so you
   can fix a defect you hit in it; change nothing there otherwise.
2. `org/devices/kit_python_repack.py` `repack` gains `--closure <json>`: the set to re-pack is every member of that closure
   whose class says it can be rebuilt from the installed copy for the closure's target (the pure ones and the ones that fit),
   in place of the 3.14 classification file; `--target` is read from the closure file and every built wheel's tags are checked
   to fit THAT target. Everything else about `repack` is as AMENDMENT 7 built it: files checked against the copy's own `RECORD`
   before packing; a locally modified copy is `MODIFIED` and left out with its paths; launchers regenerated from entry points
   are not packed; reproducible bytes; the manifest and `requirements-kit.txt` (now the closure's exact `name==version` lines,
   the 67 requirement lines first in the file's order, then the dependencies sorted by name, with a comment line saying which
   are which).
   The manifest ALSO lists what the kit does NOT carry and why: `click` (no wheel metadata here: it needs the checked route),
   any `MODIFIED` or failed package, and the two specifier conflicts by name with both versions, so the receiver knows the kit
   is not a consistent resolution for `awscli` and `boto3` (it carries what this machine runs).
3. `install-check` gains `--with-deps-from-kit`: one install of the WHOLE kit into ONE scratch target
   (`pip install --no-index --no-deps --target <scratch>/all <every wheel>`), then one import per top-level module of each of
   the 67 REQUIREMENT lines with that one target on the path: with the closure present, a missing dependency should no longer
   occur, and any that does is named. LAST line
   `PY-KIT-INSTALL-ALL python=<version> wheels=<n> installed=<i> requirement_lines=<r> imported=<m> import_missing_dep=<d> failed=<f> ok=<True|False>`.
   THIS machine runs Python 3.12, the kit's target: so, unlike the 3.14 kit, you CAN prove this kit here. Run
   `install-check --with-deps-from-kit` on the real kit into a temporary scratch target (never `--user`, never this machine's
   real environment), and report every requirement line that does not import with its first error line. A package that
   imports here only because this machine's own site-packages is on the path would be a false pass: the import subprocess runs
   isolated (`-I`) with ONLY the scratch target and the standard library on its path; assert it in the test.
4. Cut the REAL 3.12 kit once, outside every git tree, to `C:/tmp/kit-python312-pack-<UTC date as YYYYMMDD>` (derive the drive
   prefix; check free disk first: `torch` and other compiled packages are large, expect several gigabytes; stop with a report
   if under 10 gigabytes would remain), run `verify` and the whole-kit install check on it, and write
   `KIT_PYTHON312_PACK_RECORD.md` in your deliverables folder: path, total bytes, wheel count by class, the ten largest wheels,
   everything left out and why, the whole-kit install check's last line and every requirement line that failed to import,
   the commands a Dell runs in order once its Python 3.12 is installed, and what stays unproven (this machine is not a Dell;
   a Dell's own run is the proof there). Do not send the kit anywhere and do not commit it.

**ACCEPTANCE.** One criterion is ADDED; the other eleven are unchanged and must still pass (`CTk2-AC11`'s case count grows):

<criterion id="CTk2-AC12" cell_refs="CT-k-2"><invocation>python org/devices/intake/intake_closure.py closure --from-file org/devices/intake/closure_cp312_win_amd64.json</invocation><expect>INTAKE-CLOSURE target=cp312-win_amd64 lines=67</expect></criterion>
`CTk2-AC12` -- the closure for the new target is saved; the same line must read `fixed_point=True ok=True`. The real kit's
`PY-REPACK`, `verify` and `PY-KIT-INSTALL-ALL` lines go in this row's evidence and in the record.

Write a NEW proof instance over the old one covering all twelve ids, validate it, and flip `<status>` back to `complete` only
when all twelve pass.

## AMENDMENT 9 (2.0.0_SA_COO~C, 2026-10-08 ~22:5xZ) -- REOPENED, PRIORITY (BLOCKING for dell2): the Terraform provider kit gains the versions the roots LOCK, and hashicorp/local

Authority: dell2 `0.7.0_AE_CloudOps~DELL2` msg 1841, BLOCKING row `NFRA_CTLPLN-D2-S1` @c81c5e2283 (origin box/dell2), relay
0.0.0_AB_MSTR msg 107444: "The dell2 terraform kit passes the read-back of ruling 385 but NOT its other clause, 'pinned to the versions
the roots lock'. terraform.rc excludes the direct registry, so a provider the mirror lacks has no install path. Lock census,
DENOMINATOR 40: unsatisfiable on astn-pipeline, globgrph, market-overview (archive 2.8.0/2.7.1), opal-gateway (also external 2.4.2),
seeking-alpha (also a non-Windows aws 5.100.0 h1). Sixth: investor-reporting/core needs hashicorp/local, absent at any version. Both
remedies need the registry egress dell2 forbids, so both are laptop-side." Gate limb: none graded this modification. YOU APPLY
NOTHING; the only network act allowed is the Terraform registry download of the named providers on the laptop.

1. **MEASURE FIRST.** `python org/devices/kit_terraform_providers.py required` over every root at HEAD: print the denominator (dell2
   counted 40 locks) and, for the six roots named, each locked `namespace/type@version` and its `h1:`/`zh:` hashes for
   `windows_amd64`. `located` on the laptop: which of those are already in a local plugin cache. List exactly what is missing.
2. **FETCH, laptop only.** For each missing `namespace/type@version` (at least `hashicorp/archive` 2.8.0 and 2.7.1, `hashicorp/external`
   2.4.2, `hashicorp/aws` 5.100.0 with its `windows_amd64` package, and `hashicorp/local` at the version `investor-reporting/core`'s
   lock names -- if that root has no lock entry for it, take its `required_providers` constraint and STOP to report before
   choosing a version), run `terraform providers mirror -platform=windows_amd64 <scratch dir>` from a scratch root that declares
   exactly those versions. Verify each package's hash against the root lock files' hashes; a mismatch is a STOP.
3. **PACK.** Add them to the kit with `kit_terraform_providers.py pack --only <ns/type@ver> ...` in the same form and location as the
   pack AMENDMENT 1's pass made (read it first), then `verify --from <pack>`. Print the pack's manifest lines for the added providers.
4. **PROVE OFFLINE.** For each of the six roots, `kit_terraform_providers.py readback --root <root> --from <pack>` with the direct
   registry excluded (as dell2's terraform.rc does): every one must init. Print one line per root.
5. **DELIVERY.** Do NOT send anything off the laptop. Report the pack path and its manifest; the issuer routes it to dell2 by the
   intake path the kit already uses.

**ACCEPTANCE.** A new criterion `CTk2-AC13`: `python org/devices/kit_terraform_providers.py readback --root infra/aws/terraform/investor-reporting/core --from <pack>`
expecting `ok=True` (print the exact pack path in the proof row). The earlier criteria's expectations stand. Rewrite the proof
instance from your runs, validate, flip to `complete`.

**AMENDMENT 9, criterion element (issuer, ~23:4xZ):** the readback runs OFFLINE (`--init-only`, no backend), because the bare form inits the S3 backend and plans, which these bounds forbid (row S9102).

<criterion id="CTk2-AC13" cell_refs="CT-k-2"><invocation>python org/devices/kit_terraform_providers.py readback --root infra/aws/terraform/investor-reporting/core --from C:/tmp/kit-providers-20261008-k9/pack --init-only</invocation><expect>TF-READBACK version=1.15.8 init=ok</expect></criterion>

<expected_criteria>CTk2-AC1,CTk2-AC2,CTk2-AC3,CTk2-AC4,CTk2-AC5,CTk2-AC6,CTk2-AC7,CTk2-AC8,CTk2-AC9,CTk2-AC10,CTk2-AC11,CTk2-AC12,CTk2-AC13</expected_criteria>
(This `<expected_criteria>` line replaces every earlier one.)

## AMENDMENT 10 (2.0.0_SA_COO~C, 2026-10-09 ~01:3xZ) -- REOPENED, SHORT: a pinned Windows Python 3.12 set for dell2 -- pandas 2.2.3, numpy 1.26.4, pyarrow 14.0.2

dell2 2.0.0_SA_COO~D2 msg 2093 (relay 0.0.0_AB_MSTR msg 107593), per 1.0.0_SA_CTO~DELL2 ADDENDUM 1 @78928255f6: "a Windows Python 3.12 env
with pandas 2.2.3, numpy 1.26.4 and pyarrow 14.0.2, matching the served layer irpt-performance-native-layer:1 ... Please send the kit by
Taildrop or as a pinned requirements file." Basis: dell2's measured refusal DB-b-64 @9e9b3c49f2 (its Python 3.12 has pandas 2.3.3). Gate
limb: none graded this modification. The ONLY network act allowed is downloading these wheels and their dependencies from PyPI on this laptop.

1. **RESOLVE**: the dependency closure of exactly `pandas==2.2.3`, `numpy==1.26.4`, `pyarrow==14.0.2` for `cp312-win_amd64`, with
   the kit's own tooling (`org/devices/kit_python_wheels.py` / `org/devices/intake/intake_closure.py`, as AMENDMENTS 6-8 used them).
   Print every package and version in the closure (expected small: python-dateutil, pytz, tzdata, six). Wheels only, no sdists; a
   package with no cp312 win_amd64 wheel is a STOP, named.
2. **FETCH** into `C:/tmp/kit-py312-dashbd-20261009/wheels/` (OUTSIDE git): `pip download --only-binary=:all: --platform win_amd64
   --python-version 3.12 --implementation cp --abi cp312 --no-deps <each pinned spec>` per closure line. Record each wheel's sha256.
3. **PIN FILE**: write `requirements-dashbd-py312.txt` beside the wheels with `name==version --hash=sha256:...` for every closure line.
4. **PROVE OFFLINE**: in a fresh scratch venv of this laptop's Python 3.12, `pip install --no-index --find-links <wheels> --require-hashes
   -r <pin file>` and `python -c "import pandas, numpy, pyarrow; print(pandas.__version__, numpy.__version__, pyarrow.__version__)"` ->
   `2.2.3 1.26.4 14.0.2`. Delete the scratch venv after.
5. **PACK**: one zip `C:/tmp/kit-py312-dashbd-20261009.zip` of the wheels and the pin file; print its size and sha256. Commit only a
   manifest (names, versions, sha256) in the deliverables folder; never a wheel.

**ACCEPTANCE.** A new criterion `CTk2-AC14`: the offline install of step 4 printing `2.2.3 1.26.4 14.0.2`. The earlier criteria stand. Rewrite
the proof instance, validate, flip to `complete`.

<criterion id="CTk2-AC14" cell_refs="CT-k-2"><invocation>python -c "import json;print(json.load(open('org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~13/KIT_PY312_DASHBD_MANIFEST.json'))['offline_import'])"</invocation><expect>2.2.3 1.26.4 14.0.2</expect></criterion>

<expected_criteria>CTk2-AC1,CTk2-AC2,CTk2-AC3,CTk2-AC4,CTk2-AC5,CTk2-AC6,CTk2-AC7,CTk2-AC8,CTk2-AC9,CTk2-AC10,CTk2-AC11,CTk2-AC12,CTk2-AC13,CTk2-AC14</expected_criteria>
(This `<expected_criteria>` line replaces every earlier one.)
