#!/usr/bin/env python3
"""Read-only status check for NexLand on Pterodactyl."""
import json
import os
import sys
import urllib.error
import urllib.request

BASE = "https://control.play2go.cloud"
SERVER = "ef50a4b3"


def main():
    key = os.getenv("PTERODACTYL_API_KEY", "")
    if not key:
        print("ERROR: PTERODACTYL_API_KEY secret is missing.", file=sys.stderr)
        return 1

    url = f"{BASE}/api/client/servers/{SERVER}/resources"
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {key}",
            "Accept": "Application/vnd.pterodactyl.v1+json",
            "User-Agent": "NexLandStatusCheck/1.0",
        },
        method="GET",
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            data = json.load(response)
    except urllib.error.HTTPError as error:
        print(f"API request failed (HTTP {error.code}). Check credentials and permissions.", file=sys.stderr)
        return 1
    except (urllib.error.URLError, TimeoutError, ValueError) as error:
        print(f"API request failed: {type(error).__name__}.", file=sys.stderr)
        return 1

    attrs = data.get("attributes", {})
    resources = attrs.get("resources", {})
    memory = resources.get("memory_bytes")
    disk = resources.get("disk_bytes")
    cpu = resources.get("cpu_absolute")
    print("NexLand / Play2Go (read-only)")
    print(f"State: {attrs.get('current_state', 'unknown')}")
    if cpu is not None:
        print(f"CPU: {float(cpu):.2f}%")
    if memory is not None:
        print(f"Memory used: {int(memory) / (1024**2):.1f} MiB")
    if disk is not None:
        print(f"Disk used: {int(disk) / (1024**3):.2f} GiB")
    print("No commands were sent; no files were modified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
