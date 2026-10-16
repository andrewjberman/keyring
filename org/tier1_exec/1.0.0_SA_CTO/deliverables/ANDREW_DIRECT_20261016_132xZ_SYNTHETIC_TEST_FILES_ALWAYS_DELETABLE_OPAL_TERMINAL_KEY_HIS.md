# ANDREW-DIRECT 2026-10-16 ~13:2xZ, at the 1.0.0_SA_CTO terminal (laptop): synthetic test files are always deletable; he removes the Opal_Terminal key

He was replying to the cluster `/open-calls` list read at 13:23Z.

## VERBATIM

> "dc59: synthetic files that we need cleared out are always deletable, they can delete those. I will check Opal_Terminal key and get rid of it right now."

## What it settles

1. **`dell2-20261016T105058Z-dc59`: the delete is no longer his act.** The seats delete the synthetic test objects in the
   49financial intake store: the 5 run-3 probe CSVs, the 8 from the R33 sitting, and any written by the re-probe. The standing part
   of his word is "synthetic files that we need cleared out are always deletable, they can delete those". It is relayed as said;
   this record neither widens nor narrows it.
   - It reaches no file holding client data, and no object that is not synthetic.
   - Before deleting, the deleting seat reads each key against its own written-objects list (here `OBJECTS_WRITTEN_FWD1_R3.txt`).
   - The deleting seat names the keys it deleted and reads them back as absent.
   - The never-widen and S3 delete lines in CLAUDE.md are not edited by this record. Making the word law would be a separate law
     edit.
2. **`dell2-20261011T063600Z-e260` is superseded: he removes the Opal_Terminal key himself.** The NFRA_TRNSPT FWD-8 read through
   that key is no longer owed. dell2's CTO re-plans FWD-8's second-reader limb.

## State read before his act (laptop, `.tools/aws`, ~13:2xZ)

| read | value |
|---|---|
| access keys on `Opal_Terminal` | 1 key, created 2026-07-10, `Status: Inactive` |
| that key's last use | never (`ServiceName N/A`) |
| console login profile | none (`NoSuchEntity`) |
| MFA devices | none |
| groups | `AdministratorAccessOpalCapital` |
| inline policies | `OpalSecretsReader`, `ycharts-credentials-read`, `inf-andrew-otp-write`, `IAMUserChangePassword` |

## Routed

- To dell2's `1.0.0_SA_CTO~DELL2`, through `0.0.0_AB_MSTR`: dc59 is a seat delete under this word, then close; e260 closes as
  superseded.

## Addendum (~13:3xZ): the user is deleted

He said, VERBATIM: "I already deleted that user". Read on the laptop: `iam get-user --user-name Opal_Terminal` returns `NoSuchEntity`. As a control, `get-user Andrew_Berman` returns the user, so the read path works.
