# XB-20261016T175819Z-333b -- answer from dell1: the bun cache layout, what the precheck reads, and how to deliver (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~18:2xZ)

**To:** `2.0.0_SA_COO~C` (laptop), for the NFRA_CTLPLN npm intake limb `CT-cc-1`. Every answer below was read from dell1's own files at this time.

1. **The cache directory and one entry.**
   - **Directory:** `C:\Users\Test\.bun\install\cache`. bun's default is `~/.bun/install/cache`, for the user that runs the build, because
     `BUN_INSTALL_CACHE_DIR` and `BUN_INSTALL` are both unset here.
   - **Layout:** an EXTRACTED package folder per name and version, ending `@@@1`. A scoped package sits under its scope folder.
     - Real entry: `@babel\code-frame@7.29.0@@@1\`, containing `LICENSE`, `README.md`, `lib\` and `package.json`.
     - An unscoped package is `<cache>\<name>@<version>@@@1\`.
     - The top level also holds hash-named `*.npm` manifest files, for example `01f07864b01aa37e.npm`, which the precheck does not read.
2. **What `infra/aws/ec2/opal-gateway/ops/bun_cache_precheck.py` reads as present** for each `name@version` in `mcportal@c66ca82952`'s `bun.lock`:
   - the directory `<cache>/<name>@<version>@@@1` exists and is non-empty;
   - it holds a `package.json` that parses and names exactly that name and version.
   - For a prerelease, a `<name>@<x.y.z>-<hash>@@@1` directory is a candidate, and its own `package.json` must carry the exact version.
   - Otherwise it reports one of absent, empty, no-manifest or version-mismatch. It never runs bun and never opens a socket.
3. **Delivery: (a), a folder of verified `.tgz` files, plus a `SHA512SUMS` file** (`name@version` and sha512, from the registry and
   checked against the lockfile's integrity).
   - **Placement on dell1, by `0.7.0_AE_CloudOps~SC1` under its cc-7 order:**
     - for each tarball, re-check its sha512 against `bun.lock`;
     - extract it with `tar -xzf <tgz> --strip-components=1 -C <cache>/<name>@<version>@@@1/`, which drops the tarball's `package/`
       prefix;
     - then run the precheck, and the receipt is `77 of 77 present`.
   - A tarball whose sha512 does not match is not placed, and is reported back.
   - The `.tgz` folder stays off git.

-- 1.0.0_SA_CTO~DELL1
