# TBH-SSRF

<p align="center">
  <a href="https://github.com/TulungagungBlackHat/TBH-SSRF/actions/workflows/ci.yml"><img src="https://github.com/TulungagungBlackHat/TBH-SSRF/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/license-MIT-red.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/payload-safe-green.svg" alt="Safe payloads">
</p>

SSRF signal detector. Points URL-taking parameters at metadata endpoints and checks for leaked cloud metadata content.

Part of the [Tulungagung Black Hat](https://github.com/TulungagungBlackHat) toolset.

## What It Checks

- URL parameters (`?url=`, `?link=`, `?redirect=` style) that the server fetches server-side
- Response content matching cloud instance metadata (e.g. `meta-data` markers)
- Status changes from the probe

A metadata hit is **High severity** — but confirm with an out-of-band collaborator (Burp Collaborator, interactsh) before reporting. This tool finds the signal; the OOB callback is your proof.

## Install

```bash
git clone https://github.com/TulungagungBlackHat/TBH-SSRF
cd TBH-SSRF
pip install -r requirements.txt
```

## Usage

```
usage: ssrf.py [-h] -u URL [--json JSON]

options:
  -u, --url URL     Target URL whose parameter accepts a URL
  --json JSON       Save result as JSON
```

```bash
python3 ssrf.py -u "https://example.com/fetch?url=https://example.org" --json result.json
```

## Sample Output

```
[*] Testing https://example.com/fetch?url=...
[!] SSRF: metadata endpoint content reflected -> High, confirm with collaborator
[✓] JSON: result.json
```

## Authorized Use Only

Only against scopes you own or are authorized to test. Never point SSRF probes at infrastructure you don't own — cloud metadata on someone else's box is a crime, not a finding. See [SECURITY.md](SECURITY.md).

## Related Tools

- [TBH-LFI](https://github.com/TulungagungBlackHat/TBH-LFI) — file-read sibling bug class
- [TBH-OpenRedirect](https://github.com/TulungagungBlackHat/TBH-OpenRedirect) — often chained with SSRF

## License

[MIT](LICENSE) — Tulungagung Black Hat, East Java, Indonesia. Always Smile :)
