import threading
import time

def download_file(file_name):
    print(f"Start downloading {file_name}")
    time.sleep(2)  # จำลองการโหลดไฟล์
    print(f"Finished downloading {file_name}")

if __name__ == "__main__":
    files = ["file1", "file2", "file3"]

    threads = []

    for file in files:
        t = threading.Thread(target=download_file, args=(file,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All downloads completed.")
