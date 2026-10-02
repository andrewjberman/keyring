# Addendum to the sign-in option A packet -- a one-run VNC password (the CTO half's follow-up, item 1)

**Author:** `2.0.0_SA_COO~Y`, 2026-10-02 ~10:3xZ. **To:** the packet `NEVER_WIDEN_SIGNOFF_PACKET_SIGNIN_A_20261002.md` (blob
`dd879e1014`) and its CTO half `CTO_HALF_YCHARTS_SIGNIN_A_ST13_20261002.md` item 1. The half named this as a follow-up, not a
condition. This change only TIGHTENS leg A: it adds an authentication the signed packet did not have. It touches nothing
served: the change is in the operator script `live_walk/attended_signin_host.sh`, not on the host until a leg-A run sends it.

## What changed in leg A's script

- **The password.** Each run makes ONE 8-character VNC password (`secrets.token_urlsafe`). It is written only to:
  - Xvnc's obfuscated password file, `~ec2-user/.irpt-attended/vnc.passwd` (0600, in a 0700 directory, read by Xvnc
    as the resident's user);
  - `/root/irpt-attended/vnc_password_current` (0600, root).
- **Xvnc** starts with `-SecurityTypes VncAuth -PasswordFile <that file>` instead of `-SecurityTypes None`.
- **It is never printed.** The script prints only the plain file's path. The run's Systems Manager output, which an
  agent reads, never carries the password.
- **Teardown.** Both files are deleted, both on the binding refusal and at teardown, and the script prints how many
  remain (0 expected).
- **Refusal.** The script refuses before any vendor call if `vncpasswd -f` does not produce an 8-byte file.
  `vncpasswd` was read present at `/usr/bin/vncpasswd`, from `tigervnc-server-minimal`, at 10:2xZ.

## Andrew's steps (section 4 step 2, amended)

1. `aws ssm start-session --target i-0167fd745ad906a66 --region us-east-1` (his own shell on the host), then
   `sudo cat /root/irpt-attended/vnc_password_current`. The file exists only while a run is open.
2. `aws ssm start-session --target i-0167fd745ad906a66 --document-name AWS-StartPortForwardingSession --parameters "portNumber=5901,localPortNumber=5901" --region us-east-1`.
3. The TigerVNC viewer on `localhost:5901`, with that password.

## The residual this does not close

Any identity that can open a Systems Manager session on the host as root can read the password file while a run is
open. That set already holds root on the host. The password closes the half's named gap: a process on the laptop that
reaches the open forward without reading the file.

## Not exercised

The script on the host. Any run of it is a vendor sign-in, and no display-only self-test is named by the packet. The
embedded Python compiles and passes lint (F, E9).

-- 2.0.0_SA_COO~Y
