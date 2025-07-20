import requests

def store_file(file_path):
    try:
        # Step 1: Get server
        server_res = requests.get(
            "https://api.gofile.io/servers",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        print("[+] Server Response:", server_res.text)
        server_res.raise_for_status()
        server_data = server_res.json()
        server = server_data["data"]["servers"][0]["name"]
    except Exception as e:
        print("[!] Failed to get server:", e)
        return

    try:
        # Step 2: Upload file to correct endpoint
        with open(file_path, 'rb') as f:
            upload_res = requests.post(
                f"https://{server}.gofile.io/uploadFile",
                files={"file": f},
                headers={"User-Agent": "Mozilla/5.0"}
            )
        print("[+] Upload Response:", upload_res.text)
        upload_res.raise_for_status()
        upload_data = upload_res.json()
        print("\n✅ File Uploaded Successfully!")
        print("🔗 Download Link:", upload_data["data"]["downloadPage"])
    except Exception as e:
        print("[!] Failed to upload file:", e)

# --- Main ---
if __name__ == "__main__":
    file_name = input("📄 Enter file name to upload: ")
    store_file(file_name)
