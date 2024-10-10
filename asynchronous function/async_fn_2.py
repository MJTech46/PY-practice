import asyncio

async def download_file(file_name, download_time):
    """Simulates downloading a file asynchronously."""
    print(f"Starting download: {file_name}")
    await asyncio.sleep(download_time)  # Simulate download time
    print(f"Finished download: {file_name} (took {download_time} seconds)")
    return file_name

async def main():
    """Manages the download of multiple files asynchronously."""
    files_to_download = [
        ("file1.txt", 2),
        ("file2.txt", 3),
        ("file3.txt", 1),
    ]

    # Create tasks for all file downloads
    tasks = [download_file(file, time) for file, time in files_to_download]

    # Gather results from all tasks
    downloaded_files = await asyncio.gather(*tasks)
    print(f"Downloaded files: {downloaded_files}")

# Run the main async function
asyncio.run(main())

#           OUTPUT
# Starting download: file1.txt
# Starting download: file2.txt
# Starting download: file3.txt
# Finished download: file3.txt (took 1 seconds)
# Finished download: file1.txt (took 2 seconds)
# Finished download: file2.txt (took 3 seconds)
# Downloaded files: ['file1.txt', 'file2.txt', 'file3.txt']
