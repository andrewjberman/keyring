# YCharts attended sign-in (option A) -- Andrew's steps, ready whenever you take them

**Why:** the stored YCharts session was evicted at about 00:10Z on 2026-10-03 (row IRPT_BCKEND-S288). Every Analysis run
waits on a fresh sign-in, and only you can answer a CAPTCHA. Packet: `SIGNIN_A/NEVER_WIDEN_SIGNOFF_PACKET_SIGNIN_A_20261002.md`,
section 4, with the one-run VNC password addendum.

**Ready, read at 16:02Z (read-only, no vendor call; `SIGNIN_A/PREFLIGHT_LEG_A_20261003.txt`):**
- Xvnc and vncpasswd are installed, and port 5901 is free.
- The capture library carries attended mode.
- The queue is 0/0 and the provider lease is empty.

On your laptop, the Session Manager plugin and the TigerVNC viewer were read installed on 2026-10-02.

## The steps (about 5 to 15 minutes)

0. **Tell `2.0.0_SA_COO~Y` "option A now"** (in its terminal, or through `0.0.0_AB_MSTR`). It re-checks that the queue is
   empty, opens the ledger and starts the host side, then answers "started". From then the run lasts at most 14 minutes.
1. **Read the one-run password.** In a terminal:
   `aws ssm start-session --target i-0167fd745ad906a66 --region us-east-1`
   then `sudo cat /root/irpt-attended/vnc_password_current` (8 characters). Exit that shell. The file exists only while
   the run is open, and it is deleted at the end.
2. **Open the display tunnel.** In a second terminal, and keep it open:
   `aws ssm start-session --target i-0167fd745ad906a66 --document-name AWS-StartPortForwardingSession --parameters "portNumber=5901,localPortNumber=5901" --region us-east-1`
3. **Watch.** Open the TigerVNC viewer and connect to `localhost:5901` with the password from step 1. A browser signs in
   to YCharts by itself.
   - **If a CAPTCHA shows:** solve it. The run holds up to 10 minutes for you, then continues and saves the session on its own.
   - **If none shows:** there is nothing to do. The run finishes and saves the session.
4. **Close.** When the run ends (the viewer goes blank or disconnects), close the viewer and press Ctrl+C in the tunnel
   terminal.

## What happens after

`2.0.0_SA_COO~Y` reports the outcome (`LEG_A_VERDICT=`) and checks one authenticated YCharts read. It then runs the three
held checks, one at a time with the queue empty:
1. Y-3: a Multi-Comp with an ETF comparison reaches READY.
2. Y-5: Case A with SGOV standing in for TIMXX, then Case D.
3. Y-4: the typo file, where APPL is offered as AAPL; this also records the check gate's time.
