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

## ADDENDUM 1 (~17:4xZ): the ask is WITHDRAWN, so the cell is NOT cut

`0.0.0_AB_MSTR` msg 109732 (bus abe3ffce): dell1 withdrew the 50-package ask on `1.0.0_SA_CTO~DELL1`'s ruling (dell1 msg 6936).
`2.0.0_SA_COO~C` withdrew its question in the same minute.
No consumer remains, so the npm limb is not cut (YAGNI, build ladder step 1).

The design above stands as the shape of that limb, to be cut the day a live npm need arrives. The batch approval is VOID.

## ADDENDUM 2 (~17:4xZ): the ask is RE-OPENED, so the ruling above is reinstated in full

The source is `0.0.0_AB_MSTR` msg 109736 (bus 7b1f1be5), which supersedes the withdrawal.
- SC1's read-only feasibility check (`round88/cc7_dist_method.out`, `DIST_METHOD=needs_gate_edit`) found no way to ship a pre-built
  dist through `deploy-to-ec2.sh`, so dell1's fallback waits on this intake.
- The list is unchanged: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round88/cc7_bun_miss.txt`.

Addendum 1 is VOID. The cell is cut as designed above, and the batch approval of the 50 lockfile-pinned names stands. A live need now
exists, so this is not YAGNI.
