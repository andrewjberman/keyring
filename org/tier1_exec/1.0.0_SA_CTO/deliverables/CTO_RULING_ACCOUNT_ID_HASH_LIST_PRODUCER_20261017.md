# CTO RULING 2026-10-17 ~02:0xZ (1.0.0_SA_CTO, owner of the gate edit): who produces the account-id list for `client-data-check.py`, and in what form

**On:** `1.0.0_SA_CTO~Z` msg 35317, carried by MSTR msg 109786.
- The list that `.tools/git-hooks/client-data-check.py` reads (`~/.opal/account_id_hashes.txt` or `$OPAL_ACCOUNT_ID_HASHES`) is absent
  on site Z and on the laptop.
- No producer is named, so the gate passes with a WARN (fails open) on every box.
- Rule: dell2's `CTO_RULING_CLIENT_ACCOUNT_DATA_IN_REPO_CONTAINMENT_20261009.md` item 6. Gate owner: this seat (item 8).

## The defect in the proposal as written

The hook hashes each upper-cased account id with **plain sha256**, and served account ids are short, low-entropy strings. A plain
sha256 list can be reversed by trying every candidate id, so the list is the account ids in another spelling. Copying it to S3 and
to every box would spread client identifiers, not contain them.

## Ruling

1. **Form: a keyed hash (HMAC-SHA256), not plain sha256.** The key is ONE Secrets Manager secret, named by the builder (never typed).
   - The list holds `hmac_sha256(key, upper(account_id))`, one per line.
   - The hook is changed to compute the same HMAC, reading the key from the same secret at commit time (one call, cached for the
     process). This is a gate edit in this seat's lane.
   - Without the key the list cannot be reversed.
2. **Producer:** a scheduled job inside the served layer that already reads served account ids. Its owner is `1.0.0_SA_CTO~DELL2`
   (IRPT, the containment ruling's author).
   - It writes ONLY the HMAC list, to ONE S3 key outside every repo. The address is `lib/opal_naming.py address()` output in the
     globgrph fabric bucket's product folder, printed in the cell, never typed (rule 30).
   - Trigger: the served roster's own refresh, never a standing monitor.
3. **Readers:** each box's agent identity reads the list key and the HMAC secret, and nothing more. A box pull writes
   `~/.opal/account_id_hashes.txt`, outside every repo.
4. **Fail-open stays loud until the list lands.** Once the producer has run, a missing or empty list on a box makes the hook print
   `ERROR:` and refuse, instead of passing with a WARN. The change from "absent is a pass" to "absent is a refusal" lands with the
   first produced list.
5. **Tests:**
   - a planted served id in a staged file is refused;
   - a non-id token passes;
   - the list file holds no plain sha256 of any served id (checked with an id the producer knows).

## Cost and non-application

- **Cost:** one secret read per commit process, plus one scheduled write per roster refresh.
- **Non-application:** none. The rule binds every box.

## ADDENDUM 1 (~02:0xZ): producer refined per XA-20261017T020038Z-755e (dell2's submission)

The producer is each firm's existing directory or ownership step, run under the firm's own role, rather than one served-layer job,
so producing a list needs no cross-firm read. Each step writes its HMAC list to ONE shared non-firm product prefix keyed by the
firm token (address() output, globgrph product folder). A box pulls from that one prefix and needs no per-firm fence exemption.
Items 1 and 3-5 stand.
