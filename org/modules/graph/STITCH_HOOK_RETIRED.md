# STITCH HOOK RETIRED -- pointer

The local post-commit stitch publisher is retired (NFRA_CLDGRPH S29 @`a46abe413a`, R16): the keys
`s3://opal-313476888478-globgrph/stitch/*` have ONE writer, the cloud producer `opal-stitch-produce`.
The record is `.tools/git-hooks/stitch-refresh-post-commit.TOMBSTONE.md`.

This file exists for one further reason and says so: it is the in-grant path under `org/modules/graph/`
that MATCHES the retired hook's filter regex, so committing it is the 120-second silence test of
TO-CG-F-9 / F9-AC4 -- before S29 this commit would have published the stitch keys from this laptop.
