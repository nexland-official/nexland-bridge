# NexLand GitHub Bridge (read-only starter)

This is **not** a persistent ChatGPT MCP connection. It is an on-demand
GitHub Actions check of the NexLand Minecraft server on Play2Go.

## Setup from a phone

1. Create a **private** GitHub repository (suggested name: `nexland-bridge`).
2. Upload the contents of this folder, preserving `.github/workflows/status.yml`.
3. In the repository, open **Settings -> Secrets and variables -> Actions -> New repository secret**.
4. Name it `PTERODACTYL_API_KEY` and paste the **Client API** key from your
   Pterodactyl panel *there only*, never into the code, chat or screenshots.
5. Open **Actions -> NexLand status check -> Run workflow**.
6. Review the job log. It prints state, CPU, RAM and disk, but not the key.

## Security notes

- The script calls only **GET** `/api/client/servers/ef50a4b3/resources`.
- It cannot send console commands, edit files, or restart the server.
- GitHub-hosted runners generally use changing outbound IP addresses.
  If your Pterodactyl Client API key is restricted to a particular IP,
  these runs may fail. **Do not remove IP restrictions just to make it work**;
  use a fixed-egress runner or a trusted server instead.
- GitHub Actions secrets reduce accidental disclosure but an API key still
  holds its underlying Pterodactyl permissions. Keep the repository private
  and restrict who can edit workflows or run code with secrets.
- Do not share API keys or Actions logs that accidentally contain secrets.
- The server identifier is not a credential. The API key is.
- For a persistent ChatGPT MCP bridge, a separate supported host/integration
  and an authenticated, restricted service would still be required.
