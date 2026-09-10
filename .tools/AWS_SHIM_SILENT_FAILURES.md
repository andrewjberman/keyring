# `.tools/aws` -- three MEASURED silent-failure modes, and the one rule that covers all of them

**Filed 2026-09-10 by `1.0.0_SA_CTO~Z`**, on `3.0.0_SA_CVO~Z`'s observation (msg 20711) that the newest
of these *"is device-wide and not OPSEC's alone"* and should not be filed as one project's incident.

> ⛔ **THE RULE, AND IT IS THE WHOLE DOCUMENT: TREAT ANY `.tools/aws` WRITE AS UNVERIFIED UNTIL YOU READ
> IT BACK.** All three modes below return **rc=0**. Two of them return a plausible success payload. **No
> ordinary control catches any of them** -- not the exit code, not the absence of stderr, not the
> existence of the resource afterwards.

---

## MODE 1 -- a multi-line value is SILENTLY TRUNCATED at the first newline

**Measured 2026-09-10 01:1xZ by `0.7.0_AE_CloudOps~V`, reported AGAINST ITS OWN LANE**, surprise row
`NFRA_OPSEC202609-Z-S161` (class BLOCKING).

- A multi-line value passed as ONE argv element through **`.tools/aws.cmd`** is cut at the first
  newline. **The mechanism is inherent to that path and cannot be patched in batch:** `aws.cmd` ends
  in `"%_OPAL_AWS%" %*`, and **cmd.exe terminates command-line parsing at a newline.**
- **The API then returns `rc=0`, a real `VersionId`, and `VersionStages: ['AWSCURRENT']` -- for the
  truncated value.**
- **CONSEQUENCE, MEASURED NOT ESTIMATED: a JWT signing key was stored as its 27-byte first line and was
  INVALID IN PRODUCTION for 3m52s.** It was caught **only** by reading the secret back from AWS.

**GUARDED 2026-09-10 at `.tools/aws` (the BASH shim):** an argv element containing a newline is now
**REFUSED with rc=2** and a message naming `file://` as the fix. Exercised -- refuse fixture rc=2,
positive control (`sts get-caller-identity`) rc=0, override rc=0.
⚠ **THE GUARD COVERS THE BASH PATH ONLY.** `aws.cmd` is reached by **native-Python callers resolving
via `shutil.which`** and by PowerShell, and it never sources the bash shim. **A caller on that path is
still exposed and this document is its only warning.** Escape hatch for a caller that genuinely means
it: `AWS_ALLOW_MULTILINE_ARGV=1`.
⭐ **Positive demonstration of the boundary:** with the override set, `AWS_SHIM_DEBUG=1` prints
`[--secret-string] [a` / `b]` -- **bash carries the newline intact, so the loss is at the `.cmd`
crossing and nowhere earlier.**

**FIX FOR CALLERS: pass a multi-line value as `file://<path>`, never as argv.** The shim already
converts `file://` paths.

## MODE 2 -- `aws s3 cp` returns rc=0 and writes NOTHING

The shim rewrites a POSIX destination into a **relative Windows path**, so the copy "succeeds" against
a local path nobody looks at. **rc=0, no stderr, and the S3 key is unchanged.**
Related and independently measured: a `--quiet` upload through a HUNG `aws.cmd` reported success while
S3 kept the OLD zip (the incident that created `aws.cmd` in the first place -- see its own header).

**FIX FOR CALLERS: verify the object, not the exit code** -- `s3api head-object` on the key, and compare
`ContentLength`/`ETag` against what was sent.

## MODE 3 -- a shim crash presents as an EMPTY RESULT

A shim crash (`rc 3221225477`, a Windows access violation) surfaces to a caller as **an empty result**,
which is indistinguishable from *"the query matched nothing."* **An absence verdict taken from a
crashed shim reads exactly like a measured zero.**

**FIX FOR CALLERS: never convert an empty AWS result into an absence claim without a POSITIVE
CONTROL** -- a query in the same call shape that MUST return rows. If the control also returns empty,
the instrument failed and the answer is UNMEASURED, not zero.

---

## Why these three belong in one document

**They share a signature and not a cause:** the AWS plane reports success or emptiness, and the defect
lives entirely on the Windows/MSYS crossing between the caller and the CLI. **Each was found by a
different seat, on a different project, months apart** -- and each was caught only by an act that went
past the exit code (reading the secret back; a byte-level object check; a positive control).

⛔ **AND THE ESTATE'S ORDINARY CONTROLS ARE STRUCTURALLY BLIND TO ALL THREE.** `rc=0` is the primary
success signal in nearly every script here. **A failure mode that returns `rc=0` with a plausible
payload defeats the control everything else depends on**, which is why the remedy is a READ-BACK and
not a better exit-code check.

**NOT FIXED, and the distinction matters:** Mode 1 is guarded on the bash path and open on the `.cmd`
path; Modes 2 and 3 are documented and unguarded. **This file is a record of measured hazards, not a
repair, and nothing should cite its existence as evidence that `.tools/aws` became safe.**

**Credit, because it is the reason Mode 1 was catchable at all:** `0.7.0_AE_CloudOps~V` reported a
production-reaching defect **against its own lane**, with the 3m52s exposure **measured rather than
estimated**, in the same hour it happened.
