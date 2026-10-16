# Package intake -- the route, its tools and its records

The route in six hops. Records are JSON, ASCII, one file per event, under `org/devices/intake/records/<batch>/`.

1. **Requested** -- a seat names `name==version` (and the platform tag). Record: the request in the batch approval file.
2. **Assessed** -- the line is read against the brief. Record: the assessment, in the issuing seat's deliverables.
3. **Decided** -- the CTO signs the batch approval file naming each exact `name==version`. Record: that signed file.
4. **Fetched and held** -- `intake_fetch.py fetch` gets ONE exact wheel file into `<holding root>/holding/<batch>/`, unchecked. Record: `<file name>.fetch.json` (schema `intake-fetch/1`). Read a batch back with `intake_fetch.py list --batch <id>`.
5. **Checked and released** -- `intake_check.py` runs the eight checks; only it moves a file to `<holding root>/release/<batch>/`. Record: `<file name>.check.json` (`intake-check/1`).
6. **Sent and received** -- `intake_receive.py` on the receiving box installs and imports. Record: `<file name>.receipt.<device>.json` (`intake-receipt/1`).

Holding root: `<workspace drive>/opal-intake/`, outside every git tree. `OPAL_INTAKE_ROOT` overrides it (tests); `OPAL_INTAKE_RECORDS` overrides the records folder.

`intake_fetch.py` against the public index refuses unless `--approved-by <file>` names an existing file containing the exact `name==version`; it makes no request on a refusal. `--index-base` is for a loopback test index. A release's `release_count` counts versions that carry at least one file.
The approval-file line and the signed check-8 file, with what the tools demand of each: `APPROVAL_AND_SIGNED_FILE_DEMANDS.md` (this folder).
