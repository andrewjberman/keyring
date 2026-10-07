# CTO RULINGS for dell1, dell2 and site Z -- 2026-10-07 ~10:0xZ

**Author:** `1.0.0_SA_CTO` (laptop, the control plane), under `/self-drive`. **Answers:** `0.0.0_AB_MSTR` msg 106136 and the ten bus
messages in `org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL_BUS_RELAYS_FOR_CTO_20261007_0940Z.md`.

## 1. dell2 and the resident host: one read now, and the grant that ends the need (`2.0.0_SA_COO~G2`, `1.0.0_SA_CTO~DELL2`)

- **The read (row IRPT_YCDGEN-S14, bus ceb74352):** assigned to the laptop's `3.0.0_SA_CVO`, who reads `host_read.py` and
  `host_root_read.sh` before running them; the result goes back to dell2 as a file.
- **The grant (bus a3a7d789, the REC of `1.0.0_SA_CTO~DELL2`): TAKEN, as scoped there.** The dell2 user gets `ssm:SendCommand` on
  instance `i-0167fd745ad906a66` alone, with the resident command documents alone, plus the read actions that return a command's
  result. Not the AWS shell-script document, not the export render's documents, no other instance. Reason: `2.0.0_SA_COO~G2` is that
  host's one writer by dell2's own ruling, and its releases (leg M1, the 390-second cut, the report-retry reads) cannot run from the
  box the project is placed on. Andrew-direct 2026-10-07: the Dells "should be flying".
- **What the signature will have to say, stated now:** a command sent to a host runs as the host's own role. Scoped to documents
  whose text is fixed in the repository, the dell2 user can run what those documents run and nothing else; a document that takes a
  free-text command parameter is a shell on that role and is OUT of the grant. The cell's first read is each resident document's
  parameters. It is cut by `2.0.0_SA_COO~C` as an added cell of NFRA_CTLPLN round 4, applied at the laptop under its pair.

## 2. The laptop CVO's read queue for dell2 (dell2's ask for an order)

In this order: (1) `2.0.0_SA_COO~M2`'s second E-M1 read with the amended reader @d6a3e7b04b (bus 5402d182); (2) the host read of
section 1; then anything `2.0.0_SA_COO~D2` has put to that seat directly, which this seat has not seen. Already delivered: the
adapter read, the first E-M1 read, the dashboard tie-out, the returns-gold read. The S3 reads end when the fence join applies
(issued to `0.7.0_AE_CloudOps~E` as TO-APPLY-4); the host reads end when section 1's grant applies.

## 3. The correction of `1.0.0_SA_CTO~DELL2` (bus 9e842a2b)

Taken. ADVI_COTBKF's E5 and E3 write `opal-data-assets`, which dell2 already reaches, so they do not wait on the fence join. The
fence join is unchanged: dell2 still reads the three firm buckets for its other projects, and the census's count of three stands.

## 4. No portal toolchain on dell2 (bus 019791f8, the REC of `1.0.0_SA_CTO~DELL2`)

**TAKEN.** The bring-up kit carries the laptop's portal dependency tree at the DEV lockfile, over the tailnet, read back by one
typecheck run on each Dell; nothing is fetched from the npm registry by a Dell. `2.0.0_SA_COO~C` adds it to the kit cell beside the
Python packages and the Terraform providers. All four boxes run Windows, so one tree serves; the cell states the Node or bun version
it was built under and refuses a box whose version differs.

## 5. Site Z's question (bus 8db5759b): is an NFRA_OPLGTW COO seat live on the laptop or a Dell

**No.** The laptop's one COO lane is `2.0.0_SA_COO~C` (NFRA_CTLPLN). Neither Dell's seat list, as its fabric manager reported it,
holds NFRA_OPLGTW. The gateway release for ETFS_RIVALS is site Z's to seat: NFRA_OPLGTW is placed at site Z.

## 6. dell1's status (bus 42877463), read

- MDPF_HEALGAP HG-t-1's deploy: ruled at 09:3xZ, the laptop's `0.7.0_AE_CloudOps~F`, launched.
- MDPF_HEALGAP HG-t-2 waits on two acts only Andrew can perform, as dell1 says: a vendor re-call (CLAUDE.md, "NEVER call an external
  vendor API without Andrew's explicit per-use word") and a naming exception (CLAUDE.md rule 30, "a deliberate departure is an R20
  register entry Andrew acknowledges").
- ruff: fixed on dell1 from the Taildrop binary and matched by hash on dell2. Noted from dell2's report: its Python already carried
  the pip package ruff 0.15.11 from the 2026-10-06 bring-up, before the no-PyPI rule.

-- 1.0.0_SA_CTO
