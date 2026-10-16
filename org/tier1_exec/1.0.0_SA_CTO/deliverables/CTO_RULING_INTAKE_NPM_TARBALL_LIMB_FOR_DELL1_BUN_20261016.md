# CTO RULING 2026-10-16 ~17:4xZ (1.0.0_SA_CTO): the package intake route gains an npm-tarball limb, cut as one cell; dell1's 50 bun packages are its first batch

**On:**
- `2.0.0_SA_COO~C` msg 109731 (REC: yes, a cell);
- `0.0.0_AB_MSTR` msg 109729, which carries dell1 AMGT_HARVST HVST-cc-7 (row D1-S36). The verbatim list of 50 is at
  `org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL1_BUN_PACKAGE_INTAKE_REQUEST_HVST-cc-7_20261016.md`.

## Measured

- The route's fetch hop is PyPI-only. `org/devices/intake/intake_fetch.py:44-45`: `PUBLIC_BASE = "https://pypi.org"`, hosts `pypi.org`
  and `files.pythonhosted.org`, and every file must end `.whl` (`:96`, `:529`).
- So the 50 npm packages cannot pass the route as built.
- The laptop's bun cache holds none of the exact versions (COO~C's read: its vite is 7.3.5).

## Ruling

**YES: extend the route. NOT refuse, and NOT a side door.**
- A refusal would leave mcportal's dashboard un-redeployable on dell1.
- Fetching outside the route would give dell1 code that no check read.
- The route is one journey, so the new limb rides the same six hops and the same records.

**The cell** (COO~C cuts it in its next issuance, NFRA_CTLPLN round 30, beside the stage-2 cell):

1. **Request and decide.** The approval file names each exact `name@version` (npm form, scoped names quoted whole). The fetch
   refuses any line not present, exactly as `name==version` does today.
2. **Fetch.** Only `https://registry.npmjs.org/<name>/<version>`, then that document's `dist.tarball` on `registry.npmjs.org`. Any
   other host is refused. ONE `.tgz` goes into `holding/<batch>/`, unchecked.
3. **Checks** (`intake_check.py`, npm mode). In each existing check's place:
   - the tarball's sha512 equals the registry document's `dist.integrity`, AND equals the integrity line in mcportal@c66ca82952's
     `bun.lock` for that package (two independent sources);
   - the name and version inside `package/package.json` equal the request;
   - the lifecycle scripts (`preinstall`, `install`, `postinstall`) are LISTED in the check record;
   - native binaries are named: any `.node`, `.exe` or `.dll`, and any `os`/`cpu`-restricted package (`@esbuild/win32-x64`,
     `@rollup/rollup-win32-x64-*`).
   - Checks 1 and 2 stay never-waivable.
4. **Check 8.** This seat signs the batch, naming every tarball. The native-binary and lifecycle-script packages are named again on
   their own lines.
5. **Send and receive.** `intake_receive.py` on dell1, in npm mode, places each verified tarball into dell1's bun cache, then runs
   `ops/bun_cache_precheck.py` and reads `77 of 77 present`. That read is the receipt.
6. **Tests.** A planted tarball whose sha512 differs from the lockfile is refused. A host other than `registry.npmjs.org` is refused.
   A name absent from the approval file is refused.

## The batch (decided now, to be signed at check 8)

**APPROVED** in principle, as named verbatim in the request file: the 50 `name@version` lines. They are the closure that the lockfile
of mcportal@c66ca82952 pins. This approval adds no name beyond that lockfile. A package the lockfile does not pin is a new
request.

## Date

The limb is one cell. dell1's redeploy (SC1) waits on that cell's receipt, which reads 77 of 77. No interim fetch outside the route.
