# STITCH HOOK RETIRED -- pointer

The local post-commit stitch publisher is retired (NFRA_CLDGRPH S29 @`a46abe413a`, R16): the keys
`s3://opal-313476888478-globgrph/stitch/*` have ONE writer, the cloud producer `opal-stitch-produce`.
The record is `.tools/git-hooks/stitch-refresh-post-commit.TOMBSTONE.md`.

This file exists for one further reason and says so: it is the in-grant path under `org/modules/graph/`
that MATCHES the retired hook's filter regex, so committing it is the 120-second silence test of
TO-CG-F-9 / F9-AC4 -- before S29 this commit would have published the stitch keys from this laptop.

## Why this file was committed twice

The first filter commit (`00ec6d1d96`, 2026-09-09T19:50:38Z) landed four minutes after this laptop's
hook had ALREADY overwritten the cloud marker one last time: at 19:45:44Z the issuer's own commit
`6de9b76d93` fired the still-installed hook and published `producer: stitch-local` (row
`NFRA_CLDGRPH-W5-S4`; the device act removed the hook pair 46 seconds later, at 19:46:3xZ). Both keys
were therefore already moved when that first silence run compared them against the pre-order baseline,
and it read `0 of 2` -- a true statement about the keys and a false one about the commit.

The issuer re-asserted the cloud producer with an ad-hoc `opal-stitch-produce` build (marker
`built_at 2026-09-09T19:55:00Z`, `producer: stitch-codebuild`, 29,267 nodes). This second commit of
this file is the silence test re-run on a settled key, against a baseline read taken immediately
before it. The first run's transcript is kept verbatim at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~5/f9_silence_run1.txt`.
