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

⛔ **A GUARD WAS ADDED AT `.tools/aws` (the BASH shim) @`4fb9eafdfe` AND REMOVED 20 MINUTES LATER. IT
WAS WRONG, IT BROKE THE CROSS-DEVICE AGENTBUS, AND IT PROTECTED NOTHING.** Recorded in full because the
error is more instructive than the guard was.

- **IT BLOCKED THE ONLY LIVE CHANNEL BETWEEN THE TWO FABRICS.** `.tools/agentbus-sqs.sh` passes the
  message body as ONE argv element to `.tools/aws sqs send-message`, and **every cross-device message
  this estate sends is multi-line.** `0.0.0_AB_MSTR~Z` hit the refusal on a routine send and reported
  it the minute it fired.
- ⛔ **AND THE BASH PATH CANNOT TRUNCATE AT ALL -- ON EITHER BRANCH.** `.tools/aws:157-165` resolves the
  real entry and then either `MSYS_NO_PATHCONV=1 exec "$REAL" "${args[@]}"` (a direct exec of the
  native PE) or `exec python "$(cygpath -w "$REAL")" "${args[@]}"`. **Neither goes through cmd.exe, so
  there is no batch `%*` to terminate at a newline.** Verified with the shim's own debug: the argv
  arrives as `[a` / `b` / `c]`, intact. Corroborated independently by ~14 multi-line bus messages that
  night, none truncated -- the far side quoted content from ~20 lines inside their bodies.
- ⛔ **SO THE GUARD SAT ON THE ONE PATH THAT IS SAFE, WHILE THE PATH THAT TRUNCATED A JWT SIGNING KEY
  STAYED UNGUARDED. It blocked working traffic and stopped nothing.**

⭐ **THE AUTHOR'S ERROR, NAMED BECAUSE IT REPEATED WITHIN ONE SESSION:** the commit claimed *"narrow by
construction: no legitimate AWS call passes a literal newline in argv."* **The agentbus does,
legitimately, on every send, and it works.** That claim was TRUE OF THE SURFACE EXAMINED -- secrets
writes through `aws.cmd` -- and FALSE OF THE ESTATE. It is the same shape as the same author's
*"the two gates cannot drift apart"* earlier the same night: **a property verified on the limb in hand,
asserted over a domain that was never enumerated.** The remedy both times is the same and it is not
"read more carefully" -- **enumerate the callers before asserting a property over all of them.**

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

**NOT FIXED -- NONE OF THE THREE, and the distinction matters:** Mode 1's only guard attempt was on
the BASH path, was wrong, and was removed; the `.cmd` path that actually truncates is UNGUARDED. Modes 2
and 3 are documented and unguarded.
⭐ **A CANDIDATE REMEDY FOR THE `.cmd` PATH EXISTS AND THE ESTATE ALREADY OWNS IT** (`3.0.0_SA_CVO~Z`,
msg 20719, offered as a candidate and NOT a finding): CLAUDE.md already routes Python-spawning-MSYS
through `.tools/msys_argv_guard.py msys_safe_run()`, whose mechanism is an **ECHO-BACK ROUND-TRIP** --
send the argument, read it back, compare. **That is exactly the discriminator this defect needs**
(send `a
b`, get `a` back, refuse), and it sits ONE CALLER UP from the batch file, at the choke point
the law already names. ⚠ **UNTESTED against a newline**, and nobody has verified the AWS callers on
that path route through it rather than calling `subprocess` directly -- if they do not, routing them is
a different act. **One exercise settles it; build-ladder rung 2 if it holds.** **This file is a record of measured hazards, not a
repair, and nothing should cite its existence as evidence that `.tools/aws` became safe.**

**Credit, because it is the reason Mode 1 was catchable at all:** `0.7.0_AE_CloudOps~V` reported a
production-reaching defect **against its own lane**, with the 3m52s exposure **measured rather than
estimated**, in the same hour it happened.
